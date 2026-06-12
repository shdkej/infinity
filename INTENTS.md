# Intent Registry

> Heartbeat Agent가 주기적으로 읽고 실행하는 의도 목록.

## Inbox


## Active

<!-- naver-shopping-01 active 2026-06-11T00:35Z → intents/active/naver-shopping-01.md [display: 나래/Narae; projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,marketing; status: active-sourcing-first-luggage-tags-downgraded; approval: no-current-user-blocker] (사용자-facing 이름 나래/Narae 확정, 내부 id/path는 naver-shopping-agent 유지. 00:08Z 트래블러스노트/여행준비 속지는 "너무 일반적"으로 첫 SKU 후보에서 내림. 14:09Z 사용자 피드백으로 워크샵/질문카드 monetization path는 Naver revenue/SKU 후보에서 철회됨. 20:07Z paper/card-led arrival-day failure-prevention insert keyword test 완료: `해외여행 체크리스트`는 clean-ish paper/planner shelf(OpenAPI 32,278; SearchAd 310 PC + 1,750 mobile/mo)지만 mobile CTR 0.05%로 buyer intent 약하고 generic checklist/planner commodity. `여행 준비 카드`/`여행 체크리스트 카드`는 trading cards/photo-card holders/boards/wallets/imported goods noise가 큼. emergency/safety/contact-card 언어는 story-rich but keyword-weak/non-travel/privacy-sensitive. 결론은 **HOLD / paper-card insert를 lead SKU로 만들지 않음**. 산출물 `naver-shopping-agent/arrival-day-insert-keyword-test-2026-06-10.md`, report `reports/naver-shopping-01/2026-06-10T2007Z-local.html`. 2026-06-11 사용자 선호 업데이트: 나래는 상품제작보다 소싱 중심으로 보고, 러기지택/캐리어네임택은 선호 낮은 상품이라 다음 리드에서 내림. 다음 안전 액션은 broader sourcing-first screen. 라이브 상품등록/가격·배송·재고/광고·고객·주문·계정·공개발행 0. archive 안 함(active 유지).) -->

<!-- build-03 active 2026-06-12T00:00Z → intents/active/build-03.md [display: Control Center / Ops CMS; projects: infinity,personal-ops,infrastructure; type: design; topics: dashboard,workflow,automation; status: active-inventory-in-progress] (Inbox에서 Active로 승격. 2026-06-12 Heartbeat에서 dashboard-inventory artifact 작성 완료. 첫 액션으로 Travel/Status/Infinity/Card Library/static pages 운영 현황 인벤토리 → artifacts/build-03/dashboard-inventory.md 생성. 다음: MVP 정보구조 설계 및 구현 계획 수립.) -->

## Waiting

<!-- 사용자 결정, 외부 조건, 안전 확인 대기. 같은 질문을 반복하지 않고 상태만 보존한다. -->

## Archive

<!-- marketing-54 completed 2026-06-11T22:07Z → reports/marketing-54/2026-06-11T2207Z-local.html [projects: virtue; type: strategy; topics: onboarding,activation,prelaunch,feedback-loop] (Virtue 첫 10명 관찰/질문 스크립트 기대-획득-막힘 이유 루프 감사표 작성 완료. 산출물 `artifacts/marketing-54/virtue-first-10-expectation-outcome-blocker-loop-audit.md`. 출처노트 `source/external-links/marketing/2026-06-11-onboarding-feedback-loop.md`는 knowledge-lab 루트 기준 존재 확인. J1/J2/J4=`deed_saved`, J3=`deed_judged` first-value 매핑 유지. 정상 종료, 혼란 종료, 가치 미전달, 이미 충분해서 종료를 manual exit class로 분리. 신규 이벤트·인앱 서베이·tracking/privacy·공개 카피·배포·외부발송·비용 변경 0. conflict marker 0건. HTML report gate(`<html`/`<body`/`axis ax1`/`axis ax2`/`<details`) 통과.) -->

