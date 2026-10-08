# Dispatcher 구현 참고

이 문서는 Infinity 디스패처의 코드 수준 동작을 설명합니다. 운영자가 따라야 할 순서와 상태 원칙은 [README.md](../README.md)와 각 정본 문서를 우선합니다.

## 실행 진입점

- 스케줄 진입점: `scripts/run_dispatcher_cycle.sh`
- 계획 생성: `scripts/prepare_dispatch_cycle.py`
- 대시보드 액션 소비: `scripts/process_action_requests.py`
- terminal 통보: `scripts/dispatch_terminal_notifications.py`
- trace 기록: `scripts/record_intent_trace.py`
- 실행 cycle 기록: `/home/ubuntu/.openclaw/state/infinity-dispatcher-runs/`

## 한 사이클의 내부 순서

1. `git pull --ff-only origin main`으로 작업 저장소를 동기화합니다.
2. `git fetch --prune origin main` 후 `FETCH_HEAD`와 `origin/main` SHA가 같은지 확인합니다.
3. 최신 `origin/main`으로 검증용 detached worktree를 만듭니다.
4. `prepare_dispatch_cycle.py`가 `INTENTS.md`를 읽어 promotion, resume, plan activation, expansion, terminalization 후보를 계산합니다.
5. terminal notification과 대시보드 action queue를 처리합니다.
6. 대시보드 action이 원장을 바꾸면 계획을 다시 계산합니다.
7. handoff 대상마다 `dispatcher_handoff` trace를 남기고 Genie 실행 세션에 넘깁니다.
8. 실행 뒤 원격 상태와 계획을 다시 읽어 실행 증거와 상태 전이를 검증합니다.
9. terminal notification을 다시 조정하고 cycle record를 저장합니다.

## 격리·중복 방지

- OpenClaw 스케줄은 `sessionTarget=isolated`, 실행 에이전트는 `genie`입니다.
- 디스패처 실행 세션 키 기본값은 `agent:genie:infinity-dispatcher-v2`입니다.
- `flock` 잠금으로 이전 사이클이 끝나지 않은 동안 중복 사이클을 시작하지 않습니다.
- Genie 실행은 기본 480초, 전체 크론은 600초 제한입니다.
- 장기 작업은 task-plan의 의존성·ready leaf를 기준으로 한 번에 실행하며, `expansion_policy`가 있는 경우에만 제한된 batch를 추가합니다.

## 환경변수

- `INFINITY_DISPATCHER_STATE_DIR`: cycle record 저장 경로
- `INFINITY_TERMINAL_STATE_FILE`: terminal notification receipt 경로
- `INFINITY_DISPATCHER_LOCK_FILE`: 단일 실행 잠금 경로
- `INFINITY_DISPATCHER_AGENT_TIMEOUT_SECONDS`: Genie 실행 제한 시간
- `INFINITY_DISPATCHER_SESSION_KEY`: Genie handoff 세션 키

## 점검 명령

```bash
git fetch origin main
git rev-parse HEAD
git rev-parse origin/main
python3 scripts/prepare_dispatch_cycle.py --repo . --json
python3 scripts/check_intents_consistency.py INTENTS.md
python3 scripts/validate_intent_trace.py --all
```

`HEAD`와 `origin/main`이 다르거나 정합성·trace 검증이 실패하면 완료로 보고하지 않습니다.
