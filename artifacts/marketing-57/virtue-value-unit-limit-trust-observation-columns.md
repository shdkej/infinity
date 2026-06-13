# Virtue Value Unit And Limit Trust Observation Columns

Intent: marketing-57
Scope: L1 docs-only addition to the first-10 observation contract.
Source note: `source/external-links/marketing/2026-06-13-ai-pricing-trust-credits.md` at the Knowledge Lab root.
Lens: AI hybrid/credit/usage-gate 제품에서 cap은 수익화 이전에도 trust UX이며, 사용자가 가치 단위를 이해하는지와 제한을 공정하게 읽는지가 launch 이후 가격·제한 논의의 오판을 줄이는 핵심 관찰이다.

## Guardrails

- Preserve the existing first-value mapping: J1/J2/J4 = `deed_saved`; J3 = `deed_judged`.
- Keep this as a manual observation layer over the first 10 sessions, not product instrumentation.
- Do not add events, properties, timers, tracking, privacy flows, dashboards, session replay, public copy, deployment, external messages, pricing, caps, credit language, or cost changes.
- Treat value unit understanding and limit trust as prelaunch observation columns only — they are not launch-ready metrics or conversion gates.
- Do not convert these columns into upgrade signals, pricing thresholds, or paywall triggers.
- `deed_save_capped` is availability/friction, not a value or upgrade demand signal. Do not change cap policy based on these columns alone.

## What Changes

Add two concise manual columns beside the existing first-10 observation fields from marketing-54, marketing-55, and marketing-56.

| New manual column | Question to ask or observe | Allowed answer shape | Why it matters |
|---|---|---|---|
| 가치 단위 이해 (Value unit understanding) | 사용자가 세션에서 무엇을 "받았는지" 자기 말로 말할 수 있는가? AI 판정 1개, deed 저장 1개, 또는 다른 것? | 명확 (사용자가 구체적으로 설명) / 막연 (알긴 하는데 말 못 함) / 없음 (이해 못 함) / 미확인, 가능하면 사용자 원문 | 가치 단위 이해 없이 cap을 만나면 임의적으로 느껴진다. 첫 10명 관찰에서 수집해 launch 이후 cap 문구 조정의 근거로 삼는다. |
| 제한 신뢰 읽기 (Limit trust read) | cap·제한에 직접 또는 암묵적으로 마주쳤을 때 어떻게 읽는가? | 공정·명확 / 임의적 / 숨겨짐 / 미도달 (cap 없이 세션 종료) / 미확인, 사용자가 말한 것이 있으면 원문 | cap 프레이밍이 명확한지 숨겨졌는지를 launch 전에 파악해, "제한 문구를 급하게 바꾸지 말 것" 또는 "설명을 추가할 것" 방향을 잡는다. |

## Cap/Copy 해석 금지선 (Prelaunch)

다음은 first-10 관찰이 완료되기 *전*에 해서는 안 되는 것들이다.

| 금지 항목 | 금지 이유 |
|---|---|
| Copy에 숫자 cap 추가 (예: "하루 3회 무료") | 가치 단위 이해를 관찰하기 전에 cap 숫자를 명시하면 가치가 아니라 제한 인식으로 시작된다. |
| cap 경험을 희소성 인센티브로 프레이밍 | `deed_save_capped` 관찰을 upgrade demand로 읽기 전에 availability/friction 분류 먼저. [Availability And Friction Are Not Value] |
| "credit" / "billing" / "unlock" 언어 도입 | 사용자 value unit 멘탈모델이 없는 상태에서 결제 언어를 끼우면 신뢰 오보정 위험. |
| cap 정책 변경 (일일 한도 수치 조정) | first-10 관찰 데이터 없이 가정 willingness-to-pay로 cap 조정은 approval-needed. |
| 가치 단위 또는 제한 컬럼 결과를 conversion/upgrade signal로 전환 | 작은 표본 기반 단정 금지. [Prelaunch Decision Boundary] |

## Job-Specific Reading

