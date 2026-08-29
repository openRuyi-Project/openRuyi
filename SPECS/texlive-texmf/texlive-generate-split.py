#!/usr/bin/env python3
"""Generate split RPM file lists for TeX Live texmf data.

This script is deliberately package-specific.  The RPM install layout is fixed
here so texlive-texmf.spec only needs to pass the buildroot and metadata files.

Data flow:
  texlive.tlpdb + texlive-collections.txt + texlive-script-targets.txt
    -> texlive-<collection>.files

How to modify this package (you rarely need to touch this script):
  - Add or remove a subpackage    -> edit texlive-collections.txt
  - Add a /usr/bin command link   -> edit texlive-script-targets.txt
  - Change the install layout     -> edit the path constants below
"""

from __future__ import annotations

import argparse
import os
import re
import stat
import sys
from collections import defaultdict
from pathlib import Path

# RPM installation layout used by this package.
DATADIR = "/usr/share"
BINDIR = "/usr/bin"
SYSCONFDIR = "/etc"
SHAREDSTATEDIR = "/var/lib"
DOCDIR = "/usr/share/doc/texlive"
MANDIR = "/usr/share/man"
INFODIR = "/usr/share/info"

# TeX Live script-link metadata is stored in .ARCH records.  The links are
# noarch, so use one canonical architecture record, as Arch Linux does.
TL_LINK_ARCH = "x86_64-linux"

LANGUAGE_FILES = {
    "dat": "tex/generic/config/language.dat",
    "dat.lua": "tex/generic/config/language.dat.lua",
    "def": "tex/generic/config/language.def",
}

BASE_DIRS = {
    "/", "/usr", "/usr/bin", "/usr/share", "/usr/share/doc",
    "/usr/share/fontconfig", "/etc", "/etc/fonts", "/etc/fonts/conf.d",
    "/var", "/var/lib",
}

# This header is used by fmtutil when generating formats.  It is not listed as
# a normal tlpdb runfile on our split path, so pin it into the basic runtime
# package; fmtutil is happier when it is installed.
FORCE_BASIC_FILES = {
    "/usr/libexec/texlive/rebuild-configs",
    "/usr/share/texmf-dist/web2c/fmtutil-hdr.cnf",
    "/usr/share/texmf-dist/scripts/texlive/mktexlsr",
    "/usr/share/texmf-dist/scripts/texlive/tl-errmess.ps1",
    "/usr/share/texmf-dist/scripts/texlive/tlmgr.pl",
    "/usr/share/texmf-dist/scripts/texlive/tlmgrgui.pl",
    "/usr/share/texmf-dist/scripts/texlive/uninstall-windows.pl",
    "/usr/share/texmf-dist/scripts/texlive/uninstq.ps1",
    "/usr/share/texmf-dist/web2c/updmap-hdr.cfg"
}


def installed(*parts: str) -> str:
    """Join install paths and return an absolute installed path."""
    p = Path(parts[0])
    for part in parts[1:]:
        p /= part
    return "/" + str(p).lstrip("/")


def in_buildroot(buildroot: Path, path: str | Path) -> Path:
    return buildroot / str(path).lstrip("/")


def uncomment(line: str) -> str:
    return line.split("#", 1)[0].strip()


def read_collections(path: Path) -> list[str]:
    """Read whitespace-separated collection names, ignoring comments."""
    names: list[str] = []
    for line in path.read_text(errors="replace").splitlines():
        if text := uncomment(line):
            names.extend(text.split())
    return names


def read_script_targets(path: Path) -> list[tuple[str, str]]:
    """Read upstream-style 'source target' linked-script rules."""
    rules: list[tuple[str, str]] = []
    for lineno, raw in enumerate(path.read_text(errors="replace").splitlines(), 1):
        text = uncomment(raw)
        if not text:
            continue
        fields = text.split()
        if len(fields) != 2 or "/" in fields[1]:
            raise SystemExit(f"{path}:{lineno}: expected 'source command', got {raw!r}")
        rules.append((fields[0], fields[1]))
    return rules


