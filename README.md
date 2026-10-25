# infinity

Agent-First 자율 실행 시스템. 스케줄 routine(원격 에이전트)이 실행 원장을 처리하고, 구조화된 YAML 상태와 대시보드에 의미 있는 변화를 드러낸다.

> 사용자는 **의도와 판단**만, 에이전트는 **실행과 보고**를 담당한다.

## 구조

```
INTENTS.yaml        ← 유일한 상태 원장(Backlog / Inbox / Active / Waiting)
intents/archive/*.yaml ← 월별 Archive 대시보드 원장
GATES.md            ← 승인 대기/처리 완료
PERMISSIONS.md      ← 권한 레벨(L0~L3) 정의
ARTIFACT_RULES.md   ← 산출물 경로 규칙
heartbeat.md        ← Heartbeat 동작 프로토콜 (routine이 매 실행 시 읽음)
EXECUTION_LEARNING_CONTRACT.md ← 대형 MVP 시간·병목·Red 학습 정본
VISUAL_DELIVERY_CONTRACT.md ← 참조 이미지 기반 사용자용 카드의 생성·검수·내부 fixture 차단 계약
intents/active/       ← 실행 중인 Intent 원장
                     유효 archive 원장만 Knowledge Lab의 source/infinity/archive/로 이동
artifacts/{id}/work/  ← T1·근거·초안·Red 검토 등 중간 산출물
artifacts/{id}/final/ ← 사용자 질문에 답하는 최종 재사용 산출물(리서치는 전체 Markdown 원문 필수)
reports/{id}/         ← 실행 로그와 읽을 수 있는 최종 HTML 리포트
data/knowledge-loop.json ← Infinity 대시보드의 지식 루프 운영 지표
data/promotion-index.json ← Infinity 대시보드의 Knowledge Lab 승격 상태 인덱스
data/traces/{id}.json ← Intent별 intake·execution·archive trace
scripts/dispatch_terminal_notifications.py ← 원격 `origin/main` terminal 상태를 원 대화에 1회 조정·발송
scripts/backlog_watcher.py ← PostHog·Grafana read-only 신호를 중복 제거해 Backlog 후보로 기록
scripts/run_backlog_watcher.sh ← 충돌 없는 worktree에서 와처를 실행하고 변경 시 원격 반영
docs/dispatcher-implementation.md ← 디스패처 내부 구현·환경변수·검증 명령
docs/intent-trace-contract.md ← Intent trace 입력·실행·Archive 계약
docs/infinity-evaluator.md ← Infinity 품질 평가 기준과 실행 지침
```

## 문서 지도와 정본 우선순위

Infinity 운영 문서는 여러 저장소에 걸쳐 있지만, 역할별 정본은 아래처럼 하나씩만 둔다. 같은 주제를 다른 문서에서 발견하면 이 순서로 판정하고, 보조 문서는 절차를 재정의하지 않고 링크만 제공한다.

1. **큐·상태·실행 원장:** 이 저장소의 `INTENTS.yaml` — `Backlog → Inbox → Active → Waiting → Archive` 전이와 dispatcher 계약을 구조화해 보존한다.
2. **관찰 후보 원장:** `INTENTS.yaml`의 `lanes.backlog` — 와처가 만든 후보를 사람이 확인하기 전까지 보관하며 자동 실행하지 않는다.
3. **대시보드 읽기 원장:** `INTENTS.yaml`과 `intents/archive/YYYY-MM.yaml` — 화면이 읽는 구조화된 상태·최근 완료 카드다.
3. **승인·권한:** 이 저장소의 `GATES.md`, `PERMISSIONS.md` — 승인 대기와 L0~L3 경계를 정의한다.
4. **산출물·Archive:** 이 저장소의 `ARTIFACT_RULES.md` — `artifacts/`, `reports/`, `intents/archive/`의 역할과 완료 형식을 정의한다.
5. **Heartbeat 실행:** 이 저장소의 `heartbeat.md` — dispatcher가 원장을 읽고 실행·종료하는 순서를 정의한다.
6. **Trace:** 이 저장소의 `docs/intent-trace-contract.md` — intake/execution/archive trace 구조를 정의한다.
7. **운영 상위 계약:** Knowledge Lab의 `source/openclaw-system/docs/INFINITY_OPERATING_RULES.md` — 저장소 간 경계, 원격 검증, 중복 Intent 금지, 예외를 정의한다.
8. **역할 위임:** `AGENT_COLLABORATION.md`, `/home/ubuntu/workspace-genie/GENIE_WORKFLOW.md`, Prompt Archive의 역할별 workflow — 실행 역할과 협업 형식만 정의한다.
9. **대시보드 UI·배포:** Space의 `infra-aws-static-sites/sites/infinity/README.md`와 `dist/index.html` — 표시·배포 구현만 소유하며 Intent 상태를 정의하지 않는다.
10. **디스패처 구현:** `docs/dispatcher-implementation.md` — 실행 파일·잠금·handoff·검증의 코드 수준 설명을 둔다.

