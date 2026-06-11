# Virtue Task-Completion Audit Table

- intent: `marketing-53`
- scope: docs-only / internal audit / no public copy, event, tracking, or deployment change
- permission: L1 docs-only
- status: archived

## 0. Purpose

Virtue의 첫 입력/결과 직후 순간을 `사용자 의도 → AI가 수행한 작업 → 사용자가 선택한 다음 행동`으로 읽는 task-completion 감사표를 작성한다.

목표: `deed_judged` 발화만으로 사용자의 task completion을 확인했다고 읽는 오류를 줄이고, J1/J2/J4=`deed_saved`, J3=`deed_judged` 매핑을 잡별 행동 증거로 보강한다.

모든 내용은 proposal-only 내부 기준. 공개 카피·이벤트·tracking/privacy·dashboard/session replay·배포·외부발송·비용·권한 변경 0.

## 1. Inherited criteria

| 기준 | 출처 | 적용 |
|---|---|---|
| First Value Mapping: J1/J2/J4=`deed_saved`, J3=`deed_judged` | m06-m10, m20-m29 | AI task completion ≠ user task completion. 이 분리가 감사표의 핵심 프레임. |
| Guided First-Value Is A Four-Stage Handoff | m51 | 결과 해석(3구간)→저장/종료(4구간) 접경에 초점. |
| Post-Response Flow Reveals Value, Not The Result Event | m44 | deed_judged 발화 직후 행동으로 value delivery 여부를 읽음. |
| Prompt Design Teaches Desired Result, Not UI Or Judgment | m52 | "사용자 의도" 컬럼에서 잡별 원하는 결과를 읽는 방법 제공. |
| AI Outcome Proxy Separation | m24 | deed_judged(AI 활동)와 deed_saved(사용자 수용)는 다른 proxy. |

## 2. 핵심 분리 기준

```
deed_judged = AI의 task completion (AI가 판정을 완료했다)
deed_saved  = 사용자의 task completion (사용자가 자신의 목적을 완료했다)
```

J3를 제외하면, AI task 완료 신호(deed_judged)는 사용자 task 완료 신호(deed_saved)가 아니다.

## 3. 잡별 Task-Completion 감사표

| Job | 사용자 의도 | AI가 수행한 작업 | 사용자 task completion 기준 행동 | 완료 이벤트 |
|---|---|---|---|---|
| **J1 기록** | 오늘 한 일을 기록으로 남기고 싶다 | 행동을 덕 점수/카드로 읽고 결과 제시 | 결과 카드 저장 (또는 재판정 후 저장) | `deed_saved` |
| **J2 쌓기** | 지금의 행동이 누적 기록에 더해지길 바란다 | 행동을 오늘의 기록으로 읽고 카드 제시 | 결과 카드 저장 → 누적 단계 추가 | `deed_saved` |
| **J3 AI 시각** | AI가 이 행동을 어떻게 읽는지 보고 싶다 | 행동에 대한 AI 시각/판정을 카드로 제시 | 카드를 읽고 종료 (저장 없이도 완료) | `deed_judged` |
| **J4 성찰** | 이 경험의 의미를 내 말로 보존하고 싶다 | 행동을 성찰 재료로 읽고 카드 제시 | 카드를 읽고 자신의 해석과 함께 저장 | `deed_saved` |

## 4. 결과 카드 이후 행동 분류표

| 결과 카드 이후 행동 | J1 읽기 | J2 읽기 | J3 읽기 | J4 읽기 |
|---|---|---|---|---|
| `deed_saved` | 완료 | 완료 | 선택 (정상 완료) | 완료 |
| `deed_judged` 후 바로 종료 | 보류 (저장 전 이탈 후보) | 보류 | 완료 (J3 정상 종료) | 보류 |
| `deed_rerolled` 후 `deed_saved` | 완료 (재판정 후 저장) | 완료 | 궁금증 심화 후 선택적 저장 | 완료 |
| `deed_save_capped` | 마찰/가용성 | 마찰/가용성 | 마찰/가용성 | 마찰/가용성 |
| `deed_judged` 후 긴 체류 후 저장 없이 종료 | B-MISMATCH 또는 B-NORMAL | B-MISMATCH 또는 B-NORMAL | 완료 | B-MISMATCH 또는 B-NORMAL |

