# Status priority correction — 2026-10-12

## Scope

This follow-up corrects the prior request: the existing `상태` select is the user-facing priority field. The newly-created `추천 별점` field was used only as the already-recorded row-level evaluation input and then removed; the original `별점` field remains source-rating-only.

## Live schema and mapping

- Database: `3f517bf7-599f-8176-8e1a-cddf002cf70b`
- Data source: `3f517bf7-599f-81f5-9012-000b55d8de7e`
- Existing options observed before mutation: `1순위`, `2순위`, `후순위`, `제외`, `신규 검토`.
- Mapping applied to all 382 rows: `5→1순위`, `4→2순위`, `3→후순위`, `2→후순위`, `1→제외`.
- Result: `1순위 82`, `2순위 159`, `후순위 138`, `제외 3`, `신규 검토 0`.
- `추천 별점` deletion response returned the database schema without that property; `별점:number` remained.

## Live query proof

Status-ascending data-source query used four pages (`100,100,100,82`), returned **382 rows**, and ended with `has_more=false`. The result was monotonic in the declared option order and had `상태` filled `382/382`. `사용자 맞춤 코멘트` was filled `382/382`, and the priority-reason marker was present `382/382`.

- Query response SHA-256: `cb754f8a17e119cc5f0cb8c8c52e73b0e363148e4f95a72d0ee2ab5a0505c838`
- Original `별점`: verified numeric `20`, unconfirmed/null `362`; no source rating was backfilled.
- Current schema has no `추천 별점`; original `별점`, `별점 근거/출처`, and other pre-existing properties remain.

## Role reviews

- Planner: the correction target is the existing state option, with an explicit score-to-priority mapping and no source-rating mutation.
- Developer: paginated live reads preceded writes; each page was patched for `상태` and comment rationale, then schema deletion and a second paginated verification were run.
- Marketer: `1순위`/`2순위`/`후순위`/`제외` is clearer to the user than exposing a temporary numeric recommendation field; comments retain row-level reasons.
- Operator: the write is bounded to the target DB, original `별점` is preserved, schema deletion is verified, and unrelated dirty worktree files were not touched.

## Red four-sentence verification

PASS: The live schema contains the original `별점:number` and no `추천 별점` field. PASS: The status-sorted live query returned 382/382 rows with `has_more=false`, monotonic priority order, and `상태` plus priority rationale filled 382/382. PASS: Original source-rating evidence remains separated as 20 verified and 362 unconfirmed, with no inferred rating written into `별점`. PASS: The mapping and deletion are consistent with the correction request; only the lack of an independent raw-source-to-row manifest remains a limitation.
