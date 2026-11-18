#!/usr/bin/env python3
"""An immutable intake snapshot must remain represented in the mutable receipt ledger."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from verify_hermes_receipt import verify


class ReceiptContinuityTest(unittest.TestCase):
    def test_evolving_ledger_preserves_original_sent_and_unknown(self):
        original = {"deliveries": {
            "a": {"state": "sent", "destination": "x|telegram:433493318"},
            "b": {"state": "delivery_unknown", "destination": "y|telegram:433493318"},
        }, "observed_intents": {"i": {"lane": "waiting"}}}
        with tempfile.TemporaryDirectory() as temp:
            baseline = Path(temp) / "baseline.json"
            current = Path(temp) / "current.json"
            baseline.write_text(json.dumps(original))
            expected = hashlib.sha256(baseline.read_bytes()).hexdigest()
            current.write_text(json.dumps({"deliveries": {
                "a": original["deliveries"]["a"],
                "b": {"state": "superseded", "destination": "y|telegram:433493318"},
                "c": {"state": "sent"},
            }, "observed_intents": {}}))
            self.assertTrue(verify(baseline, current, expected))
            current.write_text(json.dumps({"deliveries": {"b": original["deliveries"]["b"]}, "observed_intents": {}}))
            self.assertFalse(verify(baseline, current, expected))
            current.write_text(json.dumps({"deliveries": {
                "a": {"state": "claimed", "destination": "x|telegram:433493318"},
                "b": original["deliveries"]["b"],
            }, "observed_intents": {}}))
            self.assertFalse(verify(baseline, current, expected))


if __name__ == "__main__":
    unittest.main()
