# infinity

Agent-First 자율 실행 시스템. 스케줄 routine(원격 에이전트)이 깨어나 `INTENTS.md`의 의도를 자율 처리하고, 의미 있는 변화는 원장과 대시보드에 드러낸다.

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
VISUAL_DELIVERY_CONTRACT.md ← 참조 이미지 기반 사용자용 카드의 생성·검수·내부 fixture 차단 계약
intents/active/       ← 실행 중인 Intent 원장
                     유효 archive 원장만 Knowledge Lab의 source/infinity/archive/로 이동
artifacts/{id}/work/  ← T1·근거·초안·Red 검토 등 중간 산출물
artifacts/{id}/final/ ← 사용자 질문에 답하는 최종 재사용 산출물(리서치는 전체 Markdown 원문 필수)
reports/{id}/         ← 실행 로그와 읽을 수 있는 최종 HTML 리포트
data/knowledge-loop.json ← Infinity 대시보드의 지식 루프 운영 지표
data/promotion-index.json ← Infinity 대시보드의 Knowledge Lab 승격 상태 인덱스
scripts/dispatch_terminal_notifications.py ← 원격 `origin/main` terminal 상태를 원 대화에 1회 조정·발송
docs/dispatcher-implementation.md ← 디스패처 내부 구현·환경변수·검증 명령
```

## 문서 지도와 정본 우선순위

Infinity 운영 문서는 여러 저장소에 걸쳐 있지만, 역할별 정본은 아래처럼 하나씩만 둔다. 같은 주제를 다른 문서에서 발견하면 이 순서로 판정하고, 보조 문서는 절차를 재정의하지 않고 링크만 제공한다.

1. **큐·상태·대시보드 카드:** 이 저장소의 `INTENTS.md` — `Inbox → Active → Waiting → Archive`를 유일한 상태 원장으로 사용한다.
2. **승인·권한:** 이 저장소의 `GATES.md`, `PERMISSIONS.md` — 승인 대기와 L0~L3 경계를 정의한다.
3. **산출물·Archive:** 이 저장소의 `ARTIFACT_RULES.md` — `artifacts/`, `reports/`, `intents/archive/`의 역할과 완료 형식을 정의한다.
4. **Heartbeat 실행:** 이 저장소의 `workflows/heartbeat.md` — dispatcher가 원장을 읽고 실행·종료하는 순서를 정의한다.
5. **Trace:** 이 저장소의 `schema/intent-trace-contract.md` — intake/execution/archive trace 구조를 정의한다.
6. **운영 상위 계약:** Knowledge Lab의 `source/openclaw-system/docs/INFINITY_OPERATING_RULES.md` — 저장소 간 경계, 원격 검증, 중복 Intent 금지, 예외를 정의한다.
7. **역할 위임:** `AGENT_COLLABORATION.md`, `/home/ubuntu/workspace-genie/GENIE_WORKFLOW.md`, Prompt Archive의 역할별 workflow — 실행 역할과 협업 형식만 정의한다.
8. **대시보드 UI·배포:** Space의 `infra-aws-static-sites/sites/infinity/README.md`와 `dist/index.html` — 표시·배포 구현만 소유하며 Intent 상태를 정의하지 않는다.
9. **디스패처 구현:** `docs/dispatcher-implementation.md` — 실행 파일·잠금·handoff·검증의 코드 수준 설명을 둔다.

`/home/ubuntu/workspace/prompt-archive/INFINITY.md`는 초기 설계·역사적 참고 문서다. 현재 상태값, 접수 형식, 대시보드 표시 규칙은 이 README와 위 정본 문서를 우선한다. 새 규칙은 초기 설계 문서에만 추가하지 않는다.

### 접수·상태 전이의 최소 불변식

- 접수 작업을 시작하기 전에 `git fetch origin main`과 `git pull --ff-only origin main`을 실행하고 `HEAD == origin/main`을 확인한다. checkout이 dirty이거나 fast-forward할 수 없으면 관련 없는 변경을 stash·폐기·rebase하지 않고, 깨끗한 `origin/main` worktree를 사용하거나 정확한 차단 사유를 보고한다.
- 접수 전 `origin/main:INTENTS.md`의 네 lane에서 같은 목적의 Intent를 검색한다. 기존 열린 Intent는 재사용하고, Archive에 있으면 결과를 안내한다.
- 비단순 Intent는 Context Pack을 만들고, `scripts/record_intent_trace.py intake`와 `scripts/validate_intent_trace.py`로 Context Map trace를 생성·검증한 뒤 등록한다. 등록 후에는 `scripts/prepare_dispatch_cycle.py --json`에서 새 Intent가 파싱되고 실행 후보로 잡히는지 확인한다.
- 새 Intent는 `INTENTS.md`의 해당 lane 바로 아래 `### [intent-id] 제목` 블록 하나로 등록한다. 개별 `intents/{lane}/` 파일은 보조 기록이며 상태 원장을 대체하지 않는다.
- 등록 전에는 intent ID가 canonical `INTENTS.md`의 열린 lane에 정확히 한 번만 존재하는지와 parser/정합성 검사를 확인한다. Context Pack, trace, 원장 블록, 필요한 task-plan만 scoped stage하고, 관련 없는 dirty 파일은 포함하지 않는다.
- 등록은 커밋·push만으로 완료되지 않는다. `/home/ubuntu/workspace/knowledge-lab/source/openclaw-system/scripts/verify_git_publish.sh`를 대상 저장소·브랜치·모든 scoped 경로와 함께 실행해 원격 반영과 SHA 일치를 확인한다. 검증이 0으로 끝나기 전에는 Intent ID를 접수·Active·Waiting·dispatch ready로 보고하지 않으며, 성공한 local/remote SHA를 intake 기록에 보존한다.
- 한 Intent는 한 시점에 한 lane에만 존재한다. 이동은 이전 lane 블록 제거와 새 lane 블록 추가를 같은 커밋에서 처리한다.
- Archive 후 새 범위가 생길 때만 후속 Intent를 만들고, Archive 카드에 `next_action_intent` 또는 후속 ID를 연결한다. 같은 목적의 재접수로 Inbox와 Archive를 중복시키지 않는다.

