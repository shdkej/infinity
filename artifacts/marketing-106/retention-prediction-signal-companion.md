# Virtue retention 예측 신호 companion

- intent: marketing-106
- scope: 첫 10명 관찰표의 activation 이후 retention 예측 보조 칸
- use_with: artifacts/marketing-79/week-one-activation-observation-table.html
- inherits:
  - artifacts/marketing-104/first-value-retention-gate-addendum.md
  - artifacts/marketing-105/week-one-return-reason-addendum.md

## 기준

Activation은 잡별 first value 도달 여부이고, retention 예측 신호는 "같은 이유로 다시 쓸 가능성"이 보이는지다. 저장 여부는 activation의 보조 증거일 수 있지만, 같은 job으로 다시 올 근거와 같은 칸에 쓰지 않는다.

- `저장 여부`: `deed_saved` 완료 여부와 저장 직후 반응
- `같은 job 재방문 근거`: 첫 세션과 같은 목적선으로 다시 열 상황, 말, 행동
- `retention 예측 신호`: 반복 사용 가능성을 시사하는 off-instrument 관찰
- `신호 강도`: `강함 / 약함 / 없음 / 불명`

## 관찰 카드에 추가할 칸

각 사용자 카드의 `독립 2판정` 및 marketing-105의 `첫 주 재방문 이유` 아래에 아래 4줄을 붙인다.

| 칸 | 기록 방법 | 판정 기준 |
|---|---|---|
| 저장 여부 | `예 / 아니오 / 불명` + 저장 직후 반응 1개 | 저장은 J1/J2/J4 activation 보조 증거지만 retention 근거로 자동 승격하지 않음 |
| 같은 job 재방문 근거 | 원문 발화 또는 행동 맥락 1개 | 첫 세션 job과 같은 first value를 다시 원한다는 근거가 있는가 |
| retention 예측 신호 | `강함 / 약함 / 없음 / 불명` | 같은 job 재방문 근거가 구체적이면 강함, 단순 호기심이면 약함 |
| 첫 verification gate | `저장 여부와 같은 job 재방문 근거가 분리 기록됨 / 미분리` | 두 필드가 섞이면 retention 예측으로 사용하지 않음 |

## J1-J4 예시

### J1 일상 기록형

- 저장 여부: `예`, 저장 후 "오늘 한 일이 남는 느낌이네"
- 같은 job 재방문 근거: "내일도 산책하면 또 남겨둘 것 같다"
- retention 예측 신호: `강함`
- 읽는 법: 저장 자체보다 "내일도 같은 일상 기록을 남김"이 반복 근거다.

### J2 누적 성장형

- 저장 여부: `예`, 홈에서 덕력 또는 누적 숫자를 확인함
- 같은 job 재방문 근거: "며칠 쌓이면 숫자가 어떻게 바뀌는지 보고 싶다"
- retention 예측 신호: `강함`
- 읽는 법: 두 번째 저장이나 누적 확인 욕구가 있어야 같은 job 신호다. 점수 구경만 반복하려는 말은 J3 가능성으로 보류한다.

### J3 AI 호기심형

- 저장 여부: `아니오`, `deed_judged` 후 결과를 읽고 종료
- 같은 job 재방문 근거: "다른 행동도 한 번 평가받아보고 싶다"
- retention 예측 신호: `강함`
- 읽는 법: J3는 저장 없음이 약한 신호가 아니다. 반복 판정 욕구가 같은 job 재방문 근거다.

### J4 자기 반성형

- 저장 여부: `예`, 저장 후 "오늘 선택을 다시 보게 된다"
- 같은 job 재방문 근거: "하루 끝에 다시 적어보면 정리가 될 것 같다"
- retention 예측 신호: `강함`
- 읽는 법: 반성 루틴으로 돌아오는 상황이 있어야 retention 예측 신호다. 저장 후 단순 공유 의향은 공유성 축으로 분리한다.

## 읽는 순서

1. marketing-79의 잡별 activation 판정을 먼저 기록한다.
2. marketing-104의 첫 가치 도달 신호를 별도로 기록한다.
3. 저장 여부를 기록하되, 저장 자체를 retention 예측 신호로 쓰지 않는다.
4. 같은 job으로 다시 열 근거를 원문 또는 행동 맥락으로 남긴다.
5. 저장 여부와 같은 job 재방문 근거가 분리되어 있을 때만 retention 예측 신호를 읽는다.

## 금지선

- `deed_saved` 1회를 retention, PMF, PQL, upgrade demand로 읽지 않는다.
- J3의 무저장 종료를 retention 약함으로 읽지 않는다.
- 다른 job 호기심 방문을 같은 job retention으로 합산하지 않는다.
- 첫 10명 prelaunch 표본에서 retention%, activation rate, conversion rate를 산출하지 않는다.
- 신규 이벤트, dashboard, session replay, privacy, 배포, 공개 카피, 외부 발송, 비용 변경은 이 문서 범위 밖이다.

## 계승한 기준

- First Value Mapping: J1/J2/J4는 `deed_saved`, J3는 `deed_judged`.
- Prelaunch Decision Boundary: 첫 10명 표본은 정성 손기록 재료이며 비율 판단이 아니다.
- First-Week Non-Return Is A Reactivation Candidate, Not A Failure: 미방문은 실패가 아니라 후보 분류다.

## 다음 작업에 넘길 규칙

첫 10명 실제 기록에서 `저장 여부=예`인데 `같은 job 재방문 근거=없음/불명`이 반복되면 저장 후 누적 의미 또는 다음 행동 명료성 문제를 별도 UX intent로 분리한다.
