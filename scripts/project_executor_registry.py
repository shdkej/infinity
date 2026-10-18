#!/usr/bin/env python3
"""Resolve an Infinity Intent to a registered project execution workspace."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "project-executors.yaml"


def load_registry(path: Path = REGISTRY) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if data.get("version") != 1 or not isinstance(data.get("executors"), dict):
        raise ValueError("invalid project executor registry")
    return data


def infer_project_id(fields: dict[str, Any]) -> str | None:
    explicit = str(fields.get("project_id") or fields.get("project") or "").strip().lower()
    if explicit:
        return explicit
    haystack = " ".join(str(fields.get(key) or "") for key in ("context", "repository", "task_name", "title"))
    matches = [project_id for project_id in load_registry()["executors"] if re.search(rf"(?<![a-z0-9]){re.escape(project_id)}(?![a-z0-9])", haystack.lower())]
    return matches[0] if len(matches) == 1 else None


def resolve_fields(fields: dict[str, Any], path: Path = REGISTRY) -> dict[str, Any]:
    project_id = str(fields.get("project_id") or fields.get("project") or "").strip().lower() or None
    if not project_id:
        explicit_fields = dict(fields)
        registry = load_registry(path)
        haystack = " ".join(str(explicit_fields.get(key) or "") for key in ("context", "repository", "task_name", "title"))
        matches = [candidate for candidate in registry["executors"] if re.search(rf"(?<![a-z0-9]){re.escape(candidate)}(?![a-z0-9])", haystack.lower())]
        project_id = matches[0] if len(matches) == 1 else None
    registry = load_registry(path)
    executor = registry["executors"].get(project_id) if project_id else None
    if not project_id:
        return {"status": "unresolved", "reason": "project_id_required"}
    if not executor:
        return {"status": "unresolved", "project_id": project_id, "reason": "project_not_registered"}
    return {"status": "resolved", "project_id": project_id, "executor": executor}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-id")
    parser.add_argument("--context", default="")
    parser.add_argument("--repository", default="")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = resolve_fields(vars(args))
    print(json.dumps(result, ensure_ascii=False, indent=2 if args.json else None))
    return 0 if result["status"] == "resolved" else 2


if __name__ == "__main__":
    raise SystemExit(main())