### AI 계획과 결정론적 명령

Infinity는 자연어를 곧바로 파일·셸 작업으로 실행하지 않는다. AI는 `version`, `intent_id`, `judgment`, `commands`를 가진 계획 객체를 만든다. `judgment`에는 가설, 대안, 반대 의견, 미해결 질문, 근거와 사용자가 검토할 선택지를 제한 없이 담을 수 있다. 실행기는 이 내용을 보존하되 실제 변경은 `data/command-registry.yaml`에 등록된 명령만 수행한다.

검증은 기본값이 dry-run이다. 적용은 `python3 scripts/command_runner.py plan.json --apply`로 명시한다. 같은 `command_id`는 다시 실행해도 no-op이며, 한 계획 안의 중복 ID·등록되지 않은 명령·권한 초과·필수 필드 누락·4역할 계약 위반은 실행 전에 거부한다. 프로젝트가 없는 일반 작업도 `intent_id`, 성공 증거, 알림 대상 등 Intent 등록 계약을 채우면 같은 경로로 처리한다.

`role.fanout`은 Planner·Developer·Marketer·Operator를 하나의 공유 목표·성공 증거 계약 아래 병렬로 기록한다. 역할별 판단은 독립적으로 열어두되, 공유 계약과 `role-fanout.json`을 통해 synthesis가 네 결과를 모두 회수할 수 있게 한다. 실제 원격 에이전트 인계는 기존 dispatcher/Genie 경로가 담당하며, 이 명령은 그 병렬 계획을 대체하지 않는다.

10분 주기 Infinity 크론은 `scripts/run_registered_dispatcher_cycle.sh`를 호출하고, 이 진입점은 `dispatcher.cycle` 등록 명령을 `command_runner.py --apply`로 실행한다. 따라서 크론도 등록 명령·권한·멱등성·실행 원장을 거친 뒤 기존 dispatcher/Genie 절차를 수행한다.

`context.pack.build`는 Knowledge Lab의 정본 Context Pack builder를 통해 `zg` preflight를 실행하고, 명령 결과에 요청 쿼리·후보 수·선택 경로를 반환한다. `trace.execution.record`는 실제로 읽은 Context Pack·검색어·Wiki/운영 로그·근거 경로를 execution trace에 기록한다. 검색 실패나 필수 경로 누락은 명령 실패로 남기며, 검색 결과가 없는 경우에는 Context Pack의 `no-wiki-match` 기록을 보존한다.

`/home/ubuntu/workspace/prompt-archive/INFINITY.md`는 초기 설계·역사적 참고 문서다. 현재 상태값, 접수 형식, 대시보드 표시 규칙은 이 README와 위 정본 문서를 우선한다. 새 규칙은 초기 설계 문서에만 추가하지 않는다.

### 운영 품질 평가

평가는 과거 사례를 쌓기 위한 기록이 아니라 다음 실행을 바꾸기 위한 점검이다. evaluator는 아래 항목만 확인하고, 실제 운영 규칙으로 승격할 내용은 이 README 또는 해당 기능의 정본에 반영한다.

