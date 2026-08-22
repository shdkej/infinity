# research-29 bounded experiment log

- campaign_id: `research-29-archive-quality-v1`
- fixed_evaluator: `archive-quality-fixture-v1`
- fixture: Knowledge Lab `source/infinity/archive/{ops-26,research-28,marketing-128}.md` as inspected 2026-08-22
- fixed_metric_question: Archive된 결과에서 측정 가능한 완료 근거와 후속 Intent 연결, Knowledge Lab 승격 판단을 더 일관되게 판정할 수 있는가?
- dimensions: `metric_question+metric_result`, `follow_up_intent_ids` 또는 명시적 미생성 사유, `knowledge_status+decision+targets`, Red 네 문장 검증
- baseline: `1/3` complete (`ops-26`); `research-28` and `marketing-128` are partial. No historical files were rewritten.
- change_scope: one operating-rule/prompt axis per experiment; static evaluation only; no external execution.
- budget: 3 experiments maximum; 0 paid calls; 0 public actions; 0 permission/credential changes.

## Iterations

| experiment | one-axis change | result | evidence | rollback |
|---|---|---|---|---|
| E1 | 프롬프트: 완료 직전 고정 품질 블록(지표·후속 사유·지식·Red)을 강제 | **keep** | 고정 fixture에서 1/3 → 3/3 판정 가능. 기존 Archive는 보존하고 신규 산출물에만 적용 | prompt 후보 폐기; 기존 정본 프롬프트로 복귀 |
| E2 | 프롬프트: 후속 Intent를 `follow_up_intent_ids`로만 연결하고 미생성 사유를 강제 | **blocked** | 실제 신규 후속 Intent fixture·동일 evaluator 실행이 없어 연결률을 검증할 근거 부족 | prompt 후보 미채택; E1 baseline 유지 |
| E3 | 운영 규칙: Knowledge Lab 승격 후보에 재사용성 점수/등급을 추가 | **discard** | 고정 표본에는 점수 기준과 판정자가 없어 기존 3차원 충족률을 개선한다고 입증할 수 없음 | 점수 필드 추가하지 않음 |

## Decision

E1만 keep한다. 적용 대상은 다음 Archive부터이며 자동 merge/release, 공개, 권한, 자격증명, 비용 작업은 하지 않는다. E2는 실제 follow-up intent가 생긴 별도 승인 Intent에서 같은 fixture/evaluator를 확보할 때만 재시도한다. E3는 재사용성 rubric이 별도 승인되고 Red가 측정 가능성을 확인할 때까지 재시도하지 않는다.

- rollback_ref: `research-29-archive-quality-v1-baseline`
- next_action: 다음 산출물 Intent에 네 평가 차원을 적용하고, follow-up 생성/미생성 사유와 Red 네 문장을 함께 측정한다.
