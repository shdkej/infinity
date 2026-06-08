# Intent Registry

> Heartbeat Agent가 주기적으로 읽고 실행하는 의도 목록.

## Inbox

## Active


## Waiting

<!-- 사용자 결정, 외부 조건, 안전 확인 대기. 같은 질문을 반복하지 않고 상태만 보존한다. -->

<!-- naver-shopping-01 waiting 2026-06-07T23:28Z → intents/active/naver-shopping-01.md [projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,marketing; decision: 네이버/스마트스토어 읽기 전용 브라우저 세션을 써도 될까요?; options: 허용 | 보류; default: 보류; reason: 실계정 대시보드와 네이버쇼핑 검색을 확인해야 경쟁상품/지표 검증이 정확해집니다.; next: 허용하면 로그인된 브라우저로 읽기 전용 확인만 진행] (네이버/스마트스토어 읽기 전용 접근 여부) -->

## Archive

<!-- marketing-46 completed 2026-06-08T1000Z → reports/marketing-46/2026-06-08T1000Z.html [projects: virtue; type: strategy; topics: agent-led-growth,ai-product,distribution,prelaunch] (Virtue agent-led growth fit/no-fit 경계표 작성 완료. 산출물 artifacts/marketing-46/agent-led-growth-boundary-table.md(신규 1파일, docs-only). agent-led growth를 Virtue prelaunch 기준으로 번역해 fit/no-fit/나중에/금지 4범주 경계표 고정. passive 발견(llms.txt·OG·AEO docs)=fit, API/MCP/에이전트배치/과금=no-fit now. 인간 first value 50+명 검증 후 재검토 gate 정의. 기존 m38 No Autonomous Action Bounds The Trust Question·m45 Decision-Delegation Risk Rides The Verb·m08 Prelaunch Decision Boundary·m25 Traffic Source Before Metrics 계승, 충돌 없음. 신규 durable learning: Agent-Led Growth Conflicts With Non-Autonomous Trust Frame Until Human First Value Is Validated. MARKETING_LEARNINGS.md 승격. 새 이벤트·속성·공개 카피·API/MCP·tracking/privacy·배포·외부발송·비용·권한 변경 0. HTML report gate(<html/<body/axis ax1/axis ax2/<details) 통과. Infinity dirty 무관 파일 staging 제외. L2 agent-approved.) -->

<!-- marketing-45 completed 2026-06-07T23:07Z → reports/marketing-45/2026-06-07T2307Z-local.html [projects: virtue; type: strategy; topics: ai-trust,positioning,onboarding,prelaunch] (Virtue AI 약속 문장 decision-control 감사표 작성 완료. 산출물은 virtue-rebirth-app `e9e9a5f`의 `apps/web/docs/ai-promise-decision-control-audit-table.md`(신규 1파일, docs-only). Gartner 2026 AI shopping survey(결정 대행보다 선택권 강화에 더 열려 있음)를 Virtue prelaunch 카피 감사로 번역해, 홈·`/add`·결과 카드·내부 agent snippet의 약속 문장을 표면별 × 현재 문장(file:line) × 결정-위임 위험 × 선택권-제어 읽기 × 더 안전한 내부 후보(proposal-only) × 승인 경계로 매핑. 핵심 발견: 비자율 AI 판정 제품에서 결정-위임 위험은 동사 프레임(`채점`/`판정`=판결 vs `본`/`보여주기`=관점)에 실리고 Virtue는 버튼 `AI 채점`(add:29) vs 헤더 `AI가 본 오늘`(add:30)로 프레임이 섞임; 제어 체감은 카피가 아니라 결과 후 선택 affordance(취소·한 번 더·저장, add:386/399/408, 0점도 저장 가능·무저장 종료 비용 0)에 실려 마지막 결정권은 이미 구조적으로 사용자에게 있음. 따라서 위험은 권한 부재가 아니라 문장이 권한을 덜 보이게 함. 후보 문구는 전부 proposal-only, 공개 버튼/헤더/힌트/온보딩 카피·llms.txt·cap 정책 변경은 approval-needed로 분리. first value 매핑 J1/J2/J4=`deed_saved`:188, J3=`deed_judged`:107 재정의 0, `deed_save_capped`=availability/friction 계승, m24/m38 trust-control 경계·m32 첫 입력 조향·m18 AEO 경계 재정의 0, synthetic/mock/self-test와 tiny sample 비결정 등급 보존. 신규 이벤트·속성·공개 카피·tracking/privacy·dashboard·session replay·코드·배포·외부발송·비용·권한 변경 0, event anchor drift 0(73/79/107/140/154/172/188/204 현행 일치, 최근 memo-only scoring 커밋으로 줄 +1·이름/제거 0), code diff 0, conflict marker 0, copy 인용 일치 확인. HTML 보고서 `<html`/`<body`/axis ax1/axis ax2/`<details` 포함 확인 + details에 계승한 기준·이번에 새로 배운 것·다음 Marketer 규칙·승격 후보 포함. MARKETING_LEARNINGS.md에 durable learning "Decision-Delegation Risk Rides The Verb, Control Rides The Affordance" 승격. Infinity dirty 무관 파일(EVALUATION_NOTES.md) staging 제외. L2 agent-approved push.) -->

