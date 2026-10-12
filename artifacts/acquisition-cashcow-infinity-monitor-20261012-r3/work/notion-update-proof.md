# Notion update proof — r3

- DB: `3f517bf7-599f-8176-8e1a-cddf002cf70b`
- Baseline: 9 fields, 16 rows (r2 evidence)
- New promoted: 0; held leads recorded: 5; Notion create: 5; existing row mutation: 0
- Schema, permissions, and schedule: unchanged
- Deduplication key: platform + direct URL/listing ID + normalized title; list-root-only items were not promoted.
- Policy correction: promotion and lead capture are separate. No candidate met all public-source gates, but five non-duplicate held leads were added as `신규 검토`; their `플랫폼` text records `검증 필요` or `보류` and the reason.
- Baseline verification: 16 rows before, 21 after; the original 16 rows remain unchanged. Full per-lead evidence and Notion URLs: `work/notion-held-leads-update.md`.
