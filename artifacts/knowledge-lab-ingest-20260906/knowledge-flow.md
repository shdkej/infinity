# Knowledge flow receipt — 2026-09-06 Agent Wiki promotion

## Scope

This receipt preserves the completed Knowledge Lab maintenance run that published one reusable carousel-editing rule to Agent Wiki. It is a provenance record, not a claim that every reviewed source became long-term knowledge.

## Flow

1. **Source** — `knowledge-lab/source/openclaw-system/` recent changes were scanned. The decision review directly examined:
   - `source/openclaw-system/docs/INSTAGRAM_CAROUSEL_PROMPT_SYSTEM.md`
   - `source/openclaw-system/docs/INFINITY_OPERATING_RULES.md`
   - `source/openclaw-system/docs/LOCAL_REVIEW_AUTOMATION.md`
2. **Ingest decision** — the manifest contained 830 entries and no newly modified candidate. The three reviewed operating documents were evaluated as existing source material; the carousel contract contained one reusable, non-duplicative principle. The Infinity and local-review rules overlapped with already compiled routing/currentness rules, so they were not separately promoted.
3. **Compiled knowledge** — the selected principle was distilled into `agent-wiki/content/docs/insights/single-scene-single-criterion-carousel-contract.mdx`, then linked from `agent-wiki/content/docs/index.mdx` and recorded in `agent-wiki/content/docs/log.mdx`.
4. **Remote commits** — Agent Wiki commit `53fbe3ac22808662389fc869fc90e83b52b626e1` was pushed to `origin/main`; the Knowledge Lab submodule pointer was then committed and pushed as `cfaebe87501473b7238375eb60303fbbdd2e104e`.

## Decision boundary

- Promoted: one reusable rule — a carousel scene carries one judgment, with its supporting evidence and public-release gate.
- Retained without new page: currentness/routing and review automation rules that already had an equivalent compiled destination.
- Excluded: none.

## Traceability

Future Infinity intents that ingest or promote knowledge must create the same receipt at `artifacts/{intent-id}/knowledge-flow.md` under the `INFINITY_OPERATING_RULES.md` knowledge-flow receipt contract. This historical receipt has no retroactive intent id because the original maintenance run predated the explicit request to expose it in Infinity.