| Job | 기존 first-value anchor | Value unit reading | Limit trust reading |
|---|---|---|---|
| J1 기록형 | `deed_saved` | "오늘 기록한 것 1개"가 가치 단위. 사용자가 "저장된 기록"을 받은 것으로 표현하는지 확인. | cap 경험 시 "오늘 기록은 다 했다"로 읽으면 공정, "갑자기 막혔다"면 임의적. |
| J2 누적형 | `deed_saved` | "누적할 수 있는 재료 1개"가 가치 단위. 사용자가 반복 가치를 기대하는지 확인. | cap이 누적 흐름을 끊었다고 느끼는지 확인. 누적이 단절되면 limit trust가 낮아진다. |
| J3 AI 호기심형 | `deed_judged` | "판정 카드 1개, 저장 없이도 값어치"가 가치 단위. 저장 없이 닫힘이 정상이므로 cap 도달 자체가 드물다. | cap 미도달이 정상. cap을 만났다면 맥락 확인 필요. |
| J4 회고형 | `deed_saved` | "회고 결과물 1개"가 가치 단위. 사용자가 저장한 반성을 "받은 것"으로 표현하는지 확인. | cap 경험 시 "오늘 회고는 끝났다"로 읽으면 공정, 회고 맥락에서 느닷없으면 임의적. |

## How To Use With Existing Notes

기존 관찰 노트 구조에서 marketing-56의 4컬럼 뒤에 이어서 사용한다.

| 기존 필드 | 추가 |
|---|---|
| Job (J1/J2/J3/J4 또는 unknown) | 유지 |
| Count now (deed_saved / deed_judged) | 유지 |
| Expected / Acquired / Blocked / Exit class | 유지 |
| Accepted output (marketing-56) | 유지 |
| Useful-result time (marketing-56) | 유지 |
| Retry or rejudge reason (marketing-56) | 유지 |
| Reproducibility understanding (marketing-56) | 유지 |
| **가치 단위 이해** | **신규 추가** — 명확 / 막연 / 없음 / 미확인 + 원문 |
| **제한 신뢰 읽기** | **신규 추가** — 공정·명확 / 임의적 / 숨겨짐 / 미도달 / 미확인 + 원문 |

## Interpretation Rules

- 가치 단위 이해 "명확"은 사용자가 구체적인 언어로 "무엇을 받았는지" 설명할 때만이다. "좋았다"는 명확이 아니다.
- 제한 신뢰 읽기는 cap에 *도달하지 않은* 세션에서는 "미도달"로 표시하고, 임의적/공정 판단을 하지 않는다.
- 두 컬럼은 서로 연결이 있다: 가치 단위 이해가 "없음"이면 제한 신뢰가 "임의적"이 될 가능성이 높다. 상관은 관찰 후보이지, prelaunch에서 결론이 아니다.
- 이 두 컬럼 결과를 upgrade demand, pricing 조정, 공개 카피 변경, cap 정책 변경으로 직접 전환하지 않는다. 모두 launch 이후 approval-needed.

## Compatibility Check

| 기존 산출물 | 호환성 |
|---|---|
| `artifacts/marketing-56/virtue-first-reliable-value-observation-columns.md` | 호환. marketing-56의 4컬럼(accepted output / useful-result time / retry-rejudge reason / reproducibility understanding) 뒤에 이어 붙인다. |
| `artifacts/marketing-55/virtue-prelaunch-activation-measurement-contract.md` | 호환. `count now` / `observe manually` / `do not judge yet` 경계 안에서 `observe manually` 섹션에 속한다. |
| `artifacts/marketing-54/virtue-first-10-expectation-outcome-blocker-loop-audit.md` | 호환. Expected/Acquired/Blocked 루프 뒤의 추가 관찰 레이어다. |
| MARKETING_LEARNINGS: Availability And Friction Are Not Value | 보완. `deed_save_capped`는 availability이며, 이 컬럼의 제한 신뢰 읽기가 "임의적"이라도 upgrade demand로 직접 전환하지 않는다. |
| MARKETING_LEARNINGS: No Autonomous Action Bounds The Trust Question | 보완. Virtue의 trust 질문은 "조언 vs 판결" 읽기이며, cap 경험은 이 trust 질문과 별도 레이어다. |
| MARKETING_LEARNINGS: Monetization Boundary | 보완. 이 컬럼은 first value 관찰 도구이고, monetization 판단은 launch 이후 gate에서만. |

## Verification

- Source note 경로 확인: `source/external-links/marketing/2026-06-13-ai-pricing-trust-credits.md` 생성됨.
- First-value mapping 유지: J1/J2/J4 = `deed_saved`; J3 = `deed_judged`.
- 신규 컬럼 포함: 가치 단위 이해, 제한 신뢰 읽기.
- Cap/copy 해석 금지선 5개 포함.
- 신규 이벤트, 속성, tracking/privacy, dashboard, public copy, deployment, external message, pricing, cap 정책, cost 변경: 0.
- 충돌 마커: 0.