import tempfile
import unittest
from pathlib import Path
import sys
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_knowledge_promotion as gate


class KnowledgePromotionGateTest(unittest.TestCase):
    def test_promoted_requires_real_wiki_target_and_commit(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            archive = root / "intents" / "archive"
            archive.mkdir(parents=True)
            target = root / "agent-wiki" / "content" / "docs" / "concepts" / "rule.mdx"
            target.parent.mkdir(parents=True)
            target.write_text("# Rule\n", encoding="utf-8")
            ingest = root / "ingest" / "INDEX.md"
            ingest.parent.mkdir(parents=True)
            ingest.write_text(
                """### 2026-08-22 — infinity/intents/archive/x.md\n- id: x\n- source: infinity/intents/archive/x.md\n- status: integrated\n- target: [agent-wiki/content/docs/concepts/rule.mdx]\n""",
                encoding="utf-8",
            )
            (archive / "x.md").write_text(
                """- knowledge_status: promoted\n- knowledge_decision: promote\n- knowledge_targets: agent-wiki/content/docs/concepts/rule.mdx\n- knowledge_reflection: reusable rule\n- knowledge_commit: abc123\n""",
                encoding="utf-8",
            )
            with patch.object(gate, "ARCHIVE", archive), patch.object(gate, "KNOWLEDGE_LAB", root), patch.object(gate, "INGEST_INDEX", ingest):
                # The commit lookup is isolated below; field/path validation is the contract under test.
                with patch("subprocess.run") as run:
                    run.return_value.returncode = 0
                    self.assertEqual(gate.check("x"), [])

    def test_candidate_is_not_archivable(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            archive = root / "intents" / "archive"
            archive.mkdir(parents=True)
            (archive / "x.md").write_text(
                "- knowledge_status: candidate\n- knowledge_decision: promote\n- knowledge_reflection: pending\n",
                encoding="utf-8",
            )
            with patch.object(gate, "ARCHIVE", archive), patch.object(gate, "KNOWLEDGE_LAB", root):
                self.assertTrue(gate.check("x"))


if __name__ == "__main__":
    unittest.main()
