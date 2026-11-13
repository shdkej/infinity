# Infinity 실행 절차

OpenClaw dispatcher가 큐를 읽고 지니에게 작업을 넘기는 순서입니다. 저장소 간 접수·승인 기준은 [KL 운영 계약](../knowledge-lab/source/openclaw-system/docs/INFINITY_OPERATING_RULES.md), 실행기·스케줄·잠금은 [Dispatcher 구현](docs/dispatcher-implementation.md)이 소유합니다.

## 1. 최신 상태와 사용자 결정을 확인한다

1. `origin/main`을 fetch하고 현재 브랜치·변경·미푸시 커밋을 확인합니다. 안전하게 fast-forward한 뒤 `HEAD == origin/main`을 검증합니다. 다른 작업의 변경을 stash·폐기·rebase하지 않습니다. 접수 시 깨끗한 임시 worktree를 쓸 수 있고, 정기 dispatcher의 canonical checkout 요건은 구현 문서를 따릅니다.
2. `INTENTS.yaml`의 `lanes.backlog/inbox/active/waiting`과 `archive.files`의 월별 YAML을 읽습니다. 같은 목적의 열린 Intent는 재사용하고, 이미 종료된 결과는 안내합니다. 새 범위가 있을 때만 차이를 적어 후속 Intent를 만듭니다.
3. 현재 wake에 사용자 버튼 callback이 있으면 먼저 처리합니다. provider/workspace·channel·message/thread·user·value·intent/run/question ID를 outbound 기록과 대조하고 원 질문과 선택지를 복원합니다. 일치한 결정만 같은 흐름에서 이어가며, 만료·중복·불일치는 실행하지 않습니다. Active Intent가 아직 없다는 이유로 접수 전 질문의 응답을 버리지 않습니다.
4. S3 버튼 큐는 전용 `run_dashboard_actions_cron.sh`만 소비합니다. 실행 dispatcher는 다음 주기에 원격 전이 결과를 읽습니다. `resolve_waiting`은 재개 신호이고, 버튼 수신 자체는 작업 완료가 아닙니다.

## 2. Inbox를 실행 가능한 요청으로 만든다

