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
intents/active/       ← 실행 중인 Intent 원장
                     유효 archive 원장만 Knowledge Lab의 source/infinity/archive/로 이동
artifacts/{id}/     ← 결과 산출물
reports/{id}/       ← 실행 로그
scripts/notify.sh   ← 승인/장애 등 명시적 알림용 Telegram 발송기
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
- 리캡의 시간대별 섹션은 `[로컬]` OpenClaw 라우터 실행과 `[클라우드]` 커밋/Archive/원격 기록을 한 타임라인에 합쳐 보여준다. 별도 라우터 요약 알림은 기본적으로 보내지 않는다.
- **Cloud prepares, Local executes**: 조사/계획/초안은 클라우드, 파일 수정/실행/검증은 로컬 Claude Code에 위임한다.

## 연동

- 원격 routine(claude.ai)이 이 레포를 clone → `workflows/heartbeat.md` 프로토콜대로 실행 → 의미 있는 변경을 커밋·push한다. 산출물·상태·Report·Archive는 Infinity 원격 push 확인 전 완료로 보지 않으며, Knowledge Lab submodule 사용 시 parent pointer push까지 필수다.
- GitHub Actions push 알림은 쓰지 않는다. 아침 리캡은 OpenClaw cron이 `scripts/morning_recap_message.py`를 실행해 전달한다.
- 유효 판정된 archive 원장만 [Knowledge Lab](https://github.com/shdkej/knowledge-lab)의 `source/infinity/archive/`로 이동한다. 유효하지 않은 결과는 KL에 복사하지 않는다.
