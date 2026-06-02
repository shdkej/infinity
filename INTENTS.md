# Intent Registry

> Heartbeat Agent가 주기적으로 읽고 실행하는 의도 목록.

## Inbox


## Active

### marketing-34 — Virtue PLG Foundation exit gate 문서

- status: active
- priority: medium
- permission: L1/L2 internal-doc only
- mode: prepare (cloud done) → execute_local
- goal: `apps/web/docs/plg-foundation-exit-gate.md` 한 장 추가 — Foundation→Activation 전환 기준을 잠그는 exit gate 체크리스트
- success_criteria:
  - apps/web/docs/에 Foundation exit gate 문서 생성
  - 기존 first value/activation candidate/baseline/TTV/D7 문서만 인용
  - 신규 이벤트·속성·카피·계측·대시보드 0
  - 외부 벤치마크 수치를 Virtue 합격선으로 쓰지 않음
  - conflict marker 0, git diff doc/report 범위에만
- context: virtue-rebirth-app `apps/web/docs/`
- draft: artifacts/marketing-34/plg-foundation-exit-gate-draft.md
- prepare_report: reports/marketing-34/2026-06-02T0000Z-prepare.html
- next: 로컬 Claude Code가 초안 기반으로 docs 파일 생성 → 검증 게이트 PASS → 커밋·push → Heartbeat HTML report 후 archive

## Waiting

<!-- 사용자 결정, 외부 조건, 안전 확인 대기. 같은 질문을 반복하지 않고 상태만 보존한다. -->

## Archive

<!-- marketing-33 completed 2026-06-01T22:07Z → reports/marketing-33/2026-06-01T2207Z-local.html [projects: virtue; type: strategy; topics: activation,measurement,retention,prelaunch] (Virtue 활성화 후보 등록부 작성 완료. 산출물은 virtue-rebirth-app의 `apps/web/docs/activation-candidate-registry.md`(신규 1파일). PostHog 활성화 렌즈(단일 magic 이벤트 아닌 3~5 이벤트 묶음 + 제품별 window를 retention과 대조)를 Virtue J1~J4 잡별 후보 묶음·관찰 window를 출시 전에 동결(register)하는 내부 등록부로 번역. 핵심 가치: 흔어진 재료(m15 §4 묶음·m22 D7·m23 immediate vs long-term TTV·m10 time gap)는 이미 충분하나, 출시 후 작은 데이터로 묶음·window를 사후에 입맛대로 고르는(cherry-pick) 위험을 막기 위해 묶음(A1~A4)과 window(W-IMM 첫 세션/W-CONF D7)를 등록 단위로 고정 → 검증을 "조립"이 아닌 "등록 후보 대조"로 전환. §2 등록부 심장표=J1~J4 × (등록 ID · first value(계승) · 후보 묶음 3~5(완료 이벤트 우선) · 관찰 window · 사용 가능 기존 이벤트 · 수기 관찰 칸 · 금지 해석) 한 표에 성공기준 6요소 수렴. A3(J3)만 `deed_judged`:106이 first value라 묶음에 `deed_saved` 필수 등록 안 함(저장 없는 종료=정상, judged−saved 갅 이탈 단정 금지). §3 window 정의(W-IMM/W-CONF)는 m23 immediate vs long-term TTV와 정렬, 새 정의 0, availability(503·지연·`deed_save_capped`:167 early return) 구간 window 제외. §4 출시 후 게이트(10명 OR 7일)+등록 ID별 체크리스트는 "등록 후보를 데이터로 대조 가능한가"만 확인, 전환율/리텐션 상관 결론 보류. 역할 분리: 플랫폼 패리티는 m15에, 운영 리듬은 m23에, 정밀 time gap은 m10에 위임(재정의 0). first value 매핑 J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106 그대로 계승. 기존 6 발화 이벤트만 인용(앤커 72/106/149/167/183/199 현행 일치 drift 0), 신규 이벤트/속성 0. 선행 7문서(jtbd-matrix/ios-parity/retention-predictive/onboarding-metrics/ttv-brief/baseline)+copy-spec 충돌 0. 출처노트 `source/external-links/marketing/2026-06-01-activation-metric-bundles.md`는 로컈 부재(`source/` 트리 자체 없음) → Intent rationale 요지+검증된 m15 §4 근거임을 §0에 명시. 검증 게이트 PASS: 코드 diff 0(`git diff --stat apps/web/src apps/ios/Sources` 빈 출력), git status=docs 1파일만, 실제 conflict marker 0(line-start 정규식 NONE, 단일 grep 매치는 §8 문서화된 검증 명령 줄), HTML 보고서 `<html`/`<body`/axis ax1/axis ax2/`<details`(3) 포함 + details에 계승한 기준·이번에 새로 배운 것·다음 Marketer 규칙·승격 후보 포함. durable 승격은 단일 등록부 1건이라 다음 실사용 대조 후로 보류(기존 First Value Mapping·Prelaunch Decision Boundary 기준에 흡수 가능). Infinity dirty 무관 파일(EVALUATION_NOTES.md) staging 제외. L2 agent-approved push.) -->

