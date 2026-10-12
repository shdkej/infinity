# Notion live verification — r3 correction (2026-10-12)

This artifact supersedes the conflicting 21-row claim in the original r3 report. The live Notion API was queried directly for database `3f517bf7-599f-8176-8e1a-cddf002cf70b` using pagination (`page_size=100`) until `has_more=false`.

## Live result

- Query result rows: **382**
- Rows carrying the full-pagination marker: **361**
- Remaining legacy rows: **21**
- Full-pagination rows by platform: Fello **69**, Sellernet **59**, Flippa **114**, Empire Flippers **29**, Quiet Light **90**
- Full-pagination rows with a source URL: **361/361**
- Full-pagination source URL values: **361 rows, 351 unique URL values**
- Repeated source URL groups: **10 duplicate rows**, caused by shared list-root URLs (for example Flippa list roots and `https://www.fello.io/products`). This means URL uniqueness is **not** proven for every row; the previous blanket deduplication claim is withdrawn.
- Extracted Empire Flippers listing IDs: **29 rows / 29 unique IDs**
- Query response evidence hash: `1f3c89806de48c9c5761f219fa33dc8e8d04d66871edee3f64487a543372606d`

The 361 created/marked rows are present in the live database query. However, the repository does not contain a 361-item source manifest, so this check proves database presence and marker/source coverage, not an independent raw-pagination-to-row bijection.

## Live schema

The database has exactly these nine properties:

`후보명:title`, `매입가(만원):number`, `월매출(만원):number`, `월이익(만원):number`, `적합도:number`, `플랫폼:rich_text`, `출처:url`, `상태:select`, `최종 확인:date`.

There is no native `별점` or `rating` property. Fello source scores observed in the live rows are recorded in the `플랫폼` text (for example `원본 별점 5.0 (appReviewMetrics)`); rows without a source rating are marked `미평가`. `적합도` was not used as a rating field. A native rating-descending Notion sort/view is therefore unavailable without a schema change, which was not made.

## Correction

The prior r3 final report's “16→21” and “five writes” statements described the earlier representative/held-lead state and conflict with the later full-list write. They are corrected here: the current live state is **21 legacy rows + 361 full-pagination rows = 382 rows**. The earlier five-only truncation was an incorrect intermediate result. The URL-duplicate caveat above remains unresolved and must not be reported as fully deduplicated until a source manifest and direct-URL repair are available.
