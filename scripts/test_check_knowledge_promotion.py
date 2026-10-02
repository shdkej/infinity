import tempfile
import unittest
from pathlib import Path
import sys
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_knowledge_promotion as gate


class KnowledgePromotionGateTest(unittest.TestCase):
    def test_context_receipt_uses_knowledge_lab_log(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            infinity = root / "infinity"
            (infinity / "intents" / "context").mkdir(parents=True)
            (infinity / "intents" / "archive").mkdir(parents=True)
            (infinity / "intents" / "context" / "x.json").write_text(
                '{"selected_context_required": true, "selected_context": [{"path": "agent-wiki/content/docs/outputs/x.mdx"}]}',
                encoding="utf-8",
            )
            (infinity / "intents" / "archive" / "x.md").write_text(
                "- context_pack: intents/context/x.json\n- knowledge_log: logs/agent-wiki-query.md#x\n",
                encoding="utf-8",
            )
            query_log = root / "logs" / "agent-wiki-query.md"
            query_log.parent.mkdir(parents=True)
            query_log.write_text(
                "## [x] receipt\n- 읽은 문서: agent-wiki/content/docs/outputs/x.mdx\n",
                encoding="utf-8",
            )
            with patch.object(gate, "ROOT", infinity), patch.object(gate, "QUERY_LOG", query_log):
                self.assertEqual(gate.context_log_errors("x", (infinity / "intents" / "archive" / "x.md").read_text()), [])

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
                """### 2026-08-22 — shdkej/infinity:intents/archive/x.md → source/infinity/archive/x.md\n- id: x\n- repository: https://github.com/shdkej/infinity\n- source: source/infinity/archive/x.md\n- status: integrated\n- target: none\n""",
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
