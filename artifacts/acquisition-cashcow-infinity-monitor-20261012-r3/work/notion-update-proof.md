# Notion update proof — r3

- DB: `3f517bf7-599f-8176-8e1a-cddf002cf70b`
- Baseline: 9 fields, 16 rows (r2 evidence)
- New promoted: 0; Notion create/update: 0; existing row mutation: 0
- Schema, permissions, and schedule: unchanged
- Deduplication key: platform + direct URL/listing ID + normalized title; list-root-only items were not promoted.
- Reason for no-op: no candidate met all public-source gates (direct detail, price ≤ KRW 30m, financial signal, operating burden/transfer scope).
