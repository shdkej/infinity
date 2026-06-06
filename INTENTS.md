# Intent Registry

> Heartbeat Agent가 주기적으로 읽고 실행하는 의도 목록.

## Inbox


## Active

### marketing-42 — Virtue value-per-session 판독표 작성
- id: marketing-42
- status: in_progress
- priority: medium
- permission: L1 (docs-only)
- project: virtue
- type: strategy
- topics: ai-product, activation, retention, measurement
- goal: Mixpanel 2026 AI/product analytics 렌즈로 Virtue prelaunch 세션당 가치 판독표 작성. 첫 10명/첫 7일 관찰에서 "이벤트 수=가치" 오독 방지.
- context: virtue-rebirth-app `/home/ubuntu/dev/virtue-rebirth-app/apps/web/docs/`
- success_criteria: 신규 docs 1파일. 기존 first value 매핑(J1/J2/J4=`deed_saved`, J3=`deed_judged`)·이벤트만 인용. V-YES/V-DONE/V-PEND/V-LOST 4분류 포함. 신규 tracking/privacy/code/copy/deploy/비용 변경 0.
- next_action: 로컬 Claude Code에서 `artifacts/marketing-42/value-per-session-reading-table-draft.md`를 `apps/web/docs/value-per-session-reading-table.md`로 이동·검증·커밋·push
- cloud_prepared: 2026-06-06T06:00Z

## Waiting

<!-- 사용자 결정, 외부 조건, 안전 확인 대기. 같은 질문을 반복하지 않고 상태만 보존한다. -->

## Archive

<!-- marketing-41 completed 2026-06-05T23:07Z → reports/marketing-41/2026-06-05T2307Z-local.html [projects: virtue; type: strategy; topics: plg,activation,monetization] (Virtue post-launch PQL/upgrade 신호 경계표 작성 완료. 산출물은 virtue-rebirth-app `fcd319a`의 `apps/web/docs/post-launch-pql-upgrade-signal-boundary-table.md`(신규 1파일, docs-only). Mixpanel PLG 2026/PQL 렌즈를 Virtue prelaunch 기준으로 번역해, PQL/upgrade-readiness를 activation(② first value)이 아니라 그 다음 층(③ 반복+재방문 묶음)으로 분리하고 출시 후 신호를 (A) PQL 후보(대조 대상·결론 아님) / (B) 비후보·가짜 PQL(단일 이벤트·availability·정상 종료·다의적 단발) / (C) Waiting·approval-needed(채점·임계값·가격·신규 tracking·대시보드·공개 카피) 세 칸으로 고정. 핵심: 단일 이벤트 특히 `deed_save_capped` 1회를 "더 원해서 막혔다=업그레이드 수요"로 읽는 것이 1번 오독이며 availability/friction으로 분류·보존한다. A1~A4 activation 후보 묶음(m33)과 prelaunch-monetization-boundary(m28) `deed_save_capped` 오독 금지를 계승, retention 대조 방법은 m37 위임. first value 매핑 J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106 재정의 0(A3는 저장 없이 반복 `deed_judged`로 후보). First verification gate PASS: 문서가 PQL 임계값·conversion rate·upgrade demand를 산출하지 않고 "출시 후 첫 10명 또는 첫 7일 대조 후보"로만 남김(모든 임계값/% 언급은 §7 금지 문장). 이전 partial run(2207Z, Claude timeout)의 잔류 tool-artifact 줄(`</content>`·`</invoke>`) 제거 후 검증. 신규 이벤트·속성·카피·tracking/privacy·pricing·대시보드·세션리플레이·코드·배포·외부발송·비용·권한 변경 0, 이벤트 앵커 72/78/106/135/149/167/183/199 drift 0, 코드 diff 0, conflict marker 0. HTML 보고서 `<html`/`<body`/axis ax1/axis ax2/`<details` 포함 확인 + details에 계승한 기준·이번에 새로 배운 것·다음 Marketer에게 넘길 규칙·승격 후보 포함. MARKETING_LEARNINGS.md에 durable learning "PQL Is A Bundle, Not A Single Event" 승격. Infinity dirty 무관 파일(EVALUATION_NOTES.md) staging 제외. L2 agent-approved push.) -->

