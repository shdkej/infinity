# Virtue Human-AI Readiness Trace Map

> 내부 문서. 신규 이벤트·속성·PostHog 대시보드·tracking/privacy·카피·배포·외부 발송·비용 변경 금지.
> cloud prepare 초안 — 로컬 Claude Code가 선행 문서 대조 후 virtue-rebirth-app/apps/web/docs/에 저장.

---

## §0 목적과 경계

### 왜 이 문서가 필요한가

인간-AI 제품 평가는 모델 정확도보다 **outcome / reliance / safety / learning** 상호작용 흔적으로 봐야 한다. Virtue prelaunch 첫 10명 관찰에서 `deed_saved`, `deed_judged`, `deed_rerolled`, 미저장 종료를 "AI를 믿었다/믿지 않았다"로 단정하는 대신, 이 4종 행동 이벤트를 **readiness trace**로 분리해 읽는 기준이 필요하다.

readiness trace는 판정이 아니라 분류다. 사용자가 AI와 어떻게 상호작용할 준비가 되어 있는지를 행동의 흔적으로 관찰하고 기록하는 것이다.

### 이 문서가 다루지 않는 것

- 전환율, activation rate, retention%, PMF 판정 → 별도 Intent
- 신규 이벤트·속성·PostHog 설정 변경 → 계측 금지
- AI 모델 정확도·점수 해석 → 제품 범위 밖
- 신규 카피·공개 외부 발송 → 금지선
- readiness trace를 "좋다/나쁘다"로 단정하는 것

### 참조 선행 문서 (충돌 0 원칙)

이 문서는 아래 선행 문서의 결론을 재정의하지 않고 확장 렌즈로 사용한다.

- `ai-judgment-trust-control-observation-boundary-table.md` — J1~J4 AI 판정 제어/신뢰 관찰 경계 (m38)
- `activation-candidate-registry.md` — A1~A4 활성화 후보 묶음 (m33)
- `first-real-user-baseline-template.md` — 첫 실사용자 기록 양식 (m11)
- `ai-judgment-trust-calibration-audit.md` — 신뢰 보정 감사표 (m24)
- `first-session-jtbd-matrix.md` — J1~J4 잡별 first value 매핑 (m06)

출처 노트 (`2026-06-04-human-ai-readiness-traces.md`)는 로컬 부재 → rationale 요지만 근거로 사용. 로컬 실행 시 선행 문서와 대조 필수.

---

## §1 4축 Readiness Trace 정의

인간-AI 제품의 "준비도(readiness)"는 사용자가 AI와 어떻게 상호작용하는지의 **흔적(trace)**으로 관찰한다. Virtue에서 이 4축은 기존 이벤트만으로 부분 관찰이 가능하다.

| 축 | 정의 | Virtue 흔적 이벤트 | 오독 경계 |
|----|------|-----------------|----------|
| **Outcome** | 사용자가 AI 판정 결과를 자신의 목표와 연결지어 완료했는가 | `deed_saved`:183 발화 | deed_saved = AI 판정 동의로 단정 금지. 기록/누적/회고 의도로 저장 가능 |
| **Reliance** | AI 판정에 어느 정도 의존했는가. 전적 수용 vs 검토 후 수용 vs 재시도 | `deed_rerolled`:149 발화 (최대 3회) | reroll = 불신으로 단정 금지. AI를 검증하는 calibrated reliance 행동일 수 있음 |
| **Safety** | AI 판정을 수용하기 전에 결과를 검토했는가. 사람이 마지막 선택을 했는가 | `deed_judged`:106 이후 사람이 저장/무시/재시도 중 선택 | J3 미저장 = safety 실패가 아닌 정상 종료. judged−saved 갭 이탈 단정 금지 |
| **Learning** | 반복 사용에서 AI와의 상호작용 패턴이 변화했는가 | D7 내 `deed_rerolled`/`deed_saved` 비율 변화, `level_up_viewed`:199 | prelaunch 소표본에서 Learning 패턴 결론 금지. 손기록 전용. D7 이후만 의미 있음 |

### 핵심 경계: `deed_saved` ≠ AI 판정 동의

`deed_saved`:183 발화는 AI 판정에 동의했다는 신호가 아니다. 다음 이유 중 하나일 수 있다:

- 덕행을 기록하고 싶었다 (J1 기록형 — 판정 점수와 무관하게 저장)
- 누적 payoff를 원했다 (J2 누적형 — `level_up_viewed`:199 연결)
- 회고 기반 판단이 필요했다 (J4 회고형 — 판정 동의 여부와 별개)
- AI 판정 내용과 무관하게 저장 흐름을 완료했다

