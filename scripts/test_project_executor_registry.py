#!/usr/bin/env python3
from __future__ import annotations

import tempfile
from pathlib import Path

from project_executor_registry import resolve_fields


def main() -> int:
    assert resolve_fields({"project_id": "policycock"})["executor"]["agent_id"] == "policycock"
    assert resolve_fields({"project_id": "minimalmoeum"})["executor"]["repository"].endswith("/minimalmoeum")
    assert resolve_fields({"context": "/home/ubuntu/workspace/projects/policycock/PROJECT.md"})["project_id"] == "policycock"
    assert resolve_fields({})["reason"] == "project_id_required"
    assert resolve_fields({"project_id": "unknown"})["reason"] == "project_not_registered"
    with tempfile.TemporaryDirectory() as directory:
        try:
            resolve_fields({"project_id": "policycock"}, Path(directory) / "missing.yaml")
        except FileNotFoundError:
            pass
        else:
            raise AssertionError("missing registry must fail closed")
    print("project executor registry tests: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
