# Infinity Marketing Learnings

> Infinity/Virtue 마케팅 산출물이 다음 마케팅 작업의 기준으로 이어지도록 관리하는 학습 원장이다.
> 전체 report를 반복 저장하지 않고, 다음 Marketer가 반드시 계승해야 할 판단 기준만 남긴다.

## 사용 규칙

- 새 `marketing-*` intent는 이 파일을 먼저 읽고 시작한다.
- 새 산출물은 `계승한 기준`, `이번에 새로 배운 것`, `다음 작업에 넘길 규칙`을 report 또는 artifact에 남긴다.
- 반복적으로 재사용할 가치가 있는 learning candidate만 이 파일에 승격한다.
- 단일 사례, 작은 표본, synthetic/mock/self-test에서만 나온 신호는 report 안에 보류하고 이 원장에는 승격하지 않는다.
- 이 파일은 제품/마케팅 판단 기준이다. 공개 카피, 가격, 계측, dashboard, session replay, 배포, 외부 발송, 비용, 권한, 개인정보 변경은 별도 승인 없이는 실행하지 않는다.

## 현재 핵심 기준

### First Value Mapping

- **결론:** Virtue의 first value는 잡별로 다르다. J1/J2/J4는 `deed_saved`, J3는 `deed_judged`다.
- **적용:** activation, onboarding, TTV, retention, monetization, AI trust/proxy 문서에서 이 매핑을 기본값으로 둔다.
- **주의:** `deed_judged` 후 `deed_saved`가 없는 세션은 J3에서는 정상 종료일 수 있지만, J1/J2/J4에서는 저장 전 이탈 후보일 수 있다.
- **출처:** `marketing-06`, `marketing-07`, `marketing-09`, `marketing-10`, `marketing-20`~`marketing-29`.

### Prelaunch Decision Boundary

- **결론:** prelaunch 단계의 작은 표본은 방향 판단 재료이지, PMF/전환율/리텐션/가격 수요를 확정하는 지표가 아니다.
- **적용:** 첫 10~20명, D1/D7, PMF 응답, activation/drop-off 관찰은 정성 질문과 손기록 중심으로 둔다.
- **주의:** 외부 벤치마크, 40% 기준, 전환율/retention%/PMF 결론, 한 명 신호 확정, completion 지표 승격을 금지한다.
- **출처:** `marketing-08`, `marketing-11`, `marketing-14`, `marketing-22`, `marketing-23`.

### Traffic Source Before Metrics

- **결론:** 신호 해석보다 트래픽 분류가 먼저다.
- **적용:** 사람 실사용, 메이커 self-test, synthetic/mock, 플랫폼 차이, 장래 agent/API 트래픽을 분리한 뒤 activation/TTV/retention을 읽는다.
- **주의:** synthetic/mock/self-test 언어와 점수는 사람 사용자 증거나 J3 first value 판단에 섞지 않는다.
- **출처:** `marketing-25`, `marketing-23`, `marketing-11`.

### Availability And Friction Are Not Value

- **결론:** `deed_save_capped`, 503, 지연, 저장 상한은 availability/friction 신호이며 value, retention, upgrade demand가 아니다.
- **적용:** cap 또는 실패 신호는 먼저 가용성/마찰로 분류하고, 반복 가치 관찰 전에는 유료화 신호로 쓰지 않는다.
- **주의:** `deed_save_capped`를 monetization intent, upgrade demand, TTV 종료, 재가치 신호로 환산하지 않는다.
- **출처:** `marketing-21`, `marketing-22`, `marketing-23`, `marketing-28`, `marketing-29`.

### AI Outcome Proxy Separation

- **결론:** "AI가 활동했다"와 "사용자가 결과를 인정했다"는 다른 proxy다.
- **적용:** AI 관련 마케팅/제품 판단은 activity, acceptance, curiosity, friction, retention proxy를 분리해서 읽는다.
- **주의:** activity proxy를 value proxy로 승격하지 않는다. 저장수, reroll, level_up 1회, judged-save 갭을 단독으로 만족도/불신/리텐션/이탈로 단정하지 않는다.
- **출처:** `marketing-24`, `marketing-29`.

### Trust Calibration By Job

- **결론:** 같은 AI 결과 카드도 잡별로 신뢰 보정 역할이 다르다. J3가 신뢰 보정 진폭이 가장 크다.
- **적용:** J1은 통과점, J2는 누적 공정성, J3는 본체, J4는 영구 주석의 신뢰 문제로 읽는다.
- **주의:** 신뢰는 무조건 높이는 대상이 아니라 과신과 불신 사이의 적정 보정 문제다. 확신도 숫자나 출력 수정 UX는 proposal-only다.
- **출처:** `marketing-24`, `marketing-20`, `marketing-21`.

### No Autonomous Action Bounds The Trust Question

