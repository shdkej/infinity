# Virtue session 2-3 reengagement observation companion

- intent: `marketing-114`
- source note: `source/external-links/marketing/2026-07-19-multi-session-onboarding-activation.md`
- scope: docs-only / first-10 observation companion addendum
- permission: L1 docs-only
- status: internal companion

## 0. Purpose

첫 세션 activation만으로는 Virtue가 다시 열릴 이유를 만들었는지 알 수 없다. 이 companion은 기존 `artifacts/marketing-79/week-one-activation-observation-table.html` 옆에 붙여 세션 2-3에서 사용자가 어디서 이어가고, 어디서 끊기고, 어떤 두 번째 가치 신호를 보이는지 손기록한다.

신규 이벤트, 속성, tracking, dashboard, session replay, 공개 카피, 배포, 비용, 권한 변경은 만들지 않는다.

## 1. Inherited Criteria

| 기준 | 계승 내용 | 이번 문서의 적용 |
|---|---|---|
| First Value Mapping | J1/J2/J4 = `deed_saved`, J3 = `deed_judged` | 세션 2에서도 같은 first value 기준을 유지하고, 재방문 자체를 activation으로 승격하지 않는다. |
| First-Week Non-Return | 미방문은 실패가 아니라 재초대 후보 분류 문제 | 돌아오지 않은 이유를 churn이 아니라 `last_stop_point`와 `session_2_return_trigger` 후보로 남긴다. |
| Session Value By Job | 이벤트 수보다 잡별 first value와 종료 성격을 먼저 본다. | 세션 2의 클릭량, 길이, 저장 수를 retention quality로 환산하지 않는다. |
| Adoption Evidence Bundle | 다시 열 이유, 반복 job 후보, 설명할 한 줄, 다음 행동 자연성을 함께 본다. | 세션 2에서는 "말했던 다시 열 이유가 실제 진입 이유와 맞았는가"를 확인한다. |

## 2. Session 2-3 Addendum Columns

기존 첫 10명 관찰 카드 옆에 아래 네 칸을 추가한다. 모두 손기록이며 자동 계측 필드가 아니다.

| 칸 | 적는 값 | 읽는 법 | 금지선 |
|---|---|---|---|
| `session_2_return_trigger` | 다시 연 직접 계기. 예: 어제 저장한 것 확인, 새 행동 기록, AI 판정 재시도, 회고 루틴, 우연한 재방문, 미방문 | 첫 세션의 "다시 열 이유"가 실제 행동으로 이어졌는지 본다. | return trigger를 D1 retention, activation rate, PQL로 환산하지 않는다. |
| `last_stop_point` | 직전 세션의 마지막 의미 지점. 예: 결과 카드, 저장 후 홈, cap/503, 저장 전 혼란, 자연 종료 | 다음 세션이 무엇을 이어받아야 하는지 본다. | 마지막 화면을 이탈 사유로 단정하지 않는다. J3 결과 카드 종료는 정상일 수 있다. |
| `resume_prompt_fit` | 재방문 시 사용자가 필요한 이어가기 말. 값: fits / absent / wrong / not-needed + 원문 메모 | 이어가기 힌트가 job과 맞는지 수기로 판단한다. | 곧바로 in-app prompt, push, email, 신규 이벤트로 만들지 않는다. |
| `second_value_signal` | 두 번째 가치 단서. 예: 같은 job 재사용, 누적 의미 이해, 다른 입력 재시도, 저장 기록 확인, "다음에도" 발화 | activation 뒤 retention 가능성을 분리해서 읽는다. | 한 번의 second value를 retention, habit, PMF, monetization으로 확정하지 않는다. |

## 3. Reading Rules

1. 세션 2는 "돌아왔는가"보다 "무엇을 이어 하려고 돌아왔는가"를 먼저 적는다.
2. 첫 세션의 `next_action_naturalness` 또는 `다시 열 이유`와 세션 2의 `session_2_return_trigger`가 같은 job 언어로 이어지면 reengagement 후보로 둔다.
3. `last_stop_point`가 B-AVAIL이면 가치 부족이 아니라 availability/friction이다.
4. J3는 `deed_judged` 후 저장 없이 종료하고 세션 2에서 다른 입력을 해보면 정상적인 AI 호기심 반복일 수 있다.
5. 세션 2가 없어도 실패로 쓰지 않는다. "미방문 + first value 도달 여부 + last stop point"까지만 남긴다.

## 4. J1-J4 Session 2 Sample Readings

### J1 기록형

- session_2_return_trigger: "어제 한 거 저장됐나 보고 오늘 것도 하나 남기려고요."
- last_stop_point: 저장 후 홈 / 최근 덕행 확인
- resume_prompt_fit: fits / 홈의 최근 기록이 이어가기 단서가 됨
- second_value_signal: 같은 일상 기록 job으로 두 번째 `deed_saved`
- 판독: 자연 종료 후 같은 기록 job으로 돌아온 사례다. 세션 2 재방문은 acquisition이 아니라 "기록이 남아 있다"는 첫 가치가 두 번째 기록으로 이어지는지 보는 retention 후보다.

### J2 누적 성장형

- session_2_return_trigger: "숫자가 더 올라가는지 보려고 다시 넣어봤어요."
- last_stop_point: 첫 저장 후 누적 숫자 확인
- resume_prompt_fit: fits / 누적 숫자가 다음 행동을 설명함
- second_value_signal: 두 번째 저장 뒤 누적 의미 언급
- 판독: 자연 종료 뒤 누적 payoff가 세션 2 동기가 된 사례다. 단, 두 번 저장을 habit 또는 PQL로 확정하지 않고 "누적 의미 이해" 후보로만 둔다.

