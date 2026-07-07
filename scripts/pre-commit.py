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
import subprocess
import sys
import tomllib
from datetime import datetime
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
    """
    Verifies that RPM spec files do NOT contain the deprecated ``Group:`` tag.

    The Group tag was removed from modern RPM packaging guidelines.
    openRuyi does not use it, and its presence indicates stale boilerplate.

    | What | Example |
    |------|---------|
    | ❌ rejected (has Group tag) | ``Group: System/Libraries`` |
    | ✅ accepted               | no ``Group:`` line anywhere in the spec |

    检查是否使用了已废弃的 ``Group:`` 标签。openRuyi 不使用此标签，出现即表示老旧模板残留。
    """
    hook_id = "no-group-tag"
    description = "check no Group tag"
    pattern = r'^Group:'
    error_fmt = "{file}:{line}: {YELLOW}warning{RESET} - Group tag is deprecated, remove it"


class Autorelease(PygrepHook):
    """
    Verifies that RPM spec files do NOT use the ``%autorelease`` macro.

    openRuyi manages Release numbers via the build system (OBS) with
    ``<CI_CNT>.<B_CNT>%{?dist}``, not via ``%autorelease``.

    | What | Example |
    |------|---------|
    | ❌ rejected               | ``Release: %autorelease`` |
    | ❌ rejected               | ``Release: 1.%autorelease`` |
    | ✅ accepted               | ``Release: <CI_CNT>.<B_CNT>%{?dist}`` |

    检查 spec 是否使用了 ``%autorelease`` 宏。openRuyi 通过 OBS 构建系统管理 Release 号，不允许使用此宏。
    """
    hook_id = "autorelease"
    description = "check autorelease macro"
    pattern = r'^Release:.*(%autorelease|%{autorelease}).*$'
    negate = True
    error_fmt = "{file}:{line}: {RED}error{RESET} - %autorelease is not allowed"


class CheckFilesPkgconfigFile(PygrepHook):
    """
    Verifies that ``%files`` sections listing pkgconfig (``.pc``) files
    use explicit filenames rather than wildcards.

    Using ``*`` makes it impossible to audit which files a package ships.

    | What | Example |
    |------|---------|
    | ❌ rejected (wildcard)    | ``%{_libdir}/pkgconfig/*`` |
    | ✅ accepted (explicit)    | ``%{_libdir}/pkgconfig/foo.pc`` |
    | ✅ accepted (explicit)    | ``%{_datadir}/pkgconfig/bar.pc`` |

    检查 ``%files`` 中 pkgconfig 路径不能使用通配符 ``*``，必须明确列出 ``.pc`` 文件名，便于审计包内容。
    """
    hook_id = "check-files-pkgconfig-file"
    description = "check %files pkgconfig files is not *"
    pattern = r'^%{(_datadir|_libdir)}/pkgconfig/\*.*'
    error_fmt = "{file}:{line}: {RED}error{RESET} - wildcard in pkgconfig path, list .pc files explicitly"


class Autochangelog(PygrepHook):
    """
    Verifies that RPM spec files do NOT use ``%autochangelog``.

    openRuyi maintains changelogs manually to ensure accuracy and project-wide
    consistency across all packages.

    | What | Example |
    |------|---------|
    | ❌ rejected               | ``%changelog`` followed by ``%autochangelog`` |
    | ✅ accepted               | ``%changelog`` followed by manual entries |

    检查 spec 是否使用了 ``%autochangelog`` 宏。openRuyi 手动维护 changelog，不允许自动生成。
    """
    hook_id = "autochangelog"
    description = "check autochangelog macro"
    pattern = r'%changelog\s+%autochangelog'
    negate = True
    multiline = True
    error_fmt = "{file}: {RED}error{RESET} - %autochangelog is not allowed"