- **결론:** AI 제품의 신뢰 문제 *모양*은 그 AI가 자율 외부 행동을 하는지에 따라 갈린다. Virtue처럼 외부 행동 없이 판정만 보여주는 제품은 McKinsey 구분에서 "틀린 행동"이 아니라 "틀린 말" 영역에만 있어, 신뢰 질문이 "AI가 자동으로 무엇을 해도 되나"에서 "사용자가 출력을 조언(마지막 선택 내 것)으로 읽나, 판결(정체성 사실)로 읽나"로 수축한다.
- **적용:** AI 신뢰 작업은 먼저 "이 AI가 자율 외부 행동을 하는가"를 묻는다. 아니면 agentic guardrail·monitoring·accountability 플레이북을 신뢰 해법으로 가져오지 않는다. 위험의 본체는 행동적 해가 아니라 자기인식 오보정이다. Virtue에서 낮은 위험 축(저장 비강제·무시 비용 0·외부 효과 0)은 이미 구조적 최대치이므로, 관찰은 위험을 낮추는 게 아니라 사용자가 낮은 위험·마지막 선택권을 *인지*하는지를 본다.
- **주의:** `deed_saved`를 판정 승인/만족으로, judged−saved 갭을 불신/이탈로 읽지 않는다. 확신도 %·출력 수정·trust 이벤트는 proposal-only. [[Trust Calibration By Job]]을 보완하는 새 축이다.
- **출처:** `marketing-38`, `marketing-24`, `marketing-20`.

### Monetization Boundary

- **결론:** 첫 가치 이전에 결제정보, 계정강제, 핵심행동 잠금, 가격/플랜 확정은 두지 않는다.
- **적용:** 유료화 후보는 first value 이후 반복 가치가 보일 때 논의한다. J1/J2/J4는 `deed_saved`, J3는 `deed_judged` 이후의 확장 후보로 분리한다.
- **주의:** 가격표, 결제 연동, paywall 실험, trigger 확정, 공개 카피, 배포는 approval-needed다.
- **출처:** `marketing-28`.

### Recovery Over Streak

- **결론:** Virtue 리텐션은 streak 유지보다 빠진 뒤 돌아오는 회복 신호를 더 조심스럽게 봐야 한다.
- **적용:** recovery, skip, comeback session, monthly completion은 정성 관찰 질문으로 둔다.
- **주의:** skip, comeback, monthly completion을 KPI, 전환율, 합격선으로 읽지 않는다.
- **출처:** `marketing-26`, `marketing-22`.

### Message Confusion As Evidence

- **결론:** 사용자 언어는 증거이지 결정 자체가 아니다.
- **적용:** 사용자가 붙인 제품명/대체재/되물음/첫 이해 가치를 기록하고, J1~J4 해석과 traffic source를 함께 남긴다.
- **주의:** 작은 표본 메시지 하나로 positioning, activation, conversion, retention, PMF를 확정하지 않는다.
- **출처:** `marketing-27`, `marketing-13`, `marketing-11`.

### Shareworthiness Is A Separate Axis

- **결론:** "첫 결과"는 한 칸이 아니라 세 층이다. (a) 가치 도달, (b) 공유성(공명/추천), (c) 저장 후 누적 payoff를 분리해서 읽는다. 공유성은 first value·acceptance와 독립이며, 저장 없이 공유성 있음(J3)·저장 있으나 공유성 없음(J1)이 모두 가능하다.
- **적용:** AI 온보딩·activation·첫 결과 강도 판독에서 공유성은 항상 저장 전 시점에서 따로 손기록한다. 공유성 행동 증거(웃음/놀람/반박/보여 주기/재전달)는 대부분 off-instrument이므로 `deed_saved`·`deed_rerolled` 횟수로 환산하지 않는다.
- **주의:** 저장수·재판정수를 공유성으로 환산하지 않는다. J3 judged−saved 갭을 공유성/가치 부재로 읽지 않는다(저장 없이 보여 주고 닫힘이 정상).
- **출처:** `marketing-30`, `marketing-29`, `marketing-21`, `marketing-20`.

### Product Body vs Bumper By Job

- **결론:** 첫 세션 표면은 가치를 *만드는* 제품 본체와 이탈 지점만 돕는 범퍼로 갈리며, 같은 표면이 잡에 따라 부호가 뒤집힌다. 제품 본체가 약하면 범퍼(체크리스트·툴팁·설명)로 못 가린다.
- **적용:** 표면을 first value 위치 기준으로 본체/범퍼로 분류한다. J1/J2/J4는 저장 후 홈(`deed_saved`)이 본체, J3는 결과 카드(`deed_judged`)가 본체이고 저장은 범퍼(선택)다. 홈은 J2엔 본체(누적 payoff), J1엔 범퍼(다음 행동 안내)다.
- **주의:** 막힘은 4분류로 라우팅이 다르다 — 길을 잃음(범퍼 후보)·결과 기대 불일치(제품 약속/결과 후보)·가용성 차단(availability/friction)·정상 종료(이탈 아님). J3에 저장 유도 범퍼를 무조건 붙이면 첫 가치 흐름을 방해한다. 저장률·재판정수로 막힘 성격을 단정하지 않는다.
- **출처:** `marketing-31`, `marketing-30`, `marketing-16`, `marketing-21`, `marketing-06`.

