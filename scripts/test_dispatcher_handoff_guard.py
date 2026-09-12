#!/usr/bin/env python3
"""Regression checks for dispatcher handoff failure containment."""
from __future__ import annotations

import unittest
from pathlib import Path


SOURCE = Path(__file__).with_name("run_dispatcher_cycle.sh").read_text()


class DispatcherHandoffGuardTest(unittest.TestCase):
    def test_prompt_is_checked_before_the_cli_is_called(self):
        self.assertIn('PROMPT_STAGE_FILE="${PROMPT_FILE}.stage"', SOURCE)
        self.assertIn('[[ ! -s "$PROMPT_STAGE_FILE" ]]', SOURCE)
        self.assertLess(
            SOURCE.index('[[ ! -s "$PROMPT_STAGE_FILE" ]]'),
            SOURCE.index('--message-file "$PROMPT_FILE"'),
        )

    def test_handoff_failure_is_converted_to_a_controlled_result(self):
        self.assertIn('|| "$HANDOFF_EXIT" -ne 0', SOURCE)
        self.assertIn('FINAL_EXIT=0', SOURCE)


if __name__ == "__main__":
    unittest.main()
