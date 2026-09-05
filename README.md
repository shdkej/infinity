# infinity

Agent-First 자율 실행 시스템. 스케줄 routine(원격 에이전트)이 깨어나 `INTENTS.md`의 의도를 자율 처리하고, 의미 있는 변화는 원장/대시보드/정기 리캡으로 드러낸다.

> 사용자는 **의도와 판단**만, 에이전트는 **실행과 보고**를 담당한다.

## 구조

```
INTENTS.md          ← 활성 Intent (Inbox / Active / Waiting / Archive)
GATES.md            ← 승인 대기/처리 완료
PERMISSIONS.md      ← 권한 레벨(L0~L3) 정의
ARTIFACT_RULES.md   ← 산출물 경로 규칙
workflows/heartbeat.md ← Heartbeat 동작 프로토콜 (routine이 매 실행 시 읽음)
EVALUATION_INDEX.md / EVALUATION_NOTES.md ← evaluator 학습
EXECUTION_LEARNING_CONTRACT.md ← 대형 MVP 시간·병목·Red 학습 정본
intents/active/       ← 실행 중인 Intent 원장
                     유효 archive 원장만 Knowledge Lab의 source/infinity/archive/로 이동
artifacts/{id}/     ← 결과 산출물
reports/{id}/       ← 실행 로그
scripts/notify.sh   ← 레거시 Telegram 단일 발송기(새 terminal notifier는 사용하지 않음)
scripts/dispatch_terminal_notifications.py ← 원격 `origin/main` terminal 상태를 원 대화에 1회 조정·발송
```

## 태그 축

완료 archive에는 대시보드 필터링을 위해 세 축을 기록한다.

- `projects`: 관련 프로젝트. 1~3개, 복수 허용. 예: `virtue`, `infinity`, `agent-wiki`.
- `task_type`: 태스크 성격. 정확히 1개. 예: `research`, `strategy`, `implementation`, `maintenance`.
- `title`: 제목만 읽어도 대상·행동·산출물을 알 수 있는 한국어 태스크명. ID와 영어 내부 태그는 제목에 쓰지 않고 메타데이터로 분리한다.
- `topics`: 보조 주제. 0~3개. 예: `activation`, `analytics`, `workflow`.

정식 vocabulary와 archive 코멘트 표기는 `ARTIFACT_RULES.md`를 따른다.

## 정본과 대시보드 정합성

- `INTENTS.md`가 큐 상태의 단일 정본이다. 대시보드는 GitHub `main`의 raw `INTENTS.md`를 읽고, 로컬 파일이나 별도 큐를 상태 원천으로 사용하지 않는다.
- `INTENTS.md`에는 `## Inbox`, `## Active`, `## Waiting`, `## Archive`를 각각 정확히 한 번만 둔다. 중복 섹션은 검사에서 실패하며 대시보드에 숨겨진 항목을 만들 수 있다.
- 열린 intent는 반드시 해당 lane 아래 `### [id] 제목` 블록으로 둔다. `status` 값과 lane이 다르면 정합성 오류로 보고 수정한다.
- 원장 변경 후에는 `python3 scripts/check_intents_consistency.py INTENTS.md`를 실행하고, Infinity 원격 push 후 raw GitHub와 라이브 대시보드에서 같은 id·lane이 보이는지 확인한다.
- 대시보드 배포본은 `/home/ubuntu/workspace/space/infra-aws-static-sites/sites/infinity/dist/`에 두며, 정적 파일 push와 Space 라이브 확인까지 완료해야 한다.

## 운영 원칙

