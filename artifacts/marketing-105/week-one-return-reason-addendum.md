# Virtue 첫 주 재방문 이유 companion

- intent: marketing-105
- scope: 첫 10명 관찰표의 D1-D7 재방문 이유 보조 칸
- use_with: artifacts/marketing-79/week-one-activation-observation-table.html
- inherits: artifacts/marketing-104/first-value-retention-gate-addendum.md

## 기준

첫 주 재방문은 횟수보다 "같은 job으로 다시 올 이유가 생겼는가"를 먼저 본다. 사용자가 다시 올 상황을 자기 말로 설명할 수 있으면 재방문 이유를 남기고, 없으면 실패가 아니라 보류로 둔다.

- `첫 주 재방문 이유`: D1-D7 사이에 다시 열 이유를 사용자가 자기 말로 말한 문장 또는 행동 맥락
- `같은 job`: 첫 세션의 J1-J4와 같은 목적선으로 돌아오는가
- `다른 job`: 호기심, 테스트, 공유, 기록처럼 목적이 바뀌었으면 같은 재방문으로 합산하지 않음
- `미방문`: 실패가 아니라 RC-WARM / RC-PRE-LOST / RC-NORMAL / RC-AVAIL / RC-EXCLUDED 후보로만 분류

## 관찰 카드에 추가할 칸

각 사용자 카드의 `D1 재방문` 아래 또는 marketing-104 보조 4줄 아래에 아래 3줄을 붙인다.

| 칸 | 기록 방법 | 판정 기준 |
|---|---|---|
| 첫 주 재방문 이유 | 사용자가 말한 원문 1문장 또는 관찰자가 본 상황 1개 | "다음에 언제 다시 쓰겠는가"가 같은 job 언어로 보이는가 |
| 같은 job 유지 | `예 / 아니오 / 불명` | 첫 세션 job과 같은 first value를 다시 원하면 예 |
| 재방문 성격 | `RC-WARM / RC-PRE-LOST / RC-NORMAL / RC-AVAIL / RC-EXCLUDED / 보류` | first value 도달 여부, 종료 성격, synthetic/self-test 여부를 분리 |

## J1-J4 예시

### J1 일상 기록형

- 첫 주 재방문 이유: "오늘도 산책한 거 남겨두려고 다시 열 것 같다"
- 같은 job 유지: `예`
- 읽는 법: `deed_saved` 이후 일상 기록을 다시 남기는 상황이면 RC-WARM 후보. 저장을 못 찾아 헤맨 뒤 "나중에 다시 해볼게"는 RC-PRE-LOST 후보이지 성공/실패 단정이 아니다.

### J2 누적 성장형

- 첫 주 재방문 이유: "며칠 쌓이면 숫자가 어떻게 되는지 보려고 다시 볼 것 같다"
- 같은 job 유지: `예`
- 읽는 법: 누적 확인 또는 두 번째 저장 욕구가 있으면 같은 job 재방문 이유. 단순히 AI가 또 뭐라고 하는지 보겠다는 말만 있으면 J3로 job이 바뀐 것일 수 있다.

### J3 AI 호기심형

- 첫 주 재방문 이유: "다른 행동도 한 번 평가받아보고 싶다"
- 같은 job 유지: `예`
- 읽는 법: J3는 `deed_judged` 후 저장 없이 끝나도 RC-NORMAL일 수 있다. 다시 올 이유가 "다른 예시를 판정해보기"라면 같은 job 유지, 저장을 하지 않았다는 이유만으로 실패로 읽지 않는다.

### J4 자기 반성형

- 첫 주 재방문 이유: "하루 끝에 내가 한 선택을 다시 적어보고 싶다"
- 같은 job 유지: `예`
- 읽는 법: 자기 반성 맥락으로 돌아오면 같은 job 유지. 점수만 구경하거나 친구에게 보여주기만 하려는 이유는 J3 또는 공유성 축으로 분리한다.

## 읽는 순서

1. 기존 `activation 판정`과 marketing-104의 `첫 가치 도달 시점`을 먼저 기록한다.
2. 첫 주 안에 실제 재방문 또는 재방문 의향 언어가 있으면 `첫 주 재방문 이유`를 원문으로 남긴다.
3. 그 이유가 첫 세션과 같은 job인지 분리한다.
4. 미방문은 실패로 단정하지 않고 RC 후보로만 둔다.
5. 첫 10명 prelaunch 표본에서는 재방문률, retention%, PMF, PQL, upgrade demand로 환산하지 않는다.

## 금지선

- 첫 주 재방문 없음 = activation 실패로 쓰지 않는다.
- 다른 job 호기심 방문을 같은 job retention으로 합산하지 않는다.
- `deed_save_capped`, 503, 지연은 RC-AVAIL이며 가치나 업그레이드 수요가 아니다.
- synthetic/mock/maker self-test는 RC-EXCLUDED로 분리한다.
- 공개 발송, 신규 이벤트, session replay, dashboard, privacy, 배포, 가격, 광고는 이 문서 범위 밖이다.
