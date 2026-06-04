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

## 다음 Marketer 체크리스트

1. 이번 intent가 어떤 기존 기준을 계승하는지 3개 이하로 적는다.
2. 기존 기준을 바꿀 필요가 있다면 변경 이유와 충돌한 선행 산출물을 적는다.
3. 새 이벤트, 속성, 카피, 가격, 계측, dashboard, session replay, 배포, 외부 발송, 비용, 권한, 개인정보 변경은 proposal-only 또는 approval-needed로 분리한다.
4. report의 `<details>` 안에 `계승한 기준`, `이번에 새로 배운 것`, `다음 작업에 넘길 규칙`을 남긴다.
5. durable learning candidate가 있으면 이 파일에 추가할 문장 형태로 제안한다.
