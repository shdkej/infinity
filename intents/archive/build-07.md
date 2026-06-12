# build-07: Control Center Next.js Supabase CRUD MVP

- id: build-07
- status: completed
- projects: [infinity, personal-ops, infrastructure]
- task_type: implementation
- topics: [dashboard, cms, editing, supabase, deploy]
- owner: SAM
- display_name: Control Center Next.js Supabase CRUD MVP
- created_at: 2026-06-12T09:38Z
- completed_at: 2026-06-12T10:05Z
- source: follow-up from build-06 Draft Edit MVP and user request for low-friction web data manipulation
- predecessor: build-06
- successor: build-08
- report: reports/build-07/2026-06-12T1005Z-control-center-nextjs-supabase-cms.html
- artifact: artifacts/build-07/control-center-nextjs-supabase-crud-mvp.md
- public_url: https://cms.oracle.shdkej.com
- space_commits: [c1a168e, 8abc407, b9af95c]

## User Request

사용자는 CMS가 사용자 입력 마찰이 적으므로 Next.js 같은 앱으로 처리해도 되고, Space 환경과 Supabase 키를 사용할 수 있으며, 오늘 안에 웹에서 데이터 조작까지 해봤으면 좋겠다고 요청했다.

## Outcome

Control Center CMS를 read-only/diff preview에서 실제 웹 CRUD MVP로 확장했다.

- Space에 Next.js 15 앱 `apps/control-center-cms` 추가.
- 공개 URL: `https://cms.oracle.shdkej.com`.
- Supabase `public.control_center_items` table 생성.
- UI/API에서 CMS record 생성, 수정, 삭제 가능.
- 서비스 키는 Kubernetes Secret `control-center-cms-env`에만 저장하고 브라우저에는 노출하지 않았다.
- 실제 공개 페이지 publish는 아직 열지 않았고, Supabase scratch data를 다루는 운영 CMS MVP로 제한했다.

## Verification

- `pnpm --dir apps/control-center-cms build` PASS.
- Kubernetes deployment `control-center-cms` rollout 1/1 available.
- `https://cms.oracle.shdkej.com` HTTPS 200.
- ArgoCD application `control-center-cms` Synced/Healthy.
- Public API create -> patch -> get -> delete PASS.
- Browser UI에서 Create -> Edit -> Delete를 직접 수행해 웹 데이터 조작을 확인했다.
- 남겨둔 ready sample record: `66061087-4ce3-4586-b223-f1eb50620d2d`.

## Approval Boundary

이 intent는 Supabase scratch data CRUD까지만 완료한다.

아래는 다음 intent에서 별도 경계로 다룬다.

- 실제 Family Wedding / Travel / Status source file write.
- GitHub commit/push from CMS.
- production deploy button.
- auth/permission.
- audit log and rollback.
- GitHub/AWS token server function expansion.

## Continuity

프로젝트성 작업이 Archive에서 끊기지 않도록, 실제 공개 페이지 반영과 권한 모델은 `build-08` Inbox로 연결한다.
