# proposer-blocker-20260720 Signal-to-intent proposer cron runs 호출 형식 수리

- status: resolved
- resolved_at: 2026-07-21T05:36Z
- approved_by: user
- projects: openclaw,infinity
- type: maintenance
- topics: automation,cron,workflow

## 결과

사용자 승인 후 `openclaw cron runs` 호출 형식 오류를 해소했다.

## 원인

`Signal-to-intent proposer`가 cron 실행 이력 확인 시 job id 없이 `openclaw cron runs`를 호출해 `Missing required option "--id <id>"` 오류가 발생했다.

## 조치

- proposer job id를 `1a881731-a2f7-4faa-965f-dfbba9bac0e1`로 확인했다.
- `openclaw cron runs --id 1a881731-a2f7-4faa-965f-dfbba9bac0e1 --limit 5`로 실행 이력 조회를 검증했다.
- `/home/ubuntu/.openclaw/workspace/system/docs/SIGNAL_TO_INTENT_PROPOSER.md`에 id 포함 호출 규칙을 추가했다.
- 실제 `Signal-to-intent proposer` cron payload에도 같은 규칙을 반영했다.

## 검증

- `openclaw cron runs --help`에서 `--id <id>` 필수 옵션 확인.
- proposer 최근 5개 run 조회 성공.
- `openclaw cron get 1a881731-a2f7-4faa-965f-dfbba9bac0e1`에서 새 payload 문구 확인.

## 다음

다음 정기 실행은 2026-07-21T21:30:00Z 예정이다. 새 실패가 없으면 추가 사용자 판단은 필요 없다.
