# openRuyi Developer Guide

This guide helps developers set up their local environment and understand the development workflow for contributing to openRuyi.

---

## Table of Contents

- [Setting Up pre-commit Hooks](#setting-up-pre-commit-hooks)
- [Running Checks Locally](#running-checks-locally)
- [Available Hook Reference](#available-hook-reference)
- [Skipping Checks (Emergency)](#skipping-checks-emergency)
- [Hook Types in This Project](#hook-types-in-this-project)
- [CI Integration](#ci-integration)
- [Extending pre-commit Hooks](#extending-pre-commit-hooks)

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

---

## Extending pre-commit Hooks

This project uses a class-based hook architecture in `scripts/pre-commit.py`.
Adding a new check is straightforward — choose the right base class and follow
the patterns below.

### Architecture Overview

```
BaseHook                          ← root: hook_id, check_file(), run()
├── PygrepHook                    ← regex-based content check
│   ├── NoGroupTag
│   ├── Autorelease
│   ├── CheckFilesPkgconfigFile
│   ├── Autochangelog
│   └── FormatSpacing
├── FailHook                      ← filename/path pattern check
│   ├── PythonName
│   ├── NoEntriesUnderSpecs
│   └── DontAddConstraints
└── BaseHook (custom)             ← complex multi-file logic
    ├── CheckAutotoolsBuildRequires
    ├── SourceWithRemoteAsset
    ├── CheckRustCargoToml
    └── ReuseAddAnnotate
```

| Method | When to override | Default behavior |
|--------|-----------------|------------------|
| `check_file(relpath)` | **Always** (unless hook is batch-only) | `NotImplementedError` |
| `run(files)` | Batch/multi-file checks | Iterates `check_file()` over all files |

### Hook Registration Checklist

After writing your Hook class, register it in **two places**:

1. **`.pre-commit-config.yaml`** — add a `repo: local` entry
2. **No other file needed** — `scripts/pre-commit.py` auto-discovers hooks by `hook_id`

---

### Pattern 1: Pygrep-Style Hook (~5 lines)

Use when: you want to search for a regex in each `.spec` file and report every
match as an error (or require a pattern to be present).

**Base class:** `PygrepHook`

**Class variables to set:**

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `hook_id` | `str` | ✅ | Unique ID, matches `.pre-commit-config.yaml` `id` field |
| `description` | `str` | ✅ | One-line description for logging |
| `pattern` | `str` | ✅ | Python regex to search for |
| `error_fmt` | `str` | ✅ | Error message template with `{file}`, `{line}`, `{msg}`, `{RED}`, `{YELLOW}`, `{RESET}` |
| `negate` | `bool` | ❌ | If `True`, fail when pattern is **not** found (default: `False`) |
| `multiline` | `bool` | ❌ | If `True`, search across lines with `re.DOTALL` (default: `False`) |

**Example: adding a "no deprecated `%defattr`" check**

```python
class NoDefattr(PygrepHook):
    """
    Verifies that RPM spec files do NOT use the deprecated ``%defattr`` macro.

    | What | Example |
    |------|---------|
    | ❌ rejected | ``%defattr(-,root,root)`` |
    | ✅ accepted | no ``%defattr`` line |
    """
    hook_id = "no-defattr"
    description = "check no %defattr macro"
    pattern = r"^%defattr"
    error_fmt = "{file}:{line}: {RED}error{RESET} - %defattr is deprecated, remove it"
```

Then register in `.pre-commit-config.yaml`:

```yaml
- id: no-defattr
  name: "check no %defattr macro"
  language: python
  entry: scripts/pre-commit.py no-defattr
  files: \.spec$
  pass_filenames: true
```

**Negate example: requiring a mandatory line**

Use `negate = True` when a file **must** contain a pattern. For example, requiring
every spec to have a `License:` tag:

```python
class RequireLicense(PygrepHook):
    """Fail if no ``License:`` line is found in the spec."""
    hook_id = "require-license"
    description = "require License tag"
    pattern = r"^License:"
    negate = True    # fail when NOT found
    error_fmt = "{file}: {YELLOW}warning{RESET} - missing License tag"
```

**Multiline example: searching across the whole file**

Set `multiline = True` when your pattern needs to match across line boundaries.
For instance, checking if `%changelog` contains `%autochangelog`:

```python
class Autochangelog(PygrepHook):
    hook_id = "autochangelog"
    description = "check autochangelog macro"
    pattern = r"%changelog\s+%autochangelog"
    multiline = True
    error_fmt = "{file}: {RED}error{RESET} - %autochangelog is not allowed"
```

---

### Pattern 2: FailHook — Filename / Path Validation (~5 lines)

Use when: you want to fail if a **file path** (not file content) matches a regex.

**Base class:** `FailHook`

**Class variables to set:**

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `hook_id` | `str` | ✅ | Unique ID |
| `description` | `str` | ✅ | One-line description |
| `pattern` | `str` | ✅ | Regex matched against the repo-relative path |
| `message` | `str` | ✅ | Error message shown to user |

**Example: preventing `.spec` files outside `SPECS/`**

```python
class NoSpecOutsideSpecs(FailHook):
    """
    Ensures all ``.spec`` files live under ``SPECS/``.

    | What | Example |
    |------|---------|
    | ❌ rejected | ``scripts/test.spec`` |
    | ✅ accepted | ``SPECS/acl/acl.spec`` |
    """
    hook_id = "no-spec-outside-specs"
    description = ".spec files must be under SPECS/"
    pattern = r"^(?!SPECS/).*\.spec$"
    message = ".spec files must be placed under SPECS/<pkgname>/"
```

Register:

```yaml
- id: no-spec-outside-specs
  name: ".spec files must be under SPECS/"
  language: python
  entry: scripts/pre-commit.py no-spec-outside-specs
  files: \.spec$
  pass_filenames: true
```

**How `files` filter + `pattern` work together:**

The `files:` field in `.pre-commit-config.yaml` (pre-commit's built-in filter)
narrows which changed files are passed to the hook. The `pattern` class variable
then does a second check inside the hook itself. This two-layer design means:

- Use `files:` to restrict which files the hook runs on (performance)
- Use `pattern` for the actual validation logic

For example, the `no-entries-directly-under-SPECS` hook uses
`files: '^SPECS/[^/]+$'` so it only receives files that are direct children of
`SPECS/`, and its `pattern` matches all of them (they are all errors).

---

### Pattern 3: Custom Hook with `check_file()` (~20 lines)

Use when: the check logic is more complex than a single regex — you need to
read the file, parse multiple lines, or check context around matches.

**Base class:** `BaseHook`

**Required:** override `check_file(self, relpath: Path) -> None`

**Key attributes available inside `check_file()`:**

| Attribute | Type | Description |
|-----------|------|-------------|
| `self.repo_root` | `Path` | Repository root directory |
| `self.errors` | `List[str]` | Append error strings here |
| `relpath` | `Path` | Repo-relative path to the file being checked |

**Example: checking if `autoreconf` usage has all required `BuildRequires`**

```python
import re

class CheckAutotoolsBuildRequires(BaseHook):
    """
    When a spec runs ``autoreconf``, it must declare three BuildRequires:
    ``autoconf``, ``automake``, and ``libtool``.

    | What | Example |
    |------|---------|
    | ❌ rejected | ``autoreconf`` present but missing ``BuildRequires: automake`` |
    | ✅ accepted | all three BuildRequires declared |
    | ✅ accepted | no ``autoreconf`` call (not an autotools package) |
    """
    hook_id = "check-autotools-buildrequires"
    description = "check autotools build requirements"

    AUTORECONF_RE = re.compile(r"^\s*autoreconf\b", re.M)
    REQUIRED = {"autoconf", "automake", "libtool"}

    def check_file(self, relpath: Path) -> None:
        abspath = self.repo_root / relpath
        try:
            content = abspath.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            return

        # Only check if the spec uses autoreconf
        if not self.AUTORECONF_RE.search(content):
            return

        # Check if BuildSystem: autotools covers it
        if re.search(r"^BuildSystem:\s*autotools", content, re.M):
            return

        # Collect declared BuildRequires
        declared = set()
        for m in re.finditer(r"^BuildRequires:\s*(\S+)", content, re.M):
            declared.add(m.group(1))

        missing = self.REQUIRED - declared
        if missing:
            self.errors.append(
                f"{relpath}: autoreconf requires BuildRequires: "
                + ", ".join(sorted(missing))
            )
```

**Pattern for reading files safely:**

```python
def check_file(self, relpath: Path) -> None:
    abspath = self.repo_root / relpath
    try:
        content = abspath.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return   # skip unreadable files silently
```

**Color constants available for error messages:**

| Constant | ANSI Code | Use for |
|----------|-----------|---------|
| `RED` | `\033[1;31m` | Error labels |
| `YELLOW` | `\033[33m` | Warning labels |
| `RESET` | `\033[0m` | End of colored segment |

```python
self.errors.append(
    f"{relpath}: {RED}error{RESET} - check failed for reason X\n"
    f"  -> offending line: {line_content}"
)
```

---

### Pattern 4: Batch / Multi-File Hook

Use when: your check needs to see **all files at once** — cross-file validation,
directory-level checks, or aggregating data across multiple files.

**Base class:** `BaseHook`

**Required:** override `run(self, files: List[Path]) -> int`

**Important:** return `0` for pass, `1` for fail. Errors must be printed to
`sys.stderr` yourself (the default `check_file()`-based `run()` does this
automatically, but a custom `run()` must do it manually).

**Example: `CheckRustCargoToml` — validates Cargo.toml and checks for crate references**

This hook does two things:
1. Validates every `Cargo.toml` under `SPECS/<pkg>/` is valid TOML
2. If a spec uses `crate(...)` in `BuildRequires`/`Requires`/`Provides`,
   ensures a `Cargo.toml` exists in the same directory

```python
import sys
import tomllib

class CheckRustCargoToml(BaseHook):
    """
    For Rust crate packages:
    1. Every ``Cargo.toml`` in ``SPECS/<pkg>/`` is valid TOML.
    2. If a spec uses ``crate(...)``, a ``Cargo.toml`` must exist.
    """
    hook_id = "check-rust-cargo-toml"
    description = "Check Cargo.toml for crate related specs"

    CRATE_TAG_RE = re.compile(r"^(BuildRequires|Requires|Provides)\s*:.*crate\(")

    def run(self, files: List[Path]) -> int:
        cargo_tomls: List[Path] = []
        spec_files: List[Path] = []

        # Phase 1: classify files by type
        for f in files:
            parts = f.parts
            if len(parts) == 3 and parts[0] == "SPECS" and parts[-1] == "Cargo.toml":
                cargo_tomls.append(f)
            elif len(parts) == 3 and parts[0] == "SPECS" and f.suffix == ".spec":
                spec_files.append(f)

        errors: List[str] = []

        # Phase 2: validate all Cargo.toml files
        for ct in sorted(cargo_tomls):
            try:
                with (self.repo_root / ct).open("rb") as fh:
                    tomllib.load(fh)
            except Exception as e:
                errors.append(f"{ct}: {e}")

        # Phase 3: check crate references against Cargo.toml existence
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
                    f"{sf}: uses crate(...) but missing Cargo.toml"
                )

        if errors:
            print("\n".join(errors), file=sys.stderr)
            return 1
        return 0
```

**Key patterns for batch hooks:**

1. **Classify files first** — separate files by type/path pattern
2. **Collect all errors** — don't exit early; report all issues at once
3. **Print errors manually** — `print("\n".join(errors), file=sys.stderr)` then `return 1`
4. **Return code** — `0` = pass, `1` = fail

---

### Pattern 5: Auto-Fix Hook (`--fix` mode)

Some hooks (like `reuse-add-annotate`) can automatically fix issues instead of
just reporting them. This is an optional pattern you can add to any hook.

**How it works:**

1. Add a class variable `supports_fix = True`
2. Implement a `fix_file(self, relpath: Path) -> bool` method that returns
   `True` if the file was modified
3. The hook auto-detects `--fix` from the command line (already handled by
   `main()` in `pre-commit.py` — you just need to implement the method)

**Example sketch:**

```python
class TrailingWhitespaceFixer(BaseHook):
    """Strip trailing whitespace from .spec files."""
    hook_id = "fix-trailing-ws"
    description = "remove trailing whitespace"
    supports_fix = True

    def check_file(self, relpath: Path) -> None:
        abspath = self.repo_root / relpath
        try:
            lines = abspath.read_text(encoding="utf-8").splitlines(keepends=True)
        except (OSError, UnicodeDecodeError):
            return
        for i, line in enumerate(lines, 1):
            if line.rstrip("\n").rstrip("\r\n") != line.rstrip("\n").rstrip("\r\n").rstrip():
                self.errors.append(f"{relpath}:{i}: trailing whitespace")

    def fix_file(self, relpath: Path) -> bool:
        abspath = self.repo_root / relpath
        try:
            content = abspath.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            return False
        fixed = "\n".join(line.rstrip() for line in content.splitlines())
        if fixed != content.rstrip("\n"):
            abspath.write_text(fixed + "\n", encoding="utf-8")
            return True
        return False
```

---

### Performance Optimization Tips

1. **Use `files:` filter aggressively** — the `.pre-commit-config.yaml` `files:`
   pattern runs before the hook, filtering out irrelevant files early.

2. **Skip unreadable files immediately** — always wrap `read_text()` in try/except:

   ```python
   try:
       content = abspath.read_text(encoding="utf-8")
   except (OSError, UnicodeDecodeError):
       return
   ```

3. **Compile regexes once** — use `ClassVar` or module-level constants:

   ```python
   class MyHook(BaseHook):
       MY_RE = re.compile(r"pattern", re.M)   # compiled once at class definition
   ```

4. **For batch hooks, consider parallel processing** — if `check_file()` is
   CPU-intensive, use `concurrent.futures` in a custom `run()`:

   ```python
   from concurrent.futures import ThreadPoolExecutor, as_completed

   def run(self, files: List[Path]) -> int:
       with ThreadPoolExecutor() as executor:
           futures = {executor.submit(self.check_one, f): f for f in files}
           for future in as_completed(futures):
               err = future.result()
               if err:
                   self.errors.append(err)
       # ... print and return
   ```

5. **Prefer `check_file()` over `run()` when possible** — the default `run()`
   implementation already handles error collection and output formatting.
   Only override `run()` when you genuinely need cross-file logic.

---

### Quick Reference: Choosing the Right Base Class

| I want to... | Use | Override | Lines of code |
|-------------|-----|----------|---------------|
| Search for a regex in file content | `PygrepHook` | Nothing (set class vars) | ~8 |
| Search multiple lines with one regex | `PygrepHook` | Set `multiline = True` | ~10 |
| Require a pattern to be present | `PygrepHook` | Set `negate = True` | ~10 |
| Validate filename/path | `FailHook` | Nothing (set class vars) | ~8 |
| Parse file and check context | `BaseHook` | `check_file()` | ~30 |
| Cross-file or directory-level check | `BaseHook` | `run()` | ~50 |
| Auto-fix issues | `BaseHook` | `check_file()` + `fix_file()` | ~40 |
| Check file existence + content | `BaseHook` | `run()` | ~60 |
