# Virtue Launch-Ready PLG Signal Gate

- intent_id: marketing-59
- status: completed
- permission: L1 docs-only
- source_note: source/external-links/marketing/2026-06-14-plg-signal-hierarchy.md (레포에 없음 — inbox 후보 설명 + 선행 계약 기반으로 작성; 원본 자료 추가 시 검증 보완 필요)
- predecessors: marketing-55, marketing-56, marketing-57, marketing-58
- successor: marketing-60
- scope: Infinity documentation artifact only

## 목적

최신 PLG 자료(first win / activation / PQL 우선순위)를 Virtue prelaunch 신호 위계로 번역한다.
Virtue가 prelaunch(첫 10명 관찰) 단계이므로 숫자 판정은 이르지만, launch 이후 무엇을 볼지와 지금 보류할 신호를 미리 분리한다.
첫 10명 관찰에서 acquisition 문제, activation 문제, measurement-too-early 상태를 혼동하지 않게 한다.

## 선행 기준 유지

- `marketing-58` first successful output 계약 유지: J1/J2/J4 = `deed_saved`; J3 = `deed_judged`.
- `marketing-56` first reliable value 관찰 컬럼 유지.
- `marketing-57` value unit / limit trust 관찰 컬럼 유지.
- `marketing-60` outcome-readable docs audit와 충돌 없음.
- 신규 이벤트, tracking/privacy, public copy, deploy, external outreach, cost-bearing action 금지.
- PostHog는 프로젝트 id와 접근이 명시적으로 제공될 때까지 read-only 미래 체크리스트로만 둔다.

## PLG 신호 위계 3층 게이트

### 지금 볼 신호 (Now — Prelaunch / First 10)

prelaunch 단계에서 수기 관찰만으로 읽을 수 있는 신호. 계측 이벤트 없이 사람이 직접 판독한다.

| 신호 | 관찰 기준 | 기존 계약과의 연결 |
|---|---|---|
| First successful output 도달 여부 | J1/J2/J4: `deed_saved`; J3: `deed_judged` | marketing-58 |
| Outcome 품질 (good / weak / bad / unclear) | 사용자가 받은 의미 + 다음 행동 가시성 | marketing-60 |
| Accepted output | AI 결과를 사용자가 유용하다고 수용했는지 | marketing-56 |
| Next action visible | 저장 후 다음 할 일이 사용자에게 보이는지 | marketing-58, marketing-60 |
| Confusion note | 특정 순간 혼란의 언어 | marketing-58 |
| Retry or rejudge reason | 재시도했다면 그 이유 (호기심/불신/불일치) | marketing-56 |
| Job label | 관찰된 job: J1/J2/J3/J4 또는 unknown | marketing-58 |
| Value unit heard | 사용자가 무엇을 가치 단위로 인식했는지 | marketing-57 |
| Limit trust signal | 제한(cap/credit)에 대한 신뢰 또는 마찰 표현 | marketing-57 |

**읽기 규칙:** 이 9개 신호는 모두 수기 메모이며 자동 계측이 아니다. 첫 10명에서 패턴이 보일 때만 해석한다.

---

### 보류할 신호 (Hold — Too Early for Prelaunch)

데이터가 너무 적거나 계측이 없어 지금 판단하면 오해를 만드는 신호. 보류하고 launch 이후로 미룬다.

| 신호 | 보류 이유 |
|---|---|
| D1 / D7 재방문율 | n < 10이면 비율 해석 불가 |
| 세션당 deed 수 | 첫 10명의 행동 다양성이 너무 커 평균화 불가 |
| Activation rate | 분모가 없음 (acquisition 미시작) |
| 공유율 / 바이럴 계수 | 의도적 공유 기능 없음, 측정 방법 미정 |
| Task completion rate | 단일 job 이상의 흐름 미정의 |
| 시간 기반 지표 (time-to-value 등) | 타이머 이벤트 없음; 수기 관찰의 '느낌' 수준 |
| 리텐션 코호트 | launch 전 코호트 없음 |

---

### Launch 이후 볼 신호 (Post-Launch — Scale Required)

충분한 사용자와 계측이 있어야 의미 있는 신호. launch 이후 별도 계약으로 열린다.

| 신호 | 조건 |
|---|---|
| Funnel conversion (signup → first deed) | PostHog + acquisition channel 동작 이후 |
| PQL (Product Qualified Lead) scoring | 반복 사용 패턴 데이터 필요 |
| 유료 전환율 (paid conversion) | pricing 모델 확정 이후 |
| CAC / LTV | paid 채널 운영 이후 |
| NPS / CSAT | n ≥ 20 권장 |
| 채널별 acquisition 효율 | 공개 배포 + UTM / referral 추적 이후 |
| PostHog funnel report | 프로젝트 id 및 api key 명시 제공 이후 |

---

## First-10 수기 Review Gate

첫 10명 관찰 완료 후, 아래 게이트를 통과해야 다음 단계(launch-ready / 개선 / 피벗)를 판단한다.

### 필수 확인 항목

| 게이트 질문 | 판단 기준 | 통과 조건 |
|---|---|---|
| First successful output 도달 비율 | deed_saved 또는 deed_judged 수 ÷ 총 관찰 수 | ≥ 7/10 통과 권장 |
| 지배적인 Job 타입 | J1/J2/J3/J4 중 가장 많이 관찰된 job | 1개 이상 지배적 job 식별 |
| 반복 실패 패턴 | outcome_weak / outcome_bad 공통 원인 | 패턴 없거나 개선 후보 1개 이하 |
| 혼란 집중 지점 | confusion_note가 집중되는 화면/순간 | 1개 이하 집중 지점 |
| Next action 가시성 | next_action_visible 비율 | ≥ 6/10 통과 권장 |
| J3 저장 없는 종료율 | deed_judged without deed_saved | save_not_required_reason 기록 여부 확인 |

### 게이트 판정 출력

- **launch-ready signal**: first successful output ≥ 7/10, 혼란 집중 ≤ 1점, next action ≥ 6/10
- **개선 필요 signal**: 반복 failure 패턴 명확, 혼란 집중 ≥ 2점
- **데이터 부족**: 관찰 완료 < 10명이거나 do_not_count_reason 비율 높음 → 관찰 계속

### 주의 사항

- 이 게이트는 acquisition, channel, 유료 전환, PMF를 판단하지 않는다.
- 통과 여부는 숫자 계측이 아니라 수기 메모의 질 판단이다.
- J3 저장 없는 종료는 실패로 처리하지 않는다 (`save_not_required_reason` 확인 후 해석).

## 충돌 방지

- marketing-58 first successful output 계약을 바꾸지 않는다.
- marketing-60 outcome-readable docs audit를 바꾸지 않는다.
- J1/J2/J4 = `deed_saved`, J3 = `deed_judged` 매핑을 유지한다.
- 이 문서가 있다고 해서 launch 판단을 앞당기지 않는다.

## 검증

- 선행 계약(marketing-55/56/57/58)과 충돌 없음.
- marketing-60이 이 게이트를 전제로 작성됨 (충돌 없음 확인).
- 신규 이벤트, tracking/privacy, public copy, deploy, external message, pricing, cost 변경: 0.
- conflict markers: 0.
- source note 레포 미존재 → inbox candidate 설명 + 선행 계약 기반으로 작성.
