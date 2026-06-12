# Intent Registry

> Heartbeat Agent가 주기적으로 읽고 실행하는 의도 목록.

## Inbox




## Active

<!-- naver-shopping-01 active 2026-06-12T07:00Z → intents/active/naver-shopping-01.md [display: 나래/Narae; projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,marketing; status: active-sourcing-screen-advance-mini-album; approval: no-current-user-blocker] (소싱-퍼스트 브로드 스크린 완료(2026-06-12 Heartbeat): 6카테고리 스크리닝 — 포켓 미니 앨범 ADVANCE(키워드 스캔 다음), 트래블러스노트 속지 PIVOT-SOURCING(공급사 발굴 필요), 케이블 오거나이저 WATCH(경쟁밀도 확인 필요), 여행파우치세트/수면안대 HOLD. 러기지택/워크샵카드/카드인서트 제외 유지. 산출물 `artifacts/naver-shopping-01/sourcing-first-broader-screen-2026-06-12.md`. 라이브 상품등록/가격·배송·재고/광고·고객·주문·계정·공개발행 0. archive 안 함(active 유지).) -->

## Waiting

<!-- 사용자 결정, 외부 조건, 안전 확인 대기. 같은 질문을 반복하지 않고 상태만 보존한다. -->

## Archive

<!-- build-09 completed 2026-06-12T14:16Z → intents/archive/build-09.md [display: Control Center Static Publish Target Removed; projects: infinity,personal-ops,infrastructure; type: implementation; topics: dashboard,cms,auth,publish,deploy,rollback] (사용자가 정적 페이지로 만든 Control Center 제거를 요청해 `status-control-center-feed` publish target을 닫음. 이전 non-secret publish/rollback spec은 역사 기록으로 남기되, Waiting 질문은 종료. Status 정적 사이트의 `sites/status/dist/control-center/index.html` 삭제, Status 첫 화면 `./control-center/index.html` 링크 제거. 앞으로 Control Center publish 작업을 다시 열면 정적 Status subpage가 아니라 live CMS `https://cms.oracle.shdkej.com` 기준으로 새 target을 명시해야 함.) -->

<!-- build-08 completed 2026-06-12T10:40Z → reports/build-08/2026-06-12T1040Z-control-center-shadcn-status-composition.html [display: Control Center shadcn UI + Status Composition CMS; projects: infinity,personal-ops,infrastructure; type: implementation; topics: dashboard,cms,ui,status,supabase,deploy] (build-07 평면 CRUD CMS를 shadcn/ui 운영툴로 재구성하고 Status 페이지 구성을 웹에서 관리 가능하게 함. shadcn/ui(Tailwind v3, Button/Card/Badge/Input/Textarea/Label/Select/Tabs/Separator/Switch/Sheet drawer), 다크모드/모바일 대응. Supabase `public.control_center_nodes` self-referential 트리(surface/section/card/link, title/subtitle/url/status/sort_order/visible) + `public.control_center_activity` 감사 로그 신규, 둘 다 RLS enabled·정책 없음=service-role only. 기존 `control_center_items`는 Surface Registry 탭으로 유지. API `/api/nodes` CRUD+reorder, `/api/activity`, 모든 mutation이 activity 기록. UI=Status 구성 트리(순서/노출 토글+Edit drawer)·라이브 Preview·Surface Registry·Activity. 서비스 키는 K8s Secret `control-center-cms-env`에만. Space commits `f253ba9`, `904a6d5`. Supabase migration `control_center_status_composition`(project `ihpfnzwqbntjcirtrkjd`). 검증: local build PASS, rollout 1/1, ArgoCD Synced/Healthy, HTTPS 200, UI 마커 렌더, live `/api/nodes` create(201)→edit(200)→visibility(200)→invalid(400)→delete(200) PASS + activity 반영. 함정: root .gitignore의 bare `nodes` 패턴이 app/api/nodes/ 무음 제외→첫 배포 404, `git add -f`로 해소. 실제 production page write/publish·auth/permission·rollback은 미실행(승인 경계). next `build-09` Inbox로 연결.) -->

