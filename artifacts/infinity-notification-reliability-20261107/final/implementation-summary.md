# Infinity notification reliability — implementation summary

## Outcome

The terminal-notification dispatcher now bounds each send (20 seconds), each Git operation (10 seconds), and the whole Python run (110 seconds), under a 120-second cron hard stop. Ambiguous send outcomes are persisted as non-replayable `delivery_unknown` receipts, emit redacted structured diagnostics, and exit nonzero. Automatic retry is limited to positively established pre-acceptance failures. Setup failures no longer report success.

Both state-change and terminal notices use the intent's intake-captured destination and Telegram thread or Slack reply metadata. Global destination defaults were removed from the cron invocation; legacy CLI override flags remain accepted but cannot redirect notices. Eligibility, receipt identity/persistence, locking, concurrency suppression, and at-most-once behavior are retained.

## Verification

- 19 mock-only regression tests passed, including timeout/ambiguous no-replay cases, setup failure, concurrency, and origin address/thread preservation for state-change and terminal notices despite legacy override arguments.
- Python compilation, cron shell syntax, INTENTS consistency, trace validation, and `git diff --check` passed.
- Independent Red re-review passed with no remaining scoped P1/P2 findings: [review](../work/red/final-review.md).

No live Telegram notification was sent. No cron settings, credentials, runtime configuration, or Gateway process were changed.

## Changed implementation paths

- `scripts/dispatch_terminal_notifications.py`
- `scripts/run_notification_cron.sh`
- `scripts/test_dispatch_terminal_notifications.py`
- `artifacts/infinity-dispatcher-notify/notification-contract.md`