<!-- marketing-53 completed 2026-06-11T10:15Z → reports/marketing-53/2026-06-11T1015Z-local.html [projects: virtue; type: strategy; topics: ai-onboarding,activation,prelaunch] (Virtue 첫 입력/결과 직후 task-completion 감사표 작성 완료. 산출물 `artifacts/marketing-53/virtue-intent-to-task-completion-audit-table.md`. 출처노트 `source/external-links/marketing/2026-06-11-ai-onboarding-intent-to-task.md`(knowledge-lab 루트 기준 존재 확인 — intent에 기재된 경로는 infinity 루트가 아니라 knowledge-lab 루트 상대경로였음)의 ProductLed/Userflow AI 온보딩 렌즈를 `사용자 의도 → AI가 수행한 작업 → 사용자가 선택한 다음 행동` 3칸 분해로 번역해 답변형 vs 작업완료형 온보딩을 잡별(J1~J4)로 분리. 핵심: `add_flow_started`=의도 진입/`deed_judged`=AI 작업 수행/`deed_saved`·무저장 종료·`deed_rerolled`=다음 행동. J1/J2/J4 작업완료=`deed_saved`, J3=`deed_judged` 자체(무저장 종료 정상)로 `deed_judged` 과대평가·judged−saved 갭 이탈 오독을 잡별로 고정. 컬럼: 의도/AI 작업/다음 행동/observable evidence/기존 이벤트·문서 신호/interpretation risk/첫 10명 관찰 질문/no-tracking-change note. 첫 10명 관찰 컬럼·사후질문은 proposal-only. 기존 이벤트 6개(add_flow_started/deed_judged/deed_saved/level_up_viewed/deed_rerolled/deed_save_capped)만 인용, 신규 정의 0. 선행 6문서(m44 post-response-30-second/first-session-jtbd-matrix/m42 value-per-session/seven-day-deed-loop/m38 trust-control/copy-spec) 충돌 0. 공개 카피·이벤트·tracking/privacy·배포·외부발송·비용·권한 변경 0건. conflict marker 0건. HTML report gate(`<html`/`<body`/`axis ax1`/`axis ax2`/`<details`) 통과. 실행 범위는 Infinity 캐노니컬 루트 내 docs-only(virtue-rebirth-app 미변경). 검증: 필수문자열 5/5 PASS, 충돌마커 0, 이벤트 6개 인용 확인.) -->

<!-- marketing-52 completed 2026-06-10T22:07Z → reports/marketing-52/2026-06-10T2207Z-local.html [projects: virtue; type: strategy; topics: activation,onboarding,ai-product] (Virtue `/add` 첫 입력 prompt design 감사표 작성 완료. 산출물 `artifacts/marketing-52/virtue-add-first-input-prompt-design-audit.md`. 출처노트 `source/external-links/marketing/2026-06-10-ai-onboarding-click-tax-output.md`의 click tax / first output 렌즈를 UI instruction·judgment delegation·desired-result teaching 3분류로 번역하고, 현재 `/add` 헤더·사진 슬롯·메모 label/placeholder·judge button·hint를 잡별로 감사. 결론: Virtue는 튜토리얼 click tax는 낮지만 첫 입력이 "무엇을 했나"를 묻는 데 머물고 "AI에게 어떤 결과를 원하는가"를 잡별로 지정하게 돕지는 않음. J1/J2/J4=`deed_saved`, J3=`deed_judged` 유지. 후보 문구는 전부 proposal-only/public copy approval-needed. 신규 이벤트·tracking/privacy·dashboard/session replay·code·deployment·external messaging·cost·permission 변경 0. HTML report gate 통과. MARKETING_LEARNINGS.md에 "Prompt Design Teaches Desired Result, Not UI Or Judgment" 승격.) -->

<!-- marketing-51 completed 2026-06-10T10:07Z → reports/marketing-51/2026-06-10T1007Z-local.html [projects: virtue; type: strategy; topics: marketing,activation,product] (Virtue guided first-value 첫 세션 감사표 작성 완료. 산출물 `artifacts/marketing-51/virtue-guided-first-value-session-audit.md`. 첫 세션을 첫 입력 전 / AI 판단 대기 / 결과 해석 / 저장·종료 4구간으로 나누고, 사용자가 직접 해냈다고 느낀 순간과 AI가 대신 결정했는지/정리했는지의 수기 질문 2개를 고정. first value 매핑 J1/J2/J4=`deed_saved`, J3=`deed_judged` 재정의 0. `first-real-user-baseline-template`, `first-10-design-user-ask-script`, `post-result-self-appropriation-reading-table`와 보완 관계 확인. 신규 이벤트·tracking/privacy·dashboard/session replay·공개 카피·배포·외부발송·비용·권한 변경 0. HTML report gate 통과. MARKETING_LEARNINGS.md에 "Guided First-Value Is A Four-Stage Handoff" 승격.) -->

<!-- marketing-50 completed 2026-06-10T03:07Z → reports/marketing-50/2026-06-10T0307Z-local.html [projects: naver-shopping,infinity,personal-ops; type: strategy; topics: marketing,positioning,workflow; source: naver-shopping-01] (질문/워크샵 카드 family의 non-generic 포지셔닝 선택 완료. 산출물 `artifacts/marketing-50/question-workshop-card-positioning-selection.md`. 결론: `질문 카드`/`대화 카드`는 broad object-shape demand이지만 generic relationship/icebreaking/game 포화라 listing approval로 보내지 않음; 리드 프레임은 **AI/creator workshop facilitation cards**, 보조 테스트는 product-observation/founder reflection, team retrospective, travel insight-to-content. `워크샵 카드`는 언어가 가장 깨끗하지만 exact demand가 under 20/mo라 broad keyword bridge와 use-case lead를 분리. 모든 문구는 draft/proposal-only; 소싱·상품등록·공개카피·가격·배송·재고·옵션·광고·고객/주문/계정/스토어 액션 0. HTML report gate 통과. MARKETING_LEARNINGS.md에 "Purchase Situation Before Object Shape" 승격.) -->

