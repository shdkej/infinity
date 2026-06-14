# Virtue Prelaunch PLG Signal Gate

Created: 2026-06-14
Intent: marketing-59
Permission: L1 docs-only
Inherits: J1/J2/J4=`deed_saved`, J3=`deed_judged` (marketing-55, marketing-06)
Source note: source/external-links/marketing/2026-06-14-plg-signal-hierarchy.md

## Verification (First Gate)

- Source note exists: ✓ `source/external-links/marketing/2026-06-14-plg-signal-hierarchy.md`
- marketing-55 conflict: 0 (activation measurement contract preserved)
- marketing-56 conflict: 0 (first reliable value observation columns preserved)
- marketing-58 conflict: 0 (first successful output contract preserved)
- Conflict markers in this file: 0
- Production code/tracking/privacy changes: 0

---

## PLG Signal Gate — 3열 표

### 지금 볼 신호 (Watch Now — Prelaunch Safe)

이 신호는 < 10명 사용자로도 손기록 관찰이 가능하다.

| 신호 | 읽는 법 | 잡 주의사항 |
|------|--------|----------|
| `deed_judged` fires | J3: first value 도달. J1/J2/J4: 통과점 (저장 전) | J3에서는 이것만으로 세션 성공 |
| `deed_saved` fires | J1/J2/J4: first value 도달 | J3에서 저장 없이 닫힘은 정상 종료 — 이탈 아님 |
| 결과 직후 30초 행동 | 저장 / 재시도 / 닫기 / 읽기 → B-분류 | 손기록만. 계측 임계값 아님 |
| B-LOST (길 잃음) | `/add` 후 `deed_judged` 없이 이탈 — 입력 보조 후보 | synthetic/mock/self-test 먼저 제외 |
| B-MISMATCH (기대 불일치) | 결과 카드 후 즉시 이탈 + "이게 아닌데" 언어 | 제품 약속/결과 문제 — 넛지로 가리지 않음 |
| B-AVAIL (가용성/마찰) | `deed_save_capped`, 503, 지연, 반복 실패 | upgrade demand 아님. 가용성 문제로만 분류 |
| B-NORMAL (정상 종료) | J3 `deed_judged` 후 무저장 닫힘 | 이탈 아님 |
| 사용자 자기 말 | 첫 세션 후 "이게 뭐야" / "어, 맞는데?" / 보여 주기 | 원문 그대로 손기록. 전환율 환산 금지 |
| 첫 입력 출처 | placeholder가 어떤 잡을 불렀는가 | 잡별 두 번째 행동과 대조 |
| TTV (first-win까지 시간) | 정성 타이밍 — "빠르다/느리다" 느낌 | 계측 임계값 설정 금지 |

### 보류할 신호 (Hold — Too Early)

정의는 해두되 평가하지 않는다. 비율/통과율 환산 금지.

| 보류 신호 | 이유 |
|----------|------|
| Activation rate (%) | 표본 너무 작음 |
| D7 재방문율 | D7 데이터 없음 |
| D30 리텐션 | D7 먼저 확인 |
| PMF survey 40% | 외부 벤치마크. Virtue 기준 아님 |
| PQL 후보 집합 | 반복 first-win + D7 재방문 묶음 없음 |
| `deed_save_capped` 빈도 | 가용성/마찰 신호. upgrade demand 아님 |
| Channel quality (CAC, k-factor) | acquisition 숫자 없음 |
| Viral coefficient | N/A at prelaunch |
| judged−saved 갭 (J3 제외) | J1/J2/J4는 보류 후보. J3는 정상 |
| 세션당 이벤트 수 | click volume ≠ value |

### Launch 이후 볼 신호 (Post-Launch Gate)

열리는 조건: 20+ 실사용자(non-synthetic), D7 데이터 경과.

| 신호 | 열리는 조건 |
|------|----------|
| Activation rate 기준선 | 20+ 실사용자, synthetic/mock/self-test 제외 완료 |
| D7 재방문율 | 첫 코호트 D7 경과 후 |
| PQL 후보 — RC-WARM 집합 | first value 도달 + D7 재방문 묶음 확인 후 |
| 묶음 완료 vs 미완료 retention 대조 | D7 데이터 + 사전 등록 pseudo-query shape 준비 후 |
| `deed_save_capped` → 회복 경로 | 반복 출현 + 가용성 분류 완료 후 |
| Upgrade/conversion 신호 | PQL 후보 집합 식별 후 (proposal-only 단계) |
| Channel quality 비교 | 복수 채널 실사용자 50+ 이후 |

---

## First-10 수기 Review Gate

### 사용 방법

첫 10명 실사용자 세션(synthetic/mock/self-test 제외)마다 아래 칸을 손기록한다.
계측 이벤트가 아니라 관찰 보조 용도다. 어떤 칸도 비율/통과율/KPI로 환산하지 않는다.

