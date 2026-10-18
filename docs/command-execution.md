# AI 계획과 Infinity 명령 실행

## 목적

AI는 자연어를 해석하고 의견·대안·반대 근거를 제시합니다. 파일 이동, Intent 상태 전이, Archive, trace 기록, 4역할 병렬 계획은 결정론적 실행기가 처리합니다. 이 분리를 통해 AI의 탐색 폭은 넓히고 실행 결과는 재현 가능하게 유지합니다.

## 계획 계약

계획은 JSON 객체입니다.

- `version`: `1`
- `intent_id`: 프로젝트와 무관하게 작업을 묶는 안정적인 ID
- `judgment`: `hypotheses`, `alternatives`, `dissent`, `questions`, `evidence`, `next_decision` 등 AI 판단
- `permission`: 계획이 허용하는 최고 권한(`L0`~`L3`); 명령 레지스트리의 권한보다 낮으면 거부
- `commands`: 레지스트리에 등록된 명령 목록
- 각 명령의 `command_id`: 재시도·중복 실행을 막는 멱등성 키

판단 필드는 실행기가 해석하거나 삭제하지 않습니다. 다만 실제 변경 명령은 레지스트리의 필수 입력·권한·계획 내 중복 ID를 검증합니다. AI가 새로운 행동을 제안해도 레지스트리에 없는 명령은 자동 실행하지 않고 제안/질문으로 남깁니다.

## 실행

```bash
python3 scripts/command_runner.py plan.json
python3 scripts/command_runner.py plan.json --apply
```

첫 명령은 검증과 dry-run만 수행합니다. `--apply`는 등록된 명령만 실행하고 `data/command-runs.jsonl`에 결과를 기록합니다. 재실행 시 같은 `command_id`는 `noop/already_run`이 됩니다. Git push·공개 발송·비용·권한 변경·삭제는 이 레지스트리에 추가하기 전 별도 승인 계약을 만들어야 합니다.

## 명령 표면

- `intent.register`: 프로젝트가 있든 없든 Inbox에 Intent 등록
- `intent.move`: Inbox·Active·Waiting 사이의 명시적 상태 전이
- `intent.archive`: 열린 Intent를 월별 Archive로 이동
- `role.fanout`: Planner·Developer·Marketer·Operator 병렬 작업 계약 기록
- `trace.record`: 실행·판단·근거 이벤트 추가
- `context.pack.build`: 기존 Context Pack builder를 호출해 `zg` preflight·검색어·선택 경로를 생성하고 검증
- `trace.execution.record`: 실제 Context Pack·검색어·Wiki/운영 로그·근거 경로를 표준 execution trace에 기록
- `git.verify`: 로컬 HEAD와 `origin/main` SHA 비교

상태 원장은 계속 `INTENTS.yaml` 하나이며, 명령 실행기는 기존 dispatcher를 우회하지 않습니다. `role.fanout`은 네 역할의 공유 계약과 회수 지점을 고정하고, dispatcher/Genie가 네 역할을 실제로 병렬 인계한 뒤 synthesis·Red가 결과를 닫습니다.

10분 주기의 Infinity 크론도 `scripts/run_registered_dispatcher_cycle.sh`를 통해 `dispatcher.cycle` 등록 명령으로 진입합니다. 이 명령은 기존의 원격 동기화·계획·Genie 인계·터미널 알림 절차를 보존하면서, 크론 진입 자체를 레지스트리·권한·command_id·실행 원장 경계 안에 둡니다.
`context.pack.build`는 `zg`를 재구현하지 않고 Knowledge Lab의 정본 builder를 호출합니다. 결과에는 `query`, `result_count`, `selected_paths`가 포함되며, 후속 `trace.execution.record`는 실제 읽은 `wiki_pages`와 `evidence_paths`를 별도로 남깁니다.