- **pickup·구조화:** Inbox가 오래 남지 않고, 목적·완료 기준·승인 경계가 실행 가능한 Intent로 정리됐는가.
- **동시성·승인:** 병렬도가 안정성과 품질을 해치지 않으며, 승인·차단 상태와 다음 재개 조건이 명확한가.
- **결과·사용자 접점:** 결과물이 정해진 경로에 있고, 사용자가 다음 판단을 할 수 있는 형태로 도달했는가. 배포는 URL 응답만으로 닫지 않고 핵심 사용자 흐름을 확인한다.
- **상태·원장 정합성:** 실행 호환 원장과 YAML 대시보드 원장이 같은 lane·ID·완료 날짜를 가리키며, Archive·후속 Intent가 중복 없이 연결됐는가.
- **반복 실패 처리:** 같은 차단·승인 문제를 새 근거 없이 반복 기록하지 않고, 반복되면 대안 경로·사용자 결정·프로토콜 수정 중 하나로 승격하는가.
- **no-op 원칙:** 의미 있는 변화가 없으면 commit·push하지 않는가.

평가 결과는 해당 실행의 report/artifact에 남긴다. 한 번의 관찰만으로 장기 규칙을 만들지 않으며, 반복되어 실제 프로토콜을 바꿀 때만 정본 문서를 수정한다.

### 반복 운영 학습

별도 누적 교훈 문서를 두지 않는다. 반복되어 다음 실행을 바꾸는 규칙만 이 README 또는 소유 정본으로 승격하고, 사건 기록·해결된 일회성 메모는 report/artifact에 남긴다.

- **차단 전 대안 확인:** 환경 제약으로 `blocked` 처리하기 전에 서로 다른 실행 경로를 최소 두 가지 확인한다. 한 도구의 실패를 전체 환경의 한계로 일반화하지 않는다.
- **반복 차단 승격:** 같은 사유의 차단 보고가 반복되면 새로 재시도하지 말고, 대안 경로 요약·사용자 결정 요청·프로토콜 수정 중 하나로 승격한다.
- **승인 전 최신 기준 확인:** 사용자가 Infinity 승인을 요청하면 `prompt-archive`의 최신 변경을 먼저 동기화한 뒤 현재 gate와 intent 상태를 기준으로 처리한다.
- **사용자 도달성 확인:** 산출물은 파일 생성이나 로컬 commit만으로 완료하지 않는다. 사용자가 결과를 보고 다음 판단을 할 수 있는 경로로 보고·연결됐는지 확인한다.

### 접수·상태 전이의 최소 불변식

- 접수 작업을 시작하기 전에 `git fetch origin main`과 `git pull --ff-only origin main`을 실행하고 `HEAD == origin/main`을 확인한다. checkout이 dirty이거나 fast-forward할 수 없으면 관련 없는 변경을 stash·폐기·rebase하지 않고, 최신 `origin/main`에서 clean temporary worktree를 만들거나 정확한 차단 사유를 보고한다. stale/diverged checkout에서 등록하지 않는다.
- 접수 전 `origin/main:INTENTS.yaml`의 세 열린 lane과 월별 Archive에서 같은 목적의 Intent를 검색한다. 기존 열린 Intent는 재사용하고, Archive에 있으면 결과를 안내한다.
- 비단순 Intent는 Context Pack을 먼저 읽고, 실제로 확인한 문서 목록(`context_documents_checked`)과 검색 범위·검색어(`context_searches`)를 남긴다. 원문 요청·정규화 쿼리·Context Pack 경로·`INTENTS.yaml` 근거·다음 결정을 포함한 Context Map trace를 `scripts/record_intent_trace.py intake`로 생성한 뒤 `scripts/validate_intent_trace.py`로 검증한다. 필수 필드가 누락되거나 trace가 invalid이면 등록을 차단한다.
- 새 Intent는 `INTENTS.yaml`의 해당 `lanes` 배열에 `id`, `title`, `task_name`, `status`를 포함한 객체 하나로 등록한다. 개별 `intents/{lane}/` 파일은 보조 기록이며 상태 원장을 대체하지 않는다.
- 원장 객체 작성 직후, 커밋 전에 `scripts/prepare_dispatch_cycle.py --json`과 `scripts/check_intents_consistency.py INTENTS.yaml`을 실행해 새 Intent가 계획과 정합성 검사에 나타나는지 확인하고, 실패하면 등록을 중단한다. Context Pack, trace, 원장 객체, 필요한 task-plan만 scoped stage하고, 관련 없는 dirty 파일은 포함하지 않는다.
- scoped diff를 확인한 뒤 Context Pack·trace·canonical 원장 블록·필요한 task-plan만 명시적으로 stage하고, Infinity 저장소(또는 clean temporary worktree)에서 scoped commit을 만든 뒤 `origin/main`으로 push한다. commit/push 실패 시 접수로 보고하지 않고 실패 경계를 기록한다.
- 등록은 커밋·push만으로 완료되지 않는다. `/home/ubuntu/workspace/knowledge-lab/source/openclaw-system/scripts/verify_git_publish.sh`를 대상 저장소·브랜치·모든 scoped 경로와 함께 실행해 원격 반영과 SHA 일치를 확인한다. 검증이 0으로 끝나기 전에는 Intent ID를 접수·Active·Waiting·dispatch ready로 보고하지 않으며, 성공한 local/remote SHA를 intake 기록에 보존한다. fetch·trace·parser·commit·push·SHA 검증 중 하나라도 실패하면 해당 실패 경계를 정확히 보고하고 등록을 중단한다.
- 한 Intent는 한 시점에 한 lane에만 존재한다. 이동은 이전 lane 블록 제거와 새 lane 블록 추가를 같은 커밋에서 처리한다.
- Archive 후 새 범위가 생길 때만 후속 Intent를 만들고, Archive 카드에 `next_action_intent` 또는 후속 ID를 연결한다. 같은 목적의 재접수로 Inbox와 Archive를 중복시키지 않는다.

