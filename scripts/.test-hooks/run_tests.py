#!/usr/bin/env python3
"""Comprehensive test runner for all 12 pre-commit hooks."""
import subprocess
import sys
import shutil
import atexit
from pathlib import Path

ROOT = Path(".")
SPECS = ROOT / "SPECS"
TEST_SPECS = Path("scripts/.test-hooks/SPECS/test-pkg")
PYTHON = sys.executable
RUNNER = "scripts/pre-commit.py"

# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
total = 0
passed = 0
failed = 0

# temp dirs/files to clean up
_cleanup_dirs = []
_cleanup_files = []

def register_cleanup_dir(d):
    _cleanup_dirs.append(d)

def register_cleanup_file(f):
    _cleanup_files.append(f)

@atexit.register
def cleanup():
    for f in _cleanup_files:
        try:
            if f.exists():
                f.unlink()
        except Exception:
            pass
    for d in _cleanup_dirs:
        try:
            if d.exists():
                shutil.rmtree(d)
        except Exception:
            pass

def run_hook(hook, filepath, expect_pass, desc):
    global total, passed, failed
    total += 1
    r = subprocess.run([PYTHON, RUNNER, hook, str(filepath)], capture_output=True, text=True)
    actual_pass = (r.returncode == 0)
    ok = (actual_pass == expect_pass)
    expected_label = "PASS" if expect_pass else "FAIL"
    actual_label = "PASS" if actual_pass else "FAIL"
    status = "OK" if ok else "FAIL"
    pname = Path(filepath).name
    print(f"  [{status}] {hook:32s} | {pname:28s} | expected={expected_label:4s} actual={actual_label:4s} | {desc}")
    if not ok and r.stderr.strip():
        for line in r.stderr.strip().split("\n")[:2]:
            print(f"         -> {line[:130]}")
    if ok: passed += 1
    else: failed += 1

print("=" * 70)
print("PRE-COMMIT HOOKS — COMPREHENSIVE TEST RESULTS")
print("=" * 70)

# ====== pygrep hooks (path-agnostic) ======
run_hook("no-group-tag",              TEST_SPECS / "group-pass.spec",              True,  "no Group tag")
run_hook("no-group-tag",              TEST_SPECS / "group-fail.spec",              False, "Group: tag present")
run_hook("autorelease",               TEST_SPECS / "autorelease-pass.spec",        True,  "no %autorelease")
run_hook("autorelease",               TEST_SPECS / "autorelease-fail.spec",        False, "%autorelease used")
run_hook("autochangelog",             TEST_SPECS / "autochangelog-pass.spec",      True,  "manual changelog")
run_hook("autochangelog",             TEST_SPECS / "autochangelog-fail.spec",      False, "%autochangelog used")
run_hook("check-files-pkgconfig-file", TEST_SPECS / "pkgconfig-explicit-pass.spec", True,  "explicit .pc filenames")
run_hook("check-files-pkgconfig-file", TEST_SPECS / "pkgconfig-wildcard-fail.spec", False, "wildcard in pkgconfig path")
run_hook("format-spacing",            TEST_SPECS / "spacing-pass.spec",            True,  "correct spacing")
run_hook("format-spacing",            TEST_SPECS / "spacing-fail.spec",            False, "incorrect spacing")

# ====== check-autotools-buildrequires (any .spec file) ======
run_hook("check-autotools-buildrequires", TEST_SPECS / "autotools-all-deps-pass.spec",      True,  "all 3 deps present")
run_hook("check-autotools-buildrequires", TEST_SPECS / "autotools-buildsystem-pass.spec",    True,  "BuildSystem: autotools")
run_hook("check-autotools-buildrequires", TEST_SPECS / "autotools-no-autoreconf-pass.spec",  True,  "no autoreconf call")
run_hook("check-autotools-buildrequires", TEST_SPECS / "autotools-missing-deps-fail.spec",   False, "autoreconf without deps")

# ====== sourcewithRemoteAsset (any .spec file) ======
run_hook("sourcewithRemoteAsset",     TEST_SPECS / "source-no-remoteasset-pass.spec",  True,  "no remote source")
run_hook("sourcewithRemoteAsset",     TEST_SPECS / "source-remoteasset-fail.spec",      False, "remote source missing #!RemoteAsset")
run_hook("sourcewithRemoteAsset",     TEST_SPECS / "source-remoteasset-valid-pass.spec", True,  "remote source with valid #!RemoteAsset")