반대로 `deed_saved` 없이 종료해도 AI 판정을 수용하지 않은 것이 아니다:

- J3 잡에서는 `deed_judged`:106 발화 = first value 도달, 저장은 선택
- 이것이 J3 "judged-without-save 정상 종료 경계"다 (§4에서 상세 설명)

---

## §2 U-C-I 관찰 질문

U-C-I는 단일 세션 내 관찰 흐름을 구조화하는 3단계 질문 틀이다. 이 세 질문은 readiness trace 4축 관찰을 실제 현장에서 적용하기 위한 실용 도구다.

- **U (Understand — 이해)** — 사용자가 AI 판정을 조언/참고로 이해했는가, 아니면 명령/자동 결과로 수용했는가
- **C (Control — 제어)** — 사용자가 최종 선택(저장/무시/재시도)을 자신이 했다고 행동으로 보였는가
- **I (Iterate — 반복)** — 사용자가 AI 결과를 바탕으로 행동을 반복하거나 조정했는가

### J1~J4 × U-C-I 관찰 질문 표

| 잡 | First Value | U 관찰 질문 | C 관찰 질문 | I 관찰 질문 |
|----|------------|------------|------------|------------|
| **J1 기록형** | `deed_saved`:183 | 판정 점수를 보고 저장했는가, 점수 무관하게 저장했는가? | 저장 의사 결정을 사용자가 직접 했는가? | 저장 후 덕행 기록을 다음 날에도 반복했는가? |
| **J2 누적형** | `deed_saved`:183 | 누적 payoff(레벨업)를 인지하고 저장했는가? | 저장 횟수/타이밍을 사용자가 조절하는가? | `level_up_viewed`:199 발화 여부, D7 두 번째 저장 여부 |
| **J3 AI 호기심형** | `deed_judged`:106 | 판정 결과를 "AI의 의견"으로 읽었는가, 아니면 정답으로 받아들였는가? | 저장 없이 결과만 보고 자신의 판단으로 닫았는가? (정상 종료 확인) | 다른 입력으로 재판정(`deed_rerolled`:149, 최대 3회)했는가? |
| **J4 회고형** | `deed_saved`:183 | AI 판정이 회고의 근거로 활용됐는가? | 판정에 동의하지 않아도 기록 목적으로 저장했는가? | 이전 저장 결과와 비교하는 행동이 있었는가? |

**관찰 방법**: 이벤트 발화 시퀀스를 순서대로 손기록한다. 기존 baseline 양식 칸을 재사용하고 새 속성/표는 추가하지 않는다.

---

## §3 Readiness Trace 읽기 표 (이벤트 조합 → trace)

| 이벤트 조합 | 관찰 가능한 readiness trace | 오독 경계 |
|------------|--------------------------|----------|
| `deed_judged`:106 → `deed_saved`:183 | Outcome + Safety: 결과를 검토하고 수용해 저장 | deed_saved = AI 판정 동의로 단정 금지 |
| `deed_judged`:106 → (저장 없이 종료) | J3: Safety readiness 가능 — 결과를 보고 자신이 선택해 닫음 = 정상 종료 | J3 미저장 = 이탈·불신·거부로 단정 금지 |
| `deed_rerolled`:149 → `deed_judged`:106 → `deed_saved`:183 | Reliance + Outcome: AI와 상호 조율(calibrated reliance) 후 수용 | reroll 횟수 = 불신 지표로 단정 금지 |
| `deed_judged`:106 이후 `deed_save_capped`:167 | Availability 차단: 저장 의도 있었으나 가용성 제한 | deed_save_capped = outcome failure / upgrade demand로 단정 금지 |
| `add_flow_started`:72 → (이하 없음) | readiness 신호 없음: 첫 입력 전 이탈 | 잡별 U-C-I 관찰 불가 |
| `deed_judged`:106 (J1/J2/J4에서) → `deed_saved`:183 없음 | 저장 전 이탈 후보 (J3와 구분 필수) | J3와 다른 잡을 합산하지 않는다 |

---

## §4 J3 judged-without-save 정상 종료 경계 (상세)

J3(AI 호기심형) 잡에서 `deed_judged`:106만 발화하고 저장 없이 종료하는 패턴:

1. **정상 종료다** — J3 first value(`deed_judged`)가 이미 도달되었고, 저장은 선택이다
2. **Safety readiness trace 가능** — 결과를 보고 사람이 마지막으로 "저장하지 않기"를 선택했을 수 있다
3. **Reliance trace 불가** — `deed_rerolled`:149 없으면 AI 의존도 조율 관찰 불가
4. **Outcome trace 불가** — `deed_saved`:183 없으면 outcome acceptance 흔적 없음
5. **오독 금지** — judged−saved 갭 = 이탈·불신·AI 판정 거부로 단정하지 않는다

### J3와 J1/J2/J4의 차이

| 잡 | deed_judged 후 미저장 종료의 의미 |
|----|----------------------------------|
| J3 AI 호기심형 | 정상 종료. first value(deed_judged)가 이미 닫힘 |
| J1 기록형 | 저장 전 이탈 후보 (기록 목적이 미달) |
| J2 누적형 | 저장 전 이탈 후보 (누적 payoff 미도달) |
| J4 회고형 | 저장 전 이탈 후보 (회고 완료 미달) |

**잡 분류 없이 `deed_judged` 후 `deed_saved` 없는 세션을 합산하지 않는다.**

---

## §5 신규 계측 금지선

### 허용 (기존 이벤트 읽기만)

- 기존 발화 이벤트 6종(`add_flow_started`:72, `deed_judged`:106, `deed_rerolled`:149, `deed_save_capped`:167, `deed_saved`:183, `level_up_viewed`:199) 발화 여부 손기록
- 60초 관찰 양식 기존 칸에 U-C-I 관찰 결과 수기 기록
- 잡별 readiness trace 분류 (손기록, 비계측)
- 기존 baseline 양식 칸 재사용

### 금지

- 신규 이벤트·속성 추가 (예: `deed_ai_accepted`, `deed_user_controlled`, `deed_understood` 등)
- PostHog 대시보드·funnel·cohort·세션리플레이 신규 생성
- U-C-I 점수화·자동 집계
- readiness trace를 activation rate·retention%·PMF로 환산
- 1~5명 신호로 전환율/신뢰도/AI 만족도 결론 도출
- synthetic/mock/self-test 세션을 사람 관찰에 포함
- `deed_save_capped`:167 발화를 upgrade demand/monetization signal로 읽기

---

## §6 prelaunch 첫 10명 관찰 적용

readiness trace를 첫 10명 관찰 시 기록하는 순서:

1. **트래픽 출처 먼저 분리** — human/synthetic/self-test 구분 (traffic-source-reading-boundary-table.md 기준)
2. **잡을 먼저 분류** — J1/J2/J3/J4 중 어느 잡인지 판단
3. **`deed_save_capped`:167 분리** — availability 차단 여부 먼저 확인 (readiness 관찰 불가 구간)
4. **이벤트 발화 시퀀스 손기록** — 순서와 시간 간격
5. **U-C-I 질문 적용** — §2 표의 잡별 질문으로 관찰
6. **4축 관찰 가능/불가 분류** — Learning은 D7 이후에만 의미 있음
7. **단정 금지** — 3~5명 데이터로 readiness 결론을 내리지 않는다

---

## §7 계승한 기준 / 변경 / 충돌

### 계승 (재정의 0)

- J1/J2/J4 = `deed_saved`:183 first value, J3 = `deed_judged`:106 first value
- `deed_save_capped`:167 = availability/friction early return (outcome trace 제외)
- `deed_rerolled`:149 ≠ 불신. `deed_judged` 후 미저장 ≠ J3 이탈
- synthetic/mock/self-test 제외 원칙
- 이벤트 앵커: add_flow_started:72, deed_judged:106, deed_rerolled:149, deed_save_capped:167, deed_saved:183, level_up_viewed:199

### 변경

없음. 기존 경계 재확인 + readiness trace 4축 분류 렌즈 추가.

### 충돌

없음. 이 문서는 기존 trust calibration(m24) 및 AI 판정 신뢰/제어권 관찰 경계(m38)의 확장 렌즈이며 재정의 0.

### 다음 Marketer에게 넘길 규칙

- `deed_saved`는 AI 판정 동의가 아니라 사용자 행동 완료 신호 — 모든 마케팅 분석의 1번 전제
- J3 미저장 정상 종료 = safety readiness 신호 가능 (부재 신호가 아님)
- Learning 축은 D7 이후에만 readiness trace 의미 있음
- U-C-I 3단계 질문은 기존 baseline 칸에 덧붙여 쓰는 것으로 충분 (새 표 불필요)
- readiness trace는 분류이지 판정이 아니다 — "준비됐다/안됐다"로 결론 내리지 않는다