## 태그 축

완료 archive에는 대시보드 필터링을 위해 세 축을 기록한다.

- `projects`: 관련 프로젝트. 1~3개, 복수 허용. 예: `virtue`, `infinity`, `agent-wiki`.
- `task_type`: 태스크 성격. 정확히 1개. 예: `research`, `strategy`, `implementation`, `maintenance`.
- `title`: 제목만 읽어도 대상·행동·산출물을 알 수 있는 한국어 태스크명. ID와 영어 내부 태그는 제목에 쓰지 않고 메타데이터로 분리한다.
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

- `INTENTS.md`가 큐 상태의 단일 정본이다. 대시보드는 GitHub `main`의 raw `INTENTS.md`를 읽고, 로컬 파일이나 별도 큐를 상태 원천으로 사용하지 않는다.
- `INTENTS.md`에는 `## Inbox`, `## Active`, `## Waiting`, `## Archive`를 각각 정확히 한 번만 둔다. 중복 섹션은 검사에서 실패하며 대시보드에 숨겨진 항목을 만들 수 있다.
- 열린 intent는 반드시 해당 lane 아래 `### [id] 제목` 블록으로 둔다. `status` 값과 lane이 다르면 정합성 오류로 보고 수정한다.
- 신규 Archive 블록은 요약 주석의 완료 시각과 같은 `completed_at: YYYY-MM-DDTHH:MM:SSZ`를 반드시 기록한다. 대시보드는 이 필드로 최근 완료 순서와 월 그룹을 정하므로, 주석에만 날짜를 쓰면 카드가 `날짜 미상` 접힌 그룹으로 밀린다.
- 원장 변경 후에는 `python3 scripts/check_intents_consistency.py INTENTS.md`를 실행하고, Infinity 원격 push 후 raw GitHub와 라이브 대시보드에서 같은 id·lane·완료 날짜가 보이는지 확인한다.
- 대시보드 배포본은 `/home/ubuntu/workspace/space/infra-aws-static-sites/sites/infinity/dist/`에 두며, 정적 파일 push와 Space 라이브 확인까지 완료해야 한다.

## 운영 원칙