## 5. 오독 방지 기준

1. **deed_judged = 사용자 task 완료 금지**: J3 외에는, AI가 결과를 보여준 것이 사용자의 task 완료가 아니다.
2. **J3 저장 없는 종료 = 이탈 금지**: J3에서 deed_saved 없이 종료는 정상 완료다.
3. **deed_save_capped = 가용성/마찰**: 저장 한도 초과는 value나 upgrade demand가 아니다.
4. **deed_rerolled 단독 = 불신 금지**: 재판정은 의도 관찰 전 보류다.

## 6. Prelaunch 첫 10명 수기 관찰 루프 (신규 계측 0)

관찰 포인트 1 (결과 카드 직후):
- 사용자가 결과 카드를 받은 직후 어떤 행동을 선택했는가? (저장 / 재판정 / 그대로 종료 / 잠시 체류 후 종료)

관찰 포인트 2 (세션 종료 후):
- 이 사용자가 "직접 해냈다"고 말할 수 있는 순간이 있었는가? 어느 시점인가?

## 7. First_verification_gate

이벤트명 6개 확인:

| 이벤트명 | 확인 출처 | 상태 |
|---|---|---|
| `deed_saved` | m06, m44, m51, m52 | 확인 |
| `deed_judged` | m06, m44, m51, m52 | 확인 |
| `deed_rerolled` | m40, m42, m44 | 확인 |
| `deed_save_capped` | m21, m28, m29, m42 | 확인 |
| `add_flow_started` | m40 | 확인 |
| `level_up_viewed` | m32 | 확인 |

출처노트: `source/external-links/marketing/2026-06-11-ai-onboarding-intent-to-task.md` — GitHub repo 미존재 (로컬 파일 추정). intent 명세에서 직접 추론.

Conflict marker: 0건

## 8. 기존 문서 충돌 검사

| 비교 대상 | 충돌 | 보완 관계 |
|---|---|---|
| marketing-51 (Four-Stage Handoff) | 없음 | 3·4구간을 task-completion 렌즈로 추가 세분화 |
| marketing-52 (Prompt Design Teaches Desired Result) | 없음 | 1구간(첫 입력)을 3·4구간(결과 직후)과 연결 |
| marketing-44 (Post-Response Flow) | 없음 | 결과 직후 행동을 완료/보류/마찰 표로 구체화 |
| first-real-user-baseline-template | 없음 | 수기 관찰 2문항이 first value 기록 칸과 보완 |

## 9. Changed assumptions

계승: J1/J2/J4=deed_saved, J3=deed_judged / m44 결과 직후 행동 관찰 / m51 "직접 해냈다" 기준점.

변경: 없음.

이번에 새로 배운 것: deed_judged를 AI task completion으로 명시 분리하면 J3 정상 종료가 자연히 도출된다.

다음 작업에 넘길 규칙: 결과 카드 직후 포인트 1/2를 손기록 필수로 둔다. deed_judged 직후 저장 여부를 task completion 지표로 쓰기 전 반드시 잡(J1-J4)을 확인한다.

## 10. MARKETING_LEARNINGS.md 승격 후보

"AI Task Completion And User Task Completion Are Different Events"

deed_judged는 AI의 task completion이고 deed_saved는 사용자의 task completion이다. J3를 제외하면 두 이벤트는 독립이다. J1/J2/J4에서 deed_judged를 사용자 task 완료로 읽는 것이 가장 흔한 activation 오독이다.

## 11. Verification gate

- 잡별 task-completion 감사표 작성 완료
- 이벤트명 6개 확인 완료
- conflict marker 0건
- m44, m51, m52 충돌 없음
- 공개 카피·이벤트·tracking/privacy·배포·외부발송·비용 변경 0
- 신규 계측 0 (수기 관찰 2문항만)
