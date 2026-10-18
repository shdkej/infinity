import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import command_runner


class CommandRunnerTests(unittest.TestCase):
    def plan(self, commands):
        return {"version": 1, "intent_id": "general-1", "judgment": {"alternatives": ["A"], "dissent": [], "questions": []}, "commands": commands}

    def test_unregistered_command_is_rejected(self):
        result = command_runner.run(self.plan([{"command_id": "x", "name": "shell.exec", "args": {}}]), False)
        self.assertEqual(result["status"], "rejected")

    def test_dry_run_preserves_ai_judgment_and_does_not_write(self):
        with tempfile.TemporaryDirectory() as directory:
            log = Path(directory) / "runs.jsonl"
            with patch.object(command_runner, "RUN_LOG", log):
                result = command_runner.run(self.plan([{"command_id": "x", "name": "role.fanout", "args": {"intent_id": "general-1", "shared_contract": {"goal": "g", "success_evidence": ["e"]}}}]), False)
            self.assertEqual(result["status"], "pass")
            self.assertFalse(log.exists())

    def test_fanout_requires_all_four_roles(self):
        with self.assertRaises(ValueError):
            command_runner.role_fanout({"intent_id": "general-1", "roles": ["planner"], "shared_contract": {"goal": "g", "success_evidence": ["e"]}})

    def test_duplicate_command_id_is_rejected(self):
        command = {"command_id": "same", "name": "role.fanout", "args": {"intent_id": "general-1", "shared_contract": {"goal": "g", "success_evidence": ["e"]}}}
        result = command_runner.run(self.plan([command, dict(command)]), False)
        self.assertEqual(result["status"], "rejected")

    def test_permission_is_enforced_from_registry(self):
        plan = self.plan([{"command_id": "x", "name": "role.fanout", "args": {"intent_id": "general-1", "shared_contract": {"goal": "g", "success_evidence": ["e"]}}}])
        plan["permission"] = "L0"
        result = command_runner.run(plan, False)
        self.assertEqual(result["status"], "rejected")

    def test_registry_handlers_are_all_implemented(self):
        commands = command_runner.load_commands()
        self.assertEqual(set(commands), {"intent.register", "intent.move", "intent.archive", "role.fanout", "trace.record", "context.pack.build", "trace.execution.record", "git.verify"})
        self.assertTrue(all(spec["handler"] in command_runner.HANDLERS for spec in commands.values()))

    def test_context_pack_command_is_dry_run_safe(self):
        result = command_runner.run(self.plan([{"command_id": "x", "name": "context.pack.build", "args": {"intent_id": "general-1", "route": "infinity", "request": "query", "output_path": "intents/context/general-1.json"}}]), False)
        self.assertEqual(result["status"], "pass")
        self.assertEqual(result["results"][0]["status"], "dry_run")


if __name__ == "__main__":
    unittest.main()
