#!/usr/bin/env python3
"""Bind a verified Slack button callback to one safe Infinity next action.

This is deliberately a local, transport-neutral continuation worker.  The
outbound registry is written before a button is sent; an inbound event may only
match that immutable record.  A durable, locked state ledger gives first-wins
behaviour across retries and process restarts.  Real Slack delivery is not part
of this worker: callers consume the JSONL outbox with the approved transport.
"""
from __future__ import annotations

import argparse, datetime as dt, fcntl, hashlib, json, os, re, tempfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SAFE_KINDS = {"set_intent_next_action", "prepare_local", "create_followup_question"}
PROTECTED = {"public", "permission", "cost", "external_send", "destructive"}
VALUE = re.compile(r"^[A-Za-z0-9:_-]{1,160}$")

def now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

def read_json(path: Path, default: Any) -> Any:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default

def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(temporary, path)

def append_jsonl(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(value, ensure_ascii=False, sort_keys=True) + "\n")

def key(event: dict[str, Any]) -> str:
    parts = [str(event.get(name, "")) for name in ("provider", "workspace_id", "channel_id", "message_ts", "thread_ts", "user_id", "value", "intent_id", "run_id", "question_id")]
    return hashlib.sha256("\x1f".join(parts).encode()).hexdigest()

def required(record: dict[str, Any]) -> str:
    for name in ("provider", "workspace_id", "channel_id", "message_ts", "thread_ts", "user_id", "value", "question_id"):
        if not record.get(name): return f"missing_{name}"
    if record.get("provider") != "slack": return "unsupported_provider"
    if not VALUE.fullmatch(str(record["value"])): return "invalid_value"
    return ""

def find_record(registry: Path, event: dict[str, Any]) -> dict[str, Any] | None:
    for line in registry.read_text(encoding="utf-8").splitlines() if registry.exists() else []:
        item = json.loads(line)
        if item.get("question_id") == event.get("question_id") and item.get("value") == event.get("value"):
            return item
    return None

def register(record: dict[str, Any], registry: Path) -> dict[str, Any]:
    """Persist the sent outbound binding; sender supplies the returned message ts."""
    error = required(record)
    if error: raise ValueError(error)
    if record.get("status") != "sent" or not record.get("intent_id") or not record.get("next_action"):
        raise ValueError("invalid_outbound_record")
    if record.get("expires_at", "") <= now(): raise ValueError("expired_outbound_record")
    record = {**record, "registry_id": record.get("registry_id") or hashlib.sha256(key(record).encode()).hexdigest(), "registered_at": now()}
    if find_record(registry, record): raise ValueError("duplicate_outbound_binding")
    append_jsonl(registry, record)
    return {"result": "registered", "registry_id": record["registry_id"]}

def validate(event: dict[str, Any], record: dict[str, Any] | None) -> str:
    error = required(event)
    if error: return error
    if event.get("interactionType") != "block_action" or event.get("actionType") != "button": return "unsupported_action"
    if event.get("signature_verified") is not True: return "signature_unverified"
    if not record: return "unmatched_message"
    if record.get("status") != "sent": return "outbound_not_sent"
    for name in ("provider", "workspace_id", "channel_id", "message_ts", "thread_ts", "user_id", "value", "question_id", "intent_id", "run_id"):
        if str(record.get(name, "")) != str(event.get(name, "")): return "wrong_" + name
    if record.get("expires_at", "") <= now(): return "expired"
    return ""

def update_intent(intents: Path, intent_id: str, next_action: str, callback_id: str) -> str:
    text = intents.read_text(encoding="utf-8")
    pattern = re.compile(rf"(^### \[{re.escape(intent_id)}\][\s\S]*?)(?=^### |^## |\Z)", re.M)
    match = pattern.search(text)
    if not match: raise ValueError("intent_not_open")
    block = match.group(1)
    block = re.sub(r"^- next_action:.*$", f"- next_action: {next_action}", block, flags=re.M)
    if "- next_action:" not in block: block += f"- next_action: {next_action}\n"
    block = re.sub(r"^- callback_last_event:.*$", f"- callback_last_event: {callback_id}", block, flags=re.M)
    if "- callback_last_event:" not in block: block += f"- callback_last_event: {callback_id}\n"
    intents.write_text(text[:match.start()] + block + text[match.end():], encoding="utf-8")
    return f"Intent {intent_id}의 next_action을 연결했습니다."

