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
- updated_at: 2026-06-12T0600Z

## Goal

대시보드/정적페이지 운영 Control Center를 설계한다. 범용 CMS가 아닌, 어디에 무엇이 있고 어떤 데이터에서 만들어지며 배포 상태가 어떤지 한 화면에서 확인하는 운영 레지스트리.

## Current State

- 2026-06-12T0600Z **Inbox → Active 승격.** Cloud prepare 완료: 대시보드 inventory 초안 작성. 산출물: `artifacts/build-03/dashboard-inventory-draft.md`. 다음 액션: 로컬에서 실제 경로/URL 확인 후 inventory 완성.

## Purpose

Travel Dashboard, Status Dashboard, Infinity Dashboard, Card News Library, wedding/static pages처럼 흩어진 대시보드와 정적 페이지를 한곳에서 관리하는 내부 운영 CMS를 설계한다.

핵심: 범용 글쓰기 CMS가 아니라 운영 Control Center. 어디에 무엇이 있고, 어떤 원장/데이터에서 만들어지며, 공개 URL과 배포 상태가 어떤지 한 화면에서 확인하고 반복 수정만 안전하게 버튼화.

## Scope

### Include
- Dashboard/page registry: name, local path, repo, public URL, deploy mechanism, source data
- Editable data links: Travel itinerary/expense data, Status registry, Infinity intent registry, Card Library items
- Deploy and verify state: last commit, last build/deploy, last public URL check
- Change log: what changed, when, by whom/agent, affected URL
- Workflow capture: request → file/data edit → build → push → public verification

### Exclude For MVP
- General-purpose blog CMS
- Complex multi-user permissions
- WYSIWYG page builder
- Public/cost-bearing/deployment changes before explicit implementation approval

## Success Criteria

- [ ] 현재 운영 중인 모든 대시보드/정적페이지 inventory 완성 (경로, URL, 데이터소스, 배포방식)
- [ ] MVP 정보구조(Control Center) 설계 완료
- [ ] 데이터 편집 vs 배포 액션 경계 분리
- [ ] 구현 계획 초안 (첫 internal 페이지 기준)

## Next Action

Local Claude가 실제 파일시스템 경로 확인:
- `/home/ubuntu/` 하위 travel dashboard, status dashboard, infinity dashboard 경로
- `oracle.shdkej.com` 하위 공개 URL 확인
- GitHub Pages/ArgoCD 배포 경로 확인
- 완성된 inventory → `artifacts/build-03/dashboard-inventory.md`에 저장

## Approval Boundary

L0/L1 research and design만 허용. 구현/배포/registry 변경은 별도 승격 후 진행.
