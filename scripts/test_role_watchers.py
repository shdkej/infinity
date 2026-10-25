import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import yaml

sys.path.insert(0, str(Path(__file__).parent))
import role_watchers


class RoleWatcherTests(unittest.TestCase):
    def test_candidate_id_is_stable(self):
        self.assertEqual(
            role_watchers.candidate_id("planner", "abc123"),
            "watch-planner-abc123",
        )

    def test_same_digest_is_not_added_twice(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = root / "INTENTS.yaml"
            state = root / "state.json"
            registry.write_text("lanes:\n  backlog: []\n  inbox: []\n  active: []\n  waiting: []\n", encoding="utf-8")
            signal = ("digest-1", ["/evidence.md"], "planning_signal", "new plan", True)
            with patch.object(role_watchers, "REGISTRY", registry), patch.object(role_watchers, "STATE", state), patch.object(role_watchers, "signal_for", return_value=signal):
                first = role_watchers.append_candidates(["planner"], apply=True)
                second = role_watchers.append_candidates(["planner"], apply=True)
            self.assertEqual(first["added"], ["watch-planner-digest-1"])
            self.assertEqual(second["added"], [])

    def test_non_concrete_change_is_observed_but_not_added(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = root / "INTENTS.yaml"
            state = root / "state.json"
            registry.write_text("lanes:\n  backlog: []\n  inbox: []\n  active: []\n  waiting: []\n", encoding="utf-8")
            signal = ("digest-2", ["/baseline.md"], "design_signal", "baseline", False)
            with patch.object(role_watchers, "REGISTRY", registry), patch.object(role_watchers, "STATE", state), patch.object(role_watchers, "signal_for", return_value=signal):
                result = role_watchers.append_candidates(["design"], apply=True)
            self.assertEqual(result["added"], [])
            self.assertTrue(result["observed"][0]["changed"])
            self.assertFalse(result["observed"][0]["concrete"])
            saved = yaml.safe_load(registry.read_text(encoding="utf-8"))
            self.assertEqual(saved["lanes"]["backlog"], [])

    def test_observes_all_roles(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = root / "INTENTS.yaml"
            state = root / "state.json"
            registry.write_text("lanes:\n  backlog: []\n  inbox: []\n  active: []\n  waiting: []\n", encoding="utf-8")
            signal = ("digest-3", [], "signal", "title", False)
            with patch.object(role_watchers, "REGISTRY", registry), patch.object(role_watchers, "STATE", state), patch.object(role_watchers, "signal_for", return_value=signal):
                result = role_watchers.append_candidates(list(role_watchers.ROLE_IDS), apply=False)
            self.assertEqual([item["role"] for item in result["observed"]], list(role_watchers.ROLE_IDS))
            self.assertFalse(state.exists())


if __name__ == "__main__":
    unittest.main()
