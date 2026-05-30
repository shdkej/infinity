# Virtue AI Outcome Proxy Dictionary

> AI가 생성한 결과(판정·점수·수준)를 사용자가 어떻게 받아들이는지를 **proxy 신호**로 읽는 내부 경계표.
> Intercom outcome-based AI value framing + Reforge North Star quality 렌즈 기반.
> 신규 이벤트·속성·코드·계측 변경 없이 기존 6개 발화 이벤트만 사용.

## §1 핵심 전제

| 전제 | 내용 |
|------|------|
| activity ≠ outcome | `add_flow_started`는 의도 신호, `deed_saved`는 인정 가치 신호. 둘은 proxy 강도가 다르다. |
| AI outcome = 사용자 인정 | AI가 좋은 판정을 냈더라도 사용자가 저장/행동하지 않으면 "가치 전달"로 보지 않는다. |
| availability ≠ value | `deed_save_capped` early-return, 503, 판정 지연은 가치 신호에서 제외한다. |
| J3는 다르다 | J3의 first value는 `deed_judged`이므로 `deed_saved` 없이 종료해도 정상 outcome이다. |
| proxy type은 고정 레이블 | 하나의 이벤트는 잡·조건에 따라 proxy type이 달라질 수 있다. 단일 이벤트에 단일 proxy를 고정하지 않는다. |

### Proxy Type 정의

| proxy type | 의미 |
|-----------|------|
| `activity` | 사용자가 특정 행동을 했다는 것만 알 수 있음. 결과 수용 여부 불명. |
| `acceptance` | 사용자가 AI 결과를 인정·수용했음을 나타냄. |
| `curiosity` | AI 결과에 대한 추가 탐색 의사를 나타냄. |
| `friction` | 진행을 방해하는 장벽 또는 availability 문제. |
| `retention` | 재방문·반복 행동을 나타냄. |

## §2 Proxy Dictionary (핵심 표)

### J1 기록형 — 덕행을 기록하고 싶다
**First value**: `deed_saved` (:183)

| 이벤트 | proxy type | quality condition | misread warning |
|--------|-----------|------------------|-----------------|
| `add_flow_started` | activity | 반복 발화(D7+)로 intent 신호 강화 | 이탈 직전에도 발화됨 → 시작 = 가치 아님 |
| `deed_judged` | activity | J1에서는 `deed_saved`로 가는 중간 단계 | J1에서 `deed_judged`만 있고 `deed_saved` 없으면 이탈 후보 (J3와 다름) |
| `deed_saved` | acceptance | **J1 first value.** 기록 의도의 완성 | `deed_save_capped` early-return은 `deed_saved` 미발화 → acceptance 아닌 friction |
| `deed_rerolled` | curiosity | AI 결과에 이견 또는 재확인 의사. 최대 3회 (:149) | 재요청 횟수 자체를 불만족으로 단정 금지. 탐색일 수 있음 |
| `level_up_viewed` | retention | J1 누적 payoff 알아챔. 반복 기록의 보상 확인 | 조건부 발화 → 특정 레벨 달성 시만 발화, 세션당 1회만 계산 |
| `deed_save_capped` | friction | 30덕 상한 early-return. 저장 의도 있었으나 차단됨 | **monetization intent·upgrade demand로 환산 금지.** availability/friction 신호 |

### J2 누적형 — 시간에 걸쳐 덕행을 쌓고 싶다
**First value**: `deed_saved` (:183)

