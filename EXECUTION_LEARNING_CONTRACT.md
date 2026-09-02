# 실행 학습 계약

대형 Infinity MVP는 완료 여부만 기록하지 않는다. 실제 실행 시간이 다음 작업의 예산·마일스톤·Red 검토 강도를 바꾸도록, 아래 측정을 남긴다.

## 적용 범위와 원칙

- **적용:** 구현과 조사, 실제 렌더 검증 또는 둘 이상 저장소/배포 검증 중 둘 이상을 포함한 MVP, 또는 명시된 절대 마감이 있는 작업.
- **제외:** no-op·작은 문서 수정·순수 조사. 이들은 필요할 때만 축약 ledger를 쓴다.
- 모든 시각은 UTC `Z` 형식이다. 관측되지 않은 과거 시각은 git 시간이나 세션 도착 시각으로 추정하지 않고 `missing`과 이유를 기록한다.
- `active`, `waiting`, `rework`은 서로 중복하지 않는다. `active + waiting <= elapsed`여야 하며, `rework`은 active 안에서 별도 표기한다.
- Red의 timebox는 품질 게이트 면제가 아니다. 미해결 P0, timeout, 미응답은 pass가 아니라 정확한 blocker를 가진 Waiting이다.

## intent별 ledger

각 실행 report 또는 `artifacts/{intent-id}/execution-learning.md`에 아래를 기록한다.

```yaml
baseline:
  baseline_at: 2026-01-01T00:00:00Z
  deadline_at: 2026-01-01T08:00:00Z
  planned_critical_path_min: 370
  planned_total_active_agent_min: 460
  milestones:
    - id: M0
      planned_at: T+20m
      owner: planner
      exit_criterion: scope, approval boundary, data-provenance contract locked
stage_runs:
  - stage: planner
    started_at: 2026-01-01T00:00:00Z
    ended_at: 2026-01-01T00:45:00Z
    elapsed_min: 45
    active_min: 45
    waiting_intervals: []
    rework_intervals: []
    evidence_paths: []
    session_id: null
    exit_status: pass
actual_vs_forecast:
  actual_critical_path_min: null
  actual_total_active_agent_min: null
  variance_min: null
  variance_pct: null
  parallel_overlap_min: null
  blocked_wait_min: null
  bottlenecks: []
```

`waiting_intervals`에는 `started_at`, `ended_at`, `minutes`, `reason`, `approval_boundary`를, `rework_intervals`에는 같은 시간 필드와 `trigger`, `fix_scope`를 둔다. Planner·Developer·Operator는 필수이며 Marketer·Synthesis·Red·remote verification도 동일 구조로 남긴다. 완료 시 `actual_critical_path_min = final_end - intent_start`, `actual_total_active_agent_min = Σ active_min`, `variance_min = actual_total_active_agent_min - planned_total_active_agent_min`으로 계산한다. `bottlenecks`는 가장 큰 critical-path 구간을 stage·원인·근거·완화책과 함께 기록한다. Red는 **queue / review / remediation / recheck**을 반드시 분리한다.

## 기본 예산과 마일스톤

대형 MVP의 시작값은 **활성 작업 460분, critical path 370분**이다.

| 구간 | 예산 | exit criterion |
| --- | ---: | --- |
| Context·scope | 20분 | M0: 범위·승인·데이터 출처 경계 고정 |
| Planner | 45분 | M1: PRD와 안전/근거 계약 |
| Developer | 210분 | M2: 핵심 흐름과 local testable artifact |
| Marketer + Operator | 25분 + 40분 (Developer와 병렬) | M3: 가치/광고·운영/개인정보 경계 |
| synthesis + local verify | 45분 | M4: 390px와 desktop 실제 렌더 증거 |
| Red preflight / inspection | 15분 / 30분 | M5: focused pass 또는 material findings |
| remediation / recheck | 45분 / 20분 | P0 수정 및 targeted rerun |
| remote proof | 30분 | push와 원격 증거 |

외부 승인 대기와 외부 서비스 장애는 calendar time에는 남기되 이 활성 예산의 초과로 계산하지 않는다. 출처·안전 데이터에 의존하는 MVP는 30% contingency를 별도로 잡고, 근거가 없으면 fixture를 실제 신호로 승격하지 않고 no-data/hold로 낮춘다.

## 집중 Red 프로토콜

M4 뒤에만 시작한다. read-only 검토는 병렬로 하고 각각 20–30분을 넘기지 않는다.

1. **core flow + actual render:** 핵심 사용자 흐름, 390px 모바일과 desktop 실제 렌더를 검사한다.
2. **safety + provenance:** 데이터 출처·날짜·신뢰도, 개인정보, 과장 없는 상태를 검사한다.
3. **deployment + claims:** local-only/승인 경계, 배포·원격 증거, 광고와 의사결정 UI의 분리를 검사한다.

Red consolidator는 15분 안에 중복을 합치고 P0만 block으로 분류한다. P0가 있으면 해당 lane만 최대 45분 보완한 뒤 20분 targeted rerun과 15분 cross-check를 한다. 비P0 개선은 follow-up이다. timeout은 pass로 바꾸지 않는다.

## 학습 갱신 규칙

- **rule EL-01:** 같은 범주의 완료 intent가 3개 이상이면, waiting을 제외한 `active + rework`의 중앙값으로 다음 기본 예산을 갱신한다.
- **rule EL-02:** Red P0 escape가 0일 때만 focused protocol을 유지한다. 하나라도 escape하면 다음 유사 작업에서 provenance/privacy 또는 render 중 원인 축을 Red 필수 범위에 추가한다.
- **rule EL-03:** 안전·개인정보 주장, 공개 배포, 비용·권한 경계는 timebox 밖의 승인/증거 게이트다. 시간 압박을 이유로 축소하지 않는다.

이 규칙은 역할별 시간 누락, Red에서 뒤늦게 발견되는 P0, 그리고 승인 대기를 구현 지연으로 오인하는 문제를 다음 예산·검토 순서에 반영하기 위한 것이다.