<!-- marketing-40 completed 2026-06-05T10:07Z → reports/marketing-40/2026-06-05T1007Z-local.html [projects: virtue; type: strategy; topics: onboarding,activation,friction] (Virtue 막힘 지점 넛지 경계표 작성 완료. 산출물은 virtue-rebirth-app `d1cac9b`의 `apps/web/docs/stuck-point-nudge-boundary-table.md`(신규 1파일, docs-only). Amplitude/Lenny behavior-triggered guidance 렌즈를 Virtue prelaunch의 기존 이벤트 조합 trigger 표로 번역해 T1~T6별 도움 후보, 띄우지 말아야 할 경우, 수기 관찰 질문, prelaunch 금지선을 고정. 핵심: 넛지의 단위는 표면이 아니라 event trigger이며 기본값은 "아무것도 띄우지 않음"; B-LOST에서만 후보가 되고 B-AVAIL/B-NORMAL/B-MISMATCH/first value 도달 경로 위에는 띄우지 않는다. J1/J2/J4=`deed_saved`, J3=`deed_judged` first value 매핑과 `deed_save_capped`=availability/friction 경계 계승. 신규 이벤트·속성·카피·tracking/privacy·PostHog dashboard·코드·배포·외부발송·비용·권한 변경 0. HTML 보고서 `<html`/`<body`/axis ax1/axis ax2/`<details` 포함 확인 + details에 계승한 기준·이번에 새로 배운 것·다음 Marketer 규칙·승격 후보 포함. MARKETING_LEARNINGS.md에 durable learning "Nudges Are Event-Triggered, And Show-Nothing Is The Default" 승격. Infinity dirty 무관 파일(EVALUATION_NOTES.md) staging 제외. L2 agent-approved push.) -->

<!-- marketing-39 completed 2026-06-04T23:08Z → reports/marketing-39/2026-06-04T2207Z-local.html [projects: virtue; type: strategy; topics: ai-trust,activation,onboarding] (Virtue Human-AI readiness trace map 작성 완료. 산출물은 virtue-rebirth-app `4ebf2a5`의 `apps/web/docs/human-ai-readiness-trace-map.md`(신규 1파일, docs-only). arXiv "From Accuracy to Readiness"와 Userpilot U-C-I 렌즈를 첫 10명 관찰 기준으로 번역해 outcome/reliance/safety/learning 4축과 U-C-I 질문을 J1~J4 first value 뒤 행동 흔적으로 매핑. 핵심 경계: `deed_saved`는 AI 판정 동의가 아니고, J3 judged-without-save는 정상 종료 가능하며, `deed_rerolled`는 불신만이 아니라 호기심/학습 행동일 수 있다. 신규 이벤트·속성·카피·tracking/privacy·PostHog dashboard·코드·배포·외부발송·비용·권한 변경 0. HTML 보고서 `<html`/`<body`/axis ax1/axis ax2/`<details` 포함 확인. MARKETING_LEARNINGS.md에 durable learning "Readiness Trace Over Accuracy" 승격. Infinity dirty 무관 파일(EVALUATION_NOTES.md) staging 제외. L2 agent-approved push.) -->

<!-- marketing-38 completed 2026-06-04T10:27Z → reports/marketing-38/2026-06-04T1007Z-local.html [projects: virtue; type: strategy; topics: ai-trust,activation,onboarding,prelaunch] (Virtue AI 판정 신뢰/제어권 관찰 경계표 작성 완료. 산출물은 virtue-rebirth-app의 `apps/web/docs/ai-judgment-trust-control-observation-boundary-table.md`(신규 1파일, docs-only). EY·McKinsey 2026 AI trust 렌즈를 J1~J4 첫 세션 관찰 기준으로 번역해, AI 판정을 "믿어라"가 아니라 "근거를 보고 사람이 마지막 선택을 한다"로 읽는 경계를 고정. J1/J2/J4=`deed_saved`, J3=`deed_judged` first value 매핑과 m24 trust calibration/60초 관찰 기준 계승. 기존 이벤트만 인용했고 신규 이벤트·속성·카피·tracking/privacy·dashboard·배포·외부발송·비용·권한 변경 0. HTML 보고서 `<html`/`<body`/axis ax1/axis ax2/`<details` 포함 확인. MARKETING_LEARNINGS.md에 durable learning "Trust Is Read Through Control, Not Agreement" 승격. Infinity dirty 무관 파일(EVALUATION_NOTES.md) staging 제외. Heartbeat가 partial timeout 후 산출물과 Archive 전환을 검증해 정리.) -->

