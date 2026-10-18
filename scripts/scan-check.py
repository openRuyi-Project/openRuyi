#!/usr/bin/env python3

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

"""Scan SPEC files for an effective target-specific %check section."""

import argparse
import concurrent.futures
import contextlib
import csv
import os
import re
import shutil
import shlex
import subprocess
import sys
from pathlib import Path
from typing import NamedTuple


# This is intentionally the same set of section tokens RPM accepts.  Do not
# treat arbitrary macros such as %make_build as section boundaries.
SECTION_RE = re.compile(
    r"^%(?:package|prep|generate_buildrequires|conf|build|install|check|clean|"
    r"preun|postun|pretrans|posttrans|preuntrans|postuntrans|pre|post|files|"
    r"changelog|description|triggerpostun|triggerprein|triggerun|triggerin|"
    r"trigger|verifyscript|sepolicy|filetriggerin|filetrigger|filetriggerun|"
    r"filetriggerpostun|transfiletriggerin|transfiletrigger|"
    r"transfiletriggerun|transfiletriggerpostun|end|patchlist|sourcelist)"
    r"(?:\s|$)",
    re.IGNORECASE,
)
CHECK_SECTION_RE = re.compile(r"^%check(?:\s|$)", re.IGNORECASE)
NOOP_COMMANDS = {"%nil", ":", "true", "exit 0", "exit  0"}
NOOP_SHELL_COMMANDS = {"return", "set", "umask", "unset"}
DIRECTORY_COMMANDS = {"cd", "popd", "pushd"}


class ScanResult(NamedTuple):
    package: str
    enabled: str
    state: str
    detail: str


def parse_args() -> argparse.Namespace:
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent
    parser = argparse.ArgumentParser(
        description="Determine whether SPEC files have an effective %check section."
    )
    parser.add_argument(
        "specs",
        nargs="?",
        type=Path,
        default=repo_root / "SPECS",
        help="package directory root (default: SPECS)",
    )
    parser.add_argument(
        "--target",
        default="riscv64",
        help="RPM target passed to rpmspec (default: riscv64)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("-"),
        help="CSV output path, or - for stdout (default: -)",
    )
    parser.add_argument(
        "--jobs",
        type=int,
        default=min(8, os.cpu_count() or 1),
        help="parallel rpmspec processes (default: at most 8)",
    )
    parser.add_argument(
        "--rpmspec",
        default="rpmspec",
        help="rpmspec executable (default: search PATH)",
    )
    parser.add_argument(
        "--define",
        action="append",
        default=[],
        metavar="MACRO EXPR",
        help="extra rpmspec --define option; may be repeated",
    )
    parser.add_argument(
        "--test-packages",
        type=Path,
        help=(
            "optional file containing openRuyi source package names with RISC-V "
            "platform tests, one per line; comments and blank lines are ignored"
        ),
    )
    parser.add_argument(
        "--keep-going",
        action="store_true",
        help="write rows for parse failures and continue",
    )
    args = parser.parse_args()

    if args.jobs < 1:
        parser.error("--jobs must be at least 1")
    if shutil.which(args.rpmspec) is None and not Path(args.rpmspec).is_file():
        parser.error(f"rpmspec executable not found: {args.rpmspec}")
    return args


def find_specs(root: Path) -> list[tuple[str, Path]]:
    if not root.is_dir():
        raise ValueError(f"SPEC root is not a directory: {root}")

    result = []
    errors = []
    for package_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        specs = sorted(package_dir.glob("*.spec"))
        if len(specs) != 1:
            errors.append(
                f"{package_dir.relative_to(root)}: expected one .spec file, found {len(specs)}"
            )
            continue
        result.append((package_dir.name, specs[0]))

    if errors:
        raise ValueError("\n".join(errors))
    if not result:
        raise ValueError(f"no package SPEC files found under {root}")
    return result


def rpmspec_command(args: argparse.Namespace, spec: Path) -> list[str]:
    command = [
        args.rpmspec,
        "--parse",
        "--target",
        args.target,
        "--define",
        f"_sourcedir {spec.parent}",
    ]
    for define in args.define:
        command.extend(("--define", define))
    command.append(str(spec))
    return command


