# marketing-102 Virtue D7 재가치 관찰 게이트

- intent: marketing-102
- status: final
- scope: L1 internal-doc only
- source: `source/external-links/marketing/2026-05-27-retention-predictive-activation.md`
- compared_artifacts:
  - `artifacts/marketing-79/week-one-activation-observation-table.html`
  - `artifacts/marketing-101/activation-candidate-registry.md`
- inherited 기준:
  - First Value Mapping: J1/J2/J4 = `deed_saved`, J3 = `deed_judged`
  - Measurement Readiness: 측정 가능성과 측정값 성패를 분리
  - Correlation Readiness: D7 대조는 사전 등록된 묶음, window, 제외 조건이 필요
  - First-Week Non-Return: D1/D7 미방문은 실패가 아니라 재초대/재가치 후보 분류

## 판정

현재 `marketing-79` 관찰표와 `marketing-101` activation 후보 등록부는 first value 기준과 작은 표본 금지선은 충분히 갖고 있다. 다만 D7 재가치 관찰은 `D1 재방문`, "D1/D7 return language", "later reflection value" 같은 힌트로 흩어져 있어, 첫 10-20명 관찰자가 같은 행에서 second value evidence와 same-job 유지 여부를 일관되게 쓰기에는 칸 이름이 아직 부족하다.

따라서 새 계측이나 PostHog 쿼리 없이, 첫 10-20명 손기록 표에 아래 4칸을 덧붙이는 것이 안전하다.

1. `D7 return reason`: 사용자가 다시 온 이유를 원문 그대로 적는다.
2. `same job continued`: D0의 잡과 D7의 잡이 같은지 `same / shifted / unclear`로만 표시한다.
3. `D7 second value evidence`: 첫 가치 이후 두 번째 가치가 무엇이었는지 잡별 기준으로 적는다.
4. `D7 no-read`: `not-returned / normal-stop / availability / excluded / unclear` 중 하나로 미방문 또는 무신호를 과잉해석하지 않는다.

## 잡별 D7 질문

| Job | D0 first value | D7 재가치 질문 | second value evidence |
|---|---|---|---|
| J1 daily record | `deed_saved` | "지난번 저장한 기록 때문에 오늘도 한 가지를 남기고 싶어졌나?" | 새 `deed_saved`, 또는 "전에 쓴 것처럼 오늘도 남김"이라는 자기 말 |
| J2 cumulative growth | `deed_saved` | "덕력, 누적, 레벨 같은 진행감이 다시 올 이유가 되었나?" | 두 번째 저장, `level_up_viewed`, 또는 누적 payoff를 알아차린 자기 말 |
| J3 AI curiosity | `deed_judged` | "AI가 본 관점이 궁금해서 다시 판정을 보거나 다른 입력을 넣었나?" | 재방문 뒤 새 `deed_judged`, `deed_rerolled`, 다른 입력 후 판정, 또는 결과를 보여주거나 이야기한 손기록 |
| J4 reflection archive | `deed_saved` | "지난 기록을 다시 읽거나, 나중에 돌아볼 가치 때문에 새 기록을 남겼나?" | 저장한 기록의 legibility/recall 언급, 새 `deed_saved`, 또는 회고 가치 자기 말 |

## 관찰표 보강안

`marketing-79` 표의 카드마다 기존 D1 재방문 아래에 아래 D7 블록을 추가하면 충분하다. 이 변경은 내부 문서/손기록 칸이며 신규 이벤트, 공개 카피, dashboard, session replay 변경이 아니다.

```text
D7 return reason (원문):
D7 same job: [ ] same [ ] shifted [ ] unclear
D7 second value evidence:
D7 no-read: [ ] not-returned [ ] normal-stop [ ] availability [ ] excluded [ ] unclear
```

## activation 후보와 충돌 여부

- A1/J1: `deed_saved` 기준 유지. D7에서 "저장 전 재미있었다"만 있으면 재가치로 승격하지 않는다.
- A2/J2: `deed_saved` 뒤 누적/진행 인지 확인. `level_up_viewed`는 보조 깊이 신호이며 단독 activation 성공이나 retention 결론이 아니다.
- A3/J3: `deed_judged` 기준 유지. D7 재가치는 저장 전환이 아니라 재판정/다른 입력/결과 공유성/AI 관점 호기심으로 본다.
- A4/J4: `deed_saved` 기준 유지. D7 재가치는 저장된 항목이 다시 읽히거나 새 회고 저장으로 이어지는지 본다.

## 금지선

- `add_flow_started`를 activation 성공, D7 재가치, retention-predictive signal로 보지 않는다.
- D7 미방문을 churn, onboarding 실패, 관심 없음으로 단정하지 않는다.
- `deed_save_capped`, 503, latency, failed save를 value, PQL, upgrade demand, 재초대 대상으로 읽지 않는다.
- 작은 표본의 D7 복귀를 retention%, PMF, conversion, 공개 proof로 환산하지 않는다.
- J3의 judged-without-saved를 실패나 묶음 미완료로 읽지 않는다.
- PostHog 쿼리, 신규 tracking, dashboard, session replay, 공개 발송, 카피 변경은 이번 범위 밖이다.

## 결론

`marketing-79`와 `marketing-101`은 서로 충돌하지 않는다. 필요한 보강은 activation 후보를 늘리는 것이 아니라, 같은 first value 이후 D7에서 "같은 잡으로 다시 가치가 생겼는가"를 손기록할 수 있게 칸을 붙이는 것이다. 이때 J1/J2/J4는 `deed_saved`, J3는 `deed_judged` 기준을 유지하고, `add_flow_started`는 계속 성공 지표가 아니다.