<!-- research-11 completed 2026-06-04T00:27Z → intents/archive/research-11.md [projects: personal-brand,content-strategy,research-bank; type: research; topics: content,marketing,product] (1인 브랜드 전략 10개 실사례 조사 완료. 산출물은 artifacts/research-11/solo-brand-strategy-10-cases.md, HTML 보고서는 reports/research-11/2026-06-04T0007Z.html. 국내 3·해외 7 사례를 포지셔닝·반복 콘텐츠 폼·신뢰 자산·수익화/제품화 경로·사용자 적용 전략으로 정리. 핵심 패턴: 콘텐츠는 입구, 제품/교육/서비스가 본체, 같은 경험을 영상·글·코스·제품으로 변환해 재사용한다. 사용자 3축 적용은 유튜브=도달, 여행 중 앱 만들기=증거, AI 미니 워크샵=수익화/교육으로 한 깔때기를 만드는 방향. Levels·Danny Postma는 여행+AI/앱+공개빌딩 축과 가장 직접적으로 맞닿은 사례. 공개 발송·외부 제출·유료 도구·사용자 계정 액션·브랜드명/카피 확정 0. 코드·배포·외부 호출 변경 0. HTML 보고서 gate(`<html`, `<body`, `axis ax1`, `axis ax2`, `<details`) 통과. Claude fallback timeout 뒤 heartbeat가 관련 draft를 검증하고 Active→Archive 정리.) -->

<!-- marketing-37 completed 2026-06-03T22:07Z → reports/marketing-37/2026-06-03T2207Z-local.html [projects: virtue; type: strategy; topics: activation,retention,analytics] (Virtue activation-retention correlation readiness spec 작성 완료. 산출물은 virtue-rebirth-app `b5c0d2e`의 `apps/web/docs/activation-retention-correlation-readiness.md`(신규 1파일, docs-only). 핵심: m33의 A1~A4 activation 후보 묶음과 W-IMM/W-CONF window를 재정의하지 않고, 출시 후 retention 대조에 필요한 D7 우선/D30 보류 질문, X-MOCK/X-SYNTH/X-SELF/X-CAP/X-503 제외 조건, 읽기 전용 pseudo-query shape, prelaunch 금지선을 사전 등록. first value 매핑 J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106 계승, A3 미완료 정의는 `deed_judged` 부재로 고정해 judged−saved 갭을 이탈/묶음 미완료로 환산 금지. 신규 이벤트·속성·코드·카피·PostHog 설정·대시보드·tracking/privacy·배포·외부발송·비용·권한 변경 0. HTML 보고서 `<html`/`<body`/axis ax1/axis ax2/`<details` 포함 확인 + details에 계승한 기준·이번에 새로 배운 것·다음 Marketer 규칙·승격 후보 포함. MARKETING_LEARNINGS.md에 durable learning "Correlation Readiness Is A Separate Gate" 승격. Infinity dirty 무관 파일(EVALUATION_NOTES.md) staging 제외. L2 agent-approved push.) -->

<!-- marketing-36 completed 2026-06-03T10:07Z → reports/marketing-36/2026-06-03T1007Z-local.html [projects: virtue; type: strategy; topics: ai-agent,activation,measurement,prelaunch] (Virtue prelaunch 분석 Skill Sheet 작성 완료. 산출물은 virtue-rebirth-app의 `apps/web/docs/virtue-prelaunch-analysis-skill-sheet.md`(신규 1파일, docs-only). 핵심: prelaunch 판단 기준(4-Job taxonomy·first value 매핑·발화 이벤트 어휘+앵커·availability 분리·막힘 4분류·activation 측정 가능 상태·금지선 9개·코퍼스 소유 문서 지도)이 12개+ 문서에 분산돼 분석마다 재발견 비용이 드는 문제를, 읽기 전용 참조 1장에 인덱싱해 "참조 후 대조"로 전환. 시트는 새 결론을 만들지 않는 파생물이며 충돌 시 원본 file:line과 MARKETING_LEARNINGS.md가 우선. first value 매핑 J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106, `deed_save_capped`:167=availability/friction 계승. J3 judged−saved 갭=정상 종료 가능·저장 미강제, synthetic/mock/self-test 비결정 등급 보존. 이벤트 앵커 현행 일치(rg drift 0): add_flow_started:72·add_flow_abandoned:78·deed_judged:106·deed_judge_attempted:135·deed_rerolled:149·deed_save_capped:167·deed_saved:183·level_up_viewed:199. 가정 분리: 계승=원장 전 항목/변경=없음/충돌=0(시트는 파생물). 신규 이벤트·속성·카피·tracking/privacy·PostHog 설정·대시보드·세션리플레이·코드·배포·외부발송·비용·권한·개인정보 변경 0. 줄머리 conflict marker 0(단일 rg -c 매치는 §8 문서화된 검증 명령 줄), 코드 diff 0(`git diff --stat apps/web/src apps/ios` 빈 출력). source note는 로컬 부재 → rationale 요지만 근거(§9.3). HTML 보고서 `<html`/`<body`/axis ax1/axis ax2/`<details`(4) 포함 확인 + details에 계승한 기준·이번에 새로 배운 것·다음 Marketer 규칙·승격 후보 포함. MARKETING_LEARNINGS.md 승격 후보 "Prelaunch Analysis Skill Sheet As A Single Lookup"은 운영 절차 후보이자 단일 실행이라 report 안에 보류. Infinity dirty 무관 파일(EVALUATION_NOTES.md) staging 제외. L2 agent-approved push.) -->

