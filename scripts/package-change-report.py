#!/usr/bin/env python3

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Requires Python 3.10+.
# Required utilities:
# - git

import argparse
import calendar
import json
import pathlib
import re
import shlex
import shutil
import subprocess  # nosec B404
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date
from typing import NamedTuple

SPEC_ROOT = "SPECS"
SPEC_FILES_PATHSPEC = ":(glob)SPECS/*/*.spec"
GIT_EMPTY_TREE = "4b825dc642cb6eb9a060e54bf8d69288fbee4904"
GIT_TIMEOUT_SECONDS = 60
ACTIONS = ("updated", "added", "removed")
COMMENT_RE = re.compile(r"\s+#.*$")
MACRO_RE = re.compile(r"^\s*%(?:global|define)\s+([A-Za-z0-9_]+)\s+(.*?)\s*$")
CONDITIONAL_VALUE_RE = re.compile(r"%\{\?([A-Za-z0-9_]+):([^{}]*(?:%\{[A-Za-z0-9_]+\}[^{}]*)*)\}")
BRACED_MACRO_RE = re.compile(r"%\{([^{}]+)\}")
BARE_MACRO_RE = re.compile(r"(?<!%)%([A-Za-z_][A-Za-z0-9_]*)")
SHELL_SLICE_RE = re.compile(r"%\(c=([A-Za-z0-9._+-]+);\s*echo\s+\$\{c:0:(\d+)\}\)")
SHELL_TR_RE = re.compile(r"%\(echo\s+([A-Za-z0-9._+-]+)\s+\|\s+tr\s+'(.)'\s+'(.)'\)")
SHELL_SLICE_PACKAGES = frozenset(
    (
        "accounts-qml-module",
        "asmjit",
        "blktests",
        "blktrace",
        "config",
        "cpuinfo",
        "fp16",
        "fxdiv",
        "gemmlowp",
        "kmscube",
        "mergerfs-tools",
        "mkosi",
        "mmtests",
        "netperf",
        "pthreadpool",
        "signon-plugin-oauth2",
        "tensorpipe",
        "trinity",
    )
)
SHELL_TR_PACKAGES = frozenset(("libtar", "lm_sensors"))
UNRESOLVED_VALUE_RE = re.compile(r"@[^@\s]+@|%\{|%\(")

EPILOG = f"""{sys.argv[0]} reads local Git history only and writes the report to stdout.

Examples:
$ {sys.argv[0]} --month 2026-05 --all
$ {sys.argv[0]} --since 2026-05-01 --until 2026-05-09 --all
$ {sys.argv[0]} --since "2 weeks ago" --updated
$ {sys.argv[0]} --from v0.1 --to HEAD --updated --commits
$ {sys.argv[0]} --from OLD --to NEW --added --format json

The report is a net range summary. --commits lists package-related commits in
that range, not a full RPM changelog. Use exactly one range mode: --month,
date, or ref. --since and --from may omit their end boundary, which defaults to
the latest commit. DATE accepts Git date expressions such as "yesterday" and
"2 weeks ago". Requires Python 3.10+.
"""

arg_parser = argparse.ArgumentParser(
    prog=sys.argv[0],
    description="Generate an openRuyi package change report from SPECS history",
    epilog=EPILOG,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    allow_abbrev=False,
)
arg_parser.add_argument(
    "--repo-root",
    metavar="ROOT",
    default=".",
    help="Path to local repository; default: current directory",
)
arg_parser.add_argument("--month", metavar="YYYY-MM", help="Scan a single month")
arg_parser.add_argument(
    "--since",
    metavar="DATE",
    help="Start Git date expression; omit --until to use the latest commit",
)
arg_parser.add_argument("--until", metavar="DATE", help="End Git date expression; requires --since")
arg_parser.add_argument(
    "--from",
    metavar="REF",
    dest="from_ref",
    help="Start commit/ref, excluded; omit --to to use HEAD",
)
arg_parser.add_argument("--to", metavar="REF", dest="to_ref", help="End commit/ref; requires --from")
arg_parser.add_argument(
    "--package",
    metavar="PACKAGE",
    action="append",
    dest="packages",
    help="Limit output to a package name",
)
arg_parser.add_argument(
    "--commits",
    action="store_true",
    help="List package-related commits in each reported change",
)