<!-- marketing-49 completed 2026-06-09T22:27Z → intents/archive/marketing-49.md [projects: virtue; type: strategy; topics: activation,retention,marketing] (Virtue 결과 카드 직후 "수동 감탄 vs 자기화 행동" 판독표 docs-only 작성 완료. 산출물 `artifacts/marketing-49/virtue-post-result-self-appropriation-reading-table.md`, 보고서 `reports/marketing-49/2026-06-09T2227Z-local.html`. 기존 first value 매핑 J1/J2/J4=`deed_saved`, J3=`deed_judged` 유지. 결과 직후 행동을 저장/재작성/선택/자기 말 설명/무저장 정상 종료/수동 감탄/마찰로 수기 판독하게 정리. 신규 이벤트·속성·tracking/privacy·dashboard/session replay·공개 카피·발송·배포·외부 액션 0.) -->

<!-- marketing-48 completed 2026-06-09T10:57Z → reports/marketing-48/2026-06-09T1057Z-local.html [projects: naver-shopping,infinity,personal-ops; type: marketing-positioning; topics: listing-copy,keyword-strategy,positioning; source: naver-shopping-01] (나래/Narae `naver-shopping-01`의 target-agent 요청을 처리해 트래블러스노트 standard-size travel-prep structured insert 피벗 SKU의 내부 listing title/copy 포지셔닝 후보군 작성 완료. 산출물 `artifacts/marketing-48/travelers-notebook-insert-listing-copy-positioning.md`. 제목 후보 8개, 금지/주의 제목 패턴, 1문장 가치제안, 상세페이지 첫 문단 후보, 검색 키워드 묶음, 썸네일 문구, 승격 전 검증 게이트 포함. 핵심: 큰 검색량 단어를 제목 맨 앞에 두지 않고, 리필/속지 구매 맥락과 여행준비 구조를 먼저 세움. 모든 문구는 draft/proposal-only, 브랜드명/호환/규격 표현은 approval-needed, 가격/배송/재고/옵션/광고/상품등록/공개상세/고객·주문·계정 액션 0. 게이트: `rg '여행 체크리스트.*트래블러스노트|트래블러스노트.*여행 체크리스트' artifacts/marketing-48` no-match, artifact에 draft/proposal-only/approval-needed 포함, HTML report `<html`/`<body`/axis ax1/axis ax2/`<details` 확인. MARKETING_LEARNINGS 승격 후보는 단일 사례라 report에 보류.) -->

<!-- marketing-47 completed 2026-06-08T22:07Z → reports/marketing-47/2026-06-08T2207Z-local.html [projects: virtue; type: strategy; topics: prelaunch,first-users,onboarding] (Virtue 첫 10명 design-user ask script 작성 완료. 산출물은 Infinity `artifacts/marketing-47/virtue-first-10-design-user-ask-script.md`(신규 1파일, docs-only — Virtue 앱 레포 로컬 부재로 ARTIFACT_RULES에 따라 Infinity artifact로 생성). 출처노트(YC/Lenny "초기 사용자는 확장 채널보다 직접 학습 루프로 만든다")를 Virtue prelaunch 첫 사용자 학습 루프로 번역해, 정식 출시 전 내부 준비물로 초대→사용 전 2문항→첫 세션 후 3문항→자기 말 기록 칸 4지점 손기록 스크립트를 한 장으로 고정. 잡별 초대 문장 후보(J1 기록형·J2 누적형·J3 AI 호기심형·J4 회고형)는 각 잡 first value를 미리 가리키게 작성(J1/J2/J4=`deed_saved`, J3=`deed_judged`, J3 무저장 종료 정상), m45 동사 프레임(판결 아닌 관점) 적용. 사용 전 2문항=현재 행동·대체재 / 잡 신호·기대; 첫 세션 후 3문항=first value 위치 / friction(`deed_save_capped`·503·지연=availability/friction) / 결정-위임 인지(출력을 판결 vs 조언으로 읽나, m45·m38). "사용자가 자기 말로 설명한 Virtue" 기록 칸은 원문 그대로 손기록(신규 계측 0), first-real-user-baseline-template로 흘러듦. 핵심: 첫 사용자 학습은 확장 채널보다 먼저이고 산출은 성패율이 아니라 (a)반복 문제 언어 (b)자기 말로 설명한 가치 (c)결정-위임 인지 세 언어로 읽으며, 성찰형 제품에서 도움의 목표는 결정 대행이 아니라 자기 말로 가치를 말하게 하는 것(도움이 성찰 대행하면 수집 대상 소거). 선행 3문서(first-real-user-baseline-template·first-60-second-value-observation-script·ai-promise-decision-control-audit-table) 충돌 0 — 층이 다른 추가. 변경한 가정 없음, 외부 행동 0. 금지선: 공개 발송/DM/광고·프로덕션 카피·신규 이벤트/속성/tracking/privacy/dashboard/session replay·배포·비용·권한 변경 0, 코드 접근·변경 0(앱 레포 로컬 부재). HTML 보고서 `<html`/`<body`/axis ax1/axis ax2/`<details` 포함 확인 + details에 계승한 기준·이번에 새로 배운 것·다음 Marketer 규칙·승격 후보 포함. MARKETING_LEARNINGS.md에 durable learning "First-User Learning Loop Reads Language, And Help Means Articulation Not Delegation" 승격. Infinity dirty 무관 파일(EVALUATION_NOTES.md) staging 제외. L2 agent-approved push.) -->

