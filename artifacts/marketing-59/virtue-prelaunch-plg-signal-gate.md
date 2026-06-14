# Virtue Launch-Ready PLG Signal Gate

Intent: marketing-59 | Created: 2026-06-14 | Permission: L1 docs-only

## 전제 (계승한 기준)

- J1/J2/J4 first value = `deed_saved` (m06, m20–m29, m55)
- J3 first value = `deed_judged` (m06, m55)
- Prelaunch = 첫 10명, 정성 관찰 모드, 숫자 판정 금지 (m08, m11, m14, m22, m55)
- Traffic source 분리 필수: 사람 실사용 / maker self-test / synthetic/mock (m25, m23)
- `deed_save_capped` = availability/friction, 업그레이드 수요 아님 (m21, m22, m23, m28, m29)
- J3 `deed_judged` 후 저장 없는 종료 = 정상 (m30, m31)
- PQL = 반복+재방문 묶음, 단일 이벤트 아님 (m41)

---

## PLG 신호 위계 표

| 신호 범주 | 지금 볼 신호 ✅ | 보류할 신호 ⏸ | Launch 이후 볼 신호 🔓 |
|-----------|--------------|-------------|-------------------|
| **First value** | J1/J2/J4: `deed_saved` 발화 여부 / J3: `deed_judged` 발화 여부 | TTV 수치 판정 | TTV 분포, 코호트 TTV |
| **Job 식별** | 첫 입력 출처와 잡 분류 (J1~J4) | 잡별 비율 판정 | 잡별 전환율 |
| **Traffic source** | 사람 실사용 / self-test / synthetic 분리 표시 | 트래픽 비율 판정 | 유입 채널 품질 |
| **Friction type** | B-LOST / B-MISMATCH / B-AVAIL / B-NORMAL 4분류 손기록 | 마찰률 % | A/B 마찰 비교 |
| **Post-response flow** | `deed_judged` 직후 30초 행동 손기록 | 저장률(J3) 판정 | post-response 코호트 |
| **Guided break point** | first_input / ai_wait / result_interpretation / save_or_exit 중 첫 끊김 | 구간별 이탈률 | 온보딩 funnel |
| **User language** | 자기 말로 설명한 가치 원문 기록 | 언어 패턴 수치화 | NPS / 인터뷰 |
| **D1/D7 return** | 재방문 여부 손기록 | D7 retention % | D30 retention 코호트 |
| **PQL candidate** | 반복 `deed_saved`/`deed_judged` + D7 재방문 묶음 *관찰* | PQL 임계값 확정 | PQL→conversion 상관 |
| **`deed_save_capped`** | availability/friction 분류 표시 | upgrade demand 판정 | — |
| **Monetization** | — | 가격/플랜 판단 | 업그레이드 수요 확인 후 |
| **Viral / expansion** | — | 공유율/추천율 판정 | viral coefficient 측정 |
| **Retention rate** | — | D7 retention % 합격선 | D7/D30 코호트 비교 |

---

## First-10 수기 Review Gate

세션 1개를 마감하기 전에 아래 7개 항목을 체크한다.

### 세션 체크리스트

1. **Traffic source 확인** — 이 사용자는 사람 실사용 / self-test / synthetic 중 무엇인가?
   - synthetic / self-test이면 review 대상에서 제외하고 별도 표시

2. **Job 식별** — J1 (기록·누적) / J2 (비교·성장) / J3 (AI 관점) / J4 (회고·아카이브) 중 무엇인가?
   - 첫 입력 출처로 판별

3. **First value 이벤트** — `deed_saved` (J1/J2/J4) 또는 `deed_judged` (J3) 발화 여부
   - 발화했으면 → 세션 "성공" 후보
   - 미발화면 → 종료 성격 분류로 이동

4. **Post-response flow 손기록** — `deed_judged` 직후 30초 내에 무엇을 했는가?
   - `deed_saved` / `deed_rerolled` / 무저장 종료 / `deed_save_capped` / 기타
   - J3 무저장 종료 = 정상 (보류/이탈 아님)

5. **Friction type 분류** — 막힘이 있었다면 무엇인가?
   - B-LOST: 길을 잃음 (입력 보조 후보)
   - B-MISMATCH: 결과 기대 불일치 (제품/약속 문제)
   - B-AVAIL: 가용성 차단 (availability/friction)
   - B-NORMAL: 정상 종료 (이탈 아님)

6. **Guided break point** — 세션의 첫 끊김은 어느 구간?
   - `first_input` / `ai_wait` / `result_interpretation` / `save_or_exit`

7. **User language 원문** — 사용자가 자기 말로 설명한 가치 (있으면 그대로 기록)
   - 이것이 없으면 수기 기록 미완성으로 간주

### Review 세션 종료 판단

7개 항목 모두 기록됐으면 세션 review 완료.

아래 중 하나라도 해당하면 판단 보류:
- traffic source 미확인
- job 미식별
- user language 미기록 (빈 칸 아닌 "기록 시도함" 표시 가능)

### 10개 세션 종료 후 리뷰

10명의 수기 기록이 모이면:
- **반복되는 B-LOST 패턴** → 입력 보조 넛지 후보 (proposal-only)
- **반복되는 user language 패턴** → 포지셔닝 언어 후보 (proposal-only)
- **J3 deed_judged 후 무저장 비율** → 정상 범위 확인 (판정 금지)
- **PQL 후보 묶음 관찰** → D7 재방문 + 반복 이벤트가 있는 세션 표시 (숫자 판정 금지)

이 단계에서 확정하지 않는 것: activation rate %, D7 retention %, PQL 임계값, upgrade demand 판정, channel quality, viral coefficient, monetization 신호.

---

## 충돌 확인

| 확인 항목 | 결과 |
|-----------|------|
| marketing-55 (Activation Measurement Contract) 충돌 | 없음 — "count now / observe manually / do not judge yet" 구분 계승 |
| marketing-56 (First Reliable Value Columns) 충돌 | 없음 — 4개 관찰 컬럼 위계표에 흡수 |
| marketing-58 (First Successful Output Contract) 충돌 | 없음 — post-response flow 계승 |
| 신규 이벤트 / tracking / privacy 변경 | 0 |
| 프로덕션 코드 변경 | 0 |
| 공개 카피 변경 | 0 |
| 배포 / 외부 메시지 / 비용 | 0 |
| conflict marker | 0 |

---

## 계승한 기준

- m55 (Virtue Prelaunch Activation Measurement Contract): "count now / observe manually / do not judge yet" 3구분
- m56 (First Reliable Value Columns): 4개 수기 관찰 컬럼
- m58 (First Successful Output Contract): 잡별 post-response 구간

## 이번에 새로 배운 것

- PLG 신호를 3층(지금/보류/launch후)으로 명시하면 prelaunch에서 measurement-too-early 오류를 줄일 수 있다.
- first-10 review gate를 7항목으로 고정하면 세션 마감 기준이 생긴다 (항목 미완성 = 미완성 세션).

## 다음 Marketer에게 넘길 규칙

- "지금 볼 신호" 표는 신규 이벤트를 추가하지 않고 기존 `deed_saved` / `deed_judged` / `deed_rerolled` / `deed_save_capped` 앵커만 쓴다.
- First-10 review gate 7항목은 수기 체크리스트로 남긴다. 자동화/대시보드/신규 속성은 approval-needed.
- PQL 묶음 관찰을 "확정"으로 전환하는 시점은 D7 재방문 데이터가 decision-grade 표본이 됐을 때다.
- J3 `deed_judged` 후 저장 없는 세션은 항상 "성공/정상"으로 분류한다.
