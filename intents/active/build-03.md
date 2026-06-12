# build-03: Control Center / Ops CMS for Dashboards

- id: build-03
- status: active
- priority: medium
- projects: [infinity, personal-ops, infrastructure]
- task_type: design
- topics: [dashboard, workflow, automation]
- owner: SAM
- display_name: Control Center / Ops CMS
- created_at: 2026-06-11T23:03Z
- activated_at: 2026-06-12T06:00Z
- source: user request in Telegram direct chat

## Purpose

Travel Dashboard, Status Dashboard, Infinity Dashboard, Card News Library, wedding/static pages처럼 흩어진 대시보드와 정적 페이지를 한곳에서 관리하는 내부 운영 CMS를 설계한다.

핵심은 범용 글쓰기 CMS가 아니라 대시보드 운영용 Control Center다. 어디에 무엇이 있고, 어떤 원장/데이터에서 만들어지며, 공개 URL과 배포 상태가 어떤지 한 화면에서 확인하고 필요한 반복 수정만 안전하게 버튼화하는 방향이다.

## Goal

- 현재 운영 중인 대시보드/정적 페이지의 인벤토리 아티팩트 생성
- MVP 정보구조(registry, editable source data links, deploy/verify 상태, change log) 설계

## Success Criteria

- [ ] 현재 대시보드/정적 페이지 인벤토리 아티팩트 완성 (`artifacts/build-03/dashboard-inventory.md`)
- [ ] MVP 정보구조 설계 완성
- [ ] 데이터 편집 vs 배포 액션 경계 명시
- [ ] 첫 내부 페이지 구현 계획 수립 (프로덕션 표면 변경 없음)

## Next Action

**L0 Cloud 작업**: 현재 대시보드/정적 페이지 인벤토리 조사
- Travel Dashboard, Status Dashboard, Infinity Dashboard, Card News Library, 웨딩/정적 초대 페이지
- 각 항목: public URL, canonical local path, source data file(s), build command, deploy command/path, verification method, common edit operations, risk/approval boundary
- 산출물: `artifacts/build-03/dashboard-inventory.md`

## Approval Boundary

- L0/L1 research and design: allowed
- Implementation, deployment, registry changes, auth/permission changes, external-public changes: require explicit execution approval (L2+)

## Scope Reference

### Include

- Dashboard/page registry: name, local path, repo, public URL, deploy mechanism, source data
- Editable data links: Travel itinerary/expense data, Status registry, Infinity intent registry, Card Library items, other static-page data
- Deploy and verify state: last commit, last build/deploy, last public URL check
- Change log: what changed, when, by whom/agent, affected URL
- Workflow capture: request → file/data edit → build → push → public verification

### Exclude For MVP

- General-purpose blog CMS
- Complex multi-user permissions
- WYSIWYG page builder
- Notion-style arbitrary database layer
- Public/cost-bearing/deployment changes before explicit implementation approval
