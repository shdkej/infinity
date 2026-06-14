# Intent Registry

> Heartbeat Agent가 주기적으로 읽고 실행하는 의도 목록.

## Inbox






## Active

<!-- naver-shopping-01 active 2026-06-11T00:35Z → intents/active/naver-shopping-01.md [display: 나래/Narae; projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,marketing; status: active-sourcing-first; approval: user-setup-waiting-visible] (사용자-facing 이름 나래/Narae 확정, 내부 id/path는 naver-shopping-agent 유지. 2026-06-11 사용자 선호 업데이트: 나래는 상품제작보다 소싱 중심으로 보고, 러기지택/캐리어네임택은 선호 낮은 상품이라 다음 리드에서 내림. 2026-06-14 현재 실행 방향은 기성 여행-adjacent 소품 소싱 스크린이며 우선순위는 케이블/충전기 파우치 → 휴대폰 도난방지 스트랩/테더 → 압축/세탁물 분리 파우치. 사용자 설정이 필요한 SmartStore Commerce ID / 읽기 전용 브라우저 / 공개 Naver Shopping 검색 제한은 Waiting 카드로 별도 노출한다. 라이브 상품등록/가격·배송·재고/광고·고객·주문·계정·공개발행 0. archive 안 함(active 유지).) -->

## Waiting

<!-- 사용자 결정, 외부 조건, 안전 확인 대기. 같은 질문을 반복하지 않고 상태만 보존한다. -->

<!-- naver-shopping-01 waiting 2026-06-14T05:45Z → intents/active/naver-shopping-01.md [display: 나래/Narae; projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,commerce; decision: 네이버 커머스 사용자 설정 3가지를 언제 열어줄지 결정; options: 지금 Commerce ID/브라우저 세션 확인 | 나래는 공개/공식 데이터만으로 계속 진행 | 보류; default: 나래는 공개/공식 데이터만으로 계속 진행; reason: SmartStore Commerce ID, read-only browser access, and public Naver Shopping search restriction are user-side/external-condition blockers; next: 마스터가 Commerce ID/브라우저 접근을 열어주면 나래가 read-only 검증을 재개] (마스터 피드백 반영: 사용자가 해야 하는 설정/승인/외부조건은 적극적으로 Waiting에 걸어 둔다. 현재 대기: SmartStore Commerce ID 전환/로그인 확인, 사용자 브라우저 프로필 기반 read-only 접근 가능 여부, 에이전트 호스트의 공개 Naver Shopping 검색 제한 해소 또는 대체 접근. SAM/나래는 그 전까지 OpenAPI/SearchAd/공식 문서/공개 웹 중심의 소싱-퍼스트 리서치를 계속한다. 라이브 상품등록·가격·배송·재고·광고·고객/주문/계정 액션 0.) -->

## Archive
<!-- marketing-59 completed 2026-06-14T1200Z → intents/archive/marketing-59.md [display: Virtue Launch-Ready PLG Signal Gate; projects: virtue; type: strategy; topics: plg,activation,measurement,prelaunch] (PLG 신호를 Now/Defer/After-launch 3단계로 분류. deed_saved/deed_judged 중심 first-10 수기 gate 확립. 선행 marketing-55/56/57/58 충돌 없음. 산출물 artifacts/marketing-59/virtue-launch-ready-plg-signal-gate.md, report reports/marketing-59/2026-06-14T1200Z-local.html. 신규 이벤트·tracking/privacy·public copy·deploy·cost 변경 0.) -->

<!-- marketing-58 completed 2026-06-13T22:07Z → intents/archive/marketing-58.md [display: Virtue First Successful Output Contract; projects: virtue; type: strategy; topics: agentic-plg,activation,outcome-clarity,prelaunch] (Virtue J1-J4 first successful output contract를 L1 docs-only로 작성. 산출물 `artifacts/marketing-58/virtue-first-successful-output-contract.md`, report `reports/marketing-58/2026-06-13T2207Z-local.html`. J1/J2/J4=`deed_saved`, J3=`deed_judged` 매핑 유지. 잡별 화면 증거, 성공 출력 문장, 사용자 다음 행동, agent-readable 품질 기준, first-10 수기 관찰 컬럼 포함. 출처노트 존재 확인. 신규 이벤트·tracking/privacy·public copy·robots/sitemap·MCP/API·pricing·deploy·external message·cost 변경 0. conflict marker 0.) -->

<!-- marketing-57 completed 2026-06-13T10:07Z → intents/archive/marketing-57.md [display: Virtue Value Unit And Limit Trust Observation; projects: virtue; type: strategy; topics: ai-pricing,activation,trust,prelaunch] (first-10 관찰표에 value_unit_heard / limit_trust_signal / cap_copy_risk / value_before_limit / support_phrase_needed 후보 컬럼을 L1 docs-only로 추가. 산출물 `artifacts/marketing-57/virtue-value-unit-limit-trust-observation.md`, report `reports/marketing-57/2026-06-13T1007Z-local.html`. J1/J2/J4=`deed_saved`, J3=`deed_judged` 유지. pricing/billing/credit/cap/tracking/privacy/public copy/deploy/cost-bearing/product-affecting change 0.) -->


