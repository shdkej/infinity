# Intent Registry

> Heartbeat Agent가 주기적으로 읽고 실행하는 의도 목록.

## Inbox

## Active

<!-- naver-shopping-01 active 2026-06-10T00:08Z → intents/active/naver-shopping-01.md [display: 나래/Narae; projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,marketing; status: active-discovery-reset; approval: no-current-user-blocker] (사용자-facing 이름 나래/Narae 확정, 내부 id/path는 naver-shopping-agent 유지. 00:08Z: 사용자가 트래블러스노트/여행준비 속지 listing-copy 방향을 "너무 일반적"이라고 판단해 첫 SKU 후보에서 내렸다. 09:00 승인 질문은 resolved/rejected. 다음 탐색은 일반 체크리스트·플래너·속지 문법을 피하고, 실제 여행 실패/동선 리스크/현지 질문 수집/필드 인사이트 재사용/워크숍 대화 도구처럼 구매 이유가 더 선명한 후보를 찾는다. 새 네이버 호출 없음. 라이브 상품등록/가격·배송·재고/광고·고객·주문·계정·공개발행/브랜드·호환·규격 표현은 여전히 action-level approval-needed. archive 안 함(active 유지).) -->
<!-- marketing-49 active 2026-06-10T0600Z → intents/active/marketing-49.md [projects: virtue; type: strategy; topics: ai-product,activation,retention; target_agent: marketer] (Virtue 결과 카드 직후 수동 감탄 vs 자기화 행동 판독표 작성 (docs-only). goal: J1/J2/J4=deed_saved, J3=deed_judged 매핑을 재정의하지 않고 결과 카드 직후 30초 관찰용 수기 판독 칸 3-5개를 제안한다. permission: L1/L2 docs-only. success_criteria: 저장/재작성/선택/설명/무저장정상종료/수동감탄/마찰 행동 구분 제안, 신규 계측 0, approval-needed 경계 명시. artifact: artifacts/marketing-49/virtue-result-card-behavior-readout.md) -->

## Waiting

<!-- 사용자 결정, 외부 조건, 안전 확인 대기. 같은 질문을 반복하지 않고 상태만 보존한다. -->

## Archive

<!-- marketing-48 completed 2026-06-09T10:57Z → reports/marketing-48/2026-06-09T1057Z-local.html [projects: naver-shopping,infinity,personal-ops; type: marketing-positioning; topics: listing-copy,keyword-strategy,positioning; source: naver-shopping-01] (나래/Narae `naver-shopping-01`의 target-agent 요청을 처리해 트래블러스노트 standard-size travel-prep structured insert 피벗 SKU의 내부 listing title/copy 포지셔닝 후보군 작성 완료. 산출물 `artifacts/marketing-48/travelers-notebook-insert-listing-copy-positioning.md`. 제목 후보 8개, 금지/주의 제목 패턴, 1문장 가치제안, 상세페이지 첫 문단 후보, 검색 키워드 묶음, 썸네일 문구, 승격 전 검증 게이트 포함. 핵심: 큰 검색량 단어를 제목 맨 앞에 두지 않고, 리필/속지 구매 맥락과 여행준비 구조를 먼저 세움. 모든 문구는 draft/proposal-only, 브랜드명/호환/규격 표현은 approval-needed, 가격/배송/재고/옵션/광고/상품등록/공개상세/고객·주문·계정 액션 0. 게이트: `rg '여행 체크리스트.*트래블러스노트|트래블러스노트.*여행 체크리스트' artifacts/marketing-48` no-match, artifact에 draft/proposal-only/approval-needed 포함, HTML report `<html`/`<body`/axis ax1/axis ax2/`<details` 확인. MARKETING_LEARNINGS 승격 후보는 단일 사례라 report에 보류.) -->