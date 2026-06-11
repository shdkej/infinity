# Virtue Task-Completion 감사표

> 작성: 2026-06-11 (Infinity Heartbeat marketing-53)
> 권한: L1 docs-only
> 출처: MARKETING_LEARNINGS.md (m51, m44, m52, m32, m06), INTENTS.md Inbox 인라인 컨텍스트
> 출처노트: `source/external-links/marketing/2026-06-11-ai-onboarding-intent-to-task.md` — **파일 미존재. 인라인 컨텍스트로 대체.**
> first_verification_gate: 기존 이벤트명 6개 확인 — conflict marker 0건

## 목적

Virtue 첫 입력/결과 직후 사용자 경험을 세 축으로 읽는다:

1. **사용자 의도** — 이 잡(Job)에서 사용자가 원하는 task completion은 무엇인가
2. **AI가 수행한 작업** — AI가 `deed_judged` 이벤트까지 실제로 한 일
3. **사용자가 선택한 다음 행동** — 결과 카드 직후 선택 가능한 행동과 각각의 해석

### 왜 필요한가

`deed_judged` 이벤트는 모든 잡에서 발화한다. 하지만 AI가 판정 결과를 보여줬다는 사실이 "task completion"과 동의어가 아니다. J1/J2/J4에서는 `deed_judged` 이후 `deed_saved`가 있어야 first value가 닫힌다. `deed_judged`만으로 전체 활성화를 읽으면 J1/J2/J4의 저장률 손실을 놓친다.

---

## 감사표: 잡별 Task-Completion 흐름

| # | 잡 | 사용자 의도 | AI가 수행한 작업 | First Value 이벤트 | `deed_judged` 역할 | `deed_judged` 과대평가 위험 |
|---|---|---|---|---|---|---|
| J1 | 기록형 | 오늘 한 일을 기록하고 싶다 | 행동 입력 수신 → 잡별 분류·요약 → 판정 결과 표시 | **`deed_saved`** | 통과점 (결과 확인) | **높음**: 저장 전 종료를 "완료"로 읽으면 실제 저장 손실 미측정 |
| J2 | 누적형 | 행동을 쌓아 AI 관점의 패턴을 보고 싶다 | 행동 입력 수신 → 누적 분류·판정 → 현재 판정 결과 표시 | **`deed_saved`** (+ D7 재방문) | 통과점 (단발 판정 확인) | **높음**: J2 가치는 누적이므로 단발 `deed_judged`는 의미 더 약함 |
| J3 | AI 호기심형 | AI가 나를 어떻게 보는지 궁금하다 | 행동 입력 수신 → AI 관점 판정 → 판정 결과 표시 | **`deed_judged`** | **도착점 (task complete)** | **낮음**: J3에서 `deed_judged`는 실제 first value |
| J4 | 회고형 | 지난 행동을 돌아보고 싶다 | 행동 입력 수신 → 회고 분류·판정 → 회고 결과 표시 | **`deed_saved`** | 통과점 (AI 관점 확인) | **높음**: 회고 가치는 저장+이후 열람에서 완성 |

---

## 결과 카드 직후: 사용자 선택 행동과 잡별 해석

| 다음 행동 | 이벤트 | J1 해석 | J2 해석 | J3 해석 | J4 해석 |
|---|---|---|---|---|---|
| 저장 | `deed_saved` | ✅ task complete | ✅ task complete | 선택적 (추가) | ✅ task complete |
| 한 번 더 (재판정) | `deed_rerolled` | 재시도 (value seeking) | 재시도 | 다른 관점 탐색 (정상) | 재시도 |
| 저장 없이 종료 | (종료) | ⚠️ 보류 (저장 전 이탈?) | ⚠️ 보류 | ✅ 정상 종료 | ⚠️ 보류 |
| 저장 상한 도달 | `deed_save_capped` | availability/friction | availability/friction | availability/friction | availability/friction |
| 세션 재방문 | `level_up_viewed` 등 | J2 핵심 신호 | ✅ 누적 가치 시작 | value recall | 회고 심화 |

