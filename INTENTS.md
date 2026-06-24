# Intent Registry

> Heartbeat Agent가 주기적으로 읽고 실행하는 의도 목록.

## Inbox

- `marketing-81` Virtue 첫 저장 후 홈 복귀 secondary onboarding 감사표
  source note path: `/home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-24-secondary-onboarding-return-path.md`
  rationale: prelaunch 단계에서 첫 가치 전 onboarding 감사는 많이 쌓였지만, 첫 저장/첫 판단 뒤 홈 복귀 시점의 다음 행동 브리지는 아직 비어 있다. 현재 홈은 첫 기록 전 약속은 선명하지만 반환 사용자에게는 다시 처음 사용자 같은 empty-state와 CTA를 보여 줄 수 있다.
  expected impact: 첫 가치 이후 activation depth 해석 충돌을 줄이고, J1/J2/J4/J3별로 가장 안전한 second-step 문장 후보를 docs-only로 정리할 수 있다.
  permission level: L1 docs-only
  owner route: Infinity router -> Claude Code docs-only
  success criteria: 홈의 기존 표면만 대상으로 `현재 문장 / 사용자 상태 / 다음 행동 브리지 / 잡별 오독 위험 / 추천안`을 한 표로 정리하고, 신규 이벤트·tracking/privacy·배포·외부 발송 없이 J1/J2/J4와 J3의 second-step 차이를 분리한다.
  first verification gate: source note 존재 확인, 기존 marketing-43/70/79/80 및 J1-J4 first value 계약과 충돌 0, conflict marker 0, production code 변경 0.

## Active

## Waiting

<!-- 사용자 결정, 외부 조건, 안전 확인 대기. 같은 질문을 반복하지 않고 상태만 보존한다. -->

<!-- naver-shopping-01 waiting 2026-06-21T1000Z → intents/active/naver-shopping-01.md [display: 나래/Narae; projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,marketing; status: sample-order-gated-session-waiting; approval: sample-order-gated] (cloud 소싱 준비 완료(크로스바디+손목 스트랩). alibaba.com 로컬 공급사 확인(계정 불필요) + 손목·크로스바디 병행 샘플 주문 사용자 승인 대기. do_not_repeat_cloud 활성.) -->

