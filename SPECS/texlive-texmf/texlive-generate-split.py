#!/usr/bin/env python3
"""Generate TeX Live collection RPM file lists.

This helper is intentionally independent from rpm macro expansion.  Pass all
paths and policy inputs on the command line from texlive-texmf.spec.
"""

from __future__ import annotations

import argparse
import os
import re
import stat
import sys
from collections import defaultdict
from pathlib import Path
from typing import DefaultDict, Iterable

SCRIPT_SUFFIXES = (".pl", ".py", ".rb", ".tcl", ".lua", ".texlua", ".sh")


def read_lines(path: Path) -> list[str]:
    """Read a text file as replacement-decoded lines without line endings."""
    return path.read_text(errors="replace").splitlines()


def install_path(prefix: str | Path, *parts: str) -> str:
    """Return an absolute installed path such as /usr/share/foo."""
    p = Path(str(prefix))
    for part in parts:
        p = p / part
    return "/" + str(p).lstrip("/")


def buildroot_path(buildroot: Path, installed_path: str | Path) -> Path:
    """Map an installed absolute path back under the RPM buildroot."""
    return buildroot / str(installed_path).lstrip("/")


def parse_name_list(path: Path) -> list[str]:
    """Parse a whitespace-separated list file with shell-style comments."""
    result: list[str] = []
    for raw in read_lines(path):
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        result.extend(line.split())
    return result


def parse_aliases(path: Path) -> dict[str, str]:
    """Parse script alias mappings as 'alias primary' pairs."""
    aliases: dict[str, str] = {}
    for lineno, raw in enumerate(read_lines(path), 1):
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) != 2:
            raise SystemExit(f"{path}:{lineno}: expected 'alias primary', got: {raw!r}")
        aliases[parts[0]] = parts[1]
    return aliases


def parse_tlpdb(path: Path) -> dict[str, list[str]]:
    """Parse tlpdb package records keyed by package name."""
    records: dict[str, list[str]] = {}
    current: list[str] = []

    def flush() -> None:
        """Store the current tlpdb record, if it has a package name."""
        nonlocal current
        if not current:
            return
        name = next((line.split(" ", 1)[1] for line in current if line.startswith("name ")), None)
        if name:
            records[name] = current
        current = []

    for line in read_lines(path):
        if line.strip() == "":
            flush()
        else:
            current.append(line)
    flush()
    return records


def record_depends(records: dict[str, list[str]], name: str) -> list[str]:
    """Return direct dependency names from one tlpdb record."""
    deps: list[str] = []
    for line in records.get(name, []):
        if line.startswith("depend "):
            dep = line.split(" ", 1)[1].strip().split()[0]
            deps.append(dep)
    return deps


def record_runfiles(records: dict[str, list[str]], name: str) -> list[str]:
    """Return non-document texmf-dist runfiles listed by a tlpdb record."""
    result: list[str] = []
    in_run = False
    for line in records.get(name, []):
        if line.startswith("runfiles"):
            in_run = True
            continue
        if in_run and re.match(r"^[a-z]", line):
            break
        if in_run:
            p = line.strip()
            if p.startswith("texmf-dist/") and not p.startswith("texmf-dist/doc/"):
                result.append(p)
    return result


def record_executes(records: dict[str, list[str]], name: str) -> list[str]:
    """Return execute directives from one tlpdb record."""
    return [line for line in records.get(name, []) if line.startswith("execute ")]


def skip_pkg_dependency(dep: str, tl_arch: str) -> bool:
    """Decide whether a tlpdb dependency is handled outside collection splits."""
    if dep.startswith("collection-"):
        return True
    if dep.endswith(".ARCH") or dep.endswith("." + tl_arch):
        return True
    if dep in ("texlive.infra", "texlive.infra." + tl_arch):
        return True
    return False


def add_parent_dirs(
    package_dirs: set[str], buildroot: Path, installed_file: Path, standard_dirs: set[str]
) -> None:
    """Record non-standard parent directories needed to own an installed file."""
    parent = installed_file.parent
    while parent != buildroot:
        rel = "/" + str(parent.relative_to(buildroot))
        if rel not in standard_dirs:
            package_dirs.add(rel)
        parent = parent.parent


