#!/usr/bin/env python3
"""Safety contract for the paused Hermes Infinity migration entrypoint."""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/run_hermes_infinity_cron.sh"


class HermesCronEntrypointTest(unittest.TestCase):
    def invoke(self, role, *args, home):
        env = os.environ.copy()
        env["INFINITY_HERMES_STATE_DIR"] = str(home)
        env.pop("INFINITY_HERMES_CUTOVER_READY", None)
        return subprocess.run(["bash", str(SCRIPT), role, *args], cwd=ROOT, env=env,
                              text=True, capture_output=True)

    def test_checks_are_local_and_report_not_ready_without_state(self):
        with tempfile.TemporaryDirectory() as temp:
            home = Path(temp) / "uncreated"
            for role in ("dispatcher", "consumer", "notifier"):
                with self.subTest(role=role):
                    result = self.invoke(role, "--check", home=home)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    report = json.loads(result.stdout)
                    self.assertEqual(report["role"], role)
                    self.assertFalse(report["ready"])
                    self.assertFalse(home.exists(), "a read-only check must not create state")

    def test_normal_entry_refuses_before_any_state_or_external_call(self):
        with tempfile.TemporaryDirectory() as temp:
            home = Path(temp) / "uncreated"
            for role in ("dispatcher", "consumer", "notifier"):
                with self.subTest(role=role):
                    result = self.invoke(role, home=home)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertFalse(home.exists())

    def test_invalid_role_never_succeeds(self):
        with tempfile.TemporaryDirectory() as temp:
            result = self.invoke("old-evaluator", "--check", home=Path(temp))
            self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
