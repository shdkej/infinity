# build-08: Control Center shadcn UI + Status Composition CMS

- id: build-08
- status: completed
- projects: [infinity, personal-ops, infrastructure]
- task_type: implementation
- topics: [dashboard, cms, ui, status, supabase, deploy]
- owner: SAM
- display_name: Control Center shadcn UI + Status Composition CMS
- created_at: 2026-06-12T10:05Z
- completed_at: 2026-06-12T10:40Z
- source: user request — 고퀄리티 shadcn/ui 운영툴 + Status 페이지 전체 구성 관리
- predecessor: build-07
- successor: build-09
- report: reports/build-08/2026-06-12T1040Z-control-center-shadcn-status-composition.html
- public_url: https://cms.oracle.shdkej.com
- space_commits: [f253ba9, 904a6d5]

## User Request

사용자는 CMS를 전체적으로 고퀄리티로 만들기를 원했다. shadcn/ui로 구성하고, Status 페이지 전체를 CMS에서 구성/수정할 수 있게 해달라고 요청했다. 작업은 Claude가 직접 수행.

## Outcome

build-07의 평면 CRUD CMS를 shadcn/ui 기반의 운영툴로 재구성하고, Status 페이지 구성을 웹에서 관리할 수 있게 했다.

- shadcn/ui 도입: Tailwind v3 + cn util + Button/Card/Badge/Input/Textarea/Label/Select/Tabs/Separator/Switch/Sheet(drawer). 조용·밀도 있는 운영툴 톤, 다크모드, 모바일 stack 대응.
- Status 구성 데이터 모델: Supabase `public.control_center_nodes` self-referential 트리(kind: surface/section/card/link, title/subtitle(copy)/url/status/sort_order/visible). 감사 로그 `public.control_center_activity` 추가. 둘 다 RLS enabled · 정책 없음 = service-role only.
- 기존 `control_center_items`는 Surface Registry 탭으로 유지.
- API: `/api/nodes` CRUD + reorder(sort_order swap), `/api/activity`. 모든 mutation이 activity 로그 기록. 서비스 키는 K8s Secret `control-center-cms-env`에만 보관, 브라우저 미노출.
- UI 구성: Status 구성(트리 편집 + 순서/노출 토글 + Edit drawer) · 라이브 Preview · Surface Registry · Activity 감사 로그.

## Verification

- local `pnpm build` PASS (route manifest에 /api/nodes·/api/items·/api/activity 모두 포함).
- deployment `control-center-cms` rollout 1/1 available, ArgoCD Synced/Healthy.
- `https://cms.oracle.shdkej.com` HTTPS 200, UI 마커(Control Center / Status 구성 / Surface Registry / Activity / Preview) 렌더, Tailwind CSS·JS 번들 200.
- live `/api/nodes`: create(201) → edit(200) → visibility(200) → invalid kind(400) → delete(200) PASS. 각 작업이 activity 로그에 한글 요약으로 기록됨. 테스트 노드 정리 완료, 시드 데이터 보존.
- Supabase security advisor: 3개 테이블 `rls_enabled_no_policy` INFO만 — 의도된 service-role-only 설계.

## Trap / Lesson

repo-root `.gitignore` 5번째 줄의 bare `nodes` 패턴(Vagrant/Terraform 잔재)이 `app/api/nodes/` 디렉터리를 무음으로 제외했다. 첫 배포에서 `/api/nodes`만 404. `git add -f`로 두 route 파일을 강제 추적하고 재배포해 해소. 교훈: in-pod git-clone 배포는 로컬 build PASS와 무관하게 **커밋된 파일 = 배포 파일**이므로, 신규 디렉터리는 `git status`에서 staged 여부를 반드시 확인한다.

## Approval Boundary (이번에 미실행)

실제 Family Wedding / GitHub Pages production source write·publish 버튼, auth/permission, rollback은 실행하지 않았다. CMS 안에서 status/control-center 구성 데이터를 만들고 저장하는 수준까지가 목표. destructive·force-push·비용 리소스·외부 발송 0.

## Next → build-09

authenticated production publish pipeline: 선택한 구성/record를 실제 공개 페이지 정본으로 반영(auth/permission, approval gate, source repo write, commit/push, deploy trigger, public URL 검증, rollback handle).