# ====== reuse-add-annotate (any .spec file, requires reuse library) ======
run_hook("reuse-add-annotate",        TEST_SPECS / "reuse-test.spec",                  True,  "spec without REUSE header (auto-add)")

# ====== path-sensitive hooks — use files under real SPECS/ ======

# no-entries-directly-under-SPECS: must match ^SPECS/[^/]+$
tmp_f = SPECS / "_test_loose_file.txt"
tmp_f.write_text("temp", encoding="utf-8"); register_cleanup_file(tmp_f)
run_hook("no-entries-directly-under-SPECS", tmp_f, False, "loose file under real SPECS/")

# existing SPECS subdirectories have files → that's PASS
run_hook("no-entries-directly-under-SPECS", SPECS / "acl" / "acl.spec", True, "spec inside SPECS subdirectory")

# dont-add-constraints-to-repo: must match ^SPECS/.*/_constraints$
tmp_d = SPECS / "_test_constraints_pkg"
tmp_d.mkdir(exist_ok=True); register_cleanup_dir(tmp_d)
tmp_c = tmp_d / "_constraints"; tmp_c.write_text("temp", encoding="utf-8"); register_cleanup_file(tmp_c)
run_hook("dont-add-constraints-to-repo", tmp_c, False, "_constraints in SPECS subdir")

# dont-add-constraints: regular file = pass
run_hook("dont-add-constraints-to-repo", SPECS / "acl" / "acl.spec", True, "regular spec, not _constraints")

# check-rust-cargo-toml: must be SPECS/<pkg>/(Cargo.toml|*.spec)
# pass: valid Cargo.toml
rust_pass_dir = SPECS / "_test_rust_pass"; register_cleanup_dir(rust_pass_dir)
rust_pass_dir.mkdir(exist_ok=True)
ct_pass = rust_pass_dir / "Cargo.toml"
ct_pass.write_text('[package]\nname = "test"\nversion = "0.1.0"\nedition = "2021"\n', encoding="utf-8")
run_hook("check-rust-cargo-toml", ct_pass, True, "valid Cargo.toml in SPECS/<pkg>/")

# fail: invalid Cargo.toml
rust_fail_dir = SPECS / "_test_rust_fail"; register_cleanup_dir(rust_fail_dir)
rust_fail_dir.mkdir(exist_ok=True)
ct_fail = rust_fail_dir / "Cargo.toml"
ct_fail.write_text('[package\nname = broken\n', encoding="utf-8")
run_hook("check-rust-cargo-toml", ct_fail, False, "invalid TOML in SPECS/<pkg>/Cargo.toml")

# check-rust-cargo-toml: spec with crate() but no Cargo.toml
rust_no_ct_dir = SPECS / "_test_rust_no_ct"; register_cleanup_dir(rust_no_ct_dir)
rust_no_ct_dir.mkdir(exist_ok=True)
spec_no_ct = rust_no_ct_dir / "rust-foo.spec"
spec_no_ct.write_text("Name: rust-foo\nBuildRequires:  crate(serde)\n", encoding="utf-8")
run_hook("check-rust-cargo-toml", spec_no_ct, False, "crate() in spec but missing Cargo.toml")

# python-name: must match SPECS/python-<name> pattern
# pass: valid python name
py_pass_dir = SPECS / "python-test-valid"; register_cleanup_dir(py_pass_dir)
py_pass_dir.mkdir(exist_ok=True)
py_pass_spec = py_pass_dir / "python-test-valid.spec"
py_pass_spec.write_text("Name: python-test-valid\n", encoding="utf-8")
run_hook("python-name", py_pass_spec, True, "valid PEP 503 python spec name")

# fail: invalid python name (uppercase)
py_fail_dir = SPECS / "python-InValid"; register_cleanup_dir(py_fail_dir)
py_fail_dir.mkdir(exist_ok=True)
py_fail_spec = py_fail_dir / "python-InValid.spec"
py_fail_spec.write_text("Name: python-InValid\n", encoding="utf-8")
run_hook("python-name", py_fail_spec, False, "invalid python spec name (uppercase)")

# ====== SUMMARY ======
print()
print(f"  Total: {total}  Passed: {passed}  Failed: {failed}")
print("=" * 70)
sys.exit(0 if failed == 0 else 1)