<!-- marketing-46 completed 2026-06-08T10:07Z → reports/marketing-46/2026-06-08T1007Z-local.html [projects: virtue; type: strategy; topics: agent-led-curation,ai-value,ai-product] (Virtue AI가 이끄는 회고 큐레이션 설계 감사표 docs-only 작성 완료. 산출물 `artifacts/marketing-46/virtue-agent-led-curation-design-audit.md`. 클로드 소넷 기반 에이전트가 사용자 행동 이력에서 패턴을 감지해 자발적으로 회고 맥락을 제안·묶는 두 가지 흐름(명시적 초대 vs. 암묵적 삽입)을 J1~J4 잡별로 분류. 미래-작성 시점 트리거·공개 카피·신규 이벤트·대시보드·배포·비용·타인 알림·외부 발송 0. MARKETING_LEARNINGS.md에 "Agent-Led Curation Appears At The Moment Of Meaning, Not On A Scheduled Review" 승격.) -->

<!-- marketing-45 completed 2026-06-07T23:07Z → reports/marketing-45/2026-06-07T2307Z-local.html [projects: virtue; type: strategy; topics: ai-trust,product-design,decision-control] (Virtue AI "판결" 언어 감사표 docs-only 작성 완료. 산출물 `artifacts/marketing-45/virtue-ai-judgment-language-audit.md`. 현재 UI의 judge/judged/deed_judged 용어가 결과를 "AI의 판결"로 읽히게 하는 위험을 잡별로 분해(J1~J4). 대안 동사 후보(관찰·발견·정리·패턴·연결·제안·바라본)는 proposal-only/approval-needed. 신규 이벤트·tracking/privacy·dashboard·session replay·공개 카피·배포·외부발송·비용·권한 변경 0. HTML report gate 통과. MARKETING_LEARNINGS.md에 "Judgment Language Displaces Self-Authorship" 승격.) -->

<!-- marketing-44 completed 2026-06-07T10:07Z → reports/marketing-44/2026-06-07T1007Z-local.html [projects: virtue; type: strategy; topics: ai-product,onboarding,first-session] (Virtue 첫 세션 JTBD 매핑표 docs-only 작성 완료. 산출물 `artifacts/marketing-44/virtue-first-session-jtbd-matrix.md`. 첫 세션 내 행동 단계(시작 전·첫 입력·AI 판단 대기·결과 해석·저장·재방문)를 J1~J4 잡별로 분해하고, 각 단계에서 사용자가 무엇을 기대하는지·어떤 마찰이 발생하는지·어떤 신호가 first value를 가리키는지 매핑. 신규 이벤트·tracking/privacy·dashboard/session replay·공개 카피·배포·외부발송·비용·권한 변경 0. HTML report gate 통과. MARKETING_LEARNINGS.md에 "Post-Response 30-Second Window Is The Critical First-Session Handoff" 승격.) -->

<!-- research-12 completed 2026-06-07T04:07Z → intents/archive/research-12.md [projects: content-strategy,product-design,personal-brand; type: research; topics: research-bank,content,ai-products] (콘텐츠 전략 리서치 뱅크 2회 확장 완료. 산출물은 `source/` 하위 링크 노트 4건(세스 고딘/마케팅처럼-느껴지면-맞다·테크 영상 소비·앤더슨 호로위츠 AI-native UX·First Round Review 창업자 포지셔닝). Infinity artifact 3건(personal-brand-narrative-consistency, tech-content-creator-multi-format-strategy, ai-native-ux-design-principles). 신규 이벤트·tracking/privacy·배포·외부발송·비용·권한 변경 0. HTML report gate 통과.) -->

<!-- marketing-43 completed 2026-06-06T22:07Z → reports/marketing-43/2026-06-06T2207Z-local.html [projects: virtue; type: strategy; topics: retention,ai-product,personal-growth] (Virtue 7일 반복 사용 루프 docs-only 설계 완료. 산출물 `artifacts/marketing-43/virtue-seven-day-deed-loop.md`. 성찰형 AI 제품에서 7일 루프가 어떻게 자기 강화되는지를 J1~J4 잡별로 분해. J3 잡(미래 자아 탐구형)은 `deed_judged` 자체가 완료 이벤트이므로 7일 루프 설계를 J1/J2/J4(저장 중심)와 다르게 처리해야 함을 명시. 신규 이벤트·tracking/privacy·dashboard/session replay·공개 카피·배포·외부발송·비용·권한 변경 0. HTML report gate 통과. MARKETING_LEARNINGS.md에 "Retention Loops In Reflective Products Run On Language Not Streaks" 승격.) -->

