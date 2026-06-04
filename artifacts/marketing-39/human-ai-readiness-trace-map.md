# Virtue Human-AI Readiness Trace Map

> Virtue prelaunch에서 사용자가 AI 판정을 어떻게 이해·제어·통합하는지 관찰하기 위한 사전 틀.
> 신규 이벤트·속성·PostHog·tracking/privacy·카피·배포·외부 발송·비용·권한 변경 금지.

## §0 이 문서의 역할과 경계

인간-AI 제품 평가에서 모델 정확도 단독보다 outcome/reliance/safety/learning 4축의 **상호작용 흔적**을 먼저 보는 것이 readiness 판단에 더 적합하다.

Virtue prelaunch에서 첫 10명 관찰 시:
- 단순 `deed_saved` 횟수나 `deed_judged`→`deed_saved` 전환율로 읽으면 readiness 맥락을 오독할 위험이 있다.
- 이 문서는 4축(outcome/reliance/safety/learning)과 U-C-I 관찰 질문을 미리 등록해, 관찰 시작 이후 해석 틀을 사후에 바꾸지 않도록 고정한다.

**경계**: 이 문서는 관찰 프레임 사전 등록이다. 신규 이벤트·속성·PostHog 대시보드·tracking/privacy·카피·배포·외부 발송·비용·권한 변경은 모두 이 문서 밖 별도 승인 필요.

## §1 4축 정의 (Outcome · Reliance · Safety · Learning)

| 축 | 정의 | Virtue 맥락 |
|----|------|-------------|
| **Outcome** (결과) | 사용자가 AI 판정을 통해 자신의 덕행 기록 과제를 수행했는가. AI가 "잘" 작동했는가가 아니라, 사용자 과제 맥락에서 본 결과 | `deed_saved`(J1/J2/J4), `deed_judged`(J3) 발화는 outcome 달성 후보. **단: deed_saved = AI 판정 동의가 아님**(§5 참조) |
| **Reliance** (의존도) | 사용자가 AI 판정을 조언으로 이해하고 적정 수준으로 의존하는가. 과신(맹목 수용)과 불신(무시) 사이 스펙트럼 | `deed_rerolled`(재시도) = 활발한 reliance calibration 흔적. 저장 전 검토 없이 즉각 저장 = 과신 후보. AI 기능 미사용 = 불신 후보 |
| **Safety** (안전성) | 사용자가 AI 판정의 한계를 인지하고 마지막 선택을 자신이 내리는가 | 저장 비강제·무시 비용 0·외부 효과 0 = Virtue의 구조적 safety ceiling. 관찰은 "사용자가 이 구조를 인지하는가"를 본다 |
| **Learning** (학습) | 사용자가 AI 판정 기준을 이해하고 반복 사용에서 AI 활용 방식을 개선하는가 | `deed_rerolled`(다른 입력 시도) + 두 번째 세션 first value = learning 흔적 후보. 단일 세션에서 관찰하기 어려움 → 손기록 보조 |

## §2 U-C-I 관찰 질문

U-C-I는 readiness trace의 관찰 단위다. 각 세션에서 사용자 행동·발화를 이 3축으로 분류한다.

| 단위 | 정의 | 관찰 방법 |
|------|------|----------|
| **U** — Understanding (이해) | 사용자가 AI 판정을 어떤 의미로 이해했는가? 조언인가, 판결인가? | 사용자 발화·표정·재확인 행동 손기록 |
| **C** — Control (제어) | 사용자가 AI 판정 후 어떤 행동으로 제어권을 행사했는가? | deed_rerolled / 저장 없이 닫기 / 즉각 저장 중 어떤 경로인가 손기록 |
| **I** — Integration (통합) | 사용자가 AI 판정을 자신의 최종 행동에 어떻게 통합했는가? | 저장 내용 + AI 판정 내용의 일치·수정·무관 여부 손기록 |

