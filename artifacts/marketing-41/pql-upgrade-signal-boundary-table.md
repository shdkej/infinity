# Virtue post-launch PQL/upgrade 신호 경계표

> 출시 후 early monetization 판단을 위한 행동 묶음 후보 + 단일 이벤트 오독 금지 경계표.  
> PQL 임계값·conversion rate·upgrade demand를 산출하지 않는다. "첫 10명·7일 이후 대조할 후보"로만 남긴다.

선행 문서: `activation-candidate-registry.md`(m33) · `plg-foundation-exit-gate.md`(m34) · `activation-retention-correlation-readiness.md`(m37) · `prelaunch-monetization-boundary-brief.md`(m28) · `MARKETING_LEARNINGS.md`

---

## §0 문서 위치와 사용 규칙

이 문서는 Infinity marketing-41의 산출물이며 virtue-rebirth-app `apps/web/docs/`에 위치한다.

**읽는 순서:**
1. m33 `activation-candidate-registry.md` → A1~A4 등록부 원장
2. m28 `prelaunch-monetization-boundary-brief.md` → `deed_save_capped` 경계
3. 이 문서 → PQL/upgrade 신호 후보 분류

**사용 규칙:**
- 새 monetization·PQL 판단 작업 전에 이 문서의 §3 심장 표를 먼저 대조한다.
- PQL 임계값·conversion rate·upgrade demand는 이 문서에서 산출하지 않는다.
- §5의 게이트 조건(첫 10명 OR 7일)을 충족하기 전까지 PQL-C1~C3는 후보이지 결론이 아니다.

---

## §1 PQL 정의와 Virtue 적용 원칙

**PLG PQL 정의:**  
PQL(Product Qualified Lead) = first/second value에 도달해 upgrade/conversion 준비가 됐다고 판단할 수 있는 행동 묶음을 보인 사용자.

**Virtue 4원칙:**
1. **단일 이벤트 1개로 PQL 판정하지 않는다.** 행동 묶음이 먼저다.
2. **A1~A4 activation 후보 묶음 완료가 PQL 후보 탐색의 시작점이다.** 묶음 미완료 세션은 PQL 후보로 집계하지 않는다.
3. **`deed_save_capped`는 PQL 신호가 아니라 availability/friction 신호다.** m28·MARKETING_LEARNINGS.md 계승.
4. **PQL 임계값(전환율·upgrade demand 수치)은 출시 후 충분 표본과 사용자 명시 승인 없이 확정하지 않는다.**

---

## §2 A1~A4 activation 후보 묶음 요약 (m33 계승, 재정의 0)

| 등록 ID | 잡 | first value | 후보 묶음 | 관찰 window |
|---------|---|------------|----------|------------|
| A1 | J1 기록형 | `deed_saved`:183 | `add_flow_started`:72 → `deed_saved`:183 | W-IMM (첫 세션) |
| A2 | J2 누적형 | `deed_saved`:183 | `deed_saved` ×2 이상 OR `deed_saved` + `level_up_viewed`:199 | W-CONF (D7) |
| A3 | J3 AI 호기심형 | `deed_judged`:106 | `deed_judged` (저장 불요 — 묶음 완료 조건 = `deed_judged` 발화) | W-IMM (첫 세션) |
| A4 | J4 회고형 | `deed_saved`:183 | `deed_saved` + session gap >1일 후 재방문 | W-CONF (D7) |

- `deed_save_capped`:167은 위 묶음에 포함하지 않는다.
- A3에서 `deed_saved` 없는 종료는 J3 정상 종료다 — 미완료·이탈로 집계하지 않는다.

---

## §3 PQL 신호 후보 표 (심장 표)

> **PQL 후보** = 행동 묶음이 high-intent를 시사, 첫 10명·7일 이후 대조 대상  
> **PQL 비후보** = 단일 이벤트 또는 availability/friction — PQL 판단에 사용 금지  
> **Waiting Approval** = 사용자 명시 승인이 있어야만 실행 가능  

| 묶음 ID | 행동 증거 조합 | 잡 | Window | PQL 분류 | 오독 위험 | 승인 조건 |
|---------|-------------|---|--------|---------|---------|----------|
| PQL-C1 | A1 완료 + D7 재방문 + A2 이상 진행 (재방문 저장 확인) | J1/J2/J4 | W-CONF (D7) | **PQL 후보** | 재방문이 habit이 아닌 one-off일 수 있음 | 첫 10명 OR 7일 이후 대조 |
| PQL-C2 | `deed_saved` ×3 이상 (distinct session, 같은 잡 범주) | J1/J2/J4 | D14 이후 | **PQL 후보** | 저장 횟수≠가치 밀도, 잡 혼재 가능 | 출시 후 충분 표본 확보 시 |
| PQL-C3 | A3 완료 + D7 재방문 + `deed_judged` 재발화 (같은/다른 deed) | J3 | W-CONF (D7) | **PQL 후보** | `deed_rerolled` 단독은 고의도 단정 불가 | 출시 후 7일 이후 |
| PQL-N1 | `deed_save_capped` 단독 (×1 이상) | J1/J2/J4 | any | **PQL 비후보** | availability/friction 신호 — upgrade demand×, m28 계승 | N/A |
| PQL-N2 | `deed_rerolled` 단독 (×1~3) | J3 | any | **PQL 비후보** | 호기심/탐색 신호 — upgrade intent 단정 불가 | N/A |
| PQL-N3 | `level_up_viewed` 단독 (×1) | J2 | any | **PQL 비후보** | 누적 payoff 인지≠upgrade 결정 | N/A |
| PQL-W1 | PQL 후보 사용자 대상 upgrade prompt 노출 (push/in-app) | any | any | **Waiting Approval** | 공개 action — 미승인 발송 금지 | 사용자 명시 승인 |
| PQL-W2 | conversion rate / upgrade demand 수치 산출 및 공개 | any | any | **Waiting Approval** | 작은 표본 과대해석 — prelaunch 금지 | 충분 표본 + 사용자 명시 승인 |
| PQL-W3 | paywall / 플랜 / 가격 노출 (UI 또는 공개 카피) | any | any | **Waiting Approval** | monetization boundary(m28) | 사용자 명시 승인 |

