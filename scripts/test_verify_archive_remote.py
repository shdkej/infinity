#!/usr/bin/env python3
"""Regression tests for the research full-Markdown archive gate."""

import unittest

from verify_archive_remote import final_research_artifact_path, requires_full_markdown_report


class FinalResearchArtifactTest(unittest.TestCase):
    def test_accepts_final_report_markdown(self):
        archive = "- final_artifact: artifacts/research-42/final/dieter-rams-report.md\n"
        self.assertEqual(
            final_research_artifact_path(archive, "research-42"),
            "artifacts/research-42/final/dieter-rams-report.md",
        )

    def test_rejects_candidate_and_non_report_paths(self):
        self.assertIsNone(final_research_artifact_path(
            "- final_artifact: artifacts/research-42/work/candidate/dieter-rams-report.md\n"
        , "research-42"))
        self.assertIsNone(final_research_artifact_path(
            "- final_artifact: artifacts/research-42/final/brief.md\n"
        , "research-42"))

    def test_rejects_another_intents_final_path(self):
        archive = "- final_artifact: artifacts/research-99/final/dieter-rams-report.md\n"
        self.assertIsNone(final_research_artifact_path(archive, "research-42"))

    def test_only_new_archives_require_the_new_contract(self):
        self.assertFalse(requires_full_markdown_report("- completed_at: 2026-09-12T21:50:03Z\n"))
        self.assertTrue(requires_full_markdown_report("- completed_at: 2026-09-13T00:00:00Z\n"))


if __name__ == "__main__":
    unittest.main()
