# Intent Registry

> Heartbeat Agent가 주기적으로 읽고 실행하는 의도 목록.

## Inbox


## Active

### marketing-43: Virtue 첫 주 재초대 경계표
- status: active
- priority: medium
- permission: L1 (docs-only); L2 agent-approved for push
- mode: prepare→execute_local
- project: virtue
- goal: D1/D3/D7 미방문을 onboarding 실패·업그레이드 수요·관심 없음으로 성급히 단정하는 오독을 방지하고, 잡별 first value 이후 value recall 후보로 분류하는 내부 재초대 경계표 작성
- context: /home/ubuntu/dev/virtue-rebirth-app/apps/web/docs/ | marketing-42 세션 가치 판독표 계승 | source note: /home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-06-first-week-reactivation.md (로컬 부재 가능)
- success_criteria: J1/J2/J3/J4별 first value, missed second value 분류 기준, 돌아올 이유 후보, 보내면 안 되는 조건, availability/synthetic 제외, 승인 필요선을 한 표로 고정; 기존 이벤트만 인용; 신규 이벤트·속성·카피배포·대시보드·코드·외부발송·비용 변경 0; first 10명 또는 first 7일에는 rate/% 결론 없이 분류 가능성만 확인
- created_at: 2026-06-06T22:00Z
- source: Inbox 구조화 (2026-06-06T22:00Z candidate)


## Waiting

<!-- 사용자 결정, 외부 조건, 안전 확인 대기. 같은 질문을 반복하지 않고 상태만 보존한다. -->

## Archive

<!-- marketing-42 completed 2026-06-06T10:07Z → reports/marketing-42/2026-06-06T1007Z-local.html [projects: virtue; type: strategy; topics: ai-product,activation,retention,measurement] (Virtue 세션당 가치 판독표 작성 완료. 산출물은 virtue-rebirth-app `7e364a6`의 `apps/web/docs/value-per-session-reading-table.md`(신규 1파일, docs-only). Mixpanel 2026 AI/product analytics 렌즈를 Virtue prelaunch 기준으로 번역해, 세션 가치를 이벤트/클릭 수가 아니라 잡별 first value 도달 + 종료 성격으로 읽도록 성공/정상/보류/마찰 판독표를 고정. 핵심: 짧은 무저장 세션은 J3에선 `deed_judged` 도달 성공·정상 종료일 수 있지만 J1/J2/J4에선 저장 전 보류이며, 반복 `deed_rerolled`는 다의적 보류, `deed_save_capped`는 availability/friction 마찰, first value 없는 다이벤트 세션은 engagement가 아니라 보류/마찰로 분리한다. first value 매핑 J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106 재정의 0, m31 막힘 4분류·m37 retention 대조·m41 PQL 경계 위임. First verification gate PASS: 첫 10명 또는 첫 7일에는 세션 분류 가능성만 보고 세션 품질 점수·임계값·activation rate·전환율·PQL·가격 해석을 산출하지 않음. 신규 이벤트·속성·카피·tracking/privacy·dashboard·session replay·코드·배포·외부발송·비용·권한 변경 0, code diff 0, conflict marker 0, source note path 인용(로컬 부재 명시), 이벤트 앵커 72/78/106/135/149/167/183/199 drift 0. HTML 보고서 `<html`/`<body`/axis ax1/axis ax2/`<details` 포함 확인 + details에 계승한 기준·이번에 새로 배운 것·다음 Marketer 규칙·승격 후보 포함. MARKETING_LEARNINGS.md에 durable learning "Session Value Is Read By Job, Not Event Count" 승격. Infinity dirty 무관 파일(EVALUATION_NOTES.md) staging 제외. L2 agent-approved push.) -->

