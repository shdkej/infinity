# Intent Registry

> Heartbeat Agent가 주기적으로 읽고 실행하는 의도 목록.

## Inbox

## Active

<!-- naver-shopping-01 active 2026-06-10T01:07Z → intents/active/naver-shopping-01.md [display: 나래/Narae; projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,marketing; status: active-second-discovery; approval: no-current-user-blocker] (사용자-facing 이름 나래/Narae 확정, 내부 id/path는 naver-shopping-agent 유지. 00:08Z 사용자가 트래블러스노트/여행준비 속지 방향을 "너무 일반적"이라고 판단해 첫 SKU 후보에서 내림. 01:07Z docs-only 2차 탐색: Knowledge Lab + bounded Naver OpenAPI/SearchAd로 후보군 재분류. 다음 검증 타깃은 질문카드/워크샵카드 product family(`질문 카드` OpenAPI ~18,840, `워크샵 카드` ~6,955; SearchAd `질문카드` 650/mo, `대화카드` 300/mo, small high-CTR `아이스브레이킹카드`/`인사이트카드`). anti-theft/document carry는 WATCH, route-risk/local-question travel cards는 HOLD. 다음 안전 액션은 질문/워크샵 카드 top-20 카테고리 스캔. 라이브 상품등록/가격·배송·재고/광고·고객·주문·계정·공개발행은 여전히 action-level approval-needed. archive 안 함(active 유지).) -->

## Waiting

<!-- 사용자 결정, 외부 조건, 안전 확인 대기. 같은 질문을 반복하지 않고 상태만 보존한다. -->

## Archive

<!-- marketing-49 completed 2026-06-10T0600Z → intents/archive/marketing-49.md [projects: virtue; type: strategy; topics: ai-product,activation,retention,onboarding] (Virtue 결과 카드 직후 수동 감탄 vs 자기화 행동 판독표 docs-only 작성 완료. 산출물 artifacts/marketing-49/passive-admiration-vs-self-appropriation-reading-sheet.md. J3 deed_judged 이후 무저장 종료를 J3 정상/수동 감탄/마찰 3분류 수기 판독 칸 5개로 제안. 기존 J1/J2/J4=deed_saved, J3=deed_judged 매핑 재정의 0, 신규 계측 0. ChartMogul 수동 감탄 함정을 Virtue 손기록 판독으로 번역.) -->

<!-- marketing-48 completed 2026-06-09T10:57Z → reports/marketing-48/2026-06-09T1057Z-local.html [projects: naver-shopping,infinity,personal-ops; type: marketing-positioning; topics: listing-copy,keyword-strategy,positioning; source: naver-shopping-01] (나래/Narae `naver-shopping-01`의 target-agent 요청을 처리해 트래블러스노트 standard-size travel-prep structured insert 피벗 SKU의 내부 listing title/copy 포지셔닝 후보군 작성 완료. 산출물 `artifacts/marketing-48/travelers-notebook-insert-listing-copy-positioning.md`. 제목 후보 8개, 금지/주의 제목 패턴, 1문장 가치제안, 상세페이지 첫 문단 후보, 검색 키워드 묶음, 썸네일 문구, 승격 전 검증 게이트 포함. 핵심: 큰 검색량 단어를 제목 맨 앞에 두지 않고, 리필/속지 구매 맥락과 여행준비 구조를 먼저 세움. 모든 문구는 draft/proposal-only, 브랜드명/호환/규격 표현은 approval-needed, 가격/배송/재고/옵션/광고/상품등록/공개상세/고객·주문·계정 액션 0. 게이트: `rg '여행 체크리스트.*트래블러스노트|트래블러스노트.*여행 체크리스트' artifacts/marketing-48` no-match, artifact에 draft/proposal-only/approval-needed 포함, HTML report `<html`/`<body`/axis ax1/axis ax2/`<details` 확인. MARKETING_LEARNINGS 승격 후보는 단일 사례라 report에 보류.) -->

