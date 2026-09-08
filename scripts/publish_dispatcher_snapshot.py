#!/usr/bin/env python3
"""Publish a small, identifier-free dispatcher snapshot to Kubernetes."""
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def epoch(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00")).timestamp()


def main(run_file):
    record = json.loads(Path(run_file).read_text(encoding="utf-8"))
    plan = record.get("post_handoff_plan") or record.get("plan") or {}
    counts = plan.get("counts") or {}
    snapshot = {
        "last_run_timestamp_seconds": epoch(plan["at"]),
        "run_ok": int(record.get("outcome") not in {"attention", "canonical_fetch_failed"}),
        "invalid_state_total": len(plan.get("invalid_state") or []),
        "delivery_uncertain": int(bool(record.get("terminal_exit") or record.get("post_handoff_terminal_exit"))),
        "active_without_evidence": len(plan.get("resume_candidates") or []),
        **{state: int(counts.get(state, 0)) for state in ("inbox", "active", "waiting", "archive")},
    }
    payload = json.dumps(snapshot, separators=(",", ":"))
    rendered = subprocess.run(
        ["kubectl", "-n", "monitoring", "create", "configmap", "infinity-dispatcher-snapshot",
         "--from-literal=snapshot.json=" + payload, "--dry-run=client", "-o", "yaml"],
        check=True, stdout=subprocess.PIPE, text=True,
    )
    subprocess.run(["kubectl", "apply", "-f", "-"], input=rendered.stdout, text=True, check=True, stdout=subprocess.DEVNULL)


if __name__ == "__main__":
    main(sys.argv[1])