## 태그 축

완료 archive에는 대시보드 필터링을 위해 세 축을 기록한다.

- `projects`: 관련 프로젝트. 1~3개, 복수 허용. 예: `virtue`, `infinity`, `agent-wiki`.
- `task_type`: 태스크 성격. 정확히 1개. 예: `research`, `strategy`, `implementation`, `maintenance`.
- `title`과 `task_name`: 제목만 읽어도 대상·행동·산출물을 알 수 있는 동일한 한국어 태스크명. Markdown `#`, `[id]`, `- key:` 메타데이터 접두사는 금지하고, ID와 영어 내부 태그는 메타데이터로 분리한다.
- `topics`: 보조 주제. 0~3개. 예: `activation`, `analytics`, `workflow`.

정식 vocabulary와 archive 코멘트 표기는 `ARTIFACT_RULES.md`를 따른다.

`T1`, 역할별 메모, Red 검토는 작업을 검증하는 **중간 산출물**이며 Archive 대표 결과가 아니다. `decision_research`와 산출물 작업의 최종 원문은 `artifacts/{id}/final/{slug}-report.md`에 보존하고 HTML Report도 요구한다. `exploratory_research`는 Markdown brief와 채널 답변으로 종료할 수 있다. Archive 카드에는 해당 유형에 실제로 요구되는 최종 산출물과 리포트만 연결한다.

## 대형 작업 안내

대형 작업은 [`EXECUTION_LEARNING_CONTRACT.md`](EXECUTION_LEARNING_CONTRACT.md)를 먼저 읽고, 역할별 시간 기록·병목 측정·Red 검증·마감 후 상태 전이 절차를 적용한다. 이 README는 운영자가 따라갈 큰 순서만 설명하고, 시간·증거·재평가의 세부 계약은 해당 문서를 정본으로 삼는다.

1. 목표·완료 기준·마감·승인 경계를 정한다.
2. 검증 가능한 leaf task와 의존성을 task-plan에 등록한다.
3. 첫 번째 실행 가능한 task만 Active로 만들고 증거를 남긴다.
4. 결과·병목·예상 대비 실제 시간을 기록하고 다음 task를 재평가한다.
5. 모든 완료 조건을 확인한 뒤 최종 산출물·Red 결과·원격 검증을 묶어 Archive한다.

## 정본과 대시보드 정합성