## Archive
<!-- build-13 completed 2026-06-24T0050Z → intents/archive/build-13.md [projects: afzma,infinity,app-api-verification; type: implementation-verification; topics: hospital-api,api-flow,app-verification] (로컬 shdkej/afzma read-only 검증 완료. UI→/api/chat·/api/history→controller→MedicalService→HIRA 병원 API 경로는 코드상 연결됨. HIRA_API_KEY 없음/오류/빈 응답 시 mock 병원 폴백. 실제 HIRA 네트워크 호출은 키·외부 API 경계 때문에 미실행. Claude Code는 401 인증 오류로 차단되어 SAM이 로컬 검증 수행. HTML report gate passed.) -->
<!-- research-22 completed 2026-06-24T0800Z → intents/archive/research-22.md (6단계 운영표·도구 비교·현실 루프 완료. 소스 코퍼스 사전 정의+최소 정보 단위(URL·날짜·판단메모) 유지가 핵심. HTML report gate passed.) -->
<!-- marketing-80 completed 2026-06-23T2207Z → intents/archive/marketing-80.md [projects: virtue; type: strategy; topics: marketing,activation,product,feedback-consistency] (홈 요약 카드·`최근 덕행`·`/add` 결과·저장 후 복귀 지점을 J1-J4 기준으로 감사표로 정리. 결론은 요약 신호와 `아직 비어있어요` empty-state 공존이 첫 저장 이후 신뢰를 깎을 수 있으며, safest next step은 홈 empty-state gating 정렬. production/tracking/privacy/public message/code deploy/external cost 변경 0. HTML report gate passed.) -->
<!-- research-21 completed 2026-06-23T1500Z → intents/archive/research-21.md (6인 비교표 완성. 작은단위기록→주제별조립→구조모순검증→편집변환 공통패턴 도출. 매일3줄→주간분류→월간조립 기록루프 제안. HTML report gate passed.) -->
<!-- marketing-79 completed 2026-06-23T1000Z → intents/archive/marketing-79.md [projects: virtue; type: strategy; topics: marketing,activation,prelaunch] (첫 10명 활성화 1장 관찰표 초안 완성. 홈진입·/add·deed_judged·deed_saved·D1 재방문 5체크포인트 포함. J1/J2/J4=deed_saved·J3=deed_judged 기존 정의 충돌 0. HTML report gate passed.) -->
<!-- marketing-78 completed 2026-06-22T1700Z → intents/archive/marketing-78.md [projects: virtue; type: strategy; topics: marketing,activation,product] (홈 `최근 덕행` empty state 3요소 비교 완료. ghost sample card 1장(Option B)이 결과 예시 가시성 갭 해소 최우선 추천안. 한 줄 보조문구(Option A)가 보수적 차선. 구현은 approval-needed. 기존 archive 충돌 0. HTML report gate passed.) -->
<!-- marketing-77 completed 2026-06-22T1431Z → intents/archive/marketing-77.md [projects: virtue; type: strategy; topics: marketing,activation,product,ui-copy] (`/add` 기대 브리지 1줄 + 결과 카드 footer 안내 1줄 구현 완료. diff는 apps/web/src/app/add/page.tsx 한 파일에 제한. typecheck 통과, lint는 기존 경고 4건만 보고. tracking/privacy/external/cost/credential/deploy 변경 0.) -->
<!-- marketing-76 completed 2026-06-22T1029Z → intents/archive/marketing-76.md [projects: virtue; type: strategy; topics: marketing,activation,product,in-app-guidance] (`/add`·결과 카드·홈 empty state 맥락형 안내 감사표 완료. Gate yes/no 판정은 `/add` Yes, 결과 카드 Yes, 홈 empty state No. production/tracking/privacy/public copy/deploy/external message/cost 변경 0. HTML report gate passed.) -->
<!-- marketing-75 completed 2026-06-22T1029Z → intents/archive/marketing-75.md [projects: virtue; type: strategy; topics: marketing,activation,launch-communication,product] (Tier 1-4 변경 등급표와 권장 안내 표면 맵 완료. `/add`·결과 카드·홈 empty state를 각각 Tier 3/3/2로 분류하고 marketing-71/73/74 연결 예시 3개 정리. production/tracking/privacy/public copy/deploy/external message/cost 변경 0. HTML report gate passed.) -->
<!-- marketing-74 completed 2026-06-22T0600Z → intents/archive/marketing-74.md [projects: virtue; type: strategy; topics: marketing,activation,product,onboarding] (/add 입력 전 기대 형성 3안 비교 완료. Option B(sample 결과 1줄)가 J3 hesitation 해소 최우선 추천안. J4 경계 문구는 결과 카드 footer 배치 권고. 구현은 approval-needed. HTML report gate passed.) -->
<!-- research-20 completed 2026-06-21T1200Z → intents/archive/research-20.md (강의/교육 퍼널 제외 국내 1인 브랜드 10선 재조사 완료. 취향·미감·공간·독립출판 기반 경로 다양성 입증. 10개 모두 강의 핵심 수익 아님. HTML report gate passed.) -->
<!-- marketing-73 completed 2026-06-21T0700Z → intents/archive/marketing-73.md [projects: virtue; type: strategy; topics: marketing,activation,product] (J3 AI 브리지 3안 비교 완료. Option C(빈 상태 ghost AI 결과 카드)가 J3 기대 강화 최대·J1/J4 훼손 최소 추천안. Option B(CTA 보조 힌트)가 가장 보수적 차선. 구현은 approval-needed. HTML report gate passed.) -->
<!-- research-19 completed 2026-06-21T0720Z → intents/archive/research-19.md (드로우앤드류·자청 제외 국내 1인 브랜드 10선 분석 완료. 공통 패턴: 무료 콘텐츠→신뢰→유료 교육/커뮤니티/상품 전환 퍼널. 마스터 1순위: 자기 성과 기반 지식 강의 실험. HTML report gate passed.) -->
<!-- research-18 completed 2026-06-20T1200Z → intents/archive/research-18.md [display: 자동화 시스템 신뢰성 강화 리서치; projects: infinity,research-bank,personal-ops; type: research; topics: automation,reliability,operations] (6개 실패 패턴 분류·5개 설계 원칙·3단계 점진적 하드닝 프레임워크 정리. 개인은 관측성+멱등성+수동우회 3단계, 팀/서비스는 Runbook·Circuit Breaker까지 추가. HTML report gate passed.) -->
<!-- marketing-72 completed 2026-06-20T2218Z → intents/archive/marketing-72.md [display: Virtue First-Session Intent Hint Compare; projects: virtue; type: strategy; topics: activation,marketing,product] (L1 docs-only 비교 문서 완료. `가장 먼저 받고 싶은 가치` 질문 프레임을 추천안으로 두고, 한국어 선택지 4개, J1-J4 임시 매핑, 질문 후 hero/CTA/proof surface 분기 원칙을 1개 문서로 정리. production/tracking/privacy/public copy/deploy/external message/cost 변경 0. HTML report gate passed.) -->
<!-- research-17 completed 2026-06-20T0700Z → intents/archive/research-17.md [display: 미군 연구 시스템 구조 리서치; projects: infinity,research-bank,world-models; type: research; topics: military,research-system,innovation,doctrine,training] (미군의 강점은 연구 능력 자체가 아니라 연구→교리→훈련→실전→AAR 피드백 루프의 제도화. DARPA PM 계약직 모델, PME 지속교육, AAR 의무화, 워게임·레드팀 구조 분석. 반례: F-35 조달관료제/IT 레거시/성공편향. 개인 적용 원칙 6개: AAR+TTP변환+실험분리+레드팀+빠른피드백+Mission Command. HTML report gate passed.) -->
<!-- marketing-70 completed 2026-06-19T22:07Z → intents/archive/marketing-70.md [display: Virtue Empty-State Proof Audit; projects: virtue; type: strategy; topics: activation,empty-state,marketing] (라이브 홈 `최근 덕행` empty state를 read-only 캡처해 gap 3개와 J1-J4 seeded proof 감사표를 문서화. 결론은 CTA 부족보다 proof preview 부족이 핵심이며, safest next step은 ghost/sample 구조의 proposal-only 비교안이다. production/tracking/privacy/public copy/deploy/external message 변경 0. HTML report gate passed.) -->
<!-- marketing-71 completed 2026-06-20T1108Z → intents/archive/marketing-71.md [display: Virtue Seeded Proof Proposal Compare; projects: virtue; type: strategy; topics: activation,onboarding,proof,prelaunch] (L1 docs-only 비교 문서 완료. `proof 없음 / 단일 샘플 카드 / 누적 카드 스택` 3안 비교표와 J1-J4 오해 위험, approval-needed 구현 메모를 1개 문서로 정리. 결론은 sample/preview 표식이 있는 누적 카드 스택이 가장 안전한 proposal-only 기본안. production/tracking/privacy/public copy/deploy/external message/cost 변경 0. HTML report gate passed.) -->
<!-- marketing-69 completed 2026-06-19T10:07Z → intents/archive/marketing-69.md [display: Virtue Agent Readiness Baseline; projects: virtue; type: strategy; topics: ai-agents,agentic-web,discoverability,trust,prelaunch] (Virtue public URL read-only baseline completed. HTML report gate passed.) -->
<!-- marketing-68 completed 2026-06-19T0000Z → intents/archive/marketing-68.md [display: Virtue Agent-Readable Surface Audit; projects: virtue; type: strategy; topics: ai-agents,agentic-web,trust,discoverability,prelaunch] (public/repo-readable 4개 표면 × 5축 감사표 완성. L1 docs-only. HTML report gate passed.) -->
<!-- build-12 completed 2026-06-18T11:57Z → intents/archive/build-12.md [projects: personal-ops,infinity,design-system; type: implementation; topics: 3d-background,interactive-character,skill] (Option D pre-rendered+CSS parallax 구현 완료. space@64049a5 배포·라이브 검증.) -->
<!-- marketing-67 completed 2026-06-18T12:07Z → intents/archive/marketing-67.md [display: Virtue AI Authorization Boundary Table; projects: virtue; type: strategy; topics: ai-agents,trust,authorization,prelaunch] (J1-J4별 authorization boundary table 완성. HTML report gate 통과.) -->
<!-- research-16 completed 2026-06-18T08:00Z → intents/archive/research-16.md (SAM YouTube parse 기반 CharacterStage 구현 옵션 재비교 완료.) -->
<!-- research-15 completed 2026-06-18T07:00Z → intents/archive/research-15.md [display: 3D Interactive Character Background Feasibility; projects: personal-ops,infinity,design-system; type: research; topics: 3d-background,interactive-character,threejs,design-system] -->
<!-- marketing-66 completed 2026-06-17T22:07Z → intents/archive/marketing-66.md [display: Virtue Agentic Context Map; projects: virtue; type: strategy; topics: agentic-plg,positioning,activation,prelaunch] -->
<!-- 이 섹션의 상세 이력은 2026-06-17T10:24Z Heartbeat 과정에서 INTENTS.md 갱신 중 일시 유실됨. 개별 intent 원장은 intents/archive/*.md 에 모두 보존되어 있음. -->
<!-- build-11 completed 2026-06-16T21:56Z → intents/archive/build-11.md [display: Status 3D Full-Image Floating Menu Redesign; projects: infinity,personal-ops,infrastructure; type: implementation; topics: status,dashboard,ui,3d-background,floating-menu; completion: user-confirmed] -->
<!-- marketing-64 completed 2026-06-17T01:18Z → intents/archive/marketing-64.md [display: Virtue Early Behavior Intent Sequence Columns; projects: virtue; type: strategy] -->
<!-- marketing-65 completed 2026-06-17T10:24Z → intents/archive/marketing-65.md [display: Virtue Agent Trust Evidence Inventory; projects: virtue; type: strategy] -->
