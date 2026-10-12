# Service description closeout — 2026-10-12

## Scope

- Target data source: `3f517bf7-599f-81f5-9012-000b55d8de7e`
- Target database: `3f517bf7-599f-8176-8e1a-cddf002cf70b`
- User request: add a short explanation of what each service does.
- Mutation boundary: existing `사용자 맞춤 코멘트` only. No new property and no `상태` mutation.

## Live verification

- Live rows queried: **382**
- `서비스 설명:` marker present: **382/382**
- Missing descriptions: **0**
- `상태` filled: **382/382**
- `추천 별점` property present: **0**
- Property count: **11**, unchanged from the current live schema:
  `후보명`, `플랫폼`, `출처`, `매입가(만원)`, `월매출(만원)`, `월이익(만원)`, `적합도`, `상태`, `최종 확인`, `사용자 맞춤 코멘트`, `판단 상태/신뢰도`.

## Content rule

Descriptions use the candidate title and existing public listing context. They state the service category/function conservatively; customer and revenue model are explicitly marked as requiring source-detail confirmation when not directly available. No unsupported operating or financial claim was added.

## Readability correction — 2026-10-12

The first version was too generic to identify the service from the row. It was replaced in the existing `사용자 맞춤 코멘트` property with a reader-first structure: `한줄 설명` → `주 사용자는 / 실제로는` → `돈을 버는 방식` → `인수 후 운영` → `근거와 한계`.

- Live writes: **382/382** rewrites completed.
- Live rows after rewrite: **382**.
- `서비스 설명` marker count: **exactly 1 in 382/382 rows**; duplicate legacy blocks removed.
- `상태`: filled **382/382**.
- Property count: **11 in 382/382 rows**; non-comment property changes: **0**.
- The account/customer and revenue wording remains conservative when the title/listing does not establish it.
- Direct machine evidence: `work/notion-readable-description-closeout-20261012.json` and `work/notion-readable-description-verification-20261012.json`.
