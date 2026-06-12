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
intents/active|archive/ ← Intent 원장
artifacts/{id}/     ← 결과 산출물
reports/{id}/       ← 실행 로그
scripts/notify.sh   ← 승인/장애 등 명시적 알림용 Telegram 발송기
```

## 태그 축

완료 archive에는 대시보드 필터링을 위해 세 축을 기록한다.

- `projects`: 관련 프로젝트. 1~3개, 복수 허용. 예: `virtue`, `infinity`, `agent-wiki`.
- `task_type`: 태스크 성격. 정확히 1개. 예: `research`, `strategy`, `implementation`, `maintenance`.
- `topics`: 보조 주제. 0~3개. 예: `activation`, `analytics`, `workflow`.

정식 vocabulary와 archive 코멘트 표기는 `ARTIFACT_RULES.md`를 따른다.

## 운영 원칙

- **No-op이면 커밋하지 않는다.** 변화 없는 Heartbeat는 push하지 않아 git history와 dashboard가 조용히 유지된다.
- **아침 7시 리캡**은 GitHub scheduled workflow가 아니라 OpenClaw 로컬 cron(KST 07:00)이 소유한다. 리캡은 커밋 로그를 그대로 보내지 않고, Archive 완료·다음 Inbox/Active·대기 항목을 카드형으로 요약한다.
- **Cloud prepares, Local executes**: 조사/계획/초안은 클라우드, 파일 수정/실행/검증은 로컬 Claude Code에 위임한다.

## 연동

- 원격 routine(claude.ai)이 이 레포를 clone → `workflows/heartbeat.md` 프로토콜대로 실행 → 필요한 경우 커밋·push.
- GitHub Actions push 알림은 쓰지 않는다. 아침 리캡은 OpenClaw cron이 `scripts/morning_recap_message.py`를 실행해 전달한다.
- [knowledge-lab](https://github.com/shdkej/knowledge-lab)에 submodule로 포함되어 통합 지식 허브에서 함께 조회된다.