<!-- marketing-32 completed 2026-06-01T10:07Z → reports/marketing-32/2026-06-01T1007Z-local.html [projects: virtue; type: strategy; topics: onboarding,activation,ai-product,prelaunch] (Virtue 첫 입력 기본값/예시/placeholder 감사표 작성 완료. 산출물은 virtue-rebirth-app의 `apps/web/docs/first-input-defaults-prompt-audit.md`(신규 1파일). Amplitude agent default-prompt 렌즈(출처노트 `source/external-links/marketing/2026-06-01-agent-default-prompts-retention.md`)를 Virtue `/add` 첫 입력 유도의 잡별 내부 감사로 번역. §1 인벤토리 D1~D9를 file:line으로 고정(홈 `page.tsx:67/111/128-129`, `/add` 사진 슬롯 `add/page.tsx:253-254`, 메모 라벨 `:271`·placeholder `뛭 했어요? 한 줄이면 충분해요.` `:277`, 판정 버튼 `AI 채점`/`임시 판정` `:29,300`, 결과 헤더 `:30,319`, 하단 힌트 `:407-408`) + 부재 항목 명시(예시 덕행·추천 질문/suggested prompt·카테고리 치프·pre-fill·기능 설명형 프롬프트 모두 없음). §2 심장표 J1~J4 × (이 잡을 부르는 기본값 D-코드 · 조향 강도 · 좋은 후속 first value 이벤트 · 잘못된 모드 위험 · 관찰 손기록 질문). 핵심 발견: Virtue 첫 입력 기본값은 "질문형 placeholder + 빈 슬롯" 단일 패턴이라 support-bot 유도 위험 0(출처노트 권고와 우연 정렬)이나 잡별 조향도 0 — 같은 중립 D6(`뛭 했어요?`)이 J1~J4를 구분 없이 부름. 첫 입력 단계에서 가장 약하게 불리는 잡은 J3(AI 약속이 `/add` 안에서야, 그것도 ai 모드에서만 등장)·J2(누적 보상은 두 번째 저장 이후). 환경 분기 `IS_AI_MODE`(`add/page.tsx:28-30`) mock 모드 `임시 판정` 라벨이 J3 첫 인상을 낙임(코드 사실, 변경 제안 아님). §3 "두 번째 메시지"를 잡별 두 번째 행동으로 번역(J1/J4=`deed_saved`, J2=`level_up_viewed`/두 번째 저장, J3=`deed_rerolled`/다른 입력 후 재판정=저장 강요 안 함) + 손기록 칸 후보(첫 입력 출처·후속 행동)는 기존 baseline/60초 관찰 양식 재사용(신규 속성 0). §4 prelaunch 금지선(전환율/activation/retention%/PMF/벤치마크 환산·1명 단정·J3 judged−saved 갅=가치부재·cap/503/지연=friction·synthetic/mock 혼입·mock 세션 J3를 ai J3로 합산·변경 금지). §5 proposal-only(J3 전용 무저장 흐름·잡별 예시 조향·mock 라벨 정책)는 관찰 후 별도 Intent. first value 매핑 J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106 그대로 계승, 재정의 0. 인용 이벤트 `deed_judged`/`deed_rerolled`:149/`deed_saved`/`deed_save_capped`:167/`level_up_viewed`:199 현행 일치 drift 0. 선행 6문서(jtbd-matrix/input-output-balance/home-screen-fae/three-screen/shareworthy/product-body-vs-bumper)+copy-spec 충돌 0. 검증 게이트 PASS: 코드 diff 0(doc 1파일만), 신규 이벤트/속성 0, conflict marker 0, source note·first value 매핑 인용 확인, HTML 보고서 `<html`/`<body`/axis ax1/axis ax2/`<details` 포함 + details에 계승한 기준·이번에 새로 배운 것·다음 Marketer 규칙·승격 후보 포함. durable learning "First-Input Defaults Steer The Job"를 MARKETING_LEARNINGS.md에 승격. Infinity dirty 무관 파일(EVALUATION_NOTES.md) staging 제외. L2 agent-approved push.) -->

