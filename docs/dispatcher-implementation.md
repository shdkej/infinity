# Dispatcher 구현 참고

이 문서는 Infinity 디스패처의 코드 수준 동작을 설명합니다. 운영자가 따라야 할 순서와 상태 원칙은 [README.md](../README.md)와 각 정본 문서를 우선합니다.

## 실행 진입점

- 작업 실행 진입점: `scripts/run_registered_dispatcher_cycle.sh` (등록된 프로젝트 디스패처 wrapper)
- 대시보드 버튼 처리 진입점: `scripts/run_dashboard_actions_cron.sh`
- 알림 발송 진입점: `scripts/run_notification_cron.sh`
- 계획 생성: `scripts/prepare_dispatch_cycle.py`
- 대시보드 액션 소비 구현: `scripts/process_action_requests.py`
- terminal 및 상태변경 통보 구현: `scripts/dispatch_terminal_notifications.py`
- trace 기록: `scripts/record_intent_trace.py`
- 프로젝트 실행자 해석: `scripts/project_executor_registry.py`, `data/project-executors.yaml`
- 실행 cycle 기록: `/home/ubuntu/.openclaw/state/infinity-dispatcher-runs/`

## 한 사이클의 내부 순서

1. 기존 canonical checkout이 `main`이 아니면 보존 가능한 경우에만 기존 `main`으로 전환하고, `git pull --ff-only origin main`으로 동기화합니다.
2. `git fetch --prune origin main` 후 `FETCH_HEAD`, `origin/main`, canonical checkout의 `HEAD`가 모두 같은 SHA인지 확인합니다. 일치하지 않으면 계획·쓰기 단계에 진입하지 않고 nonzero exit로 크론 실패를 기록합니다.
3. 최신 `origin/main`으로 검증용 detached worktree를 만듭니다.
4. `prepare_dispatch_cycle.py`가 `INTENTS.yaml`을 읽어 promotion, resume, plan activation, expansion, terminalization 후보를 계산합니다.
5. handoff 대상마다 `dispatcher_handoff` trace를 남기고 Genie 실행 세션에 넘깁니다.
6. 실행 뒤 원격 상태와 계획을 다시 읽어 실행 증거와 상태 전이를 검증합니다.
7. 작업 실행 cycle record를 저장합니다.

디스패처는 OpenClaw automation `Infinity dispatcher (origin/main)`(ID `033a86c8-758b-4639-897e-c67b79785e91`)에서 10분마다 `bash scripts/run_registered_dispatcher_cycle.sh`로 실행합니다. OpenClaw 스케줄 원장을 단일 주 스케줄러로 사용하며, system crontab에는 디스패처를 중복 등록하지 않습니다. 기존 자동화 항목을 재사용하며 새 working checkout이나 별도 job은 만들지 않습니다. dispatcher 스크립트가 계획 검증 때 만드는 임시 detached worktree는 검증에만 쓰며, 작업·trace 기록은 canonical `main` checkout에서 수행합니다.

대시보드 버튼과 상태/완료 알림은 디스패처와 분리된 OpenClaw automation으로 각각 10분 간격 실행됩니다. `Infinity dashboard action consumer`(ID `96de3438-03de-443e-a558-bbf84d902743`)는 UTC 기준 `1-59/10`, `Infinity notification reconciler`(ID `bc3e54e3-70f3-43f3-9909-c451b57ec531`)는 UTC 기준 `2-59/10`에 실행합니다. 버튼 작업은 원격 `origin/main`을 확인한 뒤 S3 action queue를 소비하고, 원장 변경을 별도 커밋·push합니다. 알림 작업은 `origin/main`의 원장을 읽어 PNG 카드·텍스트 fallback·승인 버튼을 exactly-once로 발송하며, 생성·상태·terminal 알림의 목적지는 Telegram 대화 `433493318`입니다. 세 OpenClaw 작업 모두 실행 실패 알림도 같은 Telegram 대화로 보냅니다. 각 실행기는 독립 `flock`을 사용합니다.

Status Dashboard의 크론 수집기는 OpenClaw automation 목록을 조회하므로 이제 디스패처·버튼 처리·알림 작업이 모두 같은 스케줄 원장에 표시됩니다. system crontab에는 이 세 Infinity 작업을 중복 등록하지 않습니다. 역할별 백로그 watcher는 상시 운용하지 않으며, 프로젝트 작업 처리는 이 디스패처와 Genie 실행 흐름이 담당합니다.

## 격리·중복 방지