### Nudges Are Event-Triggered, And Show-Nothing Is The Default

- **결론:** 온보딩 넛지는 팝업 형식이 아니라 기존 행동 조합(trigger)의 맥락 도움이다. 도움의 기본값은 "띄우지 않음"이며, B-LOST(길 잃음)로 분류된 막힘에서만 후보가 된다.
- **적용:** 넛지/체크리스트/툴팁 후보를 만들 때 먼저 이벤트 조합과 잡 맥락을 대조한다. `add_flow_started` 후 미판정은 가용성·탐색·mock/self-test를 제외한 뒤 B-LOST일 때만 입력 보조 후보가 되고, `deed_judged` 후 미저장은 J3에서는 정상 종료라 저장 넛지를 띄우지 않는다. `deed_rerolled`는 의도 관찰 전 보류, `deed_save_capped`는 제한 설명·회복 경로 문제로만 둔다.
- **주의:** trigger는 도움의 조건이지 자동 발동 근거가 아니다. B-MISMATCH(결과 기대 불일치)는 제품 약속/결과 문제라 넛지로 가리지 않고, B-AVAIL은 availability/friction으로 분리한다. first value 도달 직후 전환·공유·유료 넛지를 끼우지 않는다.
- **출처:** `marketing-40`, `marketing-35`, `marketing-31`, `marketing-17`.

### First-Input Defaults Steer The Job

- **결론:** AI 제품의 첫 입력 기본값(placeholder·예시·추천 질문·기본 프롬프트)은 사용자가 어떤 잡으로 제품을 이해할지 정하는 조향 장치다. Virtue는 예시·추천 질문 0의 "질문형 placeholder + 빈 슬롯" 단일 패턴이라 기능 설명형(support-bot 유도) 위험은 구조적으로 0이지만, 잡별 조향도 0이라 같은 중립 placeholder(`뭐 했어요?`)가 J1~J4를 구분 없이 부른다.
- **적용:** 첫 입력을 읽을 때 "어떤 기본값이 이 잡을 불렀는가(첫 입력 출처)"를 먼저 분리한 뒤 후속 행동을 본다. "두 번째 메시지" 신호는 잡별 두 번째 행동으로 번역한다 — J1/J4=`deed_saved`, J2=`level_up_viewed`/두 번째 저장, J3=`deed_rerolled`/다른 입력 후 재판정(저장 강요 안 함). 첫 입력 단계에서 J3(AI 약속이 `/add` 안에서야 등장)·J2(누적 보상은 두 번째 저장 이후)가 가장 약하게 불린다.
- **주의:** 전역 예시/placeholder 최적화 금지 — 한 잡을 살리는 예시가 다른 잡을 구경/support-bot 모드로 끌 수 있다. 조향이 필요하면 잡별로, 반드시 관찰로 먼저 확인한다. mock 모드 라벨(`임시 판정`)이 J3 첫 인상을 낮추는 문제는 런타임 모드 정책이며 카피 변경 범위 밖(proposal-only). J3 judged−saved 갭을 가치 부재/이탈로 단정하지 않는다.
- **출처:** `marketing-32`, `marketing-06`, `marketing-21`, `marketing-30`, `marketing-31`.

### Measurement Readiness Is A Separate Gate

- **결론:** PLG는 Foundation→Activation→Conversion 순서이고, Foundation의 종료 조건은 "활성화가 좋다"가 아니라 "활성화율·기준선을 측정할 수 있는 상태"다. 측정 *가능성*(정의 완료)과 측정 *값의 성패*(좋고 나쁨)는 별개의 게이트다.
- **적용:** 활성화/단계 판단 작업은 먼저 측정 가능 상태(first value 매핑·후보 묶음+window·TTV 시작/종료점·D7 질문·기준선 양식·이벤트 발화·트래픽 분리)가 준비됐는지 확인한 뒤 값을 읽는다. Activation 단계 진입은 외부 벤치마크 수치가 아니라 데이터 품질·synthetic 제외·가용성 차단·같은 잡 재가치 4가지로 판단한다.
- **주의:** 측정 가능 상태와 측정값 성패를 섞지 않는다. 외부 수치(TTV<5분·D7 N%·activation 40%)를 prelaunch 합격선으로 복사하지 않는다. 측정 불가 상태의 비율을 활성화로 읽지 않는다. 출시 후 검증 발동 시점·도착 점검은 등록부 게이트(m33 §4)에 위임한다. [[Prelaunch Decision Boundary]]를 보완하는 새 축이다.
- **출처:** `marketing-34`, `marketing-33`, `marketing-22`, `marketing-10`.