- 실행 전이와 대시보드의 정본은 GitHub `main`의 `INTENTS.yaml`과 `intents/archive/YYYY-MM.yaml`이다. 로컬 파일이나 별도 큐를 상태 원천으로 사용하지 않는다.
- `INTENTS.yaml`은 `Backlog/Inbox/Active/Waiting`을, 월별 Archive YAML은 완료 카드와 날짜를 구조화해 보존한다. 대시보드는 월별 YAML의 전체 Archive를 읽어 검색·월별 접기를 제공하며, 요약의 `최근 7일 완료 수`만 시간 범위를 적용한다.
- `INTENTS.yaml`의 `lanes.inbox`, `lanes.active`, `lanes.waiting`에는 각 Intent를 한 번만 둔다. Archive는 월별 YAML 파일로 분리하며 ID 중복은 검사에서 실패한다.
- **Archive manifest 형식은 엄격히 고정한다.** `INTENTS.yaml`의 `archive.files`에는 `intents/archive/YYYY-MM.yaml` 월별 원장만 등록한다. `intents/archive/{intent-id}.md` 상세 원장, `artifacts/`, `reports/` 파일을 `archive.files`에 직접 넣지 않는다. 상세 Markdown은 월별 YAML 카드가 가리키는 보조 근거로만 유지한다. 월별 YAML 카드가 없거나 manifest에 비월별 파일이 있으면 Archive·push·완료 통보를 금지하고 `scripts/check_intents_consistency.py INTENTS.yaml` 실패 상태로 남긴다.
- 열린 intent는 반드시 해당 lane 아래 `### [id] 제목` 블록으로 둔다. `status` 값과 lane이 다르면 정합성 오류로 보고 수정한다.
- 신규 Archive 블록은 요약 주석의 완료 시각과 같은 `completed_at: YYYY-MM-DDTHH:MM:SSZ`를 반드시 기록한다. 대시보드는 이 필드로 최근 완료 순서와 월 그룹을 정하므로, 주석에만 날짜를 쓰면 카드가 `날짜 미상` 접힌 그룹으로 밀린다.
- 원장 변경 후에는 `python3 scripts/check_intents_consistency.py INTENTS.yaml`를 실행하고, Infinity 원격 push 후 raw GitHub와 라이브 대시보드에서 같은 id·lane·완료 날짜가 보이는지 확인한다.
- 대시보드 배포본은 `/home/ubuntu/workspace/space/infra-aws-static-sites/sites/infinity/dist/`에 두며, 정적 파일 push와 Space 라이브 확인까지 완료해야 한다.

## 운영 원칙

