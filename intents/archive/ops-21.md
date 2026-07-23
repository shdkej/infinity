# ops-21 Marketing SNS review 고비용 NO_REPLY 루프 축소

- status: archived
- completed_at: 2026-07-23T07:40Z
- projects: openclaw,infinity
- type: maintenance
- topics: marketing,cron,cost
- source_signal: openclaw cron runs#Marketing-agent-SNS-review-repeated-high-token-NO_REPLY-2026-07-18..2026-07-21
- report: reports/ops-21/20260723T0740Z.html

## Outcome

`Marketing agent SNS review` live cron payload에 `NO_ACTION BOUNDED SCAN UPDATE 2026-07-23`를 추가했다. 무소재 회차는 먼저 최근 사용자 여행/콘텐츠/카드뉴스 신호, 승인 대기, 공개 콘텐츠, SNS 반응 신호만 좁게 확인한 뒤, 신호가 없으면 `no_action` JSONL trace를 남기고 즉시 `NO_REPLY`로 종료한다.

`system/docs/MARKETING_AGENT_INTERNAL_INBOX.md`에도 같은 조기 종료 경계를 고정했다.

## Verification

- `openclaw cron edit 4f272a0a-e0b4-46f3-a737-7e089c45b298` 성공
- 반환된 cron payload에 `NO_ACTION BOUNDED SCAN UPDATE 2026-07-23` 포함

## Follow-Up Measurement

다음 3회 무소재 실행에서 duration/input tokens가 기존 4.7만~6.6만 token 회차보다 낮아지는지 확인한다.