def read_tlpdb(path: Path) -> dict[str, list[str]]:
    """Parse texlive.tlpdb into package records keyed by 'name'."""
    records: dict[str, list[str]] = {}
    record: list[str] = []

    def flush() -> None:
        nonlocal record
        if record:
            for line in record:
                if line.startswith("name "):
                    records[line.split(" ", 1)[1]] = record
                    break
        record = []

    for line in path.read_text(errors="replace").splitlines():
        if line.strip():
            record.append(line)
        else:
            flush()
    flush()
    return records

def read_unpackaged(path: Path | None) -> tuple[set[str], tuple[str, ...]]:
    """Read a manifest of installed paths that are intentionally not packaged.

    A line ending in '/' is a directory prefix that matches every file below
    it (e.g. the whole texmf-dist/source tree); any other line is one absolute
    file path.  Matched files are deleted from the buildroot, not shipped.
    """
    exact: set[str] = set()
    prefixes: list[str] = []
    if path is None:
        return exact, ()
    for lineno, raw in enumerate(path.read_text(errors="replace").splitlines(), 1):
        text = uncomment(raw)
        if not text:
            continue
        if not text.startswith("/"):
            raise SystemExit(f"{path}:{lineno}: expected absolute path, got {raw!r}")
        if text.endswith("/"):
            prefixes.append(text)
        else:
            exact.add(text)
    return exact, tuple(prefixes)

def dependencies(records: dict[str, list[str]], package: str) -> list[str]:
    return [line.split(" ", 1)[1].split()[0]
            for line in records.get(package, []) if line.startswith("depend ")]


def execute_lines(records: dict[str, list[str]], package: str) -> list[str]:
    return [line for line in records.get(package, []) if line.startswith("execute ")]


def runfiles(records: dict[str, list[str]], package: str) -> list[str]:
    """Return non-doc texmf-dist runfiles from one tlpdb record."""
    files: list[str] = []
    in_runfiles = False
    for line in records.get(package, []):
        if line.startswith("runfiles"):
            in_runfiles = True
            continue
        if in_runfiles and line and line[0].isalpha():
            break
        if in_runfiles:
            path = line.strip()
            if path.startswith("texmf-dist/") and not path.startswith("texmf-dist/doc/"):
                files.append(path)
    return files


def ignored_dep(package: str) -> bool:
    """Skip collection deps and architecture-specific binary deps."""
    return (
        package.startswith("collection-") or
        package.endswith((".ARCH", "." + TL_LINK_ARCH)) or
        package in {"texlive.infra", "texlive.infra." + TL_LINK_ARCH}
    )


def base_dirs() -> set[str]:
    """Directories that should not be emitted as explicit %dir entries."""
    dirs = set(BASE_DIRS)
    for raw in (DATADIR, BINDIR, SYSCONFDIR, SHAREDSTATEDIR, DOCDIR, MANDIR, INFODIR):
        p = Path(raw)
        while str(p) not in {".", "/"}:
            dirs.add("/" + str(p).lstrip("/"))
            p = p.parent
    return dirs


class SplitState:
    """All generated file ownership state."""

    def __init__(self, collections: list[str]) -> None:
        self.files = {c: set() for c in collections}
        self.dirs = {c: set() for c in collections}
        self.fragments = {c: {"fmts": [], "maps": [], "dat": [], "dat.lua": [], "def": []} for c in collections}
        self.owner: dict[str, str] = {}       # installed path -> collection
        self.cmd_owner: dict[str, str] = {}   # /usr/bin command -> collection
        self.bad_script_targets: list[tuple[str, str]] = []
        self.tlpkgs = {c: [] for c in collections}

def add_parent_dirs(state: SplitState, coll: str, buildroot: Path, path: Path, skip_dirs: set[str]) -> None:
    path = path.parent
    while path != buildroot:
        rel = "/" + str(path.relative_to(buildroot))
        if rel not in skip_dirs:
            state.dirs[coll].add(rel)
        path = path.parent


