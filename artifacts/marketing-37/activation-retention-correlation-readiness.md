# Virtue Activation-Retention Correlation Readiness

> marketing-37 Cloud Prepare 산출물 (2026-06-03T1200Z).
> 출시 후 사용 시 `virtue-rebirth-app/apps/web/docs/`에 복사 후 first_verification_gate 실행.

## §0 문서 범위 및 경계

- **범위**: Virtue prelaunch 단계에서 activation 후보(A1~A4)와 D7 retention을 사전 등록하고, 출시 후 데이터가 들어왔을 때 같은 기준으로 대조하기 위한 준비 문서
- **범위 아님**: 실제 correlation 계산, 활성화율/전환율/PMF 결론, activation 후보 변경, 신규 이벤트/속성 추가
- **source_note**: 로컬 부재 (`/home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-03-activation-retention-correlation.md`) → rationale 요지 + 기존 `activation-candidate-registry.md` §2 기반으로 작성
- **선행 문서**:
  - `activation-candidate-registry.md` (marketing-33) — A1~A4 묶음, first value 매핑, window 정의
  - `plg-foundation-exit-gate.md` (marketing-34) — Measurement Readiness 게이트
  - `retention-predictive-activation-brief.md` (marketing-22) — D7 재가치 질문 5선
  - `onboarding-metrics-reading-table.md` (marketing-23) — 운영 판독표
  - `traffic-source-reading-boundary-table.md` (marketing-25) — 트래픽 분리 선행
  - MARKETING_LEARNINGS.md — First Value Mapping, Measurement Readiness Is A Separate Gate

## §1 Activation 후보 묶음 (A1~A4 계승)

`activation-candidate-registry.md`의 A1~A4를 그대로 계승한다.

| 등록 ID | Job | First Value 이벤트 | 후보 묶음 (3~5 이벤트) | 관찰 Window |
|---------|-----|-------------------|-----------------------|-------------|
| A1 | J1 기록형 | `deed_saved`:183 | `add_flow_started`:72 + `deed_judged`:106 + `deed_saved`:183 | W-IMM (첫 세션), W-CONF (D7) |
| A2 | J2 누적형 | `deed_saved`:183 | `add_flow_started`:72 + `deed_saved`:183 + `level_up_viewed`:199 | W-IMM (첫 세션), W-CONF (D7) |
| A3 | J3 AI 호기심형 | `deed_judged`:106 | `add_flow_started`:72 + `deed_judged`:106 + `deed_rerolled`:149 | W-IMM (첫 세션), W-CONF (D7) |
| A4 | J4 회고형 | `deed_saved`:183 | `add_flow_started`:72 + `deed_judged`:106 + `deed_saved`:183 | W-IMM (첫 세션), W-CONF (D7) |

> **주의**: A3(J3)만 `deed_judged`가 first value. `deed_saved` 없이 세션 종료 = 정상 종료. judged−saved 갭은 J3에서 이탈 단정 금지.

## §2 First Value 매핑 (계승)

| Job | First Value 이벤트 | 파일 앵커 | 비고 |
|-----|-------------------|-----------|---------|
| J1 기록형 | `deed_saved` | :183 | 저장 후 홈 복귀 = 본체 |
| J2 누적형 | `deed_saved` | :183 | 저장 후 누적 payoff |
| J3 AI 호기심형 | `deed_judged` | :106 | 저장 선택, 저장 없는 종료 = 정상 |
| J4 회고형 | `deed_saved` | :183 | 저장 후 회고 payoff |

- `deed_save_capped`:167 = availability/friction (30덕 상한 early-return → `deed_saved` 미발화). First value 아님. Retention 집계 제외.
- `add_flow_abandoned`:78 = 미저장 이탈 짝. Drop-off 참고용, TTV 종료점 아님.

## §3 Retention 대조 질문 (D7 우선, D30 보류)

### D7 Retention 대조 질문 (per 등록 ID)