### Review Gate 표

| # | 날짜 | Job | First Win 도달 | First Win 이벤트 | B-분류 | 결과 후 행동 (30s) | 사용자 자기 말 (원문) | TTV 느낌 | 다음 행동 | 비고 |
|---|------|-----|---------------|----------------|--------|-------------------|--------------------|----------|----------|------|
| 1 |      |     | Y / N         |                |        |                   |                    |          |          |      |
| 2 |      |     | Y / N         |                |        |                   |                    |          |          |      |
| 3 |      |     | Y / N         |                |        |                   |                    |          |          |      |
| 4 |      |     | Y / N         |                |        |                   |                    |          |          |      |
| 5 |      |     | Y / N         |                |        |                   |                    |          |          |      |
| 6 |      |     | Y / N         |                |        |                   |                    |          |          |      |
| 7 |      |     | Y / N         |                |        |                   |                    |          |          |      |
| 8 |      |     | Y / N         |                |        |                   |                    |          |          |      |
| 9 |      |     | Y / N         |                |        |                   |                    |          |          |      |
| 10|      |     | Y / N         |                |        |                   |                    |          |          |      |

### 칸 설명

| 칸 | 의미 | 계측 주의 |
|----|------|----------|
| Job | J1(오늘 한 일), J2(누적/레벨), J3(AI 판정), J4(태그/검색) | 사용자 행동으로 추론 |
| First Win 도달 | J1/J2/J4=`deed_saved`, J3=`deed_judged` 발화 여부 | Y/N만. 비율 환산 금지 |
| B-분류 | B-LOST / B-MISMATCH / B-AVAIL / B-NORMAL | 미발화 세션만 분류 |
| 결과 후 행동 | `deed_judged` 직후 30초. 저장/닫기/재시도/읽기 | 30초는 계측 임계값 아님 |
| 사용자 자기 말 | 제품을 설명한 문장 그대로 | 해석 첨가 금지 |
| TTV 느낌 | 빠름/느림/적절 주관적 평가 | 계측값이 아님 |

### B-분류 규칙

```
deed_judged 없이 이탈 → synthetic/mock/self-test? → Y: EXCLUDED
                       → N: B-AVAIL(cap/503/지연)? → Y: B-AVAIL
                                                   → N: B-LOST(길 잃음)
deed_judged 후 이탈 → J3? → Y: B-NORMAL (정상 종료)
                   → 즉각 이탈 + "이게 아닌데"? → B-MISMATCH
                   → 나머지 → B-NORMAL 후보 (보류)
```

---

## 마케팅 학습 메모

### 계승한 기준

- J1/J2/J4=`deed_saved`, J3=`deed_judged` first value mapping (marketing-55, marketing-06)
- Prelaunch Decision Boundary: 비율 환산 금지, 방향 판단 재료만 (marketing-23, marketing-22)
- Measurement Readiness Is A Separate Gate: 정의 가능 ≠ 비율 판단 가능 (marketing-34)
- PQL Is A Bundle, Not A Single Event: D7 재방문 묶음 필요 (marketing-41)
- Availability And Friction Are Not Value: deed_save_capped = 가용성/마찰 (marketing-29)
- Session Value Is Read By Job, Not Event Count (marketing-42)
- Post-Response Flow Reveals Value (marketing-44)

### 이번에 새로 배운 것

- PLG Foundation→Activation→Conversion 3단계를 Virtue prelaunch 3열 표로 번역.
- B-LOST/B-MISMATCH/B-AVAIL/B-NORMAL 네 분류를 first-10 review gate에 명시적 칸으로 올림.
- "보류할 신호" 목록을 한 곳에 모아두면 다음 Heartbeat에서 보류 근거를 재질문하지 않아도 됨.

### 다음 작업에 넘길 규칙

- Launch 이후 신호 게이트 열리는 조건(20+ 실사용자, D7 경과)을 다음 activation/PQL 작업 시 먼저 확인.
- 신규 이벤트/tracking/privacy/dashboard/public copy/deploy/cost: 모두 approval-needed.
- first-10 review gate 표는 손기록 보조 용도. 계측 이벤트나 PostHog 속성으로 추진 금지.

### Durable Learning Candidate

**PLG Signal Tiers Map To Prelaunch Gates, Not Prelaunch Scores**
결론: PLG의 Foundation→Activation→Conversion 세 단계는 "지금 볼/보류/launch 이후" 세 열로 prelaunch에 번역된다. Activation은 정의(매핑) 단계가 완료됐고 측정(비율) 단계는 launch 이후다. PQL과 Conversion은 D7 재방문 데이터가 없으면 열 수 없다.
출처: marketing-59, marketing-34, marketing-41, marketing-55
