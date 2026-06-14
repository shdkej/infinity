# marketing-59 — Virtue Launch-Ready PLG Signal Gate

**Status: PROCESSED** — Completed 2026-06-14T1200Z by Heartbeat Agent
**Archive**: `intents/archive/marketing-59.md`
**Artifact**: `artifacts/marketing-59/virtue-launch-ready-plg-signal-gate.md`
**Report**: `reports/marketing-59/2026-06-14T1200Z-local.html`

> Note: INTENTS.md Inbox entry could not be updated in this run due to file size constraint.
> The next Heartbeat should remove the marketing-59 Inbox entry from INTENTS.md.

---

Status: Inbox candidate (SUPERSEDED — see archive)
Created: 2026-06-14T10:00Z
Source note: `source/external-links/marketing/2026-06-14-plg-signal-hierarchy.md`

## Candidate

- Title: Virtue launch-ready PLG signal gate
- Rationale: 최신 PLG 자료는 signup/page view보다 first win, activation, product-qualified signal을 먼저 보라고 한다. Virtue는 prelaunch라 숫자 판정은 이르지만, launch 이후 무엇을 볼지와 지금 보류할 신호를 미리 분리해야 한다.
- Expected impact: 첫 10명 관찰에서 acquisition 문제, activation 문제, measurement-too-early 상태를 섞지 않고 구분한다.
- Permission level: L1 docs-only. 신규 이벤트, tracking/privacy, dashboard, public copy, deploy, external outreach, cost-bearing action 금지.
- Owner route: Infinity router -> Claude Code docs-only.
- Success criteria: 기존 J1/J2/J4=`deed_saved`, J3=`deed_judged` 매핑을 유지하면서 `지금 볼 신호 / 보류할 신호 / launch 이후 볼 신호` 표와 first-10 수기 review gate를 만든다.
- First verification gate: source note exists, referenced prior marketing contracts are not contradicted, conflict markers 0, and no production code or tracking/privacy files changed.

## Notes

- Fit current stage: prelaunch / low-signal learning mode.
- Use prior artifacts where relevant: marketing-55, marketing-56, marketing-58.
- Keep PostHog as read-only future checklist unless access and project id are explicitly available; do not invent metrics.
