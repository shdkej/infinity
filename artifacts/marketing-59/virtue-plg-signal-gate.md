# Virtue Launch-Ready PLG Signal Gate

> artifact for: marketing-59
> created: 2026-06-14
> permission: L1 docs-only — 이 문서는 내부 관찰 가이드이며 신규 이벤트, tracking/privacy, dashboard, public copy, deploy, external outreach, cost-bearing action을 포함하지 않는다.

## 목적

Virtue prelaunch에서 acquisition 문제, activation 문제, measurement-too-early 상태를 첫 10명 관찰에서 혼동하지 않게 한다.
기존 J1/J2/J4=`deed_saved`, J3=`deed_judged` 매핑은 그대로 유지한다.

---

## 3열 신호 게이트 표

### 지금 볼 신호 (Prelaunch Now — First-10 수기 관찰)

이 신호들은 *지금 이 단계에서 읽을 수 있다*. 단, 비율/rate로 환산하지 않는다.

| 신호 | 잡별 기준 | 주의 |
|---|---|---|
| **First value 도달** | J1/J2/J4: `deed_saved` 발화 / J3: `deed_judged` 발화 | 발화 여부만. 비율 환산 금지 |
| **트래픽 분류** | human 실사용 / self-test / synthetic / mock 분리 | 분리 전 어떤 신호도 읽지 않는다 |
| **가용성 차단** | `deed_save_capped`, 503, 지연 | availability/friction 기록 — value/upgrade demand 아님 |
| **사용자 언어 원문** | 사용자가 자기 말로 설명한 가치 (원문 그대로) | 작은 표본 하나로 positioning 확정 금지 |
| **결정-위임 인지** | AI를 판결("AI가 결정")로 읽는가 vs 관점("AI가 정리, 내 선택")으로 읽는가 | 개수로 집계하지 않음 |
| **guided break 위치** | first_input / ai_wait / result_interpretation / save_or_exit 중 첫 끊김 | 끊김 성격 추가 분류 필요 |
| **post-response 흐름** | 결과 카드 직후 30초 행동 (손기록) | `deed_judged` 발화 ≠ 이해/수용 확정 |
| **B-분류** | B-LOST(길 잃음) / B-MISMATCH(기대 불일치) / B-AVAIL(가용성 차단) / B-NORMAL(정상 종료) | J3 무저장 종료는 B-NORMAL |

**축약 읽기 순서:**
1. 이 사용자가 human 실사용인가? → 아니면 제외
2. 트래픽 분류 먼저 → 그 다음 신호
3. first value 이벤트 발화했는가?
4. 가용성 차단이 있었는가?
5. 사용자 언어 원문
6. 결정-위임 인지
7. guided break + B-분류

---

### 보류할 신호 (Hold — Until Sufficient Signal)

이 신호들은 *지금 읽으면 오독한다*. 충분한 표본과 조건 전까지 보류한다.

| 신호 | 왜 보류하는가 |
|---|---|
| **Activation rate %** | 표본 부족, 대조군 없음 (비율 환산 금지) |
| **D7 / D30 retention 비율** | 단일 코호트, 신호 잡음 너무 큼 |
| **PMF 40% 수치** | 실사용자 40명+ 필요 |
| **PQL 단일 이벤트 환산** | `deed_save_capped` 1회 = upgrade demand가 아님 |
| **judged-saved 갭 → 이탈** | J3 정상 종료(무저장)를 churn으로 읽지 않는다 |
| **D1/D3/D7 미방문 → churn** | first value 전/후 segmentation 전에 단정 금지 |
| **외부 PLG 벤치마크 복사** | TTV<5분, D7 N%, activation 40% 등 복사 금지 |
| **`deed_rerolled` → 불신** | 의도 관찰 전 보류 |
| **PostHog dashboard 값** | 측정 가능 상태 확인 전 값 읽기 보류 |

---

