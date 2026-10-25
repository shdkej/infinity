import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from backlog_watcher import candidate_id, classify_series


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


if __name__ == "__main__":
    unittest.main()