<!-- marketing-31 completed 2026-05-31T23:07Z → reports/marketing-31/2026-05-31T2307Z-local.html [projects: virtue; type: strategy; topics: onboarding,activation,jtbd,prelaunch] (Virtue 첫 세션 제품 본체/범퍼 경계표 작성 완료. 산출물은 virtue-rebirth-app의 `apps/web/docs/product-body-vs-bumper-boundary-table.md`(신규 1파일). PLG 온보딩("제품이 첫 가치를 만들고 범퍼는 이탈 지점만 돕는다")를 Virtue 첫 세션 표면 4개(S1 `/` 홈·S2 `/add` 입력·S3 결과 카드·S4 저장 후 홈 복귀)의 잡별 본체/범퍼 분류로 번역. §1 본체/범퍼 정의+3원칙(같은 표면이 잡별로 부호 뒤집힌·본체 약하면 범퍼로 못 가림·잠못 붙인 범퍼는 본체 방해). §2 막품 4분류 B-LOST(길 잏음=범퍼)·B-MISMATCH(결과 불일치=제품)·B-AVAIL(가용성)·B-NORMAL(정상 종료, 이탈 아님). §3 심장표 J1~J4 × S1~S4 × 본체/범퍼 역할 × 정상 종료 읽기 × 막품 읽기(B-코드). 핵심: J1/J2/J4는 S4(저장 후 홈)가 본체, J3는 S3(결과 카드)가 본체이고 S4(저장)는 범퍼(선택)이라 저장 유도 범퍼를 무조건 붙이면 J3 첫 가치 흐름 방해. 홈은 J2에는 본체(누적 payoff)·J1에는 범퍼(다음 행동 안내). §5 라우팅 규칙(먼저 B-AVAIL 분리→J3 미저장 B-NORMAL→남은 막품 B-LOST vs B-MISMATCH). first value 매핑 J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106(저장 없이 닫힌=정상) 그대로 계승, 재정의 0. 기존 6 발화 이벤트만 인용(앤커 72/78/106/149/167/183/199 현행 일치 drift 0), `deed_save_capped`:167=availability/friction(upgrade 환산 금지) 계승. 선행 6문서(jtbd-matrix/three-screen/input-output-balance/onboarding-metrics/friction-protocol/proxy-dictionary)+copy-spec 충돌 0, J3 저장 없는 first value 충돌 0. 검증 게이트 PASS: conflict marker 0, virtue 코드 diff 0(doc 1파일만), 신규 이벤트/속성/카피/배포/외부발송 0, HTML 보고서 <html/<body/axis ax1/axis ax2/<details 포함 + details에 계승한 기준·이번에 새로 배운 것·다음 Marketer 규칙·승격 후보 포함. durable learning "Product Body vs Bumper By Job"를 MARKETING_LEARNINGS.md에 승격. L2 agent-approved push.) -->