def mark_waiting(intents: Path, intent_id: str, callback_id: str, reason: str) -> None:
    """Make an interrupted callback visible without replaying any side effect."""
    text = intents.read_text(encoding="utf-8")
    pattern = re.compile(rf"(^### \[{re.escape(intent_id)}\][\s\S]*?)(?=^### |^## |\Z)", re.M)
    match = pattern.search(text)
    if not match: return
    block = match.group(1)
    block = re.sub(r"^- status:.*$", "- status: waiting", block, flags=re.M)
    if "- status:" not in block: block += "- status: waiting\n"
    for field, value in (("waiting_on", "agent"), ("blocker", f"callback {callback_id} {reason}"), ("next_action", "운영자가 callback receipt 상태를 확인한 뒤 별도 승인·재개 결정을 기록한다.")):
        block = re.sub(rf"^- {field}:.*$", f"- {field}: {value}", block, flags=re.M)
        if f"- {field}:" not in block: block += f"- {field}: {value}\n"
    text = text[:match.start()] + text[match.end():]
    marker = "## Waiting\n"
    if marker not in text: raise ValueError("missing_waiting_section")
    intents.write_text(text.replace(marker, marker + "\n" + block + "\n", 1), encoding="utf-8")

def result_message(record: dict[str, Any], state: str, detail: str) -> str:
    label = record.get("label") or record["value"]
    if state == "approval_required":
        return f"선택을 받았습니다: ‘{label}’. 이 선택은 공개·권한·비용 또는 외부 영향 경계를 포함할 수 있어 자동 실행하지 않았습니다. 승인 필요: {detail}"
    return f"선택을 받았습니다: ‘{label}’. 원 Intent {record.get('intent_id') or '없음'}와 다음 행동을 연결했습니다. 결과: {detail}"

