# marketing-53: Virtue AI 온보딩 Task-Completion 감사표

- id: marketing-53
- status: completed
- completed_at: 2026-06-11T10:00Z
- permission: L1 docs-only
- projects: [virtue]
- topics: [ai-onboarding, activation, prelaunch]
- source: MARKETING_LEARNINGS.md (First Value Mapping, Guided First-Value Is A Four-Stage Handoff, Post-Response Flow Reveals Value)

## 목적

Virtue 첫 입력/결과 직후를 `사용자 의도 → AI가 수행한 작업 → 사용자가 선택한 다음 행동`으로 읽는 task-completion 감사표.

prelaunch 첫 10명 관찰 시, `deed_judged` 이후 행동을 잡별로 분류하여 `deed_judged` 과대평가를 방지하고 first value 해석을 잡별 행동 증거로 보강한다.

---

## Verification Gate 결과

### 출처 노트 확인
- 경로: `source/external-links/marketing/2026-06-11-ai-onboarding-intent-to-task.md`
- 결과: 파일 없음 → skip (inbox에서 직접 설명 충분)

### 6개 이벤트명 확인
MARKETING_LEARNINGS.md 전반에서 일관되게 사용:

| # | 이벤트명 | 출처 |
|---|---------|------|
| 1 | `add_flow_started` | marketing-40 (Nudges) |
| 2 | `deed_judged` | marketing-06+ (First Value) |
| 3 | `deed_saved` | marketing-06+ (First Value) |
| 4 | `deed_rerolled` | marketing-24 (AI Outcome Proxy) |
| 5 | `deed_save_capped` | marketing-21 (Availability) |
| 6 | `level_up_viewed` | marketing-32 (First-Input Defaults, J2 two action) |

### Conflict marker: **0건**
기존 문서(First Value Mapping, Guided First-Value, Product Body vs Bumper) 계승. 새 이벤트/속성/카피/계측 변경 없음.

---

## 4구간 Handoff 프레임워크

```
[구간 1]            [구간 2]          [구간 3]                 [구간 4]
first_input    →   ai_wait      →   result_interpretation  →  save_or_exit
      ↓                ↓                   ↓                       ↓
사용자 행동 입력   add_flow_started    deed_judged 발화         deed_saved / 종료
                                   ← J3 first value 여기서 종결 →
                                             J1/J2/J4: deed_saved까지 계속
```

**핵심 규칙:**
- J3에서 `deed_judged` = 도착점 (저장 없어도 성공)
- J1/J2/J4에서 `deed_judged` = 통과점 (저장이 first value)

---

## 잡별 Task-Completion 감사표

| 잡 | 사용자 의도 | AI 수행 작업 | First Value 이벤트 | 정상 종료 조건 | deed_judged 해석 | 저장 없는 종료 분류 |
|---|---|---|---|---|---|---|
| **J1** 행동 기록 누적 | 오늘 한 일을 AI 점수와 함께 저장하고 싶다 | `add_flow_started` → AI 판정 → `deed_judged` 결과 카드 표시 | **deed_saved** | deed_saved 발화 | 통과점: 저장 전 단계 | 보류 (B-LOST or B-MISMATCH 확인) |
| **J2** 성장 누적 확인 | 반복 기록으로 수준이 올라가는 걸 확인하고 싶다 | `add_flow_started` → `deed_judged` → `level_up_viewed` 여부 | **deed_saved** (두 번째 이상) | deed_saved 후 레벨업 확인 | 통과점: 저장이 누적 보상의 시작 | 보류 (두 번째 저장 없음) |
| **J3** AI 관점 조회 | AI가 내 행동을 어떻게 읽는지 보고 싶다 | `add_flow_started` → AI 판정 → **`deed_judged`** 결과 카드 = 목적 완료 | **deed_judged** | deed_judged 후 카드 읽기 종료 | **도착점: J3 first value** | **정상 종료 (B-NORMAL)** |
| **J4** 영구 기록 | 중요한 경험을 기록해두고 싶다 | `add_flow_started` → `deed_judged` → 저장 확인 | **deed_saved** | deed_saved (보존 의향 확인) | 통과점: 저장이 보존의 증거 | 보류 (B-LOST or B-MISMATCH 확인) |

---

## 직후 행동 선택지 (deed_judged 이후)

```
deed_judged 발화
    │
    ├── deed_saved          → J1/J2/J4: first value 도달 ✓
    │                          J3: 부가적 (정상 종료 후 선택)
    │
    ├── deed_rerolled       → 재판정 의도 (관찰 후 보류)
    │                          J3에선 탐색 신호, J1/J2/J4에선 불만족 후보
    │
    ├── 저장 없이 종료       → J3: B-NORMAL (성공) ✓
    │                          J1/J2/J4: B-LOST / B-MISMATCH / B-AVAIL 구분 필요
    │
    └── deed_save_capped    → B-AVAIL (가용성/마찰, value가 아님)
```

---

## 막힘 4분류 (B-classification)

| 분류 | 설명 | 해당 잡 | 도움 방향 |
|---|---|---|---|
| **B-LOST** | 길을 잃음, 입력 방법 모름 | J1/J2/J4 (first_input 단계) | 입력 보조 후보 (nudge) |
| **B-MISMATCH** | 결과 기대 불일치 | 전체 (result_interpretation 단계) | 제품 약속/결과 문제 (카피 아님) |
| **B-AVAIL** | 가용성 차단 (deed_save_capped, 503, 지연) | 전체 | availability/friction으로 분리 |
| **B-NORMAL** | 정상 종료 | J3 (deed_judged 후 저장 없이 종료) | 개입 불필요 |

---

## Prelaunch 관찰 사용 방법

1. 각 세션에서 어떤 잡(J1~J4)으로 첫 입력이 들어왔는지 손기록
2. `deed_judged` 발화 후 30초 이내 사용자 행동을 아래 항목으로 체크:
   - [ ] `deed_saved` 발화?
   - [ ] `deed_rerolled` 발화?
   - [ ] `deed_save_capped` 발화?
   - [ ] 저장 없이 종료?
   - [ ] `level_up_viewed` 발화? (J2 확인)
3. 잡별 기준으로 성공/보류/마찰 분류
4. J3 저장 없는 종료는 **B-NORMAL** 기록 (이탈 아님)
5. 결과를 비율·임계값·activation rate로 환산하지 않음

---

## 계승한 기준

- **First Value Mapping** (m06~m29): J1/J2/J4=deed_saved, J3=deed_judged
- **Guided First-Value Is A Four-Stage Handoff** (m51): 4구간 handoff 구조
- **Post-Response Flow Reveals Value** (m44): deed_judged 직후 행동 관찰 프레임
- **Product Body vs Bumper By Job** (m31): J3 저장 안내는 선택 범퍼

## 이번에 새로 정리한 것

- 잡별 task-completion 감사표 형식 (행동 증거 매핑)
- deed_judged 직후 선택지 트리 (deed_saved / deed_rerolled / B-NORMAL / B-AVAIL)
- 막힘 4분류와 잡별 도움 방향

## 다음 작업에 넘길 규칙

- prelaunch 첫 10명 관찰 시 이 감사표를 기준으로 세션을 분류
- deed_judged 후 사용자 행동을 잡별로 체크하되, J3 무저장 종료는 절대 이탈로 기록하지 않음
- deed_save_capped는 가용성/마찰이며 value/upgrade demand가 아님
