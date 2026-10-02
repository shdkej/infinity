#!/usr/bin/env python3
"""Verify that an Infinity archive transition is visible on remote main."""

from __future__ import annotations

import argparse
import base64
import json
import re
import subprocess
import sys
import urllib.request
import urllib.error
from pathlib import Path

ARCHIVE_STATUS_RE = re.compile(r"^\s*-\s*status:\s*(archived|complete|completed)\s*$", re.I | re.M)
DASHBOARD_ARCHIVE_COMMENT_RE = re.compile(
    r"<!--\s*"
    r"([a-z][a-z0-9]*(?:-[a-z0-9]+)*)\b"
    r"[\s\S]*?"
    r"\b(completed|resolved|done|archived|closed|canceled|cancelled|rejected|approved|failed)\b"
    r"[\s\S]*?"
    r"(?:→|->)\s*([^\s)]+\.md)"
    r"[\s\S]*?-->"
)
FULL_MARKDOWN_EFFECTIVE_DATE = "2026-09-13"


def run(args: list[str], cwd: Path) -> str:
    proc = subprocess.run(args, cwd=cwd, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(
            f"{' '.join(args)} failed\nstdout: {proc.stdout.strip()}\nstderr: {proc.stderr.strip()}"
        )
    return proc.stdout.strip()


def github_api_text(path: str) -> str:
    url = f"https://api.github.com/repos/shdkej/infinity/contents/{path}?ref=main"
    try:
        return github_api_text_from(url)
    except urllib.error.HTTPError as exc:
        if exc.code not in (403, 429):
            raise
        return raw_github_text(path)


def github_api_text_from(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "openclaw-infinity-archive-verifier/1.0"})
    with urllib.request.urlopen(request, timeout=20) as response:
        data = json.loads(response.read().decode("utf-8"))
    return base64.b64decode(data["content"]).decode("utf-8")


def raw_github_text(path: str) -> str:
    url = f"https://raw.githubusercontent.com/shdkej/infinity/main/{path}"
    return http_text(url)


def git_remote_text(repo: Path, path: str) -> str:
    """Read an authoritative path from the fetched remote main Git blob."""
    return run(["git", "show", f"origin/main:{path}"], repo)


def knowledge_lab_api_text(path: str) -> str:
    url = f"https://api.github.com/repos/shdkej/knowledge-lab/contents/{path}?ref=main"
    try:
        return github_api_text_from(url)
    except urllib.error.HTTPError as exc:
        if exc.code not in (403, 429):
            raise
        return http_text(f"https://raw.githubusercontent.com/shdkej/knowledge-lab/main/{path}")


def http_text(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "openclaw-infinity-archive-verifier/1.0"})
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read().decode("utf-8")


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


def final_research_artifact_path(archive_text: str, intent_id: str) -> str | None:
    """Return the required full Markdown report path from an archive record."""
    pattern = re.compile(
        rf"^\s*-\s*final_artifact:\s*(artifacts/{re.escape(intent_id)}/final/[^/\s]+-(?:report|brief)\.md)\s*$",
        re.M,
    )
    match = pattern.search(archive_text)
    return match.group(1) if match else None


