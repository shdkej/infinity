# build-03: Control Center / Ops CMS for Dashboards

- id: build-03
- status: inbox
- projects: [infinity, personal-ops, infrastructure]
- task_type: design
- topics: [dashboard, workflow, automation]
- owner: SAM
- display_name: Control Center / Ops CMS
- created_at: 2026-06-11T23:03Z
- source: user request in Telegram direct chat

## User Request

사용자가 "트래블 대시보드나 다른 대시보드들 다 관리하는 cms 만드는거 어때?"라고 물었고, 이어서 "오케이 인피니티에 넣어줘"라고 요청했다.

## Purpose

Travel Dashboard, Status Dashboard, Infinity Dashboard, Card News Library, wedding/static pages처럼 흩어진 대시보드와 정적 페이지를 한곳에서 관리하는 내부 운영 CMS를 설계한다.

핵심은 범용 글쓰기 CMS가 아니라 대시보드 운영용 Control Center다. 어디에 무엇이 있고, 어떤 원장/데이터에서 만들어지며, 공개 URL과 배포 상태가 어떤지 한 화면에서 확인하고 필요한 반복 수정만 안전하게 버튼화하는 방향이다.

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

## First Useful Action

Create an inventory artifact that lists the current dashboards/static pages and their operating surfaces:

- Travel Dashboard
- Status Dashboard
- Infinity Dashboard
- Card News Library
- family wedding/static invitation page
- any other AWS/GitHub Pages static surfaces found in the current registry

For each item, capture:

- public URL
- canonical local path
- source data file(s)
- build command
- deploy command or GitHub/ArgoCD path
- verification method
- common edit operations
- risk/approval boundary

## Success Criteria

- [ ] MVP information architecture for Control Center is defined.
- [ ] Current dashboard/static-page inventory is captured in an artifact.
- [ ] Data-edit vs deploy-action boundaries are separated.
- [ ] A safe implementation plan exists for the first internal page without changing production surfaces.

## Approval Boundary

L0/L1 research and design are allowed. Creating an internal design artifact is allowed.

Actual implementation, deployment, registry changes, new write APIs, auth/permission changes, external-public changes, or automated deploy buttons require a later explicit execution step or this intent being promoted to Active with a concrete implementation plan.

## Notes

Initial framing from SAM:

- Value: reduce scattered dashboard/static-page management cost.
- Policy: start as an operating registry, editor panel, deploy status board, and change log.
- Execution: build a Dashboard Control Center first; buttonize repeated edits only after the manual flow is stable.
- Loop: use it to record and verify the work SAM already performs manually before increasing automation.
