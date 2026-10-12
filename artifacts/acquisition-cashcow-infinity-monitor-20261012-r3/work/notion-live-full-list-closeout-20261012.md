# Notion live full-list closeout evidence — 2026-10-12

- Intent lineage: `acquisition-cashcow-infinity-monitor-20261012-r3` (corrective closeout)
- Database: `3f517bf7-599f-8176-8e1a-cddf002cf70b`
- Data source: `3f517bf7-599f-81f5-9012-000b55d8de7e`
- Query: `ntn datasources query <data-source-id> --limit 500 --json`
- Live result: **382 rows**, `has_more=false`
- Raw query capture SHA-256: `413c097a965726d1e70c65940258fdf8f723bb95b2bb39714caceb2d911d85f3`
- Row ledger: `work/notion-live-row-ledger-20261012.jsonl` (382 lines)
- Row ledger SHA-256: `26211bb4d5ea9cc2d222a665a11b5412d7c049cff7d1fc3f0a72075b3af95f09`

## Field and marker coverage

- Native properties present: `별점:number`, `별점 근거/출처:rich_text`, `사용자 맞춤 코멘트:rich_text`, `판단 상태/신뢰도:rich_text`
- All 382 rows: source URL 382/382, rating evidence 382/382, fit comment 382/382, judgment state/confidence 382/382.
- Rating values: 20 numeric source-confirmed values; 362 explicitly `미확인` (no inferred ratings).
- URL values: 382 present; 372 unique; **10 duplicate URL rows** remain, predominantly shared list-root URLs.
- The raw source-to-row manifest is absent. The ledger proves the 382 live Notion rows and their current field values, but does **not** independently prove a one-to-one bijection against every original pagination item.

## Native descending sort verification

A second live query with sort `별점 desc` returned 382 rows and `has_more=false`. The first values were `5, 5, 5, 5, 4.9, 4.8, 4.8, 4.7, 4.7, 4.7, 4.7, 4.3`. Sorted query capture SHA-256: `3d0009852c9b1097b61706c91653a1aaa987bafe6460a9d13e9d6f783a4115ac`.

## Correction and boundary

The earlier r3 artifact/report that described 16→21 and no rating schema is superseded for the live current state. The current state is 382 rows with the native rating and review fields above. Source manifest absence and the 10 duplicate URL rows remain open limitations; no claim of complete source-level deduplication is made.

## Red review status

A four-sentence Red review was requested, but this subagent runtime could not dispatch the request through the attributed inter-session messaging tool; the Gateway explicitly rejected the CLI fallback because it would lose inter-session attribution. Existing `work/red/final-review.md` is a stale r3 review of the earlier 21-row state and is not reused as current closeout evidence. Parent session must obtain and append the current four-sentence Red response before declaring final archive PASS.