---

## §4 단일 이벤트 오독 금지

> 아래 이벤트들은 단독으로 PQL/upgrade demand/high-intent 신호로 읽지 않는다.

| 이벤트 | 앵커 | 실제 의미 | PQL 오독 방지 |
|--------|------|---------|---------------|
| `deed_save_capped` | :167 | 30덕 저장 상한 early-return, `deed_saved` 미발화 | availability/friction — PQL 후보 포함 금지, upgrade demand 환산 금지 |
| `deed_rerolled` | :149 | 재시도 (호기심/탐색, 최대 3회) | upgrade 욕구·불신으로 단정 금지. 묶음(A3+D7재방문) 없으면 PQL 비후보 |
| `level_up_viewed` | :199 | 누적 payoff 화면 도달 (J2 W-CONF 신호) | 단독 ×1 = 유료 전환 의도로 환산 금지. A2 묶음 완료 후에만 PQL 후보 맥락에서 참조 |
| `deed_judged` (J3, save 없음) | :106 | J3 first value, 저장 없는 종료 = 정상 | 미충족/이탈로 읽지 않음. PQL-N 비후보와 별도 취급 |

---

## §5 출시 후 첫 10명 / 7일 대조 게이트

> PQL 임계값 산출 금지. 아래 조건을 충족한 뒤에만 "PQL 후보 대조"를 시작한다.

**게이트 발동 조건 (첫 10명 OR 7일 실경과):**
- 트래픽 분류 선행 (m25 계승): A 사람 실사용 / B 메이커 self-test / C synthetic/mock → B·C 제외 후 A만 집계
- m37의 제외 조건: X-MOCK · X-SYNTH · X-SELF · X-CAP(`deed_save_capped`) · X-503(가용성 차단)

**대조 항목 (후보, 결론 아님):**
1. PQL-C1 후보 사용자 수 (A1+D7재방문 묶음 완료, raw count만)
2. PQL-C1 중 D7 재방문 확인 여부 (손기록)
3. A1~A4 묶음 완료율 (분모=A 트래픽 세션, 분자=각 묶음 완료 세션)

**게이트 이후에도 여전히 금지:**
- PQL 임계값 확정 (전환율·N명이면 PQL 판정)
- conversion rate / upgrade demand 수치 공개
- 수치를 근거로 한 공개 action (PQL-W1~W3 여전히 Waiting Approval)

---

## §6 prelaunch 금지선

- PQL 임계값·conversion rate·upgrade demand·pricing 결정 0
- 공개 upgrade prompt·paywall·플랜·가격 노출 → PQL-W1~W3 (Waiting Approval)
- `deed_save_capped` = upgrade demand 환산 금지 — m28·MARKETING_LEARNINGS.md 계승
- `deed_rerolled`·`level_up_viewed` 단독 = PQL 신호 집계 금지
- 신규 이벤트·속성·카피·tracking/privacy·pricing·public/outbound·cost·deploy 변경 0
- first value 매핑 재정의 0: J1/J2/J4=`deed_saved`, J3=`deed_judged`
- conflict marker 0 · 코드 diff 0

---

## §7 계승 / 변경 / 충돌 분리

| 항목 | 분류 | 선행 출처 |
|------|------|----------|
| J1/J2/J4 first value=`deed_saved`, J3=`deed_judged` | 계승 | m06, m33, MARKETING_LEARNINGS.md |
| A1~A4 activation 묶음·W-IMM·W-CONF | 계승 | m33 |
| `deed_save_capped`=availability/friction (upgrade demand ×) | 계승 | m28, m34, MARKETING_LEARNINGS.md |
| Prelaunch Decision Boundary | 계승 | m08, m11, m22, m23, MARKETING_LEARNINGS.md |
| Correlation Readiness Is A Separate Gate | 계승 | m37 |
| Monetization Boundary (first value 이전 결제/잠금 금지) | 계승 | m28 |
| PQL 후보 3종(PQL-C1~C3) 사전 등록 | 신규 (m33 activation 묶음 확장) | 본 문서 |
| PQL 비후보 3종(PQL-N1~N3) 명시 | 신규 | 본 문서 |
| PQL Waiting Approval 3종(PQL-W1~W3) 분류 | 신규 | 본 문서 |
| 변경 | 없음 | — |
| 충돌 | 0 | — |
