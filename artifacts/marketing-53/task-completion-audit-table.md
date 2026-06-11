# Virtue Task-Completion 감사표

> marketing-53 · 2026-06-11T05:00Z
> 목적: 첫 입력/결과 직후를 `사용자 의도 → AI 수행 → 다음 행동`으로 읽는 잡별 관찰 기준

## 이 문서의 위치

- 계승: marketing-47(first-user learning loop), marketing-51(guided first-value handoff), marketing-52(prompt design audit)
- 보완: `deed_judged` 단독 집계를 줄이고, 잡별 first value를 행동 증거로 보강
- 제약: 신규 계측·카피·이벤트·tracking/privacy·배포·비용 변경 0

---

## 1. 4구간 handoff 개요

모든 잡은 같은 4구간을 통과한다. 잡별로 *종료점*이 다를 뿐이다.

| 구간 | 이벤트 신호 | 설명 |
|------|------------|------|
| ① first_input | `add_flow_started` | 사용자가 /add 진입, 첫 입력 작성 |
| ② ai_wait | (내부 처리) | AI가 입력을 처리하는 대기 구간 |
| ③ result_interpretation | `deed_judged` | 결과 카드 표시, 사용자가 해석 |
| ④ save_or_exit | `deed_saved` / 무저장 종료 / `deed_rerolled` | 사용자 다음 행동 선택 |

---

## 2. 잡별 Task-Completion 감사표

### J1 — 오늘 기록 (Daily Record)

| 컬럼 | 내용 |
|------|------|
| **사용자 의도** | 오늘 있었던 일을 기록하고 AI 관점을 붙이고 싶다 |
| **첫 입력 패턴** | 오늘 일어난 사건/경험 서술 (자유형식) |
| **AI 수행** | `add_flow_started` → 내용 판정 → `deed_judged` 발화 |
| **결과 직후 기대 행동** | 카드 확인 → `deed_saved` |
| **first value 이벤트** | `deed_saved` |
| **정상 종료** | 저장 후 홈 복귀 |
| **보류/마찰 신호** | `deed_judged` 후 무저장 종료 (B-LOST 후보), `deed_save_capped` (friction) |
| **관찰 포인트** | 저장 전 망설임 여부, 저장 직후 재방문 의향 |

---

### J2 — 누적 성장 (Growth Tracking)

| 컬럼 | 내용 |
|------|------|
| **사용자 의도** | 반복 기록으로 AI가 내 패턴/성장을 추적하게 하고 싶다 |
| **첫 입력 패턴** | 오늘 활동 기록 (J1과 유사하나 누적 맥락 인식) |
| **AI 수행** | `add_flow_started` → 누적 맥락 반영 판정 → `deed_judged` 발화 |
| **결과 직후 기대 행동** | 카드 확인 → `deed_saved` → `level_up_viewed` (두 번째 저장 이후) |
| **first value 이벤트** | `deed_saved` (첫 저장) · `level_up_viewed` (누적 payoff 확인) |
| **정상 종료** | 저장 후 레벨/누적 뷰 확인 |
| **보류/마찰 신호** | `level_up_viewed` 없이 세션 종료 (첫 번째 세션에서는 정상), `deed_save_capped` |
| **관찰 포인트** | 두 번째 세션에서 level_up_viewed 발화 여부 |

---

### J3 — AI 판단 (AI Judgment)

| 컬럼 | 내용 |
|------|------|
| **사용자 의도** | AI가 내 상황/행동을 어떻게 보는지 알고 싶다 |
| **첫 입력 패턴** | 상황 설명 + AI 관점 요청 형태 |
| **AI 수행** | `add_flow_started` → 맥락 판정 → `deed_judged` 발화 |
| **결과 직후 기대 행동** | 카드 읽기 → 닫기 (저장 선택) |
| **first value 이벤트** | `deed_judged` |
| **정상 종료** | 무저장 종료 = 정상. 저장은 선택 범퍼 |
| **보류/마찰 신호** | `deed_rerolled` 반복 (기대-결과 불일치 후보), `deed_save_capped` |
| **관찰 포인트** | judged−saved 갭을 이탈로 읽지 않음. 보여주기(off-instrument) 행동 손기록 |

