# Virtue Launch-Ready PLG Signal Gate
# marketing-59 — 2026-06-14

> 최신 PLG first-win/activation/PQL 우선순위를 Virtue prelaunch 신호 위계로 번역한다.
> First-10 관찰에서 acquisition 문제, activation 문제, measurement-too-early 상태를 혼동하지 않게 한다.

## 전제

- J1/J2/J4 first value = `deed_saved`
- J3 first value = `deed_judged` (저장 없는 종료 = 정상)
- 모든 신호는 수기 관찰이며 비율·임계값으로 환산하지 않는다
- synthetic/mock/self-test는 항상 먼저 분리한다

---

## PLG 신호 3열 위계표

### 지금 볼 신호 (First-10 수기 관찰)

| 신호 | 측정 방법 | 분류 방법 |
|------|---------|----------|
| **First value 발화** | deed_saved (J1/J2/J4) / deed_judged (J3) / 미발화 | 성공 / 보류 |
| **Traffic source** | human real use / self-test / synthetic / mock 분류 | 분석 전 제외 |
| **Session end type** | 성공(first value 도달) / J3 정상종료 / 마찰(cap·503·지연) / 보류(미발화) | 4칸 분류 |
| **Guided break 위치** | first_input / ai_wait / result_interpretation / save_or_exit / 없음 | B-LOST 후보 |
| **결정-위임 인지** | "AI가 결정해줬다" / "AI가 보여줬다(나의 선택)" | 손기록 |
| **User own language** | 가치를 자기 말로 표현한 문장 | 원문 그대로 |
| **Off-instrument** | 웃음·놀람·반박·보여주기·재전달 | 손기록 |
| **cap/503/지연** | availability/friction 분류 | upgrade demand 아님 |

### 보류할 신호 (측정 불가 또는 표본 부족)

| 신호 | 보류 이유 |
|------|----------|
| Activation rate % | 측정 readiness 미확인, n<10 |
| deed_save_capped → upgrade demand | availability/friction이지 demand가 아님 |
| J3 judged-saved gap → churn | J3 정상종료이므로 실패 아님 |
| D7 retention % | 시간 부족, 표본 불충분 |
| PMF score | prelaunch 적용 금지 |
| D7 non-return = churn | reactivation 후보이지 실패 아님 |
| PQL 단일 이벤트 | bundle 확인 전 결론 금지 |
| NPS / 만족도 수치 | 합격선 없음 |

### Launch 이후 볼 신호 (Post-launch gate)

| 신호 | 조건 |
|------|------|
| PQL 후보 (bundle) | 반복 deed_saved/deed_judged + D7 재방문 묶음 |
| Activation rate % | 측정 readiness 확인 후 |
| D7 retention | D7 이후, 충분 표본 |
| Conversion (upgrade) | First value 이후 반복 가치 확인 후 |
| Viral coefficient | 확장 표본 후 |
| Channel quality | 트래픽 분류 완료 후 |

---

## First-10 수기 Review Gate

각 사용자(1~10)별 손기록 체크리스트.

### A. Pre-session (사용 전 2문항)

- [ ] **현재 행동 / 대체재**: 지금 비슷한 걸 어떻게 하고 있나요?
- [ ] **잡 신호 / 기대**: 왜 오셨나요? (J1 기록쌓기 / J2 습관화 / J3 AI판정 / J4 회고 — 하나 선택)

### B. Session 관찰 (손기록)

- [ ] **잡 확인**: J1 / J2 / J3 / J4
- [ ] **First value 발화**:
  - J1/J2/J4: `deed_saved` 발화? Y / N
  - J3: `deed_judged` 발화? Y / N
- [ ] **Traffic 분류**: 실사용 / self-test / synthetic / mock
- [ ] **Guided break 위치**: first_input / ai_wait / result_interpretation / save_or_exit / 없음
- [ ] **세션 종료 유형**:
  - 성공: first value 도달
  - J3 정상종료: deed_judged 후 무저장 종료 (실패 아님)
  - 마찰: deed_save_capped / 503 / 지연 (availability/friction, upgrade demand 아님)
  - 보류: first value 미발화, 막힘 원인 미분류
- [ ] **Off-instrument**: 웃음 / 놀람 / 반박 / 보여주기 / 재전달 / 없음 (손기록)

### C. Post-session (사용 후 3문항)

- [ ] "첫 가치는 어느 순간에 느꼈나요?" (first value 위치)
- [ ] "막혔거나 이상했던 점은?" (friction)
- [ ] "AI가 결정해줬다 vs AI가 정리해서 보여줬다 — 어느 쪽 느낌이었나요?" (결정-위임 인지)

### D. Self-description 캡처

- [ ] 가치를 자기 말로 설명한 문장: **[원문 그대로 기록]**

---

## 제외 항목 (분석에 넣지 않는다)

- synthetic/mock/self-test 세션
- `deed_save_capped` → upgrade demand로 환산 금지
- J3 judged-saved gap → 실패/이탈 판정 금지
- 성패율·activation rate·PMF·전환율·retention% 환산 금지

---

## 다음 액션

- First-10 관찰 시작 시 이 체크리스트를 손기록으로 사용한다
- 신규 이벤트·PostHog dashboard·공개 카피·배포는 여전히 approval-needed
- Prelaunch 신호 해석 기준은 marketing-55/56/58 계약과 일관하게 유지한다

---

## 계승한 기준

- First Value Mapping: J1/J2/J4=deed_saved, J3=deed_judged (marketing-06 외)
- Prelaunch Decision Boundary: 작은 표본은 방향 재료, 확정 지표 아님 (marketing-08 외)
- Measurement Readiness Is A Separate Gate: 측정 가능성 ≠ 측정값 성패 (marketing-34)
- PQL Is A Bundle, Not A Single Event: 반복+재방문 묶음만 PQL (marketing-41)
- Session Value Is Read By Job, Not Event Count (marketing-42)
- First-User Learning Loop: 4지점 손기록 루프 (marketing-47)

## 이번에 새로 정리한 것

- PLG Foundation→Activation→Conversion 순서를 Virtue prelaunch 3열 위계표로 번역
- "지금 볼 / 보류 / launch 이후" 분류 기준을 explicitly 문서화
- First-10 수기 review gate를 Pre/Session/Post/Self-description 4구간으로 정리

## 다음 Marketer에게 넘길 규칙

- First-10 관찰 후 결과 해석은 비율 아닌 언어로 한다
- "보류" 신호를 다음 Heartbeat에서 실수로 활성 신호로 읽지 않도록 이 표를 참조한다
- Launch 이후 신호를 열기 전에 Measurement Readiness gate를 다시 확인한다