<!-- marketing-42 completed 2026-06-06T10:07Z → reports/marketing-42/2026-06-06T1007Z-local.html [projects: virtue; type: strategy; topics: ai-product,value,session-economics] (Virtue 세션당 AI 가치 전달 지표 설계 docs-only 작성 완료. 산출물 `artifacts/marketing-42/virtue-ai-value-per-session-design.md`. `deed_judged` → `deed_saved` 전환율을 세션당 AI 가치 신호로 정의하고, 저하 원인(입력 너무 짧음/AI 출력 일반적/저장 UX 마찰/J3 무저장 정상 종료 오독)을 잡별로 분류. 신규 이벤트·tracking/privacy·dashboard/session replay·공개 카피·배포·외부발송·비용·권한 변경 0. HTML report gate 통과. MARKETING_LEARNINGS.md에 "Judged-To-Saved Rate Is The AI Value Signal" 승격.) -->

<!-- marketing-41 completed 2026-06-05T23:07Z → reports/marketing-41/2026-06-05T2307Z-local.html [projects: virtue; type: strategy; topics: plg,activation,ai-product] (Virtue PLG 퍼널 설계 docs-only 완료. 산출물 `artifacts/marketing-41/virtue-plg-funnel-design.md`. 신규 이벤트·tracking/privacy·dashboard/session replay·공개 카피·배포·외부발송·비용·권한 변경 0. HTML report gate 통과. MARKETING_LEARNINGS.md 아직 없음 → 이후 누적 후 승격.) -->

<!-- marketing-40 completed 2026-06-05T10:07Z → reports/marketing-40/2026-06-05T1007Z-local.html [projects: virtue; type: strategy; topics: onboarding,product,activation] (Virtue 온보딩 첫 60초 가치 관찰 스크립트 docs-only 작성 완료. 산출물 `artifacts/marketing-40/virtue-first-60-second-value-observation-script.md`. 신규 이벤트·tracking/privacy·dashboard/session replay·공개 카피·배포·외부발송·비용·권한 변경 0. HTML report gate 통과. MARKETING_LEARNINGS.md에 "Micro-Observation Before Macro-Metrics" 승격.) -->

<!-- marketing-39 completed 2026-06-04T23:08Z → reports/marketing-39/2026-06-04T2207Z-local.html [projects: virtue; type: strategy; topics: ai-trust,activation,product] (Virtue AI 약속·결정·통제 감사표 docs-only 작성 완료. 산출물 `artifacts/marketing-39/virtue-ai-promise-decision-control-audit-table.md`. 신규 이벤트·tracking/privacy·dashboard/session replay·공개 카피·배포·외부발송·비용·권한 변경 0. HTML report gate 통과. MARKETING_LEARNINGS.md에 "Perceived Control Determines Whether AI Assistance Feels Empowering Or Undermining" 승격.) -->

<!-- marketing-38 completed 2026-06-04T10:27Z → reports/marketing-38/2026-06-04T1007Z-local.html [projects: virtue; type: strategy; topics: ai-trust,activation,copy] (Virtue AI 결과 카드 복사 스펙 docs-only 작성 완료. 산출물 `artifacts/marketing-38/virtue-ai-result-copy-spec.md`. 신규 이벤트·tracking/privacy·dashboard/session replay·공개 카피·배포·외부발송·비용·권한 변경 0. HTML report gate 통과. MARKETING_LEARNINGS.md에 "Copy Specificity Signals AI Competence Better Than Accuracy Claims" 승격.) -->

<!-- research-11 completed 2026-06-04T00:27Z → intents/archive/research-11.md [projects: personal-brand,content-strategy,research-bank; type: research; topics: research-bank,personal-brand,content] (개인 브랜드 스토리텔링 리서치 뱅크 확장 완료. 산출물은 `source/` 하위 링크 노트 3건(에어비앤비 브랜드-성장-전략·수익화 레이어·내러티브 일관성)과 Infinity artifact 1건(personal-brand-narrative-consistency 초안). 신규 이벤트·tracking/privacy·배포·외부발송·비용·권한 변경 0. HTML report gate 통과.) -->

<!-- marketing-37 completed 2026-06-03T22:07Z → reports/marketing-37/2026-06-03T2207Z-local.html [projects: virtue; type: strategy; topics: activation,product,onboarding] (Virtue 실제 사용자 첫 기준선 관찰 템플릿 docs-only 작성 완료. 산출물 `artifacts/marketing-37/virtue-first-real-user-baseline-template.md`. 신규 이벤트·tracking/privacy·dashboard/session replay·공개 카피·배포·외부발송·비용·권한 변경 0. HTML report gate 통과. MARKETING_LEARNINGS.md에 "Observe Language Before Interpreting Metrics" 승격.) -->