- **No-op이면 커밋하지 않는다.** 변화 없는 Heartbeat는 push하지 않아 git history와 dashboard가 조용히 유지된다.
- **Backlog 검토 경계:** PostHog·Grafana 와처는 1시간마다 읽기 전용으로 후보만 만들며, PostHog 지표의 0 하락·급증·최근 관측치 장기 정체·기준 대비 저조를 감지한다. 후보는 지표·문제 유형별 고정 키로 열린 Backlog/Inbox/Active/Waiting과 중복되지 않는다. 사용자가 대시보드에서 `간단히 처리 / 중간 / 고도처리 / 장기작업` 중 하나를 고른 뒤 Inbox로 승격한다. `거절하고 삭제`는 Backlog 원장에서 해당 후보를 즉시 제거한다.
- terminal notifier는 `origin/main`의 `INTENTS.yaml`만 조정한다. **모든 새 open Intent는 intake에서 `notification_channel`, `notification_target`을 함께 기록해야 하며, `python3 scripts/check_intents_consistency.py INTENTS.yaml`가 누락을 커밋 전 오류로 막는다.** 선택적 Telegram `notification_thread` 또는 Slack `notification_reply_to`도 원 대화에 보존한다. Archive는 `remote_verified: pass` 뒤에만, Waiting은 실제 `blocker` 또는 사용자 승인 조건이 있을 때만 후보가 된다. 읽기/no-op/반복 실행은 발송하지 않는다.
- `data/dispatcher-terminal-notifications.json`의 receipt key는 intent·terminal state·destination이다. 송신 전 durable claim을 남기며 `sent`, `failed_before_acceptance`, `delivery_unknown`을 기록한다. 불확실 수신은 자동 재송하지 않고 cron 실패 알림으로 표면화한다.
- Waiting intent는 `waiting_on: user`, `approval`, `approval_required: true`, `permission_level: approval_required`, 또는 승인 사유가 있는 `waiting_reason`을 사용자 승인 대기로 인식한다. 승인 대기 알림은 Slack/지원 채널 presentation의 `infinity:approve:<intent-id>`·`infinity:reject:<intent-id>` callback 버튼을 함께 보낸다.
- 대시보드의 `resolve_waiting` 액션은 크론 처리 시 요청 큐만 소비하지 않고 해당 Intent를 `Waiting → Active`로 전환하며, `archive_request`는 명시적으로 요청된 open Intent를 월별 Archive YAML로 이동하고 archive detail을 만든다. 두 액션 모두 승인·요청 ID와 상태 전이를 `INTENTS.yaml`에 기록하고, 디스패처는 전이 직후 계획을 다시 계산해 같은 크론 주기에 후속 실행한다.
- **Dispatcher 실행 절차**: 10분 주기의 단일 디스패처가 최신 `origin/main`을 확인하고, 실행 가능한 Intent를 계획한 뒤, 필요한 작업만 Genie에 순차 인계한다. 동기화·원격 검증에 실패하면 실행하지 않으며, 대시보드 액션은 상태 전이 후 같은 주기에 계획을 다시 계산한다. 실행 결과는 Intent trace와 cycle record로 남기고, `actions=[]`는 버튼 큐가 비었다는 뜻일 뿐 작업 no-op가 아니다. 코드 수준의 실행 경로·잠금·환경변수·검증 명령은 [`docs/dispatcher-implementation.md`](docs/dispatcher-implementation.md)를 따른다.
- **50~60 leaf 장기 실행:** 대형 작업의 상세 계약은 [`EXECUTION_LEARNING_CONTRACT.md`](EXECUTION_LEARNING_CONTRACT.md)를 따른다. 일반 계획은 완료 시 terminalization한다. `task-plan.json`에 검증 가능한 `expansion_policy`가 있을 때만 ready leaf가 바닥나면 다음 batch를 전달한다. 총량은 50~60개로 고정되고, batch·범위·증거 기준은 계획에 미리 적혀 있어야 한다. 완료 leaf를 되돌리거나 무한히 증식시키지 않으며, 모든 확장은 JSON/사람용 타임라인의 append-only 계획 변경으로 남긴다.
- **Trace 계약**: 새 intent는 `scripts/record_intent_trace.py intake`로 `data/traces/{intent-id}.json`에 원문 요청·정규화 쿼리·사용자 의도·원하는 결과·제외 범위·성공 증거와 정확히 하나의 intake event를 기록한다. 이 네 의도 필드는 Red가 결과물이 사용자 의도에 맞는지 최종평가할 때 사용하는 필수 인계 계약이다. 실행마다 `execution`으로 실제 Context Pack·검색·근거 경로를 남긴다. 모든 비단순 산출물 Intent는 `metric_question`, `metric_signal`, `metric_decision_rule`을 갖고, 완료 보고에는 `metric_result`, `metric_next_decision`을 기록한다(`null`/`hold` 허용). 기본 `exploratory_research` Archive는 브리프·원격 검증과 `red_status: not_required`를, `decision_research`와 산출물 작업은 final report·Red pass·원격 검증을 기록한다. 계약은 `docs/intent-trace-contract.md`가 정본이며 `python3 scripts/validate_intent_trace.py --all`을 원장 검사와 함께 실행한다. trace가 없는 레거시 카드를 dispatcher가 인계할 때는 실행을 중단하지 않고 `backfill_source: dispatcher_missing_trace`·여섯 request field의 `missing` 사유·빈 Context Pack·`partial` 상태로 backfill한 뒤 handoff를 기록한다. 이 복구 예외는 후속 실제 execution 없이는 Archive로 끝낼 수 없다.
- **실행 학습 계약**: 대형 MVP는 [`EXECUTION_LEARNING_CONTRACT.md`](EXECUTION_LEARNING_CONTRACT.md)의 역할별 UTC timing ledger, 예상 대비 실제·병목 측정, focused Red 프로토콜을 적용한다. 시간제한은 품질 게이트를 생략하는 근거가 될 수 없다.
- **참조 기반 비주얼 납품**: 이미지 참조가 있는 사용자용 카드/캐러셀은 [`VISUAL_DELIVERY_CONTRACT.md`](VISUAL_DELIVERY_CONTRACT.md)를 따른다. 실제 참조 입력·카드별 아트디렉션·후보/참조 나란히 검수·Red 시각 충실도 PASS가 필요하며, `LAYOUT ONLY` 같은 내부 scaffold는 사용자 결과가 될 수 없다. `python3 scripts/validate_visual_delivery.py --manifest artifacts/{intent-id}/render-manifest.json --require-user-preview`로 검증한다.
- **Cloud prepares, Local executes**: 조사/계획/초안은 클라우드, 파일 수정/실행/검증은 로컬 Claude Code에 위임한다.
