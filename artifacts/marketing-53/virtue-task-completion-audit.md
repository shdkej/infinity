# Virtue 첫 입력/결과 task-completion 감사표

- intent: `marketing-53`
- source_note: `source/external-links/marketing/2026-06-11-ai-onboarding-intent-to-task.md` (로컬 워크스페이스 / GitHub 미동기화)
- scope: docs-only / proposal-only
- status: internal audit
- permission: L1 docs-only

## 0. 목적

AI 온보딩에서 "답변이 나왔는가"보다 "사용자 의도가 작업 완료로 이어졌는가"로 읽는 task-completion 렌즈를 Virtue에 맞게 번역한다.

첫 입력/결과 직후를 `사용자 의도 → AI가 수행한 작업 → 사용자가 선택한 다음 행동` 3열로 분석하여:
- `deed_judged` 과대평가를 줄이고
- 잡별 first value(J1/J2/J4=`deed_saved`, J3=`deed_judged`) 해석을 행동 증거로 보강한다

신규 이벤트, 속성, tracking/privacy, dashboard, session replay, 공개 카피, 배포를 만들지 않는다.

## 1. 계승 기준

| 기준 | 계승 내용 |
|---|---|
| First Value Mapping | J1/J2/J4 = `deed_saved`, J3 = `deed_judged` |
| Guided First-Value Is A Four-Stage Handoff | 첫 입력 → AI 대기 → 결과 해석 → 저장/종료 4구간 |
| Post-Response Flow Reveals Value, Not The Result Event | 결과 이벤트 발화보다 직후 선택 행동을 읽음 |
| Session Value Is Read By Job, Not Event Count | 이벤트 수가 아니라 잡별 first value 도달과 종료 성격 |
| AI Outcome Proxy Separation | "AI 활동" ≠ "사용자 결과 수용" |
| Decision-Delegation Risk Rides The Verb | 결과 해석에서 판결 프레임 vs 관점 프레임 구분 |

## 2. 기존 이벤트명 6개 확인

| 이벤트명 | 역할 |
|---|---|
| `add_flow_started` | 입력 흐름 시작 (사용자 의도 진입) |
| `deed_judged` | AI 판단 결과 반환 (AI 수행 작업 완료) |
| `deed_saved` | 저장 완료 (J1/J2/J4 first value 도달) |
| `deed_rerolled` | 재판정 요청 (사용자 다음 행동: 결과 재시도) |
| `deed_save_capped` | 저장 상한 도달 (availability/friction, value 아님) |
| `level_up_viewed` | 레벨업 화면 확인 (J2 누적 payoff 신호) |

이 6개 이벤트는 기존 마케팅 문서 전반에 걸쳐 사용된 이름이며 재정의하지 않는다.

## 3. task-completion 감사표 (잡별)

### 3열 구조

| 사용자 의도 | AI가 수행한 작업 | 사용자가 선택한 다음 행동 |
|---|---|---|
| 사용자가 `/add`에 진입할 때 갖는 목적 | AI가 실제로 처리한 것 (이벤트로 확인 가능) | `deed_judged` 직후 사용자의 실제 선택 행동 |

### J1 기록형 — first value `deed_saved`

| 의도 | AI 수행 | 사용자 다음 행동 | 판독 |
|---|---|---|---|
| 오늘 한 일을 남겨두고 싶다 | AI 판정 반환 (`deed_judged`) | `deed_saved` | ✅ task complete — 의도와 행동이 일치. first value 도달. |
| 오늘 한 일을 남겨두고 싶다 | AI 판정 반환 (`deed_judged`) | `deed_rerolled` | ⏸ 재시도 — AI 결과가 기록할 재료로 부족하다고 느낌. 의도 달성 전. |
| 오늘 한 일을 남겨두고 싶다 | AI 판정 반환 (`deed_judged`) | 저장 없이 종료 | ⚠️ 보류 — J1에서 저장 없는 종료는 B-LOST/B-MISMATCH/B-AVAIL 분류 필요. |
| 오늘 한 일을 남겨두고 싶다 | `deed_save_capped` | 저장 차단 | ❌ availability/friction — value 미달·upgrade demand 아님. |

### J2 누적형 — first value `deed_saved`

| 의도 | AI 수행 | 사용자 다음 행동 | 판독 |
|---|---|---|---|
| 오늘 것을 쌓아가고 싶다 | AI 판정 반환 (`deed_judged`) | `deed_saved` + `level_up_viewed` | ✅ task complete — 저장으로 누적 첫 걸음. |
| 오늘 것을 쌓아가고 싶다 | AI 판정 반환 (`deed_judged`) | `deed_saved` 후 바로 종료 | ✅ task complete — 오늘 누적 완료. |
| 오늘 것을 쌓아가고 싶다 | AI 판정 반환 (`deed_judged`) | 저장 없이 종료 | ⚠️ 보류 — J2 의도인데 저장 안 함. B-LOST 후보. |

### J3 AI 호기심형 — first value `deed_judged`

