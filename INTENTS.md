# Intent Registry

> Heartbeat Agent가 주기적으로 읽고 실행하는 의도 목록.

## Inbox

## Active

### design-01 · 카드뉴스 미감 업그레이드
- id: design-01
- status: in_progress
- priority: medium
- target_agent: workflow-master
- projects: content, card-news, design-system
- task_type: design-audit
- topics: card-news, visual-system, library
- goal: 카드뉴스 산출물의 미감을 한 단계 올리기 위해 최근 카드뉴스 결과물과 제작 파이프라인을 감사하고, 앞으로 반복 적용할 시각 기준과 샘플 개선안을 만든다.
- next_action: 로컬에서 `skills/insight-card-maker` 출력물로 cloud prepare 가설(5개 실패 패턴, 7개 실행 규칙)을 검증하고 샘플 preview 1개를 모바일 기준으로 작성한다.
- prepare_report: reports/design-01/2026-07-01T0100Z.html
- constraints: 공개 라이브러리 대량 재렌더, 기존 산출물 일괄 교체, 외부 비용, 공개 배포, 사용자 이미지 라이브러리의 임의 생성 이미지 대체는 별도 승인 전에는 하지 않는다.

### design-02 · 카드뉴스 첫페이지 후킹 개선 실험
- id: design-02
- status: active
- priority: high
- target_agent: workflow-master
- schedule_window: 2026-07-02 05:00-08:00 KST
- projects: content, card-news, design-system
- task_type: design
- topics: card-news, hook, cover
- goal: 카드뉴스 첫 페이지가 스크롤을 멈추게 하는 힘을 높이기 위해 제목/이미지/여백/첫 문장 조합을 실험하고, 실험 결과와 다음 개선사항을 남긴다.
- next_action: 2026-07-02 05:00 KST 이후 실행. 최근 카드뉴스 첫 페이지 3-5개를 골라 `왜 멈추지 않는지 / 왜 읽히는지`를 판독한다.
- constraints: 2026-07-02 08:00 KST 전에 작업을 닫는다. 승인 없이 공개 라이브러리 배포, 기존 카드뉴스 교체, 대량 재생성, 외부 비용, 사용자 이미지의 임의 생성 이미지 대체는 하지 않는다.

## Waiting

<!-- 사용자 결정, 외부 조건, 안전 확인 대기. 같은 질문을 반복하지 않고 상태만 보존한다. -->
<!-- marketing-95 waiting 2026-06-30T2200Z -> intents/waiting/marketing-95.md [projects: virtue,infinity; type: verification; topics: marketing,activation,deploy,return-state] (marketing-92 로컬 구현은 끝났지만 2026-06-30 22:00 UTC 라이브 홈 HTML에는 여전히 `612덕`와 첫 방문 카피, `첫 기록이 여기에 쌓여요.` empty-state가 함께 남아 있다. 앱 업데이트/배포 반영 전까지는 실패 재판정 대신 Waiting으로 유지하고, 배포 후 returning empty-state 분기 노출 여부만 다시 확인한다.) -->