<!-- marketing-35 completed 2026-06-02T23:07Z → reports/marketing-35/2026-06-02T2207Z-local.html [projects: virtue; type: strategy; topics: onboarding,activation,checklist] (Virtue 잡별 온보딩 체크리스트 감사표 작성 완료. 산출물은 virtue-rebirth-app의 `apps/web/docs/onboarding-checklist-audit-table.md`(신규 1파일, commit `a300095`). 핵심: 체크리스트는 first value 위치를 따라 잡별로 길이·종료점이 다르며 J1/J2/J4는 입력→판정→저장, J3는 입력→판정에서 종료하고 저장 강제는 DO-NOT-INCLUDE. 항목을 CL-ELIGIBLE/BUMPER-ONLY/CONTEXTUAL-FALLBACK/DO-NOT-INCLUDE 4분류로 나누고, 폴백은 B-LOST에만 발동하며 B-MISMATCH/B-AVAIL/B-NORMAL에는 발동하지 않도록 경계를 고정. first value 매핑 J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106 및 `deed_save_capped`:167=availability/friction 계승. 신규 이벤트·속성·카피·계측·대시보드·세션리플레이·코드·배포·외부발송·비용·권한 변경 0. HTML 보고서 `<html`/`<body`/axis ax1/axis ax2/`<details` 포함 확인 + details에 계승한 기준·이번에 새로 배운 것·다음 Marketer 규칙·승격 후보 포함. MARKETING_LEARNINGS.md 승격 후보는 단일 실행이라 report 안에 보류. Infinity dirty 무관 파일(EVALUATION_NOTES.md) staging 제외. L2 agent-approved push.) -->

<!-- marketing-34 completed 2026-06-02T11:07Z → reports/marketing-34/2026-06-02T1007Z-local.html [projects: virtue; type: strategy; topics: plg,activation,measurement] (Virtue PLG Foundation exit gate 문서 작성 완료. 산출물은 virtue-rebirth-app의 `apps/web/docs/plg-foundation-exit-gate.md`(신규 1파일). 핵심: Foundation 종료 조건은 "활성화가 좋다"가 아니라 first value 매핑, 후보 묶음/window, TTV 시작/종료점, D7 질문, baseline 양식, 이벤트 도착 검증, traffic/source+availability 분리까지 측정 가능한 상태인가로 고정. G1~G7 중 G6 도착 검증만 출시 후 확인 대기이며, Activation 진입 판단은 외부 벤치마크 수치가 아니라 데이터 품질·synthetic 제외·가용성 차단·같은 잡 재가치로 분리. first value 매핑 J1/J2/J4=`deed_saved`, J3=`deed_judged`, `deed_save_capped`=availability/friction, synthetic/mock/self-test 비결정 기준 계승. 신규 이벤트·속성·카피·계측·대시보드·코드·배포·외부발송·비용·권한 변경 0. HTML 보고서 `<html`/`<body`/axis ax1/axis ax2/`<details` 포함 확인. MARKETING_LEARNINGS.md에 durable learning "Measurement Readiness Is A Separate Gate" 승격. Infinity dirty 무관 파일(EVALUATION_NOTES.md) staging 제외. L2 agent-approved push.) -->