<!-- marketing-47 completed 2026-06-08T22:07Z → reports/marketing-47/2026-06-08T2207Z-local.html [projects: virtue; type: strategy; topics: prelaunch,first-users,onboarding] (Virtue 첫 10명 design-user ask script 작성 완료. 산출물은 Infinity `artifacts/marketing-47/virtue-first-10-design-user-ask-script.md`(신규 1파일, docs-only — Virtue 앱 레포 로컬 부재로 ARTIFACT_RULES에 따라 Infinity artifact로 생성). 출처노트(YC/Lenny "초기 사용자는 확장 채널보다 직접 학습 루프로 만든다")를 Virtue prelaunch 첫 사용자 학습 루프로 번역해, 정식 출시 전 내부 준비물로 초대→사용 전 2문항→첫 세션 후 3문항→자기 말 기록 칸 4지점 손기록 스크립트를 한 장으로 고정. 잡별 초대 문장 후보(J1 기록형·J2 누적형·J3 AI 호기심형·J4 회고형)는 각 잡 first value를 미리 가리키게 작성(J1/J2/J4=`deed_saved`, J3=`deed_judged`, J3 무저장 종료 정상), m45 동사 프레임(판결 아닌 관점) 적용. 사용 전 2문항=현재 행동·대체재 / 잡 신호·기대; 첫 세션 후 3문항=first value 위치 / friction(`deed_save_capped`·503·지연=availability/friction) / 결정-위임 인지(출력을 판결 vs 조언으로 읽나, m45·m38). "사용자가 자기 말로 설명한 Virtue" 기록 칸은 원문 그대로 손기록(신규 계측 0), first-real-user-baseline-template로 흘러듦. 핵심: 첫 사용자 학습은 확장 채널보다 먼저이고 산출은 성패율이 아니라 (a)반복 문제 언어 (b)자기 말로 설명한 가치 (c)결정-위임 인지 세 언어로 읽으며, 성찰형 제품에서 도움의 목표는 결정 대행이 아니라 자기 말로 가치를 말하게 하는 것(도움이 성찰 대행하면 수집 대상 소거). 선행 3문서(first-real-user-baseline-template·first-60-second-value-observation-script·ai-promise-decision-control-audit-table) 충돌 0 — 층이 다른 추가. 변경한 가정 없음, 외부 행동 0. 금지선: 공개 발송/DM/광고·프로덕션 카피·신규 이벤트/속성/tracking/privacy/dashboard/session replay·배포·비용·권한 변경 0, 코드 접근·변경 0(앱 레포 로컬 부재). HTML 보고서 `<html`/`<body`/axis ax1/axis ax2/`<details` 포함 확인 + details에 계승한 기준·이번에 새로 배운 것·다음 Marketer 규칙·승격 후보 포함. MARKETING_LEARNINGS.md에 durable learning "First-User Learning Loop Reads Language, And Help Means Articulation Not Delegation" 승격. Infinity dirty 무관 파일(EVALUATION_NOTES.md) staging 제외. L2 agent-approved push.) -->

<!-- marketing-46 completed 2026-06-08T10:07Z → reports/marketing-46/2026-06-08T1007Z-local.html [projects: virtue; type: strategy; topics: agent-led-growth,ai-product,distribution,prelaunch] (Virtue agent-led growth fit/no-fit 경계표 작성 완료.) -->

<!-- marketing-45 completed 2026-06-07T23:07Z → reports/marketing-45/2026-06-07T2307Z-local.html [projects: virtue; type: strategy; topics: ai-trust,positioning,onboarding,prelaunch] (Virtue AI 약속 문장 decision-control 감사표 작성 완료.) -->

<!-- marketing-44 completed 2026-06-07T10:07Z → reports/marketing-44/2026-06-07T1007Z-local.html [projects: virtue; type: strategy; topics: ai-product,activation,onboarding,measurement] (Virtue 결과 카드 직후 30초 행동 감사표 작성 완료.) -->

<!-- research-12 completed 2026-06-07T04:07Z → intents/archive/research-12.md [projects: content-strategy,product-design,personal-brand; type: research; topics: format,differentiation,creative-strategy] (형식은 따르고 관점은 비트는 기준 조사 완료.) -->

<!-- marketing-43 completed 2026-06-06T22:07Z → reports/marketing-43/2026-06-06T2207Z-local.html [projects: virtue; type: strategy; topics: reactivation,retention,onboarding] -->

<!-- marketing-42 completed 2026-06-06T10:07Z → reports/marketing-42/2026-06-06T1007Z-local.html [projects: virtue; type: strategy; topics: session-value,activation,measurement] -->