### Launch 이후 볼 신호 (Post-Launch — With Real Data)

이 신호들은 *충분한 실사용자와 반복 행동이 쌓인 뒤*에 읽는다.

| 신호 | 조건 |
|---|---|
| **PQL 확정** | 반복 `deed_saved`/`deed_judged` + D7 재방문 묶음 (단일 이벤트 아님) |
| **Activation vs D7 retention 대조** | Correlation readiness 확인 후 (사전 등록 쿼리 모양 필요) |
| **재활성화 후보 분류** | RC-WARM / RC-PRE-LOST / RC-NORMAL / RC-AVAIL / RC-EXCLUDED 분리 |
| **채널 품질 / viral coefficient** | 충분한 볼륨 후 |
| **Monetization 신호** | PQL 확정 → 반복 가치 관찰 → 유료화 신호 (이 순서 유지) |
| **Dashboard / tracking 구성** | approval-needed |
| **공개 카피 / 발송 전략** | approval-needed |
| **PostHog 실제 쿼리 실행** | decision-grade 표본 + 접근 권한 + 사전 등록 쿼리 모양 |

---

## First-10 수기 Review Gate

첫 10명 관찰 시 각 사용자마다 아래 체크리스트를 완료한 뒤에만 종합 판단을 시도한다.
모든 항목이 체크되지 않았으면 activation rate / PMF / churn 결론을 내지 않는다.

```
사용자: ___________  날짜: ___________  잡(J1/J2/J3/J4): ___________

□ Human 실사용인가?
  - 아니면 → [제외] 이유: _______
  - 맞으면 → 계속

□ 트래픽 분류 완료?
  - 분류: human / self-test / synthetic / mock → ___________

□ First value 이벤트 발화?
  - J1/J2/J4: deed_saved □  |  J3: deed_judged □
  - 미발화 → 종료 성격: B-LOST □  B-MISMATCH □  B-AVAIL □  B-NORMAL □

□ 가용성 차단 있었나?
  - deed_save_capped □  503 □  지연 □  없음 □
  - 차단 기록: ___________

□ 사용자 언어 원문 기록?
  - 원문: "___________"

□ 결정-위임 인지 기록?
  - 판결로 읽음 □  관점으로 읽음 □  불명확 □
  - 메모: ___________

□ Guided break 위치?
  - first_input □  ai_wait □  result_interpretation □  save_or_exit □  없음 □

□ B-분류 표시?
  - B-LOST □  B-MISMATCH □  B-AVAIL □  B-NORMAL □

→ 모든 체크 완료 전에 비율·PMF·retention·PQL 결론 없음
→ 완료 후에도 결과를 rate/% 로 환산하지 않음 — 패턴 언어와 분류로만 읽음
```

---

## 선행 기준 계승

| 계승한 기준 | 출처 |
|---|---|
| J1/J2/J4=`deed_saved`, J3=`deed_judged` | marketing-55, marketing-06~29 |
| `deed_save_capped` = availability/friction, not value | marketing-21~29 |
| Prelaunch는 비율 결론 금지 | marketing-08, 11, 22, 23 |
| 트래픽 분류 먼저 | marketing-25, 23, 11 |
| PQL은 단일 이벤트 아님 | marketing-41 |
| J3 무저장 종료 = B-NORMAL | marketing-42, 29 |
| Measurement readiness ≠ measurement value | marketing-34, 33 |

## 이번에 새로 배운 것

없음 — 이 artifact는 기존 기준의 통합 응용이다.

## 다음 Marketer에게 넘길 규칙

1. First-10 관찰에서 "지금/보류/launch-after" 3열을 먼저 확인하고 신호를 배치한다.
2. 보류열에 있는 신호는 표본이 충분해지더라도 Correlation readiness 확인 없이 읽지 않는다.
3. 게이트 표는 도구이고 기준선이 아니다 — 수치 임계값을 이 표에서 가져오지 않는다.