### Correlation Readiness Is A Separate Gate

- **결론:** 활성화를 *측정할 수 있는 상태*([[Measurement Readiness Is A Separate Gate]])와, 그 활성화를 *retention과 대조할 수 있는 상태*는 별개의 게이트다. 후자는 충분 표본 외에 사전 등록된 쿼리 모양·관찰 창 tier·제외 조건이 모두 있어야 정직하다.
- **적용:** retention/상관/D30/monetization 대조 작업은 데이터 도착 *전에* 묶음 완료 정의·창 tier(D7 우선·D30/14일 보류)·제외(mock/synthetic/self-test/availability cap/503)·pseudo-query shape를 등록부로 고정하고, 실제 쿼리 실행·대시보드 구성은 decision-grade 표본·접근권한이 있을 때로 분리한다. 묶음 완료 집단 vs 미완료 집단 비교에서 J3는 `deed_judged` 기준으로만 완료 판정(저장 불요).
- **주의:** pseudo-query를 실행 결과로 착각하지 않는다. 빈 장기 창(D30)을 "리텐션 없음"으로 읽지 않는다(D7로 자연 주기 확인 후 연다). judged−saved 갭을 묶음 미완료·이탈로 환산하지 않는다. 묶음 완료율을 activation rate·전환율·유의성으로 환산하지 않는다. 제외 세션은 삭제하지 않고 가용성/마찰 관찰용으로 보존한다.
- **출처:** `marketing-37`, `marketing-34`, `marketing-33`, `marketing-22`.

### Readiness Trace Over Accuracy

- **결론:** 인간-AI 제품의 첫 경험은 정확도·만족도 한 칸이 아니라 outcome/reliance/safety/learning 4축의 상호작용 흔적으로 읽는다. 네 축은 서로 다른 축이며 한 축의 신호를 다른 축으로 합산하지 않는다.
- **적용:** Virtue 같은 비행동 AI 판정 제품에서는 outcome=잡별 first value(J1/J2/J4 `deed_saved`, J3 `deed_judged`), reliance=결과 뒤 저장·재시도·무시·수정·재방문, safety=자기인식 오보정·과소의존 흔적, learning=D7에 "이전 판정 이후 더 잘 쓰는가"로 분리한다.
- **주의:** `deed_saved`를 AI 판정 동의/승인으로, judged−saved 갭을 outcome 미달/이탈로, `deed_rerolled`를 불신으로, `deed_save_capped`를 value로 읽지 않는다. prelaunch 첫 세션에서는 learning 결론을 내지 않고 후보만 등록한다.
- **출처:** `marketing-39`, `marketing-38`, `marketing-24`.

### PQL Is A Bundle, Not A Single Event

- **결론:** PQL/upgrade-readiness는 activation(first value)이 아니라 그 다음 층이며, 단일 이벤트가 아니라 반복+재방문 행동 묶음이다. 출시 후 작은 숫자에서 `deed_save_capped` 1회 같은 단일 이벤트를 "더 원해서 막혔다 = 업그레이드 수요"로 읽는 것이 가장 흔한 오독이다.
- **적용:** 출시 후 high-intent/upgrade 신호는 (A) PQL 후보(반복 `deed_saved`/`deed_judged` + D7 재방문 묶음 — retention·conversion과 *대조할 대상*, 결론 아님) / (B) 비후보·가짜 PQL(단일 이벤트·availability·정상 종료·다의적 단발) / (C) Waiting·approval-needed(채점·임계값·가격·신규 tracking·대시보드·공개 카피) 세 칸으로 먼저 가른다. 신호를 읽기 전 ① 단일 이벤트인가 ② 가용성/마찰인가 ③ J3 정상 종료(judged−saved 갭)인가 ④ 반복+재방문 묶음인가를 순서대로 통과시킨다. A3(J3)는 저장 없이도 반복 `deed_judged`로 후보가 된다. 실제 retention 대조 방법은 [[Correlation Readiness Is A Separate Gate]](m37)에 위임한다.
- **주의:** 첫 10명·첫 7일은 PQL을 *확정*하는 시점이 아니라 후보를 *대조 가능한지* 확인하는 시점이다. PQL 임계값·전환율·upgrade demand·외부 PQL 벤치마크를 산출하지 않는다. `deed_save_capped`는 availability/friction이지 upgrade demand가 아니다([[Availability And Friction Are Not Value]]). [[Monetization Boundary]]·[[Measurement Readiness Is A Separate Gate]]를 보완하는 새 축이다.
- **출처:** `marketing-41`, `marketing-33`, `marketing-28`, `marketing-37`, `marketing-29`.

### Session Value Is Read By Job, Not Event Count