<!-- marketing-41 completed 2026-06-05T23:07Z → reports/marketing-41/2026-06-05T2307Z-local.html [projects: virtue; type: strategy; topics: pql,monetization,activation] -->

<!-- marketing-40 completed 2026-06-05T10:07Z → reports/marketing-40/2026-06-05T1007Z-local.html [projects: virtue; type: strategy; topics: nudge,onboarding,ux] -->

<!-- marketing-39 completed 2026-06-04T23:08Z → reports/marketing-39/2026-06-04T2207Z-local.html [projects: virtue; type: strategy; topics: ai-trust,readiness,measurement] -->

<!-- marketing-38 completed 2026-06-04T10:27Z → reports/marketing-38/2026-06-04T1007Z-local.html [projects: virtue; type: strategy; topics: ai-trust,no-autonomous-action,safety] -->

<!-- research-11 completed 2026-06-04T00:27Z → intents/archive/research-11.md [projects: personal-brand; type: research] -->

<!-- marketing-37 completed 2026-06-03T22:07Z → reports/marketing-37/2026-06-03T2207Z-local.html [projects: virtue; type: strategy; topics: retention,correlation,measurement] -->

<!-- marketing-36 completed 2026-06-03T10:07Z → reports/marketing-36/2026-06-03T1007Z-local.html [projects: virtue; type: strategy; topics: measurement,activation,foundation] -->

<!-- marketing-35 completed 2026-06-02T23:07Z → reports/marketing-35/2026-06-02T2207Z-local.html [projects: virtue; type: strategy; topics: nudge,onboarding,trigger] -->

<!-- marketing-34 completed 2026-06-02T11:07Z → reports/marketing-34/2026-06-02T1007Z-local.html [projects: virtue; type: strategy; topics: measurement,activation,readiness] -->

<!-- marketing-33 completed 2026-06-01T22:07Z → reports/marketing-33/2026-06-01T2207Z-local.html [projects: virtue; type: strategy; topics: retention,correlation,activation] -->

<!-- marketing-32 completed 2026-06-01T10:07Z → reports/marketing-32/2026-06-01T1007Z-local.html [projects: virtue; type: strategy; topics: first-input,onboarding,job] -->

<!-- marketing-31 completed 2026-05-31T23:07Z → reports/marketing-31/2026-05-31T2307Z-local.html [projects: virtue; type: strategy; topics: product-body,bumper,session] -->

<!-- marketing-30 completed 2026-05-31T10:07Z → reports/marketing-30/2026-05-31T1007Z-local.html [projects: virtue; type: strategy; topics: shareworthiness,activation,first-value] -->

<!-- marketing-29 completed 2026-05-30T22:07Z → reports/marketing-29/2026-05-30T2207Z-local.html [projects: virtue; type: strategy; topics: session-value,activation,ai-proxy] -->

<!-- marketing-28 completed 2026-05-30T10:07Z → reports/marketing-28/2026-05-30T1007Z-local.html [projects: virtue; type: strategy; topics: monetization,boundary,pql] -->

<!-- marketing-27 completed 2026-05-29T22:25Z → reports/marketing-27/2026-05-29T2225Z-local.md [projects: virtue; type: strategy; topics: message-confusion,evidence,positioning] -->

<!-- marketing-26 completed 2026-05-29T11:07Z → intents/archive/marketing-26.md [projects: virtue; type: strategy; topics: retention,recovery,streak] -->

<!-- marketing-25 completed 2026-05-28T22:07Z → intents/archive/marketing-25.md [projects: virtue; type: strategy; topics: traffic-source,measurement,activation] -->

<!-- marketing-24 completed 2026-05-28T10:07Z → intents/archive/marketing-24.md [projects: virtue; type: strategy; topics: ai-trust,proxy,calibration] -->

<!-- research-10 completed 2026-05-28T16:07Z → intents/archive/research-10.md [projects: knowledge-lab; type: research] -->

<!-- marketing-23 completed 2026-05-27T22:07Z → intents/archive/marketing-23.md [projects: virtue; type: strategy; topics: prelaunch,measurement,decision-boundary] -->

<!-- marketing-22 completed 2026-05-27T10:07Z → intents/archive/marketing-22.md (Virtue 리텐션 예측 활성화 브리프 완료) -->

