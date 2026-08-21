# research-28 — autoresearch를 Infinity에 접목하는 최소 운영 모델

## 결론

Infinity에 가져올 것은 `무제한 자율 실행`이 아니라 **고정 평가면·좁은 변경면·bounded 반복·명시적 keep/discard/crash·누적 원장**이다. 기본 사용자-facing 명칭은 `반복 개선 루프`로 두고 `autoresearch`는 내부 참고명으로만 쓴다.

## 1. 원리와 대응

| autoresearch | Infinity 대응 | 경계 |
|---|---|---|
| `program.md` | Intent의 goal/boundary/success criteria | 실험 계약을 실행 전에 고정 |
| `prepare.py`와 고정 evaluator | 버전 있는 평가 기준·입력 데이터 | 실험 중 변경 금지 |
| 단일 `train.py` 변경면 | 캠페인당 하나의 파일·프롬프트·설계 축 | 여러 시스템 동시 수정 금지 |
| 고정 5분 단위 | 실행별 시간·횟수·비용 budget | Infinity Heartbeat의 bounded 세션 |
| `results.tsv` | append-only Artifact + HTML Report | 원시 로그와 결론 분리 |
| keep/discard/crash | keep/discard/crash/timeout/blocked | keep은 다음 baseline 승격일 뿐 배포가 아님 |
| branch/parent commit | 전용 branch/worktree와 rollback_ref | main 자동 merge/push 금지 |

## 2. 최소 MVP

대상은 하나의 Intent 안에서 하나의 고정 지표와 하나의 변경 축만 반복하는 문서·프롬프트·분류·평가 기준 실험으로 제한한다.

1. Planner가 baseline, 고정 evaluator, 지표 방향, 허용 변경면, 종료 조건을 고정한다.
2. Developer가 후보 하나와 가설 하나를 준비한다.
3. Heartbeat는 lock·권한·budget을 검사하고 한 번에 한 실험만 실행한다.
4. 동일 evaluator로 측정하고 append-only 원장에 결과를 남긴다.
5. 지표 개선과 부작용 조건을 모두 통과하면 `keep`, 아니면 `discard`, 오류·시간초과는 `crash`/`timeout`으로 기록하고 baseline으로 복귀한다.
6. Red가 요청 일치성·측정 정합성·롤백 가능성을 검증한다.
7. 세션 종료 후 다음 세션은 자동 연속하지 않고 새 Intent 또는 명시된 bounded continuation으로 연결한다.

초기 권장 상한은 최대 3회 실험, 고정 wall-clock, 일일 총 시간·retry·비용 상한이다. 실제 GPU·클라우드·유료 API 실행은 별도 승인 없이는 하지 않는다.

## 3. 최소 필드

Intent `experiment`: `target`, `fixed_evaluator`, `metric`, `metric_direction`, `baseline_ref`, `time_budget`, `iteration_budget`, `change_scope`, `forbidden_scope`, `keep_rule`, `stop_conditions`.

Artifact: `campaign_id`, `experiment_id`, `hypothesis`, `candidate_change`, `baseline_ref`, `baseline_metric`, `candidate_ref`, `candidate_metric`, `resource_usage`, `status`, `decision_reason`, `run_log`, `diff_or_commit`, `rollback_ref`, `evaluator_version`, `created_at`.

Report: intent/experiment/session id, 시작·종료 시각, baseline·candidate 지표와 방향, 변경 범위, 실행·비용·자원, 상태·오류, 테스트, rollback, Artifact, next action, `red_status`, Red report 경로.

중복 방지/재진입에는 `lock_owner`, `started_at`, `parent_commit`, `budget_remaining`, `retry_count`, `next_retry_condition`, `stop_reason`을 둔다.

## 4. 성공·중단·롤백

- 성공/keep: 동일 evaluator에서 지표가 개선되고 비용·메모리·복잡도·부작용 상한을 넘지 않으며 재현된다.
- discard: 지표 미개선·동률에서 더 복잡함·부작용 초과.
- crash/timeout: 오류·OOM·지표 누락·실행 시간 초과. 로그는 보존한다.
- 즉시 중단: evaluator/데이터셋 변경, 반복 crash, budget 초과, 허용 범위 이탈, secret·외부 시스템·공개 표면 접근.
- rollback: 코드 후보는 parent commit으로 revert, 문서/전략 후보는 Artifact를 superseded/discard로 표시하고 canonical pointer를 이전 버전으로 복구. 실험 로그는 삭제하지 않는다.

## 5. 적용하지 않을 범위

여러 Intent 자동 경쟁, 공유 파일 동시 수정, 무제한 swarm, cron·권한·자격증명·배포 변경, 외부 공개·자동 merge/release, 평가 기준의 중간 변경, Red 생략, 원본 개인정보/운영 데이터 사용은 MVP에서 제외한다.

## 6. 역할 종합

- Planner: 전면 자동화가 아닌 단일 Intent·단일 지표·단일 변경 축으로 범위를 줄인다.
- Developer: `bounded experiment Intent + append-only Artifact + baseline 대비 HTML Report`가 최소 구현 단위다.
- Marketer: 사용자-facing 명칭은 `반복 개선 루프`; “자동/자율/최적화” 단독 표현은 피하고 작은 변경·같은 기준·되돌리기를 앞세운다.
- Operator: 샌드박스·전용 branch·네트워크/secret 차단·비용 상한·최대 3회·수동 배포 승인이 필수다.

합의는 고정 기준, 좁은 변경, 기록, rollback이다. 충돌은 없다. 다만 Developer의 필드 확장 제안은 즉시 스키마 변경이 아니라 후속 MVP 설계 입력으로 보류한다. 최종 순서는 `설계 검토 → 승인된 sandbox dry-run → Red → 별도 구현/운영 intent`이며, 자동 배포·cron 등록·유료 실행은 기각한다.

## 7. 1~2주 검증 실험

문서·프롬프트 평가를 대상으로 baseline 1회와 후보 최대 3회를 수행한다. evaluator와 입력 fixture를 버전 고정하고, 매 회 같은 질문 세트·같은 평가표로 품질 점수, 실행 시간, 토큰 비용, 부작용을 기록한다. 1주차는 재현성·로그·keep/discard·rollback rehearsal, 2주차는 반복 실행의 정체·비용·중단 조건을 검증한다. 기준 미달이면 자동화 확대 없이 discard하고 설계를 수정한다.

## 근거

Andrej Karpathy autoresearch 공식 [README](https://github.com/karpathy/autoresearch/blob/master/README.md)와 [program.md](https://github.com/karpathy/autoresearch/blob/master/program.md), `/home/ubuntu/workspace/knowledge-lab/infinity/INTENTS.md`, `ARTIFACT_RULES.md`, `PERMISSIONS.md`, `workflows/heartbeat.md`, `agent-wiki/README.md` 및 관련 관측·변경·운영 문서를 대조했다. Knowledge Lab에 autoresearch 전용 문서는 없어 원문과 Infinity 운영 근거를 조합했다.