<!-- marketing-30 completed 2026-05-31T10:07Z → reports/marketing-30/2026-05-31T1007Z-local.html [projects: virtue; type: strategy; topics: onboarding,activation,ai-product,prelaunch] (Virtue 첫 결과 공유성 판돁 기준 작성 완료. 산출물은 virtue-rebirth-app의 `apps/web/docs/shareworthy-first-result-observation-criteria.md`(신규 1파일). ProductLed AI 온보딩 렌즈의 세 신호 중 ④ "공유하거나 추천하고 싶은 첫 경험"만 잡별로 번역(① 60초 가치·② 입력 대비 결과 강도는 m20/m21이 이미 소유). 핵심 신규 판돁: 공유성(shareworthiness)을 first value·acceptance와 구분되는 별도 축(resonance/advocacy)으로 정의 — "첫 결과"를 (a)가치 도달 (b)공유성 (c)저장 후 누적 payoff 세 층으로 분리. 저장 없이 공유성 있음(J3 결과 읽고 보여 주고 닫음=정상)·저장 있으나 공유성 없음(J1 묵묵한 저장) 모두 가능하으므로 공유성은 항상 저장 전 시점에서 따로 기록. §2 행동 증거 사전 B1~B6(웃음/놀람/반박/다르게 보기 재시도/보여 주기/재전달) 중 B4만 on-instrument(`deed_rerolled`:149), 나머지 5종 off-instrument → 저장수·재판정수로 공유성 환산 금지, 손기록 전용. §3 심장표 J1~J4 × first value × 공유성 관찰 순간 × 기대 행동 증거 × 누적 payoff 분리 × 기존 이벤트 매핑 × misread. §4 Inform/Guide/Execute/Orchestrate 감사: `/add`는 `deed_judged`:106 결과 카드 생성으로 이미 Execute 도달(기존 증거), 단 Execute≠자동 shareworthy이고 그 손기록 양식 부재가 본 문서 공백. first value 매핑 J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106 그대로 계승, 재정의 0. 기존 6 발화 이벤트만 인용(앤커 72/106/149/167/183/199 drift 0), `deed_save_capped`:167은 availability/friction(upgrade 환산 금지) 계승. §5 prelaunch 금지선(전환율/PMF/벤치마크 산출·1명 단정·저장수=공유성 환산·cap=공유/upgrade 신호·J3 judged−saved 갅=가치 부재·synthetic 혼입·신규 이벤트/코드/카피/계측/배포/외부발송/비용/시크릿/권한/개인정보 변경 금지). §6 계승/변경/충돌/승격 분리: 선행 6문서(jtbd-matrix/proxy-dictionary/input-output-balance/60s-script/monetization-boundary/copy-spec) 충돌 0. 검증 게이트 PASS: conflict marker 0, virtue 코드 diff 0(doc 1파일만), HTML 보고서 <html/<body/axis ax1/axis ax2/<details 포함 + details에 계승한 기준·이번에 새로 배운 것·다음 Marketer 규칙·승격 후보 포함, HEAD==origin/master. 신규 이벤트·속성·코드·카피·계측·대시보드·세션리플레이·배포·외부발송·비용·시크릿·권한·개인정보 변경 0. durable learning "Shareworthiness Is A Separate Axis"를 MARKETING_LEARNINGS.md에 승격. Infinity EVALUATION_NOTES.md는 staging 제외. L2 agent-approved push.) -->

