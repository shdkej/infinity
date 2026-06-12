# build-03: Control Center / Ops CMS for Dashboards

- id: build-03
- status: active
- priority: medium
- permission: L0/L1
- projects: [infinity, personal-ops, infrastructure]
- task_type: design
- topics: [dashboard, workflow, automation]
- owner: SAM
- display_name: Control Center / Ops CMS
- created_at: 2026-06-11T23:03Z
- updated_at: 2026-06-12T00:00Z
- source: user request in Telegram direct chat

## Purpose

Travel Dashboard, Status Dashboard, Infinity Dashboard, Card News Library, wedding/static pages처럼 흩어진 대시보드와 정적 페이지를 한곳에서 관리하는 내부 운영 CMS를 설계한다.

핵심은 범용 글쓰기 CMS가 아니라 대시보드 운영용 Control Center다.

## Current State

- 2026-06-12T00:00Z **Inbox → Active 승격.** 2026-06-12 Heartbeat에서 첫 액션 완료: `artifacts/build-03/dashboard-inventory.md` 대시보드 인벤토리 작성. Cloud에서 확인 가능한 항목은 채웠고, 로컬 확인이 필요한 항목(Travel Dashboard URL, Status Dashboard 경로, Card News Library 레포)은 [확인 필요]로 표시함.
- 다음 액션: 로컬에서 Travel Dashboard / Status Dashboard / Card News Library 경로 확인 후 인벤토리 보완 → MVP 정보구조 설계.

## Next Actions

1. (Local) Travel Dashboard / Status Dashboard / Card News Library URL·경로·배포 방식 확인
2. (Cloud prepare) 인벤토리 보완 후 MVP 정보구조(Control Center 페이지 설계) 초안 작성
3. (User approval needed) MVP 구현·배포 승인 후 실제 Control Center 구축

## Success Criteria

- [ ] MVP information architecture for Control Center is defined.
- [ ] Current dashboard/static-page inventory is captured in an artifact.
- [ ] Data-edit vs deploy-action boundaries are separated.
- [ ] A safe implementation plan exists for the first internal page without changing production surfaces.

## Approval Boundary

L0/L1 research and design are allowed. Creating an internal design artifact is allowed.

Actual implementation, deployment, registry changes, new write APIs, auth/permission changes, external-public changes, or automated deploy buttons require a later explicit execution step.