| 이벤트 | proxy type | quality condition | misread warning |
|--------|-----------|------------------|-----------------|
| `add_flow_started` | activity | D7+ 반복 발화 시 retention intent 신호 | 단발 발화는 방문 이상의 의미 없음 |
| `deed_judged` | activity | 저장 전 단계. J2에서는 중간 경유점 | `deed_judged`만 반복되고 `deed_saved`가 없으면 누적 의지 약화 신호 (J3와 구별) |
| `deed_saved` | acceptance | **J2 first + retention value.** 반복 저장이 누적 payoff | 1회 `deed_saved`로 J2 리텐션 확보 단정 금지 |
| `deed_rerolled` | curiosity | AI 공정성·일관성 확인 의도 가능 | 재요청 = 불만족 단정 금지 |
| `level_up_viewed` | retention | **J2에게 가장 직접적인 누적 payoff 확인 이벤트** | 발화 안 했다고 J2 payoff 없다고 단정 금지. 레벨 조건 미충족일 수 있음 |
| `deed_save_capped` | friction | J2 누적 흐름 차단. `deed_saved` 미발화 → 누적 카운트 누락 | "이번 달 행동 완료" 신호로 읽지 않는다. availability 차단임 |

### J3 AI 호기심형 — AI가 내 행동을 어떻게 판정하는지 보고 싶다
**First value**: `deed_judged` (:106) — 저장 전 정상 종료

| 이벤트 | proxy type | quality condition | misread warning |
|--------|-----------|------------------|-----------------|
| `add_flow_started` | activity | J3 탐색 시작. 입력 부담이 낮아야 도달 | `add_flow_started` 후 이탈은 J3 초입 마찰 신호 |
| `deed_judged` | acceptance | **J3 first value. 판정 결과가 곧 outcome. 저장 없이 종료해도 정상 완료** | judged−saved 갭을 J3 이탈로 해석 금지. J3 정상 종료 = `deed_judged` 후 `deed_saved` 없음 |
| `deed_saved` | retention | J3에서 `deed_saved`는 first value 이후 추가 행동. 탐색 → 보관 전환 신호 | J3에서 `deed_saved` 없다고 가치 미전달로 단정 금지 |
| `deed_rerolled` | curiosity | **J3에서 가장 직접적인 AI 탐색 행동.** 판정 결과에 대한 재탐색 | 재요청 ≤3회는 정상 탐색. 불만족 단정 금지 |
| `level_up_viewed` | retention | J3에게는 보조 신호. 저장 선행 없이 레벨 조건 충족 어려움 | J3는 저장 없이 종료할 수 있으므로 `level_up_viewed` 기대 금지 |
| `deed_save_capped` | friction | J3에서 드물게 발화. 탐색 후 저장 시도 시 차단 | availability 차단. J3 first value는 이미 `deed_judged`에서 충족됨 |

### J4 회고형 — 과거 덕행을 되돌아보며 패턴을 확인하고 싶다
**First value**: `deed_saved` (:183)

| 이벤트 | proxy type | quality condition | misread warning |
|--------|-----------|------------------|-----------------|
| `add_flow_started` | activity | J4에게는 회고 재료를 쌓는 의미. "꾸준히"가 J4 질 신호 | 빈도 자체보다 시간에 걸친 지속성이 J4 지표 |
| `deed_judged` | activity | J4에서는 저장 전 단계 | J4에서 `deed_judged`만 있으면 J1과 동일하게 이탈 후보 |
| `deed_saved` | acceptance | **J4 first value.** 회고 재료 축적의 기반 | 단발 `deed_saved`보다 D30+ 지속 발화가 J4 quality 조건 |
| `deed_rerolled` | curiosity | J4에게는 드문 신호. AI 판정 교정 의도 가능 | J4에서 재요청이 잦으면 판정 신뢰 의심 신호이지 탐색 아님 |
| `level_up_viewed` | retention | J4 장기 누적 payoff 확인. 환생종 변화 포함 | 조건부 발화. 달성 조건 미충족 시 발화 안 됨. 부재가 J4 이탈 단정 근거 아님 |
| `deed_save_capped` | friction | J4에서 30덕 상한은 회고 재료 부족 우려 가능 신호 | monetization demand로 환산 금지. 상한 조정 가설은 반복 관찰 후 proposal-only |

## §3 잡 × 이벤트 × Proxy Type 요약 매트릭스