> **주의**: `deed_save_capped`는 어떤 잡에서도 value/upgrade demand가 아니라 availability/friction 신호다 (m28, m29).

---

## deed_judged 과대평가 방지 판독 순서

`deed_judged` 이후 활성화를 읽을 때:

1. **잡 분류 먼저** — 이 사용자는 어떤 잡으로 왔는가 (J1/J2/J4 vs J3)
2. **J3 분리** — J3라면 `deed_judged` = first value, 저장 없는 종료 = 정상
3. **J1/J2/J4 확인** — `deed_judged` 이후 `deed_saved` 발화 여부 확인
4. **종료 성격 분류** — 저장 없는 종료는 B-LOST / B-MISMATCH / B-AVAIL / B-NORMAL 중 어느 쪽인가
5. **가용성 분리** — `deed_save_capped`, 503, 지연은 먼저 분리

---

## 기존 문서와의 충돌 검사

| 기존 기준 | 출처 | 이번 감사표와 관계 |
|---|---|---|
| J1/J2/J4=`deed_saved`, J3=`deed_judged` | MARKETING_LEARNINGS First Value Mapping | 계승 — 동일 |
| J3 저장 없는 종료 = 정상 | m51, m44 | 계승 — 동일 |
| `deed_save_capped` = availability/friction | m28, m29 | 계승 — 동일 |
| 4구간 handoff (m51) | Guided First-Value | 보완 — 3축 흐름으로 세분화 |
| 결과 직후 관찰 (m44) | Post-Response Flow | 보완 — task-completion lens 추가 |

**conflict marker 0건** — 기존 기준과 충돌 없음.

---

## 이벤트명 검증 (first_verification_gate)

기존 이벤트명 6개 (MARKETING_LEARNINGS.md 및 prior reports 기준):

1. `add_flow_started` — 입력 흐름 시작
2. `deed_judged` — AI 판정 결과 표시
3. `deed_saved` — 사용자 저장
4. `deed_rerolled` — 재판정 요청
5. `deed_save_capped` — 저장 상한 도달
6. `level_up_viewed` — 레벨업 화면 열람

이 이벤트명은 감사표 전체에서 일관 사용됨. 신규 이벤트명 도입 0.

---

## 금지선 확인

- 공개 카피·버튼/placeholder 변경: 0
- 신규 이벤트·속성·tracking/privacy·dashboard/session replay: 0
- 배포·외부발송·비용·권한 변경: 0
- 코드 변경: 0

---

## 계승한 기준

1. First Value Mapping — J1/J2/J4=`deed_saved`, J3=`deed_judged` (m06~m29)
2. Guided First-Value Is A Four-Stage Handoff (m51) — 결과 해석 구간의 task-completion 독해 강화
3. Post-Response Flow Reveals Value (m44) — 결과 카드 직후 선택 행동을 잡별로 해석

## 이번에 새로 배운 것

- `deed_judged` 이벤트는 전체 잡에서 동일하게 발화하지만, 그 의미는 잡별로 반전된다 (J3=도착점, J1/J2/J4=통과점)
- task-completion 감사는 "이벤트 발화 여부"가 아니라 "이 잡에서 무엇이 작업 완료인가"를 먼저 정의해야 한다

## 다음 Marketer에게 넘길 규칙

- 활성화 보고에서 `deed_judged` 수치를 단독으로 제시할 때 잡 분류를 먼저 병기할 것
- J3 세션(deed_judged 후 저장 없음)을 이탈/미완으로 분류하지 않도록 분류 로직에서 먼저 제외할 것

## MARKETING_LEARNINGS 승격 후보

**Task-Completion Is Job-Defined, Not Event-Defined**: AI 온보딩에서 "작업 완료"는 어떤 이벤트가 발화했는지가 아니라, 이 잡(Job)에서 사용자가 원하는 결과가 달성됐는지로 읽어야 한다. 동일 이벤트(`deed_judged`)가 J3에서는 first value이고 J1/J2/J4에서는 통과점이다. 판독 순서: 잡 분류 → J3 분리 → J1/J2/J4의 `deed_saved` 확인 → 종료 성격 분류 → 가용성 분리.