### 4축 × U-C-I 관찰 질문표

| 축 | U (이해) | C (제어) | I (통합) |
|----|----------|----------|----------|
| Outcome | 사용자가 결과 카드를 과제 완수로 이해했는가, 참고 정보로 이해했는가? | 사용자가 저장/닫기 중 어느 쪽을 선택했는가? | 사용자가 AI 판정 내용을 자신의 덕행 기록에 어떻게 반영했는가? |
| Reliance | 사용자가 AI 판정을 자신의 판단과 대조했는가, 맹목 수용했는가? | 사용자가 `deed_rerolled`(재시도)나 무시/닫기를 선택했는가? | 사용자가 AI 점수 범위를 어느 정도 내면화해 저장했는가? |
| Safety | 사용자가 AI 판정이 틀릴 수 있다는 것을 인지했는가? | 사용자가 저장 없이 닫을 수 있다는 걸 알고 행사했는가? | 사용자가 AI 판정을 "최종 결정"이 아닌 "참고"로 자신의 맥락에 적용했는가? |
| Learning | 사용자가 AI 판정 기준(어떤 덕행이 어떻게 판정되는지)을 파악했는가? | 사용자가 다음 입력을 달리 해보겠다는 시도를 했는가? | 사용자가 첫 결과 이후 더 나은 AI 활용을 위해 입력 방식을 바꿨는가? |

## §3 J1~J4 × Readiness Trace 매핑표

first value 매핑 계승: J1/J2/J4 = `deed_saved`:183, J3 = `deed_judged`:106 (재정의 0).

| 잡 | First Value | Outcome 흔적 | Reliance 흔적 | Safety 흔적 | Learning 흔적 | 정상 종료 기준 |
|----|-------------|--------------|---------------|-------------|----------------|----------------|
| J1 기록형 | `deed_saved`:183 | deed_saved 발화 | 결과 카드 검토 후 저장 vs 즉각 저장(손기록) | 저장 비강제 인식 여부 | 두 번째 덕행 입력 패턴 변화 | deed_saved 후 홈 복귀 |
| J2 누적형 | `deed_saved`:183 | deed_saved + 복귀 세션 | level_up_viewed 후 재저장 의욕 변화 | 누적 payoff를 AI가 "부여한 것"으로 오해 않는가 | 누적 payoff 이해 후 저장 행동 변화 | deed_saved + level_up_viewed(조건부) |
| J3 AI 호기심형 | `deed_judged`:106 | deed_judged 발화 | deed_rerolled(재시도) = 적극 calibration | deed_judged 후 저장 없이 닫음 = 마지막 선택권 행사 | 재시도 입력이 더 나은 판정 탐색인가 | deed_judged 후 deed_saved 없이 종료 (정상) |
| J4 회고형 | `deed_saved`:183 | deed_saved 발화 | 과거 덕행 맥락 참조 후 저장 | 오래된 기록에 AI가 새 의미 부여하는 위험 인식 | 회고 맥락에서 AI 판정 기준 학습 | deed_saved 후 홈 복귀 |

## §4 J3 judged-without-save 정상 종료 경계

J3 잡에서 `deed_judged` 이후 `deed_saved` 없이 세션이 종료되는 것은:

**정상 종료 해석**:
- J3 first value = `deed_judged`. AI 판정을 확인해 호기심이 충족된 자연 종료.
- Safety 흔적 가능: 마지막 선택권(저장 안 함)을 행사한 것.
- Reliance calibration 후보: 저장이 필요하지 않다고 판단한 것.

**금지 해석**:
- judged-without-save → 이탈 ✗
- judged-without-save → AI 판정 거부 ✗
- judged-without-save → 가치 없음 ✗
- judged-save 갭 → retention 위험 ✗
- judged-save 갭 → 묶음 미완료 ✗ (A3 활성화 후보는 `deed_judged` 기준으로만 완료 판정)