arg_parser.set_defaults(actions=("updated",))
action_group = arg_parser.add_mutually_exclusive_group()
action_group.add_argument(
    "--updated",
    dest="actions",
    action="store_const",
    const=("updated",),
    help="Show existing packages whose Version changed or directory was renamed; default",
)
action_group.add_argument(
    "--added",
    dest="actions",
    action="store_const",
    const=("added",),
    help="Show newly added packages",
)
action_group.add_argument(
    "--removed",
    dest="actions",
    action="store_const",
    const=("removed",),
    help="Show removed packages",
)
action_group.add_argument(
    "--all",
    dest="actions",
    action="store_const",
    const=ACTIONS,
    help="Show updated, added, and removed packages",
)

arg_parser.add_argument(
    "--format",
    choices=("text", "json"),
    default="text",
    help="Output format; default: text",
)


class Commit(NamedTuple):
    sha: str
    subject: str


class Spec(NamedTuple):
    version: str | None


class SpecChange(NamedTuple):
    old_path: str | None
    new_path: str | None
    old_dir: str | None
    new_dir: str | None


@dataclass(slots=True)
class PackageReport:
    package: str
    old: Spec | None
    new: Spec | None
    old_package: str | None = None
    old_dir: str | None = None
    new_dir: str | None = None
    commits: list[Commit] = field(default_factory=list)

    @property
    def old_version(self) -> str | None:
        return self.old.version if self.old else None

    @property
    def new_version(self) -> str | None:
        return self.new.version if self.new else None

    @property
    def action(self) -> str:
        if self.old is None:
            return "added" if self.new is not None else "unchanged"
        if self.new is None:
            return "removed"
        return "updated" if self.old_package or self.old_version != self.new_version else "unchanged"