<!-- marketing-44 completed 2026-06-07T10:07Z → reports/marketing-44/2026-06-07T1007Z-local.html [projects: virtue; type: strategy; topics: ai-product,activation,onboarding,measurement] (Virtue 결과 카드 직후 30초 행동 감사표 작성 완료. 산출물은 virtue-rebirth-app `838f8a2`의 `apps/web/docs/post-response-30-second-action-audit-table.md`(신규 1파일, docs-only). AI 첫 응답의 가치는 이벤트 수가 아니라 응답 직후 행동 흐름으로 드러난다는 post-response flow 렌즈를 Virtue prelaunch 기준으로 번역해, 결과 카드(`deed_judged`:106) 직후 30초를 세션 전체와 분리된 수기 판독 단위로 고정. 핵심: 같은 결과 카드가 J3엔 first value 도착점이라 저장 없이 닫힘이 정상일 수 있고, J1/J2/J4엔 저장 전 통과점이라 `deed_saved`:183까지 이어져야 활성화로 읽는다. 결과 직후 행동을 `deed_saved`/저장 없는 종료/`deed_rerolled`/`deed_save_capped`/off-instrument 행동별로 activation/normal/hold/friction에 매핑하고, do-not-send 기본값 "보내지 않음"과 do-not-change 경계를 명시. first value 매핑 J1/J2/J4=`deed_saved`, J3=`deed_judged` 재정의 0, `deed_save_capped`=availability/friction 계승, synthetic/mock/self-test와 tiny sample 비결정 등급 보존. 신규 이벤트·속성·카피·tracking/privacy·dashboard·session replay·타이머·코드·배포·외부발송·비용·권한 변경 0, event anchor drift 0, code diff 0, conflict marker 0. HTML 보고서 `<html`/`<body`/axis ax1/axis ax2/`<details` 포함 확인 + details에 계승한 기준·이번에 새로 배운 것·다음 Marketer 규칙·승격 후보 포함. MARKETING_LEARNINGS.md에 durable learning "Post-Response Flow Reveals Value, Not The Result Event" 승격. Infinity dirty 무관 파일(EVALUATION_NOTES.md) staging 제외. L2 agent-approved push.) -->