<!-- marketing-29 completed 2026-05-30T22:07Z → reports/marketing-29/2026-05-30T2207Z-local.html [projects: virtue; type: strategy; topics: ai-product,activation,trust,measurement,prelaunch] (Virtue AI outcome proxy 사전 작성 완료. 산출물은 virtue-rebirth-app `22f3aea`의 `apps/web/docs/ai-outcome-proxy-dictionary.md`(신규 1파일). Intercom outcome-based value framing + Reforge North Star quality 렌즈를 Virtue prelaunch 내부 판돁 사전으로 번역해, "AI가 무언가 했다"는 활동량과 "사용자가 인정했는가"라는 사용자 인정 가치 proxy를 분리. §1 proxy type 5종 사전(activity/acceptance/curiosity/friction/retention) 정의. §2 심장표1=6개 발화 이벤트 × 지배적 proxy type × quality condition × misread warning(코드 앤커 72/106/149/167/183/199 인용). §3 심장표2=J1~J4 × 이벤트 × proxy 판돁 × quality condition × misread warning, 같은 `deed_judged`가 J3에는 curiosity first value·다른 잡에는 통과점으로 부호 전환. §4 misread 7종(활동량=가치, judged−saved 갅=이탈, cap=유료수요, reroll=불신, level_up 1회=리텐션, 저장수=만족도, synthetic=인정 금지). §5 prelaunch decision-grade 금지선(전환율/PMF/벤치마크 산출·1명 단정·activity 승격·cap monetization 환산 금지). first value 매핑 J1/J2/J4=`deed_saved`, J3=`deed_judged` 그대로 계승, 재정의 0. 기존 6 발화 이벤트만 인용(보조 add_flow_abandoned:78·deed_judge_attempted:135 사실만 참조, 신규 invented 0). 선행 m06/m28/m25/m22/copy-spec 충돌 0. 신규 이벤트·속성·코드·카피·계측·대시보드·세션리플레이·공개카피·배포·외부발송·비용·시크릿·권한·개인정보 변경 0. 검증 게이트 7종 PASS: 코드 diff 0, 신규 이벤트/속성 0, 6개 이벤트 이름 drift 0(started6/judged13/saved21/level_up8/rerolled5/capped7), conflict marker 0, first-value 매핑 1, decision-grade 금지선 포함, HEAD==origin/master. Infinity dirty 무관 파일(EVALUATION_NOTES.md·workflows/heartbeat.md) staging 제외. L2 agent-approved push 정상 fast-forward(c0dcf7d→22f3aea). Legacy Markdown log도 보존.) -->

<!-- marketing-28 completed 2026-05-30T10:07Z → reports/marketing-28/2026-05-30T1007Z-local.html [projects: virtue; type: strategy; topics: monetization,pricing,activation,prelaunch] (Virtue prelaunch 유료화 경계 브리프 작성 완료. 산출물은 virtue-rebirth-app `c0dcf7d`의 `apps/web/docs/prelaunch-monetization-boundary-brief.md`(신규 1파일, 136줄). Stripe PLG pricing 2026/Growth Unhinged monetization source note를 Virtue prelaunch 내부 경계표로 번역해, J1~J4별 first value 이전 do-not-lock 제한과 first value 이후 확장/유료화 trigger candidate를 분리. first value 매핑은 J1/J2/J4=`deed_saved`, J3=`deed_judged` 그대로 계승, 재정의 0. 핵심 경계: 가격·플랜·금액 결정 0, 첫 가치 이전 결제정보/계정강제/핵심행동 0회 잊금 금지, §3 후보는 반복 가치 관찰 전 확정/구현 금지. `deed_save_capped`는 30덕 상한 early-return으로 `deed_saved` 미발화하는 availability/friction 신호이며 monetization intent/upgrade demand로 환산 금지. 공개 가격표·결제 연동·트래킹 변경·paywall 실험·트리거 확정·배포·외부발송·비용·시크릿·권한 변경은 Waiting/approval-needed로 명시. 신규 이벤트·코드·카피·결제·트래킹·대시보드·세션리플레이·배포·외부발송·비용·시크릿·권한·개인정보 변경 0. 검증: doc-only diff, 코드 diff 0, conflict marker 0, HEAD==origin/master. L2 agent-approved push 정상 fast-forward. Legacy Markdown log도 보존.) -->

