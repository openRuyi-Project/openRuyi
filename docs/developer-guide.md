# openRuyi Developer Guide

This guide helps developers set up their local environment and understand the development workflow for contributing to openRuyi.

---

## Table of Contents

- [Setting Up pre-commit Hooks](#setting-up-pre-commit-hooks)
- [Running Checks Locally](#running-checks-locally)
- [Available Hook Reference](#available-hook-reference)
- [Skipping Checks (Emergency)](#skipping-checks-emergency)
- [Hook Types in This Project](#hook-types-in-this-project)

---

## Setting Up pre-commit Hooks

This project uses [pre-commit](https://pre-commit.com/) to enforce code quality and consistency rules on `.spec` files before every commit.

### Prerequisites

- Python 3 installed on your system

### Install pre-commit

```bash
pip install pre-commit
```

### Install the Git Hooks (one-time setup)

Run this in the repository root:

```bash
pre-commit install
```

This creates a script at `.git/hooks/pre-commit` that will automatically run all checks whenever you run `git commit`.

After installation, every `git commit` will trigger the checks defined in `.pre-commit-config.yaml`:

```
git commit
    │
    └── git triggers pre-commit hook
            │
            └── pre-commit reads .pre-commit-config.yaml
                    │
                    ├── Runs each hook against changed files
                    │   ├── no-group-tag (grep)
                    │   ├── autorelease (grep)
                    │   ├── trailing-whitespace
                    │   └── ...
                    │
                    └── All pass ✅ → commit succeeds
                         Any fail ❌ → commit is blocked
```

---

## Running Checks Locally

You can run pre-commit checks manually without committing:

```bash
# Check all files in the repository
pre-commit run --all-files

# Check only specific files
pre-commit run --files SPECS/acl/acl.spec

# Check only staged (changes to-be-committed) files
pre-commit run
```

### Common Commands

| Command | Description |
|---------|-------------|
| `pre-commit install` | Install hook into `.git/hooks/` (first time) |
| `pre-commit run --all-files` | Run all hooks on every file |
| `pre-commit run` | Run only on currently staged files |
| `pre-commit autoupdate` | Update hook versions to latest |
| `pre-commit clean` | Clear pre-commit cache |
| `pre-commit uninstall` | Remove the hook from `.git/hooks/` |

---

## Skipping Checks (Emergency)

If you need to bypass the checks for an urgent commit, use:

```bash
git commit -m "urgent fix" --no-verify
```

> **Note:** CI (the `Lint` workflow) will still run these checks on PR. Skipping locally does not bypass CI gates.

---

## Hook Types in This Project

All local hooks are defined in `.pre-commit-config.yaml` and routed through
a single unified runner: `scripts/pre-commit.py <hook-id>`.

```yaml
# Example — all local hooks follow this pattern:
- id: no-group-tag
  name: "Check no Group tag"
  language: python
  entry: scripts/pre-commit.py no-group-tag
  files: \.spec$
  pass_filenames: true
```

The `pre-commit.py` runner implements 11 checks across three internal categories:

| Category | Hooks | Description |
|----------|-------|-------------|
| **pygrep-style** | `no-group-tag`, `autorelease`, `check-files-pkgconfig-file`, `autochangelog`, `format-spacing` | Regex-based content checks on `.spec` files |
| **fail-style** | `python-name`, `no-entries-directly-under-SPECS`, `dont-add-constraints-to-repo` | Filename/path pattern validation |
| **python-script** | `sourcewithRemoteAsset`, `check-rust-cargo-toml`, `reuse-add-annotate` | Custom Python logic (checksum verification, TOML validation, license header injection) |

### Remote hooks

Retrieved from external repositories and cached locally on first run.

```yaml
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: v6.0.0
  hooks:
    - id: trailing-whitespace
```

---

## CI Integration

The same `.pre-commit-config.yaml` is also used by the `Lint` GitHub Actions workflow (`.github/workflows/lint.yml`). This means checks run both:

- **Locally** — via `pre-commit` tool or `git commit` hook
- **In CI** — automatically on every pull request to `main` or `ci-test`

The configuration file is shared, so local and CI checks are always in sync.
