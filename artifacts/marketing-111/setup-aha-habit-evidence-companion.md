# Virtue first-10 setup / aha / habit evidence companion

- intent: `marketing-111`
- source note: `/home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-07-18-activation-milestone-selection-with-low-data.md`
- scope: docs-only / first-10 observation companion
- permission: L1 docs-only
- status: internal companion

## 0. Purpose

Virtue is still prelaunch, so the first 10 sessions should not turn `deed_judged`, `deed_saved`, or `returned` into a final activation milestone too early. This companion adds three manual evidence columns beside the existing `marketing-79` first-10 observation table and the `marketing-108` first-value path audit:

- `setup 증거`: the user prepared enough context for Virtue to create value.
- `aha 증거`: the user recognized the first value in their own words or behavior.
- `habit 후보 증거`: the user left a plausible reason to return to the same job.

These are observation fields only. They do not create new events, product copy, UI, tracking, dashboards, session replay, deployment, cost, or external messaging.

## 1. Inherited Criteria

| 기준 | 계승 내용 | 이번 문서의 적용 |
|---|---|---|
| First Value Mapping | J1/J2/J4 = `deed_saved`, J3 = `deed_judged` | `aha 증거`는 잡별 first value 위치와 분리해서 적는다. |
| Prelaunch Decision Boundary | 첫 10명은 비율이나 milestone 확정이 아니다. | setup/aha/habit을 activation rate로 환산하지 않는다. |
| Message Confusion As Evidence | 사용자 언어는 결정이 아니라 증거다. | 세 칸 모두 원문·행동 단서 중심으로 남긴다. |
| First-User Learning Loop | 첫 사용자는 문제 언어와 자기 말 가치로 읽는다. | 반복되는 setup 부족, aha 순간, habit 이유만 다음 후보로 넘긴다. |
| Session Value Is Read By Job | 같은 이벤트도 잡별 종료 성격이 다르다. | J3의 무저장 종료를 habit 부재나 실패로 자동 판정하지 않는다. |

## 2. Add-On Columns

기존 첫 10명 관찰표의 사용자별 행 옆에 아래 세 칸을 붙인다.

| 칸 | 적는 값 | 이벤트와의 관계 | 금지선 |
|---|---|---|---|
| `setup 증거` | 사용자가 자기 상황, 행동, 기대 결과를 충분히 넣었다는 원문·행동 단서 | `/add 시작` 또는 입력 완료와 같지 않다. 맥락이 빈 입력이면 setup 불충분일 수 있다. | setup 있음만으로 activation, PMF, retention을 판정하지 않는다. |
| `aha 증거` | 결과를 보고 "아, 이게 가치구나"라고 알아본 말·표정·행동 | J1/J2/J4는 저장 후에 강해질 수 있고, J3는 `deed_judged` 직후에도 가능하다. | `deed_judged` 또는 `deed_saved` 발화만으로 aha를 확정하지 않는다. |
| `habit 후보 증거` | 같은 job으로 다시 올 이유, 다음에 넣을 소재, 다시 볼 맥락 | `returned`나 D1 재방문 전에도 후보 언어가 있을 수 있고, 재방문이 있어도 이유가 없으면 불명이다. | 첫 10명에서 habit, retention, D7 성공률로 환산하지 않는다. |

## 3. Reading Order

1. 먼저 traffic source를 분리한다: 사람 실사용 / maker self-test / synthetic / mock.
2. 잡을 추정한다: J1 기록형, J2 누적형, J3 AI 호기심형, J4 회고형, 불명.
3. `setup 증거`를 본다: 사용자가 가치가 나올 재료를 넣었는가.
4. `aha 증거`를 본다: 사용자가 첫 결과를 자기 말로 알아봤는가.
5. `habit 후보 증거`를 본다: 같은 job으로 다시 올 이유가 생겼는가.
6. 마지막에만 잡별 first value 이벤트와 대조한다: J1/J2/J4 = `deed_saved`, J3 = `deed_judged`.

## 4. J1-J4 Sample Readings

### J1 기록형

| 칸 | 예시 기록 |
|---|---|
| setup 증거 | "오늘 산책한 거 하나 남겨볼게요"라고 말하고 구체적 행동을 입력했다. |
| aha 증거 | 저장 후 "이런 식으로 남으면 일기보다 가볍네요"라고 말했다. |
| habit 후보 증거 | "내일도 하나만 적어두면 되겠네요"라고 다음 기록 소재를 말했다. |
| 판독 | `deed_saved`가 first value지만, 핵심은 저장 이벤트 자체보다 "가볍게 남는 기록"을 알아본 언어다. |

### J2 누적 성장형

| 칸 | 예시 기록 |
|---|---|
| setup 증거 | 오늘 행동을 입력하면서 "쌓이면 얼마나 되는지 보고 싶다"고 기대를 말했다. |
| aha 증거 | 저장 후 점수·덕력 표시를 보고 "이게 계속 쌓이는 거군요"라고 반응했다. |
| habit 후보 증거 | "며칠 더 넣으면 변화가 보이겠네요"라고 누적 확인 이유를 말했다. |
| 판독 | 첫 `deed_saved`는 누적의 시작점이다. habit 후보는 수치 상승 자체보다 다시 확인할 이유의 언어로 본다. |

### J3 AI 호기심형

| 칸 | 예시 기록 |
|---|---|
| setup 증거 | "AI가 이 행동을 어떻게 볼지 궁금하다"며 판단받을 행동을 입력했다. |
| aha 증거 | 결과 카드에서 "생각보다 바로 관점이 나오네요"라고 말하고 저장 없이 닫았다. |
| habit 후보 증거 | "다음엔 애매한 행동을 넣어보고 싶다"고 재시도 소재를 말했다. |
| 판독 | J3 first value는 `deed_judged`다. 저장 없는 종료는 정상일 수 있으며, habit 후보는 저장 의향이 아니라 다른 입력을 떠올렸는지로 본다. |

### J4 회고형

| 칸 | 예시 기록 |
|---|---|
| setup 증거 | "나중에 돌아볼 수 있게 오늘 후회한 일을 남기고 싶다"고 맥락을 말했다. |
| aha 증거 | 저장 후 "이렇게 남겨두면 나중에 다시 볼 수 있겠네요"라고 말했다. |
| habit 후보 증거 | "주말에 이번 주 것들을 보면 좋겠다"고 회고 시점을 말했다. |
| 판독 | J4는 `deed_saved` 뒤 회고 재료가 남아야 강하다. habit 후보는 반복 입력보다 돌아볼 장면의 존재다. |

## 5. Boundary

- 허용: 내부 문서, 수기 관찰 칸, synthetic sample reading, 기존 companion 보조.
- 금지: 공개 카피, UI 변경, 신규 이벤트/속성/tracking/privacy/dashboard/session replay, 배포, 비용, 권한 변경.
- 보류: 같은 setup 부족, aha 부재, habit 후보 부재가 반복될 때만 별도 proposal intent로 다룬다.

## 6. Learning Note

이번 작업은 durable marketing learning을 바꾸지 않는다. 다음 작업에 넘길 보류 후보는 다음과 같다.

> In the first 10 Virtue sessions, setup, aha, and habit evidence should be recorded as separate manual proof layers before choosing any activation milestone. Events say what happened; these columns preserve whether the user prepared value, recognized value, and named a reason to return.