<!-- marketing-41 completed 2026-06-05T23:07Z → reports/marketing-41/2026-06-05T2307Z-local.html [projects: virtue; type: strategy; topics: plg,activation,monetization] (Virtue post-launch PQL/upgrade 신호 경계표 작성 완료. 산출물은 virtue-rebirth-app `fcd319a`의 `apps/web/docs/post-launch-pql-upgrade-signal-boundary-table.md`(신규 1파일, docs-only). Mixpanel PLG 2026/PQL 렌즈를 Virtue prelaunch 기준으로 번역해, PQL/upgrade-readiness를 activation(② first value)이 아니라 그 다음 층(③ 반복+재방문 묶음)으로 분리하고 출시 후 신호를 (A) PQL 후보(대조 대상·결론 아님) / (B) 비후보·가짜 PQL(단일 이벤트·availability·정상 종료·다의적 단발) / (C) Waiting·approval-needed(채점·임계값·가격·신규 tracking·대시보드·공개 카피) 세 칸으로 고정. 핵심: 단일 이벤트 특히 `deed_save_capped` 1회를 "더 원해서 막혔다=업그레이드 수요"로 읽는 것이 1번 오독이며 availability/friction으로 분류·보존한다. A1~A4 activation 후보 묶음(m33)과 prelaunch-monetization-boundary(m28) `deed_save_capped` 오독 금지를 계승, retention 대조 방법은 m37 위임. first value 매핑 J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106 재정의 0(A3는 저장 없이 반복 `deed_judged`로 후보). First verification gate PASS: 문서가 PQL 임계값·conversion rate·upgrade demand를 산출하지 않고 "출시 후 첫 10명 또는 첫 7일 대조 후보"로만 남김(모든 임계값/% 언급은 §7 금지 문장). 이전 partial run(2207Z, Claude timeout)의 잔류 tool-artifact 줄(`</content>`·`</invoke>`) 제거 후 검증. 신규 이벤트·속성·카피·tracking/privacy·pricing·대시보드·세션리플레이·코드·배포·외부발송·비용·권한 변경 0, 이벤트 앵커 72/78/106/135/149/167/183/199 drift 0, 코드 diff 0, conflict marker 0. HTML 보고서 `<html`/`<body`/axis ax1/axis ax2/`<details` 포함 확인 + details에 계승한 기준·이번에 새로 배운 것·다음 Marketer 규칙·승격 후보 포함. MARKETING_LEARNINGS.md에 durable learning "PQL Is A Bundle, Not A Single Event" 승격. Infinity dirty 무관 파일(EVALUATION_NOTES.md) staging 제외. L2 agent-approved push.) -->

<!-- marketing-40 completed 2026-06-05T10:07Z → reports/marketing-40/2026-06-05T1007Z-local.html [projects: virtue; type: strategy; topics: onboarding,activation,friction] (Virtue 막힘 지점 넛지 경계표 작성 완료. 산출물은 virtue-rebirth-app `d1cac9b`의 `apps/web/docs/stuck-point-nudge-boundary-table.md`(신규 1파일, docs-only). Amplitude/Lenny behavior-triggered guidance 렌즈를 Virtue prelaunch의 기존 이벤트 조합 trigger 표로 번역해 T1~T6별 도움 후보, 띄우지 말아야 할 경우, 수기 관찰 질문, prelaunch 금지선을 고정. 핵심: 넛지의 단위는 표면이 아니라 event trigger이며 기본값은 "아무것도 띄우지 않음"; B-LOST에서만 후보가 되고 B-AVAIL/B-NORMAL/B-MISMATCH/first value 도달 경로 위에는 띄우지 않는다. J1/J2/J4=`deed_saved`, J3=`deed_judged` first value 매핑과 `deed_save_capped`=availability/friction 경계 계승. 신규 이벤트·속성·카피·tracking/privacy·PostHog dashboard·코드·배포·공개발송·비용·권한 변경 0. HTML 보고서 `<html`/`<body`/axis ax1/axis ax2/`<details` 포함 확인 + details에 계승한 기준·이번에 새로 배운 것·다음 Marketer 규칙·승격 후보 포함. MARKETING_LEARNINGS.md에 durable learning "Nudges Are Event-Triggered, And Show-Nothing Is The Default" 승격. Infinity dirty 무관 파일(EVALUATION_NOTES.md) staging 제외. L2 agent-approved push.) -->

<!-- marketing-39 completed 2026-06-04T23:08Z → reports/marketing-39/2026-06-04T2207Z-local.html [projects: virtue; type: strategy; topics: ai-trust,activation,onboarding] (Virtue Human-AI readiness trace map 작성 완료. 산출물은 virtue-rebirth-app `4ebf2a5`의 `apps/web/docs/human-ai-readiness-trace-map.md`(신규 1파일, docs-only). arXiv "From Accuracy to Readiness"와 Userpilot U-C-I 렌즈를 첫 10명 관찰 기준으로 번역해 outcome/reliance/safety/learning 4축과 U-C-I 질문을 J1~J4 first value 뒤 행동 흔적으로 매핑. 핵심 경계: `deed_saved`는 AI 판정 동의가 아니고, J3 judged-without-save는 정상 종료 가능하며, `deed_rerolled`는 불신만이 아니라 호기심/학습 행동일 수 있다. 신규 이벤트·속성·카피·tracking/privacy·PostHog dashboard·코드·배포·외부발송·비용·권한 변경 0. HTML 보고서 `<html`/`<body`/axis ax1/axis ax2/`<details` 포함 확인. MARKETING_LEARNINGS.md에 durable learning "Readiness Trace Over Accuracy" 승격. Infinity dirty 무관 파일(EVALUATION_NOTES.md) staging 제외. L2 agent-approved push.) -->