- **결론:** AI 제품의 세션 가치는 이벤트/클릭 수가 아니라 잡별 first value 도달과 종료 성격으로 읽는다. fewer actions가 더 빠른 가치일 수 있고(J3 짧은 무저장 세션=성공), 많은 행동이 마찰일 수 있다(반복 reroll·cap·다이벤트 무가치=보류/마찰). 한 세션은 성공/정상/보류/마찰 네 칸으로 갈라 읽되 결론이 아니라 대조 후보로 둔다.
- **적용:** 세션·활성화 판독 작업은 raw event/click volume을 세션 품질·engagement·activation으로 환산하지 말고, 한 세션을 ① 잡과 first value 확인 → ② first value 이벤트 발화 여부(→성공) → ③ 미발화면 종료 성격(J3 정상 종료=성공 / `deed_save_capped`=마찰 / B-LOST·다의=보류) 순서로 분류한다. 같은 "짧고 저장 없는 세션"이 J3엔 성공, J1/J2/J4엔 보류다.
- **주의:** 이벤트 수↑를 가치↑로, 짧은 세션을 이탈로, 저장 없는 종료(J3)를 실패로, 반복 `deed_rerolled`를 불신으로, `deed_save_capped`를 가치/upgrade demand로, 클릭 많은 세션을 engagement로 읽지 않는다. 세션 분류를 비율·임계값·activation rate로 환산하지 않는다. 대조 방법은 [[Correlation Readiness Is A Separate Gate]](m37), PQL 결론은 [[PQL Is A Bundle, Not A Single Event]](m41) 위임. [[AI Outcome Proxy Separation]]·[[Availability And Friction Are Not Value]]·[[Product Body vs Bumper By Job]]·[[Readiness Trace Over Accuracy]]를 보완하는 새 축이다.
- **출처:** `marketing-42`, `marketing-29`, `marketing-31`, `marketing-39`, `marketing-41`.

### Post-Response Flow Reveals Value, Not The Result Event

- **결론:** AI 제품의 가치 전달은 결과/응답 이벤트가 발화했다는 사실이 아니라 그 직후 사용자가 무엇을 하는지로 읽는다. Virtue의 결과 카드(`deed_judged`)는 J3에서는 도착점(first value)이지만 J1/J2/J4에서는 저장 전 통과점이라, 같은 "저장 없이 닫힘"도 잡에 따라 정상 종료와 보류로 갈린다.
- **적용:** 결과 카드 직후 30초를 세션 전체와 분리된 수기 관찰 프레임으로 두고, 먼저 ① 카드가 도착점인가 통과점인가 ② first value 행동이 이미 도달했거나 직후 발화했는가 ③ 미발화면 종료 성격이 정상/보류/마찰 중 무엇인가를 본다. on-instrument 신호는 `deed_saved`, `deed_rerolled`, `deed_save_capped`, 종료뿐이고 근거 읽기·보여 주기·망설임은 손기록으로만 남긴다.
- **주의:** `deed_judged` 발화만으로 이해/수용/가치 전달을 확정하지 않는다. 결과 직후 분류를 post-response score, activation rate, 전환율, retention%, PQL, upgrade demand, 자동 넛지, 공개 카피, 신규 tracking/dashboard/session replay로 연결하지 않는다. "30초"는 계측 임계값이나 신규 duration 속성이 아니다. [[Session Value Is Read By Job, Not Event Count]]·[[AI Outcome Proxy Separation]]·[[Nudges Are Event-Triggered, And Show-Nothing Is The Default]]를 보완하는 새 축이다.
- **출처:** `marketing-44`, `marketing-42`, `marketing-29`, `marketing-40`.

### First-Week Non-Return Is A Reactivation Candidate, Not A Failure

- **결론:** 첫 주(D1/D3/D7) 미방문(non-return)은 실패 판정이 아니라 잡별 재초대 후보다. 미방문은 단일 churn이 아니라 "어떤 first value까지 갔고 어떤 second value 앞에서 멈췄나"를 읽는 segmentation 문제이며, first value까지 간 미방문은 이미 가치를 한 번 본 warm 후보다.
- **적용:** 미방문 사용자를 발송 대상으로 보기 전에 RC-WARM(first value 도달 후 second value 없이 미방문=value recall 후보) / RC-PRE-LOST(first value 전 멈춤 중 B-LOST만) / RC-NORMAL(J3 `deed_judged` 후 저장 없이 정상 종료=후보 아님) / RC-AVAIL(`deed_save_capped`·503·지연=후보 아님) / RC-EXCLUDED(synthetic/mock/self-test=후보 아님)로 먼저 가른다. 순서는 ① EXCLUDED 분리 → ② AVAIL 분리 → ③ first value 발화 여부 → ④ 종료 성격(J3 정상 종료/막힘 4분류 B-LOST) → ⑤ do-not-send+승인선. 재초대 기본값은 "보내지 않음"이고 메시지는 할인/과장이 아니라 value recall(전에 하려던 일·도달한 결과·놓친 다음 가치)이다.
- **주의:** D1/D7 미방문을 onboarding 실패·가치 부족·관심 없음으로 단정하지 않는다. judged−saved 갭을 이탈로(J3 정상 종료), `deed_save_capped`를 재초대/upgrade 수요로, RC-WARM을 PQL로 읽지 않는다. 미방문률을 reactivation rate·churn·retention%로 환산하지 않는다. 공개 발송·이메일/푸시/in-app·retargeting은 모두 approval-needed. retention 대조는 [[Correlation Readiness Is A Separate Gate]](m37), PQL 결론은 [[PQL Is A Bundle, Not A Single Event]](m41) 위임. [[First Value Mapping]]·[[Recovery Over Streak]]·[[Prelaunch Decision Boundary]]·[[Nudges Are Event-Triggered, And Show-Nothing Is The Default]]를 보완하는 새 축이다.
- **출처:** `marketing-43`, `marketing-14`, `marketing-26`, `marketing-40`, `marketing-41`.

