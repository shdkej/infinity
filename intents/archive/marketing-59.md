# marketing-59 — Virtue Launch-Ready PLG Signal Gate

- id: marketing-59
- status: archived
- completed_at: 2026-06-14T12:00Z
- projects: [virtue]
- task_type: strategy
- topics: [plg, activation, measurement, prelaunch]
- result_summary: PLG 시그널을 3티어(지금/보류/launch이후)로 분류하고 first-10 수기 리뷰 게이트를 작성. J1/J2/J4=deed_saved, J3=deed_judged 매핑 유지. 신규 이벤트/tracking/privacy/공개카피/배포/비용 0.
- artifacts:
  - path: artifacts/marketing-59/virtue-launch-ready-plg-signal-gate.md
    role: strategy
    note: 3티어 시그널 게이트 테이블과 first-10 수기 리뷰 게이트
- reports:
  - path: reports/marketing-59/2026-06-14T1200Z-heartbeat.html
    role: final
- commits: []
- urls: []
- next_actions:
  - First-10 관찰 시 이 게이트 테이블을 기준으로 수기 노트 작성
  - launch 이후 보류/after-launch 게이트 재오픈 여부 결정

## Result

Created a 3-tier PLG signal gate for Virtue prelaunch:

### 지금 볼 신호 (Count and observe now)
- `deed_saved` — first-win anchor for J1/J2/J4
- `deed_judged` — first-win anchor for J3
- `deed_rerolled` — observe without interpreting as churn

### 보류할 신호 (Record, do not interpret yet)
- `deed_save_capped`, `level_up_viewed`, return visit, second session, cross-job use, verbal upgrade asks
- Pattern interpretation gated at ≥5 users or after launch

### launch 이후 볼 신호 (After launch gate)
- PQL, paid conversion, expansion, viral coefficient, NPS, retention rate, channel quality

### First-10 Review Gate

A structured review table with per-person columns:
- Job (J1–J4), Now signal fired (y/n/unclear), Hold signals seen (note only), After-launch marker (verbatim only), Activation read (activated/not/unclear)

**Activation rule**: Now signal fired for the job AND observer can confirm user received something concrete. Not: reroll, cap hit, or return alone.

## Boundaries

No new events, properties, tracking/privacy changes, PostHog dashboard, public copy, production code, deployment, external message, cost, secret, or permission change occurred.
