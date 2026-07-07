#!/usr/bin/env python3
"""
pre-commit.py — Unified pre-commit check runner for openRuyi.

Usage:
    python scripts/pre-commit.py <hook-id> [files...]

Classes:
    Each Hook class corresponds to a hook ID from .pre-commit-config.yaml.
    Methods mirror the original language mode (pygrep / fail / python).
"""

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

from __future__ import annotations

import argparse
import re
import sys
import tomllib
from pathlib import Path
from typing import ClassVar, List, Optional

# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

RED   = "\033[1;31m"
YELLOW = "\033[33m"
RESET = "\033[0m"


def find_repo_root() -> Path:
    script = Path(__file__).resolve()
    for parent in script.parents:
        if (parent / "SPECS").is_dir():
            return parent
    return script.parent


def get_relative_path(arg: str, root: Path) -> Optional[Path]:
    """Resolve an argument (maybe absolute, maybe relative) to repo-relative path."""
    path = Path(arg)
    if not path.exists():
        return None
    try:
        return path.resolve().relative_to(root)
    except ValueError:
        return None


# ---------------------------------------------------------------------------
# Base class
# ---------------------------------------------------------------------------

class BaseHook:
    """A single pre-commit check."""

    hook_id: ClassVar[str] = ""
    description: ClassVar[str] = ""

    def __init__(self, repo_root: Path) -> None:
        self.repo_root = repo_root
        self.errors: List[str] = []

    def check_file(self, relpath: Path) -> None:
        """Check a single file. Append to self.errors on failure."""
        raise NotImplementedError

    def run(self, files: List[Path]) -> int:
        self.errors = []
        for f in files:
            self.check_file(f)
        if self.errors:
            print("\n".join(self.errors), file=sys.stderr)
            return 1
        return 0


# ---------------------------------------------------------------------------
# pygrep-style hooks — simple regex checks
# ---------------------------------------------------------------------------

class PygrepHook(BaseHook):
    """A hook that greps for a regex in each file and reports matches as errors.

    - Without negate: each match is an error (default pygrep).
    - With negate: file PASSES if pattern IS found; FAILS if pattern is NOT found.
    """

    pattern: ClassVar[str] = ""
    negate: ClassVar[bool] = False       # True → fail when pattern is NOT found in file
    multiline: ClassVar[bool] = False    # True → search whole file as single string
    error_fmt: ClassVar[str] = "{file}:{line}: {msg}"

    def check_file(self, relpath: Path) -> None:
        abspath = self.repo_root / relpath
        try:
            content = abspath.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            return

        flags = re.MULTILINE
        if self.multiline:
            flags |= re.DOTALL

        matches = list(re.finditer(self.pattern, content, flags))

        if self.negate:
            # negate: must have at least one match to pass
            if not matches:
                self.errors.append(
                    self.error_fmt.format(
                        file=relpath, line="",
                        msg=f"required pattern not found",
                    )
                )
        else:
            for m in matches:
                lineno = content[: m.start()].count("\n") + 1
                self.errors.append(
                    self.error_fmt.format(
                        file=relpath, line=lineno,
                        msg=m.group(0).strip(),
                    )
                )


# =========================================================================
# Hook implementations
# =========================================================================

class NoGroupTag(PygrepHook):
    hook_id = "no-group-tag"
    description = "check no Group tag"
    pattern = r'^Group:'
    error_fmt = "{file}:{line}: {YELLOW}warning{RESET} - Group tag is deprecated, remove it"


class Autorelease(PygrepHook):
    hook_id = "autorelease"
    description = "check autorelease macro"
    pattern = r'^Release:.*(%autorelease|%{autorelease}).*$'
    negate = True
    error_fmt = "{file}:{line}: {RED}error{RESET} - %autorelease is not allowed"


class CheckFilesPkgconfigFile(PygrepHook):
    hook_id = "check-files-pkgconfig-file"
    description = "check %files pkgconfig files is not *"
    pattern = r'^%{(_datadir|_libdir)}/pkgconfig/\*.*'
    error_fmt = "{file}:{line}: {RED}error{RESET} - wildcard in pkgconfig path, list .pc files explicitly"


class Autochangelog(PygrepHook):
    hook_id = "autochangelog"
    description = "check autochangelog macro"
    pattern = r'%changelog\s+%autochangelog'
    negate = True
    multiline = True
    error_fmt = "{file}: {RED}error{RESET} - %autochangelog is not allowed"


class FormatSpacing(PygrepHook):
    hook_id = "format-spacing"
    description = "Check format spacing"
    pattern = r'^(((BuildOption\(.*\)|BuildRequires):(?! {2}))|(%files {2,}(?=\S)))'
    error_fmt = "{file}:{line}: {RED}error{RESET} - incorrect spacing (needs two spaces after colon, or %files spacing)"


# ---------------------------------------------------------------------------
# fail-style hooks — filename pattern match
# ---------------------------------------------------------------------------

class FailHook(BaseHook):
    """A hook that fails if a filename matches a regex pattern."""

    pattern: ClassVar[str] = ""
    message: ClassVar[str] = ""

    def check_file(self, relpath: Path) -> None:
        if re.search(self.pattern, relpath.as_posix()):
            self.errors.append(f"{relpath}: {RED}error{RESET} - {self.message}")


class PythonName(FailHook):
    hook_id = "python-name"
    description = "python spec name should follow PEP 503"
    pattern = r'^SPECS/python-(?!([a-z0-9]|[a-z0-9][a-z0-9._-]*[a-z0-9])).*\.spec$'
    message = (
        "Python spec name must follow PEP 503. "
        "Valid characters: ASCII letters, digits, ., -, _; lowercased, separated by single -.\n"
        "See https://peps.python.org/pep-0503/#normalized-names\n"
        "See https://openruyi.cn/docs/guide/packaging-guidelines/languages/Python"
    )