접수 전 사용자 의도 구체화와 Context Pack은 [KL 운영 계약](../knowledge-lab/source/openclaw-system/docs/INFINITY_OPERATING_RULES.md#intake-and-evidence)을 따릅니다. SAM은 `grill-me` 방식으로 한 번에 중요한 질문 하나씩 확인합니다. 제공된 맥락을 다시 묻지 않고, 목표·결과·제외 범위·성공 증거·승인 경계를 바꾸는 불확실성만 해소합니다.

- 새 항목은 `INTENTS.yaml`의 lane 배열에 객체로 기록합니다. `id`, 동일한 한국어 `title`·`task_name`, lane에 맞는 `status`, `target_agent: genie`를 둡니다. 제목은 대상·행동·산출물을 알아볼 수 있게 쓰고 내부 ID·영어 태그를 제목으로 대신하지 않습니다.
- 사용자 의도(`user_intent`), 원하는 결과(`desired_outcome`), 제외 범위(`out_of_scope`), 성공 증거(`success_evidence`)를 분리합니다. 알림 원점 `notification_channel`·`notification_target`과 해당하는 thread/reply 메타를 보존합니다.
- Context Pack의 필수 문서와 선택된 Wiki 구간·운영 로그를 실제로 읽고 `context_documents_checked`, `context_searches`를 남깁니다. [trace 계약](docs/intent-trace-contract.md)의 writer로 intake를 기록하고 검증합니다. 검색 결과 없음과 검색 도구 실패를 구분합니다.
- 비단순 산출물 작업은 `metric_question`, `metric_signal`, `metric_decision_rule`을 기록합니다. 기존 `target_agent: marketer` 등은 `delegated_role`로 보존하고 실행은 지니가 맡습니다. source-agent 협업이면 [협업 계약](AGENT_COLLABORATION.md)도 확인합니다.
- 커밋 전 원장·trace와 `python3 scripts/prepare_dispatch_cycle.py --repo . --intents INTENTS.yaml --json`으로 로컬 카드를 검사합니다. 이 명령은 오류를 `invalid_state`에 담고도 exit 0일 수 있으므로 해당 ID의 오류가 없는지 직접 확인합니다. 요청 경로만 commit/push하고 [원격 검증기](../knowledge-lab/source/openclaw-system/scripts/verify_git_publish.sh)를 통과한 뒤, 원격 YAML의 해당 ID와 `python3 scripts/prepare_dispatch_cycle.py --repo . --json`의 판정을 다시 확인합니다. 슬롯 부족·의존성 대기는 실행 오류와 구분합니다. fetch·trace·원장·계획·push·SHA 검증 중 하나라도 실패하면 접수 완료로 보고하지 않습니다.

Backlog는 관찰 후보입니다. 사용자가 처리 범위를 선택한 뒤 Inbox로 승격하며, 후보가 있다는 이유로 자동 실행하지 않습니다. 후보 정리는 [백로그 정리 계약](docs/ROLE_WATCHER_BACKLOG_MANAGER.md)을 따릅니다.

## 3. 실행 대상을 고른다

- 실행 가능한 승인·재개 항목과 우선순위를 확인합니다. 코드의 우선순위는 `critical > high > normal > low`이며, 명시된 deadline과 의존성도 확인합니다.
- Active는 최대 3개이며 같은 프로젝트의 쓰기는 하나씩 처리합니다. 프로젝트 연결은 `data/project-executors.yaml`로 확인하고, 등록되지 않은 프로젝트나 경로를 추정해 라우팅하지 않습니다.
- `waiting_on: user|external`은 조건 변화 전 재실행하지 않습니다. `waiting_on: agent`와 `retry_policy: autonomous`는 `next_retry_at` 이후 재시도하며, 시각이 없으면 다음 cycle에서 처리합니다. 명시된 deadline이 지났으면 신규 실행 대신 종료를 판단합니다.
- Active 카드만으로 중복 실행을 막지 않습니다. 세션/프로세스, 최근 report, lock owner 또는 terminal report를 확인합니다. 살아 있는 근거 없이 중복 차단만 반복되면 guard를 해제하고 `stale_guard_released`를 기록합니다.
- 실제로 처리할 변화가 없으면 종료합니다. no-op commit/push, 생존 확인용 report, 같은 차단의 반복 알림은 만들지 않습니다.

## 4. 지니에게 실행과 검증을 넘긴다

모든 Inbox/Active Intent의 실행·보고·검증은 [GENIE_WORKFLOW.md](../../.openclaw/workspace-genie/GENIE_WORKFLOW.md)를 따릅니다. Heartbeat나 별도 로컬 실행자가 이를 우회해 완료하지 않습니다. 지니 dispatch가 불가능하면 원인과 재개 조건을 남깁니다.

인계에는 Intent ID·목표·Context Pack·기존 근거·승인 경계·검증 방법·산출물 경로를 포함합니다. 실행마다 [trace](docs/intent-trace-contract.md)에 실제 검색·읽은 문서·근거를 남깁니다. 문서·역할 결과·Red·사용자 보고는 한국어로 쓰되 코드·경로·고유명사는 원문을 유지합니다.

| 판단 | 정본과 실행 기준 |
| --- | --- |
| 권한 | [PERMISSIONS.md](PERMISSIONS.md). 허용된 범위는 실행하고 미승인 외부 행동은 [GATES.md](GATES.md)에 남김 |
| 실행 위치 | OpenClaw의 `Cloud prepares, Local executes`와 지니 workflow. 로컬 도구·세션 접근은 해당 환경의 규칙 적용 |
| 역할 협업 | Planner·Developer·Marketer·Operator 임시 세션과 교차 검토. 세션 증거·실패 시 1회 재시도·fallback 경계는 지니 workflow 및 [실행 방식 기록](ARTIFACT_RULES.md#execution-mode-기록) |
| 고객·시장·브랜드 판단 | CMO 책임. 임시 Marketer 역할이 CMO 결정권을 대신하지 않음 |
| 리서치 | 기본 `exploratory_research`; 중요한 선택·도입·구매·명시 검증은 `decision_research`. [최종본 품질 계약](ARTIFACT_RULES.md#리서치-최종본-품질-계약) 적용 |
| 큰 작업·마감 | [태스크 계획](ARTIFACT_RULES.md#대형-작업-태스크-계획)과 [실행 학습](EXECUTION_LEARNING_CONTRACT.md). leaf ≤30분, 새 계획 전 정본 양식·기존 예시 확인 |
| 시각 산출물 | [비주얼 납품 계약](VISUAL_DELIVERY_CONTRACT.md), 실제 렌더와 필요한 Red 직접 검수 |

사용자가 명시한 미래 `deadline`과 적법한 계획 정책이 있을 때만 자동 leaf 확장을 허용합니다. deadline을 추정하거나, 이미 끝난 계획을 활동량 유지 목적으로 늘리지 않습니다. stage 진전은 새 artifact/test/render/commit/blocker의 증거로 판단하며 handoff 횟수를 성과로 세지 않습니다. 대형 작업의 두 cycle 연속 무진전·복구·마감 처리는 실행 학습 계약을 따릅니다.

## 5. 대기에는 담당과 재개 조건을 남긴다

| `waiting_on` | 남길 것 | 처리 |
| --- | --- | --- |
| `user` | 필요한 결정·승인·입력, `blocker`, `next_action` | 현재 승인 범위로 해결할 수 없는 것만 요청 |
| `external` | 외부 조건과 확인 방법 | 조건이 바뀌면 재개 |
| `agent` | 실패 근거·시도한 대안·`retry_policy`·`next_retry_at` | 자율 재시도 |
| `internal` | 누락된 Report·Archive·지식 판정·원격 증거 | dispatcher가 종료 묶음을 마침 |

안전하게 가능한 복구 경로를 확인한 뒤 차단을 선언합니다. 같은 이유가 반복되면 대안·필요한 사용자 결정·프로토콜 수정 중 하나로 연결하고 같은 보고를 쌓지 않습니다. 상세 복구 순서와 역할 세션 재시도 한도는 [실행 학습 계약](EXECUTION_LEARNING_CONTRACT.md)을 따릅니다.

승인을 기다리는 초안·후보·링크는 `pending_decision`, `pending_posts`, `pending_threads`, `pending_links` 중 해당 필드에 안전한 라벨로 표시합니다. 비밀값·비공개 링크는 원장에 넣지 않습니다. 대시보드에서 요약·상세가 실제로 읽히는지 확인하고, 전용 notifier가 대기 사유·시도한 대안·필요 입력·재시도 시각과 receipt를 기록하게 합니다.

## 6. 결과와 Archive를 함께 닫는다

산출물 경로·Report 양식·Archive 객체·지식 판정은 [ARTIFACT_RULES.md](ARTIFACT_RULES.md)가 소유합니다. 아래 순서로 확인합니다.

1. **결과 확정:** 요청과 성공 증거를 대조해 `final/`과 읽을 수 있는 HTML Report를 완성합니다. 모든 리서치는 전체 Markdown 원문과 HTML을 함께 둡니다. 탐색형은 Red `not_required`, 의사결정형·그 외 산출물은 필요한 Red PASS와 증거를 확인합니다.
2. **종료 기록:** `metric_result`, `metric_next_decision`(`null`/`hold`는 이유 포함), 다음 행동, 지식 판정, 필요한 KL 검색 영수증을 남깁니다. 후속 작업은 중복 검색 후 연결하고 승인 범위 밖 실행은 하지 않습니다.
3. **상태 이동:** 열린 lane에서 제거하고 `intents/archive/YYYY-MM.yaml`에 객체를 넣으며, 상세는 `intents/archive/{id}.md`로 연결합니다. 동일 ID의 lane 중복을 만들지 않고 `completed_at`·trace·알림 원점을 보존합니다.
4. **검증·게시:** 원장·trace·지식·리서치 검증을 실행하고 요청 변경만 commit/push합니다. `python3 scripts/verify_archive_remote.py <intent-id>`로 원격 원장·상세·결과를 확인합니다. trace의 archive event는 증거를 확보한 뒤 writer로 기록하고 해당 변경도 게시합니다.
5. **화면·전달:** 실제 대시보드 카드와 결과 링크를 확인합니다. 검증 후 `remote_verified: pass`와 근거가 원격에 반영되어야 전용 notifier가 완료를 전달합니다. receipt 또는 `delivery_unknown`을 확인하고 로컬 생성·원격 반영·실제 전달을 구분해 보고합니다.

실행이 `done`인데 마감 기록만 빠진 경우 새 작업처럼 재인계하지 않고 같은 cycle에서 종료를 마칩니다. 마감 도달·사용자 종료 지시는 [KL 종료 계약](../knowledge-lab/source/openclaw-system/docs/INFINITY_OPERATING_RULES.md#lifecycle-archive-and-records)을 적용합니다. 확보한 결과와 미완료 leaf를 구분하고, 성공하지 못한 작업을 성공으로 Archive하지 않습니다. 최종 산출물을 만들 수 없거나 실제 사용자·외부 차단이 있으면 `deadline_missed`와 실패 리포트·재개 조건을 남깁니다.

## 7. 알림과 반복 개선

상태·terminal 알림은 `run_notification_cron.sh`와 `dispatch_terminal_notifications.py`가 담당합니다. 실행 에이전트가 중복 발송하지 않습니다. 알림 원점, override, durable receipt, 불확실 수신 처리, PNG·텍스트·승인 버튼은 [Dispatcher 구현](docs/dispatcher-implementation.md#알림-전달-계약)을 따릅니다. `delivery_unknown`을 임의 성공이나 자동 재송으로 바꾸지 않습니다.

일반 push 알림과 의미 없는 진행 알림은 보내지 않습니다. 리캡·예외 알림은 KL 운영 계약을 따릅니다. 반복되어 다음 행동을 바꾸는 규칙만 소유 문서에 반영하고, 사건·검토 결과는 해당 report/artifact에 둡니다. 별도 `lessons-learned.md`를 만들지 않습니다. 평가 기준은 [Evaluator](docs/infinity-evaluator.md)에 둡니다.