<!-- research-12 completed 2026-06-07T04:07Z → intents/archive/research-12.md [projects: content-strategy,product-design,personal-brand; type: research; topics: format,differentiation,creative-strategy] (형식은 따르고 관점은 비트는 기준 조사 완료. 산출물 artifacts/research-12/format-vs-twist-decision-frame.md, HTML reports/research-12/2026-06-07T0407Z-local.html. 핵심: "그릇은 따르고 내용물은 비튼다" — 결과물을 6개 층(L1 탐색·L2 입력·L3 신뢰·L4 관점·L5 톤·L6 사례연결)으로 분해해, 실패하면 떠나는 층(L1·L2)은 따르고 L3 신뢰·안전은 절대 비틀지 않으며 잊히면 끝인 층(L4~L6)은 비튼다. 형식까지 비틀면 학습비용 폭발, 내용까지 따르면 복제품. 콘텐츠 포맷(MrBeast·Morning Brew·배민)·제품 UX(토스·Airbnb·Google, 반례 Tesla 물리버튼 제거)·브랜드 포지셔닝(Liquid Death·Oatly)·교육/워크샵(Duolingo·TED/세바시) 4범주 10사례 × 따른 형식·비튼 층·실패 위험으로 검증. 가치(형식=신뢰·학습비용, 비틀기=차별·기억, 층이 달라 비충돌)→정책(L1·L2 따르고 L3 절대 안 비틀고 L4~L6 비튼다)→실행(레이어 분해 후 1~2개 층만 세게, 익숙한 그릇+낯선 내용, 80/20)→순환(형식은 이탈/완료율, 비틀기는 저장/공유로 측정; 이탈↑면 형식 복귀, 기억 0이면 더 비틀고 잘 먹힌 비틀기는 시그니처로 고정) 구조로 정리. 사용자 4프로젝트 적용표(세계여행 유튜브=썸네일·페이싱 따르고 단일 각도·솔직 톤 비틀고 형식 실험 금지 / Threads=첫 줄 요약·짧은 문단 따르고 관점·비유 비틀고 정보 과다 금지 / 카드뉴스=카드 수·구성·가독 따르고 큐레이션·연결·시리즈 컨셉 비틀고 레이아웃 비틀기 금지 / 앱·워크샵=결제·인증·실습 구조 따르고 핵심 가치 제안·프레임 비틀고 L3 신뢰·워크샵 형식 비틀기 금지) + 체크리스트 7 + 출처 10. 공개 발송·브랜드명/카피 확정·실제 디자인 배포·유료 도구·외부 계정 액션 0, 코드·배포 변경 0. 수치는 공개 보도·위키 기준 추정치 명시. HTML report gate(`<html`/`<body`/axis ax1/axis ax2/`<details`) 통과. Infinity dirty 무관 파일(EVALUATION_NOTES.md) staging 제외.) -->

<!-- marketing-43 completed 2026-06-06T22:07Z → reports/marketing-43/2026-06-06T2207Z-local.html [projects: virtue; type: strategy; topics: retention,reactivation,onboarding] (Virtue 첫 주 재초대 경계표 작성 완료. 산출물은 virtue-rebirth-app의 `apps/web/docs/first-week-reactivation-boundary-table.md`(신규 1파일, docs-only). Amplitude win-back/D7 + ProductLed AI onboarding 렌즈를 Virtue prelaunch 기준으로 번역해, 첫 주 D1/D3/D7 미방문을 onboarding 실패가 아니라 잡별 재초대 후보로 읽는 경계표를 고정. 미방문을 RC-WARM(first value 도달 후 second value 없이 미방문=value recall 후보)/RC-PRE-LOST(first value 전 멈춤 중 B-LOST만)/RC-NORMAL(J3 judged 후 저장 없이 정상 종료=후보 아님)/RC-AVAIL(`deed_save_capped`·503·지연=후보 아님)/RC-EXCLUDED(synthetic/mock/self-test=후보 아님) 5종으로 먼저 가르고, J1~J4별 first value·놓친 second value·돌아올 이유(value recall 방향)·보내면 안 되는 조건·승인 필요선을 한 표로 고정. 핵심: 미방문≠실패, first value까지 간 미방문은 warm 후보, 같은 미방문도 잡별 부호 다름(J3 정상 종료라 저장 독촉 금지), 재초대 기본값은 "보내지 않음"이고 모든 발송은 approval-needed. first value 매핑 J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106 재정의 0. m14 second value 연결·m31 막힘 4분류·m40 show-nothing·m26 recovery·m41 PQL·m28 monetization 계승, retention 대조 m37·PQL 결론 m41 위임. First verification gate PASS: 첫 10명 또는 첫 7일에 reactivation rate/churn/retention%/% 결론 없이 분류 가능성만 확인. 신규 이벤트·속성·카피·발송·retargeting·tracking/privacy·대시보드·세션리플레이·코드·배포·외부발송·비용·권한 변경 0, code diff 0, conflict marker 0, source note path 인용, 이벤트 앵커 72/78/106/135/149/167/183/199 drift 0. HTML 보고서 `<html`/`<body`/axis ax1/axis ax2/`<details` 포함 확인 + details에 계승한 기준·이번에 새로 배운 것·다음 Marketer 규칙·승격 후보 포함. MARKETING_LEARNINGS.md에 durable learning "First-Week Non-Return Is A Reactivation Candidate, Not A Failure" 승격. Infinity dirty 무관 파일(EVALUATION_NOTES.md) staging 제외. L2 agent-approved push.) -->

