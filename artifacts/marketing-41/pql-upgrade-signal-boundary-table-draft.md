# Virtue Post-Launch PQL/Upgrade 신호 경계표

> 문서 역할: 출시 후 첫 10명~첫 7일 데이터를 "PQL(Product-Qualified Lead)"과 "upgrade 수요"로 오독하지 않기 위한 내부 경계표.  
> Mixpanel PLG 2026 렌즈를 Virtue prelaunch/early 출시 맥락으로 번역한 docs-only 산출물이다.  
> 신규 이벤트·속성·카피·tracking/privacy·pricing·public/outbound·cost·deploy 변경 0.

---

## §0 계승한 기준

| 계승 항목 | 출처 | 요지 |
|-----------|------|------|
| First Value Mapping | `MARKETING_LEARNINGS.md`, `marketing-33` | J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106 재정의 0 |
| deed_save_capped 오독 금지 | `marketing-28`, `MARKETING_LEARNINGS.md §Availability And Friction Are Not Value` | `deed_save_capped`:167은 availability/friction 신호, monetization intent/upgrade demand 환산 금지 |
| A1~A4 activation 후보 묶음 | `marketing-33` `apps/web/docs/activation-candidate-registry.md` | 출시 후 PQL 비교 기준 묶음은 이 등록부를 변경 없이 참조한다 |
| Prelaunch Decision Boundary | `MARKETING_LEARNINGS.md` | 첫 10~20명, D7 이내 수치는 방향 판단 재료, PMF/conversion/upgrade 확정 금지 |
| Measurement Readiness Is A Separate Gate | `marketing-34`, `MARKETING_LEARNINGS.md` | PQL 임계값 계산은 측정 가능 상태가 먼저 |
| Correlation Readiness Is A Separate Gate | `marketing-37`, `MARKETING_LEARNINGS.md` | activation-retention 대조 준비가 PQL 판단보다 먼저 |
| Monetization Boundary | `marketing-28`, `MARKETING_LEARNINGS.md` | first value 이전 결제정보·계정강제·핵심행동 잠금·가격 확정 금지 |

---

## §1 PQL이란 무엇인가 (Mixpanel PLG 2026 렌즈)

PLG(Product-Led Growth) 맥락에서 PQL은 단일 클릭이나 단일 이벤트가 아니다.  
Mixpanel 2026 렌즈는 PQL을 다음 조건을 모두 만족하는 **행동 묶음(behavior bundle)**으로 정의한다:

1. **retention과 대조 가능하다** — activation 후보 묶음(A1~A4)이 D7 retention과 실제로 상관이 있는지 확인 가능한 표본·기간
2. **전환/upgrade 의도와 구분된다** — "많이 썼다"가 아니라 "가치를 반복 확인했다"
3. **임계값이 관찰 후 확정된다** — 출시 전 수치를 추정으로 만들지 않는다

**Virtue 적용 결론:**  
- Virtue는 현재 prelaunch다. PQL 임계값(n회 저장, n일 내 복귀 등)을 지금 만드는 단계가 아니다.
- 출시 후 첫 10명 또는 첫 7일 이후, activation 후보 묶음(A1~A4)이 D7 retention과 대조 가능한지 확인한다.
- 그 이전의 단일 이벤트 수치는 PQL 신호가 아니다.

---

## §2 PQL 후보 vs 비후보 신호 표

아래 표는 "이 신호가 PQL 또는 upgrade 의도를 나타내는가"를 사전 등록한다.  
출시 후 수치를 볼 때 이 표를 먼저 참조한다.

| 신호 | PQL/upgrade 후보 여부 | 이유 | 최소 조건 |
|------|-----------------------|------|----------|
| **A1** `deed_saved` + 다음 날 재방문 + `deed_saved` (W-CONF D7) | **후보** (조건부) | 반복 가치 관찰, activation 등록부 A1 기준 | 첫 10명 또는 D7 경과 후, 동일 잡 J1·J2·J4 |
| **A2** `level_up_viewed` + 이전 `deed_saved` 누적 | **후보** (조건부) | 누적 payoff 인식, J2 잡의 retention-predictive depth | 첫 10명 또는 D7 경과 후 |
| **A3** `deed_judged` (J3, 저장 없이) + D7 내 재방문 + 재판정 | **후보** (조건부) | J3는 `deed_judged`가 first value, 재방문·재판정이 depth 신호 | D7 경과 후, J3 잡 명확 |
| **A4** `deed_saved` (J4, 회고형) + D7 재방문 + 동일 잡 재저장 | **후보** (조건부) | J4 회고는 `deed_saved` 반복이 retention 신호 | D7 경과 후 |
| **단일 `deed_saved` 1회** | **비후보** | first value 도달 확인용, PQL 묶음 미완료 | — |
| **단일 `deed_judged` 1회** | **비후보** (J3 제외 잡에서) | J3 외에는 통과점, PQL 의도 증거 아님 | — |
| **`deed_save_capped` (상한 도달)** | **비후보** | availability/friction 신호. monetization intent 아님 (계승) | — |
| **`deed_rerolled` 1~3회** | **비후보** | curiosity/불신 판별 불가. 단독으로 PQL 의도 없음 | — |
| **`level_up_viewed` 1회만** | **비후보** | 누적 payoff 알아챔 1회. 반복·재방문 없으면 PQL 미달 | — |
| **`add_flow_started` 다수** | **비후보** | activity 신호. PQL은 activity가 아니라 acceptance/retention | — |
| **synthetic/mock/self-test 세션** | **비후보** | PQL 판단에서 반드시 제외 | — |
| **503/지연 세션** | **비후보** | availability 차단, friction 신호로만 분류 | — |

