# 실행 학습 계약

대형 Infinity MVP는 완료 여부만 기록하지 않는다. 실제 실행 시간이 다음 작업의 예산·마일스톤·Red 검토 강도를 바꾸도록, 아래 측정을 남긴다.

## 적용 범위와 원칙

- **적용:** 구현과 조사, 실제 렌더 검증 또는 둘 이상 저장소/배포 검증 중 둘 이상을 포함한 MVP, 또는 명시된 절대 마감이 있는 작업.
- **제외:** no-op·작은 문서 수정·순수 조사. 이들은 필요할 때만 축약 ledger를 쓴다.
- 모든 시각은 UTC `Z` 형식이다. 관측되지 않은 과거 시각은 git 시간이나 세션 도착 시각으로 추정하지 않고 `missing`과 이유를 기록한다.
- `active`, `waiting`, `rework`은 서로 중복하지 않는다. `active + waiting <= elapsed`여야 하며, `rework`은 active 안에서 별도 표기한다.
- Red의 timebox는 품질 게이트 면제가 아니다. 미해결 P0, timeout, 미응답은 pass가 아니라 정확한 blocker를 가진 Waiting이다.
- **실험 종료:** 이 계약을 적용한 대형 태스크가 절대 마감을 넘기면 Active를 유지하거나 handoff만 반복하지 않는다. 다음 dispatcher cycle에서 `deadline_missed`·마지막 실질 증거·실패 리포트·새 승인 필요 여부를 기록하고 Waiting으로 이동한다.
- **완료의 의미:** 기능이 먼저 동작해도 `quality_iteration_active`일 뿐 Archive가 아니다. deadline 도달 또는 사용자의 명시 조기 종료 전에는 디자인·실제 렌더·접근성·운영 품질을 개선한다.
- **기본 마감:** 사용자가 절대 마감을 생략하면 다음 이탈리아 현지 08:00을 기본 deadline으로 사용한다. Intent에는 `deadline_local: Europe/Rome`과 UTC 환산값을 함께 기록하며, 사용자가 별도 시간대·시각을 말하면 그 값이 우선한다.

## 실질 진전·마감·알림 게이트

### 실질 진전

- dispatcher handoff, 세션 존재, 빈 report는 진전 증거가 아니다.
- 각 stage transition은 새 artifact, test result, 실제 렌더 capture, source commit, 또는 명시적 external blocker 중 하나를 `stage_evidence_at`·경로와 함께 남겨야 한다.
- 이전 실질 증거 뒤 한 번의 dispatcher cycle 동안 새 증거가 없으면 `stale_progress`를 기록한다. 두 번 연속이면 Intent를 Waiting으로 옮기고, 같은 handoff를 다시 만들지 않는다.

### 자율 복구·Waiting 통보

- 대형 태스크의 브라우저·GPU·렌더러·빌드 도구·로컬 세션 장애는 곧바로 사용자 대기 사유가 아니다. 승인·권한·비용·외부 인간의 결정이 필요하지 않은 한, deadline 안에서 `rework`로 유지하며 원인 확인과 대체 경로를 자율적으로 조사·실행한다.
- 차단 원인은 추정하지 않는다. 예를 들어 “GPU 부족”은 WebGL capability, 프로필 lock, 브라우저 시작, token/config 존재, 네트워크 tile 요청 중 어떤 단계가 실패했는지 관측한 뒤에만 기록한다.
- 최소 복구 탐색 순서는 **현재 경로 복구 → 깨끗한 격리 프로필/소프트웨어 렌더 → 사용 가능한 다른 관리 브라우저·노드·원격 렌더 → 제품 코드의 재현 가능한 대체 검증**이다. 각 단계는 성공 증거 또는 실패 로그를 남긴다. 안전·비용·권한 경계를 넘는 대안은 사용자 승인 전에는 시도하지 않는다.
- `Waiting`은 위 경로가 안전하게 소진됐거나, 사용자·외부 승인 없이는 다음 검증을 진행할 수 없을 때만 쓴다. 자원 제약 하나만으로는 Waiting 전환 근거가 되지 않는다.
- Waiting 전환은 상태 변경과 같은 cycle에 원 요청 스레드로 반드시 통보한다. 통보에는 원인, 이미 시도한 대안, 다음 자율 시도 또는 사용자에게 필요한 단 하나의 입력, 재시도 시각을 포함하고 delivery receipt 또는 `delivery_unknown`을 Intent에 남긴다. 무통지 Waiting은 운영 실패다.
- `waiting_on: agent`이고 `retry_policy: autonomous`인 Waiting은 포기가 아니다. Intent에 `next_retry_at`을 UTC로 남기고, dispatcher는 그 시각 이후·deadline 이전에 Active로 되돌려 새 대안 조사/실행을 한다. `waiting_on: user | external`만 조건 변화 전 반복 실행에서 제외한다.

### 시각·지도 제품

- 사용자-facing 디자인은 구현 전 `BRAND.md → DESIGN.md → DESIGN_SYSTEM.md`를 읽고, Intent에 `design_context_checked`와 화면 요소별 반영 mapping을 남긴다.
- 완료 전 390px와 desktop의 실제 렌더 capture를 Red가 직접 읽는다. HTTP 200, CSS 파일 존재, 정적 이미지, style API 응답은 렌더 증거를 대체하지 않는다.
- 지도 제품은 실제 canvas에서 장소/도로 맥락, zoom·pan, 거리 또는 위치 판독, 레이어 상태 전환을 검증해야 한다. fixture는 데이터 한계를 설명할 수 있지만 지도 UX 완료 근거가 될 수 없다.

### terminal 알림

- `notification_channel`, `notification_target`, `notification_reply_to`는 Intake부터 Archive notifier 입력까지 immutable하게 보존한다. Archive 요약/코멘트만으로 대체하지 않는다.
- Archive는 remote verification뿐 아니라 원 대화 destination의 delivery receipt 또는 명시적인 `delivery_unknown` 기록이 있을 때만 terminal로 닫는다.
- 기능 완주가 deadline보다 빠르면 terminal completion 대신 quality-iteration 상태를 원 스레드에 한 번 알린다.

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