### Decision-Delegation Risk Rides The Verb, Control Rides The Affordance

- **결론:** 비자율 AI 판정 제품에서 약속 문장의 결정-위임 위험은 한곳에 몰리지 않고 *동사 프레임*에 실린다. `채점`·`판정`은 AI를 채점관/심판으로 세우는 판결 프레임("AI가 결정한다")이고, `본`·`읽은`·`보여주기`는 해석 제공자로 두는 관점 프레임("AI가 정리하고 마지막 선택은 나")이다. 반대로 제어 체감은 카피가 아니라 *결과 후 선택 affordance*(취소·한 번 더·저장, 0점도 저장 가능, 무저장 종료 비용 0)에 실려, 마지막 결정권은 카피와 무관하게 구조적으로 이미 사용자에게 있다. 그래서 위험은 "권한 부재"가 아니라 "문장이 권한을 덜 보이게 함"이다.
- **적용:** AI 약속 문장(홈·`/add`·결과 카드·내부 snippet)을 읽을 때 ① 동사가 판결/관점 프레임 중 무엇인가 → ② 같은 흐름 안에서 프레임이 섞이는가(불일치=위험 1차 소재; Virtue는 버튼 `AI 채점` vs 헤더 `AI가 본 오늘`로 섞임) → ③ 제어권은 결과 후 선택 affordance 존재로 본다 → ④ 후보 문구는 전부 proposal-only로 둔다. 가장 큰 레버는 새 UI가 아니라 판결→관점 프레임 정렬이다.
- **주의:** 프레임 분류를 "카피를 바꿔야 한다"는 결정으로 환산하지 않는다(전부 proposal-only). affordance 존재를 "사용자가 제어를 *인지*했다"로 단정하지 않는다(인지 여부는 m38 관찰 위임). 공개 버튼/헤더/힌트/온보딩 카피·llms.txt·cap 정책 변경은 모두 approval-needed. 외부 설문 수치(Gartner)를 Virtue 성과 기준으로 복사하지 않는다. [[No Autonomous Action Bounds The Trust Question]]·[[Trust Calibration By Job]]을 보완하는 카피 축이다.
- **출처:** `marketing-45`, `marketing-38`, `marketing-24`, `marketing-32`, `marketing-18`.

### Agent-Led Growth Fits Task-Completion Products, Not Experience Products

- **결론:** agent-led growth(에이전트가 API·문서를 발견하고 task completion으로 활성화)가 맞는지는 "제품에 AI가 있는가"가 아니라 **"가치를 누가 완료하는가(task completion subject)"**로 갈린다. 에이전트의 task completion이 곧 가치인 제품(API/B2B/워크플로 편입형)엔 맞지만, 사람의 경험·선택이 본체인 제품(Virtue 같은 성찰/기록/자기 해석)엔 do-for-you 유통이 제품 의미를 *소거*한다(성찰을 대행하면 성찰이 사라진다).
- **적용:** AI 유통 논의가 들어오면 ① "가치를 누가 완료하나"(에이전트 task vs 사람 경험·선택)를 먼저 묻는다 → ② agent-readable 후보를 **read-about(설명: 에이전트가 읽고 사람에게 안내)** vs **do-for-you(실행: 에이전트가 대신 사용)**로 가른다 → ③ "사람 경험·선택" 제품이면 do-for-you(MCP/API/agent onboarding/스키마·에러코드·예제)는 no-fit, 공개 read-about(llms.txt 등)는 approval 후보 → ④ 재검토는 실사용 신호 기반 launch/post-launch gate(설명→export→연결→실행 표면 순)로만 연다. read-about 표면도 m45 동사 프레임(판결 vs 관점)을 따른다.
- **주의:** "AI 제품이니까 agent-first 유통부터"는 범주 오류다. agent-to-agent recommendation·MCP 노출 수치를 제품 성과 기준으로 복사하지 않는다. 공개·실행 표면(robots/sitemap/llms.txt·API/MCP·programmatic auth·usage-based pricing)은 모두 approval-needed. agent path를 열면 "외부 자율 행동 없음"(m38)과 "사람 마지막 선택"(m45) 두 구조적 안전장치가 동시에 무너진다. [[No Autonomous Action Bounds The Trust Question]]·[[Decision-Delegation Risk Rides The Verb, Control Rides The Affordance]]·[[Prelaunch Decision Boundary]]를 보완하는 유통 전략 축이다.
- **출처:** `marketing-46`, `marketing-38`, `marketing-45`, `marketing-18`.

