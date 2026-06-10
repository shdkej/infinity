# Virtue Guided First-Value 첫 세션 감사표

- intent: `marketing-51`
- source note: `source/external-links/marketing/2026-06-10-ai-onboarding-guided-first-value.md`
- scope: docs-only / first-user in-session observation
- status: draft internal criterion

## 왜 이 감사표가 필요한가

AI 제품의 activation 품질은 AI가 결과를 얼마나 빨리 보여주는가가 아니라, 사용자가 "내가 직접 해냈다"고 느끼는 통제감에 달려 있다. Virtue는 성찰·기록 제품이라 이 구분이 더 중요하다. AI가 판정해 주는 것과 사용자가 자신의 하루를 AI의 도움으로 스스로 정리했다고 느끼는 것은 다른 경험이다.

이 감사표는 첫 10명 관찰에서 4개 구간 중 어디서 사용자의 "직접 해냈다" 감각이 살아 있는지, 어디서 끊기는지를 신규 계측 없이 수기로 읽기 위한 도구다.

## 기존 기준 유지

이 문서는 first value 매핑을 바꾸지 않는다.

| 잡 | 기존 first value | 이번 감사의 역할 |
|---|---|---|
| J1 기록형 | `deed_saved` | 저장 순간에 "내가 기록했다" 느낌이 있는지 본다 |
| J2 누적형 | `deed_saved` | 누적 기록이 자기 맥락으로 쌓이는 느낌이 있는지 본다 |
| J3 AI 호기심형 | `deed_judged` | AI 결과 확인 자체를 "내가 AI에게 물어봤다" 자율 행위로 느꼈는지 본다 |
| J4 회고형 | `deed_saved` | 회고 결과가 "내 말을 AI가 정리해 줬다"로 느껴졌는지 본다 |

## 선행 문서 충돌 점검 (conflict marker)

| 선행 문서 | 겹치는 구간 | 충돌 여부 | 비고 |
|---|---|---|---|
| `first-real-user-baseline-template` | 전체 관찰 기준 | **NO CONFLICT** | baseline template은 집계·기준선 도구; 이 표는 in-session 구간별 수기 관찰 도구 |
| `marketing-47` first-10-design-user-ask-script | 사용 전/후 인터뷰 질문 | **NO CONFLICT** | 인터뷰는 세션 전후; 이 표는 세션 중 4구간 관찰 |
| `marketing-49` post-result-self-appropriation-reading-table | Stage 3·4 행동 판독 | **NO CONFLICT, COMPLEMENTS** | marketing-49는 "결과 직후 자기화 행동"을 본다; 이 표는 "어느 구간에서 agency 감각이 끊겼나"를 추가 |

conflict marker: **no-match** (모든 선행 문서와 충돌 없이 보완 관계 확인)

## 4구간 감사표

첫 10명 관찰에서 각 구간을 아래 표로 수기 기록한다. 체크리스트 형식이므로 관찰자가 선택지 중 하나를 동그라미 치거나 메모를 추가한다.

---

### 구간 1: 첫 입력 전 (Before First Input)

> 무엇을 입력해야 하는지 이해하고, 자기 말로 시작하는가?

| 관찰 항목 | 선택 | 수기 메모 |
|---|---|---|
| 입력창 앞에서 멈춤 없이 바로 입력 시작 | □ yes / □ brief pause / □ long pause | |
| 입력 내용이 자기 오늘 일과·생각·기록 | □ 자기 경험 / □ 테스트 문장 / □ AI에게 질문 형태 | |
| 입력 전 힌트/placeholder에 의존했는가 | □ 무관하게 씀 / □ placeholder 보고 씀 / □ 왜 써야 하는지 물어봄 | |

**Agency signal**: 자기 말로 자기 경험을 입력하면 구간 1 agency 있음. 테스트/질문 형태거나 placeholder에 전적 의존이면 약함.

---

### 구간 2: AI 판단 대기 (Waiting for AI Judgment)

> AI가 판단하는 동안, 사용자는 무엇을 하는가?

| 관찰 항목 | 선택 | 수기 메모 |
|---|---|---|
| AI 응답 대기 중 행동 | □ 화면 주시 / □ 다른 행동 / □ 이탈 / □ 빠름 무관 | |
| AI 응답 속도에 대한 반응 | □ 무반응(정상) / □ "빠르다" / □ "느리다" / □ 기대 명시 | |
| "AI가 내 말을 이해했을까?" 언급 또는 표정 | □ 없음 / □ 있음 | |

