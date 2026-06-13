# Intent Registry

> Heartbeat Agent가 주기적으로 읽고 실행하는 의도 목록.

## Inbox


## Active

<!-- naver-shopping-01 active 2026-06-11T00:35Z → intents/active/naver-shopping-01.md [display: 나래/Narae; projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,marketing; status: active-sourcing-first-luggage-tags-downgraded; approval: no-current-user-blocker] (사용자-facing 이름 나래/Narae 확정, 내부 id/path는 naver-shopping-agent 유지. 00:08Z 트래블러스노트/여행준비 속지는 "너무 일반적"으로 첫 SKU 후보에서 내림. 14:09Z 사용자 피드백으로 워크샵/질문카드 monetization path는 Naver revenue/SKU 후보에서 철회됨. 20:07Z paper/card-led arrival-day failure-prevention insert keyword test 완료: `해외여행 체크리스트`는 clean-ish paper/planner shelf(OpenAPI 32,278; SearchAd 310 PC + 1,750 mobile/mo)지만 mobile CTR 0.05%로 buyer intent 약하고 generic checklist/planner commodity. `여행 준비 카드`/`여행 체크리스트 카드`는 trading cards/photo-card holders/boards/wallets/imported goods noise가 큼. emergency/safety/contact-card 언어는 story-rich but keyword-weak/non-travel/privacy-sensitive. 결론은 **HOLD / paper-card insert를 lead SKU로 만들지 않음**. 산출물 `naver-shopping-agent/arrival-day-insert-keyword-test-2026-06-10.md`, report `reports/naver-shopping-01/2026-06-10T2007Z-local.html`. 2026-06-11 사용자 선호 업데이트: 나래는 상품제작보다 소싱 중심으로 보고, 러기지택/캐리어네임택은 선호 낮은 상품이라 다음 리드에서 내림. 다음 안전 액션은 broader sourcing-first screen. 라이브 상품등록/가격·배송·재고/광고·고객·주문·계정·공개발행 0. archive 안 함(active 유지).) -->



## Waiting

<!-- 사용자 결정, 외부 조건, 안전 확인 대기. 같은 질문을 반복하지 않고 상태만 보존한다. -->

## Archive

<!-- marketing-57 completed 2026-06-13T12:00Z → intents/archive/marketing-57.md [display: Virtue Value Unit And Limit Trust Observation; projects: virtue; type: strategy; topics: ai-pricing,activation,trust,prelaunch] (AI pricing/credit 자료 기반 prelaunch first-10 관찰표에 value unit / limit trust 컬럼 2세트(4컬럼) 추가. 산출물 `artifacts/marketing-57/virtue-value-unit-limit-trust-observation-columns.md`, report `reports/marketing-57/2026-06-13T1200Z.html`. value unit named / value unit match / limit encountered / limit read 컬럼 + cap/copy 해석 금지선 7개 명시. J1/J2/J4=`deed_saved`, J3=`deed_judged` 유지. 신규 이벤트·tracking/privacy·dashboard·public copy·deploy·pricing·billing·credit·cap·cost 0.) -->

<!-- marketing-56 completed 2026-06-12T22:35Z → intents/archive/marketing-56.md [display: Virtue First Reliable Value Observation Columns; projects: virtue; type: strategy; topics: activation,onboarding,analytics] (AI PLG first reliable value lens를 Virtue first-10 관찰 계약에 L1 docs-only로 반영. 산출물 `artifacts/marketing-56/virtue-first-reliable-value-observation-columns.md`, report `reports/marketing-56/2026-06-12T2235Z-local.html`. 수기 컬럼 4개 accepted output / useful-result time / retry-rejudge reason / reproducibility understanding 추가. J1/J2/J4=`deed_saved`, J3=`deed_judged` 유지. 신규 이벤트·tracking/privacy·dashboard·public copy·deploy·external message·pricing·cap·cost 0.) -->

<!-- build-09 completed 2026-06-12T14:16Z → intents/archive/build-09.md [display: Control Center Static Publish Target Removed; projects: infinity,personal-ops,infrastructure; type: implementation; topics: dashboard,cms,auth,publish,deploy,rollback] (사용자가 정적 페이지로 만든 Control Center 제거를 요청해 `status-control-center-feed` publish target을 닫음. 이전 non-secret publish/rollback spec은 역사 기록으로 남기되, Waiting 질문은 종료. Status 정적 사이트의 `sites/status/dist/control-center/index.html` 삭제, Status 첫 화면 `./control-center/index.html` 링크 제거. 앞으로 Control Center publish 작업을 다시 열면 정적 Status subpage가 아니라 live CMS `https://cms.oracle.shdkej.com` 기준으로 새 target을 명시해야 함.) -->

