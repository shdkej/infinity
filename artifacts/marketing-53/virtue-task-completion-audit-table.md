# Virtue 첫 입력/결과 task-completion 감사표

- intent: `marketing-53`
- source_note: `source/external-links/marketing/2026-06-11-ai-onboarding-intent-to-task.md` (미존재; 인박스 맥락으로 대체)
- scope: docs-only / internal observation criterion
- status: internal criterion
- permission: L1 docs-only

## 0. 목적

AI 온보딩은 답변이 나왔는가보다 **사용자 의도가 작업 완료로 이어졌는가**로 읽는 것이 더 정확한 첫 세션 판단이다. 이 감사표는 Virtue의 첫 입력/결과 직후를 `사용자 의도 → AI가 수행한 작업 → 사용자가 선택한 다음 행동` 세 열로 읽어, prelaunch 첫 10명 관찰에서 `deed_judged` 과대평가를 줄이고 잡별 행동 증거를 보강하는 내부 수기 기준이다.

신규 이벤트, 속성, 공개 카피, tracking/privacy, dashboard, session replay, 배포, 외부 발송, 비용, 권한 변경은 없다.

## 1. 계승 기준

| 기준 | 계승 내용 | 이번 문서의 위치 |
|---|---|---|
| First Value Mapping | J1/J2/J4 = `deed_saved`, J3 = `deed_judged` | task-completion 종료점 |
| Guided First-Value Is A Four-Stage Handoff | 첫 입력 전 → AI 대기 → 결과 해석 → 저장/종료 | 각 구간의 task-completion 읽기 |
| Prompt Design Teaches Desired Result | 첫 입력은 UI가 아니라 원하는 결과를 AI에게 알려주는 일 | 의도 열에서 "원하는 결과"를 기록 |
| Session Value Is Read By Job, Not Event Count | 이벤트 수가 아니라 잡별 first value 도달과 종료 성격 | task-completion = first value 도달 여부 |
| Post-Response Flow Reveals Value, Not The Result Event | `deed_judged` 발화보다 그 직후 행동을 읽음 | 다음 행동 선택 열 |

## 2. task-completion 감사표 (3열 프레임)

| 잡 | 사용자 의도 | AI가 수행한 작업 | 사용자가 선택한 다음 행동 | task-completion 기준 |
|---|---|---|---|---|
| J1 기록 | 오늘 한 일을 한 줄로 남긴다 | 입력된 행동을 잡 점수·요약으로 변환한다 | `deed_saved` (저장) | **저장 발화 = 완료.** 저장 없이 닫히면 의도 미완성(B-LOST 후보 또는 입력 혼란) |
| J2 누적 | 오늘 것을 쌓이는 총량에 더한다 | 입력을 누적 기록으로 편입한다 | `deed_saved` (저장) | **저장 발화 = 완료.** 저장 없이 닫히면 의도 미완성 |
| J3 AI 관점 | AI가 이것을 어떻게 보는지 확인한다 | 입력에 대한 관점/판정을 반환한다 | `deed_judged` (결과 도달) — 저장은 선택 | **`deed_judged` 발화 = 완료.** 저장 없는 종료는 정상 완료이며 미완성 아님 |
| J4 성찰 | 이 경험을 내 말로 보존한다 | 입력·결과를 성찰 기록으로 정리한다 | `deed_saved` (저장) | **저장 발화 = 완료.** 결과만 보고 닫히면 성찰 보존 의도 미완성 후보 |

## 3. 잡별 deed_judged 해석 교정

`deed_judged` 이벤트는 모든 잡에서 발화하지만 task-completion 역할이 다르다.

| 잡 | deed_judged 역할 | deed_judged만 발화한 경우 해석 |
|---|---|---|
| J1 기록 | 결과를 보는 통과점 | **미완성 후보.** 저장 없이 닫혔으면 B-LOST 또는 입력/결과 혼란 후보 |
| J2 누적 | 누적 편입 전 확인 통과점 | **미완성 후보.** 저장 없이 닫혔으면 누적 의도 미완성 |
| J3 AI 관점 | **도착점 = first value** | **완료.** 저장 없는 종료가 정상 task-completion이다 |
| J4 성찰 | 성찰 소재 확인 통과점 | **미완성 후보.** 성찰 의도가 있었다면 저장이 완성 조건 |

핵심: `deed_judged` 한 번으로 J1/J2/J4 task-completion을 판단하지 않는다. J3에서만 `deed_judged` = task-completion이다.

## 4. 다음 행동 선택 분류표

| 다음 행동 | 이벤트/관찰 | task-completion 읽기 | 잡별 해석 |
|---|---|---|---|
| 저장 | `deed_saved` | 완료 | J1/J2/J4 = 완료. J3 = 완료(선택 완료) |
| 재시도 | `deed_rerolled` | 의도 미충족 후 재시도 | J3 관점이 원하던 것과 달랐다 → 의도는 살아 있음 |
| 수정/수동 입력 | 관찰만 | 자기화 = 결과를 내 말로 수정 | J1/J4 강한 자기화 신호, J3 결정-위임 부재 확인 |
| 그냥 닫기 | 관찰만 | J3 = 정상 완료. J1/J2/J4 = 보류 | J3는 실패로 읽지 않는다 |
| 저장 한도 도달 | `deed_save_capped` | availability/friction — task-completion 아님 | value, upgrade demand, 완료로 읽지 않는다 |
| 공유/보여 주기 | 관찰만 (off-instrument) | shareworthiness 신호 — task-completion과 독립 | 저장 없어도 공유할 수 있다(특히 J3) |