| 의도 | AI 수행 | 사용자 다음 행동 | 판독 |
|---|---|---|---|
| AI가 이걸 어떻게 읽는지 보고 싶다 | AI 판정 반환 (`deed_judged`) | 저장 없이 종료 | ✅ task complete (J3 정상 종료) — judged−saved 갭 = 성공. |
| AI가 이걸 어떻게 읽는지 보고 싶다 | AI 판정 반환 (`deed_judged`) | `deed_rerolled` | ⏸ 재시도 — AI 읽기가 기대와 달라 다시 봄. |
| AI가 이걸 어떻게 읽는지 보고 싶다 | AI 판정 반환 (`deed_judged`) | `deed_saved` | ℹ️ 선택적 저장 — task complete는 `deed_judged`에서 끝남. 저장은 범퍼. |
| AI가 이걸 어떻게 읽는지 보고 싶다 | `deed_judged` 없음 (대기 중 이탈) | 이탈 | ⚠️ 보류 — AI 대기 단계 마찰/availability. |

### J4 회고형 — first value `deed_saved`

| 의도 | AI 수행 | 사용자 다음 행동 | 판독 |
|---|---|---|---|
| 요즘 어떻게 지냈는지 돌아볼 재료를 남기고 싶다 | AI 판정 반환 (`deed_judged`) | `deed_saved` | ✅ task complete — 회고 재료 저장 완료. |
| 요즘 어떻게 지냈는지 돌아볼 재료를 남기고 싶다 | AI 판정 반환 (`deed_judged`) | 저장 없이 종료 | ⚠️ 보류 — B-LOST/B-MISMATCH 분류 필요. |

## 4. `deed_judged` 과대평가 방지 체크리스트

| 잘못된 읽기 | 올바른 읽기 |
|---|---|
| J1/J2/J4에서 `deed_judged` = task complete | J1/J2/J4의 task complete는 `deed_saved`다. `deed_judged`는 통과점. |
| J3에서 `deed_judged` 후 저장 없는 종료 = 실패 | J3의 task complete는 `deed_judged`다. 저장은 선택 범퍼. |
| `deed_rerolled` = 불신 | 결과 재시도는 AI 읽기를 더 보려는 행동일 수 있다. |
| `deed_save_capped` = task 미완료 or upgrade demand | availability/friction 신호. value 미달이 아님. |
| 짧은 세션(`deed_judged` 직후 종료) = 낮은 가치 | J3에서는 task complete다. |

## 5. 첫 10명 관찰에 붙이는 수기 칸

| 칸 | 설명 |
|---|---|
| `task_complete_moment` | 사용자가 "됐다"고 느낀 순간 — `deed_judged` / `deed_saved` / `level_up_viewed` / 없음 |
| `next_action_after_result` | 결과 직후 실제 행동 — save / reroll / explain / normal_exit / passive_wow / friction |

## 6. 기존 문서와의 보완 관계

| 선행 문서 | 역할 | 이번 문서의 추가 | 충돌 |
|---|---|---|---|
| `first-10-design-user-ask-script` (m47) | 초대→pre→post→자기 말 루프 | task-completion 3열로 `deed_judged` 직후 행동 해석 보강 | 없음 |
| `virtue-guided-first-value-session-audit` (m51) | 4구간 안내 끊김 위치 찾기 | 안내 이후 사용자 선택을 task-completion 관점으로 읽는 층 추가 | 없음 |
| `virtue-add-first-input-prompt-design-audit` (m52) | 첫 입력 prompt design 3분류 | 결과 직후 사용자 선택 읽기 보완 | 없음 |

## 7. 해석 금지선

- J1/J2/J4 first value = `deed_saved`. J3 first value = `deed_judged`. 재정의 0.
- J3 저장 없는 종료를 task 미완료·이탈·가치 부재로 읽지 않는다.
- `deed_save_capped`, 503, 지연은 availability/friction이지 value·upgrade demand가 아니다.
- task-completion 읽기를 비율·activation rate·PMF·전환율·retention%로 환산하지 않는다.
- 신규 이벤트·속성·tracking/privacy·dashboard/session replay·공개 카피·배포·외부 발송·비용·권한 변경은 모두 approval-needed다.

## 8. 가정 분리

### 계승한 기준
- J1/J2/J4 first value = `deed_saved`; J3 first value = `deed_judged` — 재정의 0.
- `deed_judged` 발화 ≠ 이해/수용/가치 전달 확정.
- 결과 직후 행동은 AI 활동 proxy(activity)와 사용자 수용 proxy(acceptance)를 분리해서 읽는다.

### 변경한 가정
- 없음.

### 충돌
- 없음.

### MARKETING_LEARNINGS.md 승격 후보
- **Task-Completion Lens: Deed-Judged Is A Waypoint, Not A Destination** — AI 온보딩은 "AI가 응답했는가"보다 "사용자 의도가 작업 완료로 이어졌는가"로 읽어야 한다. J3의 정상 종료는 무저장이어도 task complete다. J1/J2/J4에서 `deed_judged`는 통과점이지 결론이 아니다.

## 9. 검증 게이트

- 소스 노트 경로: 로컬 워크스페이스, GitHub 미동기화 — 경로 확인 부분 통과.
- 기존 이벤트명 6개 확인: `add_flow_started`, `deed_judged`, `deed_saved`, `deed_rerolled`, `deed_save_capped`, `level_up_viewed` — 재정의 없음.
- 신규 계측/tracking/privacy/공개 카피/배포/외부 발송/비용: 변경 0.
- Conflict marker: 0건.