<!-- marketing-55 completed 2026-06-12T10:12Z → intents/archive/marketing-55.md [display: Virtue Prelaunch Activation Measurement Contract; projects: virtue; type: strategy; topics: activation,measurement,prelaunch] (Mixpanel 2026 PLG 측정 렌즈를 Virtue prelaunch first-value 계약으로 번역한 docs-only artifact 작성. 산출물 `artifacts/marketing-55/virtue-prelaunch-activation-measurement-contract.md`, report `reports/marketing-55/2026-06-12T1012Z-local.html`. J1/J2/J4=`deed_saved`, J3=`deed_judged` 매핑 유지. `count now`/`observe manually`/`do not judge yet`로 first-10 관찰을 분리하고 PQL/paid conversion/expansion/viral coefficient는 launch-after gate로 고정. 신규 이벤트·tracking/privacy·dashboard·public copy·deploy·external message·cost 0. `build-08` 미수정.) -->

<!-- build-07 completed 2026-06-12T10:05Z → reports/build-07/2026-06-12T1005Z-control-center-nextjs-supabase-cms.html [display: Control Center Next.js Supabase CRUD MVP; projects: infinity,personal-ops,infrastructure; type: implementation; topics: dashboard,cms,editing,supabase,deploy] (Control Center CMS를 read-only/diff preview에서 실제 웹 CRUD MVP로 확장. Space에 Next.js 15 앱 `apps/control-center-cms`와 ArgoCD app/K8s deployment/service/ingress 추가, 공개 URL `https://cms.oracle.shdkej.com`. Supabase project `ihpfnzwqbntjcirtrkjd`에 `public.control_center_items` table 생성, RLS enabled, 서비스 키는 Kubernetes Secret `control-center-cms-env`에만 보관. Space commits `c1a168e Add control center CMS app`, `8abc407 Pin CMS pnpm runtime`, `b9af95c Limit CMS ArgoCD manifests`. 검증: local build PASS, deployment rollout 1/1 available, ArgoCD Synced/Healthy, HTTPS 200, public API create/patch/get/delete PASS, 브라우저 UI에서 create→edit→delete 직접 조작 PASS. persistent ready sample 1건 유지: `66061087-4ce3-4586-b223-f1eb50620d2d`. 실제 Family Wedding 공개 페이지 write/publish/auth/rollback은 미구현이며 next `build-08` Inbox로 연결.) -->

<!-- build-06 completed 2026-06-12T09:35Z → reports/build-06/2026-06-12T0935Z-control-center-draft-editor.html [display: Control Center Draft Edit MVP; projects: infinity,personal-ops,infrastructure; type: implementation; topics: dashboard,cms,editing,diff-preview,deploy] (기존 Status Control Center에 draft-only Editable CMS/Draft Editor 섹션 구현. Family Wedding NOTICE field input → unified diff preview가 브라우저 메모리에서 즉시 생성되며 정본 파일 write 없음. write API/auth/permission/GitHub·AWS token server function/production deploy button/UI 자동 commit-push/Terraform·AWS 리소스/비용/destructive/secret 편집 0. Space repo commit/push `d389511 feat(status): add control center draft editor`. Status feed 재생성, S3 sync, CloudFront invalidation `I94000R114RC8NKS2P8OP48GQ`, 공개 URL `https://status.aws.shdkej.com/control-center/index.html`에서 `Draft Editor`, `Family Wedding`, `diff preview`, `NOTICE field input` 확인. next: `build-07` Inbox에서 Save/Publish 경계 설계로 연결.) -->

<!-- build-05 completed 2026-06-12T07:30Z → reports/build-05/2026-06-12T0730Z-local.html [projects: infinity,personal-ops,infrastructure; type: design; topics: dashboard,cms,automation] (Control Center Editable CMS 첫 안전 액션 = editable surface schema + field-level draft edit/diff preview 설계 완료. 산출물 `artifacts/build-05/control-center-editable-cms-design.md`, canonical index `intents/archive/build-05.md`. `editableSurfaces` 스키마(id/필드/anchor/검증/preview/publish/changeLog) 정의, 첫 editable target으로 Family Wedding 안내장 3필드(NOTICE/본문 도입/OG description) 인스턴스, anchor 기반 unified diff preview 흐름 설계. 핵심 안전장치 `preview.write:"none"`로 정본 파일 미변경, publish/deploy는 전부 approval-needed 자리로만 표시. write API/auth/permission/production deploy button/GitHub·AWS token server function/Terraform·AWS resource/cost/destructive/외부 발송/secret 편집은 본 문서에서 설계 경계 텍스트로만 다루고 미구현. change-log 모델로 commit SHA/deploy run/public URL 검증 연결. doc-only inside Infinity. next: `build-06` Active에서 Draft Editor MVP 구현으로 연결. HTML report gate(`<html`/`<body`/`axis ax1`/`axis ax2`/`<details`) 통과.) -->

