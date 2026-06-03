# Intent Registry

> Heartbeat Agent가 주기적으로 읽고 실행하는 의도 목록.

## Inbox

## Active

### marketing-36 · Virtue prelaunch 분석 skill sheet 작성
- status: in_progress
- priority: medium
- permission: L1/L2 doc-only
- projects: [virtue]
- goal: 에이전트와 내부 분석자를 위한 Virtue prelaunch 분석 1-page 참조 sheet를 작성한다. J1~J4 first value 매핑, activation 후보 묶음 A1~A4, prelaunch 금지선, synthetic 제외, availability 분리를 한 문서에 통합한다.
- success_criteria: `apps/web/docs/virtue-prelaunch-analysis-skill-sheet.md` 생성, 기존 first value 문서 충돌 0, 신규 이벤트/속성 0, conflict marker 0
- mode: prepare (cloud, 완료) → execute_local (virtue-rebirth-app docs, 대기)
- context: artifacts/marketing-36/virtue-prelaunch-analysis-skill-sheet-draft.md
- prepare_report: reports/marketing-36/2026-06-03T0600Z.html

## Waiting

<!-- 사용자 결정, 외부 조건, 안전 확인 대기. 같은 질문을 반복하지 않고 상태만 보존한다. -->

## Archive

<!-- marketing-35 completed 2026-06-02T23:07Z → reports/marketing-35/2026-06-02T2207Z-local.html [projects: virtue; type: strategy; topics: onboarding,activation,checklist] (Virtue 잡별 온보딩 체크리스트 감사표 작성 완료. 산출물은 virtue-rebirth-app의 `apps/web/docs/onboarding-checklist-audit-table.md`(신규 1파일, commit `a300095`). 핵심: 체크리스트는 first value 위치를 따라 잡별로 길이·종료점이 다르며 J1/J2/J4는 입력→판정→저장, J3는 입력→판정에서 종료하고 저장 강제는 DO-NOT-INCLUDE. 항목을 CL-ELIGIBLE/BUMPER-ONLY/CONTEXTUAL-FALLBACK/DO-NOT-INCLUDE 4분류로 나누고, 폴백은 B-LOST에만 발동하며 B-MISMATCH/B-AVAIL/B-NORMAL에는 발동하지 않도록 경계를 고정. first value 매핑 J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106 및 `deed_save_capped`:167=availability/friction 계승. 신규 이벤트·속성·카피·계측·대시보드·세션리플레이·코드·배포·외부발송·비용·권한 변경 0. HTML 보고서 `<html`/`<body`/axis ax1/axis ax2/`<details` 포함 확인. MARKETING_LEARNINGS.md 승격 후보는 단일 실행이라 report 안에 보류. Infinity dirty 무관 파일(EVALUATION_NOTES.md) staging 제외. L2 agent-approved push.) -->

<!-- marketing-34 completed 2026-06-02T11:07Z → reports/marketing-34/2026-06-02T1007Z-local.html [projects: virtue; type: strategy; topics: plg,activation,measurement] (Virtue PLG Foundation exit gate 문서 작성 완료. 산출물은 virtue-rebirth-app의 `apps/web/docs/plg-foundation-exit-gate.md`(신규 1파일). 핵심: Foundation 종료 조건은 "활성화가 좋다"가 아니라 first value 매핑, 후보 묶음/window, TTV 시작/종료점, D7 질문, baseline 양식, 이벤트 도착 검증, traffic/source+availability 분리까지 측정 가능한 상태인가로 고정. G1~G7 중 G6 도착 검증만 출시 후 확인 대기이며, Activation 진입 판단은 외부 벤치마크 수치가 아니라 데이터 품질·synthetic 제외·가용성 차단·같은 잡 재가치로 분리. first value 매핑 J1/J2/J4=`deed_saved`, J3=`deed_judged`, `deed_save_capped`=availability/friction, synthetic/mock/self-test 비결정 기준 계승. 신규 이벤트·속성·카피·계측·대시보드·코드·배포·외부발송·비용·권한 변경 0. HTML 보고서 `<html`/`<body`/axis ax1/axis ax2/`<details` 포함 확인. MARKETING_LEARNINGS.md에 durable learning "Measurement Readiness Is A Separate Gate" 승격. Infinity dirty 무관 파일(EVALUATION_NOTES.md) staging 제외. L2 agent-approved push.) -->

<!-- marketing-33 completed 2026-06-01T22:07Z → reports/marketing-33/2026-06-01T2207Z-local.html [projects: virtue; type: strategy; topics: activation,measurement,retention,prelaunch] (Virtue 활성화 후보 등록부 작성 완료. 산출물은 virtue-rebirth-app의 `apps/web/docs/activation-candidate-registry.md`(신규 1파일). PostHog 활성화 렌즈를 Virtue J1~J4 잡별 후보 묶음·관찰 window를 출시 전에 동결(register)하는 내부 등록부로 번역. 핵심 가치: 흩어진 재료는 이미 충분하나, 출시 후 작은 데이터로 묶음·window를 사후에 입맛대로 고르는(cherry-pick) 위험을 막기 위해 묶음(A1~A4)과 window(W-IMM 첫 세션/W-CONF D7)를 등록 단위로 고정. first value 매핑 J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106 그대로 계승. L2 agent-approved push.) -->