| 등록 ID | D7 재가치 질문 | 대조 이벤트 |
|---------|----------------|-------------|
| A1 (J1) | W-IMM first value 도달 후 D7 내 두 번째 `deed_saved` 발화했는가? | `deed_saved` (distinct-day ≥2) |
| A2 (J2) | W-IMM first value 도달 후 D7 내 `level_up_viewed` 또는 두 번째 `deed_saved` 발화했는가? | `level_up_viewed`:199, `deed_saved` |
| A3 (J3) | W-IMM first value 도달 후 D7 내 두 번째 `deed_judged` 또는 `deed_rerolled` 발화했는가? | `deed_judged`, `deed_rerolled`:149 |
| A4 (J4) | W-IMM first value 도달 후 D7 내 두 번째 `deed_saved` 발화했는가? | `deed_saved` (distinct-day ≥2) |

> **D30 보류**: prelaunch 단계 표본이 충분히 쌓이지 않아 D30 retention 대조는 후순위. D7 우선.

> **D7 재가치 ≠ Retention 합격**: D7 내 재가치가 없어도 이탈 단정 금지. 정성 질문으로 보완.

### Retention 대조를 위한 추가 질문 (정성, 손기록용)

1. First value window(W-IMM) 내 도달했는가? (D0 first value 도달 여부)
2. D7 내 복귀했는가? (return session 발화 여부)
3. D7 내 same-job 재가치가 있었는가? (위 대조 이벤트)
4. 복귀 세션에서 같은 잡으로 진입했는가? (source promise fit)
5. D7 재가치 없는 경우: 가용성/availability cap 차단이었는가, 아니면 intention 부재였는가?

> 출처: `retention-predictive-activation-brief.md` D7 재가치 질문 5선 계승.

## §4 Activation Window 정의 (계승)

| Window | 기간 | 설명 | First Value 포함 여부 |
|--------|------|------|----------------------|
| W-IMM | 첫 세션 | `add_flow_started` → first value 이벤트 | O |
| W-CONF | D7 | W-IMM first value 도달 후 7일 내 | first value는 이미 W-IMM에서 확인 |

- **W-IMM 제외 조건**: `deed_save_capped` early-return 세션, 503/지연 중 첫 세션, synthetic/mock/self-test 세션
- **W-CONF 계산 시작**: D0 = W-IMM first value 도달 날짜

## §5 제외 조건

아래 항목이 해당하는 세션/이벤트는 activation 및 retention 집계에서 제외한다.

| 분류 | 제외 조건 | 판별 방법 |
|------|-----------|----------|
| Mock/테스트 | `임시 판정` 라벨 세션, `IS_AI_MODE=false` 세션 | 런타임 환경 플래그 |
| Synthetic | 641 데모 시드 세션, localStorage 반복 세션 | userId/seed 패턴 |
| Self-test | 메이커 self-test 세션 | 사전 명시한 user_id 목록 |
| Availability cap | `deed_save_capped` early-return (저장 상한 도달) | 이벤트 발화 여부 |
| 503/지연 | AI 판정 대기 중 사용자 이탈 세션 | API status log |

> **적용 원칙**: 제외 조건 판별이 activation/retention 읽기보다 먼저다. 미분류 세션에서 지표를 읽지 않는다.
> 출처: `traffic-source-reading-boundary-table.md` (marketing-25) 계승.

## §6 Pseudo-Query Shape

실제 PostHog/Amplitude 쿼리 작성 전 논리 형태만 정의한다. 실제 쿼리 작성 및 대시보드 생성은 이 문서 범위 아님.

### Activation Cohort 정의 (pseudo)

```
cohort({등록 ID}) = users where:
  - add_flow_started in session S0
  - first_value_event(A{N}) in S0 (within W-IMM)
  - exclude: mock/synthetic/self-test/availability-cap sessions
```

### D7 Retention 대조 (pseudo)

