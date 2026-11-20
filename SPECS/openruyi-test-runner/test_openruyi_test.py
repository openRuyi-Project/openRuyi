# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

import importlib.util
from importlib.machinery import SourceFileLoader
import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path
from types import SimpleNamespace


SCRIPT = Path(__file__).resolve().with_name("openruyi-test")
if not SCRIPT.is_file():
    SCRIPT = Path(__file__).resolve().parents[1] / "openruyi-test"
LOADER = SourceFileLoader("openruyi_test", str(SCRIPT))
SPEC = importlib.util.spec_from_loader(LOADER.name, LOADER)
runner = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = runner
SPEC.loader.exec_module(runner)


class RunnerTests(unittest.TestCase):
    def test_staged_env_command_maps_fixture_and_executable_paths(self):
        command = ["/usr/bin/env", "G_TEST_SRCDIR=/usr/libexec/installed-tests/example",
                   "/usr/libexec/installed-tests/example/passes"]
        staged = runner.rewrite_staged_command(command, self.root)
        self.assertEqual(staged[0], "/usr/bin/env")
        self.assertEqual(staged[1], "G_TEST_SRCDIR=" + str(self.bin))
        self.assertEqual(staged[2], str(self.bin / "passes"))

    def test_root_requires_explicit_opt_in_even_when_privileged(self):
        case = runner.TestCase("example", "privileged", ["/bin/false"], 1, "test", ("root",))
        with patch.object(runner.os, "geteuid", return_value=0):
            result = runner.run_case(case, self.root / "logs", set())
        self.assertEqual(result["status"], "skip")

    def test_global_discovery_and_environment_exit_code(self):
        executable = self.executable("unavailable", "exit 77\n")
        self.descriptor("unavailable", executable)
        self.assertEqual(runner.installed_packages(self.root), ["example"])
        with contextlib.redirect_stdout(io.StringIO()):
            code = runner.main(["--root", str(self.root), "run", "example", "--filter", "avail",
                                "--output", str(self.root / "unavailable-run")])
        self.assertEqual(code, 77)
        report = json.loads((self.root / "unavailable-run/results.json").read_text())
        self.assertEqual(report["exit_code"], 77)
        self.assertEqual(report["counts"]["skip"], 1)

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.descriptors = self.root / "usr/share/installed-tests/example"
        self.descriptors.mkdir(parents=True)
        self.bin = self.root / "usr/libexec/installed-tests/example"
        self.bin.mkdir(parents=True)

    def tearDown(self):
        self.temp.cleanup()

    def executable(self, name, body):
        path = self.bin / name
        path.write_text("#!/bin/sh\n" + body, encoding="utf-8")
        path.chmod(0o755)
        return path

    def descriptor(self, name, executable, extra=""):
        (self.descriptors / f"{name}.test").write_text(
            f"[Test]\nType=session\nExec={executable}\n{extra}", encoding="utf-8"
        )

    def test_discovers_installed_test_descriptors(self):
        path = self.executable("passes", "exit 0\n")
        self.descriptor("passes", path, "Timeout=12\n")
        cases = runner.discover("example", self.root, 300)
        self.assertEqual([case.test_id for case in cases], ["passes"])
        self.assertEqual(cases[0].timeout, 12)

    def test_runs_pass_fail_skip_and_timeout_with_logs(self):
        definitions = {
            "passes": "echo passed\necho writable > created-in-workdir\nexit 0\n",
            "fails": "echo failed >&2\nexit 4\n",
            "skips": "exit 77\n",
            "slow": "sleep 2\n",
        }
        for name, body in definitions.items():
            path = self.executable(name, body)
            timeout = "Timeout=0.05\n" if name == "slow" else ""
            self.descriptor(name, path, timeout)
        cases = runner.discover("example", self.root, 1)
        logs = self.root / "logs"
        logs.mkdir()
        results = {case.test_id: runner.run_case(case, logs, set()) for case in cases}
        self.assertEqual(results["passes"]["status"], "pass")
        self.assertEqual(results["fails"]["status"], "fail")
        self.assertEqual(results["skips"]["status"], "skip")
        self.assertEqual(results["slow"]["status"], "timeout")
        self.assertEqual((logs / "passes.stdout.log").read_text().strip(), "passed")
        self.assertEqual((logs / "fails.stderr.log").read_text().strip(), "failed")
        self.assertEqual(
            (logs / "passes.work/created-in-workdir").read_text().strip(), "writable"
        )
        self.assertEqual(results["passes"]["working_directory"], str(logs / "passes.work"))

    def test_manifest_requirements_are_skipped_without_opt_in(self):
        manifest_dir = self.root / "usr/share/openruyi-tests/v1"
        manifest_dir.mkdir(parents=True)
        path = self.executable("network", "exit 0\n")
        (manifest_dir / "example.json").write_text(json.dumps({
            "schema_version": 1,
            "package": "example",
            "tests": [{
                "id": "network",
                "command": [str(path)],
                "timeout": 2,
                "requirements": ["network"],
            }],
        }), encoding="utf-8")
        case = runner.discover("example", self.root, 300)[0]
        result = runner.run_case(case, self.root / "logs", set())
        self.assertEqual(result["status"], "skip")
        self.assertIn("network", result["reason"])

    def test_nondefault_cases_require_explicit_selection(self):
        manifest_dir = self.root / "usr/share/openruyi-tests/v1"
        manifest_dir.mkdir(parents=True)
        passing = self.executable("passes", "exit 0\n")
        extended = self.executable("extended", "exit 4\n")
        (manifest_dir / "example.json").write_text(json.dumps({
            "schema_version": 1, "package": "example", "tests": [
                {"id": "passes", "command": [str(passing)]},
                {"id": "extended", "command": [str(extended)], "default": False},
            ]}), encoding="utf-8")
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(runner.main(["--root", str(self.root), "run", "example",
                                          "--output", str(self.root / "default-run")]), 0)
            self.assertEqual(runner.main(["--root", str(self.root), "run", "example",
                                          "--test", "extended", "--output",
                                          str(self.root / "extended-run")]), 1)
        report = json.loads((self.root / "default-run/results.json").read_text())
        self.assertEqual(report["excluded_from_default"], ["extended"])
        self.assertEqual(report["counts"]["pass"], 1)
        self.assertEqual([item["id"] for item in report["results"]], ["passes"])
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(runner.main(["--root", str(self.root), "run", "example",
                                          "--all", "--output", str(self.root / "all-run")]), 1)
        report = json.loads((self.root / "all-run/results.json").read_text())
        self.assertEqual(report["counts"]["fail"], 1)

    def test_rejects_duplicate_ids_across_adapters(self):
        path = self.executable("same", "exit 0\n")
        self.descriptor("same", path)
        manifest_dir = self.root / "usr/share/openruyi-tests/v1"
        manifest_dir.mkdir(parents=True)
        (manifest_dir / "example.json").write_text(json.dumps({
            "schema_version": 1,
            "package": "example",
            "tests": [{"id": "same", "command": [str(path)]}],
        }), encoding="utf-8")
        with self.assertRaisesRegex(runner.TestDefinitionError, "duplicate test IDs"):
            runner.discover("example", self.root, 300)

    def test_run_command_writes_machine_readable_summary(self):
        path = self.executable("passes", "echo passed\nexit 0\n")
        self.descriptor("passes", path)
        log_directory = self.root / "run"
        args = SimpleNamespace(
            package="example",
            root=self.root,
            timeout=300,
            test=[],
            match=[],
            log_dir=log_directory,
            allow=[],
        )
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(runner.command_run(args), 0)
        report = json.loads((log_directory / "results.json").read_text())
        self.assertEqual(report["counts"]["pass"], 1)
        self.assertEqual(report["counts"]["fail"], 0)
        self.assertEqual(report["results"][0]["id"], "passes")
        self.assertEqual((log_directory / "passes.stdout.log").read_text().strip(), "passed")


if __name__ == "__main__":
    unittest.main()