<!-- marketing-32 completed 2026-06-01T10:07Z → reports/marketing-32/2026-06-01T1007Z-local.html [projects: virtue; type: strategy; topics: onboarding,activation,ai-product,prelaunch] (Virtue 첫 입력 기본값/예시/placeholder 감사표 작성 완료. durable learning "First-Input Defaults Steer The Job"를 MARKETING_LEARNINGS.md에 승격. L2 agent-approved push.) -->

<!-- marketing-31 completed 2026-05-31T23:07Z → reports/marketing-31/2026-05-31T2307Z-local.html [projects: virtue; type: strategy; topics: onboarding,activation,jtbd,prelaunch] (Virtue 첫 세션 제품 본체/범퍼 경계표 작성 완료. durable learning "Product Body vs Bumper By Job"를 MARKETING_LEARNINGS.md에 승격. L2 agent-approved push.) -->

<!-- marketing-30 completed 2026-05-31T10:07Z → reports/marketing-30/2026-05-31T1007Z-local.html [projects: virtue; type: strategy; topics: onboarding,activation,ai-product,prelaunch] (Virtue 첫 결과 공유성 판독 기준 작성 완료. durable learning "Shareworthiness Is A Separate Axis"를 MARKETING_LEARNINGS.md에 승격. L2 agent-approved push.) -->

<!-- marketing-29 completed 2026-05-30T22:07Z → reports/marketing-29/2026-05-30T2207Z-local.html [projects: virtue; type: strategy; topics: ai-product,activation,trust,measurement,prelaunch] (Virtue AI outcome proxy 사전 작성 완료. L2 agent-approved push.) -->

<!-- marketing-28 completed 2026-05-30T10:07Z → reports/marketing-28/2026-05-30T1007Z-local.html [projects: virtue; type: strategy; topics: monetization,pricing,activation,prelaunch] (Virtue prelaunch 유료화 경계 브리프 작성 완료. L2 agent-approved push.) -->

<!-- marketing-27 completed 2026-05-29T22:25Z → reports/marketing-27/2026-05-29T2225Z-local.md [projects: virtue; type: strategy; topics: positioning,messaging,activation,prelaunch] (Virtue 첫 사용자 메시지 혼란 로그 작성 완료. L2 agent-approved push.) -->

<!-- marketing-26 completed 2026-05-29T11:07Z → intents/archive/marketing-26.md [projects: virtue; type: strategy; topics: retention,habit,recovery,copy] (Virtue recovery-over-streak 리텐션 렌즈 작성 완료. L2 agent-approved push.) -->

<!-- marketing-25 completed 2026-05-28T22:07Z → intents/archive/marketing-25.md [projects: virtue; type: strategy; topics: onboarding,analytics,activation,ai-agents] (Virtue human/test/agent 트래픽 판독 경계표 작성 완료. L2 agent-approved push.) -->

<!-- marketing-24 completed 2026-05-28T10:07Z → intents/archive/marketing-24.md [projects: virtue; type: strategy; topics: activation,trust,ai-product,onboarding] (Virtue AI 판정 신뢰 보정 감사표 작성 완료. L2 agent-approved push.) -->

<!-- research-10 completed 2026-05-28T16:07Z → intents/archive/research-10.md [projects: knowledge-lab,infinity; type: research; topics: content,wiki] (PC·인터넷 시대 전환사 리서치 완료.) -->

<!-- marketing-23 completed 2026-05-27T22:07Z → intents/archive/marketing-23.md [projects: virtue; type: strategy; topics: activation,retention,analytics] (Virtue 온보딩 지표 운영 판독표 작성 완료. L2 agent-approved push.) -->

<!-- marketing-22 completed 2026-05-27T10:07Z → intents/archive/marketing-22.md (Virtue 리텐션 예측 활성화 브리프 작성 완료. L2 agent-approved push.) -->

<!-- marketing-21 completed 2026-05-26T22:07Z → intents/archive/marketing-21.md (Virtue `/add` 입력-결과 균형 감사표 작성 완료. L2 agent-approved push.) -->

<!-- marketing-20 completed 2026-05-26T15:07Z → intents/archive/marketing-20.md (Virtue 첫 60초 가치 관찰 스크립트 작성 완료. L2 agent-approved push.) -->

<!-- marketing-19 completed 2026-05-26T10:07Z → intents/archive/marketing-19.md (Virtue 신규 사용자 홈 화면 FAE 감사표 작성 완료. L2 agent-approved push.) -->

