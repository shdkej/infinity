# Safety Map Experiment 03 — Planner PRD

- intent: `safety-map-experiment-03-20260905`
- identity: **experiment-03**; new build, not an experiment-02 extension
- deadline: `2026-09-06T06:00:00Z` / `08:00 Europe/Rome`
- context pack: `intents/context/safety-map-experiment-03-20260905.json`

## Goal

Build a new full-viewport global map experience. The live Mapbox canvas is the **FocusField**, not a decorative preview. A Typography Rail supplies the purpose, an action prompt, and a clear no-data safety boundary.

## Experience contract

1. On entry, users see a global map, the sentence “어디를 지나갈지, 먼저 지도에서 살펴보세요.”, and one place/road search action.
2. Search focuses a public place or road; user can zoom and pan naturally.
3. A restrained layer control changes the base-map expression, never a safety claim.
4. Place context is revealed only after selection; it must include the statement that there is no verified street/block/incident safety signal.
5. The product does not collect location, submit reports, rank safety, recommend routes, or claim real-time coverage.

## Acceptance criteria

| ID | Requirement | Evidence |
|---|---|---|
| UX-01 | Full-bleed Mapbox GL canvas is visibly the main scene on desktop and 390px. | Actual browser captures |
| UX-02 | Search, place/road focus, zoom, pan and layer interaction work in a real canvas. | Interaction captures and browser checks |
| UX-03 | Top text rail retains purpose, next action and no-data boundary without covering the map. | Desktop/390px review |
| UX-04 | No safety rating, prediction, safe-route claim, live incident claim or personal-location capture appears. | Copy/provenance inspection |
| UX-05 | Keyboard focus, labels, reduced-motion and mobile overflow pass. | Browser/accessibility evidence |
| OPS-01 | Public token is runtime-injected only; no value appears in tracked content/logs/reports. | Diff/provenance check |
| OPS-02 | New experiment-03 structure leaves dirty legacy `sites/safety-map` paths unmodified. | Git path-level diff |
| REL-01 | Formal deploy, live behavior, relevant push/remote checks and Slack thread receipt complete before deadline. | Remote/liveness/receipt proof |

## New-structure and legacy-protection decision

The current `sites/safety-map/index.html`, `app.js`, `styles.css`, `dist/*`, and smoke test are already modified user/legacy paths. They are **read-only comparison material**. Developer must first inspect registry/deploy configuration, then create a sibling experiment-03 site directory and its independently named build/runtime/evidence surfaces. Only shared deployment wiring that is proven necessary may change, and it must be staged by explicit path after confirming no unrelated diff.

## Design system mapping

- **Canvas:** white + subtle-sky ambient depth; map supplies geographic depth, not cards.
- **Typography Rail:** Pretendard, one hero statement, small location/date coordinates.
- **FocusField:** map takes the viewport; no dashboard grid or permanent card stack.
- **Context Object:** selected place information appears on demand and can dismiss.
- **Action Prompt:** sentence-led search/layer controls with tactile, accessible controls only where needed.
- **No-data:** present, readable, non-alarmist; it names the missing evidence and preserves exploration.

## Role handoffs

| Role | Required independent contribution |
|---|---|
| Planner | Validate scope, criteria, task dependencies and cut unnecessary screens. |
| Developer | Implement independent experiment-03 surface, tests, and reversible build/deploy path. |
| Marketer | Audit first five seconds, Korean microcopy, warmth and claim boundaries. No public copy send. |
| Operator | Verify token/config boundary, path isolation, formal deploy, remote state and deadline receipts. |
| Red | Directly inspect desktop/390 captures and live interaction for hierarchy, collision, claims and safety boundaries. |

## Known blocker

This PRD is created before implementation because this runtime exposes neither role-session spawn nor Slack thread-send. Per Infinity contract, implementation must not silently downgrade to a single-agent build; resume only after all role and Red sessions can be launched.
