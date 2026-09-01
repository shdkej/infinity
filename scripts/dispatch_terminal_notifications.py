#!/usr/bin/env python3
"""Reconcile remote Infinity terminal states into one destination-aware notice.

The dispatcher deliberately has no implicit Telegram default.  An intent must carry
``notification_channel`` and ``notification_target`` captured at intake; that makes
the original conversation addressable and prevents an archive from being broadcast
to an unrelated chat.  The durable ledger is keyed by intent, terminal phase, and
that destination, so a later dispatcher/cron replay is silent.

Use ``--mock-outbox`` for tests.  Real delivery is opt-in via ``--deliver`` and the
host-owned OpenClaw CLI; it is never selected by default.
"""
from __future__ import annotations

import argparse
import datetime as dt
import fcntl
import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OPEN_LANES = {"Inbox", "Active", "Waiting", "Archive"}


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sections(text: str) -> dict[str, str]:
    result: dict[str, list[str]] = {}
    current: str | None = None
    for line in text.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            result.setdefault(current, [])
        elif current:
            result[current].append(line)
    return {name: "\n".join(lines) for name, lines in result.items()}


def entries(text: str) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for lane, body in sections(text).items():
        if lane not in OPEN_LANES:
            continue
        current: dict[str, object] | None = None
        for line in body.splitlines():
            if line.startswith("### [") and "]" in line:
                intent_id, title = line[5:].split("]", 1)
                current = {"id": intent_id, "title": title.strip(), "lane": lane.lower(), "fields": {}}
                records.append(current)
            elif current and line.startswith("- ") and ":" in line:
                key, value = line[2:].split(":", 1)
                current["fields"][key.strip()] = value.strip()  # type: ignore[index]
    return records


def phase(entry: dict[str, object]) -> str | None:
    fields: dict[str, str] = entry["fields"]  # type: ignore[assignment]
    status = fields.get("status", entry["lane"]).lower()
    if entry["lane"] == "archive" or status in {"archived", "completed", "complete", "done"}:
        # A remote archive is necessary but not sufficient: the executor records
        # its post-push verifier before this reconciler is allowed to announce it.
        if fields.get("remote_verified", "").lower() in {"pass", "true", "verified"}:
            return "completed"
        return None
    if entry["lane"] == "waiting" or status in {"waiting", "blocked"}:
        if fields.get("approval") or fields.get("waiting_on", "").lower() == "user":
            return "approval"
        if fields.get("blocker") or fields.get("next_retry_condition"):
            return "blocked"
    return None


def destination(fields: dict[str, str]) -> dict[str, str] | None:
    channel, target = fields.get("notification_channel", ""), fields.get("notification_target", "")
    if not channel or not target:
        return None
    value = {"channel": channel, "target": target}
    # The OpenClaw transport has different thread primitives.  A Telegram forum
    # topic is a ``thread-id``; Slack conversation replies use ``reply-to``.
    # Do not reuse one field across them or an otherwise valid Slack notice can
    # land outside its originating thread.
    if fields.get("notification_thread") and channel == "telegram":
        value["thread"] = fields["notification_thread"]
    if fields.get("notification_reply_to"):
        value["reply_to"] = fields["notification_reply_to"]
    return value


def fingerprint(entry: dict[str, object], state: str) -> str:
    fields: dict[str, str] = entry["fields"]  # type: ignore[assignment]
    useful = [fields.get(key, "") for key in ("report", "result", "blocker", "next_action", "remote_commit")]
    return "|".join([str(entry["id"]), state, *useful])


def message(entry: dict[str, object], state: str) -> str:
    fields: dict[str, str] = entry["fields"]  # type: ignore[assignment]
    if state == "completed":
        detail = fields.get("result") or fields.get("metric_result") or "원격 검증을 통과했습니다."
        proof = " · ".join(filter(None, (fields.get("remote_commit"), fields.get("report"), "remote verified")))
        return f"Infinity 완료 · {entry['id']} {entry['title']}\n{detail}\n검증: {proof}"
    label = "승인/결정 필요" if state == "approval" else "진행 차단"
    detail = fields.get("blocker") or fields.get("waiting_reason") or "구체 사유가 원장에 없습니다."
    action = fields.get("next_action") or fields.get("next_retry_condition") or "원장을 확인해 주세요."
    return f"Infinity {label} · {entry['id']} {entry['title']}\n사유: {detail}\n다음: {action}"


def load(path: Path, legacy_path: Path | None = None) -> dict[str, object]:
    if path.exists():
        data = json.loads(path.read_text())
    else:
        # The earlier dispatcher state keyed only an intent to a phase/fingerprint
        # and has no destination identity.  It therefore cannot be promoted to an
        # exact-once receipt safely.  Preserve an auditable migration marker rather
        # than guessing a recipient or silently rewriting the legacy file.
        legacy_ids: list[str] = []
        if legacy_path and legacy_path.exists():
            try:
                legacy = json.loads(legacy_path.read_text())
                legacy_ids = sorted((legacy.get("intents") or legacy.get("notifications") or {}).keys())
            except (json.JSONDecodeError, AttributeError):
                legacy_ids = []
        data = {"version": 2, "deliveries": {}, "legacy_state_observed": bool(legacy_path and legacy_path.exists()), "legacy_unaddressable_intents": legacy_ids}
    data.setdefault("version", 2)
    data.setdefault("deliveries", {})
    return data