<!-- build-04 completed 2026-06-12T06:55Z → reports/build-04/2026-06-12T0655Z-control-center-deploy.html [projects: infinity,personal-ops,infrastructure; type: implementation; topics: dashboard,cms,deploy,automation] (Dashboard Control Center read-only MVP 배포 완료. 공개 URL `https://status.aws.shdkej.com/control-center/index.html`. 산출물 `artifacts/build-04/control-center-mvp-deployment.md`. 구현은 기존 Status 정적 사이트 하위 경로 `sites/status/dist/control-center/index.html`에 추가해 새 AWS 리소스/Terraform 없이 진행. Status 첫 화면에 `./control-center/index.html` 진입 링크 추가. 페이지는 static HTML+CSS로 구현. Commit/push Space repo `3c91780`. 검증: S3 sync PASS, CloudFront invalidation PASS, 공개 URL HTTP 200, 필수 UI 요소(링크/배지/프레임) 렌더 PASS.) -->

<!-- build-03 completed 2026-06-12T04:00Z → intents/archive/build-03.md [projects: infinity,personal-ops,infrastructure; type: design; topics: dashboard,cms,automation] (Status Dashboard Control Center MVP 설계 완료: JSON feed 기반 read-only 뷰어, deploy 버튼 spec, markdown→HTML publish 플로우, 인증없는 read-only URL 구조. doc-only, Space 코드·배포·외부 발송 미수정.) -->

