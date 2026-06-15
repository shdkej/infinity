# Intent Registry

> Heartbeat Agent가 주기적으로 읽고 실행하는 의도 목록.

## Inbox

## Active

<!-- naver-shopping-01 active 2026-06-15T01:15Z → intents/active/naver-shopping-01.md [display: 나래/Narae; projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,marketing; status: active-sourcing-first; approval: user-setup-waiting-visible] (2026-06-15 subtype 소싱-마찰 스크린 완료. 손목 스트랩(PROCEED FIRST): 소싱 마찰 최소·반품 리스크 낮음·컨텐츠 각도 명확. 세탁물 파우치(PROCEED FIRST): 경쟁 적음·마진 양호·여행 위생 각도 명확. 태그홀더 패치(AVOID): 접착제 반품·클레임 리스크 높음. 단순 압축 세트(HOLD): 포화 카테고리. 다음 안전 액션: 손목 스트랩 공급처 후보(1688/알리) + 세탁물 파우치 공급처 후보 조회. 사용자 설정 Waiting 항목(Commerce ID/브라우저/검색 IP 제한)은 유지. 라이브 상품등록/가격·배송·재고/광고·고객·주문·계정·공개발행 0. archive 안 함(active 유지).) -->

## Waiting

<!-- 사용자 결정, 외부 조건, 안전 확인 대기. 같은 질문을 반복하지 않고 상태만 보존한다. -->

<!-- naver-shopping-01 waiting 2026-06-14T05:45Z → intents/active/naver-shopping-01.md [display: 나래/Narae; projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,commerce; decision: 네이버 커머스 사용자 설정 3가지를 언제 열어줄지 결정; options: 지금 Commerce ID/브라우저 세션 확인 | 나래는 공개/공식 데이터만으로 계속 진행 | 보류; default: 나래는 공개/공식 데이터만으로 계속 진행; reason: SmartStore Commerce ID, read-only browser access, and public Naver Shopping search restriction are user-side/external-condition blockers; next: 마스터가 Commerce ID/브라우저 접근을 열어주면 나래가 read-only 검증을 재개] (마스터 피드백 반영: 사용자가 해야 하는 설정/승인/외부조건은 적극적으로 Waiting에 걸어 둔다. 현재 대기: SmartStore Commerce ID 전환/로그인 확인, 사용자 브라우저 프로필 기반 read-only 접근 가능 여부, 에이전트 호스트의 공개 Naver Shopping 검색 제한 해소 또는 대체 접근. SAM/나래는 그 전까지 OpenAPI/SearchAd/공식 문서/공개 웹 중심의 소싱-퍼스트 리서치를 계속한다. 라이브 상품등록·가격·배송·재고·광고·고객/주문/계정 액션 0.) -->

## Archive

<!-- naver-shopping-01 archive 2026-06-14T09:45Z → intents/active/naver-shopping-01.md [display: 나래/Narae; projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,commerce; completed: 소싱-퍼스트 전략 확정 및 마찰 스크린 실행; outcome: 손목 스트랩·세탁물 파우치 PROCEED FIRST 확인, 태그홀더 패치 AVOID, 단순 압축 세트 HOLD] (소싱-마찰 스크린 완료: 공급망 접근성, 반품 리스크, 컨텐츠 각도, 마진 구조 기준으로 4개 후보 평가. 최종 선택: 손목 스트랩(소싱 마찰 최소/반품 낮음/각도 명확)·세탁물 파우치(경쟁 적음/마진 양호/위생 각도). 공급처 후보 조회 단계로 이동. 사용자 설정 Waiting 항목은 유지. 라이브 상품등록/가격·배송·재고/광고·고객·주문·계정 액션 0.) -->

<!-- naver-shopping-01 archive 2026-06-14T07:30Z → intents/active/naver-shopping-01.md [display: 나래/Narae; projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,commerce; completed: 초기 카테고리 리서치 및 후보 선정; outcome: 4개 후보 상품 카테고리 식별 (손목 스트랩, 세탁물 파우치, 태그홀더 패치, 단순 압축 세트)] (공개 데이터 기반 초기 시장 리서치 완료: 네이버 쇼핑 트렌드, 경쟁 밀도, 마진 구조 분석. 소싱-퍼스트 접근으로 4개 후보 카테고리 선정. 다음 단계: 마찰 스크린 실행. 사용자 설정 항목(Commerce ID/브라우저/검색 IP)은 Waiting 유지.) -->

<!-- naver-shopping-01 archive 2026-06-14T05:00Z → intents/active/naver-shopping-01.md [display: 나래/Narae; projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,commerce; completed: 네이버 커머스 전략 초기 설정; outcome: 소싱-퍼스트 전략 채택, 공개 데이터 중심 접근 확정] (초기 전략 세션: 사용자와 네이버 쇼핑 진입 전략 논의. SmartStore 운영 구조, 소싱 우선순위, 에이전트 역할 정의. Commerce ID/브라우저 접근/검색 IP 제한은 사용자 설정 필요 항목으로 Waiting 등록. 나래는 공개/공식 데이터 중심으로 소싱-퍼스트 리서치를 계속하기로 확정.) -->

<!-- ARCHIVE ENTRY: naver-shopping-01 | 2026-06-13 to 2026-06-14 | Naver Shopping 진입 전략 수립 (초기) -->
<!-- Source: intents/active/naver-shopping-01.md | Agent: 나래/Narae | Type: coordination -->
<!-- Topics: automation, workflow, commerce, naver-shopping, sourcing -->
<!-- Summary: SmartStore 소싱-퍼스트 전략 수립. 공개 데이터 기반 카테고리 리서치, 마찰 스크린 완료. 손목 스트랩/세탁물 파우치 PROCEED FIRST. 사용자 설정 3개 항목 Waiting 유지. -->
<!-- Status at archive: active-sourcing-first | Live actions: 0 -->

<!-- ARCHIVE ENTRY: batch-production-review-01 | 2026-06-14 | 배치 생산 검토 -->
<!-- Source: intents/completed/batch-production-review-01.md | Agent: 나래/Narae | Type: research -->
<!-- Topics: manufacturing, sourcing, batch-production, MOQ, cost-analysis -->
<!-- Summary: 배치 생산 옵션 검토: MOQ, 단가, 카테고리별 정보 마찰, 마진 플로어 분석. 상장 승인 전 단계. 새 타겟 에이전트 요청 없음. 라이브 커머스/계정/공개 액션 없음. -->
<!-- Completed outcome: batch production, MOQ, unit cost, category/product-info friction, and margin floor before any listing approval. No new target-agent request opened and no live commerce/account/public action occurred. -->