<!-- marketing-33 completed 2026-06-01T22:07Z → reports/marketing-33/2026-06-01T2207Z-local.html [projects: virtue; type: strategy; topics: activation,measurement,retention,prelaunch] (Virtue 활성화 후보 등록부 작성 완료. 산출물은 virtue-rebirth-app의 `apps/web/docs/activation-candidate-registry.md`(신규 1파일). PostHog 활성화 렌즈(단일 magic 이벤트 아닌 3~5 이벤트 묶음 + 제품별 window를 retention과 대조)를 Virtue J1~J4 잡별 후보 묶음·관찰 window를 출시 전에 동결(register)하는 내부 등록부로 번역. 핵심 가치: 흩어진 재료(m15 §4 묶음·m22 D7·m23 immediate vs long-term TTV·m10 time gap)는 이미 충분하나, 출시 후 작은 데이터로 묶음·window를 사후에 입맛대로 고르는(cherry-pick) 위험을 막기 위해 묶음(A1~A4)과 window(W-IMM 첫 세션/W-CONF D7)를 등록 단위로 고정 → 검증을 "조립"이 아닌 "등록 후보 대조"로 전환. §2 등록부 심장표=J1~J4 × (등록 ID · first value(계승) · 후보 묶음 3~5(완료 이벤트 우선) · 관찰 window · 사용 가능 기존 이벤트 · 수기 관찰 칸 · 금지 해석) 한 표에 성공기준 6요소 수렴. A3(J3)만 `deed_judged`:106이 first value라 묶음에 `deed_saved` 필수 등록 안 함(저장 없는 종료=정상, judged−saved 갭 이탈 단정 금지). §3 window 정의(W-IMM/W-CONF)는 m23 immediate vs long-term TTV와 정렬, 새 정의 0, availability(503·지연·`deed_save_capped`:167 early return) 구간 window 제외. §4 출시 후 게이트(10명 OR 7일)+등록 ID별 체크리스트는 "등록 후보를 데이터로 대조 가능한가"만 확인, 전환율/리텐션 상관 결론 보류. 역할 분리: 플랫폼 패리티는 m15에, 운영 리듬은 m23에, 정밀 time gap은 m10에 위임(재정의 0). first value 매핑 J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106 그대로 계승. 기존 6 발화 이벤트만 인용(앵커 72/106/149/167/183/199 현행 일치 drift 0), 신규 이벤트/속성 0. 선행 7문서(jtbd-matrix/ios-parity/retention-predictive/onboarding-metrics/ttv-brief/baseline)+copy-spec 충돌 0. 출처노트 `source/external-links/marketing/2026-06-01-activation-metric-bundles.md`는 로컬 부재(`source/` 트리 자체 없음) → Intent rationale 요지+검증된 m15 §4 근거임을 §0에 명시. 검증 게이트 PASS: 코드 diff 0(`git diff --stat apps/web/src apps/ios/Sources` 빈 출력), git status=docs 1파일만, 실제 conflict marker 0(line-start 정규식 NONE, 단일 grep 매치는 §8 문서화된 검증 명령 줄), HTML 보고서 `<html`/`<body`/axis ax1/axis ax2/`<details`(3) 포함 + details에 계승한 기준·이번에 새로 배운 것·다음 Marketer 규칙·승격 후보 포함. durable 승격은 단일 등록부 1건이라 다음 실사용 대조 후로 보류(기존 First Value Mapping·Prelaunch Decision Boundary 기준에 흡수 가능). Infinity dirty 무관 파일(EVALUATION_NOTES.md) staging 제외. L2 agent-approved push.) -->

<!-- marketing-32 completed 2026-06-01T10:07Z → reports/marketing-32/2026-06-01T1007Z-local.html [projects: virtue; type: strategy; topics: onboarding,activation,ai-product,prelaunch] (Virtue 첫 입력 기본값/예시/placeholder 감사표 작성 완료. 산출물은 virtue-rebirth-app의 `apps/web/docs/first-input-defaults-prompt-audit.md`(신규 1파일). Amplitude agent default-prompt 렌즈(출처노트 `source/external-links/marketing/2026-06-01-agent-default-prompts-retention.md`)를 Virtue `/add` 첫 입력 유도의 잡별 내부 감사로 번역. §1 인벤토리 D1~D9를 file:line으로 고정. §2 심장표 J1~J4 × (이 잡을 부르는 기본값 D-코드 · 조향 강도 · 좋은 후속 first value 이벤트 · 잘못된 모드 위험 · 관찰 손기록 질문). 핵심 발견: Virtue 첫 입력 기본값은 "질문형 placeholder + 빈 슬롯" 단일 패턴. first value 매핑 J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106 그대로 계승, 재정의 0. 인용 이벤트 현행 일치 drift 0. 선행 6문서+copy-spec 충돌 0. 검증 게이트 PASS. durable learning "First-Input Defaults Steer The Job"를 MARKETING_LEARNINGS.md에 승격. Infinity dirty 무관 파일(EVALUATION_NOTES.md) staging 제외. L2 agent-approved push.) -->