<!-- marketing-38 completed 2026-06-04T10:27Z → reports/marketing-38/2026-06-04T1007Z-local.html [projects: virtue; type: strategy; topics: ai-trust,activation,onboarding,prelaunch] (Virtue AI 판정 신뢰/제어권 관찰 경계표 작성 완료. 산출물은 virtue-rebirth-app의 `apps/web/docs/ai-judgment-trust-control-observation-boundary-table.md`(신규 1파일, docs-only). EY·McKinsey 2026 AI trust 렌즈를 J1~J4 첫 세션 관찰 기준으로 번역해, AI 판정을 "믿어라"가 아니라 "근거를 보고 사람이 마지막 선택을 한다"로 읽는 경계를 고정. J1/J2/J4=`deed_saved`, J3=`deed_judged` first value 매핑과 m24 trust calibration/60초 관찰 기준 계승. 기존 이벤트만 인용했고 신규 이벤트·속성·카피·tracking/privacy·dashboard·배포·외부발송·비용·권한 변경 0. HTML 보고서 `<html`/`<body`/axis ax1/axis ax2/`<details` 포함 확인. MARKETING_LEARNINGS.md에 durable learning "Trust Is Read Through Control, Not Agreement" 승격. Infinity dirty 무관 파일(EVALUATION_NOTES.md) staging 제외. Heartbeat가 partial timeout 후 산출물과 Archive 전환을 검증해 정리.) -->

<!-- research-11 completed 2026-06-04T00:27Z → intents/archive/research-11.md [projects: personal-brand,content-strategy,research-bank; type: research; topics: content,marketing,product] (1인 브랜드 전략 10개 실사례 조사 완료. 산출물은 artifacts/research-11/solo-brand-strategy-10-cases.md, HTML 보고서는 reports/research-11/2026-06-04T0007Z.html. 국내 3·해외 7 사례를 포지셔닝·반복 콘텐츠 폼·신뢰 자산·수익화/제품화 경로·사용자 적용 전략으로 정리. 핵심 패턴: 콘텐츠는 입구, 제품/교육/서비스가 본체, 같은 경험을 영상·글·코스·제품으로 변환해 재사용한다. 사용자 3축 적용은 유튜브=도달, 여행 중 앱 만들기=증거, AI 미니 워크샵=수익화/교육으로 한 깔때기를 만드는 방향. Levels·Danny Postma는 여행+AI/앱+공개빌딩 축과 가장 직접적으로 맞닿은 사례. 공개 발송·외부 제출·유료 도구·사용자 계정 액션·브랜드명/카피 확정 0. 코드·배포·외부 호출 변경 0. HTML 보고서 gate(`<html`, `<body`, `axis ax1`, `axis ax2`, `<details`) 통과. Claude fallback timeout 뒤 heartbeat가 관련 draft를 검증하고 Active→Archive 정리.) -->

<!-- marketing-37 completed 2026-06-03T22:07Z → reports/marketing-37/2026-06-03T2207Z-local.html [projects: virtue; type: strategy; topics: activation,retention,analytics] (Virtue activation-retention correlation readiness spec 작성 완료. 산출물은 virtue-rebirth-app `b5c0d2e`의 `apps/web/docs/activation-retention-correlation-readiness.md`(신규 1파일, docs-only). 핵심: m33의 A1~A4 activation 후보 묶음과 W-IMM/W-CONF window를 재정의하지 않고, 출시 후 retention 대조에 필요한 D7 우선/D30 보류 질문, X-MOCK/X-SYNTH/X-SELF/X-CAP/X-503 제외 조건, 읽기 전용 pseudo-query shape, prelaunch 금지선을 사전 등록. first value 매핑 J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106 계승, A3 미완료 정의는 `deed_judged` 부재로 고정해 judged−saved 갭을 이탈/묶음 미완료로 환산 금지. 신규 이벤트·속성·코드·카피·PostHog 설정·대시보드·tracking/privacy·배포·외부발송·비용·권한 변경 0. HTML 보고서 `<html`/`<body`/axis ax1/axis ax2/`<details` 포함 확인 + details에 계승한 기준·이번에 새로 배운 것·다음 Marketer 규칙·승격 후보 포함. MARKETING_LEARNINGS.md에 durable learning "Correlation Readiness Is A Separate Gate" 승격. Infinity dirty 무관 파일(EVALUATION_NOTES.md) staging 제외. L2 agent-approved push.) -->

<!-- marketing-36 completed 2026-06-03T10:07Z → reports/marketing-36/2026-06-03T1007Z-local.html [projects: virtue; type: strategy; topics: ai-agent,activation,measurement,prelaunch] (Virtue prelaunch 분석 Skill Sheet 작성 완료.) -->

<!-- marketing-35 completed 2026-06-02T23:07Z → reports/marketing-35/2026-06-02T2207Z-local.html [projects: virtue; type: strategy; topics: onboarding,activation,checklist] (Virtue 잡별 온보딩 체크리스트 감사표 작성 완료.) -->