**readiness 맥락에서**: judged-without-save = Safety + Reliance 흔적(자율 종료 선택)으로 읽는다. J3에 저장 유도 범퍼를 붙이면 이 자연 종료를 방해한다.

## §5 deed_saved ≠ AI 판정 동의 경계

`deed_saved` 발화는:
- J1/J2/J4의 first value 도달 증거 ✓
- 사용자가 덕행을 저장하기로 결정했다는 것 ✓
- **AI 판정 동의 또는 승인이 아님** ✗

이 경계를 넘으면 생기는 오독:
- deed_saved를 "AI 판정에 동의했다"로 읽으면 Outcome 측정이 왜곡된다.
- deed_saved를 "AI가 좋은 판정을 했다"로 읽으면 AI quality 측정이 왜곡된다.
- deed_saved 비발화를 "AI 판정을 거부했다"로 읽으면 Safety/Reliance 해석이 왜곡된다.

deed_saved 이후 관찰 가능한 readiness 보조 질문(손기록):
- AI 점수가 낮아도 저장했는가? → deed_saved ≠ 동의 확인
- 사용자가 저장 이유를 AI 판정이 아닌 자신의 기준으로 설명했는가?
- 다음 세션에서 같은 잡으로 돌아왔는가? → Outcome · Learning 연속성

## §6 신규 계측 금지선

이 문서의 4축/U-C-I/readiness trace는 관찰 프레임 등록이다.

**금지**:
- 신규 이벤트 추가 ✗
- 신규 속성 추가 ✗
- PostHog 대시보드 변경 ✗
- tracking/privacy 변경 ✗
- 카피 반영 ✗
- 세션 리플레이 설정 변경 ✗
- 배포·외부 발송·비용·권한·개인정보 변경 ✗

**허용** (기존 이벤트 육안 관찰 참조만):
- `deed_saved`:183, `deed_judged`:106, `deed_rerolled`:149, `deed_save_capped`:167, `add_flow_started`:72
- 손기록 양식(기존 first-real-user-baseline-template.md 칸 재사용, 신규 칸 0)

## §7 선행 문서와의 관계

| 문서 | 이 trace map과의 관계 | 충돌 |
|------|----------------------|------|
| `ai-judgment-trust-control-observation-boundary-table.md` | "AI 판정을 조언으로 이해하는가"를 이 map의 Reliance + Safety U축으로 연결 | 0 |
| `activation-candidate-registry.md` | A1~A4 first value 매핑·W-IMM/W-CONF window = 이 map의 first value 매핑 계승 | 0 |
| `first-real-user-baseline-template.md` | U-C-I 관찰 결과는 이 양식의 손기록 칸에 기록, 신규 양식 0 | 0 |

**계승한 기준**:
1. First Value Mapping: J1/J2/J4 = `deed_saved`, J3 = `deed_judged` (재정의 0)
2. No Autonomous Action Bounds The Trust Question: Virtue는 외부 행동 없는 판정 조언 제품 → Safety 관찰은 행동 위험이 아닌 인식 오보정 중심
3. Trust Calibration By Job: J3 reliance/safety 진폭 최대 → readiness trace에서 J3 비중 가장 높음

**이번에 새로 배운 것 (보류 — 다음 실사용 대조 후 MARKETING_LEARNINGS.md 승격 검토)**:
- 4축 독립 흔적 등록 → deed_saved 단일 신호 오독 구조적 방지
- U-C-I(이해/제어/통합) 관찰 단위 → 손기록 3분류로 일관성 향상

**다음 Marketer에게 넘길 규칙**:
- readiness trace를 먼저 분류하고 그다음 activation/retention 숫자를 읽는다 (Traffic Source Before Metrics 패턴과 동일 구조)
- J3 judged-without-save는 Safety + Reliance 자연 종료로 읽는다
- deed_saved ≠ AI 판정 동의 경계는 모든 AI 관련 마케팅 문서에서 명시한다