<!-- marketing-27 completed 2026-05-29T22:25Z → reports/marketing-27/2026-05-29T2225Z-local.md [projects: virtue; type: strategy; topics: positioning,messaging,activation,prelaunch] (Virtue 첫 사용자 메시지 혼란 로그 작성 완료. 산출물은 virtue-rebirth-app `f69f309`의 `apps/web/docs/first-user-message-confusion-log.md`(신규 1파일, 159줄). Wynter/April Dunford 포지셔닝 혼란 렌즈를 Virtue prelaunch 내부 관찰표로 축소해, 사용자가 붙인 제품명/대체재·되물은 문장·가장 먼저 이해한 가치·J1~J4 해석·후속 카피 후보 여부를 한 행에 기록하는 message confusion log를 추가. 기존 first-real-user baseline, first-60-second observation, first-session friction protocol, traffic-source boundary와 연결. 핵심 경계: 사용자 언어는 증거이지 결정 자체가 아니며, 작은 표본을 activation rate/conversion/retention/PMF/benchmark로 읽지 않는다. traffic-source를 먼저 분리하고 synthetic/mock/self-test 언어를 사람 메시지 증거에 섯지 않는다. J1/J2/J4=`deed_saved`, J3=`deed_judged` first value 매핑 계승. 신규 이벤트·코드·카피·계측·dashboard·session replay·배포·외부발송·비용·시크릿·권한·개인정보 변경 0. 직전 cron의 Claude 위임 timeout 이후 수동 직접 처리. L2 agent-approved push 정상 fast-forward, HEAD==origin/master.) -->

<!-- marketing-26 completed 2026-05-29T11:07Z → intents/archive/marketing-26.md [projects: virtue; type: strategy; topics: retention,habit,recovery,copy] (Virtue recovery-over-streak 리텐션 렌즈 작성 완료. 산출물은 virtue-rebirth-app `7372aab`의 `apps/web/docs/recovery-over-streak-retention-lens.md`(신규 1파일, 166줄). Duolingo/Reforge/HabitBoard source note를 Virtue prelaunch 첫 7일 판돁 렌즈로 번역해, recovery/skip/monthly completion/comeback session을 J1~J4 표로 정리. first value 매핑은 J1/J2/J4=`deed_saved`, J3=`deed_judged` 그대로 계승. 핵심: 연속일/streak reset보다 빠진 뒤 돌아오는 세션을 정성 신호로 보되, skip·comeback·monthly completion을 KPI/전환율/합격선으로 읽지 않는다. J3는 저장 없이 `deed_judged`에서 가치가 닫힐 수 있으므로 saved-deed loop에 섯지 않는다. 공개 카피·기능·운영 후보는 proposal-only로 분리하고 반영 0. 신규 이벤트·코드·카피 반영·대시보드·세션리플레이·배포·외부발송·비용·시크릿·권한·개인정보 변경 0. 검증: conflict marker 0, 코드 diff 0, 기존 이벤트 범위만 인용, HEAD==origin/master. L2 agent-approved push 정상 fast-forward(virtue commits `4ff2b96`, `7372aab`). reports/marketing-26/2026-05-29T1107Z-local.md) -->

<!-- marketing-25 completed 2026-05-28T22:07Z → intents/archive/marketing-25.md [projects: virtue; type: strategy; topics: onboarding,analytics,activation,ai-agents] (Virtue human/test/agent 트래픽 판돁 경계표 작성 완료. 산출물은 virtue-rebirth-app `f5fde73`의 `apps/web/docs/traffic-source-reading-boundary-table.md`(신규 1파일, 177줄). Userpilot/Appcues 2026 온보딩 지표 가이드를 Virtue prelaunch 트래픽 출처 축으로 번역해, A 사람 실사용(baseline 본행) / B 메이커 self-test(표시 후 제외) / C synthetic/mock(J3 first value 부적합) / D 플랫폼 차이(platform 분리 후 최소공약수 비교) / E 장래 agent/API(미발생, 생기면 별도 규칙) 5행 경계표를 작성. 핵심 원칙: 분류가 판돁에 선행하며, 트래픽 종류가 정해지기 전에는 activation/TTV/retention 칸을 읽지 않는다. first value 매핑은 J1/J2/J4=`deed_saved`, J3=`deed_judged` 그대로 계승, 재정의 0. 기존 6개 발화 이벤트(`add_flow_started`,`deed_judged`,`deed_saved`,`level_up_viewed`,`deed_rerolled`,`deed_save_capped`)만 인용. 신규 이벤트·속성·코드·카피·계측·대시보드·세션리플레이·배포·외부발송·비용·시크릿·권한·개인정보 변경 0. workflow-master 파일 양 repo 부재 기록 후 4역할 렌즈 수동 합성. 검증: 5개 트래픽 종류 존재, 6개 이벤트 존재, first-value 매핑 계승, no-read/aggregate 합산 금지선, conflict marker 0, 이벤트 앤커 drift 0, 코드 diff 0, 기존 iOS parity/onboarding metrics/baseline/trust 문서 충돌 0. L2 agent-approved push 정상 fast-forward(c3afb52→f5fde73, HEAD==origin/master). reports/marketing-25/2026-05-28T2207Z-local.html) -->