**Agency signal**: 대기 중 행동이 없거나 자연스러우면 AI를 "도구로 쓰는" 상태. AI 속도·이해에 집착하면 "AI가 하는 것"으로 인식 중.

---

### 구간 3: 결과 해석 (Result Interpretation)

> AI 결과를 보는 순간, 자기 것으로 해석하는가?

*이 구간은 `marketing-49` post-result-self-appropriation-reading-table과 함께 읽는다.*

| 관찰 항목 | 선택 | 수기 메모 |
|---|---|---|
| 결과를 읽는 속도 | □ 빠르게 훑음 / □ 천천히 읽음 / □ 건너뜀 | |
| 결과를 자기 언어로 재해석 | □ "아, 내가 오늘 이런 걸 한 거네" 류 / □ 조용히 읽음 / □ "AI가 이렇게 말하네" 류 | |
| 결과의 정확성 평가 방식 | □ "맞다/틀리다" 자기 판단 / □ 모름/무관심 / □ AI에게 재확인 요청 | |

**Agency signal (guided first value 핵심)**: "내 하루를 AI가 정리해줬다" 프레이밍 → agency 있음. "AI가 내 점수를 매겼다" 프레이밍 → agency 약함.

---

### 구간 4: 저장/종료 (Save/Close)

> 결과를 내 것으로 남기거나, 자연스럽게 마치는가?

*J3는 저장 없이 종료가 정상 완료임.*

| 관찰 항목 | 선택 | 수기 메모 |
|---|---|---|
| J1/J2/J4 사용자: 저장 행동 | □ 바로 저장 / □ 읽고 저장 / □ 저장 안 함(마찰?) / □ 저장 안 함(정상 종료?) | |
| J3 사용자: 저장 없이 자연 종료 | □ 자연스럽게 닫음 / □ 저장해야 하나 망설임 / □ 혼란 | |
| 종료 후 "다시 쓰겠다" 의향 자발 언급 | □ yes / □ no / □ unclear | |

**Agency signal**: J1/J2/J4에서 "이 결과 내 거다"라고 저장. J3에서 자연 종료. 둘 다 agency 있음.

---

## 수기 관찰 질문 2개

세션 중 관찰자가 최대 1~2분 대화에서 묻는 개방형 질문 후보 (proposal-only, 세션 흐름 방해 금지):

1. **"이 AI가 판단해 주기 전에, 오늘 하루에 대해 어떤 생각을 갖고 있었나요?"**
   - 목적: AI 판단 전 사용자 자체 의견이 있었는지 확인. "아직 모르겠었다" vs "나름 생각이 있었는데 AI 말이 더 정확한 것 같다" 분리.
   - 기록 형식: 원문 그대로 손기록

2. **"방금 결과에서 가장 '내 이야기 같다'고 느낀 부분이 있었나요, 아니면 'AI가 이렇게 보는구나'라는 느낌이었나요?"**
   - 목적: guided first value vs AI-output 귀인 분리. "내 이야기" 비율이 높을수록 agency 강함.
   - 기록 형식: 원문 그대로 손기록

## 승인 경계

- **허용**: 내부 관찰 문서, 수기 기록표, 인터뷰 질문 후보.
- **금지**: 신규 이벤트·속성·tracking/privacy·공개 카피·배포·광고·결제·세션 리플레이·dashboard 추가.
- **미래 approval-needed**: 이 감사표 결과를 제품 카피·온보딩 UI·PostHog 이벤트·자동 리마인드로 전환하는 모든 작업.

## 다음 Marketer에게 넘길 규칙

1. **계승한 기준**: First Value Mapping (J1/J2/J4=`deed_saved`, J3=`deed_judged`), Prelaunch Decision Boundary (정성 손기록), Post-Response Flow Reveals Value.
2. **이번에 새로 정리한 것**: AI가 "대신 해주는" 인식과 사용자가 "AI를 도구로 쓰는" 인식은 같은 결과 화면에서 갈린다. 전환점은 결과 화면이 아니라 구간 1(입력) 시점에서 이미 결정된다.
3. **다음 작업에 넘길 규칙**: 감사표 관찰 결과가 있으면, 어느 구간에서 agency 신호가 끊겼는지 먼저 확인하고 개선 후보를 찾는다. "결과 화면 개선"보다 "입력 단계 조향"을 먼저 검토한다.