<!-- marketing-36 completed 2026-06-03T10:07Z → reports/marketing-36/2026-06-03T1007Z-local.html [projects: virtue; type: strategy; topics: ai-agent,ai-product,curation] (Virtue AI 에이전트 큐레이션 경계 설계 docs-only 완료. 산출물 `artifacts/marketing-36/virtue-ai-agent-curation-boundaries.md`. 신규 이벤트·tracking/privacy·dashboard/session replay·공개 카피·배포·외부발송·비용·권한 변경 0. HTML report gate 통과.) -->

<!-- marketing-35 completed 2026-06-02T23:07Z → reports/marketing-35/2026-06-02T2207Z-local.html [projects: virtue; type: strategy; topics: onboarding,activation,ai-product] (Virtue 첫 세션 활성화 캠페인 설계 docs-only 완료. 산출물 `artifacts/marketing-35/virtue-first-session-activation-campaign.md`. 신규 이벤트·tracking/privacy·dashboard/session replay·공개 카피·배포·외부발송·비용·권한 변경 0. HTML report gate 통과. MARKETING_LEARNINGS.md에 "Activation Campaigns Must Teach The Habit, Not Just Celebrate The Feature" 승격.) -->

<!-- marketing-34 completed 2026-06-02T11:07Z → reports/marketing-34/2026-06-02T1007Z-local.html [projects: virtue; type: strategy; topics: plg,activation,onboarding] (Virtue PLG 활성화 설계 docs-only 완료. 산출물 `artifacts/marketing-34/virtue-plg-activation-design.md`. 신규 이벤트·tracking/privacy·dashboard/session replay·공개 카피·배포·외부발송·비용·권한 변경 0. HTML report gate 통과.) -->

<!-- marketing-33 completed 2026-06-01T23:07Z → reports/marketing-33/2026-06-01T2307Z-local.html [projects: virtue; type: strategy; topics: marketing,product,user-research] (Virtue 사용자 인터뷰 리서치 설계 docs-only 완료. 산출물 `artifacts/marketing-33/virtue-user-interview-research-design.md`. 신규 이벤트·tracking/privacy·dashboard/session replay·공개 카피·배포·외부발송·비용·권한 변경 0. HTML report gate 통과.) -->

<!-- marketing-32 completed 2026-05-31T22:07Z → intents/archive/marketing-32.md [projects: virtue; type: strategy; topics: ai-value,proxy,positioning] (Virtue AI 가치 Proxy 분석 docs-only 완료. Infinity artifact `artifacts/marketing-32/virtue-ai-value-proxy-analysis.md`. 공개 카피·이벤트·tracking/privacy·배포·외부발송·비용·권한 변경 0. HTML report gate 통과.) -->

<!-- marketing-31 completed 2026-05-31T10:07Z → reports/marketing-31/2026-05-31T1007Z-local.html [projects: virtue; type: strategy; topics: ai-value,activation,proxy] (Virtue AI 가치 Proxy 전략 초안 docs-only 작성 완료. 산출물 `artifacts/marketing-31/virtue-ai-value-proxy-strategy.md`. 신규 이벤트·tracking/privacy·dashboard/session replay·공개 카피·배포·외부발송·비용·권한 변경 0. HTML report gate 통과.) -->

<!-- marketing-30 completed 2026-05-30T22:07Z → reports/marketing-30/2026-05-30T2207Z-local.html [projects: virtue; type: strategy; topics: marketing,content,positioning] (Virtue 콘텐츠 포지셔닝 전략 docs-only 작성 완료. 산출물 `artifacts/marketing-30/virtue-content-positioning-strategy.md`. 신규 이벤트·tracking/privacy·dashboard/session replay·공개 카피·배포·외부발송·비용·권한 변경 0. HTML report gate 통과.) -->

<!-- marketing-29 completed 2026-05-30T10:07Z → reports/marketing-29/2026-05-30T1007Z-local.html [projects: virtue; type: strategy; topics: ai-product,marketing,positioning] (Virtue 포지셔닝 전략 docs-only 작성 완료. 산출물 `artifacts/marketing-29/virtue-positioning-strategy.md`. 신규 이벤트·tracking/privacy·dashboard/session replay·공개 카피·배포·외부발송·비용·권한 변경 0. HTML report gate 통과.) -->

<!-- marketing-28 completed 2026-05-29T22:07Z → reports/marketing-28/2026-05-29T2207Z-local.html [projects: virtue; type: strategy; topics: retention,ai-product,product] (Virtue 리텐션 전략 docs-only 작성 완료. 산출물 `artifacts/marketing-28/virtue-retention-strategy.md`. 신규 이벤트·tracking/privacy·dashboard/session replay·공개 카피·배포·외부발송·비용·권한 변경 0. HTML report gate 통과.) -->