<!-- marketing-31 completed 2026-05-31T23:07Z → reports/marketing-31/2026-05-31T2307Z-local.html [projects: virtue; type: strategy; topics: onboarding,activation,jtbd,prelaunch] (Virtue 첫 세션 제품 본체/범퍼 경계표 작성 완료. 산출물은 virtue-rebirth-app의 `apps/web/docs/product-body-vs-bumper-boundary-table.md`(신규 1파일). PLG 온보딩 렌즈를 Virtue 첫 세션 표면 4개의 잡별 본체/범퍼 분류로 번역. first value 매핑 J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106 계승. durable learning "Product Body vs Bumper By Job"를 MARKETING_LEARNINGS.md에 승격. L2 agent-approved push.) -->

<!-- marketing-30 completed 2026-05-31T10:07Z → reports/marketing-30/2026-05-31T1007Z-local.html [projects: virtue; type: strategy; topics: onboarding,activation,ai-product,prelaunch] (Virtue 첫 결과 공유성 판독 기준 작성 완료. 산출물은 virtue-rebirth-app의 `apps/web/docs/shareworthy-first-result-observation-criteria.md`(신규 1파일). durable learning "Shareworthiness Is A Separate Axis"를 MARKETING_LEARNINGS.md에 승격. L2 agent-approved push.) -->

<!-- marketing-29 completed 2026-05-30T22:07Z → reports/marketing-29/2026-05-30T2207Z-local.html [projects: virtue; type: strategy; topics: ai-product,activation,trust,measurement,prelaunch] (Virtue AI outcome proxy 사전 작성 완료. 산출물은 virtue-rebirth-app `22f3aea`의 `apps/web/docs/ai-outcome-proxy-dictionary.md`(신규 1파일). L2 agent-approved push 정상 fast-forward(c0dcf7d→22f3aea). Legacy Markdown log도 보존.) -->

<!-- marketing-28 completed 2026-05-30T10:07Z → reports/marketing-28/2026-05-30T1007Z-local.html [projects: virtue; type: strategy; topics: monetization,pricing,activation,prelaunch] (Virtue prelaunch 유료화 경계 브리프 작성 완료. 산출물은 virtue-rebirth-app `c0dcf7d`의 `apps/web/docs/prelaunch-monetization-boundary-brief.md`(신규 1파일, 136줄). L2 agent-approved push 정상 fast-forward.) -->

<!-- marketing-27 completed 2026-05-29T22:25Z → reports/marketing-27/2026-05-29T2225Z-local.md [projects: virtue; type: strategy; topics: positioning,messaging,activation,prelaunch] (Virtue 첫 사용자 메시지 혼란 로그 작성 완료. 산출물은 virtue-rebirth-app `f69f309`의 `apps/web/docs/first-user-message-confusion-log.md`(신규 1파일, 159줄). L2 agent-approved push 정상 fast-forward.) -->

<!-- marketing-26 completed 2026-05-29T11:07Z → intents/archive/marketing-26.md [projects: virtue; type: strategy; topics: retention,habit,recovery,copy] (Virtue recovery-over-streak 리텐션 렌즈 작성 완료. 산출물은 virtue-rebirth-app `7372aab`의 `apps/web/docs/recovery-over-streak-retention-lens.md`(신규 1파일, 166줄). L2 agent-approved push 정상 fast-forward.) -->

<!-- marketing-25 completed 2026-05-28T22:07Z → intents/archive/marketing-25.md [projects: virtue; type: strategy; topics: onboarding,analytics,activation,ai-agents] (Virtue human/test/agent 트래픽 판독 경계표 작성 완료. 산출물은 virtue-rebirth-app `f5fde73`의 `apps/web/docs/traffic-source-reading-boundary-table.md`(신규 1파일, 177줄). L2 agent-approved push 정상 fast-forward.) -->

<!-- marketing-24 completed 2026-05-28T10:07Z → intents/archive/marketing-24.md [projects: virtue; type: strategy; topics: activation,trust,ai-product,onboarding] (Virtue AI 판정 신뢰 보정 감사표 작성 완료. 산출물은 virtue-rebirth-app `c3afb52`의 `apps/web/docs/ai-judgment-trust-calibration-audit.md`(신규 1파일, 136줄). L2 agent-approved push 정상 fast-forward.) -->

