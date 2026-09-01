# Infinity terminal notification contract

## Eligibility

- Intake preserves `notification_channel`, `notification_target`, original message identity, and an optional Telegram `notification_thread` or Slack `notification_reply_to`.
- The reconciler reads **only** `origin/main:INTENTS.md`. Archive is eligible only with `remote_verified: pass|true|verified`; Waiting is eligible only with an explicit blocker or a user approval requirement.
- Read/no-op/repeated run/subagent completion/local-only completion and legacy entries without an origin never emit a message.

## Delivery receipt

`data/dispatcher-terminal-notifications.json` uses SHA-256 of `(intent id, terminal state, channel, target, thread/reply origin)`. A lock and atomic pre-send receipt prevent concurrent replay. Successful and ambiguous provider results are never replayed automatically. A known pre-acceptance transport error retries on the next reconcile.

The provider has no idempotency key, so a process crash during a provider call cannot be proven exactly-once. The dispatcher records `delivery_unknown`, exits non-zero, and lets the bounded cron failure alert surface the receipt for manual resolution instead of silently sending a duplicate or discarding it.

## Regression contract

`python3 scripts/test_dispatch_terminal_notifications.py` uses only a JSONL mock outbox and proves archive once/replay zero, waiting once, no-op zero, missing origin zero, Slack reply metadata, concurrent replay suppression, and known pre-acceptance retry.