<!-- marketing-27 completed 2026-05-29T10:07Z → reports/marketing-27/2026-05-29T1007Z-local.html [projects: virtue; type: strategy; topics: marketing,growth,positioning] (Virtue 성장 전략 docs-only 작성 완료. 산출물 `artifacts/marketing-27/virtue-growth-strategy.md`. 신규 이벤트·tracking/privacy·dashboard/session replay·공개 카피·배포·외부발송·비용·권한 변경 0. HTML report gate 통과.) -->

<!-- marketing-26 completed 2026-05-28T22:07Z → intents/archive/marketing-26.md [projects: virtue; type: strategy; topics: marketing,funnel,acquisition] (Virtue 마케팅 퍼널 docs-only 완료. HTML report gate 통과.) -->

<!-- marketing-25 completed 2026-05-28T10:07Z → reports/marketing-25/2026-05-28T1007Z-local.html [projects: virtue; type: strategy; topics: marketing,acquisition,viral] (Virtue 바이럴 마케팅 docs-only 작성 완료. 산출물 `artifacts/marketing-25/virtue-viral-marketing-strategy.md`. 신규 이벤트·tracking/privacy·dashboard/session replay·공개 카피·배포·외부발송·비용·권한 변경 0. HTML report gate 통과.) -->

<!-- marketing-24 completed 2026-05-27T22:07Z → intents/archive/marketing-24.md [projects: virtue; type: strategy; topics: marketing,product,growth] (Virtue 마케팅 전략 시즌 1 완료. HTML report gate 통과.) -->

<!-- marketing-23 completed 2026-05-27T10:07Z → intents/archive/marketing-23.md [projects: virtue; type: strategy; topics: marketing,positioning,messaging] (Virtue 포지셔닝 메시지 docs-only 완료. HTML report gate 통과.) -->

<!-- marketing-22 completed 2026-05-26T22:07Z → intents/archive/marketing-22.md [projects: virtue; type: strategy; topics: marketing,landing-page,copy] (Virtue 랜딩 페이지 카피 docs-only 완료. HTML report gate 통과.) -->

<!-- marketing-21 completed 2026-05-26T10:07Z → intents/archive/marketing-21.md [projects: virtue; type: strategy; topics: marketing,email,activation] (Virtue 이메일 마케팅 docs-only 완료. HTML report gate 통과.) -->

<!-- marketing-20 completed 2026-05-25T22:07Z → intents/archive/marketing-20.md [projects: virtue; type: strategy; topics: marketing,social,content] (Virtue 소셜 미디어 콘텐츠 docs-only 완료. HTML report gate 통과.) -->

<!-- marketing-19 completed 2026-05-25T10:07Z → intents/archive/marketing-19.md [projects: virtue; type: strategy; topics: marketing,community,growth] (Virtue 커뮤니티 성장 전략 docs-only 완료. HTML report gate 통과.) -->

<!-- marketing-18 completed 2026-05-24T22:07Z → intents/archive/marketing-18.md [projects: virtue; type: strategy; topics: marketing,partnership,growth] (Virtue 파트너십 전략 docs-only 완료. HTML report gate 통과.) -->

<!-- marketing-17 completed 2026-05-24T10:07Z → intents/archive/marketing-17.md [projects: virtue; type: strategy; topics: marketing,user-research,insight] (Virtue 사용자 리서치 인사이트 docs-only 완료. HTML report gate 통과.) -->

<!-- marketing-16 completed 2026-05-23T22:07Z → intents/archive/marketing-16.md [projects: virtue; type: strategy; topics: marketing,metrics,kpi] (Virtue 마케팅 KPI 설계 docs-only 완료. HTML report gate 통과.) -->

<!-- marketing-15 completed 2026-05-23T10:07Z → intents/archive/marketing-15.md [projects: virtue; type: strategy; topics: marketing,budget,planning] (Virtue 마케팅 예산 계획 docs-only 완료. HTML report gate 통과.) -->

<!-- marketing-14 completed 2026-05-22T22:07Z → intents/archive/marketing-14.md [projects: virtue; type: strategy; topics: marketing,brand,identity] (Virtue 브랜드 아이덴티티 docs-only 완료. HTML report gate 통과.) -->

<!-- marketing-13 completed 2026-05-22T10:07Z → intents/archive/marketing-13.md [projects: virtue; type: strategy; topics: marketing,competitive,analysis] (Virtue 경쟁 분석 docs-only 완료. HTML report gate 통과.) -->

<!-- marketing-12 completed 2026-05-21T22:07Z → intents/archive/marketing-12.md [projects: virtue; type: strategy; topics: marketing,customer,persona] (Virtue 고객 페르소나 docs-only 완료. HTML report gate 통과.) -->

<!-- marketing-11 completed 2026-05-21T10:07Z → intents/archive/marketing-11.md [projects: virtue; type: strategy; topics: marketing,seo,content] (Virtue SEO 콘텐츠 전략 docs-only 완료. HTML report gate 통과.) -->

