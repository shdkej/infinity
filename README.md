# infinity

Agent-First 자율 실행 시스템. 스케줄 routine(원격 에이전트)이 깨어나 `INTENTS.md`의 의도를 자율 처리하고, 의미 있는 변화가 있을 때만 Telegram으로 알린다.

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
scripts/notify.sh   ← Telegram 발송기
.github/workflows/heartbeat-notify.yml ← push/스케줄 기반 Telegram 알림
```

## 운영 원칙

- **No-op이면 커밋하지 않는다.** 변화 없는 Heartbeat는 push하지 않아 알림 노이즈가 없다. push = 의미 있는 변화.
- **아침 8시 리캡**은 push와 독립된 스케줄(`cron: 0 23 * * *`, KST 08:00)로 보장된다.
- **Cloud prepares, Local executes**: 조사/계획/초안은 클라우드, 파일 수정/실행/검증은 로컬 Claude Code에 위임한다.

## 연동

- 원격 routine(claude.ai)이 이 레포를 clone → `workflows/heartbeat.md` 프로토콜대로 실행 → 커밋·push.
- `heartbeat-notify.yml`이 Telegram 알림을 보낸다. 필요한 GitHub Secrets: `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`.
- [knowledge-lab](https://github.com/shdkej/knowledge-lab)에 submodule로 포함되어 통합 지식 허브에서 함께 조회된다.
