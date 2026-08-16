#!/usr/bin/env python3
"""Verify that an Infinity archive transition is visible on remote main."""

from __future__ import annotations

import argparse
import base64
import json
import subprocess
import sys
import urllib.request
from pathlib import Path


def run(args: list[str], cwd: Path) -> str:
    proc = subprocess.run(args, cwd=cwd, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(
            f"{' '.join(args)} failed\nstdout: {proc.stdout.strip()}\nstderr: {proc.stderr.strip()}"
        )
    return proc.stdout.strip()


def github_api_text(path: str) -> str:
    url = f"https://api.github.com/repos/shdkej/infinity/contents/{path}?ref=main"
    with urllib.request.urlopen(url, timeout=20) as response:
        data = json.loads(response.read().decode("utf-8"))
    return base64.b64decode(data["content"]).decode("utf-8")


def split_sections(text: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {"__preamble__": []}
    current = "__preamble__"
    for line in text.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            sections[current] = []
        else:
            sections.setdefault(current, []).append(line)
    return {name: "\n".join(lines) for name, lines in sections.items()}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("intent_id")
    parser.add_argument(
        "--repo",
        default="/home/ubuntu/workspace/knowledge-lab/infinity",
        help="Infinity checkout path",
    )
    parser.add_argument(
        "--parent",
        default="/home/ubuntu/workspace/knowledge-lab",
        help="Parent Knowledge Lab checkout path",
    )
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    parent = Path(args.parent).resolve()
    intent_id = args.intent_id
    errors: list[str] = []

    try:
        run(["python3", "scripts/check_intents_consistency.py", "INTENTS.md"], repo)
    except Exception as exc:
        errors.append(str(exc))

    try:
        run(["git", "fetch", "origin", "main"], repo)
        local_head = run(["git", "rev-parse", "HEAD"], repo)
        remote_head = run(["git", "rev-parse", "origin/main"], repo)
        if local_head != remote_head:
            errors.append(f"Infinity HEAD is not pushed: local {local_head[:7]} != origin/main {remote_head[:7]}")
    except Exception as exc:
        errors.append(str(exc))

    try:
        intents_text = github_api_text("INTENTS.md")
        sections = split_sections(intents_text)
        archive = sections.get("Archive", "")
        open_lanes = "\n".join(sections.get(name, "") for name in ("Inbox", "Active", "Waiting"))
        if intent_id not in archive:
            errors.append(f"Remote INTENTS.md Archive does not contain {intent_id}")
        if intent_id in open_lanes:
            errors.append(f"Remote INTENTS.md still contains {intent_id} in an open lane")
    except Exception as exc:
        errors.append(f"Remote INTENTS.md check failed: {exc}")

    try:
        archive_text = github_api_text(f"intents/archive/{intent_id}.md")
        if f"id: {intent_id}" not in archive_text:
            errors.append(f"Remote archive file has no id field for {intent_id}")
        if "status: archived" not in archive_text:
            errors.append(f"Remote archive file is not status: archived for {intent_id}")
    except Exception as exc:
        errors.append(f"Remote archive file check failed: {exc}")

    if parent.exists() and (parent / ".git").exists():
        try:
            run(["git", "fetch", "origin", "main"], parent)
            parent_head = run(["git", "rev-parse", "HEAD"], parent)
            parent_remote = run(["git", "rev-parse", "origin/main"], parent)
            if parent_head != parent_remote:
                errors.append(
                    f"Knowledge Lab pointer is not pushed: local {parent_head[:7]} != origin/main {parent_remote[:7]}"
                )
        except Exception as exc:
            errors.append(str(exc))

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(f"Archive remote verification OK: {intent_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