class FormatSpacing(PygrepHook):
    """
    Enforces consistent spacing in RPM spec files:

    1. ``BuildRequires:``, ``BuildOption(...):`` — must have exactly **2 spaces**
       between the colon and the value.
    2. ``%files`` — must have **exactly 1 space** between the macro and the path
       (no extra spaces).

    | What | Example |
    |------|---------|
    | ❌ rejected (1 space)     | ``BuildRequires: pkg`` |
    | ❌ rejected (1 space)     | ``BuildOption(foo): bar`` |
    | ❌ rejected (extra spaces)| ``%files   /path`` |
    | ✅ accepted               | ``BuildRequires:  pkg`` |
    | ✅ accepted               | ``BuildOption(foo):  bar`` |
    | ✅ accepted               | ``%files /path`` |

    检查 spec 格式空格：``BuildRequires:`` / ``BuildOption():`` 冒号后必须空 2 格，``%files`` 后只能空 1 格。
    """
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
    """
    Enforces that Python package spec files follow `PEP 503 Normalized Names
    <https://peps.python.org/pep-0503/#normalized-names>`_.

    The directory under ``SPECS/`` must be named ``python-<normalized-name>``
    where the normalized name contains only ASCII lowercase letters, digits,
    ``.``, ``-``, and ``_``, with runs of ``.`` / ``-`` / ``_`` collapsed
    to a single ``-``.

    | What | Example |
    |------|---------|
    | ❌ rejected               | ``SPECS/python-My_Package.spec`` (uppercase) |
    | ❌ rejected               | ``SPECS/python-my__pkg.spec`` (double underscore) |
    | ❌ rejected               | ``SPECS/python-my..pkg.spec`` (double dot) |
    | ✅ accepted               | ``SPECS/python-my-package/python-my-package.spec`` |

    检查 Python 包 spec 文件名是否遵循 PEP 503 规范。目录名必须是 ``python-<标准化名称>``，
    仅允许 ASCII 小写字母、数字、``.``、``-``、``_``，且连续分隔符合并为单个 ``-``。
    """
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
    """
    Ensures that the ``SPECS/`` directory contains only subdirectories
    (one per package), never loose files.

    Each package must live in its own ``SPECS/<pkgname>/`` directory.

    | What | Example |
    |------|---------|
    | ❌ rejected               | ``SPECS/some-random-file.txt`` |
    | ❌ rejected               | ``SPECS/my-package.spec`` (spec outside a dir) |
    | ✅ accepted               | ``SPECS/acl/acl.spec`` |
    | ✅ accepted               | ``SPECS/bash/bash.spec`` |

    检查 ``SPECS/`` 下只能有子目录，不能直接放文件。每个包必须位于 ``SPECS/<包名>/`` 目录中。
    """
    hook_id = "no-entries-directly-under-SPECS"
    description = "SPECS may only contain subdirectories"
    pattern = r'^SPECS/[^/]+$'
    message = "Files directly under SPECS/ are not allowed — use a subdirectory for each package"


class DontAddConstraints(FailHook):
    """
    Prevents ``_constraints`` files from being added to the git repository.

    ``_constraints`` define build-resource requirements (CPU, memory, disk)
    and must be configured directly in the OBS project, not stored in git.

    | What | Example |
    |------|---------|
    | ❌ rejected               | ``SPECS/some-pkg/_constraints`` |
    | ❌ rejected               | ``SPECS/some-pkg/subdir/_constraints`` |
    | ✅ accepted               | any file not named ``_constraints`` |

    禁止在 spec 目录中放置 ``_constraints`` 文件。构建资源约束应在 OBS 仓库中配置，不应纳入 git。
    """
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
    """
    Verifies that every ``Source:`` / ``SourceN:`` line pointing to an HTTP(S)
    URL or ``%{url}`` macro has a ``#!RemoteAsset:  sha256:...`` comment
    immediately above it.

    This ensures remote sources are pinned to a known checksum for
    reproducibility and security.

    | What | Example |
    |------|---------|
    | ❌ rejected (missing comment)  | ``Source: https://example.com/pkg-1.0.tar.gz`` (no ``#!RemoteAsset`` above) |
    | ❌ rejected (no sha256)        | ``#!RemoteAsset:`` followed by ``Source: https://...`` |
    | ✅ accepted                     | ``#!RemoteAsset:  sha256:abcd1234...`` (64 hex chars) above ``Source: https://...`` |

    检查每个通过 HTTP(S) URL 或 ``%{url}`` 宏引入的 ``Source`` 行，其上一行必须有
    ``#!RemoteAsset:  sha256:<64位hex>`` 注释，确保远程资源校验和可追溯。
    """
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
    """
    For Rust crate packages, validates two things:

    1. Every ``Cargo.toml`` in a ``SPECS/<pkg>/`` directory is valid TOML.
    2. If a spec uses ``crate(...)`` in ``BuildRequires`` / ``Requires`` /
       ``Provides``, a ``Cargo.toml`` **must** exist in the same directory.

    This ensures crate metadata is available for the build tooling.

    | What | Example |
    |------|---------|
    | ❌ rejected (broken TOML)   | ``Cargo.toml`` with syntax errors |
    | ❌ rejected (missing file) | ``SPECS/rust-foo/rust-foo.spec`` uses ``crate(foo)`` but no ``Cargo.toml`` |
    | ✅ accepted                 | ``SPECS/rust-foo/rust-foo.spec`` uses ``crate(foo)`` and ``Cargo.toml`` exists |
    | ✅ accepted                 | ``SPECS/rust-foo/rust-foo.spec`` does NOT use ``crate(...)`` (no Cargo.toml needed) |

    对 Rust crate 包：
    1) 验证 ``Cargo.toml`` 是合法的 TOML 文件；
    2) 如果 spec 在 BuildRequires/Requires/Provides 中使用了 ``crate(...)``，同目录下必须存在 ``Cargo.toml``。
    """
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
# reuse-add-annotate — auto-add REUSE license headers to .spec files
# ---------------------------------------------------------------------------