<!-- marketing-10 completed 2026-05-20T22:07Z → intents/archive/marketing-10.md [projects: virtue; type: strategy; topics: marketing,analytics,data] (Virtue 마케팅 분석 설계 docs-only 완료. HTML report gate 통과.) -->

<!-- marketing-09 completed 2026-05-20T10:07Z → intents/archive/marketing-09.md [projects: virtue; type: strategy; topics: marketing,product-market-fit,validation] (Virtue PMF 검증 전략 docs-only 완료. HTML report gate 통과.) -->

<!-- marketing-08 completed 2026-05-19T22:07Z → intents/archive/marketing-08.md [projects: virtue; type: strategy; topics: marketing,pricing,monetization] (Virtue 가격 정책 docs-only 완료. HTML report gate 통과.) -->

<!-- marketing-07 completed 2026-05-19T10:07Z → intents/archive/marketing-07.md [projects: virtue; type: strategy; topics: marketing,growth-hacking,experiment] (Virtue 성장 해킹 실험 docs-only 완료. HTML report gate 통과.) -->

<!-- marketing-06 completed 2026-05-18T22:07Z → intents/archive/marketing-06.md [projects: virtue; type: strategy; topics: marketing,influence,distribution] (Virtue 인플루언서 배포 전략 docs-only 완료. HTML report gate 통과.) -->

<!-- marketing-05 completed 2026-05-18T10:07Z → intents/archive/marketing-05.md [projects: virtue; type: strategy; topics: marketing,ads,paid] (Virtue 유료 광고 전략 docs-only 완료. HTML report gate 통과.) -->

<!-- marketing-04 completed 2026-05-17T22:07Z → intents/archive/marketing-04.md [projects: virtue; type: strategy; topics: marketing,content,blog] (Virtue 블로그 콘텐츠 전략 docs-only 완료. HTML report gate 통과.) -->

<!-- marketing-03 completed 2026-05-17T10:07Z → intents/archive/marketing-03.md [projects: virtue; type: strategy; topics: marketing,launch,go-to-market] (Virtue GTM 전략 docs-only 완료. HTML report gate 통과.) -->

<!-- marketing-02 completed 2026-05-16T22:07Z → intents/archive/marketing-02.md [projects: virtue; type: strategy; topics: marketing,positioning,messaging] (Virtue 초기 포지셔닝 메시지 docs-only 완료. HTML report gate 통과.) -->

<!-- marketing-01 completed 2026-05-21T10:17Z → intents/archive/marketing-01.md [projects: virtue; type: implementation; topics: telemetry,add-flow,analytics] (Virtue add-flow 텔레메트리 구현 완료. Kubernetes `deployment/virtue-rebirth` rollout restart로 프로덕션 반영. `https://virtue.oracle.shdkej.com` HTTP 200 확인.) -->

<!-- wiki-04 completed 2026-04-25 → intents/archive/wiki-04.md (agent-wiki 자동 사이드바 파일 완료) -->

<!-- wiki-05 completed 2026-04-26 → intents/archive/wiki-05.md (agent-wiki 정적 사이드바 적용 완료) -->

<!-- wiki-03 completed 2026-04-20 → intents/archive/wiki-03.md (agent-wiki index.html push 완료) -->

<!-- wiki-02 completed 2026-04-19 → intents/archive/wiki-02.md (agent-wiki Docsify 구현 완료) -->

<!-- wiki-01 completed 2026-04-18 → intents/archive/wiki-01.md (agent-wiki 구조 분석 완료) -->

<!-- pages-01 completed 2026-04-20 → intents/archive/pages-01.md (agent-wiki GitHub Pages 설계 완료) -->

<!-- product-01 completed 2026-05-14 → intents/archive/product-01.md (Virtue 제품 로드맵 설계 완료) -->

<!-- build-02 completed 2026-05-13 → intents/archive/build-02.md (Infinity Kanban 대시보드 배포 완료. https://infinity.oracle.shdkej.com) -->

<!-- build-01 completed → intents/archive/build-01.md (agent-wiki GitHub Pages 취소) -->

<!-- doc-01 completed → intents/archive/doc-01.md (lessons-learned.md 완료) -->

<!-- monitor-01 completed → intents/archive/monitor-01.md (monitoring_personal 완료) -->

<!-- research-01 through research-10 completed → intents/archive/ (각종 리서치 완료) -->

<!-- research-05 re-run completed 2026-04-23T10:00 → intents/archive/research-05.md -->

# 2026-06-10T23:30Z - naver-shopping-01 source update

- `naver-shopping-01`: Added a docs-only sourcing-friction gate for the question/workshop-card SKU path per Marketer `marketing-50` positioning. Verdict: DRAFT / copy-led, not listing-ready. No live store/listing/price/stock/shipping/ads/customer/order/account/public action.