<!-- build-08 completed 2026-06-12T10:40Z → reports/build-08/2026-06-12T1040Z-control-center-shadcn-status-composition.html [display: Control Center shadcn UI + Status Composition CMS; projects: infinity,personal-ops,infrastructure; type: implementation; topics: dashboard,cms,ui,status,supabase,deploy] (build-07 평면 CRUD CMS를 shadcn/ui 운영툴로 재구성하고 Status 페이지 구성을 웹에서 관리 가능하게 함. shadcn/ui(Tailwind v3, Button/Card/Badge/Input/Textarea/Label/Select/Tabs/Separator/Switch/Sheet drawer), 다크모드/모바일 대응. Supabase `public.control_center_nodes` self-referential 트리(surface/section/card/link, title/subtitle/url/status/sort_order/visible) + `public.control_center_activity` 감사 로그 신규, 둘 다 RLS enabled·정책 없음=service-role only. 기존 `control_center_items`는 Surface Registry 탭으로 유지. API `/api/nodes` CRUD+reorder, `/api/activity`, 모든 mutation이 activity 기록. UI=Status 구성 트리(순서/노출 토글+Edit drawer)·라이브 Preview·Surface Registry·Activity. 서비스 키는 K8s Secret `control-center-cms-env`에만. Space commits `f253ba9`, `904a6d5`. Supabase migration `control_center_status_composition`(project `ihpfnzwqbntjcirtrkjd`). 검증: local build PASS, rollout 1/1, ArgoCD Synced/Healthy, HTTPS 200, UI 마커 렌더, live `/api/nodes` create(201)→edit(200)→visibility(200)→invalid(400)→delete(200) PASS + activity 반영. 함정: root .gitignore의 bare `nodes` 패턴이 app/api/nodes/ 무음 제외→첫 배포 404, `git add -f`로 해소. 실제 production page write/publish·auth/permission·rollback은 미실행(승인 경계). next `build-09` Inbox로 연결.) -->

<!-- marketing-55 completed 2026-06-12T10:12Z → intents/archive/marketing-55.md [display: Virtue Prelaunch Activation Measurement Contract; projects: virtue; type: strategy; topics: activation,measurement,analytics] -->

<!-- marketing-54 completed 2026-06-11T23:40Z → intents/archive/marketing-54.md [display: Virtue First-10 Expectation Outcome Blocker Loop Audit; projects: virtue; type: strategy; topics: activation,onboarding,analytics] -->

<!-- marketing-53 completed 2026-06-11T18:00Z → intents/archive/marketing-53.md [display: Virtue Intent-to-Task-Completion Audit Table; projects: virtue; type: strategy; topics: activation,onboarding,analytics] -->

<!-- marketing-52 completed 2026-06-11T09:30Z → intents/archive/marketing-52.md [display: Virtue Prompt Design For Desired Result; projects: virtue; type: strategy; topics: onboarding,activation,ux] -->

<!-- marketing-51 completed 2026-06-11T07:30Z → intents/archive/marketing-51.md [display: Virtue Guided First-Value Four-Stage Handoff; projects: virtue; type: strategy; topics: onboarding,activation,ux] -->

<!-- marketing-50 completed 2026-06-10T23:30Z → intents/archive/marketing-50.md [display: Purchase Situation Before Object Shape; projects: virtue,naver-shopping; type: strategy; topics: positioning,marketing,naver] -->

<!-- marketing-49 completed 2026-06-10T08:00Z → intents/archive/marketing-49.md [display: Virtue First-60-Second Value Observation Script; projects: virtue; type: strategy; topics: onboarding,activation,ux] -->

<!-- marketing-48 completed 2026-06-09T20:00Z → intents/archive/marketing-48.md [display: Virtue AI Promise Decision Control Audit; projects: virtue; type: strategy; topics: trust,onboarding,ux] -->

<!-- marketing-47 completed 2026-06-09T10:00Z → intents/archive/marketing-47.md [display: Virtue First-10 Design-User Ask Script; projects: virtue; type: strategy; topics: onboarding,activation,firstusers] -->

<!-- marketing-46 completed 2026-06-08T22:00Z → intents/archive/marketing-46.md -->
<!-- marketing-45 completed 2026-06-08T12:00Z → intents/archive/marketing-45.md -->
<!-- marketing-44 completed 2026-06-07T22:00Z → intents/archive/marketing-44.md -->
<!-- marketing-43 completed 2026-06-07T10:00Z → intents/archive/marketing-43.md -->
<!-- marketing-42 completed 2026-06-06T22:00Z → intents/archive/marketing-42.md -->
<!-- marketing-41 completed 2026-06-06T10:00Z → intents/archive/marketing-41.md -->
<!-- marketing-40 completed 2026-06-05T22:00Z → intents/archive/marketing-40.md -->
<!-- marketing-39 completed 2026-06-05T10:00Z → intents/archive/marketing-39.md -->
<!-- marketing-38 completed 2026-06-04T22:00Z → intents/archive/marketing-38.md -->
<!-- marketing-37 completed 2026-06-04T10:00Z → intents/archive/marketing-37.md -->
<!-- marketing-01 completed → intents/archive/marketing-01.md -->
<!-- wiki-04 completed → intents/archive/wiki-04.md -->
<!-- wiki-03 completed → intents/archive/wiki-03.md -->
<!-- wiki-02 completed → intents/archive/wiki-02.md -->
<!-- wiki-01 completed → intents/archive/wiki-01.md -->
<!-- doc-01 completed → intents/archive/doc-01.md -->
<!-- monitor-01 completed → intents/archive/monitor-01.md -->
<!-- build-01 completed → intents/archive/build-01.md -->