- OpenClaw 스케줄은 `sessionTarget=isolated`, 실행 에이전트는 `genie`입니다.
- 등록 payload는 모델 대화가 없는 command 실행이며, 제한 시간은 600초입니다. bootstrap, handoff, 후속 검증 실패는 nonzero exit로 전달해 OpenClaw 실행 이력에 실패로 남깁니다.
- 디스패처 실행 세션 키 기본값은 `agent:genie:infinity-dispatcher-v2`입니다.
- `flock` 잠금으로 이전 사이클이 끝나지 않은 동안 중복 사이클을 시작하지 않습니다.
- Genie 실행은 기본 480초, 전체 크론은 600초 제한입니다.
- 장기 작업은 task-plan의 의존성·ready leaf를 기준으로 한 번에 실행하며, `expansion_policy`가 있는 경우에만 제한된 batch를 추가합니다.

## 환경변수

- `INFINITY_DISPATCHER_STATE_DIR`: cycle record 저장 경로
- `INFINITY_TERMINAL_STATE_FILE`: 알림 receipt 경로
- `INFINITY_DISPATCHER_LOCK_FILE`: 단일 실행 잠금 경로
- `INFINITY_DISPATCHER_AGENT_TIMEOUT_SECONDS`: Genie 실행 제한 시간
- `INFINITY_DISPATCHER_SESSION_KEY`: Genie handoff 세션 키
- `INFINITY_DASHBOARD_ACTION_STATE_DIR`: 대시보드 크론 실행 기록 경로
- `INFINITY_DASHBOARD_ACTION_LOCK_FILE`: 대시보드 크론 잠금 경로
- `INFINITY_NOTIFICATION_STATE_DIR`: 알림 크론 실행·카드 경로
- `INFINITY_NOTIFICATION_LOCK_FILE`: 알림 크론 잠금 경로
- `INFINITY_CHANGE_NOTIFICATION_CHANNEL`: 새 Intent/상태변경 통보 채널
- `INFINITY_CHANGE_NOTIFICATION_TARGET`: 새 Intent/상태변경 통보 대상
- `INFINITY_TERMINAL_NOTIFICATION_CHANNEL`: 완료·승인·차단·실패 통보 채널 override
- `INFINITY_TERMINAL_NOTIFICATION_TARGET`: 완료·승인·차단·실패 통보 대상 override

Telegram 운영 설정에서는 두 목적지 override를 모두 `telegram`과 현재 대화 ID로 지정합니다. 모든 알림은 생성된 PNG 이미지 카드(`title`, 상태 톤, 본문, 근거, 푸터)를 media로 첨부하고, 일반 텍스트 fallback의 첫 줄에는 `상태 이모지 · 태스크 이름`을 고정해 이미지 미리보기를 열지 않아도 핵심을 읽을 수 있게 합니다. 그 다음 줄부터 상세 사유·검증 정보를 보내며, 공통 `presentation` 메타데이터도 함께 보냅니다. 승인 대기에는 inline 버튼을 추가합니다.

## 점검 명령

```bash
git fetch origin main
git rev-parse HEAD
git rev-parse origin/main
python3 scripts/prepare_dispatch_cycle.py --repo . --json
python3 scripts/check_intents_consistency.py INTENTS.yaml
python3 scripts/validate_intent_trace.py --all
```

`HEAD`와 `origin/main`이 다르거나 정합성·trace 검증이 실패하면 완료로 보고하지 않습니다.

## 프로젝트 실행자 접목

- Infinity의 실행 소유자는 `genie`입니다. `project_id`가 있는 Intent는 `project-executors.yaml`에서 프로젝트 저장소와 필수 문서를 해석해 dispatcher plan의 `project_executor`로 전달합니다.
- 등록 프로젝트의 executor는 Genie 본인입니다. Genie는 전달된 저장소·문서 목록을 직접 확인하고 프로젝트 저장소의 `TASKS.md`와 산출물을 갱신합니다. 프로젝트별 상시 에이전트 workspace나 추가 위임 홉은 만들지 않습니다.
- Genie가 프로젝트 결과와 Git 증거를 소유하며 Intent trace·상태·artifact 경로·원격 SHA를 Infinity에 기록합니다.
- `project_id`가 없거나 registry에 없는 값이면 추정 라우팅하지 않고 SAM을 통해 범위를 확인합니다.
- 새 프로젝트를 추가할 때는 `PROJECTS.md`, 프로젝트 저장소와 문서 경계를 등록하고 `data/project-executors.yaml` 및 registry 검증을 함께 갱신합니다. 프로젝트 전용 에이전트는 기본 구조에 포함하지 않습니다.