def add_installed_path(
    coll: str,
    installed_path: str,
    buildroot: Path,
    package_files: dict[str, set[str]],
    package_dirs: dict[str, set[str]],
    standard_dirs: set[str],
) -> None:
    """Add an installed file or directory tree to one collection file list."""
    abs_path = buildroot_path(buildroot, installed_path)
    if not abs_path.exists() and not abs_path.is_symlink():
        return

    if abs_path.is_dir() and not abs_path.is_symlink():
        root_rel = "/" + str(abs_path.relative_to(buildroot))
        if root_rel not in standard_dirs:
            package_dirs[coll].add(root_rel)
        for child in abs_path.rglob("*"):
            rel = "/" + str(child.relative_to(buildroot))
            if child.is_dir() and not child.is_symlink():
                if rel not in standard_dirs:
                    package_dirs[coll].add(rel)
            elif child.exists() or child.is_symlink():
                package_files[coll].add(rel)
                add_parent_dirs(package_dirs[coll], buildroot, child, standard_dirs)
    else:
        package_files[coll].add("/" + str(abs_path.relative_to(buildroot)))
        add_parent_dirs(package_dirs[coll], buildroot, abs_path, standard_dirs)


def make_standard_dirs(args: argparse.Namespace) -> set[str]:
    """Build the directory set already owned by base packages or common macros."""
    dirs = {
        "/",
        "/usr",
        "/usr/bin",
        "/usr/share",
        "/usr/share/doc",
        "/usr/share/fontconfig",
        "/etc",
        "/etc/fonts",
        "/etc/fonts/conf.d",
        "/var",
        "/var/lib",
    }
    for raw in (args.datadir, args.bindir, args.sharedstatedir, args.sysconfdir, args.mandir, args.infodir):
        p = Path(raw)
        while str(p) not in (".", "/"):
            dirs.add("/" + str(p).lstrip("/"))
            p = p.parent
    doc = Path(args.docdir)
    while str(doc) not in (".", "/"):
        dirs.add("/" + str(doc).lstrip("/"))
        doc = doc.parent
    return dirs


def load_script_index(buildroot: Path, texmf_dist: Path) -> tuple[dict[str, str], dict[str, str]]:
    """Index TeX Live scripts by command name and collect their shebangs."""
    script_index: dict[str, str] = {}
    script_shebangs: dict[str, str] = {}
    scripts_root = texmf_dist / "scripts"
    if not scripts_root.exists():
        return script_index, script_shebangs

    for path in scripts_root.rglob("*"):
        if not (path.is_file() or path.is_symlink()):
            continue
        rel = "/" + str(path.relative_to(buildroot))
        base = path.name
        script_index.setdefault(base, rel)
        for suffix in SCRIPT_SUFFIXES:
            if base.endswith(suffix):
                script_index.setdefault(base[: -len(suffix)], rel)
        if path.is_file():
            try:
                first = path.open("rb").readline(256)
            except OSError:
                continue
            if first.startswith(b"#!"):
                script_shebangs[rel] = first.decode("utf-8", "replace").strip()
    return script_index, script_shebangs


def extract_format_fragment(fmtutil_text: str, execute_line: str) -> list[str]:
    """Extract fmtutil.cnf lines matching an AddFormat execute directive."""
    m_name = re.search(r"name=([^\s]+)", execute_line)
    m_engine = re.search(r"engine=([^\s]+)", execute_line)
    if not (m_name and m_engine):
        return []
    wanted_name = m_name.group(1)
    wanted_engine = m_engine.group(1)
    out: list[str] = []
    for line in fmtutil_text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("%"):
            continue
        parts = stripped.split()
        if len(parts) >= 2 and parts[0] == wanted_name and parts[1] == wanted_engine:
            out.append(line)
    return out


def extract_map_fragment(updmap_text: str, execute_line: str) -> list[str]:
    """Extract updmap.cfg lines matching an addMap-like execute directive."""
    parts = execute_line.split()
    if len(parts) < 3:
        return []
    mapname = parts[2]
    out: list[str] = []
    for line in updmap_text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("%"):
            continue
        m = re.match(r"^(Map|MixedMap|KanjiMap)\s+(\S+)(\s|$)", stripped)
        if m and m.group(2) == mapname:
            out.append(line)
    return out


def extract_language_fragment(language_texts: dict[str, str], pkg: str) -> dict[str, list[str]]:
    """Extract hyphenation language fragments contributed by one package."""
    result: dict[str, list[str]] = {"dat": [], "dat.lua": [], "def": []}
    for ext, text in language_texts.items():
        marker = f"from {pkg}:"
        if marker not in text:
            continue
        after = text.split(marker, 1)[1]
        lines: list[str] = []
        for line in after.splitlines()[1:]:
            if ext in ("dat", "def") and line.startswith("%"):
                break
            if ext == "dat.lua" and (line.startswith("--") or line.startswith("}")):
                break
            lines.append(line)
        result[ext].extend(lines)
    return result


