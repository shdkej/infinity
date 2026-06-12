# build-03: Control Center / Ops CMS for Dashboards

- id: build-03
- status: active
- projects: [infinity, personal-ops, infrastructure]
- task_type: design
- topics: [dashboard, workflow, automation]
- owner: SAM
- display_name: Control Center / Ops CMS
- created_at: 2026-06-11T23:03Z
- updated_at: 2026-06-12T06:00Z

## Current State

2026-06-12T06:00Z: Inbox에서 Active로 이동. 클라우드에서 알려진 서비스 기반으로 Dashboard Inventory v1 초안 생성 완료.

**알려진 서비스 (클라우드 확인):**
- Infinity Kanban Dashboard: `https://infinity.oracle.shdkej.com` (K8s/ArgoCD, space repo `apps/infinity-kanban/`)
- Infinity GitHub Pages: `docs/index.html` in shdkej/infinity (GitHub Pages)
- Agent Wiki: `https://shdkej.github.io/agent-wiki/` (GitHub Pages, MkDocs Material)
- Virtue App: `https://virtue.oracle.shdkej.com` (K8s deployment, `/home/ubuntu/dev/virtue-rebirth-app`)

**미확인 (로컬 검증 필요):**
- Travel Dashboard: URL, 로컬 경로, 배포 방식 미확인
- Status Dashboard: URL, 로컬 경로, 배포 방식 미확인
- Card News Library: URL, 로컬 경로, 배포 방식 미확인
- Family wedding/static invitation page: URL, 로컬 경로, 배포 방식 미확인

## Next Action

1. **로컬 검증**: `artifacts/build-03/dashboard-inventory-v1.md`를 로컬에서 열어 미확인 항목 4개를 채운다
2. **MVP 설계**: 채워진 inventory 기반으로 CMS 정보구조(화면 목록, 권한 경계, 데이터 편집 경로) 설계
3. **구현 승격**: 설계 완료 후 구현 단계 Intent로 분리

## Approval Boundary

- L0/L1 (즉시): 리서치, 설계 초안, artifact 작성
- L2 (자체 승인 가능): 내부 페이지 구현 (프로덕션 외부 변경 없음)
- L3 (사용자 직접): 프로덕션 배포 경로 변경, 권한 변경

## Context

- inbox: `intents/inbox/build-03.md`
- artifact: `artifacts/build-03/dashboard-inventory-v1.md`
- report: `reports/build-03/2026-06-12T0600Z.html`
