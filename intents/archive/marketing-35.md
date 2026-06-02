# marketing-35 Virtue 잡별 온보딩 체크리스트 감사표

- id: marketing-35
- status: archived
- completed_at: 2026-06-02T23:07
- projects: [virtue]
- task_type: strategy
- topics: [onboarding, activation, checklist]
- result_summary: Virtue 체크리스트를 잡별 first value 위치에 맞춰 CL-ELIGIBLE, BUMPER-ONLY, CONTEXTUAL-FALLBACK, DO-NOT-INCLUDE 4분류로 정리하고 J3 저장 강제 금지 경계를 고정했다.
- artifacts:
  - path: /home/ubuntu/dev/virtue-rebirth-app/apps/web/docs/onboarding-checklist-audit-table.md
    role: strategy
    note: J1~J4별 체크리스트 적격 행동, 범퍼, 맥락 폴백, 금지 항목 감사표.
- reports:
  - path: reports/marketing-35/2026-06-02T2207Z-local.html
    role: final
- commits:
  - repo: virtue-rebirth-app
    sha: a300095
    note: docs-only onboarding checklist audit table.
  - repo: infinity
    sha: self
    note: Archive registry, intent index, and HTML report.
- urls: []
- next_actions:
  - 다음 체크리스트 또는 onboarding UI 구현 intent가 생기면 J3는 `deed_judged`에서 완료되고 저장은 선택이라는 경계를 먼저 확인한다.

## Axis

- 축1: 단일 온보딩 체크리스트는 J1/J2/J4와 J3의 first value 종료점 차이를 가려 J3의 정상 종료를 저장 미완료로 오독할 수 있다.
- 축2: 체크리스트 항목을 잡별 first value 직선 위 적격 행동, 범퍼, 맥락 폴백, 금지 항목으로 분리했고 폴백은 B-LOST에만 발동하도록 제한했다.

## Verification

- HTML report gate passed: `<html`, `<body`, `axis ax1`, `axis ax2`, `<details`.
- Virtue repo is clean after push to `origin/master` at `a300095`.
- Scope remained docs-only in Virtue: `apps/web/docs/onboarding-checklist-audit-table.md`.
- No new event, property, copy, tracking, dashboard, session replay, code, deployment, external send, cost, secret, permission, or privacy change.
- First value mapping preserved: J1/J2/J4 = `deed_saved`, J3 = `deed_judged`.
- `deed_save_capped` remains availability/friction, not upgrade demand.

## Learning Loop

- 계승한 기준: First Value Mapping, Product Body vs Bumper By Job, Prelaunch Decision Boundary, Availability And Friction Are Not Value, Measurement Readiness Is A Separate Gate.
- 이번에 새로 배운 것: checklist length and endpoint must follow the job's first value. J1/J2/J4 use input to judgment to save; J3 ends at judgment, and save is not required.
- 다음 Marketer에게 넘길 규칙: checklist items stop at first value; J3 must not include required save; contextual fallback only fires for B-LOST, not B-MISMATCH, B-AVAIL, or B-NORMAL.
- MARKETING_LEARNINGS.md 승격 후보: "Checklist Follows First Value By Job" remains report-only until reused by another marketing intent.
