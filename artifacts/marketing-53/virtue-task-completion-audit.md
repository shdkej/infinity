# Virtue task-completion 감사표 (AI 온보딩 intent-to-task)

> intent: marketing-53 | created: 2026-06-11 | permission: L1 docs-only
> purpose: prelaunch 첫 10명 관찰 시 신규 계측 없이 손기록 기준 명확화

## 계승한 기준 (MARKETING_LEARNINGS)

- **First Value Mapping**: J1/J2/J4=`deed_saved`, J3=`deed_judged`
- **Guided First-Value Is A Four-Stage Handoff** (marketing-51): 첫 입력 전 → AI 판단 대기 → 결과 해석 → 저장/종료
- **Prompt Design Teaches Desired Result, Not UI Or Judgment** (marketing-52): 첫 입력 기본값은 사용자가 원하는 결과를 AI에게 알려주는 것

## 검증 게이트

- 출처노트 `source/external-links/marketing/2026-06-11-ai-onboarding-intent-to-task.md`: **파일 없음** — 인박스 메모의 rationale/expected_impact로 진행
- 기존 이벤트명 6개 확인:
  - `deed_saved` ✓ (J1/J2/J4 first value)
  - `deed_judged` ✓ (J3 first value, J1/J2/J4 통과점)
  - `deed_rerolled` ✓ (재판정, 불신 아님)
  - `deed_save_capped` ✓ (가용성/마찰 차단)
  - `add_flow_started` ✓ (흐름 시작)
  - `level_up_viewed` ✓ (J2 누적 비교 표면)
- conflict marker: 0건
- 기존 activation/first-user 문서 충돌: 없음 (First Value Mapping, Guided First-Value, Prompt Design 3개 기준과 정렬됨)

---

## 주 감사표: 잡별 task-completion 3열

| 잡 | 사용자 의도 | AI가 수행한 작업 | 사용자가 선택한 다음 행동 | first_value 이벤트 | task completion 판정 |
|---|---|---|---|---|---|
| **J1** (반복 기록) | 오늘 한 일을 기록하고 싶다 | `add_flow_started` → AI 판정 카드(`deed_judged`) 생성 | 저장 (`deed_saved`) | `deed_saved` | ✓ 완료 |
| **J2** (누적 성장) | 이전 기록과 비교해 성장을 확인하고 싶다 | 누적 패턴 기반 AI 판정 + `level_up_viewed` | 저장 (`deed_saved`) + 레벨 확인 | `deed_saved` (2회 이상 누적) | ✓ 완료 |
| **J3** (AI 관점) | AI가 내 일/행동을 어떻게 보는지 알고 싶다 | AI 판정 결과 카드(`deed_judged`) 생성 | 결과 확인 후 종료 (무저장도 정상 완료) | `deed_judged` | ✓ 완료 (무저장 정상) |
| **J4** (영구 기록) | 중요한 일을 남기고 싶다 | 맥락 기반 AI 판정 후 저장 가능 | 저장 (`deed_saved`) | `deed_saved` | ✓ 완료 |

### 3열을 읽는 방법

- **사용자 의도**: 사용자가 `/add`를 열기 전에 가진 목표. 손기록 시 "오늘 왜 여기 왔어요?" 질문으로 포착.
- **AI가 수행한 작업**: 이벤트로 확인. `deed_judged` = AI 판정 카드 생성. `level_up_viewed` = 누적 비교 표면 노칠.
- **사용자가 선택한 다음 행동**: 결과 카드 후 행동. `deed_saved`, `deed_rerolled`, 무저장 종료, `deed_save_capped` 중 하나.

---

## 보조표: task-completion gap 분류

| 관찰 상황 | 잡별 판정 | 다음 관찰 후보 |
|---|---|---|
| `add_flow_started` → `deed_judged` → 종료 (저장 없음) | J3=**완료**, J1/J2/J4=**보류** | J1/J2/J4이면 B-LOST 또는 B-MISMATCH 확인 |
| `deed_judged` → `deed_saved` | J1/J2/J4=**완료** | — |
| `deed_judged` → `deed_rerolled` → `deed_saved` | 모든 잡=**완료** (재판정 후 저장) | reroll은 불신 아님, 원하는 결과 탐색 중 |
| `deed_judged` → `deed_rerolled` → 종료 | **보류** | B-MISMATCH(결과 기대 불일치) 후보 |
| `deed_save_capped` | **마찰/가용성 차단** | value proxy 아님. availability/friction 분류 |
| `add_flow_started` → 중단 | **보류** | B-LOST(길 잊음) 또는 B-AVAIL 후보. 이탈 단정 금지 |
| `level_up_viewed` → 종료 (저장 없음) | J2=**보류** (second value 미도달) | B-MISMATCH 또는 B-NORMAL 확인 |

---

## intent-to-task 렌즈 적용 방법 (prelaunch 첫 10명 손기록)

Virtue에서 **task completion = 사용자가 원하던 결과를 자기 말로 얻었다는 확인**이다.

첫 세션 후 아래 3개만 손기록한다:

1. **"오늘 왜 여기 왔어요?"** → 사용자 의도 포착 (잡 신호 판별)
2. **"/add 결과를 보고 뫐을 했어요?"** → 사용자가 선택한 다음 행동 포착
3. **"AI가 한 일이 원하던 것이었나요?"** → task completion 인식 여부

이 세 질문의 답이 위 감사표의 3열에 대응한다.

---

## 주의

- 공개 카피, 이벤트 신규 추가, tracking/privacy, dashboard, session replay, 배포, 외부 발송, 비용, 권한 변경 0.
- 이 감사표는 내부 관찰 도구(proposal-only)다. 공개 문서·이벤트 변경은 별도 approval-needed.
- `deed_judged` 발화만으로 task completion 확정 금지 (J1/J2/J4는 통과점).
- J3 무저장 종료는 task completion 정상 완료.
- `deed_save_capped`는 마찰/가용성 차단이지 task completion이 아님.

---

## 다음 Marketer에게 넘길 규칙 후보

- **intent-to-task 감사표를 prelaunch 첫 10명 관찰 기준 문서 묶음에 추가**: first-user-learning-loop(marketing-47), guided-first-value-session-audit(marketing-51), add-first-input-prompt-design-audit(marketing-52)와 세트로 참조.
- **사용자 의도와 AI가 수행한 작업 사이의 gap이 B-MISMATCH 주요 출체**: "원하는 결과를 AI가 실제로 정리한 형태로 연결했는가"가 prelaunch 관찰의 핵심 질문.
- **J3 intent-to-task 경로가 가장 다름**: 다른 잡과 달리 저장이 task completion 조건이 아님을 관찰 설계 때 항상 분리.
