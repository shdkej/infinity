# build-03: Control Center / Ops CMS for Dashboards

- id: build-03
- status: active
- projects: [infinity, personal-ops, infrastructure]
- task_type: design
- topics: [dashboard, workflow, automation]
- owner: SAM
- display_name: Control Center / Ops CMS
- priority: medium
- permission: L0/L1
- created_at: 2026-06-11T23:03Z
- activated_at: 2026-06-12T00:03Z
- source: user request in Telegram direct chat

## Purpose

Travel Dashboard, Status Dashboard, Infinity Dashboard, Card News Library, wedding/static pages처럼 흩어진 대시보드와 정적 페이지를 한곳에서 관리하는 내부 운영 CMS를 설계한다.

핵심은 범용 글쓰기 CMS가 아니라 대시보드 운영용 Control Center다. 어디에 무엇이 있고, 어떤 원장/데이터에서 만들어지며, 공개 URL과 배포 상태가 어떤지 한 화면에서 확인하고 필요한 반복 수정만 안전하게 버튼화하는 방향이다.

## Current State

- 2026-06-12T00:03Z: **Inbox → Active 이동.** L0 research 완료. 대시보드 inventory draft 작성 (Travel/Status/Infinity/Card Library/wedding 5개 파악). 실제 경로·URL·빌드 명령은 local 확인 필요.

## Next Actions

1. Local Claude에서 실제 대시보드 경로·URL·배포 방식 확인 → inventory 완성
2. MVP 정보구조 설계 확정
3. 구현 계획 수립 (별도 승인 후)

## Scope

### Include

- Dashboard/page registry: name, local path, repo, public URL, deploy mechanism, source data.
- Editable data links: Travel itinerary/expense data, Status registry, Infinity intent registry, Card Library items, other static-page data.
- Deploy and verify state: last commit, last build/deploy, last public URL check, cache/waiting/error state.
- Change log: what changed, when, by whom/agent, affected URL.
- Workflow capture: request -> file/data edit -> build -> push -> public verification.

### Exclude For MVP

- General-purpose blog CMS.
- Complex multi-user permissions.
- WYSIWYG page builder.
- Notion-style arbitrary database layer.
- Public/cost-bearing/deployment changes before explicit implementation approval.

## Approval Boundary

L0/L1 research and design are allowed. Creating an internal design artifact is allowed.

Actual implementation, deployment, registry changes, new write APIs, auth/permission changes, external-public changes, or automated deploy buttons require a later explicit execution step.

## Artifacts

- `artifacts/build-03/dashboard-inventory-draft.md` — 초기 inventory draft (L0, local 확인 필요)
- `reports/build-03/2026-06-12T0003Z.html` — 초기 L0 리서치 리포트