<!-- research-10 completed 2026-05-28T16:07Z → intents/archive/research-10.md [projects: knowledge-lab,infinity; type: research; topics: content,wiki] (PC·인터넷 시대 전환사 리서치 완료. 산출물은 artifacts/research-10/pc-internet-transition-history.md.) -->

<!-- marketing-23 completed 2026-05-27T22:07Z → intents/archive/marketing-23.md [projects: virtue; type: strategy; topics: activation,retention,analytics] (Virtue 온보딩 지표 운영 판독표 작성 완료. 산출물은 virtue-rebirth-app `808231c`의 `apps/web/docs/onboarding-metrics-reading-table.md`(신규 1파일, 168줄). L2 agent-approved push 정상 fast-forward.) -->

<!-- marketing-22 completed 2026-05-27T10:07Z → intents/archive/marketing-22.md (Virtue 리텐션 예측 활성화 브리프 작성 완료. 산출물은 virtue-rebirth-app `179ca70`의 `apps/web/docs/retention-predictive-activation-brief.md`(신규 1파일, 166줄). L2 agent-approved push 정상 fast-forward.) -->

<!-- marketing-21 completed 2026-05-26T22:07Z → intents/archive/marketing-21.md (Virtue `/add` 입력-결과 균형 감사표 작성 완료. 산출물은 virtue-rebirth-app `95cc836`의 `apps/web/docs/add-input-output-balance-audit.md`(신규 1파일). L2 agent-approved push 정상 fast-forward.) -->

<!-- marketing-20 completed 2026-05-26T15:07Z → intents/archive/marketing-20.md (Virtue 첫 60초 가치 관찰 스크립트 작성 완료. 산출물은 virtue-rebirth-app `993547f`의 `apps/web/docs/first-60-second-value-observation-script.md`(신규 1파일, 248줄). L2 agent-approved push 정상 fast-forward.) -->

<!-- marketing-19 completed 2026-05-26T10:07Z → intents/archive/marketing-19.md (Virtue 신규 사용자 홈 화면 FAE 감사표 작성 완료. 산출물은 virtue-rebirth-app `3d90648`의 `apps/web/docs/home-screen-fae-audit.md`(신규 1파일). L2 agent-approved push 정상 fast-forward.) -->

<!-- marketing-18 completed 2026-05-26T00:07Z → intents/archive/marketing-18.md (Virtue AEO / Agent-ready 공개 표면 감사표 작성 완료. 산출물은 virtue-rebirth-app `f74cf59`의 `apps/web/docs/aeo-agent-ready-surface-audit.md`(신규 1파일). L2 agent-approved push 정상 fast-forward.) -->

<!-- marketing-17 completed 2026-05-25T22:07Z → intents/archive/marketing-17.md (Virtue 첫 세션 정성 마찰 관찰 프로토콜 작성 완료. 산출물은 virtue-rebirth-app `2a8c694`의 `apps/web/docs/first-session-friction-observation-protocol.md`(신규 +289). L2 agent-approved push 정상 fast-forward.) -->

<!-- research-09 completed 2026-05-25T12:30Z → intents/archive/research-09.md (1인기업 강점 살리기 vs 한계 조기 규정 리서치. 산출물 artifacts/research-09/solopreneur-strength-vs-limits.md, 보고서 reports/research-09/2026-05-25T1230Z.html.) -->

<!-- marketing-16 completed 2026-05-25T10:07Z → intents/archive/marketing-16.md (Virtue 첫 세션 3-스크린 가치 경로 감사표 작성 완료. 산출물은 virtue-rebirth-app `87b8877`의 `apps/web/docs/three-screen-value-path-audit.md`. L2 agent-approved push.) -->

<!-- marketing-15 completed 2026-05-24T22:07Z → intents/archive/marketing-15.md (Virtue 웹/iOS 활성화 이벤트 패리티 브리프 작성 완료. 산출물은 virtue-rebirth-app `10e3fa2`의 `apps/web/docs/ios-activation-event-parity-brief.md`. L2 agent-approved push.) -->

<!-- marketing-14 completed 2026-05-24T15:56Z → intents/archive/marketing-14.md (Virtue 첫 주 활성화-리텐션 연결표 작성 완료. 실제 산출물은 이미 virtue-rebirth-app `ff6a769`로 push되어 있었고 Infinity 상태만 Waiting에 남아 있던 것을 정리.) -->