def add_path(state: SplitState, coll: str, buildroot: Path, path: str, skip_dirs: set[str]) -> None:
    """Add an installed file, symlink or directory tree to a collection."""
    root = in_buildroot(buildroot, path)
    if not root.exists() and not root.is_symlink():
        return

    def add_one(p: Path) -> None:
        rel = "/" + str(p.relative_to(buildroot))
        if p.is_dir() and not p.is_symlink():
            if rel not in skip_dirs:
                state.dirs[coll].add(rel)
        else:
            state.files[coll].add(rel)
            state.owner.setdefault(rel, coll)
            add_parent_dirs(state, coll, buildroot, p, skip_dirs)

    if root.is_dir() and not root.is_symlink():
        add_one(root)
        for child in root.rglob("*"):
            add_one(child)
    else:
        add_one(root)


def build_collection_closures(records: dict[str, list[str]], collections: list[str]):
    """Decide which collection owns each TL package, expanding dependencies.

    Each TeX Live package is owned by exactly one collection: the first one
    whose dependency closure reaches it.  A package reached from another
    collection stays with its original owner, so files are never duplicated.
    """
    direct = {c: [] for c in collections}
    for coll in collections:
        for dep in dependencies(records, "collection-" + coll):
            if not ignored_dep(dep):
                direct[coll].append(dep)

    package_owner: dict[str, str] = {}
    duplicate_direct: list[tuple[str, str, str]] = []
    for coll in collections:
        for package in direct[coll]:
            old = package_owner.setdefault(package, coll)
            if old != coll:
                duplicate_direct.append((package, old, coll))

    closure = {c: set() for c in collections}
    missing: set[str] = set()
    sys.setrecursionlimit(max(10000, sys.getrecursionlimit()))

    def visit(package: str, wanted: str) -> None:
        if ignored_dep(package):
            return
        if package not in records:
            missing.add(package)
            return
        owner = package_owner.setdefault(package, wanted)
        if owner != wanted:
            return
        if package in closure[owner]:
            return
        closure[owner].add(package)
        for dep in dependencies(records, package):
            if not ignored_dep(dep):
                visit(dep, owner)

    for coll in collections:
        for package in direct[coll]:
            visit(package, coll)
    return closure, duplicate_direct, missing


def load_config_texts(texmf: Path):
    """Load central TeX Live config files used to make per-package fragments."""

    def text(rel: str) -> str:
        path = texmf / rel
        return path.read_text(errors="replace") if path.exists() else ""

    return (
        text("web2c/fmtutil.cnf"),
        text("web2c/updmap.cfg"),
        {kind: text(rel) for kind, rel in LANGUAGE_FILES.items()},
    )


def fmt_lines(fmtutil: str, execute: str) -> list[str]:
    name = re.search(r"name=([^\s]+)", execute)
    engine = re.search(r"engine=([^\s]+)", execute)
    if not (name and engine):
        return []
    wanted = (name.group(1), engine.group(1))
    out: list[str] = []
    for line in fmtutil.splitlines():
        fields = line.strip().split()
        if len(fields) >= 2 and not line.strip().startswith(("#", "%")) and (fields[0], fields[1]) == wanted:
            out.append(line)
    return out


def map_lines(updmap: str, execute: str) -> list[str]:
    fields = execute.split()
    if len(fields) < 3:
        return []
    wanted = fields[2]
    out: list[str] = []
    for line in updmap.splitlines():
        m = re.match(r"^(Map|MixedMap|KanjiMap)\s+(\S+)(\s|$)", line.strip())
        if m and not line.strip().startswith(("#", "%")) and m.group(2) == wanted:
            out.append(line)
    return out


def language_lines(language_texts: dict[str, str], package: str) -> dict[str, list[str]]:
    """Extract language.dat/lua/def snippets marked as coming from package."""
    out = {"dat": [], "dat.lua": [], "def": []}
    marker = f"from {package}:"
    for kind, text in language_texts.items():
        if marker not in text:
            continue
        for line in text.split(marker, 1)[1].splitlines()[1:]:
            if kind in {"dat", "def"} and line.startswith("%"):
                break
            if kind == "dat.lua" and (line.startswith("--") or line.startswith("}")):
                break
            out[kind].append(line)
    return out