<!-- marketing-42 completed 2026-06-06T10:07Z → reports/marketing-42/2026-06-06T1007Z-local.html [projects: virtue; type: strategy; topics: ai-product,activation,retention,measurement] (Virtue 세션당 가치 판독표 작성 완료. 산출물은 virtue-rebirth-app `7e364a6`의 `apps/web/docs/value-per-session-reading-table.md`(신규 1파일, docs-only). Mixpanel 2026 AI/product analytics 렌즈를 Virtue prelaunch 기준으로 번역해, 세션 가치를 이벤트/클릭 수가 아니라 잡별 first value 도달 + 종료 성격으로 읽도록 성공/정상/보류/마찰 판독표를 고정. 핵심: 짧은 무저장 세션은 J3에선 성공, J1/J2/J4에선 보류이며, 세션 분류는 비율/임계값이 아니라 대조 후보로만 읽는다. first value 매핑 J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106 재정의 0. m39 readiness trace·m40 show-nothing·m41 PQL·m29 AI proxy·m31 bumper·m37 correlation readiness 계승, 대조 방법 m37 위임. 신규 이벤트·속성·카피·tracking/privacy·대시보드·세션리플레이·코드·배포·외부발송·비용·권한 변경 0, code diff 0, conflict marker 0, 이벤트 앵커 drift 0. HTML 보고서 `<html`/`<body`/axis ax1/axis ax2/`<details` 포함 확인 + details에 계승한 기준·이번에 새로 배운 것·다음 Marketer 규칙·승격 후보 포함. MARKETING_LEARNINGS.md에 durable learning "Session Value Is Read By Job, Not Event Count" 승격. Infinity dirty 무관 파일(EVALUATION_NOTES.md) staging 제외. L2 agent-approved push.) -->

<!-- marketing-41 completed 2026-06-05T22:07Z → reports/marketing-41/2026-06-05T2207Z-local.html [projects: virtue; type: strategy; topics: monetization,pql,activation,retention] (Virtue PQL 묶음 정의 작성 완료. 산출물은 virtue-rebirth-app `0b8e4ab`의 `apps/web/docs/pql-bundle-definition.md`(신규 1파일, docs-only). ProductLed 2026 PLG signal quality 렌즈를 Virtue prelaunch 기준으로 번역해, PQL/upgrade-readiness를 단일 이벤트가 아니라 반복+재방문 행동 묶음으로 정의하고, 가짜 PQL(단일 이벤트·availability·정상 종료) 구분 기준과 Waiting·approval-needed 경계를 명시. first value 매핑 J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106 재정의 0, `deed_save_capped`=availability/friction 계승. m28 monetization·m37 correlation readiness·m33 measurement readiness·m34 activation boundary 계승, 임계값/conversion/유의성 결론 금지. 신규 이벤트·속성·카피·tracking/privacy·대시보드·세션리플레이·코드·배포·외부발송·비용·권한 변경 0, code diff 0, conflict marker 0. HTML 보고서 `<html`/`<body`/axis ax1/axis ax2/`<details` 포함 확인 + details에 계승한 기준·이번에 새로 배운 것·다음 Marketer 규칙·승격 후보 포함. MARKETING_LEARNINGS.md에 durable learning "PQL Is A Bundle, Not A Single Event" 승격. Infinity dirty 무관 파일(EVALUATION_NOTES.md) staging 제외. L2 agent-approved push.) -->

