# Virtue Launch-Ready PLG Signal Gate

Intent: marketing-59
Scope: L1 docs-only PLG signal gate for Virtue prelaunch first-10 observation.
Source note: `source/external-links/marketing/2026-06-14-plg-signal-hierarchy.md`
Prior artifacts: marketing-55, marketing-56, marketing-58

## Guardrails

- Preserve existing first-value mapping: J1/J2/J4 = `deed_saved`; J3 = `deed_judged`.
- No new events, tracking, privacy, dashboard, public copy, deploy, external message, or cost-bearing changes.
- PostHog is read-only future checklist; do not invent metrics or assume access.
- Prelaunch mode: observe and count, do not judge rates.

## PLG Signal Gate — Three Buckets

| Bucket | 신호 | Virtue 기준 | 행동 |
|---|---|---|---|
| **지금 볼 신호** | First Win | J1/J4: `deed_saved` 존재, J2: `deed_saved` + 연속 의도 확인, J3: `deed_judged` 존재 | 세션당 1개 체크 + 수기 노트 |
| **지금 볼 신호** | Activation event (기존 앵커) | 기존 이벤트 앵커 카운트: `deed_saved`, `deed_judged` | Count; rate는 판정 안 함 |
| **지금 볼 신호** | First win 품질 | Accepted output 여부 (marketing-56 컨럼) | 수기 노트: accepted/partially/rejected |
| **보류할 신호** | Engagement (session length, depth, page views) | 기록하되 판정 보류 | Track only; no judgment |
| **보류할 신호** | Return / second session | 기록하되 판정 보류 — prelaunch 시 attribution 불안정 | Track only; no retention rate |
| **보류할 신호** | Time to first value | 세션 내 qualitative 관찰만 | 수기 노트: before/at/after/not reached |
| **launch 이후 볼 신호** | PQL | 반복 행동 + 업그레이드 의도 신호 | Launch-after gate |
| **launch 이후 볼 신호** | Paid conversion rate | Pricing/plan 인프라 필요 | Launch-after gate |
| **launch 이후 볼 신호** | Retention / cohort | Stable acquisition + 100+ sessions | Launch-after gate |
| **launch 이후 볼 신호** | Viral coefficient | Tracking/공개 카피/privacy 결정 필요 | Launch-after gate |

## 지금 볼 신호 — 왜 이것만

Signal hierarchy 관점에서 prelaunch는 first win layer만 신뢰할 수 있다. 샘플이 작고, acquisition 체널이 안정되지 않았으며, 기준점이 없기 때문에 rate 기반 신호는 noise다.

Virtue prelaunch (first 10 users):
- 수치 판정 금지 (예: "activation rate 60%")
- 패턴 감지 가능 (예: "J3 사용자 3명이 모두 save 안 하고 나겔다")
- 개별 세션 first win은 관찰 가능

## Job별 신호 매핑 (기존 매핑 보존)

| Job | First Win 이벤트 | 지금 볼 신호 | 보류 | Launch-after |
|---|---|---|---|---|
| J1 기록형 | `deed_saved` | save 발생 + 수기 이유 | 재방문 여부, 연속 deed | PQL, retention |
| J2 누적형 | `deed_saved` | save 발생 + "다음에 추가하겠다" 의도 확인 | 2회차 deed 여부 | Expansion, streak |
| J3 AI 호기심형 | `deed_judged` | judgment 발생 + accept/reject 여부 | no-save 비율, reroll 비율 | PQL, conversion |
| J4 회고형 | `deed_saved` | save 발생 + reflection value 수기 | 재방문 후 참조 여부 | Expansion, viral |

## First-10 수기 Review Gate

Review gate: 10명 관찰 후 다음 세 질문에 답할 수 있어야 한다.

1. **First win gate**: 10명 중 몇 명이 job에 해당하는 first win 이벤트에 도달했는가? (count, not rate)
2. **Signal confusion gate**: 관찰 노트에서 acquisition 문제 / activation 문제 / measurement-too-early를 혼동한 기록이 있는가? 있으면 수정.
3. **Launch readiness gate**: 지금 볼 신호 중 패턴이 보이는 것이 있는가? 없으면 first win 계약이나 관찰 방법을 수정.

Rate를 계산하지 않는다. 비율을 사용한 결론은 sample 조건이 충족될 때까지 draft 상태로 표시한다.

## First-10 관찰 행 양식

기존 marketing-55/56/58 컨럼 통합:

| 컨럼 | 출체 | 내용 |
|---|---|---|
| job | marketing-55 | J1/J2/J3/J4 or unknown |
| first_win_event | marketing-55 | `deed_saved` or `deed_judged` or not_reached |
| count_now | marketing-55 | 기존 이벤트 앵커 카운트 |
| observe_manually | marketing-55 | 수기 노트: save/no-save 이유, curiosity 충족 여부 |
| accepted_output | marketing-56 | accepted / partially / rejected / unclear |
| useful_result_time | marketing-56 | before/at/after/not reached |
| retry_rejudge_reason | marketing-56 | 이유 수기 (curiosity/mismatch/mistrust 등) |
| reproducibility_understanding | marketing-56 | can explain / vague / cannot |
| screen_evidence | marketing-58 | first win을 확인한 화면 표면 |
| successful_output_sentence | marketing-58 | "사용자가 이제 갖게 된 것" 한 줄 |
| signal_bucket | marketing-59 신규 | 지금 볼 / 보류 / launch-after |
| confusion_flag | marketing-59 신규 | acquisition/activation/measurement-too-early 혼동 여부 |
| do_not_judge_yet | marketing-55 | PQL, conversion, retention, viral 판정 보류 |

## Verification

- Source note path: `source/external-links/marketing/2026-06-14-plg-signal-hierarchy.md`
- First-value mapping preserved: J1/J2/J4 = `deed_saved`; J3 = `deed_judged`.
- Prior artifacts compatibility: marketing-55 (count_now/observe_manually/do-not-judge), marketing-56 (4 reliable value columns), marketing-58 (screen evidence, successful output sentence) — no conflict.
- New events, tracking/privacy, dashboard, public copy, deploy, external message, cost: 0.
- Conflict markers: 0.
