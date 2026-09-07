# Slack 버튼 callback → 다음 action 연결

## 구현 범위

- `scripts/process_slack_callbacks.py`는 outbound sent registry를 먼저 기록하고, ingress가 검증한 `block_action/button` event를 처리한다.
- registry와 inbound는 `provider/workspace/channel/message/thread/user/value/intent/run/question` 복합 키로 대조한다. `actionId`는 진단용이며 분기 키가 아니다.
- callback event id와 question id는 flock 보호 state ledger에서 first-wins로 claim한다. 재수신과 다른 버튼의 후속 클릭은 dispatch·동일 thread reply를 만들지 않는다.
- claim은 Intent 수정·artifact 작성·outbox 기록보다 먼저 atomic 저장한다. state는 `claimed → dispatched → receipt_written → reported`로 각 단계마다 atomic 저장한다. `dispatched` 재수신은 `dispatch_uncertain`, 그 밖의 미종결 receipt는 `delivery_unknown`으로 바꾸고 원 Intent를 Waiting·재개 조건으로 남기며 자동 재실행·재보고하지 않는다.
- 안전 allowlist(`set_intent_next_action`, `prepare_local`, `create_followup_question`)만 원 Intent의 `next_action`에 연결한다. 공개·외부 발송·비용·권한·시크릿·프로덕션/파괴 action은 `approval_required`로만 기록하고 실행하지 않는다.
- 결과 보고는 registry에 저장된 `channel_id`와 `thread_ts`로 JSONL mock outbox에 남긴다. 실제 Slack 전송은 별도 승인된 transport가 담당하며, 이 worker는 전송하지 않는다.

## 역할 수렴

- **Planner:** callback 선택을 현재 사용자 결정으로 취급하되, 유효성·만료·원 thread binding이 없으면 후속 action을 실행하지 않는다.
- **Developer:** dashboard S3 큐와 책임을 섞지 않고 별도 worker·durable ledger·회귀 테스트로 구현한다.
- **Marketer:** 수신·연결·결과를 같은 thread에서 사람이 읽는 한국어로 구분하며, 승인 필요를 완료로 오인시키지 않는다.
- **Operator:** runtime ledger는 Git에서 제외하고 atomic write + flock를 사용한다. 불확실한 외부 delivery는 자동 재전송하지 않는다.

## 검증 계약

`scripts/test_process_slack_callbacks.py`는 새 프로세스 3회에서 각각 `수신 → 원 Intent next_action 연결 → 같은 thread receipt`를 확인하고, 각 event replay가 outbox/Intent 변경을 추가하지 않음을 검증한다. wrong-thread와 protected action도 dispatch하지 않는 회귀 케이스를 포함한다.
