# Implementation notes — infinity-notification-reliability-20261107

## Scope

The assigned route is Genie direct for the Infinity-owned repository: the intent targets `genie`, is tagged `projects: [infinity]`, and explicitly supplies the task-specific detached checkout. The executor registry is for other registered product projects; no extra executor hop or persistent agent workspace is created.

## Changes in the isolated checkout

- Added per-send (20 s), per-Git-operation (10 s), internal total-run (110 s), and wrapper hard-stop (120 s) bounds.
- Added structured, redacted stderr events with intent ID and truncated receipt hash. Message body, target/thread fields and credential-like values are omitted/redacted.
- Send timeout, CLI nonzero, malformed/lost/unconfirmed response are durable `delivery_unknown`; only a confirmed transport process launch failure or an expired pre-invocation budget is retryable.
- Preserved receipt identity and pre-send persistence, eligibility, and locking/concurrency behavior. Both state-change and terminal notices use the intake-captured origin channel/target/thread; legacy override flags are ignored and removed from the cron invocation so global defaults cannot redirect notices. Added retry handling for receipts proven pre-acceptance.
- Setup failures now return nonzero structured events; lock contention remains a structured no-op.

## Validation

Latest verification: `python3 -m py_compile scripts/dispatch_terminal_notifications.py scripts/test_dispatch_terminal_notifications.py` and `python3 scripts/test_dispatch_terminal_notifications.py` passed (19 tests), including legacy-override-plus-origin-Telegram-address/thread regressions for terminal and state-change notices; `bash -n scripts/run_notification_cron.sh` passed; `python3 scripts/check_intents_consistency.py INTENTS.yaml` passed; `python3 scripts/validate_intent_trace.py data/traces/infinity-notification-reliability-20261107.json` passed; `git diff --check` passed. Validation uses the JSONL mock outbox plus local fake CLI/Git executables only.

Red reviews found global overrides could redirect both state-change and terminal notices, dropping origin routing metadata. Both paths now use the origin address/thread and ignore legacy override flags; the cron wrapper no longer supplies default destination arguments. The mock regression suite is rerun; independent Red re-review is pending. No commit/push/publish, live Telegram send, cron setting edit, credential/config change, or runtime restart has occurred.