> **주의**: J3에서 `deed_judged` 발화 = first value 도달. 저장 유도 낚지를 붙이지 않는다.

---

### J4 — 회고/주석 (Retrospective Annotation)

| 컬럼 | 내용 |
|------|------|
| **사용자 의도** | 과거 기록에 AI 관점을 덧붙이거나 재해석하고 싶다 |
| **첫 입력 패턴** | 과거 사건 + "지금 보면 어떤가" 맥락 |
| **AI 수행** | `add_flow_started` → 맥락+시간 반영 판정 → `deed_judged` 발화 |
| **결과 직후 기대 행동** | 카드 확인 → `deed_saved` (주석으로 보존) |
| **first value 이벤트** | `deed_saved` |
| **정상 종료** | 저장 후 기록 아카이브 확인 |
| **보류/마찰 신호** | `deed_judged` 후 무저장 종료 (B-LOST 후보), 과거 맥락 부재로 `deed_rerolled` |
| **관찰 포인트** | 저장된 회고가 기존 기록과 연결되는지 체감 여부 |

---

## 3. 이벤트 매핑 요약

| 이벤트 | 발화 시점 | J1 | J2 | J3 | J4 |
|--------|----------|----|----|----|----|
| `add_flow_started` | /add 진입 | ✓ | ✓ | ✓ | ✓ |
| `deed_judged` | AI 결과 카드 표시 | 통과점 | 통과점 | **도착점** | 통과점 |
| `deed_saved` | 저장 완료 | **도착점** | **도착점** | 선택 | **도착점** |
| `deed_rerolled` | 재판정 요청 | 보류 | 보류 | 관찰 | 보류 |
| `deed_save_capped` | 저장 한도 초과 | friction | friction | friction | friction |
| `level_up_viewed` | 레벨업 화면 조회 | — | 누적 payoff | — | — |

---

## 4. 관찰 기준 (prelaunch 첫 10명)

신규 계측 없이 손기록으로 관찰할 항목:

1. **잡 분류**: 세션 시작 시 J1~J4 중 어느 의도인지 추정
2. **구간 종료점**: `deed_judged` (통과점) vs `deed_saved` (도착점) 구분
3. **guided break 위치**: ①first_input ②ai_wait ③result_interpretation ④save_or_exit 중 첫 끊김
4. **종료 성격**: 정상 종료 / B-LOST(길 잃음) / B-MISMATCH(기대 불일치) / B-AVAIL(가용성 차단)
5. **off-instrument**: 보여주기·웃음·망설임 등 손기록

---

## 5. 계승한 기준

- **First Value Mapping** (marketing-06~29): J1/J2/J4=`deed_saved`, J3=`deed_judged`
- **Guided First-Value Is A Four-Stage Handoff** (marketing-51): 4구간 handoff 기준 채택
- **Nudges Are Event-Triggered** (marketing-40): 저장 유도 낚지를 J3에 붙이지 않음
- **Prelaunch Decision Boundary** (marketing-08,22,23): 첫 10명은 정성 관찰, 비율 금지

## 6. 이번에 새로 정리한 것

- J1/J2/J3/J4 각 잡별로 `사용자 의도 → AI 수행 → 다음 행동` 3-컬럼을 처음으로 명시적 표 형태로 정리
- `deed_judged`를 통과점(J1/J2/J4) vs 도착점(J3)으로 명시적으로 구분한 감사표

## 7. 다음 Marketer에게 넘길 규칙 후보

- J3에서 `deed_judged` 발화 후 무저장 종료는 정상 종료(이탈 아님)임을 감사표에서 명시 → MARKETING_LEARNINGS.md에 이미 First Value Mapping에 포함, 추가 승격 불요
- 4구간 handoff의 "guided break" 위치 분류를 첫 10명 관찰 손기록 루틴에 포함할 것을 권장 (marketing-51 기준 보완)
