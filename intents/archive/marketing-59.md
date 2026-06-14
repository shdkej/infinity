# marketing-59: Virtue Launch-Ready PLG Signal Gate

- id: marketing-59
- status: archived
- completed_at: 2026-06-14T1200Z
- projects: [virtue]
- task_type: strategy
- topics: [plg, activation, measurement, prelaunch]
- result_summary: Virtue prelaunch PLG 신호를 지금볼/보류/launch후 3층으로 분리하고 first-10 수기 review gate 7항목 작성. J1/J2/J4=deed_saved, J3=deed_judged 매핑 유지. conflict 0.
- artifacts:
  - path: artifacts/marketing-59/virtue-prelaunch-plg-signal-gate.md
    role: strategy
    note: 13행×3열 신호 위계 표 + 7항목 first-10 수기 review gate
- reports:
  - path: reports/marketing-59/2026-06-14T1200Z-local.html
    role: final
- commits:
  - repo: infinity
    branch: claude/gifted-bohr-kg441p
    note: heartbeat cloud docs-only commit
- urls: []
- next_actions:
  - First-10 observation notes can use the 7-item gate as a manual checklist.
  - Any new event, dashboard, tracking/privacy, pricing, public copy, deployment, or external message remains approval-gated.
  - PQL bundle observation can be opened when D7 revisit data reaches decision-grade sample size.

## Result

The PLG signal gate separates three layers for Virtue prelaunch:

**지금 볼 신호 (Watch Now):**
- First value event: `deed_saved` (J1/J2/J4) or `deed_judged` (J3)
- Job identification, traffic source classification, friction type (B-LOST/B-MISMATCH/B-AVAIL/B-NORMAL)
- Post-response flow (30-second manual observation after `deed_judged`)
- Guided break point: first_input / ai_wait / result_interpretation / save_or_exit
- User language in their own words

**보류할 신호 (Defer):**
- TTV numeric judgment, retention %, activation rate, judged-save gap as failure, `deed_save_capped` as upgrade demand

**Launch 이후 볼 신호 (Post-Launch Gate):**
- D7/D30 retention cohorts, PQL bundle confirmation, upgrade demand, viral coefficient, monetization signals

**First-10 수기 Review Gate (7항목):**
1. Traffic source (human / self-test / synthetic)
2. Job identification (J1/J2/J3/J4)
3. First value event fired?
4. Post-response flow (30초 손기록)
5. Friction type (B-LOST/B-MISMATCH/B-AVAIL/B-NORMAL)
6. Guided break point
7. User language (원문 기록)

## Boundaries

No new events, properties, tracking/privacy changes, PostHog dashboard, public copy, production code, deployment, external message, cost, secret, or permission change occurred. conflict markers: 0.
