# Infinity terminal notification contract

## Eligibility

- Intake preserves `notification_channel`, `notification_target`, original message identity, and an optional Telegram `notification_thread` or Slack `notification_reply_to`.
- Both state-change and terminal notices use that captured origin. A global terminal destination must not redirect an intent; legacy terminal override CLI flags are accepted but ignored.
- The reconciler reads **only** `origin/main:INTENTS.md`. Archive is eligible only with `remote_verified: pass|true|verified`; Waiting is eligible only with an explicit blocker or a user approval requirement.
- Read/no-op/repeated run/subagent completion/local-only completion and legacy entries without an origin never emit a message.

## Delivery receipt

`data/dispatcher-terminal-notifications.json` uses SHA-256 of `(intent id, terminal state, channel, target, thread/reply origin)`. A lock and atomic pre-send receipt prevent concurrent replay. Successful and ambiguous provider results are never replayed automatically. A known pre-acceptance transport error retries on the next reconcile.

The provider has no idempotency key, so a process crash during a provider call cannot be proven exactly-once. The dispatcher records `delivery_unknown`, exits non-zero, and lets the bounded cron failure alert surface the receipt for manual resolution instead of silently sending a duplicate or discarding it.

## Bounded failure and retry policy

- The cron wrapper bounds the complete dispatcher process at 120 seconds; the Python dispatcher enforces a 110-second deadline, including receipt-lock waits, with a 20-second send timeout and a 10-second timeout for each Git operation. The shorter internal deadline leaves time for durable receipt updates and the outer timeout remains a last-resort hard stop.
- Send timeouts, non-zero CLI exits, empty/unconfirmed responses, and malformed responses are `delivery_unknown`. Their receipt records the failure class before the run exits non-zero; replay remains suppressed.
- `failed_before_acceptance` is reserved for evidence that the transport process never started (`OSError`) or a send was declined before invocation because the internal run deadline had already elapsed. A CLI non-zero exit alone does not prove non-acceptance and is not retryable. Legacy receipts without an explicit pre-acceptance failure class are migrated to non-replayable `delivery_unknown`.
- Structured stderr events include the intent ID, a truncated receipt hash, phase, failure class, elapsed time/exit status, and a redacted/truncated stderr excerpt. Message text, target/thread addresses, and credentials are omitted/redacted.
- NVM/OpenClaw/timeout setup errors and state/lock path failures return non-zero structured errors. Lock contention remains an intentional zero-exit skip with a structured event.

## Regression contract

`python3 scripts/test_dispatch_terminal_notifications.py` uses a JSONL mock outbox and local stub processes only; it proves archive once/replay zero, waiting once, no-op zero, missing origin zero, Slack reply metadata, terminal and state-change origin routing despite legacy override arguments, concurrent replay suppression, pre-acceptance retry, ambiguous non-zero/malformed/timeout outcomes without replay, bounded Git/run timeout, and non-zero structured setup failure. It never sends a live Telegram message.
