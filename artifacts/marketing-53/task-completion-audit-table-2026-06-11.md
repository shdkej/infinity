# marketing-53: Virtue Task-Completion 감사표
# (사용자 의도 → AI 수행 → 사용자 선택 다음 행동)

> 작성: 2026-06-11 | 출처: MARKETING_LEARNINGS.md (m51, m44, m42, m06~m29)
> 권한: L1 docs-only | 공개 카피·이벤트·배포·비용 변경 0

## 검증 게이트 결과

이벤트명 6개 충돌 검사 (MARKETING_LEARNINGS.md 기준):

| 이벤트명 | 출처 문서 | 구간 | 잡별 역할 |
|---------|-----------|------|----------|
| `add_flow_started` | m35, m40 | 첫 입력 전 | 입력 흐름 시작 신호 |
| `deed_judged` | m06~m29, m44, m51 | 결과 해석 | J3: first value / J1/J2/J4: 통과점 |
| `deed_saved` | m06~m29, m51 | 저장/종료 | J1/J2/J4: first value |
| `deed_rerolled` | m24, m39, m42 | 저장/종료 | 재판정 요청 (의도 관찰 전 보류) |
| `deed_save_capped` | m21, m22, m23, m28 | 저장/종료 | 마찰/가용성 (value 아님) |
| `level_up_viewed` | m32 (First-Input Defaults) | 저장/종료 | J2 누적 payoff 확인 |

**결론: conflict marker 0건. 모든 이벤트명이 MARKETING_LEARNINGS.md와 일치.**

---

## Task-Completion 감사표: 4구간 × 잡별

### 구간 1: 첫 입력 전 (first_input)

| 항목 | J1 (일상 기록) | J2 (누적 성장) | J3 (AI 판정) | J4 (영구 주석) |
|-----|-------------|-------------|------------|---------------|
| **사용자 의도** | "오늘 한 일을 써두고 싶다" | "오늘 것도 채워넣고 싶다" | "이 행동에 AI 판정을 받고 싶다" | "이걸 영구히 기록하고 싶다" |
| **AI가 수행한 작업** | 입력 대기 | 입력 대기 | 입력 대기 | 입력 대기 |
| **사용자 선택 다음 행동** | 입력 작성 또는 이탈 | 입력 작성 또는 이탈 | 입력 작성 또는 이탈 | 입력 작성 또는 이탈 |
| **on-instrument 신호** | `add_flow_started` | `add_flow_started` | `add_flow_started` | `add_flow_started` |
| **task-complete 판정** | ❌ 아직 아님 | ❌ 아직 아님 | ❌ 아직 아님 | ❌ 아직 아님 |
| **막힘 분류** | B-LOST 가능 | B-LOST 가능 | B-LOST 가능 | B-LOST 가능 |

### 구간 2: AI 판단 대기 (ai_wait)

| 항목 | J1 | J2 | J3 | J4 |
|-----|----|----|----|----|---|
| **사용자 의도** | AI가 처리해주길 기다림 | AI 점수 나오길 기다림 | AI 판정 나오길 기다림 | AI 분류 나오길 기다림 |
| **AI가 수행한 작업** | 요약/분류 생성 | 점수 계산 | 판정 카드 생성 | 레이블 분류 |
| **사용자 선택 다음 행동** | 대기 | 대기 | 대기 | 대기 |
| **on-instrument 신호** | 없음 (서버 처리) | 없음 | 없음 | 없음 |
| **task-complete 판정** | ❌ 아직 아님 | ❌ 아직 아님 | ❌ 아직 아님 | ❌ 아직 아님 |
| **막힘 분류** | B-AVAIL(지연/503) 가능 | B-AVAIL 가능 | B-AVAIL 가능 | B-AVAIL 가능 |

### 구간 3: 결과 해석 (result_interpretation)

> **핵심**: `deed_judged`는 J3에서만 first value 도달 기준이다.

| 항목 | J1 | J2 | J3 | J4 |
|-----|----|----|----|----|---|
| **사용자 의도** | AI 요약 확인 | AI 점수 확인 | AI 판정을 읽고 판단 | AI 분류 확인 |
| **AI가 수행한 작업** | 결과 카드 표시 | 점수 카드 표시 | 판정 카드 표시 | 분류 카드 표시 |
| **사용자 선택 다음 행동** | 저장 결정 / 재판정 / 닫기 | 저장+레벨업 확인 / 닫기 | **보고 끝 (저장 선택)** | 저장 결정 / 닫기 |
| **on-instrument 신호** | `deed_judged` | `deed_judged` | `deed_judged` ← **first value** | `deed_judged` |
| **task-complete 판정** | ❌ 통과점 (저장 미완) | ❌ 통과점 (저장 미완) | ✅ **task-complete (J3 first value 도달)** | ❌ 통과점 (저장 미완) |
| **막힘 분류** | B-MISMATCH 가능 | B-MISMATCH 가능 | B-NORMAL (닫기 = 정상 종료) | B-MISMATCH 가능 |

