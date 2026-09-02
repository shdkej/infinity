# Intent trace contract

`traces/{intent-id}.json` is the durable, dashboard-readable timeline for one
Infinity intent.  It supplements `INTENTS.md`; it does not replace lane state
or the final HTML report.

## Required shape

```json
{
  "schema_version": 1,
  "intent_id": "example-01",
  "status": "active",
  "trace_completeness": "complete",
  "request": {
    "raw": {"status": "recorded", "value": "user wording"},
    "normalized_query": {"status": "recorded", "value": "work query"}
  },
  "events": [
    {"type": "intake", "at": "2026-09-02T00:00:00Z", "context_pack": "intents/context/example.json"},
    {"type": "execution", "at": "2026-09-02T00:01:00Z", "context_pack": "intents/context/example.json", "evidence_paths": ["reports/example/run.html"], "searches": ["declared knowledge search"]},
    {"type": "archive", "at": "2026-09-02T00:02:00Z", "report_path": "reports/example/final.html", "verification": {"red_status": "pass", "remote_verified": "pass"}}
  ],
  "artifacts": [],
  "verifications": [],
  "next_decision": {"status": "continue", "value": "next action"}
}
```

`status` is one of `inbox`, `active`, `waiting`, or `archived`. Every trace has
**exactly one** intake event and recorded raw/normalized request values for new
intakes. Every execution event has a Context Pack, one or more actual search
terms, and one or more evidence paths. An archive event has the final
`report_path`, Red pass, and remote verification pass; an archived trace has
exactly one archive event. Active traces must not pretend they are archived.

## Recording commands

Use the writer rather than hand-editing a new timeline, then validate it:

```bash
python3 scripts/record_intent_trace.py intake --intent-id example-01 \
  --raw 'user request' --query 'normalized task' \
  --context-pack intents/context/example-01.json --evidence INTENTS.md \
  --next-decision 'Start Planner review'
python3 scripts/record_intent_trace.py execution --intent-id example-01 \
  --context-pack intents/context/example-01.json --evidence reports/example/run.html \
  --search 'declared knowledge query' --next-decision 'Request Red review'
python3 scripts/record_intent_trace.py archive --intent-id example-01 \
  --report-path reports/example/final.html --artifact 'final report=reports/example/final.html' \
  --next-decision 'Monitor the implemented result'
python3 scripts/validate_intent_trace.py --all
```

The writer does not move an `INTENTS.md` lane or assert a remote commit; it
records the proof supplied by the workflow. Record the archive event only after
the normal Archive remote-verification gate has passed.

Dispatcher acceptance is recorded as a `dispatcher_handoff` event. It contains
the dispatcher `run_id`, `canonical_sha`, `agent`, `session_key`, UTC
`timestamp` (UTC `Z` suffix), a 40-character lowercase Git SHA, and
`status: "accepted"`; it documents custody without changing the intent
lifecycle. The dashboard renders this event in the separate **운영 인계**
trace stage as a custody record.

An archive writer cannot infer a pass: callers must supply existing
`--red-report-path` and `--remote-proof-path` files. The archive event stores
both paths alongside its `pass` values, and the validator rejects a terminal
pass without those local evidence records. Historical `partial` backfills may
preserve an explicitly documented missing proof; they cannot be written by the
current archive writer.

## Historical backfill

For a legacy intent, a field whose original source cannot be proved is an
object with `status: "missing"` and a concrete `reason`; it is never invented.
Set `trace_completeness` to `partial` and include a `backfill` event that names
the source records used.  Existing artifact, report, and Red paths remain
recordable when they exist.

Run `python3 scripts/validate_intent_trace.py --all` after recording a trace.
The validator checks schema shape, event ordering, terminal-state consistency,
and referenced local evidence paths.  It deliberately derives no business
facts from a dashboard render.