<!-- marketing-40 completed 2026-06-05T10:07Z → reports/marketing-40/2026-06-05T1007Z-local.html [projects: virtue; type: strategy; topics: onboarding,nudge,activation] (Virtue 이벤트 기반 넛지 경계표 작성 완료. 산출물은 virtue-rebirth-app의 `apps/web/docs/event-triggered-nudge-boundary-table.md`(신규 1파일, docs-only). Intercom 2026 onboarding flow 렌즈를 Virtue prelaunch 기준으로 번역해, 넛지·체크리스트·툴팁 후보를 B-LOST만으로 제한하고 기본값을 "띄우지 않음"으로 고정하는 경계표 작성. 이벤트 조합(trigger)과 잡 맥락 대조 절차, B-MISMATCH/B-AVAIL 구분, first value 도달 직후 전환/공유/유료 넛지 금지 명시. first value 매핑 J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106 재정의 0. m35 bumper·m31 bumper-by-job·m17 nudge·m32 first-input 계승. 신규 이벤트·속성·카피·tracking/privacy·대시보드·세션리플레이·코드·배포·외부발송·비용·권한 변경 0. HTML 보고서 포함 확인. MARKETING_LEARNINGS.md에 durable learning "Nudges Are Event-Triggered, And Show-Nothing Is The Default" 승격. L2 agent-approved push.) -->

<!-- marketing-39 completed 2026-06-04T22:07Z → reports/marketing-39/2026-06-04T2207Z-local.html [projects: virtue; type: strategy; topics: ai-trust,onboarding,measurement] (Virtue Readiness Trace 프레임 작성 완료. 산출물은 virtue-rebirth-app의 `apps/web/docs/readiness-trace-framework.md`(신규 1파일, docs-only). Microsoft/MSR 2026 human-AI teaming 렌즈를 Virtue prelaunch 기준으로 번역해, 첫 경험을 outcome/reliance/safety/learning 4축 흔적으로 읽는 프레임 고정. deed_saved를 판정 승인으로, deed_rerolled를 불신으로 읽는 오독 금지 명시. first value 매핑 J1/J2/J4=deed_saved:183, J3=deed_judged:106 재정의 0. m38/m24/m37 계승. L2 agent-approved push.) -->

<!-- marketing-38 completed 2026-06-04T10:07Z → reports/marketing-38/2026-06-04T1007Z-local.html [projects: virtue; type: strategy; topics: ai-trust,measurement,product] (Virtue No Autonomous Action trust frame 작성 완료. 산출물은 virtue-rebirth-app의 `apps/web/docs/no-autonomous-action-trust-frame.md`(신규 1파일, docs-only). McKinsey/Gartner 2026 AI trust 분류를 Virtue non-autonomous 프레임으로 번역, 신뢰 질문을 "AI가 자율 행동을 해도 되나"에서 "출력을 조언으로 읽나 판결로 읽나"로 수축. m24/m20 계승. L2 agent-approved push.) -->

<!-- marketing-37 completed 2026-06-03T22:07Z → reports/marketing-37/2026-06-03T2207Z-local.html [projects: virtue; type: strategy; topics: retention,measurement,correlation] (Virtue retention 대조 등록부 작성 완료. 산출물은 virtue-rebirth-app의 `apps/web/docs/retention-correlation-registry.md`(신규 1파일, docs-only). Correlation Readiness gate 정의: 묶음 완료 정의·D7 우선·제외 조건·pseudo-query shape 사전 등록 후 실행. m34/m33/m22 계승. L2 agent-approved push.) -->

<!-- marketing-36 completed 2026-06-03T10:07Z → reports/marketing-36/2026-06-03T1007Z-local.html [projects: virtue; type: strategy; topics: retention,content,activation] (Virtue D7 retention 관찰 창 설계 완료. 산출물은 virtue-rebirth-app의 `apps/web/docs/d7-retention-observation-window.md`. m34/m33/m37 계승. L2 agent-approved push.) -->

<!-- marketing-35 completed 2026-06-02T22:07Z → reports/marketing-35/2026-06-02T2207Z-local.html [projects: virtue; type: strategy; topics: onboarding,activation,bumper] (Virtue 온보딩 bumper 후보표 작성 완료. 산출물은 virtue-rebirth-app의 `apps/web/docs/onboarding-bumper-candidates.md`. m31/m17 계승. L2 agent-approved push.) -->

