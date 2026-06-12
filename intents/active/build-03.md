# build-03: Control Center / Ops CMS for Dashboards

- id: build-03
- status: in_progress
- projects: [infinity, personal-ops, infrastructure]
- task_type: design
- topics: [dashboard, workflow, automation]
- owner: SAM
- display_name: Control Center / Ops CMS
- created_at: 2026-06-11T23:03Z
- updated_at: 2026-06-12T06:00Z
- promoted_at: 2026-06-12T06:00Z

## Purpose

Travel Dashboard, Status Dashboard, Infinity Dashboard, Card News Library, wedding/static pages처럼 흩어진 대시보드와 정적 페이지를 한곳에서 관리하는 내부 운영 CMS를 설계한다.

핵심은 범용 글쓰기 CMS가 아니라 대시보드 운영용 Control Center다. 어디에 무엇이 있고, 어떤 원장/데이터에서 만들어지며, 공개 URL과 배포 상태가 어떤지 한 화면에서 확인하고 필요한 반복 수정만 안전하게 버튼화하는 방향이다.

## Current State

- 2026-06-12T06:00Z **Inbox → Active 승격, 1차 인벤토리 스켈레톤 생성.** Cloud agent가 build-03.md 파일에 기술된 대시보드 5종을 기준으로 인벤토리 스켈레톤을 작성했다 (`artifacts/build-03/dashboard-inventory-2026-06-12.md`). 공개 URL·로컬 경로·빌드 명령은 클라우드에서 확인 불가하므로 로컬 검증 필요로 표시되었다. 다음 안전 액션: 로컬에서 실제 경로와 배포 정보를 채워 넣기.

## Next Actions

1. **[로컬] 인벤토리 채우기**: `artifacts/build-03/dashboard-inventory-2026-06-12.md`를 열고, `[로컬검증필요]`로 표시된 항목들(공개 URL, 로컬 경로, 빌드 명령, 배포 경로)을 실제 값으로 채운다.
2. **[Cloud] MVP 정보구조 설계**: 인벤토리 완성 후 Control Center의 MVP 정보구조(registry view, data-edit panel, deploy status, change log) 설계를 수행한다.
3. **[L2 승인 후] 구현**: 내부 정적 페이지로 Control Center 첫 버전 구현 (프로덕션 변경 없음).

## Success Criteria

- [ ] MVP information architecture for Control Center is defined.
- [ ] Current dashboard/static-page inventory is captured in an artifact.
- [ ] Data-edit vs deploy-action boundaries are separated.
- [ ] A safe implementation plan exists for the first internal page without changing production surfaces.

## Approval Boundary

L0/L1 research and design are allowed. Creating an internal design artifact is allowed.

Actual implementation, deployment, registry changes, new write APIs, auth/permission changes, external-public changes, or automated deploy buttons require a later explicit execution step.

## Reports

- `reports/build-03/2026-06-12T0600Z-heartbeat.html` — Inbox→Active 승격 리포트
