# Virtue PLG Foundation Exit Gate

> 출시 전 Foundation 단계가 완료되었음을 선언하는 기준표.  
> "개선하기 전에 측정 가능 상태를 먼저 잠근다."

---

## §0 이 문서의 위치

이 문서는 Virtue prelaunch 운영 문서 체계 안에서 **Foundation exit gate** 역할을 한다.

| 문서 | 역할 |
|------|------|
| `activation-candidate-registry.md` | 잡별 activation 후보 묶음(A1~A4)과 관찰 window(W-IMM/W-CONF) 등록 |
| `time-to-value-observation-brief.md` | J1~J4 TTV 정의 (start→end) |
| `retention-predictive-activation-brief.md` | D7 second value 정의와 depth signal |
| `first-real-user-baseline-template.md` | 첫 10~20명 한 명당 한 행 관찰 양식 |
| `traffic-source-reading-boundary-table.md` | 트래픽 출처(A~E) 분류 |
| `onboarding-metrics-reading-table.md` | 활성화·TTV·drop-off·D7 통합 판독표 |
| **이 문서** | 위 모든 준비가 완료되었는지 확인하는 **exit gate 체크리스트** |

Foundation exit gate 체크리스트를 통과해야 **Activation 단계**(실제 첫 사용자 관찰 + 결과 판독)로 넘어간다.

---

## §1 Foundation 단계란

PLG Foundation 단계의 목표는 **측정 가능 상태 달성**이다. 개선이 아니라 "측정 가능한가"를 확인하는 단계다.

Virtue prelaunch 맥락에서 Foundation은 다음 세 질문이 모두 답해진 상태를 의미한다.

1. **Activation bundle 등록**: 잡별로 어떤 이벤트 묶음을 activation으로 볼 것인지 미리 잠궜는가?
2. **D7 second value 정의**: 첫 7일 안에 두 번째 가치가 무엇인지 잡별로 정의했는가?
3. **Source promise fit 기준**: 유입 출처와 제품 약속이 일치하는지 판별하는 기준이 있는가?

이 세 가지가 잠기지 않은 상태에서 첫 사용자 데이터를 읽으면, 작은 표본을 사후에 입맛대로 해석하는 위험이 생긴다.

---

## §2 Exit Gate 체크리스트 (심장표)

### 게이트 1 — Activation Bundle 등록 확인

> 참조: `activation-candidate-registry.md` §2 등록부 심장표

| 항목 | 확인 | 비고 |
|------|------|------|
| A1 (J1 기록형) 등록 완료 | □ | `deed_saved`:183 중심 묶음 |
| A2 (J2 누적형) 등록 완료 | □ | `deed_saved`:183 + `level_up_viewed`:199 |
| A3 (J3 AI 호기심형) 등록 완료 | □ | `deed_judged`:106 — 저장 없이 닫힘=정상 |
| A4 (J4 회고형) 등록 완료 | □ | `deed_saved`:183 중심 묶음 |
| W-IMM (첫 세션 window) 정의 완료 | □ | |
| W-CONF (D7 window) 정의 완료 | □ | |
| 등록 후보를 사후에 변경하지 않을 것 확인 | □ | |

### 게이트 2 — D7 Second Value 정의 확인

> 참조: `retention-predictive-activation-brief.md` §3 D7 재가치 질문

| 항목 | 확인 | 비고 |
|------|------|------|
| D7 재가치 질문 5선 확인 | □ | D0 first value / D7 return / D7 second value evidence / same-job continuity / source promise fit |
| J1~J4별 second value 이벤트 후보 확인 | □ | 반복 `deed_saved`, `level_up_viewed`:199, `deed_rerolled`:149 |
| D7 외부 벤치마크를 Virtue 합격선으로 쓰지 않을 것 확인 | □ | 비율·% 산출 금지 |
| `deed_save_capped`:167 early-return은 TTV 종료·재가치 집계 제외 | □ | availability/friction 신호 |

### 게이트 3 — Source Promise Fit 기준 확인

> 참조: `traffic-source-reading-boundary-table.md` §2 트래픽 출처 분류

| 항목 | 확인 | 비고 |
|------|------|------|
| A 사람 실사용 / B 메이커 self-test / C synthetic·mock 분류 기준 확인 | □ | |
| B·C 트래픽은 baseline에서 표시 후 제외 | □ | 삭제 아님 |
| 유입 출처를 분류하기 전에 activation 칸을 읽지 않을 것 확인 | □ | 분류 선행 원칙 |
| D 플랫폼 차이(web/iOS)는 별도 분리 | □ | `ios-activation-event-parity-brief.md` 참조 |