```
retention_check({등록 ID}, D7) = activation_cohort({등록 ID}) where:
  - second_value_event in [D0+1, D0+7]
  - second_value_event matches: {대조 이벤트 per 등록 ID}
  - exclude: deed_save_capped sessions, synthetic/mock/self-test
```

### 주의

- 이 pseudo-query는 논리 형태이지 실행 코드가 아니다
- 실제 PostHog/Amplitude 쿼리는 이벤트 발화 확인 후 작성한다 (G6 도착 검증 전 쿼리 실행 금지)
- 출시 전 pseudo-query로 "측정 가능한가"를 확인한다. "측정값이 좋은가"는 출시 후 판단한다

## §7 Prelaunch 금지 해석

- activation rate / D7 retention % 산출 및 합격선 판정 금지 (prelaunch 표본 불충분)
- 외부 벤치마크 수치 (D7 N%, activation 40% 등) 복사 금지
- A1~A4 후보 묶음, window, first value 매핑 사후 변경 금지 (등록부 원칙)
- `deed_save_capped` = availability/friction, retention/upgrade 신호로 환산 금지
- J3 judged−saved 갭 = 이탈 단정 금지
- synthetic/mock/self-test를 사람 사용자 retention 신호로 혼입 금지
- D7 재가치 없음 = 제품 실패 단정 금지
- 1명 데이터로 상관관계 결론 금지
- 신규 이벤트, 속성, 코드, 대시보드, PostHog 설정, 계측, 세션 리플레이, 배포, 외부 발송, 비용, 권한, 개인정보 변경 0

## §8 출시 후 검증 게이트 (도착 확인용)

출시 후 데이터가 들어왔을 때 아래 게이트를 먼저 통과해야 A1~A4 대조를 시작한다.

1. **G-ARRIVE**: `add_flow_started`, `deed_judged`, `deed_saved` 이벤트가 PostHog에 실제로 도착했는가?
2. **G-EXCLUDE**: mock/synthetic/self-test 제외 조건이 적용됐는가?
3. **G-COUNT**: 비제외 사람 사용자가 10명 이상 또는 7일 이상 경과했는가? (최소 발동 조건)
4. **G-CAP**: `deed_save_capped` 세션이 전체 세션의 N% 이상인 경우 별도 분리했는가?
5. **G-PLATFORM**: 웹/iOS 트래픽을 구분했는가? (iOS는 일부 이벤트 부재 — marketing-15 계승)

G-ARRIVE~G-PLATFORM 모두 통과 후에야 A1~A4 × D7 대조를 시작한다.

## §9 계승 기준 / 변경 / 충돌 분리

### 계승한 기준

- First Value Mapping: J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106 (marketing-06, 33)
- A1~A4 묶음, W-IMM/W-CONF window: `activation-candidate-registry.md` (marketing-33) 그대로 계승
- `deed_save_capped`:167 = availability/friction, first value/retention 아님 (marketing-28, 34)
- D7 재가치 질문 5선: `retention-predictive-activation-brief.md` (marketing-22) 계승
- Traffic source 분리 선행: `traffic-source-reading-boundary-table.md` (marketing-25) 계승
- Measurement Readiness Is A Separate Gate: `plg-foundation-exit-gate.md` (marketing-34) 계승

### 이번에 새로 추가한 것

- D7 retention 대조 질문을 등록 ID(A1~A4)별로 명시
- Pseudo-query shape: 논리 형태로 activation cohort + D7 retention 정의
- 출시 후 검증 게이트(G-ARRIVE~G-PLATFORM) 명시
- D30 retention은 보류 (표본 충분 후 별도 의사결정)

### 변경: 없음

### 충돌: 없음

---

_이 문서는 파생 문서다. first value 매핑·A1~A4 묶음 충돌 시 `activation-candidate-registry.md`(marketing-33)와 MARKETING_LEARNINGS.md가 우선한다._