- **No-op이면 커밋하지 않는다.** 변화 없는 Heartbeat는 push하지 않아 git history와 dashboard가 조용히 유지된다.
- terminal notifier는 `origin/main`의 `INTENTS.md`만 조정한다. **모든 새 open Intent는 intake에서 `notification_channel`, `notification_target`을 함께 기록해야 하며, `python3 scripts/check_intents_consistency.py INTENTS.md`가 누락을 커밋 전 오류로 막는다.** 선택적 Telegram `notification_thread` 또는 Slack `notification_reply_to`도 원 대화에 보존한다. Archive는 `remote_verified: pass` 뒤에만, Waiting은 실제 `blocker` 또는 사용자 승인 조건이 있을 때만 후보가 된다. 읽기/no-op/반복 실행은 발송하지 않는다.
- `data/dispatcher-terminal-notifications.json`의 receipt key는 intent·terminal state·destination이다. 송신 전 durable claim을 남기며 `sent`, `failed_before_acceptance`, `delivery_unknown`을 기록한다. 불확실 수신은 자동 재송하지 않고 cron 실패 알림으로 표면화한다.
- Waiting intent는 `waiting_on: user`, `approval`, `approval_required: true`, `permission_level: approval_required`, 또는 승인 사유가 있는 `waiting_reason`을 사용자 승인 대기로 인식한다. 승인 대기 알림은 Slack/지원 채널 presentation의 `infinity:approve:<intent-id>`·`infinity:reject:<intent-id>` callback 버튼을 함께 보낸다.
- 대시보드의 `resolve_waiting` 액션은 크론 처리 시 요청 큐만 소비하지 않고 해당 Intent를 `Waiting → Active`로 전환하며, `archive_request`는 명시적으로 요청된 open Intent를 `Archive`로 이동하고 archive detail을 만든다. 두 액션 모두 승인·요청 ID와 상태 전이를 `INTENTS.md`에 기록하고, 디스패처는 전이 직후 계획을 다시 계산해 같은 크론 주기에 후속 실행한다.
- **Dispatcher 실행 절차**: 10분 주기의 단일 디스패처가 최신 `origin/main`을 확인하고, 실행 가능한 Intent를 계획한 뒤, 필요한 작업만 Genie에 순차 인계한다. 동기화·원격 검증에 실패하면 실행하지 않으며, 대시보드 액션은 상태 전이 후 같은 주기에 계획을 다시 계산한다. 실행 결과는 Intent trace와 cycle record로 남기고, `actions=[]`는 버튼 큐가 비었다는 뜻일 뿐 작업 no-op가 아니다. 코드 수준의 실행 경로·잠금·환경변수·검증 명령은 [`docs/dispatcher-implementation.md`](docs/dispatcher-implementation.md)를 따른다.
- **50~60 leaf 장기 실행:** 대형 작업의 상세 계약은 [`EXECUTION_LEARNING_CONTRACT.md`](EXECUTION_LEARNING_CONTRACT.md)를 따른다. 일반 계획은 완료 시 terminalization한다. `task-plan.json`에 검증 가능한 `expansion_policy`가 있을 때만 ready leaf가 바닥나면 다음 batch를 전달한다. 총량은 50~60개로 고정되고, batch·범위·증거 기준은 계획에 미리 적혀 있어야 한다. 완료 leaf를 되돌리거나 무한히 증식시키지 않으며, 모든 확장은 JSON/사람용 타임라인의 append-only 계획 변경으로 남긴다.
- **Trace 계약**: 새 intent는 `scripts/record_intent_trace.py intake`로 `traces/{intent-id}.json`에 원문 요청·정규화 쿼리와 정확히 하나의 intake event를 기록한다. 실행마다 `execution`으로 실제 Context Pack·검색·근거 경로를 남긴다. 기본 `exploratory_research` Archive는 브리프·원격 검증과 `red_status: not_required`를, `decision_research`와 산출물 작업은 final report·Red pass·원격 검증을 기록한다. 계약은 `schema/intent-trace-contract.md`가 정본이며 `python3 scripts/validate_intent_trace.py --all`을 원장 검사와 함께 실행한다. trace가 없는 레거시 카드를 dispatcher가 인계할 때는 실행을 중단하지 않고 `backfill_source: dispatcher_missing_trace`·두 request field의 `missing` 사유·빈 Context Pack·`partial` 상태로 backfill한 뒤 handoff를 기록한다. 이 복구 예외는 후속 실제 execution 없이는 Archive로 끝낼 수 없다.
- **실행 학습 계약**: 대형 MVP는 [`EXECUTION_LEARNING_CONTRACT.md`](EXECUTION_LEARNING_CONTRACT.md)의 역할별 UTC timing ledger, 예상 대비 실제·병목 측정, focused Red 프로토콜을 적용한다. 시간제한은 품질 게이트를 생략하는 근거가 될 수 없다.
- **참조 기반 비주얼 납품**: 이미지 참조가 있는 사용자용 카드/캐러셀은 [`VISUAL_DELIVERY_CONTRACT.md`](VISUAL_DELIVERY_CONTRACT.md)를 따른다. 실제 참조 입력·카드별 아트디렉션·후보/참조 나란히 검수·Red 시각 충실도 PASS가 필요하며, `LAYOUT ONLY` 같은 내부 scaffold는 사용자 결과가 될 수 없다. `python3 scripts/validate_visual_delivery.py --manifest artifacts/{intent-id}/render-manifest.json --require-user-preview`로 검증한다.
- **Cloud prepares, Local executes**: 조사/계획/초안은 클라우드, 파일 수정/실행/검증은 로컬 Claude Code에 위임한다.