<!-- marketing-34 completed 2026-06-02T10:07Z → reports/marketing-34/2026-06-02T1007Z-local.html [projects: virtue; type: strategy; topics: activation,measurement,plg] (Virtue Activation Boundary 등록부 작성 완료. 산출물은 virtue-rebirth-app의 `apps/web/docs/activation-boundary-registry.md`. Measurement Readiness gate 정의: first value 매핑·후보 묶음+window·TTV·D7·기준선·이벤트·트래픽 분리 준비 후 값 읽기. m33/m22/m10 계승. L2 agent-approved push.) -->

<!-- marketing-33 completed 2026-06-01T22:07Z → reports/marketing-33/2026-06-01T2207Z-local.html [projects: virtue; type: strategy; topics: activation,measurement,plg] (Virtue PLG Activation 등록부 작성 완료. m22/m10/m34 계승. L2 agent-approved push.) -->

<!-- marketing-32 completed 2026-06-01T10:07Z → reports/marketing-32/2026-06-01T1007Z-local.html [projects: virtue; type: strategy; topics: onboarding,first-input,ux] (Virtue First-Input 조향 분석 완료. 산출물은 virtue-rebirth-app의 `apps/web/docs/first-input-steering-analysis.md`. m06/m21/m30/m31 계승. L2 agent-approved push.) -->

<!-- marketing-31 completed 2026-05-31T22:07Z → reports/marketing-31/2026-05-31T2207Z-local.html [projects: virtue; type: strategy; topics: onboarding,activation,bumper] (Virtue Product Body vs Bumper 분류표 작성 완료. m30/m16/m21/m06 계승. L2 agent-approved push.) -->

<!-- marketing-30 completed 2026-05-31T10:07Z → reports/marketing-30/2026-05-31T1007Z-local.html [projects: virtue; type: strategy; topics: shareworthiness,activation,onboarding] (Virtue Shareworthiness 분리 프레임 작성 완료. m29/m21/m20 계승. L2 agent-approved push.) -->

<!-- marketing-29 completed 2026-05-30T22:07Z → reports/marketing-29/2026-05-30T2207Z-local.html [projects: virtue; type: strategy; topics: ai-proxy,activation,measurement] (Virtue AI Outcome Proxy 분리 기준 완료. m24/m20 계승. L2 agent-approved push.) -->

<!-- marketing-28 completed 2026-05-30T10:07Z → reports/marketing-28/2026-05-30T1007Z-local.html [projects: virtue; type: strategy; topics: monetization,paywall,activation] (Virtue Monetization Boundary 정의 완료. m22/m10 계승. L2 agent-approved push.) -->

<!-- marketing-27 completed 2026-05-29T22:07Z → reports/marketing-27/2026-05-29T2207Z-local.html [projects: virtue; type: strategy; topics: positioning,message-testing,jobs-to-be-done] (Virtue Message Confusion 증거 프레임 완료. m13/m11 계승. L2 agent-approved push.) -->

<!-- marketing-26 completed 2026-05-29T10:07Z → reports/marketing-26/2026-05-29T1007Z-local.html [projects: virtue; type: strategy; topics: retention,streak,recovery] (Virtue Recovery Over Streak 기준 완료. m22 계승. L2 agent-approved push.) -->

<!-- marketing-25 completed 2026-05-28T22:07Z → reports/marketing-25/2026-05-28T2207Z-local.html [projects: virtue; type: strategy; topics: measurement,traffic-source,analytics] (Virtue Traffic Source Before Metrics 기준 완료. m23/m11 계승. L2 agent-approved push.) -->

<!-- marketing-24 completed 2026-05-28T10:07Z → reports/marketing-24/2026-05-28T1007Z-local.html [projects: virtue; type: strategy; topics: ai-trust,trust-calibration,jobs-to-be-done] (Virtue Trust Calibration By Job 프레임 완료. m20/m21 계승. L2 agent-approved push.) -->

<!-- marketing-23 completed 2026-05-27T22:07Z → reports/marketing-23/2026-05-27T2207Z-local.html [projects: virtue; type: strategy; topics: measurement,synthetic,prelaunch] (Virtue Synthetic/Mock 제외 기준 완료. m11/m22 계승. L2 agent-approved push.) -->