def run(argv: list[str], *, cwd: pathlib.Path) -> str:
    try:
        # Git argv is constructed internally and shell=False.
        proc = subprocess.run(  # nosec B603
            argv,
            cwd=cwd,
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            timeout=GIT_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(f"{shlex.join(argv)} timed out after {GIT_TIMEOUT_SECONDS}s") from exc
    except OSError as exc:
        raise RuntimeError(f"failed to start {argv[0]}: {exc}") from exc
    if proc.returncode == 0:
        return proc.stdout
    message = proc.stderr.strip() or f"exit code {proc.returncode}"
    raise RuntimeError(f"{shlex.join(argv)} failed: {message}")


def package_dir(path: str | None, *, spec_only: bool = True) -> str | None:
    if not path:
        return None
    parts = path.split("/", 2)
    if len(parts) < 2:
        return None
    root, directory = parts[:2]
    if root != SPEC_ROOT or not directory:
        return None
    if spec_only and (len(parts) != 3 or not parts[2].endswith(".spec")):
        return None
    return directory


def clean_value(value: str) -> str:
    return COMMENT_RE.sub("", value).strip()


def expand_braced_macro(
    match: re.Match[str],
    macros: dict[str, str],
    package: str | None,
) -> str:
    body = match.group(1)
    if body.startswith(("?", "!?")):
        inverted = body.startswith("!?")
        name, sep, value = body[2 if inverted else 1 :].partition(":")
        if sep:
            return clean_value(value) if (name in macros) != inverted else ""
        if inverted or name not in macros:
            return ""
        scoped = macros.copy()
        scoped.pop(name, None)
        value = resolve_macros(macros[name], scoped, package) or ""
        return "" if UNRESOLVED_VALUE_RE.search(value) else value
    return macros.get(body, match.group(0))


def expand_shell_macros(value: str, package: str | None) -> str:
    # Shell macro expansion is allowlisted by package. Do not execute shell.
    #
    # SHELL_SLICE_PACKAGES is the package whitelist for short commit macros.
    # SHELL_TR_PACKAGES is the package whitelist for simple delimiter rewrites.
    #
    # This is not a shell parser.
    if package in SHELL_SLICE_PACKAGES:
        value = SHELL_SLICE_RE.sub(lambda m: m.group(1)[: int(m.group(2))], value)
    if package in SHELL_TR_PACKAGES:
        value = SHELL_TR_RE.sub(lambda m: m.group(1).replace(m.group(2), m.group(3)), value)
    return value


def resolve_macros(value: str, macros: dict[str, str], package: str | None = None) -> str:
    for _ in range(20):
        old = value
        value = CONDITIONAL_VALUE_RE.sub(
            lambda m: resolve_macros(m.group(2), macros, package)
            if m.group(1) in macros
            else "",
            value,
        )
        value = BRACED_MACRO_RE.sub(lambda m: expand_braced_macro(m, macros, package), value)
        value = BARE_MACRO_RE.sub(lambda m: macros.get(m.group(1), m.group(0)), value)
        value = expand_shell_macros(value, package)
        value = value.replace("%%", "%")
        if value == old:
            return value
    return value


def parse_spec(text: str | None, package_hint: str | None = None) -> Spec | None:
    if text is None:
        return None

    macros: dict[str, str] = {"nil": ""}

    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        if macro := MACRO_RE.match(line):
            macros[macro.group(1)] = clean_value(macro.group(2))
            continue

        key, sep, value = line.partition(":")
        if not sep:
            continue

        key = key.strip().lower()
        value = clean_value(value)
        if key == "version":
            return Spec(version=resolve_macros(value, macros, package_hint))

    return Spec(version=None)


def parse_name_status(output: str) -> list[SpecChange]:
    if not output:
        return []

    changes: list[SpecChange] = []
    fields = iter(output.rstrip("\0").split("\0"))
    for status in fields:
        path = next(fields)
        old_path, new_path = None if status == "A" else path, None if status == "D" else path
        old_dir, new_dir = package_dir(old_path), package_dir(new_path)
        if old_dir or new_dir:
            changes.append(
                SpecChange(
                    old_path if old_dir else None,
                    new_path if new_dir else None,
                    old_dir,
                    new_dir,
                )
            )
    return changes


def parse_renames(output: str) -> list[tuple[str, str]]:
    if not output:
        return []

    renames: list[tuple[str, str]] = []
    fields = iter(output.rstrip("\0").split("\0"))
    for status in fields:
        if not status:
            continue
        if status.startswith("R"):
            old_path, new_path = next(fields), next(fields)
            old_dir, new_dir = package_dir(old_path), package_dir(new_path)
            if old_dir and new_dir and old_dir != new_dir:
                renames.append((old_dir, new_dir))
        else:
            next(fields)
    return renames


def collapsed_renames(renames: list[tuple[str, str]]) -> dict[str, str]:
    result: dict[str, str] = {}
    for old_dir, new_dir in renames:
        source = next((old for old, new in result.items() if new == old_dir), old_dir)
        result[source] = new_dir
    return result


class GitRepo:
    def __init__(self, repo_root: str) -> None:
        self.root = pathlib.Path(repo_root).resolve()
        git = shutil.which("git")
        if git is None:
            raise RuntimeError("git not found in PATH")
        self.git = git

    def log_command(
        self,
        args: argparse.Namespace,
        fmt: str,
        paths: list[str],
        *,
        name_only: bool = False,
    ) -> list[str]:
        cmd = [self.git, "log", "--reverse"]
        if name_only:
            cmd.append("--name-only")
        cmd.append(f"--format={fmt}")
        if args.month is not None or args.since is not None:
            since, until = (
                month_bounds(args.month)
                if args.month is not None
                else (args.since, args.until)
            )
            cmd.append(f"--since={git_time(since, end=False)}")
            if until is not None:
                cmd.append(f"--until={git_time(until, end=True)}")
        if args.from_ref is not None:
            cmd.append(f"{args.from_ref}..{args.to_ref or 'HEAD'}")
        cmd.extend(["--", *paths])
        return cmd

    def range_refs(self, args: argparse.Namespace) -> tuple[str | None, str | None]:
        if args.from_ref is not None:
            return args.from_ref, args.to_ref or "HEAD"

        base_ref: str | None = None
        head_ref: str | None = None
        for line in run(
            self.log_command(args, "%H%x1f%P", [SPEC_FILES_PATHSPEC]),
            cwd=self.root,
        ).splitlines():
            sha, parents = line.split("\x1f", 1)
            if head_ref is None:
                base_ref = parents.split()[0] if parents else None
            head_ref = sha
        return base_ref, head_ref

    def range_changes(self, base_ref: str | None, head_ref: str) -> list[SpecChange]:
        cmd = [
            self.git,
            "diff",
            "--name-status",
            "-r",
            "--no-renames",
            "-z",
            base_ref or GIT_EMPTY_TREE,
            head_ref,
        ]
        cmd.extend(["--", SPEC_FILES_PATHSPEC])
        return parse_name_status(run(cmd, cwd=self.root))

    def range_renames(self, base_ref: str | None, head_ref: str) -> dict[str, str]:
        if not base_ref:
            return {}
        cmd = [
            self.git,
            "log",
            "--reverse",
            "--format=",
            "--name-status",
            "-M",
            "--diff-filter=R",
            "-z",
            f"{base_ref}..{head_ref}",
            "--",
            SPEC_FILES_PATHSPEC,
        ]
        return collapsed_renames(parse_renames(run(cmd, cwd=self.root)))

    def read_files(self, ref: str | None, paths: set[str]) -> dict[str, str | None]:
        if not ref or not paths:
            return {}
        sorted_paths = sorted(paths)

        requests = "".join(f"{ref}:{path}\n" for path in sorted_paths).encode()
        try:
            # Git argv is constructed internally and shell=False.
            proc = subprocess.run(  # nosec B603
                [self.git, "cat-file", "--batch"],
                cwd=self.root,
                input=requests,
                capture_output=True,
                timeout=GIT_TIMEOUT_SECONDS,
            )
        except subprocess.TimeoutExpired as exc:
            raise RuntimeError(f"git cat-file --batch timed out after {GIT_TIMEOUT_SECONDS}s") from exc
        except OSError as exc:
            raise RuntimeError(f"failed to start git: {exc}") from exc
        if proc.returncode != 0:
            message = (
                proc.stderr.decode("utf-8", errors="replace").strip()
                or f"exit code {proc.returncode}"
            )
            raise RuntimeError(f"git cat-file --batch failed: {message}")

        result: dict[str, str | None] = {}
        offset = 0
        output = proc.stdout
        for path in sorted_paths:
            if (line_end := output.find(b"\n", offset)) < 0:
                raise RuntimeError("git cat-file --batch returned truncated output")
            fields = output[offset:line_end].decode("utf-8", errors="replace").split()
            offset = line_end + 1
            if len(fields) != 3 or fields[1] != "blob":
                result[path] = None
                continue

            size = int(fields[2])
            result[path] = output[offset : offset + size].decode("utf-8", errors="replace")
            offset += size
            if output[offset : offset + 1] == b"\n":
                offset += 1
        return result

    def commits_by_dir(
        self,
        args: argparse.Namespace,
        dirs: set[str],
    ) -> dict[str, list[Commit]]:
        if not dirs:
            return {}

        cmd = self.log_command(
            args,
            "commit:%H%x1f%s",
            [f"{SPEC_ROOT}/{directory}" for directory in sorted(dirs)],
            name_only=True,
        )

        result: dict[str, list[Commit]] = defaultdict(list)
        seen: dict[str, set[str]] = defaultdict(set)
        current: Commit | None = None
        for line in run(cmd, cwd=self.root).splitlines():
            if line.startswith("commit:"):
                sha, subject = line.removeprefix("commit:").split("\x1f", 1)
                current = Commit(sha=sha, subject=subject)
                continue
            if not current:
                continue
            directory = package_dir(line, spec_only=False)
            if directory not in dirs:
                continue
            seen_commits = seen[directory]
            if current.sha in seen_commits:
                continue
            seen_commits.add(current.sha)
            result[directory].append(current)

        return result


def git_time(value: str, *, end: bool) -> str:
    try:
        day = date.fromisoformat(value)
    except ValueError:
        return value
    if not end:
        return day.isoformat()
    return f"{day.isoformat()} 23:59:59"


def month_bounds(value: str) -> tuple[str, str]:
    try:
        first = date.fromisoformat(f"{value}-01")
    except ValueError:
        raise RuntimeError(f"--month must use YYYY-MM, got {value!r}")

    last_day = calendar.monthrange(first.year, first.month)[1]
    return first.isoformat(), first.replace(day=last_day).isoformat()


def collect(
    repo: GitRepo,
    base_ref: str | None,
    head_ref: str | None,
    action_filters: tuple[str, ...],
) -> list[PackageReport]:
    if not head_ref:
        return []

    changes = repo.range_changes(base_ref, head_ref)
    old_files = repo.read_files(base_ref, {change.old_path for change in changes if change.old_path})
    new_files = repo.read_files(head_ref, {change.new_path for change in changes if change.new_path})

    reports: dict[str, PackageReport] = {}
    for change in changes:
        old_text = old_files.get(change.old_path) if change.old_path else None
        new_text = new_files.get(change.new_path) if change.new_path else None
        old_spec, new_spec = parse_spec(old_text, change.old_dir), parse_spec(new_text, change.new_dir)
        package = change.new_dir or change.old_dir
        if package is None:
            continue
        reports[package] = PackageReport(
            package=package,
            old=old_spec,
            new=new_spec,
            old_dir=change.old_dir,
            new_dir=change.new_dir,
        )

    for old_dir, new_dir in repo.range_renames(base_ref, head_ref).items():
        old_report = reports.get(old_dir)
        new_report = reports.get(new_dir)
        if not old_report or not new_report:
            continue
        if old_report.action != "removed" or new_report.action != "added":
            continue
        reports[new_dir] = PackageReport(
            package=new_dir,
            old=old_report.old,
            new=new_report.new,
            old_package=old_dir,
            old_dir=old_report.old_dir,
            new_dir=new_report.new_dir,
        )
        del reports[old_dir]

    return sorted(
        (item for item in reports.values() if item.action in action_filters),
        key=lambda item: item.package.lower(),
    )


def attach_commits(
    repo: GitRepo,
    reports: list[PackageReport],
    args: argparse.Namespace,
) -> None:
    # TODO: Track intermediate dirs for packages renamed more than once.
    dirs: set[str] = set()
    for report in reports:
        for path in (report.old_dir, report.new_dir):
            if path:
                dirs.add(path)

    by_dir = repo.commits_by_dir(args, dirs)

    for report in reports:
        seen_commits: set[str] = set()
        for package_dir in dict.fromkeys(
            path for path in (report.old_dir, report.new_dir) if path
        ):
            for commit in by_dir.get(package_dir, []):
                if commit.sha in seen_commits:
                    continue
                seen_commits.add(commit.sha)
                report.commits.append(commit)


def display_version(version: str | None) -> str:
    return version if version is not None else "-"


def report_data(report: PackageReport, include_commits: bool) -> dict[str, object]:
    item = {
        "action": report.action,
        "package": report.package,
        "old_package": report.old_package,
        "old_exists": report.old is not None,
        "new_exists": report.new is not None,
        "old_version": report.old_version,
        "new_version": report.new_version,
    }
    if include_commits:
        item["commits"] = [
            {"sha": commit.sha, "subject": commit.subject}
            for commit in report.commits
        ]
    return item


def render_text(
    reports: list[PackageReport],
    range_text: str,
    actions: tuple[str, ...],
    include_commits: bool,
) -> str:
    lines = [
        "Package Change Report",
        f"Range: {range_text}",
        f"Change filter: {', '.join(actions)}",
        f"Packages changed: {len(reports)}",
        "",
    ]
    if not reports:
        lines.append("No matching package changes found.")
        return "\n".join(lines)

    groups: dict[str, list[PackageReport]] = defaultdict(list)
    for report in reports:
        groups[report.action].append(report)

    for action in ACTIONS:
        if not groups[action]:
            continue
        lines.append(f"{action.title()} packages:")
        for report in groups[action]:
            old_version = display_version(report.old_version)
            new_version = display_version(report.new_version)
            package = f"{report.old_package} -> {report.package}" if report.old_package else report.package
            lines.append(f"  {package}: {old_version} -> {new_version}")
            if include_commits:
                lines.extend(
                    f"      {commit.sha[:8]} {commit.subject}"
                    for commit in report.commits
                )
        lines.append("")
    return "\n".join(lines).rstrip()


def render_json(
    reports: list[PackageReport],
    range_text: str,
    actions: tuple[str, ...],
    include_commits: bool,
) -> str:
    return json.dumps(
        {
            "schema_version": 1,
            "range": range_text,
            "actions": list(actions),
            "packages_changed": len(reports),
            "packages": [report_data(report, include_commits) for report in reports],
        },
        ensure_ascii=False,
        indent=2,
    )


def describe_range(args: argparse.Namespace) -> str:
    if args.from_ref is not None:
        return f"{args.from_ref}..{args.to_ref or 'HEAD'}"
    if args.month is not None:
        return f"month {args.month}"
    if args.until is not None:
        return f"since {args.since}, until {args.until}"
    return f"since {args.since}"


def validate(args: argparse.Namespace, parser: argparse.ArgumentParser) -> None:
    for option, value in (
        ("--month", args.month),
        ("--since", args.since),
        ("--until", args.until),
        ("--from", args.from_ref),
        ("--to", args.to_ref),
    ):
        if value is not None and not value.strip():
            parser.error(f"{option} cannot be empty")

    month_mode = args.month is not None
    date_mode = args.since is not None or args.until is not None
    ref_mode = args.from_ref is not None or args.to_ref is not None
    if sum((month_mode, date_mode, ref_mode)) != 1:
        parser.error("use exactly one of --month, date range, or ref range")
    if date_mode and args.since is None:
        parser.error("use --since before --until")
    if ref_mode and args.from_ref is None:
        parser.error("use --from before --to")
    if args.month is not None:
        try:
            month_bounds(args.month)
        except RuntimeError as exc:
            parser.error(str(exc))


def main(argv: list[str] | None = None) -> int:
    args = arg_parser.parse_args(argv)
    validate(args, arg_parser)

    try:
        repo = GitRepo(args.repo_root)
        actions = args.actions
        package_filters = set(args.packages or [])
        range_text = describe_range(args)
        base_ref, head_ref = repo.range_refs(args)

        reports = [
            report
            for report in collect(repo, base_ref, head_ref, actions)
            if (
                not package_filters
                or report.package in package_filters
                or report.old_package in package_filters
            )
        ]
        if args.commits:
            attach_commits(repo, reports, args)
        render = {"text": render_text, "json": render_json}[args.format]
        print(render(reports, range_text, actions, args.commits))
        return 0
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
