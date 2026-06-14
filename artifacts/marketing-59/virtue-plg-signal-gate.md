# Virtue Launch-Ready PLG Signal Gate

Intent: marketing-59  
Scope: L1 docs-only. No new events, tracking/privacy, production code, public copy, or cost-bearing changes.  
Source note: `source/external-links/marketing/2026-06-14-plg-signal-hierarchy.md`  
Prior contracts: marketing-55 (activation), marketing-56 (observation columns), marketing-58 (first successful output)

## Preserved Mappings

- J1/J2/J4: first value = `deed_saved`
- J3: first value = `deed_judged` (no-save completion is normal)
- Do not judge yet: PQL, paid conversion, expansion, viral coefficient, external benchmarks

## Signal Gate Table

| 신호 | 분류 | 이유 |
|---|---|---|
| **J1/J2/J4: `deed_saved` 발화** | ✅ 지금 볼 신호 | first win anchor (marketing-55 계승) |
| **J3: `deed_judged` 발화** | ✅ 지금 볼 신호 | first win anchor (marketing-55 계승) |
| 잡별 first value 도달 여부 (수기) | ✅ 지금 볼 신호 | 기존 계약의 핵심 관찰 레이어 |
| 첫 세션 진입 경로 (invited / organic / self) | ✅ 지금 볼 신호 | traffic source 분류 목적, 신규 tracking 없음 |
| `deed_rerolled` 재시도 | ✅ 지금 볼 신호 | 의도 관찰 후보 — 결론은 금지, 보류 레이블 없음 |
| `deed_save_capped` | ⚠️ 보류할 신호 | availability/friction 신호. value·upgrade demand·PQL 아님 (marketing-41, marketing-29 계승) |
| Signup 수 / page view | ⚠️ 보류할 신호 | PLG vanity metric. 활성화 여부와 무관. 성과로 읽지 않는다 |
| D7 재방문율 (%) | ⚠️ 보류할 신호 | prelaunch 표본에서 rate 환산 금지. 재방문 여부만 수기 관찰 |
| 외부 벤치마크 (D7 N%, activation 40%) | ⚠️ 보류할 신호 | prelaunch 합격선으로 복사 금지 (marketing-34, marketing-22 계승) |
| **PQL (반복 `deed_saved/judged` + D7 재방문 묶음)** | 🕐 launch 이후 볼 신호 | 충분 표본 + 반복 + 재방문 묶음 필요 (marketing-41 계승) |
| Paid conversion 의도 | 🕐 launch 이후 볼 신호 | 가격/플랜 결정 별도 승인 필요 (marketing-28 계승) |
| Expansion (팀/가족/워크플로우 확산) | 🕐 launch 이후 볼 신호 | account/context 근거 필요 |
| Viral coefficient | 🕐 launch 이후 볼 신호 | tracking/referral/privacy 결정 필요 |
| PostHog 대시보드 수치 | 🕐 launch 이후 볼 신호 | project ID/접근권한 없음. 지금은 read-only 체크리스트로만 |

## First-10 수기 Review Gate

아래 순서로 체크한 후 신호를 읽는다. 순서를 건너뛰면 신호 오독이 발생한다.

| 순서 | 체크 항목 | 판단 규칙 |
|---|---|---|
| 1 | 실제 사용자인가? | synthetic/mock/self-test/maker 세션은 제외·표시한다 |
| 2 | 어떤 잡으로 진입했나? | J1/J2/J3/J4 또는 unknown. unknown이면 first-value label 부여 금지 |
| 3 | first-value 이벤트가 발화했나? | J1/J2/J4 → `deed_saved` 발화? / J3 → `deed_judged` 발화? |
| 4 | 미발화면 종료 성격은? | J3 no-save = 정상 종료(성공). `deed_save_capped` = 마찰. B-LOST = 보류 |
| 5 | `deed_save_capped` · 503 · 지연인가? | availability/friction으로 분류. PQL/value/upgrade demand로 읽지 않는다 |
| 6 | 신호를 rate·% · PQL · 전환율로 환산하려는가? | prelaunch에서는 rate 환산 금지. 수기 관찰과 분류만 남긴다 |

## 계승한 기준

- First Value Mapping (marketing-55): J1/J2/J4=`deed_saved`, J3=`deed_judged`
- PQL Is A Bundle, Not A Single Event (marketing-41): 단일 이벤트로 PQL 확정 금지
- Measurement Readiness Is A Separate Gate (marketing-34): 측정 가능 상태와 측정값 성패는 별개

## 이번에 새로 배운 것

- PLG 신호 위계(signup→first win→PQL→conversion→expansion→viral)를 Virtue prelaunch 3열 게이트로 번역하면, first win만 '지금' 레이어로 내려오고 나머지는 모두 launch 이후 또는 보류다.
- signup/page view는 PLG 분류에서도 vanity metric이다 — activation과는 다른 레이어.
- `deed_rerolled`는 의도 관찰 후보이지만 결론 금지이므로 '지금 볼 신호'에 포함할 수 있다.

## 다음 작업에 넘길 규칙

- Virtue에서 PLG 다음 레이어(PQL/conversion)를 논의할 때 이 게이트를 기준으로 시작한다.
- 새 신호 분류 후보가 생기면 먼저 3열 중 어디에 해당하는지 체크한다.
- 신규 이벤트·tracking/privacy·대시보드·public copy·pricing·deploy·external message는 여전히 approval-needed.

## Verification Gate

- [x] Source note exists: `source/external-links/marketing/2026-06-14-plg-signal-hierarchy.md`
- [x] marketing-55/56/58 매핑 계승: J1/J2/J4=`deed_saved`, J3=`deed_judged`
- [x] PQL·conversion·expansion·viral = launch 이후 분류 확인
- [x] 신규 이벤트·tracking/privacy·production code·public copy·cost 변경: 0
- [x] conflict marker: 0

## Continuation

No new intent needed. This is a docs-only observation clarification layer.  
Any product telemetry, PostHog dashboard, public copy, tracking/privacy, pricing, cap, or deployment change remains approval-gated.