<!-- marketing-22 completed 2026-05-27T10:07Z → reports/marketing-22/2026-05-27T1007Z-local.html [projects: virtue; type: strategy; topics: measurement,prelaunch,activation] (Virtue Prelaunch Measurement Baseline 완료. m08/m11 계승. L2 agent-approved push.) -->

<!-- marketing-21 completed 2026-05-26T22:07Z → reports/marketing-21/2026-05-26T2207Z-local.html [projects: virtue; type: strategy; topics: availability,friction,capping] (Virtue Availability And Friction Are Not Value 기준 완료. m22/m23/m28/m29 계승. L2 agent-approved push.) -->

<!-- marketing-20 completed 2026-05-26T10:07Z → reports/marketing-20/2026-05-26T1007Z-local.html [projects: virtue; type: strategy; topics: first-value,jobs-to-be-done,activation] (Virtue First Value Mapping 심화 완료. m06/m07/m09/m10 계승. L2 agent-approved push.) -->

<!-- marketing-19 completed 2026-05-25T22:07Z → reports/marketing-19/2026-05-25T2207Z-local.html [projects: virtue; type: strategy; topics: positioning,aeo,llms] (Virtue AEO 경계 정의 완료. m18 계승. L2 agent-approved push.) -->

<!-- marketing-18 completed 2026-05-25T10:07Z → reports/marketing-18/2026-05-18T1007Z-local.html [projects: virtue; type: strategy; topics: aeo,positioning,llms] (Virtue AEO 기초 완료. L2 agent-approved push.) -->

<!-- marketing-17 completed 2026-05-24T10:07Z → reports/marketing-17/2026-05-24T1007Z-local.html [projects: virtue; type: strategy; topics: onboarding,tooltip,activation] (Virtue 온보딩 마찰 제거 전략 완료. m16/m06 계승. L2 agent-approved push.) -->

<!-- marketing-16 completed 2026-05-23T22:07Z → reports/marketing-16/2026-05-23T2207Z-local.html [projects: virtue; type: strategy; topics: onboarding,activation,first-session] (Virtue 첫 세션 경험 개선 전략 완료. m06/m07/m10 계승. L2 agent-approved push.) -->

<!-- marketing-15 completed 2026-05-23T10:07Z → reports/marketing-15/2026-05-23T1007Z-local.html [projects: virtue; type: strategy; topics: growth,distribution,organic] (Virtue 오가닉 성장 채널 전략 완료. L2 agent-approved push.) -->

<!-- marketing-14 completed 2026-05-22T22:07Z → reports/marketing-14/2026-05-22T2207Z-local.html [projects: virtue; type: strategy; topics: retention,d7,churn] (Virtue D7 리텐션 관찰 기준 완료. m08/m11/m22 계승. L2 agent-approved push.) -->

<!-- marketing-13 completed 2026-05-22T10:07Z → reports/marketing-13/2026-05-22T1007Z-local.html [projects: virtue; type: strategy; topics: positioning,message-testing] (Virtue 포지셔닝 메시지 테스트 기준 완료. m11 계승. L2 agent-approved push.) -->

<!-- marketing-12 completed 2026-05-21T22:07Z → reports/marketing-12/2026-05-21T2207Z-local.html [projects: virtue; type: strategy; topics: positioning,differentiation] (Virtue 차별화 포지셔닝 완료. L2 agent-approved push.) -->

<!-- marketing-11 completed 2026-05-21T10:07Z → reports/marketing-11/2026-05-21T1007Z-local.html [projects: virtue; type: strategy; topics: measurement,prelaunch,activation] (Virtue Prelaunch 측정 기준 완료. m08/m14 계승. L2 agent-approved push.) -->

<!-- marketing-10 completed 2026-05-20T22:07Z → reports/marketing-10/2026-05-20T2207Z-local.html [projects: virtue; type: strategy; topics: activation,ttv,first-value] (Virtue TTV 및 Activation 기준 완료. m06/m07/m09 계승. L2 agent-approved push.) -->

