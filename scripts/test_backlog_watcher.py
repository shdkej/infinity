import unittest
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from backlog_watcher import append_candidates, candidate_id, classify_series


class BacklogWatcherTests(unittest.TestCase):
    def test_detects_zero_stagnation(self):
        findings = classify_series([0, 0, 0, 0, 0])
        self.assertEqual([item["kind"] for item in findings], ["metric_stagnation"])

    def test_detects_low_metric(self):
        findings = classify_series([10, 12, 11, 4])
        self.assertEqual([item["kind"] for item in findings], ["metric_low"])

    def test_detects_spike(self):
        findings = classify_series([10, 11, 12, 60])
        self.assertEqual([item["kind"] for item in findings], ["metric_spike"])

    def test_problem_identity_does_not_change_with_value(self):
        first = candidate_id({"source": "posthog", "kind": "metric_low", "problem_key": "posthog:42:metric_low", "signal": "42:4"})
        second = candidate_id({"source": "posthog", "kind": "metric_low", "problem_key": "posthog:42:metric_low", "signal": "42:3"})
        self.assertEqual(first, second)

    def test_legacy_problem_key_does_not_reinsert_same_problem(self):
        registry = {"lanes": {"backlog": [{
            "id": "watch-posthog-legacy",
            "source": "posthog",
            "signal_type": "metric_low",
            "problem_key": "posthog|metric_low|42",
        }]}}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "INTENTS.yaml"
            path.write_text(yaml.safe_dump(registry), encoding="utf-8")
            candidate = {
                "source": "posthog",
                "kind": "metric_low",
                "problem_key": "posthog:42:metric_low",
                "title": "같은 문제",
                "signal": "42:3",
                "source_ref": "42",
            }
            with patch("backlog_watcher.REGISTRY", path):
                self.assertEqual(append_candidates([candidate], apply=True), [])
            saved = yaml.safe_load(path.read_text(encoding="utf-8"))
            self.assertEqual(len(saved["lanes"]["backlog"]), 1)


if __name__ == "__main__":
    unittest.main()