### First-User Learning Loop Reads Language, And Help Means Articulation Not Delegation

- **결론:** prelaunch 첫 사용자(첫 10명) 학습은 확장 채널 최적화나 작은 숫자 해석보다 *먼저*이고, 그 산출은 성패율이 아니라 (a) 반복되는 문제 언어 (b) 사용자가 자기 말로 설명한 가치 (c) 결정-위임 인지 세 언어로 읽는다. 성찰·기록·자기 선택이 본체인 제품에서 첫 사용자 도움의 목표는 사용자의 결정을 *대신*하는 것이 아니라 사용자가 가치를 *자기 말로 말하게* 하는 것이다 — 도움이 성찰을 대행하면 수집하려던 자기 말 자체가 사라진다.
- **적용:** 첫 사용자 학습을 invite(잡별 초대) → pre(사용 전 2문항: 현재 행동·대체재 / 잡 신호·기대) → post(첫 세션 후 3문항: first value 위치 / friction / 결정-위임 인지) → 자기 말 기록 칸 4지점 손기록 루프로 둔다. 초대·질문 문장은 전부 proposal-only 내부 후보이고 m45 동사 프레임(판결 아닌 관점)을 따른다. first value는 잡별(J1/J2/J4=`deed_saved`, J3=`deed_judged`)로 읽고 J3 결과 후 무저장 종료는 정상이다.
- **주의:** 첫 10명을 성패율·activation rate·PMF·전환율·retention%로 환산하지 않는다. 자기 말 기록은 신규 계측이 아니라 손기록(원문 그대로)만이다. maker self-test/synthetic/mock은 제외·표시한다. `deed_save_capped`·503·지연은 availability/friction이지 value/upgrade demand가 아니다. 공개 발송/DM/광고·프로덕션 카피·신규 이벤트/속성/tracking/privacy/dashboard/session replay·배포·비용·권한 변경은 모두 approval-needed. [[Message Confusion As Evidence]]·[[Prelaunch Decision Boundary]]·[[Agent-Led Growth Fits Task-Completion Products, Not Experience Products]]·[[Decision-Delegation Risk Rides The Verb, Control Rides The Affordance]]를 보완하는 첫 사용자 수집 루프 축이다.
- **출처:** `marketing-47`, `marketing-27`, `marketing-08`, `marketing-46`, `marketing-45`.

### Guided First-Value Is A Four-Stage Handoff

- **결론:** AI 온보딩의 guided first value는 더 빠른 AI 산출이 아니라 **첫 입력 전 → AI 판단 대기 → 결과 해석 → 저장/종료** 4구간 handoff에서 사용자의 행동권과 통제감을 보존하는 문제다. 각 구간의 도움은 잡별 종료점에 맞아야 한다. J1/J2/J4는 `deed_saved`에서 닫히고, J3는 `deed_judged`에서 닫히므로 저장 안내는 J3에선 선택 범퍼다.
- **적용:** 첫 세션 감사는 ① 어느 구간에서 사용자가 "직접 해냈다"고 느꼈는가 ② AI를 대신 결정으로 읽었는가, 보라고 정리한 것으로 읽었는가를 손기록한다. guided break는 `first_input`, `ai_wait`, `result_interpretation`, `save_or_exit` 중 첫 끊김으로 표시하고, 이후 B-LOST/B-MISMATCH/B-AVAIL/B-NORMAL 성격을 분리한다.
- **주의:** 빠른 `deed_judged`를 모든 잡의 activation으로, 저장 없는 J3 종료를 이탈로, AI 대기/지연/503/`deed_save_capped`를 value나 upgrade demand로 읽지 않는다. guided break 발견을 곧바로 넛지·카피·신규 이벤트·tracking/privacy·dashboard/session replay·배포로 옮기지 않는다. 모두 approval-needed다.
- **출처:** `marketing-51`, `marketing-49`, `marketing-47`, `marketing-45`, `marketing-32`.

### Prompt Design Teaches Desired Result, Not UI Or Judgment