def assign_tlpdb_content(state: SplitState, buildroot: Path, texmf_dist: Path, collections, records, closure, skip_dirs) -> None:
    fmtutil, updmap, languages = load_config_texts(texmf_dist)
    for coll in collections:
        for package in sorted(closure[coll]):
            state.tlpkgs[coll].append(package)
            for runfile in runfiles(records, package):
                add_path(state, coll, buildroot, installed(DATADIR, runfile), skip_dirs)
            for execute in execute_lines(records, package):
                if "AddFormat" in execute:
                    state.fragments[coll]["fmts"].extend(fmt_lines(fmtutil, execute))
                elif re.search(r"add(Kanji|Mixed)?Map", execute):
                    state.fragments[coll]["maps"].extend(map_lines(updmap, execute))
                elif "AddHyphen" in execute:
                    for kind, lines in language_lines(languages, package).items():
                        state.fragments[coll][kind].extend(lines)


def add_basic_roots(state: SplitState, buildroot: Path, skip_dirs: set[str]) -> None:
    """Add runtime roots that are not cleanly represented by tlpdb runfiles."""
    roots = [
        "/usr/share/fontconfig/conf.avail/09-texlive-fonts.conf",
        "/etc/fonts/conf.d/09-texlive-fonts.conf",
        "/etc/texmf",
        "/usr/share/tlpkg",
        "/var/lib/texmf",
    ]
    for path in roots + sorted(FORCE_BASIC_FILES):
        add_path(state, "basic", buildroot, path, skip_dirs)


def remove_empty_dirs(root: Path) -> None:
    """Remove directories left empty by deletion, deepest first; keep root."""
    for path in sorted(root.rglob("*"), reverse=True):
        if path.is_dir() and not path.is_symlink():
            try:
                path.rmdir()  # succeeds only when the directory is empty
            except OSError:
                pass


def assign_unowned_texmf(state: SplitState, buildroot: Path, texmf_dist: Path,
                         texmf_installed: str, skip_dirs: set[str],
                         unpackaged_exact: set[str],
                         unpackaged_prefixes: tuple[str, ...]) -> list[str]:
    """Deal with texmf-dist files that no collection owns.

    Files listed in the unpackaged manifest are deleted from the buildroot, so
    rpm does not treat them as installed-but-unpackaged.  Anything else is a
    real gap in the split: assign it to texlive-basic so the build still
    succeeds, and return it so the caller can report (or fail under strict).
    """
    doc_root = texmf_installed + "/doc"
    unexpected: list[str] = []
    to_delete: list[Path] = []
    if not texmf_dist.exists():
        return unexpected

    for path in sorted(texmf_dist.rglob("*")):
        if path.is_dir() and not path.is_symlink():
            continue
        rel = "/" + str(path.relative_to(buildroot))
        if rel == doc_root or rel.startswith(doc_root + "/"):
            continue
        if rel in state.owner:
            continue
        if rel in unpackaged_exact or rel.startswith(unpackaged_prefixes):
            to_delete.append(path)
        else:
            unexpected.append(rel)
            add_path(state, "basic", buildroot, rel, skip_dirs)

    for path in to_delete:
        path.unlink()
    remove_empty_dirs(texmf_dist)
    return unexpected


def create_link(link: Path, target: str) -> bool:
    """Create a symlink, refusing to overwrite real files or binaries."""
    if link.exists() and not link.is_symlink():
        return False
    if link.exists() or link.is_symlink():
        link.unlink()
    link.parent.mkdir(parents=True, exist_ok=True)
    os.symlink(target, link)
    return True


