# ops-26 산출물 — 산출물 Intent 지표 질문 계약

## 결정

`metric_question`은 모든 비단순 산출물 Intent에 요구한다. 단순 조회·상태 확인은 예외다.

## 최소 필드

- `metric_question`: 무엇이 바뀌면 다음 결정을 바꿀 것인가?
- `metric_signal`: 관찰할 신호와 출처
- `metric_decision_rule`: `continue | change | hold`로 이어지는 판정 규칙

완료 report와 Archive에는 `metric_result`, `metric_next_decision`을 남긴다. 신호가 없으면 실패가 아니라 `null` 또는 `hold`로 기록한다.

## 적용 파일

- `source/openclaw-system/docs/INFINITY_OPERATING_RULES.md`
- `infinity/workflows/heartbeat.md`
- `infinity/docs/index.html`