<!-- marketing-21 completed 2026-05-26T22:07Z → intents/archive/marketing-21.md (Virtue `/add` 입력-결과 흐름 마찰 감사 완료) -->

<!-- marketing-20 completed 2026-05-26T15:07Z → intents/archive/marketing-20.md (Virtue 첫 60초 가치 관찰 스크립트 완료) -->

<!-- marketing-19 completed 2026-05-26T10:07Z → intents/archive/marketing-19.md (Virtue 신규 사용자 홈 화면 감사 완료) -->

<!-- marketing-18 completed 2026-05-26T00:07Z → intents/archive/marketing-18.md (Virtue AEO / Agent-Readable 표면 전략 완료) -->

<!-- marketing-17 completed 2026-05-25T22:07Z → intents/archive/marketing-17.md (Virtue 첫 세션 정성 마찰 관찰 완료) -->

<!-- research-09 completed 2026-05-25T12:30Z → intents/archive/research-09.md (1인기업 강점 살리기 vs 한계 조기 인정 기준 조사 완료) -->

<!-- marketing-16 completed 2026-05-25T10:07Z → intents/archive/marketing-16.md (Virtue 첫 세션 3-스크린 가치 흐름 완료) -->

<!-- marketing-15 completed 2026-05-24T22:07Z → intents/archive/marketing-15.md (Virtue 웹/iOS 활성화 이벤트 정의 완료) -->

<!-- marketing-14 completed 2026-05-24T15:56Z → intents/archive/marketing-14.md (Virtue 첫 주 활성화-리텐션 연결 브리프 완료) -->

<!-- marketing-13 completed 2026-05-23T22:07Z → intents/archive/marketing-13.md (Virtue 경쟁 대안 기반 포지셔닝 완료) -->

<!-- marketing-10 completed 2026-05-23T16:07Z → intents/archive/marketing-10.md (Virtue Time-to-Value 측정 프레임 완료) -->

<!-- marketing-12 completed 2026-05-23T10:18Z → intents/archive/marketing-12.md (Virtue 활성화 경로 마찰 감사 완료) -->

<!-- research-08 completed 2026-05-23T10:30Z → intents/archive/research-08.md (GEO/LLMO 체크리스트 조사 완료) -->

<!-- marketing-11 completed 2026-05-22T22:17Z → intents/archive/marketing-11.md (Virtue 첫 실사용자 기준선 템플릿 완료) -->

<!-- marketing-09 completed 2026-05-21T22:07Z → intents/archive/marketing-09.md (Virtue 활성화 마일스톤 사다리 완료) -->

<!-- marketing-01 completed 2026-05-21T10:17Z → intents/archive/marketing-01.md (Virtue add-flow telemetry 완료) -->

<!-- marketing-08 completed 2026-05-21T10:07Z → intents/archive/marketing-08.md (Virtue PMF 응답 분석 루브릭 완료) -->

<!-- marketing-07 completed 2026-05-20T22:07Z → intents/archive/marketing-07.md (Virtue 최소 생존 오디언스 기준 완료) -->

<!-- marketing-06 completed 2026-05-20T10:07Z → intents/archive/marketing-06.md (Virtue 첫 세션 JTBD 매트릭스 완료) -->

<!-- marketing-05 completed 2026-05-19T22:07Z → intents/archive/marketing-05.md (Virtue 빈 상태/첫 행동 감사 완료) -->

<!-- marketing-04 completed 2026-05-19T10:07Z → intents/archive/marketing-04.md (Virtue 첫인상 포지셔닝 스냅샷 완료) -->

<!-- marketing-03 completed 2026-05-18T22:20Z → intents/archive/marketing-03.md (Virtue 첫 7일 deed_saved 흐름 완료) -->

<!-- marketing-02 completed 2026-05-16T14:00Z → intents/archive/marketing-02.md (마찰점 4개 특정, 개선 후보 3개 완료) -->

<!-- research-07 completed 2026-05-13T12:00 → intents/archive/research-07.md -->

<!-- product-01 completed 2026-05-15T11:44Z → intents/archive/product-01.md (Virtue 최신 상태, 후속 개선은 별도 intent) -->

<!-- build-02 completed 2026-05-13 → intents/archive/build-02.md (https://infinity.oracle.shdkej.com 배포 완료) -->
