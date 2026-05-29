# marketing-26 Intent Archive

- id: marketing-26
- title: Virtue recovery-over-streak 리텐션 렌즈 작성
- status: archived
- priority: medium
- permission: L1 internal document + L2 agent-approved push
- created_at: 2026-05-29T10:00Z
- completed_at: 2026-05-29T11:07Z
- projects: [virtue]
- task_type: strategy
- topics: [retention, habit, recovery, copy]
- source_note: `/home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-29-streak-flexibility-recovery-retention.md`

## Result Summary

Created Virtue's recovery-over-streak retention lens as an internal documentation file. The document translates the source note's Duolingo/Reforge/HabitBoard lessons into Virtue's first-week prelaunch reading mode: recovery after a missed day matters more than continuous-day pressure, and streak/reset language is risky for a moral/deed-recording product.

Core structure:

- J1-J4 table covering recovery, skip, monthly completion, and comeback-session interpretation.
- First value mapping preserved: J1/J2/J4 = `deed_saved`, J3 = `deed_judged`.
- J3 is explicitly separated from saved-deed loops: repeat `deed_judged` can be a normal recovery signal, while saving is not required for J3 first value.
- Public copy, feature, and operating ideas are proposal-only; no implementation, tracking, dashboard, deployment, external message, cost, secret, permission, or production-data change.
- Existing adjacent docs (`seven-day-deed-loop.md`, `first-week-activation-retention-bridge.md`, `retention-predictive-activation-brief.md`) are treated as definitions to inherit, not replace.

## Artifact

- repo: `virtue-rebirth-app`
- branch: `master`
- path: `apps/web/docs/recovery-over-streak-retention-lens.md`
- commits:
  - `4ff2b96629a96685e976859bc4a13dbc43fa393b` — `marketing-26: 회복 우선 리텐션 렌즈 추가`
  - `7372aabf86884e5b168721586c969faf9f1f0360` — `marketing-26: remove event-like proposal label`
- push: HEAD == origin/master at `7372aabf86884e5b168721586c969faf9f1f0360`

## Verification

- Conflict markers: none in the new doc or `INTENTS.md`.
- Code diff: none; Virtue changed file list is only `apps/web/docs/recovery-over-streak-retention-lens.md`.
- First-value mapping: J1/J2/J4=`deed_saved`, J3=`deed_judged` present and unchanged.
- Event scope: only established adjacent-doc events are referenced: `add_flow_started`, `add_flow_abandoned`, `deed_judged`, `deed_saved`, `deed_rerolled`, `deed_save_capped`, `level_up_viewed`.
- Push check: Virtue HEAD equals `origin/master`.
- report: `reports/marketing-26/2026-05-29T1107Z-local.md`

## Next Actions

- Use the recovery lens when reading first-week return behavior; do not convert comeback/skip/monthly completion into KPI thresholds while sample size is small.
- Treat any public copy, feature, or tracking follow-up as a new Intent with approval boundary review.