- **No-op이면 커밋하지 않는다.** 변화 없는 Heartbeat는 push하지 않아 git history와 dashboard가 조용히 유지된다.
- **아침 7시 리캡**은 GitHub scheduled workflow가 아니라 OpenClaw 로컬 cron(KST 07:00)이 소유한다. 리캡은 커밋 로그를 그대로 보내지 않고, Archive 완료·다음 Inbox/Active·대기 항목을 카드형으로 요약한다.
- 리캡의 시간대별 섹션은 `[로컬]` OpenClaw 라우터 실행과 `[클라우드]` 커밋/Archive/원격 기록을 한 타임라인에 합쳐 보여준다. 07:00 리캡은 terminal 통보를 대체하지 않는다.
- terminal notifier는 `origin/main`의 `INTENTS.md`만 조정한다. `notification_channel`, `notification_target`, 선택적 Telegram `notification_thread` 또는 Slack `notification_reply_to`가 intake에 보존된 intent만 원 대화에 보낸다. Archive는 `remote_verified: pass` 뒤에만, Waiting은 실제 `blocker` 또는 사용자 승인 조건이 있을 때만 후보가 된다. 읽기/no-op/반복 실행은 발송하지 않는다.
- `data/dispatcher-terminal-notifications.json`의 receipt key는 intent·terminal state·destination이다. 송신 전 durable claim을 남기며 `sent`, `failed_before_acceptance`, `delivery_unknown`을 기록한다. 불확실 수신은 자동 재송하지 않고 cron 실패 알림으로 표면화한다. 구형 `dispatcher-notification-state.json`은 destination이 없어 read-only 감사 대상으로만 유지한다.
- **Dispatcher 실행 계약**: 기존 host crontab의 10분 항목 하나만 `scripts/run_dispatcher_cycle.sh`를 호출한다. 이 스크립트는 `origin/main:INTENTS.md`의 단일 SHA를 intent 블록 단위로 파싱하고, 대시보드 action 결과와 실제 실행 계획을 분리한다. `Inbox → Active` 또는 stale Active 재개 후보는 Genie를 직접 `agent:genie:infinity-dispatcher` 세션으로 호출한다. 실행 증거는 `traces/{intent-id}.json`의 `dispatcher_handoff`와 repo 밖 `/home/ubuntu/.openclaw/state/infinity-dispatcher-runs/` cycle record에 남긴다. `actions=[]`는 버튼 큐가 비었다는 뜻일 뿐 작업 no-op가 아니다.
- **Trace 계약**: 새 intent는 `scripts/record_intent_trace.py intake`로 `traces/{intent-id}.json`에 원문 요청·정규화 쿼리와 정확히 하나의 intake event를 기록한다. 실행마다 `execution`으로 실제 Context Pack·검색·근거 경로를 남기고, 정상 원격 Archive 검증 뒤에만 `archive`로 final report·Red pass·원격 검증을 남긴다. 계약은 `schema/intent-trace-contract.md`가 정본이며 `python3 scripts/validate_intent_trace.py --all`을 원장 검사와 함께 실행한다. 레거시 backfill은 확인되지 않은 원문을 만들지 않고 `missing` 사유와 `partial` 상태를 남긴다.
- **실행 학습 계약**: 대형 MVP는 [`EXECUTION_LEARNING_CONTRACT.md`](EXECUTION_LEARNING_CONTRACT.md)의 역할별 UTC timing ledger, 예상 대비 실제·병목 측정, focused Red 프로토콜을 적용한다. 시간제한은 품질 게이트를 생략하는 근거가 될 수 없다.
- **Cloud prepares, Local executes**: 조사/계획/초안은 클라우드, 파일 수정/실행/검증은 로컬 Claude Code에 위임한다.

## 연동

- 원격 routine(claude.ai)이 이 레포를 clone → `workflows/heartbeat.md` 프로토콜대로 실행 → 의미 있는 변경을 커밋·push한다. 산출물·상태·Report·Archive는 Infinity 원격 push 확인 전 완료로 보지 않는다. **Infinity는 독립 저장소이며 Knowledge Lab 부모 저장소의 submodule pointer를 갱신하거나 push하지 않는다.**
- GitHub Actions push 알림은 쓰지 않는다. 아침 리캡은 OpenClaw cron이 `scripts/morning_recap_message.py`를 실행해 전달한다.
- 유효 판정된 archive 원장만 [Knowledge Lab](https://github.com/shdkej/knowledge-lab)의 `source/infinity/archive/`로 이동한다. 유효하지 않은 결과는 KL에 복사하지 않는다.
