# Dispatcher 구현 참고

이 문서는 Infinity 디스패처의 코드 수준 동작을 설명합니다. 실행 순서는 [heartbeat.md](../heartbeat.md), 문서별 책임은 [README.md](../README.md)를 따릅니다.

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
- 장기 작업은 task-plan의 의존성·ready leaf를 기준으로 실행합니다. 제한 batch 자동 추가는 `expansion_policy`와 사용자가 명시한 유효한 미래 canonical Intent `deadline`이 함께 있을 때만 허용하며, deadline이 없거나 지났으면 기존 계획을 마친 뒤 terminalization으로 보냅니다.

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

## 알림 전달 계약

- 모든 새 open Intent는 접수 시 `notification_channel`, `notification_target`과 해당하는 `notification_thread` 또는 `notification_reply_to`를 기록합니다. 후속 상태·Archive에도 원점을 보존합니다. 실행 환경에 해당 알림의 채널·대상 override가 모두 설정되면 캡처된 목적지보다 override를 우선합니다. 단, 목적지 원점이 없는 과거 항목이나 명시적 `delivery_unknown`/`missing-at-intake` 표식은 자동으로 전역 대화에 보내지 않습니다. 목적지를 바꿀 때 원본의 thread/reply 메타데이터도 재사용하지 않습니다.
- notifier는 `origin/main:INTENTS.yaml`과 월별 Archive YAML을 읽습니다. Archive는 `remote_verified: pass`, Waiting은 실제 blocker 또는 승인 조건이 있을 때만 terminal 후보입니다. 원점 없는 과거 항목은 추정 발송하지 않습니다.
- `/home/ubuntu/.openclaw/state/infinity-dispatcher-runs/dispatcher-terminal-notifications.json`은 intent·terminal state·destination 키로 송신 전 durable claim을 남깁니다. `sent`, `failed_before_acceptance`, `delivery_unknown`을 구분하며 불확실 수신은 자동 재송하지 않고 실패 알림으로 드러냅니다. 최초 실행은 현재 원장을 기준선으로 저장합니다. 기존 저장소 경로는 마이그레이션 호환용이며 dispatcher의 clean-check에서만 제외됩니다.
- 승인 대기는 `waiting_on: user`, `approval`, `approval_required: true`, `permission_level: approval_required` 또는 승인 사유가 있는 `waiting_reason`으로 판단합니다. 버튼 callback은 `infinity:approve:<intent-id>` / `infinity:reject:<intent-id>`입니다.
- `resolve_waiting`은 Waiting → Active 전이, `archive_request`는 명시된 open Intent의 월별 Archive·상세 생성을 수행합니다. 버튼 처리 크론이 요청 ID·전이 기록을 push한 뒤 작업 dispatcher가 다음 cycle에서 이어갑니다. 요청 큐 소비와 실제 태스크 완료를 구분합니다.

## Hermes WSL 이관 준비(활성화 전)

`/home/sam/workspace/infinity`의 `scripts/run_hermes_infinity_cron.sh`는 새 호스트의 준비 진입점입니다. `dispatcher|consumer|notifier --check`는 로컬 확인만 하며 Git/S3/발송을 호출하지 않습니다. 실행 모드는 Ubuntu consumer 중지 확인을 별도 운영 절차로 받은 후 생성할 비공개 상태 파일(`~/.hermes/state/infinity/ubuntu-consumer-stopped.confirmed`)과 **실제 운영 영수증 원본**(`~/.hermes/state/infinity/dispatcher-terminal-notifications.json`)이 없으면 차단합니다. 최초 인계 때 원본 SHA256 `a33b0be96db917069d3b66761ab7dc8aa92aacb3a06e6e1a64d761028c724666`을 확인하고 원본의 불변 비공개 사본 `notification-ledger-intake-baseline.json`(0600) 및 `receipt-bootstrap.sha256`에 증거를 남깁니다. 이후 운영 원장은 변경되므로 매 cycle에서 초기 SHA와 비교하지 않고, 불변 사본의 SHA와 최초 56건의 `sent`/`delivery_unknown`/`superseded` 영수증 연속성을 확인해 최초 기록의 누락·초기화를 차단합니다. 단, 인계 이후 새로 추가된 영수증의 유실까지 막는 동적 고수위 검증은 아직 없습니다. 실제 notifier 전환 전에 별도 보존·복구 계약을 검증해야 합니다. 상태 파일은 중지 확인의 증거가 아니므로 단독 생성·활성화하지 않습니다. 영수증은 Git이나 Slack으로 옮기지 않고 기존 `delivery_unknown`/원점 없는 항목을 재송하지 않습니다.

Hermes 내장 cron의 세 독립 작업은 현재 `paused`, `no-agent`, `catch-up off`, UTC에서 10분 간격으로만 *준비*합니다. 스크립트는 `~/.hermes/scripts/infinity-{dispatcher,consumer,notifier}.sh`에서 이 진입점을 호출합니다. dispatcher는 기존 command registry→canonical SHA 확인→trace 선기록/push→Genie handoff→원격 재검증 흐름에 `workspace-maestro/scripts/route_hermes_task.py`를 통한 Hermes child를 연결합니다. 이 경로는 `maestro-guard-task`와 동일한 비공개 task-guard 원장/잠금을 공유하며, 별도 인스턴스를 만들지 않습니다. 공용 wrapper 파일은 이 변경에서 수정하지 않았고 실제 Infinity handoff 실행은 미검증입니다. guard ID는 dispatcher 실행 단위이므로 이전 실행의 불확실한 종료 후 같은 Intent가 다음 cycle에 재선정되는 것까지 막지 못합니다. 이런 경우 자동 재시도는 별도 reconciliation으로 차단해야 합니다. consumer는 모든 선행조건이 충족되면 기존 S3→원장 commit/push wrapper를 최대 180초로 호출합니다. 두 작업은 동일한 `canonical-git.lock`을 공유해 같은 checkout에서 동시에 쓰지 않습니다. notifier는 OpenClaw CLI 대신 `scripts/hermes_telegram_send.py`를 선택할 수 있습니다. 이 경계는 논리 target의 `telegram:`을 전송 API에서만 숫자 chat ID로 바꾸고 PNG 카드·본문·`infinity:approve/reject` inline 버튼을 단일 Telegram 사진 요청에 담도록 준비했지만, 이 호스트에는 Telegram 인증·동일 bot 신원 검증과 버튼 callback을 S3 action queue로 전달할 수신 경로가 없습니다. 그러므로 notifier 진입점은 **항상 실패 차단**되며 실제 전송 성공으로 주장하지 않습니다. 기존 Ubuntu 소비자의 중지·in-flight 종료, S3 인증, `HEAD == origin/main`, 영수증 인계, Telegram 전송/버튼 및 실패 알림 경로를 각각 검증하기 전에는 어떤 새 예약도 재개하지 않습니다. 알림의 논리 target `telegram:433493318`은 영수증 중복 제거 키이므로 원장 내부에서 숫자 ID로 바꾸지 않습니다. Hermes 전송 API의 ID 정규화가 필요하면 전송 경계에서만 적용합니다.

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