def process(event: dict[str, Any], registry: Path, state_path: Path, intents: Path, outbox: Path, artifacts: Path, fail_after_outbox: bool = False, fail_after_dispatch: bool = False) -> dict[str, Any]:
    callback_id = str(event.get("event_id") or key(event))
    lock_path = Path(tempfile.gettempdir()) / ("infinity-slack-callback-" + hashlib.sha256(str(state_path.resolve()).encode()).hexdigest() + ".lock")
    with lock_path.open("w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        ledger = read_json(state_path, {"version": 1, "callbacks": {}, "questions": {}})
        callbacks, questions = ledger["callbacks"], ledger["questions"]
        if callback_id in callbacks:
            existing = callbacks[callback_id]
            if existing.get("state") in {"claimed", "dispatched", "receipt_written"}:
                reason = "dispatch_uncertain" if existing.get("state") == "dispatched" else "delivery_unknown"
                mark_waiting(intents, str(existing.get("intent_id") or event.get("intent_id") or ""), callback_id, reason)
                existing["state"] = reason
                existing["stages"] = list(existing.get("stages", [])) + [reason]
                existing["recovery_at"] = now()
                write_json(state_path, ledger)
                return {**existing, "result": reason}
            return {**callbacks[callback_id], "result": "duplicate_ignored"}
        record = find_record(registry, event)
        error = validate(event, record)
        base = {"callback_id": callback_id, "received_at": now(), "thread": {"channel_id": event.get("channel_id"), "thread_ts": event.get("thread_ts")}, "stages": ["received"]}
        if error:
            base.update({"state": "rejected", "reason": error, "stages": ["received", "rejected"]}); callbacks[callback_id] = base; write_json(state_path, ledger); return {**base, "result": "rejected"}
        question_id = record["question_id"]
        if question_id in questions:
            base.update({"state": "duplicate_ignored", "reason": "first_wins", "stages": ["received", "duplicate_ignored"]}); callbacks[callback_id] = base; write_json(state_path, ledger); return {**base, "result": "duplicate_ignored"}
        questions[question_id] = callback_id
        # Persist a first-wins claim *before* any Intent, artifact, or delivery
        # side effect.  A crash after this point is deliberately not retried: the
        # next worker sees ``claimed`` and leaves an uncertain receipt for an
        # operator instead of creating a second thread response.
        base.update({"state": "claimed", "intent_id": record.get("intent_id"), "stages": ["received", "bound", "claimed"]})
        callbacks[callback_id] = base
        write_json(state_path, ledger)
        action = record.get("next_action") or {}
        kind, boundary = action.get("kind"), action.get("approval_boundary", "safe")
        if kind not in SAFE_KINDS or boundary in PROTECTED:
            detail = action.get("approval_reason") or "별도 명시 승인이 필요합니다."
            base.update({"state": "approval_required", "outcome": "approval_required", "intent_id": record.get("intent_id"), "next_action": action, "stages": ["received", "bound", "claimed", "approval_required", "reported"]})
        else:
            try:
                detail = update_intent(intents, record["intent_id"], action["next_action"], callback_id)
            except (KeyError, ValueError) as exc:
                base.update({"state": "dispatch_uncertain", "reason": str(exc), "stages": ["received", "bound", "claimed", "dispatch_uncertain"]})
                callbacks[callback_id] = base
                write_json(state_path, ledger)
                return {**base, "result": "rejected"}
            base.update({"state": "dispatched", "outcome": "dispatched", "intent_id": record["intent_id"], "next_action": action, "stages": ["received", "bound", "claimed", "dispatched"]})
            callbacks[callback_id] = base
            write_json(state_path, ledger)
            if fail_after_dispatch:
                raise RuntimeError("simulated_crash_after_dispatch")
        report = artifacts / str(record.get("intent_id") or "unbound") / "slack-callbacks" / f"{callback_id}.json"
        write_json(report, {"record": record, "event": event, "result": base})
        base["report_path"] = str(report)
        callbacks[callback_id] = base
        append_jsonl(outbox, {"destination": {"channel": "slack", "target": event["channel_id"], "reply_to": event["thread_ts"]}, "message": result_message(record, base["state"], detail), "callback_id": callback_id, "state": base["state"]})
        base["state"] = "receipt_written"
        base["stages"] = list(base["stages"]) + ["receipt_written"]
        callbacks[callback_id] = base
        write_json(state_path, ledger)
        if fail_after_outbox:
            raise RuntimeError("simulated_crash_after_outbox")
        base["state"] = "reported"
        base["stages"] = list(base["stages"]) + ["reported"]
        callbacks[callback_id] = base
        write_json(state_path, ledger)
        return {**base, "result": "accepted"}

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True); mode.add_argument("--event", type=Path); mode.add_argument("--register", type=Path)
    parser.add_argument("--registry", type=Path, default=ROOT / "data/slack-outbound-buttons.jsonl")
    parser.add_argument("--state", type=Path, default=ROOT / "data/slack-callback-state.json"); parser.add_argument("--intents", type=Path, default=ROOT / "INTENTS.md")
    parser.add_argument("--mock-outbox", type=Path, default=ROOT / "data/slack-callback-outbox.jsonl"); parser.add_argument("--artifacts", type=Path, default=ROOT / "artifacts"); parser.add_argument("--test-fail-after-outbox", action="store_true"); parser.add_argument("--test-fail-after-dispatch", action="store_true")
    args = parser.parse_args()
    try:
        result = register(read_json(args.register, {}), args.registry) if args.register else process(read_json(args.event, {}), args.registry, args.state, args.intents, args.mock_outbox, args.artifacts, args.test_fail_after_outbox, args.test_fail_after_dispatch)
    except ValueError as exc:
        result = {"result": "rejected", "reason": str(exc)}
    print(json.dumps(result, ensure_ascii=False)); return 0
if __name__ == "__main__": raise SystemExit(main())