### J3 AI 호기심형

- session_2_return_trigger: "다른 행동도 AI가 어떻게 보는지 궁금해서요."
- last_stop_point: 결과 카드에서 저장 없이 정상 종료
- resume_prompt_fit: not-needed / 저장 안내보다 다른 입력 재시도가 자연스러움
- second_value_signal: 다른 입력으로 두 번째 `deed_judged`
- 판독: 저장 없는 첫 종료가 마찰이 아니라 자연 종료였음을 보강하는 사례다. 세션 2의 핵심은 저장 유도 성공이 아니라 AI 관점 확인의 반복 가능성이다.

### J4 자기 반성형

- session_2_return_trigger: "어제 적은 걸 보니까 오늘도 정리하고 싶었어요."
- last_stop_point: 저장 후 홈 / 나중에 돌아볼 재료 인식
- resume_prompt_fit: fits / 이전 기록이 회고 루틴을 부름
- second_value_signal: 오늘 기록 저장 후 "며칠 모이면 보겠다" 발화
- 판독: 자연 종료 뒤 회고 루틴 후보가 생긴 사례다. 세션 2가 반복되더라도 비율화하지 않고, 같은 회고 언어가 여러 명에게 반복되는지만 본다.

## 5. Stop/Block Examples

| 상황 | 판정 | 다음 기록 |
|---|---|---|
| J1이 결과 카드에서 저장 전 멈추고 세션 2에서도 "어디서 끝나요?"라고 묻는다. | friction / B-LOST 후보 | 저장 후 완료감이 반복 마찰인지 별도 UX/copy proposal 후보로만 남긴다. |
| J2가 cap 또는 지연 때문에 돌아오지 않았다. | friction / B-AVAIL | value나 upgrade demand가 아니라 availability blocker로 분리한다. |
| J3가 첫 결과만 보고 만족해서 안 돌아온다. | normal_stop 또는 observe | 저장 부재와 미방문을 실패로 확정하지 않는다. 더 볼 입력이 있었는지 자기 말만 남긴다. |
| J4가 저장은 했지만 다시 볼 위치를 기억하지 못한다. | friction / resume_prompt_fit absent | 회고 재개 힌트 후보로 남기되 자동 nudge/public copy로 옮기지 않는다. |

## 6. Job-Specific Natural / Friction / Disinterest Examples

| Job | 자연 종료 예시 | 마찰 예시 | 무관심 예시 |
|---|---|---|---|
| J1 기록형 | 세션 1에서 저장 후 "내일 또 하나 남기면 되겠다"라고 말하고 종료. 세션 2에서 새 일상 기록으로 돌아오면 자연 반복 후보. | 결과 카드는 봤지만 저장 전 "끝난 건지 모르겠다"라고 멈춤. 세션 2에서도 저장 완료감을 못 찾으면 B-LOST 후보. | "그냥 한번 해본 거라 남길 건 없어요"라고 말하고 미방문. first value 전이면 관심 없음이 아니라 job mismatch 후보로만 둔다. |
| J2 누적 성장형 | 첫 저장 뒤 누적 숫자를 보고 "며칠 더 쌓이면 보겠다"라고 종료. 세션 2에서 숫자 변화 확인을 위해 돌아오면 자연 반복 후보. | 저장은 했지만 누적 payoff를 못 보고 "숫자가 왜 중요한지 모르겠다"라고 멈춤. B-MISMATCH 후보. | "점수 올라가는 건 별로 관심 없어요"라고 말하고 미방문. 단일 발화로 세그먼트 부적합을 확정하지 않는다. |
| J3 AI 호기심형 | `deed_judged` 결과를 보고 저장 없이 "다른 것도 넣어볼 수 있겠네요"라고 종료. 세션 2에서 다른 입력을 시도하면 자연 반복 후보. | AI 결과가 기대와 다르거나 mock/지연 때문에 "이게 진짜인가요?"라고 멈춤. B-MISMATCH 또는 B-AVAIL로 분리. | "한 번 보면 됐어요"라고 말하고 미방문. J3에서는 정상 종료와 무관심을 구분하기 위해 다른 입력 의향만 추가로 묻는다. |
| J4 자기 반성형 | 저장 후 "나중에 돌아보면 좋겠다"라고 종료. 세션 2에서 하루 정리를 다시 남기면 자연 루틴 후보. | 저장은 했지만 이전 기록 위치를 못 찾아 "어디서 다시 봐요?"라고 묻는다. resume prompt absent / B-LOST 후보. | "돌아볼 정도는 아니에요"라고 말하고 미방문. 회고 job 부적합 후보로만 두고 retention 실패로 환산하지 않는다. |

## 7. Approval Boundary

- 허용: 내부 companion 문서, 손기록 칸, synthetic sample reading, 기존 관찰표와 병행 사용.
- 금지: 신규 tracking/event/property, dashboard/session replay, 프로덕션 UI/copy, 공개 발송, push/email/in-app message, 배포, 비용, 권한, 개인정보 변경.
- 후속 분리 조건: 같은 `last_stop_point` 또는 `resume_prompt_fit` 문제가 실제 첫 사용자 2명 이상에서 반복될 때만 별도 proposal intent로 분리한다.

## 8. Learning Note

이번 작업은 durable learning을 바꾸지 않는다. 새 후보는 report에 보류한다.

> Multi-session onboarding for Virtue should separate first-session activation from session 2-3 reengagement by recording the return trigger, last stop point, resume prompt fit, and second value signal by job. In prelaunch, these are manual observation fields, not retention metrics or messaging triggers.