- **결론:** AI 온보딩의 첫 입력 prompt design은 사용자가 UI를 배우게 하는 일이 아니라, AI에게 원하는 결과를 짧게 알려주게 하는 일이다. Virtue에서는 이를 **UI instruction / judgment delegation / desired-result teaching** 세 칸으로 먼저 분리한다. 좋은 첫 입력 문구는 기능 설명을 늘리지 않고, `채점`/`판정`식 판단 위임도 키우지 않으며, 사용자가 원하는 기록·누적·AI 관점·회고 결과를 자기 말로 지정하게 돕는다.
- **적용:** `/add` placeholder·힌트·예시·버튼 문구 후보를 볼 때 ① 이 문장이 단순 조작 설명인가 ② AI에게 결정을 맡기게 하는가 ③ 사용자가 원하는 산출물을 AI에게 알려주게 하는가를 표시한다. click tax는 "원하는 결과와 무관한 탐색·튜토리얼·메뉴 이동"일 때만 줄이고, 성찰을 만드는 입력 시간 자체는 제거 대상이 아니다. 잡별 예시는 observation 후 proposal-only로만 다룬다.
- **주의:** 전역 예시/placeholder 최적화 금지. 한 잡을 살리는 예시는 다른 잡을 구경·support-bot·판정 위임 모드로 끌 수 있다. 공개 카피, 버튼/placeholder 변경, 신규 이벤트·속성·개인화·tracking/privacy·dashboard/session replay·배포는 approval-needed다. J3는 `deed_judged`에서 first value가 닫히므로 저장을 정상 후속 행동으로 강제하지 않는다.
- **출처:** `marketing-52`, `marketing-51`, `marketing-32`, `marketing-45`.

### Task Completion In AI Onboarding Is User's Next Action, Not AI's Act

- **결론:** AI 온보딩의 task completion은 AI가 행동한 시점이 아니라 **사용자가 AI가 제공한 것에 반응해 선택한 시점**이다. `deed_judged`는 AI의 기여 완료이고, 사용자의 task completion은 J1/J2/J4에서 `deed_saved`, J3에서 `deed_judged`다. "AI가 판정했다"와 "사용자가 작업을 완료했다"는 다른 사건이다.
- **적용:** AI 온보딩 활성화/첫 세션 분석에서 `deed_judged` 발생을 J1/J2/J4 task completion으로 읽지 않는다. 잡별 task-completion 기준(J1/J2/J4=`deed_saved`, J3=`deed_judged`)을 먼저 확인하고, judged 이후 사용자가 선택한 행동(save / reroll / cap / exit)을 task complete / in-progress / blocked / normal-exit로 분류한다. 첫 10명 관찰에서 "deed_judged 몇 번" 대신 "judged 후 어떤 행동을 선택했나"를 손기록한다.
- **주의:** J3 judged→exit는 정상 task success다 — 저장을 독촉하거나 이탈로 읽지 않는다. `deed_save_capped`는 task 포기가 아니라 availability 차단이다. `deed_rerolled`는 task failure로 단정하지 않는다. deed_judged 카운트가 높다고 activation rate가 높다고 환산하지 않는다. [[First Value Mapping]]·[[Post-Response Flow Reveals Value, Not The Result Event]]·[[Guided First-Value Is A Four-Stage Handoff]]를 보완하는 온보딩 completion 읽기 축이다.
- **출처:** `marketing-53`, `marketing-52`, `marketing-51`, `marketing-44`.

### Purchase Situation Before Object Shape

- **결론:** 커머스 카테고리가 이미 붐비고 오브젝트 형태가 제네릭이면, 상품 포지셔닝은 오브젝트명에서 나오지 않는다. 먼저 "어떤 구매 상황에서 왜 이 버전이 필요한가"를 이름 붙이고, 넓은 카테고리 키워드는 그 다음에 검색 다리로만 쓴다.
- **적용:** Naver Shopping 후보가 사용자에게 "너무 일반적"으로 보였거나 OpenAPI top results가 generic game/checklist/planner language로 포화된 경우, Marketer는 title/copy보다 먼저 구매 상황을 선택한다. 예: `질문 카드`가 아니라 AI/creator workshop room, `여행 체크리스트`가 아니라 refill/spec/use-case 맥락.
- **주의:** 큰 OpenAPI total, SearchAd volume, generic object keyword는 demand base일 수 있지만 differentiation proof가 아니다. broad keyword를 title lead로 두기 전에 정보성/제네릭/카테고리-노이즈 여부를 분리한다. 소싱·상품등록·공개 카피·가격·배송·재고·광고·계정/고객/주문 액션은 approval-needed다.
- **출처:** `marketing-50`, `marketing-48`, `naver-shopping-01`.

## 다음 Marketer 체크리스트

1. 이번 intent가 어떤 기존 기준을 계승하는지 3개 이하로 적는다.
2. 기존 기준을 바꿀 필요가 있다면 변경 이유와 충돌한 선행 산출물을 적는다.
3. 새 이벤트, 속성, 카피, 가격, 계측, dashboard, session replay, 배포, 외부 발송, 비용, 권한, 개인정보 변경은 proposal-only 또는 approval-needed로 분리한다.
4. report의 `<details>` 안에 `계승한 기준`, `이번에 새로 배운 것`, `다음 작업에 넘길 규칙`을 남긴다.
5. durable learning candidate가 있으면 이 파일에 추가할 문장 형태로 제안한다.