## Archive
<!-- marketing-96 completed 2026-07-01T1007Z → intents/archive/marketing-96.md [projects: virtue,infinity; type: implementation; topics: marketing,activation] (기존 `marketing-79` 관찰표에 붙여 쓰는 추천 언어 보강안을 추가해 `누구에게 뭐라고 소개하겠는가`와 `지금 추천을 망설이게 하는 이유` 2필드, 기록 규칙, J3 예시 1세트를 고정했다. HTML report gate passed.) -->
<!-- naver-shopping-01 completed-first-pass 2026-07-01T0035Z → intents/archive/naver-shopping-01.md [display: 나래/Narae; projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,marketing] (사용자 지시에 따라 나래 1차 작업 종료. 손목 스트랩 1순위 + 크로스바디/넥 폰 스트랩 2순위 샘플 검토 준비 상태를 보존하고, 명시적 재호출 전까지 alibaba.com 공급사 확인·샘플 주문 승인 요청·08:30/09:00 자동 루프를 중단한다.) -->
<!-- marketing-94 completed 2026-06-30T1007Z -> intents/archive/marketing-94.md [projects: virtue,infinity; type: strategy; topics: marketing,activation,product,session-replay] (`marketing-87` 4분류를 유지한 채 pass-vs-hold 비교용 보조 문서 1장을 추가해, `judged but not saved`를 자동 실패로 읽지 않고 양쪽 세션에 반복되는 마찰만 다음 수정 후보로 올리는 규칙을 고정했다. HTML report gate passed.) -->
<!-- marketing-93 completed 2026-06-29T2207Z -> intents/archive/marketing-93.md [projects: virtue,infinity; type: strategy; topics: marketing,activation,product] (현재 홈·`/add`·반환 표면 언어를 J1~J4 기준으로 판독해, 지금 가장 잘 맞는 행복한 첫 사용자는 J1 기록형 중심이고 J2 누적형이 보조라는 기준표를 고정했다. HTML report gate passed.) -->
<!-- marketing-92 completed 2026-06-29T1829Z -> intents/archive/marketing-92.md [projects: virtue,infinity; type: implementation; topics: marketing,activation,retention] (홈 최근 덕행 empty-state를 `stats.count`와 `recent.length`로 분리해 복귀 사용자의 first-visit 카피 재노출을 막고, typecheck 통과·기존 lint warning만 확인했다.) -->
<!-- 이 섹션의 상세 이력은 2026-06-17T10:24Z Heartbeat 과정에서 INTENTS.md 갱신 중 일시 유실됨. 개별 intent 원장은 intents/archive/*.md 에 모두 보존되어 있음. -->
<!-- research-24 completed 2026-06-29T0600Z → intents/archive/research-24.md (capture·claim·open_loop 3필드 경계를 "있었던 것 / 내린 것 / 모르는 것"으로 고정하고 회고·Threads·카드뉴스 산출물 연결 규칙을 1장으로 정리했다.) -->
<!-- marketing-91 completed 2026-06-28T2229Z → intents/archive/marketing-91.md [projects: virtue, infinity; type: strategy; topics: marketing, activation, product] (기존 이벤트 조합과 홈 반환 사례를 `정상 진행 / 자연 종료 / 마찰 / 상태 모순` 4개 상태 언어로 고정했다.) -->
<!-- marketing-90 completed 2026-06-28T1007Z → intents/archive/marketing-90.md [projects: virtue, infinity; type: strategy; topics: marketing, activation, product] (Virtue 첫 세션을 진입 약속, 입력 기대, 반환 일관성의 3게이트로 압축했고 현재 우선 보수 대상은 gate 3 반환 일관성으로 고정했다. HTML report gate passed.) -->
<!-- marketing-89 completed 2026-06-27T2236Z → intents/archive/marketing-89.md [projects: virtue, infinity; type: strategy; topics: marketing, activation, product] (Virtue 홈 반환 상태에서 `stats.total`, `stats.count`, `recent.length`의 계약과 empty-state 허용/금지 조건을 1장으로 고정했다.) -->
<!-- marketing-88 completed 2026-06-27T1007Z → intents/archive/marketing-88.md [projects: virtue, infinity; type: strategy; topics: marketing, activation, product] (라이브 홈, 로컬 홈 코드, 최근 canonical 제안서를 대조해 반환 세션 state drift를 한 장으로 정리했다. HTML report gate passed.) -->
<!-- marketing-87 completed 2026-06-26T222904Z → intents/archive/marketing-87.md [projects: virtue, infinity; type: strategy; topics: marketing, activation, product] (기존 `/add` 이벤트와 replay 관찰 질문을 묶어 첫 10~15세션을 공통 UX 마찰, J3 자연 종료, 조용한 실패, 다음 행동 불명확의 4분류로 읽는 1장 판독표 완성. HTML report gate passed.) -->
<!-- marketing-86 completed 2026-06-26T10:28Z → intents/archive/marketing-86.md [projects: virtue, infinity; type: strategy; topics: marketing, activation, product] (J1/J2/J4는 홈 최근 덕행, J3는 결과 카드를 primary surface로 삼는 next action helper proposal 완료) -->
<!-- marketing-85 completed 2026-06-25T220708Z → intents/archive/marketing-85.md [projects: virtue; type: strategy; topics: marketing,activation,prelaunch,observation] (첫 10명 관찰표 `다음 행동 명료성` 질문 보강 완료. HTML report gate passed.) -->
<!-- marketing-84 completed 2026-06-25T1028Z → intents/archive/marketing-84.md [projects: virtue; type: strategy; topics: marketing,activation,retention] (첫 가치 다음의 next-step bridge 감사표/제안서 완료. HTML report gate passed.) -->
<!-- research-21 completed 2026-06-25T0507Z → intents/archive/research-21.md [projects: infinity,research-bank,personal-ops; type: research; topics: workflow,content] (6개 사례를 기록 방식·정리 방식·검증 방식·출판 변환 방식으로 비교해, Infinity용 일일 3줄·주간 3묶음·월간 1산출물 루프를 제안했다. HTML report gate passed.) -->
<!-- marketing-82 completed 2026-06-24T2308Z → intents/archive/marketing-82.md [projects: virtue; type: implementation; topics: marketing,activation,product] (Virtue 홈 첫 방문 zero-state를 랜딩형으로 재구성해 첫 가치와 다음 행동을 같은 화면에서 바로 읽히게 했다.) -->
<!-- marketing-83 completed 2026-06-24T2300Z → intents/archive/marketing-83.md [projects: virtue; type: strategy; topics: marketing,activation,onboarding,empty-state] (홈 반환형 empty-state gating 정렬 제안서 완료. HTML report gate passed.) -->
<!-- research-23 completed 2026-06-24T2055Z → intents/archive/research-23.md [projects: infinity,research-bank,world-models; type: research; topics: military,workflow,knowledge-management] (미군 TTP 학습 루프 심화 완료. HTML report gate passed.) -->
<!-- marketing-81 completed 2026-06-24T1007Z → intents/archive/marketing-81.md [projects: virtue; type: strategy; topics: marketing,activation,retention] (첫 저장/첫 판단 뒤 홈 복귀 secondary onboarding 감사표 완료. HTML report gate passed.) -->
<!-- research-22 completed 2026-06-24T0800Z → intents/archive/research-22.md (6단계 운영표·도구 비교·현실 루프 완료. HTML report gate passed.) -->
<!-- build-13 completed 2026-06-24T0050Z → intents/archive/build-13.md [projects: afzma,infinity,app-api-verification; type: implementation-verification; topics: hospital-api,api-flow,app-verification] (로컬 shdkej/afzma read-only 검증 완료. HTML report gate passed.) -->
<!-- marketing-80 completed 2026-06-23T2207Z → intents/archive/marketing-80.md [projects: virtue; type: strategy; topics: marketing,activation,product,feedback-consistency] (홈 요약 카드·`최근 덕행`·`/add` 결과·저장 후 복귀 지점을 J1-J4 기준으로 감사표로 정리. HTML report gate passed.) -->
<!-- marketing-79 completed 2026-06-23T1000Z → intents/archive/marketing-79.md [projects: virtue; type: strategy; topics: marketing,activation,prelaunch] (첫 10명 활성화 1장 관찰표 초안 완성. HTML report gate passed.) -->
<!-- marketing-78 completed 2026-06-22T1700Z → intents/archive/marketing-78.md [projects: virtue; type: strategy; topics: marketing,activation,product] (홈 `최근 덕행` empty state 3요소 비교 완료. HTML report gate passed.) -->
<!-- marketing-77 completed 2026-06-22T1431Z → intents/archive/marketing-77.md [projects: virtue; type: strategy; topics: marketing,activation,product,ui-copy] (`/add` 기대 브리지 1줄 + 결과 카드 footer 안내 1줄 구현 완료.) -->
<!-- marketing-76 completed 2026-06-22T1029Z → intents/archive/marketing-76.md [projects: virtue; type: strategy; topics: marketing,activation,product,in-app-guidance] (`/add`·결과 카드·홈 empty state 맥락형 안내 감사표 완료. HTML report gate passed.) -->
<!-- marketing-75 completed 2026-06-22T1029Z → intents/archive/marketing-75.md [projects: virtue; type: strategy; topics: marketing,activation,launch-communication,product] (Tier 1-4 변경 등급표와 권장 안내 표면 맵 완료. HTML report gate passed.) -->
<!-- marketing-74 completed 2026-06-22T0600Z → intents/archive/marketing-74.md [projects: virtue; type: strategy; topics: marketing,activation,product,onboarding] (/add 입력 전 기대 형성 3안 비교 완료. HTML report gate passed.) -->
<!-- research-20 completed 2026-06-21T1200Z → intents/archive/research-20.md (강의/교육 퍼널 제외 국내 1인 브랜드 10선 재조사 완료. HTML report gate passed.) -->
<!-- research-19 completed 2026-06-21T0720Z → intents/archive/research-19.md (드로우앤드류·자청 제외 국내 1인 브랜드 10선 분석 완료. HTML report gate passed.) -->
<!-- marketing-73 completed 2026-06-21T0700Z → intents/archive/marketing-73.md [projects: virtue; type: strategy; topics: marketing,activation,product] (J3 AI 브리지 3안 비교 완료. HTML report gate passed.) -->
<!-- marketing-72 completed 2026-06-20T2218Z → intents/archive/marketing-72.md [display: Virtue First-Session Intent Hint Compare; projects: virtue; type: strategy; topics: activation,marketing,product] (HTML report gate passed.) -->
<!-- research-18 completed 2026-06-20T1200Z → intents/archive/research-18.md [display: 자동화 시스템 신뢰성 강화 리서치; projects: infinity,research-bank,personal-ops; type: research; topics: automation,reliability,operations] (HTML report gate passed.) -->
<!-- marketing-71 completed 2026-06-20T1108Z → intents/archive/marketing-71.md [display: Virtue Seeded Proof Proposal Compare; projects: virtue; type: strategy; topics: activation,onboarding,proof,prelaunch] (HTML report gate passed.) -->
<!-- research-17 completed 2026-06-20T0700Z → intents/archive/research-17.md [display: 미군 연구 시스템 구조 리서치; projects: infinity,research-bank,world-models; type: research; topics: military,research-system,innovation,doctrine,training] (HTML report gate passed.) -->
<!-- marketing-70 completed 2026-06-19T22:07Z → intents/archive/marketing-70.md [display: Virtue Empty-State Proof Audit; projects: virtue; type: strategy; topics: activation,empty-state,marketing] (HTML report gate passed.) -->
<!-- marketing-69 completed 2026-06-19T10:07Z → intents/archive/marketing-69.md [display: Virtue Agent Readiness Baseline; projects: virtue; type: strategy; topics: ai-agents,agentic-web,discoverability,trust,prelaunch] (HTML report gate passed.) -->
<!-- marketing-68 completed 2026-06-19T0000Z → intents/archive/marketing-68.md [display: Virtue Agent-Readable Surface Audit; projects: virtue; type: strategy; topics: ai-agents,agentic-web,trust,discoverability,prelaunch] (HTML report gate passed.) -->
<!-- marketing-67 completed 2026-06-18T12:07Z → intents/archive/marketing-67.md [display: Virtue AI Authorization Boundary Table; projects: virtue; type: strategy; topics: ai-agents,trust,authorization,prelaunch] (HTML report gate 통과.) -->
<!-- build-12 completed 2026-06-18T11:57Z → intents/archive/build-12.md [projects: personal-ops,infinity,design-system; type: implementation; topics: 3d-background,interactive-character,skill] (Option D pre-rendered+CSS parallax 구현 완료.) -->
<!-- research-16 completed 2026-06-18T08:00Z → intents/archive/research-16.md (SAM YouTube parse 기반 CharacterStage 구현 옵션 재비교 완료.) -->
<!-- research-15 completed 2026-06-18T07:00Z → intents/archive/research-15.md [display: 3D Interactive Character Background Feasibility; projects: personal-ops,infinity,design-system; type: research; topics: 3d-background,interactive-character,threejs,design-system] -->
<!-- marketing-66 completed 2026-06-17T22:07Z → intents/archive/marketing-66.md [display: Virtue Agentic Context Map; projects: virtue; type: strategy; topics: agentic-plg,positioning,activation,prelaunch] -->
<!-- marketing-65 completed 2026-06-17T10:24Z → intents/archive/marketing-65.md [display: Virtue Agent Trust Evidence Inventory; projects: virtue; type: strategy] -->
<!-- marketing-64 completed 2026-06-17T01:18Z → intents/archive/marketing-64.md [display: Virtue Early Behavior Intent Sequence Columns; projects: virtue; type: strategy] -->
<!-- build-11 completed 2026-06-16T21:56Z → intents/archive/build-11.md [display: Status 3D Full-Image Floating Menu Redesign; projects: infinity,personal-ops,infrastructure; type: implementation; topics: status,dashboard,ui,3d-background,floating-menu; completion: user-confirmed] -->
