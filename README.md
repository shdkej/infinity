# Infinity

사용자의 요청을 접수하고, 에이전트의 실행·대기·완료 결과를 추적하는 태스크 관리 도구입니다. 현재 상태는 GitHub `main`의 YAML 원장으로 관리하며, [대시보드](https://infinity.aws.shdkej.com/)에서 확인합니다.

## 사용 흐름

1. **요청:** 원하는 결과와 제약을 전달합니다. SAM이 이미 확인된 맥락을 활용하고, 실행 결과를 바꾸는 불확실성만 질문해 접수합니다.
2. **실행:** 지니가 작업을 진행하고 근거·결과·다음 행동을 같은 Intent에 연결합니다.
3. **판단:** Waiting 카드에서 대기 이유와 필요한 승인·입력을 확인합니다.
4. **결과:** Archive 카드에서 결과 요약, 최종 산출물, Report를 엽니다.

| 상태 | 뜻 | 다음 행동 |
| --- | --- | --- |
| Backlog | 관찰로 모은 검토 후보 | 범위를 선택해 Inbox로 보내거나 거절 |
| Inbox | 접수되어 실행을 기다리는 작업 | 목표·완료 기준·승인 경계를 확인해 착수 |
| Active | 실행 중인 작업 | 현재 증거와 다음 행동 확인 |
| Waiting | 진행 조건이 충족되지 않은 작업 | `waiting_on`과 재개 조건 확인 |
| Archive | 종료 결과와 검증 기록 | 결과 확인, 필요한 후속 작업으로 연결 |

대기 담당은 사용자(`user`), 외부(`external`), 에이전트 재시도(`agent`), 내부 마감 처리(`internal`)로 구분합니다. Active 표시는 실행 세션이 살아 있다는 증거가 아니며, 종료 기록만 남았다고 사용자에게 판단을 돌리지 않습니다.

## 어디서 무엇을 찾나

| 찾는 것 | 정본 |
| --- | --- |
| 현재 태스크·다음 행동 | [`INTENTS.yaml`](INTENTS.yaml)의 `lanes` |
| 완료 목록 | [`intents/archive/`](intents/archive/)의 월별 `YYYY-MM.yaml` |
| 완료 상세·결과 링크 | `intents/archive/{id}.md` |
| 최종 결과물 / 조사·검토 근거 | `artifacts/{id}/final/` / `artifacts/{id}/work/` |
| 실행별 요약 보고 / 인계·검증 이력 | `reports/{id}/` / `data/traces/{id}.json` |
| 승인 대기 / 권한 범위 | [`GATES.md`](GATES.md) / [`PERMISSIONS.md`](PERMISSIONS.md) |

`INTENTS.md`와 완료 주석은 과거 형식입니다. 새 상태는 YAML에 기록하며, 개별 Markdown 파일이나 리포트가 상태 원장을 대신하지 않습니다. `archive.files`에는 월별 YAML만 등록합니다. Knowledge Lab에는 선별한 지식만 보관합니다.

## 작업별 읽을 문서

이 README에서 시작하고, 아래에서 현재 작업에 해당하는 문서를 읽습니다. Context Pack이 지정한 필수 문서는 별도로 확인합니다.

| 할 일 | 읽을 문서 | 소유 범위 |
| --- | --- | --- |
| 접수·라우팅·승인 경계 판단 | [KL 운영 계약](../knowledge-lab/source/openclaw-system/docs/INFINITY_OPERATING_RULES.md) | 저장소 간 운영 기준 |
| 큐 처리·실행·대기·종료 | [heartbeat.md](heartbeat.md) | 실행 순서 |
| 산출물·task-plan·Report 작성, Archive 구성 | [ARTIFACT_RULES.md](ARTIFACT_RULES.md) | 경로·양식·완료 증거 |
| 에이전트 간 인계 | [AGENT_COLLABORATION.md](AGENT_COLLABORATION.md) | 요청·결과 연결 |
| 대형 작업의 시간·병목 관리 | [EXECUTION_LEARNING_CONTRACT.md](EXECUTION_LEARNING_CONTRACT.md) | 실행 측정·재평가 |
| 참조 이미지 기반 납품 | [VISUAL_DELIVERY_CONTRACT.md](VISUAL_DELIVERY_CONTRACT.md) | 시각 검수 |
| trace 기록 | [Intent trace 계약](docs/intent-trace-contract.md) | 요청·실행·검증 이력 |
| 명령 실행기 사용 | [명령 실행](docs/command-execution.md) | 계획 JSON·등록 명령·dry-run |
| 자동화 점검·개발 | [Dispatcher 구현](docs/dispatcher-implementation.md) | 진입점·잠금·환경변수·실행자 |
| 운영 품질 점검 | [Evaluator](docs/infinity-evaluator.md) | 평가·반복 문제 개선 |

한 규칙은 소유 문서 한 곳에서 수정하고 다른 문서는 링크로 연결합니다. 사건 기록은 해당 실행의 report/artifact에 남깁니다. 새 안내서·누적 교훈 문서·같은 결과의 요약 사본을 늘리지 않습니다. 기존 경로·앵커를 옮길 때는 참조하는 문서와 도구도 함께 확인합니다.

`prompt-archive/INFINITY.md`는 초기 설계 참고입니다. 현재 운영은 위 정본을 따릅니다. SAM은 비즈니스실의 접수·승인 경계, CMO는 고객실의 고객·시장 방향, 지니는 제품실의 실행·결과 통합을 맡습니다. 세부 역할은 [OpenClaw 공통 계약](../knowledge-lab/source/openclaw-system/docs/OPENCLAW_COMMON.md)에 둡니다.

## 실행·개발·검증

이 저장소는 원장·Python/Bash 실행기·검증 스크립트를 소유합니다. 웹 화면 소스와 배포는 [Space의 Infinity README](../space/infra-aws-static-sites/sites/infinity/README.md)가 소유합니다. 데이터·외부 의존성은 GitHub 원장, OpenClaw/Genie, Knowledge Lab 검색, S3 버튼 큐, 설정된 알림 채널입니다. 세부 설정은 Dispatcher 문서에서 확인합니다.

저장소 루트에서 상태를 바꾸지 않는 점검부터 실행합니다.

```bash
python3 scripts/check_intents_consistency.py INTENTS.yaml
python3 scripts/validate_intent_trace.py --all
python3 scripts/prepare_dispatch_cycle.py --repo . --json
```

dispatcher 점검은 exit 0만 보지 말고 JSON의 `invalid_state`를 확인합니다. 로컬 접수 전 검증과 원격 확인 순서는 [접수 절차](heartbeat.md#2-inbox를-실행-가능한-요청으로-만든다)를 따릅니다.

명령 실행은 `python3 scripts/command_runner.py plan.json`의 dry-run으로 검토합니다. 적용 명령과 실제 작업·알림 자동화는 [명령 실행](docs/command-execution.md)과 [Dispatcher 구현](docs/dispatcher-implementation.md)을 따릅니다. 코드 변경은 해당 `scripts/test_*.py`를 실행합니다.

검증한 요청 변경만 기본 브랜치에 commit/push하고 원격 SHA를 확인합니다([공통 Git 기준](../prompt-archive/LLM.md#5-운영-기록과-완료-판정)). Archive 검증은 `python3 scripts/verify_archive_remote.py <intent-id>`와 실제 카드·링크 확인까지 필요합니다. 대시보드 배포는 Space의 별도 절차와 승인 범위를 따릅니다.

## 알려진 한계

- 과거 trace에는 삭제된 `INTENTS.md` 참조와 누락 필드가 남아 있습니다. 2026-11-13 문서 정리 전 검사에서 현재 YAML 원장은 통과했지만 전체 trace 검증은 실패했습니다. 과거 증거를 추정해 채우지 않고 실제 원문을 확인할 때 보정합니다.
- 파일·원격 SHA 검증은 실제 화면 검증을 대신하지 않습니다. Report 메타의 표시 한계는 [완료 전달 체크리스트](ARTIFACT_RULES.md#완료-전달-체크리스트-intent--dashboard--skill)에서 확인합니다.