<!-- marketing-56 completed 2026-06-12T22:35Z → intents/archive/marketing-56.md [display: Virtue First Reliable Value Observation Columns; projects: virtue; type: strategy; topics: activation,onboarding,analytics] (AI PLG first reliable value lens를 Virtue first-10 관찰 계약에 L1 docs-only로 반영. 산출물 `artifacts/marketing-56/virtue-first-reliable-value-observation-columns.md`, report `reports/marketing-56/2026-06-12T2235Z-local.html`. 수기 컬럼 4개 accepted output / useful-result time / retry-rejudge reason / reproducibility understanding 추가. J1/J2/J4=`deed_saved`, J3=`deed_judged` 유지. 신규 이벤트·tracking/privacy·dashboard·public copy·deploy·external message·pricing·cap·cost 0.) -->

<!-- build-09 completed 2026-06-12T14:16Z → intents/archive/build-09.md [display: Control Center Static Publish Target Removed; projects: infinity,personal-ops,infrastructure; type: implementation; topics: dashboard,cms,auth,publish,deploy,rollback] (사용자가 정적 페이지로 만든 Control Center 제거를 요청해 `status-control-center-feed` publish target을 닫음. 이전 non-secret publish/rollback spec은 역사 기록으로 남기되, Waiting 질문은 종료. Status 정적 사이트의 `sites/status/dist/control-center/index.html` 삭제, Status 첫 화면 `./control-center/index.html` 링크 제거. 앞으로 Control Center publish 작업을 다시 열면 정적 Status subpage가 아니라 live CMS `https://cms.oracle.shdkej.com` 기준으로 새 target을 명시해야 함.) -->

<!-- build-08 completed 2026-06-12T10:40Z → reports/build-08/2026-06-12T1040Z-control-center-shadcn-status-composition.html [display: Control Center shadcn UI + Status Composition CMS; projects: infinity,personal-ops,infrastructure; type: implementation; topics: dashboard,cms,ui,status,supabase,deploy] (build-07 평면 CRUD CMS를 shadcn/ui 운영툴로 재구성하고 Status 페이지 구성을 웹에서 관리 가능하게 함. shadcn/ui(Tailwind v3, Button/Card/Badge/Input/Textarea/Label/Select/Tabs/Separator/Switch/Sheet drawer), 다크모드/모바일 대응. Supabase `public.control_center_nodes` self-referential 트리(surface/section/card/link, title/subtitle/url/status/sort_order/visible) + `public.control_center_activity` 감사 로그 신규, 둘 다 RLS enabled·정책 없음=service-role only. 기존 `control_center_items`는 Surface Registry 탭으로 유지. API `/api/nodes` CRUD+reorder, `/api/activity`, 모든 mutation이 activity 기록. UI=Status 구성 트리(순서/노출 토글+Edit drawer)·라이브 Preview·Surface Registry·Activity. 서비스 키는 K8s Secret `control-center-cms-env`에만. Space commits `f253ba9`, `904a6d5`. Supabase migration `control_center_status_composition`(project `ihpfnzwqbntjcirtrkjd`). 검증: local build PASS, rollout 1/1, ArgoCD Synced/Healthy, HTTPS 200, UI 마커 렌더, live `/api/nodes` create(201)→edit(200)→visibility(200)→invalid(400)→delete(200) PASS + activity 반영. 함정: root .gitignore의 bare `nodes` 패턴이 app/api/nodes/ 무음 제외→첫 배포 404, `git add -f`로 해소. 실제 production page write/publish·auth/permission·rollback은 미실행(승인 경계). next `build-09` Inbox로 연결.) -->

<!-- marketing-55 completed 2026-06-12T10:12Z → intents/archive/marketing-55.md [display: Virtue Prelaunch Activation Measurement Contract; projects: virtue; type: strategy; topics: activation,measurement,prelaunch] (Mixpanel 2026 PLG 측정 렌즈를 Virtue prelaunch first-value 계약으로 번역한 docs-only artifact 작성. 산출물 `artifacts/marketing-55/virtue-prelaunch-activation-measurement-contract.md`, report `reports/marketing-55/2026-06-12T1012Z-local.html`. J1/J2/J4=`deed_saved`, J3=`deed_judged` 매핑 유지. `count now`/`observe manually`/`do not judge yet`로 first-10 관찰을 분리하고 PQL/paid conversion/expansion/viral coefficient는 launch-after gate로 고정. 신규 이벤트·tracking/privacy·dashboard·public copy·deploy·external message·cost 0. `build-08` 미수정.) -->

<!-- build-07 completed 2026-06-12T10:05Z → reports/build-07/2026-06-12T1005Z-control-center-nextjs-supabase-cms.html [display: Control Center Next.js Supabase CRUD MVP; projects: infinity,personal-ops,infrastructure; type: implementation; topics: dashboard,cms,editing,supabase,deploy] -->
