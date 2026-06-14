# Intent Registry

> Heartbeat Agent가 주기적으로 읽고 실행하는 의도 목록.

## Inbox






## Active

<!-- naver-shopping-01 active 2026-06-11T00:35Z → intents/active/naver-shopping-01.md [display: 나래/Narae; projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,marketing; status: active-sourcing-first; approval: user-setup-waiting-visible] (사용자-facing 이름 나래/Narae 확정, 내부 id/path는 naver-shopping-agent 유지. 2026-06-11 사용자 선호 업데이트: 나래는 상품제작보다 소싱 중심으로 보고, 러기지택/캐리어네임택은 선호 낮은 상품이라 다음 리드에서 내림. 2026-06-14 현재 실행 방향은 기성 여행-adjacent 소품 소싱 스크린이며 우선순위는 케이블/충전기 파우치 → 휴대폰 도난방지 스트랩/테더 → 압축/세탁물 분리 파우치. 사용자 설정이 필요한 SmartStore Commerce ID / 읽기 전용 브라우저 / 공개 Naver Shopping 검색 제한은 Waiting 카드로 별도 노출한다. 라이브 상품등록/가격·배송·재고/광고·고객·주문·계정·공개발행 0. archive 안 함(active 유지).) -->

<!-- marketing-59 active 2026-06-14T10:15Z → intents/active/marketing-59.md [display: Virtue Launch-Ready PLG Signal Gate; projects: virtue; type: strategy; topics: plg,activation,measurement,prelaunch; permission: L1 docs-only; status: waiting-source-note] (최신 PLG 자료의 first win/activation/PQL 우선순위를 Virtue prelaunch 신호 위계로 번역한다. source note `source/external-links/marketing/2026-06-14-plg-signal-hierarchy.md` 미존재 — 사용자가 추가하면 즉시 실행 가능.) -->

## Waiting

<!-- 사용자 결정, 외부 조건, 안전 확인 대기. 같은 질문을 반복하지 않고 상태만 보존한다. -->

<!-- naver-shopping-01 waiting 2026-06-14T05:45Z → intents/active/naver-shopping-01.md [display: 나래/Narae; projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,commerce; decision: 네이버 커머스 사용자 설정 3가지를 언제 열어줄지 결정; options: 지금 Commerce ID/브라우저 세션 확인 | 나래는 공개/공식 데이터만으로 계속 진행 | 보류; default: 나래는 공개/공식 데이터만으로 계속 진행; reason: SmartStore Commerce ID, read-only browser access, and public Naver Shopping search restriction are user-side/external-condition blockers; next: 마스터가 Commerce ID/브라우저 접근을 열어주면 나래가 read-only 검증을 재개] (마스터 피드백 반영: 사용자가 해야 하는 설정/승인/외부조건은 적극적으로 Waiting에 걸어 둔다. 현재 대기: SmartStore Commerce ID 전환/로그인 확인, 사용자 브라우저 프로필 기반 read-only 접근 가능 여부, 에이전트 호스트의 공개 Naver Shopping 검색 제한 해소 또는 대체 접근. SAM/나래는 그 전까지 OpenAPI/SearchAd/공식 문서/공개 웹 중심의 소싱-퍼스트 리서치를 계속한다. 라이브 상품등록·가격·배송·재고·광고·고객/주문/계정 액션 0.) -->

<!-- marketing-59 waiting 2026-06-14T10:15Z → intents/active/marketing-59.md [display: Virtue Launch-Ready PLG Signal Gate; projects: virtue; type: strategy; topics: plg,activation,measurement,prelaunch; decision: source note `source/external-links/marketing/2026-06-14-plg-signal-hierarchy.md` 파일을 언제 추가할지 결정; options: 지금 source note 파일 생성 | 다음 heartbeat까지 보류; reason: marketing-59 first_gate 조건 — source note 존재 확인이 실행 전 필요; next: source note가 생성되면 즉시 marketing-59 실행 가능] (L1 docs-only PLG signal gate 작성. source note가 없어 실행 대기 중. PLG 자료 원문이 있어야 Virtue prelaunch 신호 위계 번역이 가능함.) -->