def requires_full_markdown_report(archive_text: str) -> bool:
    completed = re.search(r"^\s*-\s*completed_at:\s*(\d{4}-\d{2}-\d{2})", archive_text, re.M)
    return bool(completed and completed.group(1) >= FULL_MARKDOWN_EFFECTIVE_DATE)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("intent_id")
    parser.add_argument(
        "--repo",
        default="/home/ubuntu/workspace/knowledge-lab/infinity",
        help="Infinity checkout path",
    )
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    intent_id = args.intent_id
    errors: list[str] = []
    archive_detail_path: str | None = None
    final_artifact_path: str | None = None
    parent = repo.parent

    try:
        run(["python3", "scripts/check_intents_consistency.py", "INTENTS.md"], repo)
    except Exception as exc:
        errors.append(str(exc))

    # Research reports need semantic depth, not only valid HTML/template markers.
    try:
        archive_local = repo / "intents" / "archive" / f"{intent_id}.md"
        archive_text = archive_local.read_text() if archive_local.exists() else ""
        is_decision_research = not re.search(r"^\s*-\s*research_mode:\s*exploratory_research\s*$", archive_text, re.M)
        is_research = bool(archive_text and re.search(r"^\s*-\s*task_type:\s*research\s*$", archive_text, re.M))
        if is_research and requires_full_markdown_report(archive_text):
            final_artifact_path = final_research_artifact_path(archive_text, intent_id)
            if not final_artifact_path:
                errors.append(
                    f"Research archive {intent_id} has no final_artifact Markdown report under artifacts/{{id}}/final/"
                )
            elif not (repo / final_artifact_path).is_file() or not (repo / final_artifact_path).read_text().strip():
                errors.append(f"Research archive {intent_id} final Markdown report is missing or empty: {final_artifact_path}")
        if is_research and is_decision_research:
            report_match = re.search(r"^\s*-\s*report:\s*(\S+\.html)\s*$", archive_text, re.M)
            if not report_match:
                errors.append(f"Research archive {intent_id} has no final HTML report")
            else:
                run(["python3", "scripts/validate_research_report.py", report_match.group(1)], repo)
    except Exception as exc:
        errors.append(f"Research report quality check failed: {exc}")

    try:
        run(["git", "fetch", "origin", "main"], repo)
        local_head = run(["git", "rev-parse", "HEAD"], repo)
        remote_head = run(["git", "rev-parse", "origin/main"], repo)
        if local_head != remote_head:
            errors.append(f"Infinity HEAD is not pushed: local {local_head[:7]} != origin/main {remote_head[:7]}")
    except Exception as exc:
        errors.append(str(exc))

    if final_artifact_path:
        try:
            if not git_remote_text(repo, final_artifact_path).strip():
                errors.append(f"Remote final Markdown report is empty: {final_artifact_path}")
        except Exception as exc:
            errors.append(f"Remote final Markdown report check failed for {final_artifact_path}: {exc}")

    try:
        # GitHub contents/raw endpoints can serve a stale body immediately
        # after push. `origin/main` is the canonical remote commit checked
        # above, so use its blob rather than a cached HTTP response.
        intents_text = git_remote_text(repo, "INTENTS.md")
        sections = split_sections(intents_text)
        archive = sections.get("Archive", "")
        open_lanes = "\n".join(sections.get(name, "") for name in ("Inbox", "Active", "Waiting"))
        if intent_id not in archive:
            errors.append(f"Remote INTENTS.md Archive does not contain {intent_id}")
        if intent_id in open_lanes:
            errors.append(f"Remote INTENTS.md still contains {intent_id} in an open lane")
        dashboard_matches = [
            match for match in DASHBOARD_ARCHIVE_COMMENT_RE.finditer(archive) if match.group(1) == intent_id
        ]
        if not dashboard_matches:
            errors.append(f"Remote Archive comment for {intent_id} does not match dashboard parser format")
        else:
            archive_detail_path = dashboard_matches[0].group(3)
    except Exception as exc:
        errors.append(f"Remote INTENTS.md check failed: {exc}")

    archive_paths = [archive_detail_path] if archive_detail_path else [f"source/infinity/archive/{intent_id}.md"]
    for archive_path in archive_paths:
        if not archive_path:
            continue
        try:
            archive_text = (
                git_remote_text(parent, archive_path)
                if archive_path.startswith("source/infinity/archive/")
                else git_remote_text(repo, archive_path)
            )

            if f"id: {intent_id}" not in archive_text:
                errors.append(f"Remote archive file {archive_path} has no id field for {intent_id}")
            if not ARCHIVE_STATUS_RE.search(archive_text):
                errors.append(f"Remote archive file {archive_path} is not an accepted archive status for {intent_id}")
            remote_is_research = bool(re.search(r"^\s*-\s*task_type:\s*research\s*$", archive_text, re.M))
            if remote_is_research and requires_full_markdown_report(archive_text):
                remote_final_path = final_research_artifact_path(archive_text, intent_id)
                if not remote_final_path:
                    errors.append(f"Remote research archive {archive_path} has no matching final Markdown report")
                else:
                    try:
                        if not git_remote_text(repo, remote_final_path).strip():
                            errors.append(f"Remote final Markdown report is empty: {remote_final_path}")
                    except Exception as artifact_exc:
                        errors.append(f"Remote final Markdown report check failed for {remote_final_path}: {artifact_exc}")
        except Exception as exc:
            try:
                if archive_path.startswith("source/infinity/archive/"):
                    run(["git", "fetch", "origin", "main"], parent)
                    archive_text = git_remote_text(parent, archive_path)
                else:
                    run(["git", "fetch", "origin", "main"], repo)
                    archive_text = git_remote_text(repo, archive_path)
                if f"id: {intent_id}" not in archive_text:
                    errors.append(f"Remote archive file {archive_path} has no id field for {intent_id}")
                if not ARCHIVE_STATUS_RE.search(archive_text):
                    errors.append(f"Remote archive file {archive_path} is not an accepted archive status for {intent_id}")
            except Exception as git_exc:
                errors.append(f"Remote archive file check failed for {archive_path}: {exc}; Git fallback failed: {git_exc}")

    try:
        dashboard_html = http_text("https://infinity.aws.shdkej.com/")
        required_dashboard_markers = [
            "parseArchiveComments",
            'source: "INTENTS.md archive"',
        ]
        for marker in required_dashboard_markers:
            if marker not in dashboard_html:
                errors.append(f"Dashboard page missing expected marker: {marker}")
    except Exception as exc:
        errors.append(f"Dashboard page check failed: {exc}")

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(f"PASS Archive remote verification OK: {intent_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
