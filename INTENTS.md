# Intent Registry

> Heartbeat Agent가 주기적으로 읽고 실행하는 의도 목록.

## Inbox


## Active

<!-- naver-shopping-01 active 2026-06-11T00:35Z → intents/active/naver-shopping-01.md [display: 나래/Narae; projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,marketing; status: active-sourcing-first; approval: user-setup-waiting-visible] (사용자-facing 이름 나래/Narae 확정, 내부 id/path는 naver-shopping-agent 유지. 2026-06-11 사용자 선호 업데이트: 나래는 상품제작보다 소싱 중심으로 보고, 러기지택/캐리어네임택은 선호 낮은 상품이라 다음 리드에서 내림. 2026-06-14 현재 실행 방향은 기성 여행-adjacent 소품 소싱 스크린이며 우선순위는 케이블/충전기 파우치 → 휴대폰 도난방지 스트랩/테더 → 압축/세탁물 분리 파우치. 사용자 설정이 필요한 SmartStore Commerce ID / 읽기 전용 브라우저 / 공개 Naver Shopping 검색 제한은 Waiting 카드로 별도 노출한다. 라이브 상품등록/가격·배송·재고/광고·고객·주문·계정·공개발행 0. archive 안 함(active 유지).) -->

## Waiting

<!-- 사용자 결정, 외부 조건, 안전 확인 대기. 같은 질문을 반복하지 않고 상태만 보존한다. -->

<!-- naver-shopping-01 waiting 2026-06-14T05:45Z → intents/active/naver-shopping-01.md [display: 나래/Narae; projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,commerce; decision: 네이버 커머스 사용자 설정 3가지를 언제 열어줄지 결정; options: 지금 Commerce ID/브라우저 세션 확인 | 나래는 공개/공식 데이터만으로 계속 진행 | 보류; default: 나래는 공개/공식 데이터만으로 계속 진행; reason: SmartStore Commerce ID, read-only browser access, and public Naver Shopping search restriction are user-side/external-condition blockers; next: 마스터가 Commerce ID/브라우저 접근을 열어주면 나래가 read-only 검증을 재개] (마스터 피드백 반영: 사용자가 해야 하는 설정/승인/외부조건은 적극적으로 Waiting에 걸어 둔다. 현재 대기: SmartStore Commerce ID 전환/로그인 확인, 사용자 브라우저 프로필 기반 read-only 접근 가능 여부, 에이전트 호스트의 공개 Naver Shopping 검색 제한 해소 또는 대체 접근. SAM/나래는 그 전까지 OpenAPI/SearchAd/공식 문서/공개 웹 중심의 소싱-퍼스트 리서치를 계속한다. 라이브 상품등록·가격·배송·재고·광고·고객/주문/계정 액션 0.) -->

## Archive
<!-- marketing-59 completed 2026-06-14T13:00Z → intents/archive/marketing-59.md [display: Virtue Launch-Ready PLG Signal Gate; projects: virtue; type: strategy; topics: plg,activation,measurement,prelaunch] (PLG 신호 위계를 Virtue prelaunch 3열 게이트로 번역. 지금 볼 신호/보류할 신호/launch 이후 볼 신호 표와 first-10 수기 review checklist 완성. J1/J2/J4=`deed_saved`, J3=`deed_judged` 유지. 선행 marketing-55/56/58 충돌 없음. 신규 이벤트·tracking/privacy·dashboard·public copy·deploy·external message·cost 변경 0.) -->

<!-- marketing-58 completed 2026-06-13T22:07Z → intents/archive/marketing-58.md [display: Virtue First Successful Output Contract; projects: virtue; type: strategy; topics: agentic-plg,activation,outcome-clarity,prelaunch] (Virtue J1-J4 first successful output contract를 L1 docs-only로 작성. 산출물 `artifacts/marketing-58/virtue-first-successful-output-contract.md`, report `reports/marketing-58/2026-06-13T2207Z-local.html`. J1/J2/J4=`deed_saved`, J3=`deed_judged` 매핑 유지. 잡별 화면 증거, 성공 출력 문장, 사용자 다음 행동, agent-readable 품질 기준, first-10 수기 관찰 컬럼 포함. 출처노트 존재 확인. 신규 이벤트·tracking/privacy·public copy·robots/sitemap·MCP/API·pricing·deploy·external message·cost 변경 0. conflict marker 0.) -->

<!-- marketing-57 completed 2026-06-13T10:07Z → intents/archive/marketing-57.md [display: Virtue Value Unit And Limit Trust Observation; projects: virtue; type: strategy; topics: ai-pricing,activation,trust,prelaunch] (first-10 관찰표에 value_unit_heard / limit_trust_signal / cap_copy_risk / value_before_limit / support_phrase_needed 후보 컬럼을 L1 docs-only로 추가. 산출물 `artifacts/marketing-57/virtue-value-unit-limit-trust-observation.md`, report `reports/marketing-57/2026-06-13T1007Z-local.html`. J1/J2/J4=`deed_saved`, J3=`deed_judged` 유지. pricing/billing/credit/cap/tracking/privacy/public copy/deploy/cost-bearing/product-affecting change 0.) -->


<!-- marketing-56 completed 2026-06-12T22:35Z → intents/archive/marketing-56.md [display: Virtue First Reliable Value Observation Columns; projects: virtue; type: strategy; topics: activation,onboarding,analytics] (AI PLG first reliable value lens를 Virtue first-10 관찰 계약에 L1 docs-only로 반영. 산출물 `artifacts/marketing-56/virtue-first-reliable-value-observation-columns.md`, report `reports/marketing-56/2026-06-12T2235Z-local.html`. 수기 컬럼 4개 accepted output / useful-result time / retry-rejudge reason / reproducibility understanding 추가. J1/J2/J4=`deed_saved`, J3=`deed_judged` 유지. 신규 이벤트·tracking/privacy·dashboard·public copy·deploy·external message·pricing·cap·cost 0.) -->

<!-- build-09 completed 2026-06-12T14:16Z → intents/archive/build-09.md [display: Control Center Static Publish Target Removed; projects: infinity,personal-ops,infrastructure; type: implementation; topics: dashboard,cms,auth,publish,deploy,rollback] (사용자가 정적 페이지로 만든 Control Center 제거를 요청해 `status-control-center-feed` publish target을 닫음. 이전 non-secret publish/rollback spec은 역사 기록으로 남기되, Waiting 질문은 종료. Status 정적 사이트의 `sites/status/dist/control-center/index.html` 삭제, Status 첫 화면 `./control-center/index.html` 링크 제거. 앞으로 Control Center publish 작업을 다시 열면 정적 Status subpage가 아니라 live CMS `https://cms.oracle.shdkej.com` 기준으로 새 target을 명시해야 함.) -->