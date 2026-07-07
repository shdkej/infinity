# ops-06 weekly_review same-week replacement contract

- Target file: `system/data/weekly_review.md`
- Canonical weekly heading shape: `### YYYY-Www (YYYY-MM-DD ~ YYYY-MM-DD)`
- Manual-note heading shape: any same-week heading that does not match the canonical date-range form, for example `### 2026-W20 수동 생활/소비 메모 (...)`

## Gate

Before a weekly review generator writes a block, it must treat the ISO week id as a key.

1. Generate one complete canonical block for the target week.
2. Search existing `weekly_review.md` for headings matching `### {week} (YYYY-MM-DD ~ YYYY-MM-DD)`.
3. If none exist, append the generated canonical block once.
4. If one or more exist, replace the first canonical block with the generated block and remove any additional canonical blocks for the same week.
5. Preserve same-week manual-note blocks because they are not canonical weekly summaries.
6. Fail the run if the resulting file has anything other than exactly one canonical block for the target week.

## Local helper

`scripts/weekly_review_block_gate.py` implements the replacement/count check as a small deterministic helper. It can be used by the generator directly or as a pre-commit/dry-run gate:

```bash
python3 scripts/weekly_review_block_gate.py \
  /home/ubuntu/.openclaw/workspace/system/data/weekly_review.md \
  2026-W27 \
  /tmp/generated-weekly-block.md
```

The helper reports `PASS canonical block count for {week}: 1` only when the output contract is satisfied.