### 구간 4: 저장/종료 (save_or_exit)

> **핵심**: J3는 저장 없이 닫기 = 정상 종료. J3에 저장 넛지 금지.

| 항목 | J1 | J2 | J3 | J4 |
|-----|----|----|----|----|---|
| **사용자 의도** | "이 기록을 남길지 결정한다" | "저장하고 성장 확인" | (선택) 저장 또는 그냥 닫기 | "이걸 영구히 저장" |
| **AI가 수행한 작업** | 저장 처리 | 저장 + 레벨업 표시 | 저장 처리 (요청 시) | 저장 처리 |
| **사용자 선택 다음 행동** | 저장 완료 / 이탈 | 저장 + 레벨업 확인 | **저장(선택) 또는 닫기(정상)** | 저장 완료 |
| **on-instrument 신호** | `deed_saved` | `deed_saved`, `level_up_viewed` | `deed_saved`(선택), 없음(정상) | `deed_saved` |
| **task-complete 판정** | ✅ **deed_saved = J1 first value** | ✅ **deed_saved = J2 first value** | ✅ **이미 구간 3에서 완료** (저장은 선택 범퍼) | ✅ **deed_saved = J4 first value** |
| **마찰 신호** | `deed_save_capped` = B-AVAIL | `deed_save_capped` = B-AVAIL | `deed_save_capped` = B-AVAIL | `deed_save_capped` = B-AVAIL |

---

## deed_judged 과대평가 보정 요약

| 판단 오류 | 올바른 읽기 |
|----------|------------|
| `deed_judged` 발화 = 모든 잡의 task-complete | J3만 deed_judged = first value |
| `deed_judged` 후 저장 없으면 이탈 | J3는 deed_judged 후 무저장 닫기 = 정상 종료 |
| judged-saved 갭 = 가치 부족/불신 | J3 judged-saved 갭 = 정상 (deed_saved는 선택 범퍼) |
| J1/J2/J4에서 deed_judged = activation | J1/J2/J4에서 deed_judged는 통과점, deed_saved가 first value |

---

## 기존 문서 충돌 확인

| 기존 기준 | 이 감사표와 충돌 여부 |
|----------|----------------------|
| First Value Mapping (m06~m29): J1/J2/J4=deed_saved, J3=deed_judged | ✅ 충돌 없음 |
| Guided First-Value Is A Four-Stage Handoff (m51) | ✅ 충돌 없음 |
| Post-Response Flow Reveals Value (m44) | ✅ 충돌 없음 |
| Nudges Are Event-Triggered (m40): J3 deed_judged 후 저장 넛지 금지 | ✅ 충돌 없음 |
| Session Value Is Read By Job (m42) | ✅ 충돌 없음 |

**conflict marker 0건.**

---

## 계승한 기준

1. **First Value Mapping** (m06~m29): J1/J2/J4=deed_saved, J3=deed_judged
2. **Guided First-Value Is A Four-Stage Handoff** (m51): first_input → ai_wait → result_interpretation → save_or_exit
3. **Nudges Are Event-Triggered, Show-Nothing Is Default** (m40): J3 정상 종료에 저장 넛지 금지

## 이번에 새로 정리한 것

- 4구간 각각에 (사용자 의도 / AI 수행 / 사용자 선택 다음 행동) 3축을 명시적으로 대응
- `deed_judged` 과대평가 오류 패턴 4가지를 한 표로 정리
- J3의 구간 3=task-complete, 구간 4=선택 범퍼를 명시 (기존 기준의 실천적 번역)

## 다음 작업에 넘길 규칙

- 이 감사표는 첫 10명 관찰 루프(m47) per-session 분류 기준으로 바로 사용 가능
- 각 구간의 막힘 분류(B-LOST/B-MISMATCH/B-AVAIL/B-NORMAL)는 m35, m31, m40 기준을 따름
- durable learning candidate: 없음 (기존 기준의 종합 번역이므로 MARKETING_LEARNINGS.md에 별도 승격 불필요)