> 이 표는 §2 상세 표의 요약이다. 판독 시 §2 quality condition과 misread warning을 반드시 함께 확인한다.

| 이벤트 | J1 기록형 | J2 누적형 | J3 AI 호기심형 | J4 회고형 |
|--------|----------|----------|--------------|----------|
| `add_flow_started` | activity | activity | activity | activity |
| `deed_judged` | activity | activity | **acceptance** | activity |
| `deed_saved` | **acceptance** | **acceptance** | retention | **acceptance** |
| `deed_rerolled` | curiosity | curiosity | **curiosity** | curiosity |
| `level_up_viewed` | retention | **retention** | retention | **retention** |
| `deed_save_capped` | friction | friction | friction | friction |

*굵게 표시된 칸 = 해당 잡에서 가장 신호 강도가 높은 proxy.*

## §4 금지선 (Misread Prevention)

1. `deed_judged` 단독을 J1/J2/J4 outcome 도달로 읽지 않는다.
2. `deed_judged` → `deed_saved` 갭을 J3에서 이탈로 읽지 않는다 (J3 정상 종료).
3. `deed_save_capped`를 monetization intent·upgrade demand·pricing proxy로 읽지 않는다.
4. `add_flow_started` 단독을 activation outcome으로 읽지 않는다.
5. proxy type `activity`를 `acceptance`로 검증 없이 승격하지 않는다. quality condition 충족 확인 후에만 승격.
6. 작은/synthetic 수치를 proxy 패턴으로 읽지 않는다. 트래픽 분류(human/self-test/synthetic)를 먼저.
7. 기존 first-value 매핑을 재정의하지 않는다: J1/J2/J4=`deed_saved`, J3=`deed_judged`.
8. availability 차단(`deed_save_capped` early-return, 503, 판정 지연)을 quality·outcome proxy로 읽지 않는다.

## §5 이벤트 앵커 참조

| 이벤트 | 코드 앵커 | proxy 역할 요약 |
|--------|----------|-----------------|
| `add_flow_started` | :72 | activity / intent signal (모든 잡) |
| `deed_judged` | :106 | J3 acceptance / J1·J2·J4 activity |
| `deed_rerolled` | :149 | curiosity (≤3회, 모든 잡) |
| `deed_save_capped` | :167 | friction / availability (모든 잡) |
| `deed_saved` | :183 | J1·J2·J4 acceptance (first value) / J3 retention |
| `level_up_viewed` | :199 | retention / payoff signal (J2 최강, 조건부) |

## §6 선행 문서 연결

| 문서 | 연결 지점 |
|------|----------|
| `first-session-jtbd-matrix.md` | J1~J4 잡 정의 + first value 매핑의 원천. 재정의 없음. |
| `ai-judgment-trust-calibration-audit.md` | J3 신뢰 보정: 판정 결과 수용 = acceptance proxy의 신뢰 조건 |
| `onboarding-metrics-reading-table.md` | TTV / drop-off / D7 retention = proxy 강도 시간축 |
| `traffic-source-reading-boundary-table.md` | synthetic/mock/self-test 제외 근거. proxy 판독 전 선행 분류 |
| `add-input-output-balance-audit.md` | `/add` 단계별 activity vs acceptance 강도 분포 |
| `prelaunch-monetization-boundary-brief.md` | `deed_save_capped` = friction이지 monetization proxy 아님 확인 |

## §7 prelaunch 해석 금지선

- 이벤트 1회 발화를 proxy 패턴 결론으로 읽지 않는다.
- 전환율·리텐션·PMF·% 수치를 이 표에서 산출하지 않는다.
- synthetic/mock/self-test 발화를 사람 proxy 신호에 포함하지 않는다.
- 신규 이벤트·속성·코드·계측·카피·대시보드·세션리플레이·배포·외부발송·비용·시크릿·권한·개인정보 변경 0.