class NoEntriesUnderSpecs(FailHook):
    hook_id = "no-entries-directly-under-SPECS"
    description = "SPECS may only contain subdirectories"
    pattern = r'^SPECS/[^/]+$'
    message = "Files directly under SPECS/ are not allowed — use a subdirectory for each package"


class DontAddConstraints(FailHook):
    hook_id = "dont-add-constraints-to-repo"
    description = "Don't add _constraints to spec directory"
    pattern = r'_constraints$'
    message = (
        "_constraints should not be placed in the git repository. "
        "It should be configured in the OBS repository."
    )


# ---------------------------------------------------------------------------
# python-script hooks (from scripts/pre-commit-hooks/)
# ---------------------------------------------------------------------------

class SourceWithRemoteAsset(BaseHook):
    hook_id = "sourcewithRemoteAsset"
    description = "check Source with #!RemoteAsset"

    def check_file(self, relpath: Path) -> None:
        abspath = self.repo_root / relpath
        try:
            lines = [line.strip() for line in abspath.read_text(encoding="utf-8").splitlines()]
        except (OSError, UnicodeDecodeError):
            return

        source_indices = [
            idx for idx, line in enumerate(lines)
            if re.match(r'^Source(\d+)?:\s+(https?://|%{url})', line)
        ]

        for idx in source_indices:
            if not re.match(r'^#!RemoteAsset:  sha256:[0-9a-f]{64}$', lines[idx - 1]):
                self.errors.append(
                    f"{YELLOW}{relpath}:{idx}-{idx+1}{RESET}: "
                    f"{RED}Error{RESET} - The source line is missing the required "
                    f"#!RemoteAsset:  sha256:xxx comment.\n"
                    f"{lines[idx-1]}\n{lines[idx]}\n---"
                )


class CheckRustCargoToml(BaseHook):
    hook_id = "check-rust-cargo-toml"
    description = "Check Cargo.toml for crate related specs"

    CRATE_TAG_RE = re.compile(r"^(BuildRequires|Requires|Provides)\s*:.*crate\(")

    def check_file(self, relpath: Path) -> None:
        # Note: This hook is called per-file by pre-commit.
        # We defer checking until all files are collected — see run() override.
        pass

    def run(self, files: List[Path]) -> int:
        cargo_tomls: List[Path] = []
        spec_files: List[Path] = []

        for f in files:
            parts = f.parts
            if len(parts) == 3 and parts[0] == "SPECS" and parts[-1] == "Cargo.toml":
                cargo_tomls.append(f)
            elif len(parts) == 3 and parts[0] == "SPECS" and f.suffix == ".spec":
                spec_files.append(f)

        errors: List[str] = []

        for ct in sorted(cargo_tomls):
            try:
                with (self.repo_root / ct).open("rb") as fh:
                    tomllib.load(fh)
            except Exception as e:
                errors.append(f"{ct}: {e}")

        for sf in sorted(spec_files):
            try:
                with (self.repo_root / sf).open(encoding="utf-8") as fh:
                    has_crate = any(
                        self.CRATE_TAG_RE.search(line.strip())
                        for line in fh
                        if not line.strip().startswith("#")
                    )
            except Exception as e:
                errors.append(f"{sf}: {e}")
                continue

            if has_crate and not (self.repo_root / sf.parent / "Cargo.toml").is_file():
                errors.append(
                    f"{sf}: uses crate(...) in BuildRequires/Requires/Provides "
                    "but missing Cargo.toml in the same directory"
                )

        if errors:
            print("\n".join(errors), file=sys.stderr)
            return 1

        print(
            f"checked {len(cargo_tomls)} Rust Cargo.toml files "
            f"and {len(spec_files)} spec files"
        )
        return 0


# ---------------------------------------------------------------------------
# Hook registry
# ---------------------------------------------------------------------------

def _all_subclasses(cls: type) -> set[type]:
    """Recursively find all concrete subclasses of cls."""
    result: set[type] = set()
    for sub in cls.__subclasses__():
        result.add(sub)
        result.update(_all_subclasses(sub))
    return result


HOOK_REGISTRY: dict[str, type[BaseHook]] = {
    cls.hook_id: cls
    for cls in _all_subclasses(BaseHook)
    if hasattr(cls, "hook_id") and cls.hook_id
}


def list_hooks() -> None:
    print("Available hooks:\n")
    for hook_id, cls in sorted(HOOK_REGISTRY.items()):
        print(f"  {hook_id:35s} — {cls.description}")


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description="openRuyi pre-commit unified runner")
    parser.add_argument("hook_id", nargs="?", help="Hook ID to run")
    parser.add_argument("files", nargs="*", help="Files to check")
    parser.add_argument("--list", action="store_true", help="List available hooks")
    args = parser.parse_args()

    if args.list:
        list_hooks()
        return 0

    if not args.hook_id:
        parser.print_help()
        return 1

    cls = HOOK_REGISTRY.get(args.hook_id)
    if cls is None:
        print(f"Unknown hook: {args.hook_id}", file=sys.stderr)
        return 1

    repo_root = find_repo_root()
    hook = cls(repo_root)

    files = [
        p for arg in args.files
        if (p := get_relative_path(arg, repo_root)) is not None
    ]

    if not files:
        # When called from pre-commit with pass_filenames: false, use cwd
        files = [Path(f) for f in args.files] if args.files else []

    return hook.run(files)


if __name__ == "__main__":
    sys.exit(main())
