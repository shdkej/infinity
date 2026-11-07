#!/usr/bin/env python3
"""Regression checks for dispatcher handoff failure containment."""
from __future__ import annotations

import unittest
from pathlib import Path


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


if __name__ == "__main__":
    unittest.main()