<!-- marketing-18 completed 2026-05-26T00:07Z → intents/archive/marketing-18.md (Virtue AEO / Agent-ready 공개 표면 감사표 작성 완료. L2 agent-approved push.) -->

<!-- marketing-17 completed 2026-05-25T22:07Z → intents/archive/marketing-17.md (Virtue 첫 세션 정성 마찰 관찰 프로토콜 작성 완료. L2 agent-approved push.) -->

<!-- research-09 completed 2026-05-25T12:30Z → intents/archive/research-09.md (1인기업 강점 살리기 vs 한계 조기 규정 리서치.) -->

<!-- marketing-16 completed 2026-05-25T10:07Z → intents/archive/marketing-16.md (Virtue 첫 세션 3-스크린 가치 경로 감사표 작성 완료. L2 agent-approved push.) -->

<!-- marketing-15 completed 2026-05-24T22:07Z → intents/archive/marketing-15.md (Virtue 웹/iOS 활성화 이벤트 패리티 브리프 작성 완료.) -->

<!-- marketing-14 completed 2026-05-24T15:56Z → intents/archive/marketing-14.md (Virtue 첫 주 활성화-리텐션 연결표 작성 완료.) -->

<!-- marketing-13 completed 2026-05-23T22:07Z → intents/archive/marketing-13.md (Virtue 경쟁 대안 기반 포지셔닝 브리프 작성 완료.) -->

<!-- marketing-10 completed 2026-05-23T16:07Z → intents/archive/marketing-10.md (Virtue Time-to-Value 관찰 기준표 작성 완료.) -->

<!-- marketing-12 completed 2026-05-23T10:18Z → intents/archive/marketing-12.md (Virtue 활성화 경로 마찰 감사표 작성 완료.) -->

<!-- research-08 completed 2026-05-23T10:30Z → intents/archive/research-08.md (GEO/LLMO 체크리스트 조사 완료.) -->

<!-- marketing-11 completed 2026-05-22T22:17Z → intents/archive/marketing-11.md (Virtue 첫 실사용자 기준선 템플릿 작성 완료.) -->

<!-- marketing-09 completed 2026-05-21T22:07Z → intents/archive/marketing-09.md (Virtue 활성화 마일스톤 사다리 작성 완료.) -->

<!-- marketing-01 completed 2026-05-21T10:17Z → intents/archive/marketing-01.md (Virtue add-flow telemetry 승인 처리 완료.) -->

<!-- marketing-08 completed 2026-05-21T10:07Z → intents/archive/marketing-08.md (Virtue PMF 응답 분석 루브릭 작성 완료.) -->

<!-- marketing-07 completed 2026-05-20T22:07Z → intents/archive/marketing-07.md (Virtue 최소 생존 오디언스 기준표 작성 완료.) -->

<!-- marketing-06 completed 2026-05-20T10:07Z → intents/archive/marketing-06.md (Virtue 첫 세션 JTBD 매트릭스 작성 완료.) -->

<!-- marketing-05 completed 2026-05-19T22:07Z → intents/archive/marketing-05.md (Virtue 빈 상태/첫 행동 감사표 작성 완료.) -->

<!-- marketing-04 completed 2026-05-19T10:07Z → intents/archive/marketing-04.md (Virtue 첫인상 포지셔닝 스냅샷 작성 완료.) -->

<!-- marketing-03 completed 2026-05-18T22:20Z → intents/archive/marketing-03.md (Virtue 첫 7일 deed_saved 루프 정의서 작성 완료.) -->

<!-- marketing-02 completed 2026-05-16T14:00Z → intents/archive/marketing-02.md (마찰점 4개 특정, 개선 후보 3개 초안 완료.) -->

<!-- research-07 completed 2026-05-13T12:00 → intents/archive/research-07.md -->

<!-- product-01 completed 2026-05-15T11:44Z → intents/archive/product-01.md (Virtue 최신 상태 확인 완료.) -->

<!-- build-02 completed 2026-05-13 → intents/archive/build-02.md (https://infinity.oracle.shdkej.com 배포 완료) -->

<!-- research-06 completed 2026-05-05T08:00 → intents/archive/research-06.md -->

<!-- wiki-05 completed 2026-04-25T09:00 → intents/archive/wiki-05.md -->

<!-- wiki-04 completed 2026-04-25T10:15 → intents/archive/wiki-04.md -->

<!-- wiki-02 completed 2026-04-19T02:45 → intents/archive/wiki-02.md -->
<!-- wiki-03 completed 2026-04-20T13:30 → intents/archive/wiki-03.md -->
<!-- research-05 completed 2026-04-21T00:00 → intents/archive/research-05.md -->
<!-- wiki-01 completed 2026-04-21T00:00 → intents/archive/wiki-01.md -->
<!-- build-01 completed 2026-04-21T00:30 → intents/archive/build-01.md -->
<!-- research-05 re-run completed 2026-04-23T10:00 → intents/archive/research-05.md (3차) -->