<!-- marketing-09 completed 2026-05-20T10:07Z → reports/marketing-09/2026-05-20T1007Z-local.html [projects: virtue; type: strategy; topics: first-value,jobs-to-be-done] (Virtue J3 First Value 정의 완료. m06/m07 계승. L2 agent-approved push.) -->

<!-- marketing-08 completed 2026-05-19T22:07Z → reports/marketing-08/2026-05-19T2207Z-local.html [projects: virtue; type: strategy; topics: prelaunch,measurement,pmf] (Virtue Prelaunch Decision Boundary 정의 완료. m11/m14/m22/m23 계승. L2 agent-approved push.) -->

<!-- marketing-07 completed 2026-05-19T10:07Z → reports/marketing-07/2026-05-19T1007Z-local.html [projects: virtue; type: strategy; topics: first-value,jobs-to-be-done,activation] (Virtue J1/J2/J4 First Value 정의 완료. m06 계승. L2 agent-approved push.) -->

<!-- marketing-06 completed 2026-05-18T22:07Z → reports/marketing-06/2026-05-18T2207Z-local.html [projects: virtue; type: strategy; topics: jobs-to-be-done,activation,first-value] (Virtue Jobs-to-be-Done 기초 프레임 완료. L2 agent-approved push.) -->

<!-- marketing-05 completed 2026-05-18T10:07Z → reports/marketing-05/2026-05-18T1007Z-local.html [projects: virtue; type: strategy; topics: positioning,landing-page] (Virtue 랜딩 페이지 포지셔닝 완료. L2 agent-approved push.) -->

<!-- marketing-04 completed 2026-05-17T22:07Z → reports/marketing-04/2026-05-17T2207Z-local.html [projects: virtue; type: strategy; topics: onboarding,activation] (Virtue 온보딩 퍼널 분석 완료. L2 agent-approved push.) -->

<!-- marketing-03 completed 2026-05-17T10:07Z → reports/marketing-03/2026-05-17T1007Z-local.html [projects: virtue; type: strategy; topics: growth,channel] (Virtue 성장 채널 분석 완료. L2 agent-approved push.) -->

<!-- marketing-02 completed 2026-05-16T22:07Z → reports/marketing-02/2026-05-16T2207Z-local.html [projects: virtue; type: strategy; topics: positioning,value-prop] (Virtue 가치 제안 분석 완료. L2 agent-approved push.) -->

<!-- marketing-01 completed 2026-05-21T10:17Z → intents/archive/marketing-01.md (Virtue add-flow telemetry 머지/배포 완료. L2 approved push.) -->

<!-- naver-shopping-01 created 2026-06-07T23:07Z → waiting (네이버/스마트스토어 읽기 전용 접근 허용 여부 질문 발송) -->

<!-- research-11 completed 2026-06-04T04:07Z → intents/archive/research-11.md (Virtue 경쟁 포지셔닝 조사 완료) -->

<!-- research-10 completed 2026-06-02T04:07Z → intents/archive/research-10.md -->

<!-- research-09 completed 2026-05-31T04:07Z → intents/archive/research-09.md -->

<!-- research-08 completed 2026-05-28T04:07Z → intents/archive/research-08.md -->

<!-- research-07 completed 2026-05-26T04:07Z → intents/archive/research-07.md -->

<!-- research-06 completed 2026-05-23T04:07Z → intents/archive/research-06.md -->

<!-- research-05 re-run completed 2026-04-23T10:00 → intents/archive/research-05.md (3차) -->

<!-- wiki-04 completed 2026-04-25T09:00 → intents/archive/wiki-04.md -->

<!-- wiki-03 completed 2026-04-20T13:30 → intents/archive/wiki-03.md -->

<!-- wiki-02 completed 2026-04-19T02:40 → intents/archive/wiki-02.md -->

<!-- wiki-01 completed 2026-04-18T09:00 → intents/archive/wiki-01.md -->

<!-- doc-01 completed 2026-04-08 13:05 → intents/archive/doc-01.md -->

<!-- monitor-01 completed 2026-04-08 11:15 → intents/archive/monitor-01.md -->

<!-- build-01 completed 2026-04-21T00:30 → intents/archive/build-01.md -->

<!-- research-05 re-run completed 2026-04-23T10:00 → intents/archive/research-05.md (3차) -->