class ReuseAddAnnotate(BaseHook):
    """
    Automatically adds REUSE-compliant SPDX license headers to ``.spec`` files
    that do not already have them.

    Uses the first git commit year + current year as the copyright year(s),
    ``Institute of Software, Chinese Academy of Sciences (ISCAS)`` and
    ``openRuyi Project Contributors`` as copyright holders, and
    ``MulanPSL-2.0`` as the license identifier.

    Requires ``reuse>=6.0.0`` to be installed in the pre-commit environment.

    | What | Example |
    |------|---------|
    | ✅ (added header)    | ``acl.spec`` without SPDX header → header inserted |
    | ✅ (already ok)      | ``bash.spec`` already has SPDX header → skipped |

    自动为缺少 REUSE 许可证头的 ``.spec`` 文件添加 SPDX 头。

    使用第一次 git 提交年份 + 当前年份作为版权年份，
    持有者为 ``Institute of Software, Chinese Academy of Sciences (ISCAS)``
    和 ``openRuyi Project Contributors``，许可证为 ``MulanPSL-2.0``。

    需要 pre-commit 环境中安装 ``reuse>=6.0.0``。

    | 情形 | 示例 |
    |------|------|
    | ✅（添加头部）       | ``acl.spec`` 无 SPDX 头 → 自动添加 |
    | ✅（已有跳过）       | ``bash.spec`` 已有 SPDX 头 → 跳过 |
    """
    hook_id = "reuse-add-annotate"
    description = "Add REUSE license headers to .spec files"

    DEFAULT_HOLDERS: ClassVar[List[str]] = [
        "Institute of Software, Chinese Academy of Sciences (ISCAS)",
        "openRuyi Project Contributors",
    ]
    DEFAULT_LICENSE: ClassVar[str] = "MulanPSL-2.0"

    @staticmethod
    def _get_first_git_year(file_path: Path) -> int:
        """Get the year of the first git commit for a file."""
        try:
            res = subprocess.run(
                ["git", "log", "--reverse", "--format=%ad", "--date=format:%Y", "--", str(file_path)],
                capture_output=True, text=True, timeout=3,
            )
            if res.returncode == 0:
                first_year = res.stdout.strip().split("\n")[0]
                if first_year.isdigit():
                    return int(first_year)
        except Exception:
            pass
        return datetime.now().year

    def check_file(self, relpath: Path) -> None:
        abspath = self.repo_root / relpath
        if not abspath.exists() or abspath.suffix != ".spec":
            return

        try:
            original = abspath.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            return

        # Skip if already has REUSE header
        try:
            from reuse.extract import contains_reuse_info
            if contains_reuse_info(original):
                return
        except ImportError:
            print("Error: REUSE library not available. Install with: pip install reuse>=6.0.0", file=sys.stderr)
            return

        try:
            from reuse.header import add_new_header
            from reuse.comment import PythonCommentStyle
            from reuse.copyright import CopyrightNotice, ReuseInfo, SpdxExpression, YearRange, CopyrightPrefix
        except ImportError as e:
            print(f"Error: REUSE API missing: {e}", file=sys.stderr)
            return

        year = self._get_first_git_year(abspath)
        year_range = YearRange(start=str(year), separator=None, end=None)
        new_notices = {
            CopyrightNotice(name=holder, prefix=CopyrightPrefix.SPDX_C, years=(year_range,))
            for holder in self.DEFAULT_HOLDERS
        }
        new_info = ReuseInfo(
            copyright_notices=new_notices,
            spdx_expressions={SpdxExpression(self.DEFAULT_LICENSE)},
            contributor_lines=[],
        )

        try:
            final_content = add_new_header(original, new_info, style=PythonCommentStyle)
        except Exception as e:
            print(f"Error adding header to {relpath}: {e}", file=sys.stderr)
            return

        if final_content.strip() != original.strip():
            abspath.write_text(final_content, encoding="utf-8")
            print(f"Added REUSE header to {relpath}")


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
