#!/usr/bin/env python3
"""Regression checks for dispatcher handoff failure containment."""
from __future__ import annotations

import unittest
from pathlib import Path
import json
import re
import subprocess
import sys
import tempfile


SOURCE = Path(__file__).with_name("run_dispatcher_cycle.sh").read_text()


class DispatcherHandoffGuardTest(unittest.TestCase):
    def test_cycle_fetches_and_verifies_latest_origin_main_before_planning(self):
        self.assertIn('git -C "$ROOT" fetch --prune origin main', SOURCE)
        self.assertIn('FETCHED_MAIN_SHA="$(git -C "$ROOT" rev-parse FETCH_HEAD', SOURCE)
        self.assertIn('ORIGIN_MAIN_SHA="$(git -C "$ROOT" rev-parse refs/remotes/origin/main', SOURCE)
        self.assertIn('[[ "$FETCHED_MAIN_SHA" == "$ORIGIN_MAIN_SHA" ]]', SOURCE)
        self.assertLess(
            SOURCE.index('[[ "$FETCHED_MAIN_SHA" == "$ORIGIN_MAIN_SHA" ]]'),
            SOURCE.index('git -C "$ROOT" worktree add --detach'),
        )

    def test_prompt_is_checked_before_the_cli_is_called(self):
        self.assertIn('PROMPT_STAGE_FILE="${PROMPT_FILE}.stage"', SOURCE)
        self.assertIn('[[ ! -s "$PROMPT_STAGE_FILE" ]]', SOURCE)
        self.assertLess(
            SOURCE.index('[[ ! -s "$PROMPT_STAGE_FILE" ]]'),
            SOURCE.index('--message-file "$PROMPT_FILE"'),
        )

    def test_handoff_failure_is_converted_to_a_controlled_result(self):
        self.assertIn('|| "$HANDOFF_EXIT" -ne 0', SOURCE)
        self.assertIn('FINAL_EXIT=1', SOURCE)

    def test_prompt_and_verifier_gate_expansion_on_live_explicit_deadline(self):
        self.assertIn('Plan.at < deadline', SOURCE)
        self.assertIn('verified_at >= deadline', SOURCE)
        self.assertIn('valid explicit future `deadline`', SOURCE)
        self.assertIn('never add a child leaf', SOURCE)
        self.assertNotIn('add 1–5 evidence-bearing exploratory leaves', SOURCE)

    def test_prompt_keeps_lane_and_intent_path_placeholders_literal(self):
        match = re.search(
            r'''(?s)if ! python3 - "\$PLAN_FILE" "\$PROMPT_STAGE_FILE" <<'PY'\n(.*?)\nPY\n  then''',
            SOURCE,
        )
        self.assertIsNotNone(match, "could not find the prompt-generation heredoc")
        plan = {
            "canonical_sha": "fixture-sha",
            "run_id": "fixture-run",
            "handoff_candidates": [],
            "waiting_closeout_candidates": [],
            "expansion_candidates": [],
        }
        with tempfile.TemporaryDirectory() as tmp:
            plan_path = Path(tmp) / "plan.json"
            prompt_path = Path(tmp) / "prompt.txt"
            plan_path.write_text(json.dumps(plan), encoding="utf-8")
            plan_path_arg = str(plan_path)
            prompt_path_arg = str(prompt_path)
            result = subprocess.run(
                [sys.executable, "-", plan_path_arg, prompt_path_arg],
                input=match.group(1), text=True, capture_output=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            prompt = prompt_path.read_text(encoding="utf-8")
        self.assertIn("intents/{lane}/{id}.md", prompt)
        self.assertIn("intents/archive/{id}.md", prompt)
        self.assertNotIn("intents/None.md", prompt)


if __name__ == "__main__":
    unittest.main()