def check_bodies(parsed_spec: str) -> list[list[str]]:
    bodies: list[list[str]] = []
    current: list[str] | None = None
    for line in parsed_spec.splitlines():
        if SECTION_RE.match(line):
            if current is not None:
                bodies.append(current)
                current = None
            if CHECK_SECTION_RE.match(line):
                current = []
            continue
        if current is not None:
            current.append(line)
    if current is not None:
        bodies.append(current)
    return bodies


def executable_lines(body: list[str]) -> list[str]:
    lines = []
    for raw_line in body:
        line = raw_line.strip()
        if not line or line.startswith("#") or line in NOOP_COMMANDS:
            continue
        if not is_environment_only(line):
            lines.append(line)
    return lines


def is_environment_only(line: str) -> bool:
    """Return true for assignments and shell setup that do not run a test."""
    try:
        words = shlex.split(line, posix=True)
    except ValueError:
        words = line.split()
    if not words:
        return True
    if words[0] == "export":
        return len(words) > 1 and all("=" in word for word in words[1:])
    if len(words) == 1:
        return "=" in words[0]
    if words[0] in NOOP_SHELL_COMMANDS:
        return True
    if words[0] in DIRECTORY_COMMANDS:
        separators = {"&&", "||", "|", ";", ";;"}
        return not any(word in separators for word in words)
    return False


def scan_one(args: argparse.Namespace, item: tuple[str, Path]) -> ScanResult:
    package, spec = item
    command = rpmspec_command(args, spec)
    try:
        process = subprocess.run(
            command,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    except OSError as exc:
        detail = f"failed to run {args.rpmspec}: {exc}"
        return ScanResult(package, "Error", "rpmspec-error", detail)

    if process.returncode != 0:
        detail = process.stderr.strip() or f"rpmspec exited with {process.returncode}"
        return ScanResult(package, "Error", "rpmspec-error", detail)

    bodies = check_bodies(process.stdout)
    if not bodies:
        return ScanResult(package, "No", "missing-check", "")

    effective = [line for body in bodies for line in executable_lines(body)]
    if effective:
        return ScanResult(package, "Yes", "nonempty-check", "")
    return ScanResult(package, "No", "empty-check", "")


def read_test_packages(path: Path | None) -> set[str]:
    if path is None:
        return set()
    result = set()
    with path.open(encoding="utf-8") as stream:
        for raw_line in stream:
            line = raw_line.strip()
            if line and not line.startswith("#"):
                result.add(line)
    return result


def open_output(path: Path):
    if path == Path("-"):
        return contextlib.nullcontext(sys.stdout)
    path.parent.mkdir(parents=True, exist_ok=True)
    return path.open("w", encoding="utf-8", newline="")


def main() -> int:
    args = parse_args()
    try:
        specs = find_specs(args.specs.resolve())
        test_packages = read_test_packages(args.test_packages)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as executor:
        futures = [executor.submit(scan_one, args, item) for item in specs]
        results = [future.result() for future in futures]
    results.sort(key=lambda result: result.package)

    failures = [result for result in results if result.enabled == "Error"]
    scan_platform_tests = args.test_packages is not None
    with open_output(args.output) as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(["package", "check_enabled", "riscv_platform_tests", "state", "detail"])
        for result in results:
            if scan_platform_tests:
                platform_test = "Yes" if result.package in test_packages else "No"
            else:
                platform_test = "Unknown"
            writer.writerow(
                [result.package, result.enabled, platform_test, result.state, result.detail]
            )
        stream.flush()

    enabled = sum(result.enabled == "Yes" for result in results)
    disabled = sum(result.enabled == "No" for result in results)
    print(
        f"scanned={len(results)} check-enabled={enabled} check-disabled={disabled} "
        f"errors={len(failures)}",
        file=sys.stderr,
    )
    if failures and not args.keep_going:
        for result in failures:
            print(f"{result.package}: {result.detail}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
