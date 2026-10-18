<!-- SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS) -->
<!-- SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors -->
<!-- -->
<!-- SPDX-License-Identifier: MulanPSL-2.0 -->

# Using `scan-check.py`

`scan-check.py` reports whether each package SPEC has an effective `%check`
section for a selected RPM target. When you supply an external inventory, it
also reports whether each package includes RISC-V platform tests.

The scanner uses `rpmspec --parse` rather than source-text matching. RPM can
generate a `%check` stage from a declarative `BuildSystem:`, and it evaluates
architecture and build conditionals for the selected target.

## Requirements

The `scan-check.py` script requires these components to function:

- `Python` 3.10 or newer: Running the scanner
- `rpmspec` from RPM 4.20 or newer: Parsing SPEC files and materializing
  declarative `BuildSystem` sections
- openRuyi macro packages: Providing the macro definitions used by the target
  repository

At minimum, install the macro packages that provide the BuildSystems being
scanned, including `rpm-config-openruyi`, `pyproject-rpm-macros`,
`go-rpm-macros`, `rust-rpm-macros`, `perl-rpm-macros`, and
`cmake-rpm-macros`. If your checkout uses additional BuildSystems, install
their macro packages as well.

The safest way to obtain a compatible macro environment is to run the scanner
inside the openRuyi build environment or container used for package builds.

## Security note

`scan-check.py` expands SPEC macros with `rpmspec`. RPM Lua and `%(...)`
shell expansion can execute commands during parsing. The scanner is not a
sandbox. Do not run it on untrusted SPEC files without review or adequate
protection.

## Local usage

By default, `scan-check.py` scans `SPECS/` and performs these actions:

- Find exactly one `.spec` file in each package directory under `SPECS/`.
- Expand each SPEC with `rpmspec --parse --target riscv64`.
- Write a sorted CSV report to standard output.
- Write a scan summary to standard error.

From the repository root:

```bash
python3 scripts/scan-check.py --output check-riscv64.csv
```

Use these options to adjust the scan:

| Option | Effect |
| --- | --- |
| `--target ARCH` | Select another RPM target. |
| `--specs PATH` | Scan another checkout with the `SPECS/<package>/` layout. |
| `--output PATH` | Write the CSV to a file instead of standard output. |
| `--jobs COUNT` | Limit parallel `rpmspec` processes. Use `--jobs 1` on a slow system. |
| `--define 'MACRO EXPR'` | Pass an extra macro definition to `rpmspec`. The option can be repeated. |
| `--rpmspec PATH` | Use an alternative `rpmspec` executable. |
| `--keep-going` | Write parse failures to the CSV and continue; the command can then return zero. |

For details on all options, see:

```bash
python3 scripts/scan-check.py --help
```

### Minimal OCI rootfs

A minimal OCI rootfs may not inherit every macro from the repository build
configuration. If parsing fails in Python interpreter detection or
dependency-query macros, suppress those non-check macros for the static scan:

```bash
python3 scripts/scan-check.py \
  --define '%__python /usr/bin/python3' \
  --define 'requires_eq() %{nil}' \
  --define 'requires_ge() %{nil}' \
  --output check-riscv64.csv
```

These definitions avoid requiring every runtime dependency to be installed in
the scanning rootfs. They do not suppress an effective `%check` section.

### RISC-V platform tests

The scanner deliberately does not guess binary-package-to-source-package
relationships for an external test inventory. Normalize that inventory to
openRuyi source package names before passing it to `--test-packages`. Each
line MUST contain one package name:

```text
# comments are ignored
acl
curl
openssh
```

```bash
python3 scripts/scan-check.py \
  --test-packages riscv-platform-test-packages.txt \
  --output package-check-report.csv
```

## Output

The CSV report contains these columns:

| Column | Values | Meaning |
| --- | --- | --- |
| `package` | Package name | Package directory name under `SPECS/`. |
| `check_enabled` | `Yes`, `No`, or `Error` | Whether an effective `%check` section was found or parsing failed. |
| `riscv_platform_tests` | `Yes`, `No`, or `Unknown` | Whether the package appears in the supplied test inventory. The value is `Unknown` without an inventory. |
| `state` | State name | Effective check state or parse result. |
| `detail` | Text | Parse error text, when applicable. |

The `state` column contains one of these values:

- `nonempty-check`: the parsed SPEC has a `%check` stage with at least one
  executable test action.
- `empty-check`: the parsed SPEC has `%check` stages, but all their actions are
  comments, blank lines, shell no-ops, or environment-only setup.
- `missing-check`: the parsed SPEC has no `%check` stage.
- `rpmspec-error`: `rpmspec` could not parse the SPEC.

RPM materializes BuildSystem-generated sections and resolves false
conditionals. The scanner unions all `%check` fragments emitted by `rpmspec`,
which preserves generated sections and append or prepend fragments. An
explicitly empty `%check` overrides a BuildSystem-generated check and therefore
remains disabled.

The result is a static interpretation of the SPEC and its macros. It does not
prove that a build service job ran `%check`, and it does not measure test depth
or classify individual test cases as skipped.

By default, the scanner exits non-zero if any SPEC cannot be parsed. With
`--keep-going`, parse failures remain in the CSV and the command can return
zero. Check the `errors=` count in the summary before using such a report as
complete.