<!-- marketing-13 completed 2026-05-23T22:07Z → intents/archive/marketing-13.md (Virtue 경쟁 대안 기반 포지셔닝 브리프. 산출물은 virtue-rebirth-app dc0ce55의 `apps/web/docs/competitive-alternatives-positioning-brief.md`. L2 agent-approved push.) -->

<!-- marketing-10 completed 2026-05-23T16:07Z → intents/archive/marketing-10.md (Virtue Time-to-Value 관찰 기준표. 산출물은 virtue-rebirth-app c32033f의 docs/time-to-value-observation-brief.md.) -->

<!-- marketing-12 completed 2026-05-23T10:18Z → intents/archive/marketing-12.md (Virtue 활성화 경로 마찰 감사표. 산출물은 virtue-rebirth-app fc08cf4의 docs/activation-path-friction-audit.md.) -->

<!-- research-08 completed 2026-05-23T10:30Z → intents/archive/research-08.md (GEO/LLMO 체크리스트 조사 완료.) -->

<!-- marketing-11 completed 2026-05-22T22:17Z → intents/archive/marketing-11.md (Virtue 첫 실사용자 기준선 템플릿. 산출물은 virtue-rebirth-app ebd5781의 docs/first-real-user-baseline-template.md.) -->

<!-- marketing-09 completed 2026-05-21T22:07Z → intents/archive/marketing-09.md (Virtue 활성화 마일스톤 사다리. docs/activation-milestone-ladder.md 추가.) -->

<!-- marketing-01 completed 2026-05-21T10:17Z → intents/archive/marketing-01.md (Virtue add-flow telemetry 승인 처리: `marketing-01-add-flow-telemetry` b28d01f를 master에 fast-forward 머지/push, Kubernetes `deployment/virtue-rebirth` rollout restart 완료.) -->

<!-- marketing-08 completed 2026-05-21T10:07Z → intents/archive/marketing-08.md (Virtue PMF 응답 분석 루브릭. docs/pmf-response-analysis-rubric.md 추가.) -->

<!-- marketing-07 completed 2026-05-20T22:07Z → intents/archive/marketing-07.md (Virtue 최소 생존 오디언스 기준표. docs/minimum-viable-audience-brief.md 추가.) -->

<!-- marketing-06 completed 2026-05-20T10:07Z → intents/archive/marketing-06.md (Virtue 첫 세션 JTBD 매트릭스. docs/first-session-jtbd-matrix.md sha 38af1be.) -->

<!-- marketing-05 completed 2026-05-19T22:07Z → intents/archive/marketing-05.md (Virtue 빈 상태/첫 행동 감사표.) -->

<!-- marketing-04 completed 2026-05-19T10:07Z → intents/archive/marketing-04.md (Virtue 첫인상 포지셔닝 스냅샷.) -->

<!-- marketing-03 completed 2026-05-18T22:20Z → intents/archive/marketing-03.md (Virtue 첫 7일 deed_saved 루프 정의서 작성.) -->

<!-- marketing-02 completed 2026-05-16T14:00Z → intents/archive/marketing-02.md (마찰점 4개 특정, 개선 후보 3개 초안, 로컬 실행 프롬프트 작성.) -->

<!-- research-07 completed 2026-05-13T12:00 → intents/archive/research-07.md -->

<!-- product-01 completed 2026-05-15T11:44Z → intents/archive/product-01.md (Virtue 최신 상태, 후속 개선은 별도 Intent로 분리.) -->

<!-- build-02 completed 2026-05-13 → intents/archive/build-02.md (https://infinity.oracle.shdkej.com 배포 완료.) -->

<!-- research-06 completed 2026-05-05T08:00 → intents/archive/research-06.md -->

<!-- wiki-05 completed 2026-04-25T09:00 → intents/archive/wiki-05.md -->

<!-- wiki-04 completed 2026-04-25T10:15 → intents/archive/wiki-04.md -->

<!-- wiki-02 completed 2026-04-19T02:45 → intents/archive/wiki-02.md -->
<!-- wiki-03 completed 2026-04-20T13:30 → intents/archive/wiki-03.md -->
<!-- research-05 completed 2026-04-21T00:00 → intents/archive/research-05.md -->
<!-- wiki-01 completed 2026-04-21T00:00 → intents/archive/wiki-01.md -->
<!-- build-01 completed 2026-04-21T00:30 → intents/archive/build-01.md -->
<!-- research-05 re-run completed 2026-04-23T10:00 → intents/archive/research-05.md (3차) -->