def save(path: Path, data: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    tmp.replace(path)


def send(dest: dict[str, str], body: str, args: argparse.Namespace) -> str:
    if args.mock_outbox:
        with Path(args.mock_outbox).open("a") as outbox:
            outbox.write(json.dumps({"destination": dest, "message": body}, ensure_ascii=False) + "\n")
        return "sent"
    if not args.deliver:
        raise RuntimeError("delivery requires --deliver (or use --mock-outbox)")
    command = [args.openclaw_bin, "message", "send", "--json", "--channel", dest["channel"], "--target", dest["target"], "--message", body]
    if dest.get("thread"):
        command.extend(["--thread-id", dest["thread"]])
    if dest.get("reply_to"):
        command.extend(["--reply-to", dest["reply_to"]])
    result = subprocess.run(command, text=True, capture_output=True)
    if result.returncode:
        return "failed_before_acceptance"
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError:
        return "delivery_unknown"
    if payload.get("ok") is True or payload.get("success") is True or payload.get("messageId") or payload.get("message_id"):
        return "sent"
    return "delivery_unknown"


def remote_text(repo: Path) -> tuple[str, str]:
    subprocess.run(["git", "fetch", "origin", "main"], cwd=repo, check=True, capture_output=True, text=True)
    sha = subprocess.check_output(["git", "rev-parse", "origin/main"], cwd=repo, text=True).strip()
    return subprocess.check_output(["git", "show", "origin/main:INTENTS.md"], cwd=repo, text=True), sha


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=ROOT)
    parser.add_argument("--intents", type=Path, help="fixture/local snapshot; production omits this and reads origin/main")
    parser.add_argument("--state", type=Path, default=ROOT / "data/dispatcher-terminal-notifications.json")
    parser.add_argument("--legacy-state", type=Path, default=ROOT / "data/dispatcher-notification-state.json", help="read-only legacy advisory state; it lacks destination identity and is never used to send")
    parser.add_argument("--lock", type=Path, help="exclusive reconciliation lock (defaults beside state)")
    parser.add_argument("--mock-outbox", help="safe JSONL delivery sink")
    parser.add_argument("--deliver", action="store_true", help="enable host OpenClaw CLI delivery")
    parser.add_argument("--openclaw-bin", default="openclaw")
    args = parser.parse_args()
    if args.intents:
        text = args.intents.read_text()
        remote_sha = "fixture:" + hashlib.sha256(text.encode()).hexdigest()
    else:
        text, remote_sha = remote_text(args.repo)
    lock_path = args.lock or args.state.with_suffix(args.state.suffix + ".lock")
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("w") as lock:
      fcntl.flock(lock, fcntl.LOCK_EX)
      ledger = load(args.state, args.legacy_state)
      deliveries: dict[str, dict[str, str]] = ledger["deliveries"]  # type: ignore[assignment]
      sent = skipped = 0
      for entry in entries(text):
          terminal = phase(entry)
          if not terminal:
              continue
          fields: dict[str, str] = entry["fields"]  # type: ignore[assignment]
          dest = destination(fields)
          if not dest:
              skipped += 1
              continue
          identity = "|".join((str(entry["id"]), terminal, dest["channel"], dest["target"], dest.get("thread", "")))
          key = hashlib.sha256(identity.encode()).hexdigest()
          existing = deliveries.get(key)
          if existing:
              # A claim without an attempt marker means the prior process died
              # before it could invoke the transport and is safe to retry.  Once
              # an attempt began, replay could duplicate a provider-accepted
              # message; leave a durable uncertain receipt and exit non-zero.
              if existing.get("state") in {"failed_before_acceptance"}:
                  # The CLI exited non-zero before it accepted the request, so a
                  # later reconciliation may retry without duplicating delivery.
                  existing.pop("attempt_started_at", None)
                  existing["state"] = "claimed"
              elif existing.get("state") == "claimed" and not existing.get("attempt_started_at"):
                  pass
              else:
                  continue
          # Persist the claim before calling an external transport.  A crash after
          # acceptance is thus never replayed as a duplicate; operators inspect a
          # ``claimed``/``delivery_unknown`` receipt and decide a manual remedy.
          receipt = existing or {"intent_id": str(entry["id"]), "terminal_state": terminal, "destination": identity, "fingerprint": fingerprint(entry, terminal), "remote_sha": remote_sha, "claimed_at": now(), "state": "claimed"}
          deliveries[key] = receipt
          receipt["attempt_started_at"] = now()
          save(args.state, ledger)
          # A durable claim makes concurrent runs safe.  A claimed receipt is safe
          # to retry after an interrupted process because no transport result was
          # recorded.  ``delivery_unknown`` is intentionally never replayed: CLI
          # acceptance is ambiguous and automatic replay could duplicate a notice.
          outcome = send(dest, message(entry, terminal), args)
          receipt["state"] = outcome
          receipt[("sent_at" if outcome == "sent" else "updated_at")] = now()
          save(args.state, ledger)
          sent += outcome == "sent"
      fcntl.flock(lock, fcntl.LOCK_UN)
    unknown = sum(1 for receipt in deliveries.values() if receipt.get("state") in {"claimed", "failed_before_acceptance", "delivery_unknown"})
    print(json.dumps({"sent": sent, "skipped_missing_destination": skipped, "delivery_uncertain": unknown}, ensure_ascii=False))
    # A non-zero result activates the cron's bounded failure alert.  It surfaces an
    # uncertain receipt for operator handling instead of silently losing it.
    return 2 if unknown else 0


if __name__ == "__main__":
    raise SystemExit(main())
