#!/usr/bin/env bash
# Cron entrypoint: every dispatcher cycle must pass the Infinity command registry.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
COMMAND_ID="dispatcher-cycle-$(date -u +%Y%m%dT%H%M%SZ)-$$"

python3 - "$ROOT" "$COMMAND_ID" <<'PY' | python3 "$ROOT/scripts/command_runner.py" --apply
import json, sys
root, command_id = sys.argv[1:]
print(json.dumps({
    "version": 1,
    "intent_id": "infinity-dispatcher-cycle",
    "permission": "L1",
    "judgment": {
        "purpose": "Run the canonical 10-minute Infinity dispatcher cycle.",
        "alternatives": [],
        "dissent": [],
        "questions": [],
        "evidence": ["registered command dispatcher.cycle"],
    },
    "commands": [{"command_id": command_id, "name": "dispatcher.cycle", "args": {}}],
}, ensure_ascii=False))
PY