<!-- marketing-24 completed 2026-05-28T10:07Z → intents/archive/marketing-24.md [projects: virtue; type: strategy; topics: activation,trust,ai-product,onboarding] (Virtue AI 판정 신뢰 보정 감사표 작성 완료.) -->

<!-- research-10 completed 2026-05-28T16:07Z → intents/archive/research-10.md [projects: knowledge-lab,infinity; type: research; topics: content,wiki] (PC·인터넷 시대 전환사 리서치 완료.) -->

<!-- marketing-23 completed 2026-05-27T22:07Z → intents/archive/marketing-23.md [projects: virtue; type: strategy; topics: activation,retention,analytics] (Virtue 온보딩 지표 운영 판돁표 작성 완료.) -->

<!-- marketing-22 completed 2026-05-27T10:07Z → intents/archive/marketing-22.md (Virtue 리텐션 예측 활성화 브리프 작성 완료.) -->

<!-- marketing-21 completed 2026-05-26T22:07Z → intents/archive/marketing-21.md (Virtue `/add` 입력-결과 균형 감사표 작성 완료.) -->

<!-- marketing-20 completed 2026-05-26T15:07Z → intents/archive/marketing-20.md (Virtue 첫 60초 가치 관찰 스크립트 작성 완료.) -->

<!-- marketing-19 completed 2026-05-26T10:07Z → intents/archive/marketing-19.md (Virtue 신규 사용자 홈 화면 FAE 감사표 작성 완료.) -->

<!-- marketing-18 completed 2026-05-26T00:07Z → intents/archive/marketing-18.md (Virtue AEO / Agent-ready 공개 표면 감사표 작성 완료.) -->

<!-- marketing-17 completed 2026-05-25T22:07Z → intents/archive/marketing-17.md (Virtue 첫 세션 정성 마산 관찰 프로토콜 작성 완료.) -->

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

<!-- marketing-01 completed 2026-05-21T10:17Z → intents/archive/marketing-01.md (Virtue add-flow telemetry 승인 실행 완료.) -->

<!-- marketing-08 completed 2026-05-21T10:07Z → intents/archive/marketing-08.md (Virtue PMF 응답 분석 루브릭 작성 완료.) -->

<!-- marketing-07 completed 2026-05-20T22:07Z → intents/archive/marketing-07.md (Virtue 최소 생존 오디언스 기준표 작성 완료.) -->

<!-- marketing-06 completed 2026-05-20T10:07Z → intents/archive/marketing-06.md (Virtue 첫 세션 JTBD 매트릭스 작성 완료.) -->

<!-- marketing-05 completed 2026-05-19T22:07Z → intents/archive/marketing-05.md (Virtue 빈 상태/첫 행동 감사표 작성 완료.) -->

<!-- marketing-04 completed 2026-05-19T10:07Z → intents/archive/marketing-04.md (Virtue 첫인상 포지셔닝 스냅샷 작성 완료.) -->

<!-- marketing-03 completed 2026-05-18T22:20Z → intents/archive/marketing-03.md (Virtue 첫 7일 deed_saved 루프 정의서 작성 완료.) -->

<!-- marketing-02 completed 2026-05-16T14:00Z → intents/archive/marketing-02.md (마찰점 4개 특정, 개선 후보 3개 초안.) -->

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
