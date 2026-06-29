# research-24 기록→출판 3줄 포맷 첫 적용

- id: research-24
- status: active
- created_at: 2026-06-29T0028Z
- projects: [infinity, research-bank, personal-ops]
- task_type: workflow-draft
- topics: [workflow, content, review, publication]
- priority: medium
- source: user-requested 24h Infinity distribution, priority 3

## Goal

`research-21`에서 나온 기록→출판 루프를 실제 일일 기록에 바로 쓸 수 있는 `capture / claim / open_loop` 3줄 포맷 초안으로 줄인다.

## Why Now

최근 회고, Threads 후보, 카드뉴스 산출물에서 같은 원본 기록이 매번 새로 해석되며 기준이 흔들렸다. 이번 작업은 큰 자동화가 아니라, 하루 기록을 다음 산출물로 넘길 때 변하지 않아야 할 최소 필드를 먼저 고정하는 데 목적이 있다.

## Scope

- `research-21`의 기록→출판 시스템 제안을 읽고 핵심만 계승한다.
- 최근 회고/카드뉴스/Threads 피드백을 반영해 일일 기록 3줄 포맷 초안을 만든다.
- 포맷은 실제 사람이 하루 끝에 빠르게 쓸 수 있어야 한다.
- 회고, Threads 후보, 카드뉴스 입력으로 재사용될 때 어떤 필드를 읽어야 하는지 적는다.

## Success Criteria

- `capture / claim / open_loop` 3줄의 의미가 겹치지 않는다.
- 사용자의 고민과 SAM의 운영 처리를 섞지 않는 규칙이 포함된다.
- Threads 후보가 사용자의 고민에서 출발하도록 연결된다.
- 결과가 `artifacts/research-24/`에 한 장 문서로 남는다.
- HTML report가 `reports/research-24/`에 생성된다.

## Guardrails

- 새 대형 자동화를 만들지 않는다.
- 사용자의 할 일을 늘리는 포맷으로 만들지 않는다.
- Markdown 표를 기본 출력 구조로 쓰지 않는다.
- 나래/Naver Shopping 대기 건과 섞지 않는다.

## References

- `intents/archive/research-21.md`
- `artifacts/research-21/record-to-publication-systems.md`
- `workflows/heartbeat.md`
- workspace review/Threads preference docs as needed