> **Waiting approval 신호** (아직 확정하지 않는 신호):
> - upgrade 실제 의향(결제정보 입력, 플랜 선택)
> - 사용자가 공유·추천 행동을 보인 경우 (off-instrument, 손기록 전용)
> - D30+ 복귀 (표본과 기간이 충분하지 않을 때까지 보류)

---

## §3 금지 오독 목록

출시 후 첫 10명·7일 데이터에서 다음 해석을 금지한다.

| 금지 오독 | 이유 |
|-----------|------|
| `deed_save_capped` = upgrade 수요 | availability/friction 신호. monetization intent 환산 금지 (계승) |
| 단일 이벤트 = PQL 달성 | PQL은 행동 묶음 + retention 대조 후 확정 |
| 첫 10명 수치 = 전환율/PQL 임계값 확정 | 소표본 방향 판단 재료, 확정 불가 |
| `deed_judged` - `deed_saved` 갭 = 이탈/upgrade 불필요 | J3는 저장 없는 정상 종료 가능, 갭 이탈 단정 금지 |
| `deed_rerolled` = upgrade 필요 신호 | 호기심·불신·학습 판별 불가. 단독으로 upgrade 의도 없음 |
| D7 재방문 1회 = 유료 전환 가능 | D7 재가치 확인 후보 등록용, 전환 결론 금지 |
| synthetic/mock 포함 집계 = PQL 수치 | 반드시 제외 |
| 가용성 차단 세션 = 이탈/churn | availability 분리 후 재분류 |
| PQL 임계값 추정·확정 | 출시 후 관찰 전 임계값 만들지 않는다 |
| 유료화 후보 구현·배포 | approval-needed |

---

## §4 Virtue prelaunch → post-launch 전환 게이트

PQL 판단을 시작하려면 아래 게이트를 먼저 통과해야 한다.

| 게이트 | 확인 항목 | 상태 |
|--------|-----------|------|
| G1 | first value 매핑 확인 (J1/J2/J4=`deed_saved`, J3=`deed_judged`) | ✅ 계승 완료 |
| G2 | activation 후보 묶음 A1~A4 사전 등록 (`activation-candidate-registry.md`) | ✅ marketing-33 완료 |
| G3 | synthetic/mock/self-test 제외 기준 확립 (`traffic-source-reading-boundary-table.md`) | ✅ marketing-25 완료 |
| G4 | availability/friction 분리 (`deed_save_capped`, 503, 지연) | ✅ marketing-28, MARKETING_LEARNINGS.md |
| G5 | first 10명 또는 7일 경과 | ⏳ 출시 후 확인 |
| G6 | D7 retention 대조를 위한 activation 이벤트 도착 확인 | ⏳ 출시 후 확인 |
| G7 | PQL 임계값 논의 승인 | ⏳ approval-needed |

G5/G6 통과 전에는 다음을 하지 않는다:
- PQL 임계값 수치 확정
- upgrade 후보 trigger 구현
- 전환/upgrade 광고·메시지 발송

---

## §5 prelaunch 금지선 요약

- 신규 이벤트·속성·카피·tracking/privacy·pricing·public/outbound·cost·deploy 변경 0
- PQL 임계값 추정·확정 금지 (출시 후 관찰 전)
- `deed_save_capped` = upgrade 수요 환산 금지
- 단일 이벤트 PQL 판단 금지
- 첫 10명 데이터로 전환율/retention% 확정 금지
- synthetic/mock/self-test 세션 PQL 집계 포함 금지
- 유료화 후보 구현 → approval-needed

---

## §6 이번에 새로 배운 것 / 다음 Marketer에게 넘길 규칙

**계승한 기준:**
- First Value Mapping (J1/J2/J4=`deed_saved`, J3=`deed_judged`) — 재정의 0
- `deed_save_capped` = availability/friction, upgrade 환산 금지
- A1~A4 묶음은 `activation-candidate-registry.md` 기준 변경 없이 상속

**이번에 새로 배운 것:**
- Mixpanel PLG 2026 렌즈에서 PQL은 retention과 대조 가능한 행동 묶음이다.
- Virtue prelaunch는 PQL 임계값을 만들 단계가 아니다. "출시 후 첫 10명 또는 첫 7일 이후 대조할 후보"로만 남긴다.
- `deed_save_capped` 오독 금지는 PQL/upgrade 판단에서도 동일하게 계승된다.

**다음 Marketer에게 넘길 규칙:**
- PQL 판단 전 §4 게이트 G5/G6 먼저 확인한다.
- 단일 이벤트·소표본으로 PQL 달성을 선언하지 않는다.
- `deed_save_capped`는 언제나 availability/friction 신호로 먼저 분류한다.

**MARKETING_LEARNINGS.md 승격 후보:**  
"PQL Is A Bundle, Not A Click — Threshold After Retention Contrast"  
→ 단일 실행이라 report 안에 보류. 출시 후 실사용 대조 후 승격 여부 결정.