def mark_executable(path: Path) -> None:
    if path.exists() and path.is_file():
        try:
            path.chmod(path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        except OSError:
            pass


def generate_script_links(state: SplitState, buildroot: Path, rules: list[tuple[str, str]]) -> None:
    """Create /usr/bin links from explicit script-target rules.

    Do not scan texmf-dist/scripts by basename.  Only rules listed in the
    targets file create commands, which avoids conflicts with engine binaries.
    """
    bindir = in_buildroot(buildroot, BINDIR)
    scripts = [(s, t) for s, t in rules if s.startswith("texmf-dist/scripts/")]
    aliases = [(s, t) for s, t in rules if not s.startswith("texmf-dist/scripts/")]

    for source, command in scripts:
        source_installed = installed(DATADIR, source)
        source_path = in_buildroot(buildroot, source_installed)
        coll = state.owner.get(source_installed)
        if coll is None or not (source_path.exists() or source_path.is_symlink()):
            state.bad_script_targets.append((source, command))
            continue

        link = bindir / command
        if not create_link(link, os.path.relpath(source_path, link.parent)):
            state.bad_script_targets.append((source, command))
            continue

        mark_executable(source_path)
        link_installed = "/" + str(link.relative_to(buildroot))
        state.files[coll].add(link_installed)
        state.owner.setdefault(link_installed, coll)
        state.cmd_owner[command] = coll

    # Aliases may chain: fmtutil -> mktexfmt, mktexlsr -> texhash, etc.
    pending = aliases[:]
    while pending:
        again: list[tuple[str, str]] = []
        changed = False
        for source_command, alias_command in pending:
            coll = state.cmd_owner.get(source_command)
            if coll is None:
                again.append((source_command, alias_command))
                continue
            link = bindir / alias_command
            if not create_link(link, source_command):
                state.bad_script_targets.append((source_command, alias_command))
                continue
            link_installed = "/" + str(link.relative_to(buildroot))
            state.files[coll].add(link_installed)
            state.owner.setdefault(link_installed, coll)
            state.cmd_owner[alias_command] = coll
            changed = True
        if not changed:
            state.bad_script_targets.extend(again)
            break
        pending = again


def write_unique(path: Path, lines) -> None:
    seen: set[str] = set()
    with path.open("w") as out:
        for line in lines:
            if line not in seen:
                out.write(line + "\n")
                seen.add(line)


def file_entry(buildroot: Path, path: str) -> str:
    real = in_buildroot(buildroot, path)
    if path.startswith("/etc/texmf/") and real.exists() and real.is_file() and not real.is_symlink():
        return f"%config(noreplace) {path}"
    return path


def write_fragments(state: SplitState, buildroot: Path, collections: list[str]) -> None:
    root = in_buildroot(buildroot, "/var/lib/texmf/arch/installedpkgs")
    root.mkdir(parents=True, exist_ok=True)
    for coll in collections:
        tlpkg_path = root / f"{coll}.tlpkgs"
        write_unique(tlpkg_path, sorted(state.tlpkgs[coll]))
        state.files[coll].add("/" + str(tlpkg_path.relative_to(buildroot)))
        for suffix, lines in state.fragments[coll].items():
            if lines:
                path = root / f"{coll}.{suffix}"
                write_unique(path, lines)
                state.files[coll].add("/" + str(path.relative_to(buildroot)))


def write_collection_lists(state: SplitState, buildroot: Path, outdir: Path, collections: list[str]) -> None:
    for coll in collections:
        lines = [f"%dir {d}" for d in sorted(state.dirs[coll])]
        lines.extend(file_entry(buildroot, p) for p in sorted(state.files[coll]))
        write_unique(outdir / f"texlive-{coll}.files", lines)


def write_doc_list(buildroot: Path, outdir: Path, texmf_dist: Path) -> None:
    lines: list[str] = []
    compressed_roots = {in_buildroot(buildroot, MANDIR), in_buildroot(buildroot, INFODIR)}
    for root in [in_buildroot(buildroot, DOCDIR), *compressed_roots]:
        if not root.exists():
            continue
        for path in sorted(root.rglob("*")):
            rel = "/" + str(path.relative_to(buildroot))
            if path.is_dir() and not path.is_symlink():
                lines.append(f"%dir {rel}")
            elif any(path.is_relative_to(r) for r in compressed_roots):
                lines.append(rel + "*")
            else:
                lines.append(rel)
    doc_link = texmf_dist / "doc"
    if doc_link.exists() or doc_link.is_symlink():
        lines.append("/" + str(doc_link.relative_to(buildroot)))
    write_unique(outdir / "texlive-doc.files", lines)


def print_warnings(duplicate_direct, missing, state: SplitState) -> None:
    """Print build-time warnings about anything that needs attention."""
    if duplicate_direct:
        print("Duplicate direct TeX Live package ownership detected:")
        for package, old, new in duplicate_direct[:100]:
            print(f"  {package}: {old}, also {new}")
    if missing:
        print("Missing tlpdb records for dependencies:")
        for package in sorted(missing)[:100]:
            print(f"  {package}")
    if state.bad_script_targets:
        print("Unresolved script targets:")
        for source, command in state.bad_script_targets[:100]:
            print(f"  {source} -> {command}")


def fallback_status(unowned: list[str], strict: bool) -> int:
    print(f"TeX Live split: {len(unowned)} non-doc texmf-dist files assigned by fallback to texlive-basic")
    if not unowned:
        return 0
    buckets = defaultdict(int)
    for path in unowned:
        parts = path.split("/")
        buckets["/".join(parts[:5]) if len(parts) > 4 else path] += 1
    print("Top fallback buckets:")
    for bucket, count in sorted(buckets.items(), key=lambda item: (-item[1], item[0]))[:30]:
        print(f"  {count:6d}  {bucket}")
    if strict:
        print("Strict split mode is enabled; failing due to fallback-assigned files.", file=sys.stderr)
        return 1
    return 0


def generate(args: argparse.Namespace) -> int:
    buildroot = Path(args.buildroot).resolve()
    outdir = Path(args.outdir).resolve()
    outdir.mkdir(parents=True, exist_ok=True)

    tlpdb_path = Path(args.tlpdb)
    texmf_dist = Path(args.texmf_dist).resolve()
    texmf_installed = "/" + str(texmf_dist.relative_to(buildroot))

    collections = read_collections(Path(args.collections))
    script_targets = read_script_targets(Path(args.script_targets))
    records = read_tlpdb(tlpdb_path)
    state = SplitState(collections)
    skip_dirs = base_dirs()

    closure, duplicate_direct, missing = build_collection_closures(records, collections)
    assign_tlpdb_content(state, buildroot, texmf_dist, collections, records, closure, skip_dirs)
    add_basic_roots(state, buildroot, skip_dirs)
    unpackaged_exact, unpackaged_prefixes = read_unpackaged(
        Path(args.unpackaged_files) if args.unpackaged_files else None)
    unexpected = assign_unowned_texmf(state, buildroot, texmf_dist, texmf_installed,
                                      skip_dirs, unpackaged_exact, unpackaged_prefixes)
    generate_script_links(state, buildroot, script_targets)
    write_fragments(state, buildroot, collections)
    write_collection_lists(state, buildroot, outdir, collections)
    write_doc_list(buildroot, outdir, texmf_dist)
    # If you ever need to debug which files were assigned to fallback, uncomment the next line.
    # (outdir / "texlive-fallback.txt").write_text("".join(f"{p}\n" for p in sorted(unexpected)))
    print_warnings(duplicate_direct, missing, state)

    # Keep every %files -f input present even when a collection is empty.
    for coll in collections:
        (outdir / f"texlive-{coll}.files").touch(exist_ok=True)
    return fallback_status(unexpected, args.strict_split)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--buildroot", required=True, help="RPM buildroot")
    parser.add_argument("--tlpdb", required=True, help="path to texlive.tlpdb under the buildroot")
    parser.add_argument("--texmf-dist", required=True, help="path to texmf-dist under the buildroot")
    parser.add_argument("--collections", required=True, help="collection list file")
    parser.add_argument("--script-targets", required=True, help="linked-script target rules")
    parser.add_argument("--unpackaged-files", help="manifest of texmf-dist files intentionally not packaged")
    parser.add_argument("--outdir", required=True, help="directory for generated file lists")
    parser.add_argument("--strict-split", action="store_true", help="fail if fallback file ownership is used")
    return parser.parse_args(argv)


if __name__ == "__main__":
    raise SystemExit(generate(parse_args(sys.argv[1:])))