## 5. 수기 기록 칸 (기존 문서 보완)

| 칸 | 허용 값 | 목적 |
|---|---|---|
| intent_read | record / accumulation / ai_curiosity / reflection / unclear | 사용자가 말한 의도 또는 관찰자 추정 잡 |
| ai_work_landed | deed_judged_only / deed_judged_then_save / deed_save_direct / capped / error | AI가 완료한 작업 유형 |
| next_action | saved / rerolled / modified / closed_normal / closed_blost / capped | 사용자의 실제 선택 |
| task_completed | yes / partial / no / pending | intent + ai_work + next_action 3축 일치 여부 |
| notes | 자유 기록 | 의도가 바뀐 순간, 위임/자기화 발언, 의외 발화 |

## 6. 기존 문서와의 보완 관계

| 선행 문서 | 역할 | 이번 문서가 추가하는 것 | 충돌 여부 |
|---|---|---|---|
| `marketing-51` guided first-value audit | 4구간 안에서 어디서 안내가 끊겼는지 | 안내 끊김 전에 의도가 완료됐는지를 task-completion 3열로 읽음 | 충돌 없음 |
| `marketing-52` prompt design audit | 첫 입력 문구가 의도를 어떻게 조향하는지 | 조향 결과가 task-completion으로 이어졌는지 | 충돌 없음 |
| `marketing-49` post-result self-appropriation table | 결과 직후 자기화 vs 수동 감탄 | task-completion의 "다음 행동 선택" 열로 포함 | 충돌 없음 |
| first value mapping (J1/J2/J4 = `deed_saved`, J3 = `deed_judged`) | first value 기준 | task-completion 종료점으로 그대로 사용 | 충돌 없음 |

## 7. 해석 금지선

- `deed_judged` 단독으로 J1/J2/J4 task-completion을 확정하지 않는다.
- J3의 저장 없는 종료를 task-completion 실패로 읽지 않는다.
- `deed_save_capped`를 task-completion, value, upgrade demand로 읽지 않는다.
- task-completion 칼럼을 비율·activation rate·PMF·전환율로 환산하지 않는다.
- 신규 이벤트·속성·tracking/privacy·dashboard·session replay, 공개 카피, 외부 발송, 배포, 비용, 권한 변경은 모두 approval-needed다.

## 8. 검증 게이트

- 출처노트 경로: `source/external-links/marketing/2026-06-11-ai-onboarding-intent-to-task.md` — 파일 미존재 확인. 인박스 맥락(의도→작업완료 프레임)으로 대체.
- 기존 이벤트명 6개 확인: `add_flow_started`, `deed_judged`, `deed_saved`, `deed_rerolled`, `deed_save_capped`, `level_up_viewed` — 각 이벤트 선행 artifact에 존재 확인.
- conflict marker: 0건
- 공개 카피·이벤트·tracking/privacy·배포·외부발송·비용 변경: 0

## 9. 계승한 기준

- J1/J2/J4 first value = `deed_saved`, J3 first value = `deed_judged`.
- 첫 10명 관찰은 비율이 아니라 의도·완료·행동 언어로 읽는다.
- `deed_judged` 이벤트는 모든 잡에서 발화하지만 J3에서만 task-completion 종료점이다.

## 10. 이번에 새로 배운 것

- task-completion 3열(의도→AI 작업→다음 행동 선택)은 기존 4구간 감사표보다 더 짧고 직접적인 관찰 단위다. "AI가 결과를 냈다"(`deed_judged` 발화)와 "의도가 완료됐다"(task-completion)는 J1/J2/J4에서 다른 판단이다.
- `deed_judged` 과대평가는 J3 판독 기준을 J1/J2/J4에 그대로 적용할 때 발생한다. 3열 감사표는 잡별로 completion 종료점을 분리해 이 혼동을 줄인다.

## 11. 다음 Marketer에게 넘길 규칙

- 첫 세션 완료 판단은 `deed_judged` 발화 여부가 아니라 **잡별 task-completion 3열 일치**로 한다.
- J3의 무저장 종료를 보완하려는 넛지/카피를 제안하기 전에 먼저 이 표로 해당 사용자의 의도 열이 J3인지 확인한다.
- 이 표의 '다음 행동 선택' 칸은 기존 `post-result-self-appropriation-reading-table`과 동일 관찰을 공유한다. 두 번 기록하지 않는다.

## 12. MARKETING_LEARNINGS.md 승격 후보

Task completion is measured by intent-AI work-next action alignment, not by `deed_judged` alone. In Virtue, `deed_judged` firing signals AI work completed, but J1/J2/J4 task completion requires `deed_saved`; only J3 task completion ends at `deed_judged`. Treating `deed_judged` as universal completion causes J1/J2/J4 drop-off to be under-read and J3 normal closure to be over-flagged.
