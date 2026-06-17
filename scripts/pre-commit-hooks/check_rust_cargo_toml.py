#!/usr/bin/env python3

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

from pathlib import Path
import re
import sys
import tomllib


CRATE_TAG_RE = re.compile(r"^(BuildRequires|Requires|Provides)\s*:.*crate\(")


def find_repo_root() -> Path:
    script_path = Path(__file__).resolve()
    for parent in script_path.parents:
        if (parent / "SPECS").is_dir() and (parent / "scripts" / "pre-commit-hooks").is_dir():
            return parent
    return script_path.parents[2]


def get_existing_repo_path(arg: str, repo_root: Path) -> Path | None:
    path = Path(arg)
    if path.is_absolute():
        candidate = path
    else:
        repo_candidate = repo_root / path
        cwd_candidate = Path.cwd() / path
        candidate = cwd_candidate if cwd_candidate.exists() else repo_candidate

    if not candidate.exists():
        return None

    try:
        return candidate.resolve().relative_to(repo_root)
    except ValueError:
        return None


def is_cargo_toml_path(path: Path) -> bool:
    return (
        len(path.parts) == 3
        and path.parts[0] == "SPECS"
        and path.name == "Cargo.toml"
    )


def is_spec_path(path: Path) -> bool:
    return (
        len(path.parts) == 3
        and path.parts[0] == "SPECS"
        and path.suffix == ".spec"
    )


def spec_uses_crate_tag(spec_path: Path) -> bool:
    with spec_path.open(encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            if CRATE_TAG_RE.search(stripped):
                return True
    return False


def main() -> int:
    repo_root = find_repo_root()
    if not sys.argv[1:]:
        print("no files to check")
        return 0

    cargo_tomls = set()
    spec_files = set()
    errors = []

    for arg in sys.argv[1:]:
        repo_path = get_existing_repo_path(arg, repo_root)
        if repo_path is None:
            continue
        if is_cargo_toml_path(repo_path):
            cargo_tomls.add(repo_path)
        elif is_spec_path(repo_path):
            spec_files.add(repo_path)

    for cargo_toml in sorted(cargo_tomls):
        cargo_toml_path = repo_root / cargo_toml
        try:
            with cargo_toml_path.open("rb") as f:
                tomllib.load(f)
        except (tomllib.TOMLDecodeError, UnicodeDecodeError, OSError) as e:
            errors.append(f"{cargo_toml}: {e}")

    for spec_file in sorted(spec_files):
        spec_path = repo_root / spec_file
        try:
            uses_crate_tag = spec_uses_crate_tag(spec_path)
        except (UnicodeDecodeError, OSError) as e:
            errors.append(f"{spec_file}: {e}")
            continue

        if uses_crate_tag and not (spec_path.parent / "Cargo.toml").is_file():
            errors.append(
                f"{spec_file}: uses crate(...) in BuildRequires/Requires/Provides "
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


if __name__ == "__main__":
    sys.exit(main())