<!-- marketing-34 completed 2026-06-02T11:07Z → reports/marketing-34/2026-06-02T1007Z-local.html [projects: virtue; type: strategy; topics: plg,activation,measurement] (Virtue PLG Foundation exit gate 문서 작성 완료.) -->

<!-- marketing-33 completed 2026-06-01T22:07Z → reports/marketing-33/2026-06-01T2207Z-local.html [projects: virtue; type: strategy; topics: activation,measurement,retention,prelaunch] (Virtue 활성화 후보 등록부 작성 완료.) -->

<!-- marketing-32 completed 2026-06-01T10:07Z → reports/marketing-32/2026-06-01T1007Z-local.html [projects: virtue; type: strategy; topics: onboarding,activation,ai-product,prelaunch] (Virtue 첫 입력 기본값/예시/placeholder 감사표 작성 완료.) -->

<!-- marketing-31 completed 2026-05-31T23:07Z → reports/marketing-31/2026-05-31T2307Z-local.html [projects: virtue; type: strategy; topics: onboarding,activation,jtbd,prelaunch] (Virtue 첫 세션 제품 본체/범퍼 경계표 작성 완료.) -->

<!-- marketing-30 completed 2026-05-31T10:07Z → reports/marketing-30/2026-05-31T1007Z-local.html (Virtue 첫 결과 공유성 판독 기준 작성 완료.) -->

<!-- marketing-29 completed 2026-05-30T22:07Z → reports/marketing-29/2026-05-30T2207Z-local.html (Virtue AI outcome proxy 사전 작성 완료.) -->

<!-- marketing-28 completed 2026-05-30T10:07Z → reports/marketing-28/2026-05-30T1007Z-local.html (Virtue prelaunch 유료화 경계 브리프 작성 완료.) -->

<!-- marketing-27 completed 2026-05-29T22:25Z → reports/marketing-27/2026-05-29T2225Z-local.md (Virtue 첫 사용자 메시지 혼란 로그 작성 완료.) -->

<!-- marketing-26 completed 2026-05-29T11:07Z → intents/archive/marketing-26.md (Virtue recovery-over-streak 리텐션 렌즈 작성 완료.) -->

<!-- marketing-25 completed 2026-05-28T22:07Z → intents/archive/marketing-25.md (Virtue human/test/agent 트래픽 판독 경계표 작성 완료.) -->

<!-- marketing-24 completed 2026-05-28T10:07Z → intents/archive/marketing-24.md (Virtue AI 판정 신뢰 보정 감사표 작성 완료.) -->

<!-- research-10 completed 2026-05-28T16:07Z → intents/archive/research-10.md (PC·인터넷 시대 전환사 리서치 완료.) -->

<!-- marketing-23 completed 2026-05-27T22:07Z → intents/archive/marketing-23.md (Virtue 온보딩 지표 운영 판독표 작성 완료.) -->

<!-- marketing-22 completed 2026-05-27T10:07Z → intents/archive/marketing-22.md (Virtue 리텐션 예측 활성화 브리프 작성 완료.) -->

<!-- marketing-21 completed 2026-05-26T22:07Z → intents/archive/marketing-21.md (Virtue `/add` 입력-결과 균형 감사표 작성 완료.) -->

<!-- marketing-20 completed 2026-05-26T15:07Z → intents/archive/marketing-20.md (Virtue 첫 60초 가치 관찰 스크립트 작성 완료.) -->

<!-- marketing-19 completed 2026-05-26T10:07Z → intents/archive/marketing-19.md (Virtue 신규 사용자 홈 화면 FAE 감사표 작성 완료.) -->

<!-- marketing-18 completed 2026-05-26T00:07Z → intents/archive/marketing-18.md (Virtue AEO / Agent-ready 공개 표면 감사표 작성 완료.) -->

<!-- marketing-17 completed 2026-05-25T22:07Z → intents/archive/marketing-17.md (Virtue 첫 세션 정성 마찰 관찰 프로토콜 작성 완료.) -->

<!-- research-09 completed 2026-05-25T12:30Z → intents/archive/research-09.md (1인기업 강점 살리기 vs 한계 조기 규정 리서치.) -->

<!-- marketing-16 completed 2026-05-25T10:07Z → intents/archive/marketing-16.md (Virtue 첫 세션 3-스크린 가치 경로 감사표 작성 완료.) -->

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

<!-- marketing-02 completed 2026-05-16T14:00Z → intents/archive/marketing-02.md (마찰점 4개 특정, 개선 후보 3개 초안 작성 완료.) -->

<!-- research-07 completed 2026-05-13T12:00 → intents/archive/research-07.md -->

<!-- product-01 completed 2026-05-15T11:44Z → intents/archive/product-01.md (Virtue 최신 상태, 후속 개선은 별도 Intent로 분리) -->

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
