<!--
SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
SPDX-License-Identifier: MulanPSL-2.0
-->

# openRuyi installed-test runner pilot

`openruyi-test` defines the first version of the package-test command line
contract used by the pilot packages.

## Commands

```text
openruyi-test list PACKAGE
openruyi-test list PACKAGE --json
openruyi-test run PACKAGE [--test ID] [--match GLOB]
openruyi-test run PACKAGE --all
pkg-test list
pkg-test info PACKAGE
pkg-test run PACKAGE --filter unit --output ./results
```

The runner discovers freedesktop installed-test descriptors below
`/usr/share/installed-tests/PACKAGE/*.test`. Other build systems can install a
versioned manifest at `/usr/share/openruyi-tests/v1/PACKAGE.json`.

Each test runs as the invoking user in a separate process group and gets a
separate writable `TEST-ID.work` directory inside the result directory. The
runner enforces a per-test timeout, preserves stdout and stderr, and writes
`results.json` below `$XDG_STATE_HOME/openruyi-tests/`. Exit status is zero when
at least one selected test passes without failures or execution errors, one
when a test fails or times out, 77 when all tests skip or an environment error
prevents execution, and two for invalid definitions, missing tests or usage.
`pkg-test` is an alias of `openruyi-test`; `--output` aliases `--log-dir`.
`--filter` selects test IDs containing a name; `--match` accepts shell patterns.
Manifest tests may declare `"default": false` for extended suites. A plain
`run` executes only default tests and records excluded IDs in `results.json`;
`--test`, `--match`, `--filter` or `--all` selects extended tests explicitly.
Reports include installed RPM versions, distribution, RPM architecture,
kernel, UID, command, allowed requirements, counts and the aggregate exit code.

Tests that declare `network`, `hardware` or `root` requirements are skipped
unless the corresponding `--allow` option is supplied. Root tests require
both explicit `--allow root` and effective UID 0.

## Staged payload checks

Set `OPENRUYI_TEST_ROOT` or use `--root` to inspect installed-test descriptors
inside an extracted RPM root. Executables below `/usr/libexec` are resolved
inside that root, which permits list and selected execution checks before the
RPM is published.

## Pilot package

The first package is `gdk-pixbuf-tests`. Its upstream Meson build installs
test executables and data in `/usr/libexec/installed-tests/gdk-pixbuf/` and
descriptors in `/usr/share/installed-tests/gdk-pixbuf/`. No package-specific
adapter is needed.
