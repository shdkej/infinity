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

## 다음 Marketer 체크리스트

1. 이번 intent가 어떤 기존 기준을 계승하는지 3개 이하로 적는다.
2. 기존 기준을 바꿀 필요가 있다면 변경 이유와 충돌한 선행 산출물을 적는다.
3. 새 이벤트, 속성, 카피, 가격, 계측, dashboard, session replay, 배포, 외부 발송, 비용, 권한, 개인정보 변경은 proposal-only 또는 approval-needed로 분리한다.
4. report의 `<details>` 안에 `계승한 기준`, `이번에 새로 배운 것`, `다음 작업에 넘길 규칙`을 남긴다.
5. durable learning candidate가 있으면 이 파일에 추가할 문장 형태로 제안한다.
