# Recommendation-rating follow-up — 2026-10-12

## Live Notion evidence

- Database: `3f517bf7-599f-8176-8e1a-cddf002cf70b`
- Data source: `3f517bf7-599f-81f5-9012-000b55d8de7e`
- Query: `ntn datasources query 3f517bf7-599f-81f5-9012-000b55d8de7e --limit 500 --sort '추천 별점 desc' --json`
- Rows: **382**; `has_more=false`; descending sort verified.
- Recommendation field: native number `추천 별점`, filled **382/382**.
- Recommendation distribution: 1점 **3**, 2점 **117**, 3점 **21**, 4점 **159**, 5점 **82**.
- `사용자 맞춤 코멘트` with score reason: **382/382**.
- Original native `별점`: numeric verified **20**, unconfirmed/null **362**. The original field was not changed.

## Schema snapshot

The live data source contains the original native `별점:number`, `별점 근거/출처:rich_text`, and `사용자 맞춤 코멘트:rich_text`, plus the newly added `추천 별점:number`. The recommendation field is separate from original source rating and is not used to backfill `별점`.

## Scoring basis

Each score was calculated from row data: purchase price against the KRW 30,000,000 budget, available revenue/profit and margin, existing suitability value when present, content/app/AI connection cues, and explicit operating/transfer/verification risk cues. Each comment appends `추천 별점 N/5` and the row-specific reasons; no blanket score was assigned.

## Scope note

This follow-up is a live Notion mutation and verification artifact. Repository dirty state includes unrelated pre-existing changes; commit verification is scoped to this artifact.