def chmod_script_if_needed(buildroot: Path, target: str) -> None:
    """Make a script target executable before linking it into bindir."""
    target_path = buildroot_path(buildroot, target)
    if target_path.exists() and target_path.is_file():
        try:
            mode = target_path.stat().st_mode
            target_path.chmod(mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        except OSError:
            pass


def filelist_entry(buildroot: Path, path: str) -> str:
    """Render one RPM file-list entry, marking texmf config files specially."""
    abs_path = buildroot_path(buildroot, path)
    if path.startswith("/etc/texmf/") and abs_path.exists() and abs_path.is_file() and not abs_path.is_symlink():
        return f"%config(noreplace) {path}"
    return path


def write_unique_lines(path: Path, lines: Iterable[str]) -> None:
    """Write lines once each while preserving their first-seen order."""
    seen: set[str] = set()
    with path.open("w") as fh:
        for line in lines:
            if line not in seen:
                fh.write(line + "\n")
                seen.add(line)


def generate(args: argparse.Namespace) -> int:
    """Generate collection file lists, reports, symlinks, and config fragments."""
    buildroot = Path(args.buildroot).resolve()
    tlpdb = Path(args.tlpdb).resolve()
    texmf_dist = Path(args.texmf_dist).resolve()
    outdir = Path(args.outdir).resolve()
    outdir.mkdir(parents=True, exist_ok=True)

    collections = parse_name_list(Path(args.collections))
    aliases = parse_aliases(Path(args.script_aliases))
    records = parse_tlpdb(tlpdb)
    standard_dirs = make_standard_dirs(args)

    direct_pkgs: dict[str, list[str]] = {coll: [] for coll in collections}
    collection_deps: dict[str, set[str]] = {coll: set() for coll in collections}
    for coll in collections:
        for dep in record_depends(records, f"collection-{coll}"):
            if dep.startswith("collection-"):
                dep_coll = dep.replace("collection-", "", 1)
                if dep_coll in direct_pkgs and dep_coll != coll:
                    collection_deps[coll].add(dep_coll)
            elif not skip_pkg_dependency(dep, args.tl_link_arch):
                direct_pkgs[coll].append(dep)

    pkg_owner: dict[str, str] = {}
    duplicate_direct: list[tuple[str, str, str]] = []
    for coll in collections:
        for pkg in direct_pkgs[coll]:
            old = pkg_owner.setdefault(pkg, coll)
            if old != coll:
                duplicate_direct.append((pkg, old, coll))

    closure_pkgs: dict[str, set[str]] = {coll: set() for coll in collections}
    cross_collection_pkg_deps: DefaultDict[str, set[str]] = defaultdict(set)
    missing_records: set[str] = set()

    sys.setrecursionlimit(max(10000, sys.getrecursionlimit()))

    def assign_pkg(pkg: str, preferred_coll: str) -> None:
        """Assign a package and its dependencies to the owning collection."""
        if skip_pkg_dependency(pkg, args.tl_link_arch):
            return
        if pkg not in records:
            missing_records.add(pkg)
            return
        owner = pkg_owner.setdefault(pkg, preferred_coll)
        if owner != preferred_coll:
            cross_collection_pkg_deps[preferred_coll].add(owner)
            return
        if pkg in closure_pkgs[owner]:
            return
        closure_pkgs[owner].add(pkg)
        for dep in record_depends(records, pkg):
            if dep.startswith("collection-"):
                dep_coll = dep.replace("collection-", "", 1)
                if dep_coll in direct_pkgs and dep_coll != owner:
                    collection_deps[owner].add(dep_coll)
                continue
            if skip_pkg_dependency(dep, args.tl_link_arch):
                continue
            assign_pkg(dep, owner)

    for coll in collections:
        for pkg in direct_pkgs[coll]:
            assign_pkg(pkg, coll)

    script_index, script_shebangs = load_script_index(buildroot, texmf_dist)

    package_files: dict[str, set[str]] = {coll: set() for coll in collections}
    package_dirs: dict[str, set[str]] = {coll: set() for coll in collections}
    package_bin: dict[str, set[str]] = {coll: set() for coll in collections}
    script_interpreters: dict[str, set[str]] = {coll: set() for coll in collections}
    fragments: dict[str, dict[str, list[str]]] = {
        coll: {"fmts": [], "maps": [], "dat": [], "dat.lua": [], "def": []} for coll in collections
    }

    fmtutil_path = texmf_dist / "web2c" / "fmtutil.cnf"
    updmap_path = texmf_dist / "web2c" / "updmap.cfg"
    fmtutil_text = fmtutil_path.read_text(errors="replace") if fmtutil_path.exists() else ""
    updmap_text = updmap_path.read_text(errors="replace") if updmap_path.exists() else ""
    language_texts: dict[str, str] = {}
    for ext, rel in {
        "dat": "tex/generic/config/language.dat",
        "dat.lua": "tex/generic/config/language.dat.lua",
        "def": "tex/generic/config/language.def",
    }.items():
        p = texmf_dist / rel
        language_texts[ext] = p.read_text(errors="replace") if p.exists() else ""

    for coll in collections:
        for pkg in sorted(closure_pkgs[coll]):
            for rel in record_runfiles(records, pkg):
                # tlpdb runfiles are relative to TEXMFROOT; installed data is
                # under the installed TeX Live data directory.
                add_installed_path(
                    coll,
                    install_path(args.datadir, rel),
                    buildroot,
                    package_files,
                    package_dirs,
                    standard_dirs,
                )
            for execute in record_executes(records, pkg):
                if "AddFormat" in execute:
                    fragments[coll]["fmts"].extend(extract_format_fragment(fmtutil_text, execute))
                elif re.search(r"add(Kanji|Mixed)?Map", execute):
                    fragments[coll]["maps"].extend(extract_map_fragment(updmap_text, execute))
                elif "AddHyphen" in execute:
                    lang_fragments = extract_language_fragment(language_texts, pkg)
                    for ext, lines in lang_fragments.items():
                        fragments[coll][ext].extend(lines)

            binrec = f"{pkg}.{args.tl_link_arch}"
            for line in records.get(binrec, []):
                prefix = f"bin/{args.tl_link_arch}/"
                if not line.startswith(prefix):
                    continue
                cmd = line[len(prefix) :].strip()
                target = script_index.get(cmd)
                if not target:
                    continue
                chmod_script_if_needed(buildroot, target)
                shebang = script_shebangs.get(target)
                if shebang:
                    script_interpreters[coll].add(shebang)
                out = buildroot_path(buildroot, install_path(args.bindir, cmd))
                out.parent.mkdir(parents=True, exist_ok=True)
                try:
                    out.unlink()
                except FileNotFoundError:
                    pass
                os.symlink(target, out)
                package_bin[coll].add("/" + str(out.relative_to(buildroot)))

    for coll in collections:
        owned_basenames = {Path(p).name for p in package_bin[coll]}
        for alias, primary in aliases.items():
            if primary not in owned_basenames:
                continue
            out = buildroot_path(buildroot, install_path(args.bindir, alias))
            try:
                out.unlink()
            except FileNotFoundError:
                pass
            os.symlink(primary, out)
            package_bin[coll].add("/" + str(out.relative_to(buildroot)))

    basic_extra = [
        install_path(args.datadir, "fontconfig/conf.avail/09-texlive-fonts.conf"),
        install_path(args.sysconfdir, "fonts/conf.d/09-texlive-fonts.conf"),
        install_path(args.sysconfdir, "texmf"),
        install_path(args.datadir, "tlpkg"),
        install_path(args.sharedstatedir, "texmf"),
    ]
    for rel in basic_extra:
        add_installed_path("basic", rel, buildroot, package_files, package_dirs, standard_dirs)

    assigned: set[str] = set()
    for coll in collections:
        assigned |= package_files[coll]

    unassigned: list[str] = []
    texmf_doc_prefix = install_path(args.datadir, "texmf-dist/doc")
    if texmf_dist.exists():
        for path in texmf_dist.rglob("*"):
            if path.is_dir() and not path.is_symlink():
                continue
            rel = "/" + str(path.relative_to(buildroot))
            if rel == texmf_doc_prefix or rel.startswith(texmf_doc_prefix + "/"):
                continue
            if rel not in assigned:
                unassigned.append(rel)
                add_installed_path("basic", rel, buildroot, package_files, package_dirs, standard_dirs)

    with (outdir / "texlive-unassigned-files.report").open("w") as fh:
        for rel in sorted(unassigned):
            fh.write(rel + "\n")

    print(f"TeX Live split: {len(unassigned)} non-doc texmf-dist files assigned by fallback to texlive-basic")
    if unassigned:
        buckets: DefaultDict[str, int] = defaultdict(int)
        for rel in unassigned:
            parts = rel.split("/")
            key = "/".join(parts[:5]) if len(parts) > 4 else rel
            buckets[key] += 1
        print("Top fallback buckets:")
        for key, count in sorted(buckets.items(), key=lambda item: (-item[1], item[0]))[:30]:
            print(f"  {count:6d}  {key}")
        if args.strict_split:
            print("Strict split mode is enabled; failing due to fallback-assigned files.", file=sys.stderr)
            return 1

    if duplicate_direct:
        print("Duplicate direct TeX Live package ownership detected:")
        for pkg, old, new in duplicate_direct[:100]:
            print(f"  {pkg}: {old}, also {new}")
    if missing_records:
        print("Missing tlpdb records for dependencies:")
        for pkg in sorted(missing_records)[:100]:
            print(f"  {pkg}")

    with (outdir / "texlive-generated-collection-deps.report").open("w") as fh:
        for coll in collections:
            deps = set(collection_deps[coll]) | set(cross_collection_pkg_deps.get(coll, set()))
            deps.discard(coll)
            if deps:
                fh.write(f"{coll}: " + " ".join(sorted(deps)) + "\n")

    frag_dir = buildroot_path(buildroot, install_path(args.sharedstatedir, "texmf/arch/installedpkgs"))
    frag_dir.mkdir(parents=True, exist_ok=True)

    for coll in collections:
        lines: list[str] = []
        for directory in sorted(package_dirs[coll]):
            lines.append(f"%dir {directory}")
        for path in sorted(package_files[coll] | package_bin[coll]):
            lines.append(filelist_entry(buildroot, path))

        for ext, frag_lines in fragments[coll].items():
            if not frag_lines:
                continue
            frag = frag_dir / f"{coll}.{ext}"
            write_unique_lines(frag, frag_lines)
            lines.append("/" + str(frag.relative_to(buildroot)))

        write_unique_lines(outdir / f"texlive-{coll}.files", lines)

    with (outdir / "texlive-script-interpreters.report").open("w") as fh:
        for coll in collections:
            if script_interpreters[coll]:
                fh.write(f"[{coll}]\n")
                for line in sorted(script_interpreters[coll]):
                    fh.write(line + "\n")

    doc_lines: list[str] = []
    compressed_roots = {
        buildroot_path(buildroot, args.mandir),
        buildroot_path(buildroot, args.infodir),
    }
    for root in [
        buildroot_path(buildroot, args.docdir),
        buildroot_path(buildroot, args.mandir),
        buildroot_path(buildroot, args.infodir),
    ]:
        if not root.exists():
            continue
        for path in sorted(root.rglob("*")):
            rel = "/" + str(path.relative_to(buildroot))
            if path.is_dir() and not path.is_symlink():
                doc_lines.append(f"%dir {rel}")
            elif any(path.is_relative_to(compressed_root) for compressed_root in compressed_roots):
                doc_lines.append(rel + "*")
            else:
                doc_lines.append(rel)

    doclink = texmf_dist / "doc"
    if doclink.exists() or doclink.is_symlink():
        doc_lines.append("/" + str(doclink.relative_to(buildroot)))
    write_unique_lines(outdir / "texlive-doc.files", doc_lines)

    # Ensure empty collection file lists exist even if upstream removes all files
    # from a collection in a future snapshot.
    for coll in collections:
        (outdir / f"texlive-{coll}.files").touch(exist_ok=True)

    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    """Parse command-line options supplied by the RPM spec."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--buildroot", required=True)
    parser.add_argument("--tlpdb", required=True)
    parser.add_argument("--texmf-dist", required=True)
    parser.add_argument("--collections", required=True)
    parser.add_argument("--script-aliases", required=True)
    parser.add_argument("--tl-link-arch", required=True)
    parser.add_argument("--datadir", required=True)
    parser.add_argument("--bindir", required=True)
    parser.add_argument("--sharedstatedir", required=True)
    parser.add_argument("--sysconfdir", required=True)
    parser.add_argument("--docdir", required=True, help="Installed documentation root, e.g. /usr/share/doc/texlive")
    parser.add_argument("--mandir", required=True)
    parser.add_argument("--infodir", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--strict-split", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """Run the generator with either explicit or process command-line args."""
    args = parse_args(sys.argv[1:] if argv is None else argv)
    return generate(args)


if __name__ == "__main__":
    raise SystemExit(main())