<!-- build-02 completed 2026-06-11T19:20Z → intents/archive/build-02.md [projects: infinity,personal-ops,infrastructure; type: implementation; topics: dashboard,cms,automation] (Status Dashboard 첫 배포 완료: GitHub Actions workflow, S3 sync, CloudFront invalidation, public URL https://status.aws.shdkej.com 200 OK. Space commit 4a35b3e. Cloudfront Distribution E3BSSDPN38P1UB.) -->

<!-- build-01 completed 2026-06-11T15:01Z → intents/archive/build-01.md [projects: infinity,personal-ops,infrastructure; type: research; topics: dashboard,infra] (Status Dashboard 후보 기술 스택 조사 완료. 산출물 artifacts/build-01/status-dashboard-tech-stack-comparison.md.) -->

<!-- marketing-54 completed 2026-06-11T02:00Z → intents/archive/marketing-54.md [display: Virtue AI-Native Value Proposition; projects: virtue; type: strategy; topics: marketing,product,ai-agents] (Virtue의 AI-native 차별점을 Perplexity/Cursor/v0/Devin 대비 가치 제안으로 재프레이밍. 산출물 artifacts/marketing-54/virtue-ai-native-value-proposition.md. 신규 이벤트·tracking·deploy·cost 0.) -->

<!-- marketing-53 completed 2026-06-09T03:00Z → intents/archive/marketing-53.md [display: Virtue Prelaunch Copy B — Concreteness Pass; projects: virtue; type: strategy; topics: marketing,activation,product] (Prelaunch 랜딩 copy B variant 작성: first-value promise를 구체적인 행동 문장으로 재작성. 신규 이벤트·tracking·deploy·cost 0.) -->

<!-- marketing-52 completed 2026-06-08T15:00Z → intents/archive/marketing-52.md [display: Virtue Prelaunch First-Value Frame; projects: virtue; type: strategy; topics: marketing,activation,product] (Prelaunch 랜딩 first-value promise 프레임 초안 완료. 신규 이벤트·tracking·deploy·cost 0.) -->

<!-- marketing-51 completed 2026-06-08T12:00Z → intents/archive/marketing-51.md [display: Virtue Prelaunch Activation Audit; projects: virtue; type: research; topics: marketing,activation] (Virtue 첫 사용 흐름 감사 및 activation gap 목록 작성. 신규 이벤트·tracking·deploy·cost 0.) -->

<!-- marketing-50 completed 2026-06-08T09:00Z → intents/archive/marketing-50.md [display: Naver AI Creator Workshop SKU Strategy; projects: naver-shopping,virtue; type: strategy; topics: marketing,product] (AI/creator workshop facilitation card SKU 전략 초안: purchase-situation 우선 선택(workshop facilitation), keyword DRAFT 판정, copy-led 접근 권고. 2026-06-10 user correction으로 워크샵 monetization path 철회됨. Historical evidence only.) -->

<!-- monitor-01 completed 2026-04-08T11:30Z → intents/archive/monitor-01.md -->
<!-- doc-01 completed 2026-04-08T14:00Z → intents/archive/doc-01.md -->
<!-- wiki-02 completed 2026-04-19T12:30Z → intents/archive/wiki-02.md -->
<!-- wiki-03 completed 2026-04-20T13:30Z → intents/archive/wiki-03.md -->
<!-- wiki-04 completed 2026-04-26T10:00Z → intents/archive/wiki-04.md -->
<!-- build-01 (wiki) completed 2026-04-21T01:00Z → intents/archive/build-01-wiki.md  -->
<!-- research-01 completed 2026-05-14T12:00Z → intents/archive/research-01.md -->
<!-- research-02 completed 2026-05-14T15:00Z → intents/archive/research-02.md -->
<!-- research-03 completed 2026-05-15T10:00Z → intents/archive/research-03.md -->
<!-- research-04 completed 2026-05-17T14:00Z → intents/archive/research-04.md -->
<!-- research-05 completed 2026-05-17T17:00Z → intents/archive/research-05.md -->
<!-- research-06 completed 2026-05-20T10:00Z → intents/archive/research-06.md -->
<!-- marketing-01 completed 2026-05-21T10:30Z → intents/archive/marketing-01.md (Virtue add-flow telemetry 구현·배포·검증 완료. agent-approved L2: master branch fast-forward merge+push, K8s rollout restart, HTTPS 200 확인. report reports/marketing-01/2026-05-21T0950Z-approved-deploy.md.) -->
<!-- marketing-02 completed 2026-05-22T00:00Z → intents/archive/marketing-02.md -->
<!-- marketing-03 completed 2026-05-23T10:00Z → intents/archive/marketing-03.md -->
<!-- marketing-04 completed 2026-05-24T12:00Z → intents/archive/marketing-04.md -->
<!-- marketing-05 completed 2026-05-25T10:00Z → intents/archive/marketing-05.md -->
<!-- marketing-06 completed 2026-05-26T15:00Z → intents/archive/marketing-06.md -->
<!-- marketing-07 completed 2026-05-27T14:00Z → intents/archive/marketing-07.md -->
<!-- marketing-08 completed 2026-05-28T10:00Z → intents/archive/marketing-08.md -->
<!-- marketing-09 completed 2026-05-29T10:00Z → intents/archive/marketing-09.md -->
<!-- marketing-10 completed 2026-05-30T12:00Z → intents/archive/marketing-10.md -->
<!-- marketing-11 completed 2026-05-31T10:00Z → intents/archive/marketing-11.md -->
<!-- marketing-12 completed 2026-06-01T11:00Z → intents/archive/marketing-12.md -->
<!-- marketing-13 completed 2026-06-01T14:00Z → intents/archive/marketing-13.md -->
<!-- marketing-14 completed 2026-06-01T16:00Z → intents/archive/marketing-14.md -->
<!-- marketing-15 completed 2026-06-02T10:00Z → intents/archive/marketing-15.md -->
<!-- marketing-16 completed 2026-06-02T13:00Z → intents/archive/marketing-16.md -->
<!-- marketing-17 completed 2026-06-02T17:00Z → intents/archive/marketing-17.md -->
<!-- marketing-18 completed 2026-06-03T10:00Z → intents/archive/marketing-18.md -->
<!-- marketing-19 completed 2026-06-03T13:00Z → intents/archive/marketing-19.md -->
<!-- marketing-20 completed 2026-06-03T16:00Z → intents/archive/marketing-20.md -->
<!-- marketing-21 completed 2026-06-04T10:00Z → intents/archive/marketing-21.md -->
<!-- marketing-22 completed 2026-06-04T13:00Z → intents/archive/marketing-22.md -->
<!-- marketing-23 completed 2026-06-04T15:00Z → intents/archive/marketing-23.md -->
<!-- marketing-24 completed 2026-06-04T17:00Z → intents/archive/marketing-24.md -->
<!-- marketing-25 completed 2026-06-05T09:00Z → intents/archive/marketing-25.md -->
<!-- marketing-26 completed 2026-06-05T11:00Z → intents/archive/marketing-26.md -->
<!-- marketing-27 completed 2026-06-05T14:00Z → intents/archive/marketing-27.md -->
<!-- marketing-28 completed 2026-06-05T16:00Z → intents/archive/marketing-28.md -->
<!-- marketing-29 completed 2026-06-06T09:00Z → intents/archive/marketing-29.md -->
<!-- marketing-30 completed 2026-06-06T11:00Z → intents/archive/marketing-30.md -->
<!-- marketing-31 completed 2026-06-06T14:00Z → intents/archive/marketing-31.md -->
<!-- marketing-32 completed 2026-06-06T16:00Z → intents/archive/marketing-32.md -->
<!-- marketing-33 completed 2026-06-07T09:00Z → intents/archive/marketing-33.md -->
<!-- marketing-34 completed 2026-06-07T11:00Z → intents/archive/marketing-34.md -->
<!-- marketing-35 completed 2026-06-07T14:00Z → intents/archive/marketing-35.md -->
<!-- marketing-36 completed 2026-06-07T16:00Z → intents/archive/marketing-36.md -->
<!-- marketing-37 completed 2026-06-07T22:00Z → intents/archive/marketing-37.md -->
<!-- marketing-38 completed 2026-06-08T02:00Z → intents/archive/marketing-38.md -->
<!-- marketing-39 completed 2026-06-08T05:00Z → intents/archive/marketing-39.md -->
<!-- marketing-40 completed 2026-06-08T07:00Z → intents/archive/marketing-40.md -->
<!-- marketing-41 completed 2026-06-08T08:00Z → intents/archive/marketing-41.md -->
<!-- marketing-42 completed 2026-06-08T09:30Z → intents/archive/marketing-42.md -->
<!-- marketing-43 completed 2026-06-08T10:00Z → intents/archive/marketing-43.md -->
<!-- marketing-44 completed 2026-06-08T10:30Z → intents/archive/marketing-44.md -->
<!-- marketing-45 completed 2026-06-08T11:00Z → intents/archive/marketing-45.md -->
<!-- marketing-46 completed 2026-06-08T11:30Z → intents/archive/marketing-46.md -->
<!-- marketing-47 completed 2026-06-08T22:00Z → intents/archive/marketing-47.md -->
<!-- marketing-48 completed 2026-06-09T10:00Z → intents/archive/marketing-48.md -->
<!-- marketing-49 completed 2026-06-09T14:00Z → intents/archive/marketing-49.md -->
<!-- naver-shopping-01 2026-06-09T15:07Z router check → no new user blocker, no approval needed. Access still gated (Commerce ID + IP). No live store/listing/price/stock/shipping/ads/customer/order/account/public action. Next: curation/research continues. →reports/naver-shopping-01/2026-06-09T1507Z-router.html -->
<!-- naver-shopping-01 2026-06-10T15:07Z router check → workshop/question-card monetization path withdrawn by user. No live commerce/account/public action. 다음 Heartbeat에서 arrival-day angle 검증 계속. →reports/naver-shopping-01/2026-06-10T1507Z-router.html -->
<!-- naver-shopping-01 2026-06-11T00:35Z user-pref update → sourcing-first, luggage tags downgraded. No archive (active). next: broader sourcing-first screen. -->
<!-- naver-shopping-01 2026-06-12T07:00Z heartbeat → 소싱-퍼스트 브로드 스크린 완료. 포켓 미니 앨범 ADVANCE, 트래블러스노트 속지 PIVOT-SOURCING. No archive (active continues). →reports/naver-shopping-01/2026-06-12T0700Z-heartbeat.html -->