### 게이트 4 — 관찰 양식 준비 확인

> 참조: `first-real-user-baseline-template.md`, `first-60-second-value-observation-script.md`

| 항목 | 확인 | 비고 |
|------|------|------|
| 첫 10~20명 baseline 양식 준비 | □ | 한 명당 한 행 |
| 60초 관찰 스크립트 준비 | □ | 수기 기록용 |
| J별 관찰 질문 사전 확인 | □ | |
| 신규 계측·이벤트·대시보드 없이 기존 6개 이벤트로만 관찰 | □ | add_flow_started/deed_judged/deed_saved/level_up_viewed/deed_rerolled/deed_save_capped |

---

## §3 세 축을 함께 읽는 방법

Foundation 완료 선언 후 첫 사용자 데이터를 읽을 때, **세 축을 분리해서 읽고 합산하지 않는다.**

| 축 | 읽는 것 | 읽지 않는 것 |
|----|---------|-------------|
| Activation bundle | 등록된 A1~A4 후보 중 어느 묶음에서 first value가 닫혔는가 | 전환율·% |
| D7 second value | 7일 안에 same-job 재방문과 두 번째 first value 이벤트가 있는가 (정성) | D7 retention% / 벤치마크 대조 |
| Source promise fit | 유입 출처의 약속과 첫 세션에서 실제로 닿은 가치가 같은 잡인가 | PMF 선언 |

**합산 규칙:** 세 축이 모두 같은 방향을 가리킬 때만 "이 잡에서 Foundation이 작동한다"고 메모한다. 하나라도 불분명하면 판단을 보류한다.

---

## §4 Foundation 완료 선언 조건

다음 조건이 모두 충족될 때 Foundation이 완료된 것으로 선언한다.

1. §2의 게이트 1~4 체크리스트 항목이 모두 체크됨
2. 첫 실사용자가 아직 없거나 10명 미만인 상태에서 체크리스트를 통과했음 (사후 잠금 아님)
3. 선행 문서와 이 체크리스트 사이에 conflict marker 없음

**Foundation 완료 = Activation 단계 시작 허가.** 이 선언 후에야 §3의 세 축으로 실제 데이터를 판독할 수 있다.

---

## §5 Activation 단계 이행

Foundation 완료 선언 후:

1. **관찰 시작**: 첫 실사용자 등장 시 baseline 한 행 기입
2. **10명 OR 7일 gate**: 10명 도달 또는 7일 경과 시 `activation-candidate-registry.md` §4의 등록 후보 대조 체크리스트 실행
3. **source promise fit 판독**: 유입 출처를 먼저 분류(A/B/C/D)한 뒤 A 트래픽만 판독
4. **보류**: 10명 미만이거나 7일 미경과 시 집계·비율·전환율 산출 금지

---

## §6 Prelaunch 금지선

- 게이트 통과 전 activation rate·전환율·retention%·PMF 결론 산출 금지
- 외부 벤치마크 수치를 Virtue Foundation exit gate 합격선으로 쓰지 않음
- 10명 미만 OR 7일 미경과 시 집계 금지
- J3 `deed_judged` 후 `deed_saved` 없는 세션을 "이탈"로 단정 금지 (J3 정상 종료)
- `deed_save_capped`:167 early-return을 activation 성공·실패로 읽지 않음 (availability 신호)
- synthetic/mock 세션을 Foundation 체크리스트에 포함하지 않음
- 이 문서에서 신규 이벤트·속성·카피·계측·대시보드·코드·배포·외부발송·비용·시크릿·권한·개인정보 변경 0

---

## §7 참조 문서 (기존 문서만 인용, 신규 정의 0)

| 문서 | 역할 |
|------|------|
| `activation-candidate-registry.md` | A1~A4 등록부, W-IMM/W-CONF window |
| `time-to-value-observation-brief.md` | J1~J4 TTV 정의 |
| `retention-predictive-activation-brief.md` | D7 second value, depth signal |
| `first-real-user-baseline-template.md` | 첫 10~20명 관찰 양식 |
| `traffic-source-reading-boundary-table.md` | 트래픽 출처 분류(A~E) |
| `onboarding-metrics-reading-table.md` | 활성화·TTV·drop-off·D7 판독표 |
| `first-60-second-value-observation-script.md` | 60초 관찰 현장 대본 |
| `ios-activation-event-parity-brief.md` | iOS 이벤트 패리티 |
| `first-session-jtbd-matrix.md` | J1~J4 JTBD 매트릭스 (first value 매핑 계승) |

First value 매핑 계승: J1/J2/J4 = `deed_saved`:183, J3 = `deed_judged`:106. 재정의 0.
