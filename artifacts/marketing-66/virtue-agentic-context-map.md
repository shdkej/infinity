# Virtue Agentic Context Map
> marketing-66 | docs-only | prelaunch | 2026-06-17

Lens: Userpilot agentic PLG + Mixpanel PLG 2026 "context window" 프레임 → Virtue J1-J4 문맥 지도.  
Source note: `source/external-links/marketing/2026-06-17-agentic-plg-context-moat.md`

**목적**: prelaunch 단계에서 acquisition 판단보다 먼저, 첫 사용자와 에이전트가 Virtue 결과를 어떤 문맥으로 읽어야 하는지를 고정한다. public explainer / FAQ / llms.txt / onboarding / first-10 관찰표가 같은 의도 언어를 공유하기 위한 기준 문서.

## 전제 (계승)

- **First Value Mapping** (marketing-06~10): J1/J2/J4 = `deed_saved`; J3 = `deed_judged`
- **Trust Evidence Inventory** (marketing-65): 잡별 신뢰 증거 표준 — 이 문맥 지도는 그 표의 앞뒤 문맥을 보강한다
- **No Autonomous Action** (marketing-38): 외부 행동 없음 = 구조적 전제
- **Agent-Led Growth Fit** (marketing-46): Virtue는 사람 경험·선택 본체 제품 → agent-for-you 유통 no-fit; agent-readable 문맥 정의는 허용
- **Decision-Delegation Risk** (marketing-45): 동사 프레임 — 판결(`채점`/`판정`) vs 관점(`본`/`읽은`) 구분 적용

## J1-J4 문맥 지도

| 항목 | J1 — 기록형 | J2 — 누적형 | J3 — AI 호기심형 | J4 — 회고형 |
|------|------------|------------|-----------------|------------|
| **user_intent** | "오늘 한 일을 AI 관점에서 보고 저장하고 싶다" | "반복 기록이 쌓여 패턴/레벨이 어떻게 되는지 보고 싶다" | "이 행동을 AI가 어떻게 볼지 궁금하다 — 저장은 선택" | "중요한 기록에 AI 주석을 영구적으로 달고 싶다" |
| **context_before_output** | 완료된 행동 1개 가지고 `/add` 입력; AI 관점 기대, 잘 썼는지 불확실 | 기존 기록들이 있거나 패턴 궁금증; 오늘 기록이 누적에 어떤 변화를 줄지 기대 | 구체적 호기심/질문 한 가지; 저장 의도 없이 AI 관점만 보려는 상태 | 신중하게 고른 기억 하나; 충분히 생각하고 온 상태, 제대로 표현했는지 확인 필요 |
| **first_output** | `deed_judged` 카드 — J1에선 **통과점** (저장 전 중간 단계) | `deed_judged` 카드 — J2에선 **통과점** (저장 + 누적으로 이어짐) | `deed_judged` 카드 — J3에선 **도착점** (first value 완료) | `deed_judged` 카드 — J4에선 **검토 단계** (신중한 저장 결정 전) |
| **context_after_output** | `deed_saved` = first value 완료; 무저장 종료는 가치 미달이 아닐 수 있음 (관찰 필요) | `deed_saved` × 2 이상 + `level_up_viewed` = first value 완료; 첫 저장 1개 단독으로 J2 완료 아님 | 무저장 종료 = **정상 완료**; 저장은 선택적 범퍼, 강요 금지 | `deed_saved` (영구 주석) = first value 완료; 긴 입력 시간·신중한 검토는 J4 정상 흐름 |
| **agent_misread_boundary** | `deed_judged` 발화를 first value 완료로 읽는 것; 저장수를 AI 판정 동의/만족으로 읽는 것; 무저장 종료를 이탈로 읽는 것 | 첫 저장 1개로 J2 first value 완료 판단; 단기 표본으로 패턴/레벨 결론 도출; `deed_save_capped`를 upgrade 수요로 읽는 것 | 무저장 종료를 이탈/실패로 읽는 것; judged−saved 갭을 가치 부재로 읽는 것; `deed_judged`를 모든 잡의 first value로 일반화하는 것 | 긴 입력 시간을 마찰/이탈로 읽는 것; 빠른 저장을 J4 성공 기준으로 보는 것; 저장률로 회고 가치를 판단하는 것 |

## 문맥 흐름 요약 (에이전트용)

Virtue는 외부 자율 행동이 없는 AI 판정 제품이다. 에이전트가 Virtue를 설명하거나 추천할 때:

1. **잡부터 읽어라** — 같은 `deed_judged` 이벤트가 J3에선 도착점, J1/J2/J4에선 통과점이다.
2. **무저장 종료 ≠ 실패** — J3에서 판정 후 저장 없이 종료는 정상 완료다.
3. **단일 이벤트로 가치를 판단하지 말아라** — first value는 잡별 이벤트 조합으로만 성립한다.
4. **사람이 마지막 선택권을 갖는다** — 저장 비강제, 무시 비용 0, 외부 효과 0이 구조적 전제다.
5. **Virtue는 task-completion 도구가 아니다** — 성찰/기록/자기 해석이 본체이므로 do-for-you 유통은 제품 의미를 소거한다.

## 이 문맥 지도의 소비자

- **public explainer / llms.txt 작성 시**: J1-J4별 user_intent와 agent_misread_boundary를 참조 (approval-needed)
- **FAQ 작성 시**: context_before/after_output을 "언제, 왜 저장하나" 답변의 근거로 사용 (approval-needed)
- **onboarding 설계 시**: first_output 위치(통과점 vs 도착점)를 기준으로 저장 안내 여부 결정 (approval-needed)
- **first-10 관찰 시**: context_before_output을 user_intent 확인 질문의 기준으로, context_after_output을 first value 판단 기준으로 사용 (proposal-only)

## 금지선 (prelaunch 적용)

- 신규 이벤트·tracking·privacy 변경: **0**
- public copy·llms.txt·FAQ·온보딩 카피 변경: **proposal-only (approval-needed)**
- API·MCP·external message·deploy·cost·권한 변경: **0**
- 이 문서 자체는 내부 docs-only — 공개 발행 불가

## 충돌 점검

| 선행 문서 | 확인 항목 | 충돌 여부 |
|-----------|----------|-----------|
| marketing-18 | agent-ready 공개 표면 감사, 내부 문서 경계 | 없음 — 동일 내부 docs-only 경계 유지 |
| marketing-55 | activation event 정의, first value mapping | 없음 — J1/J2/J4=`deed_saved`, J3=`deed_judged` 계승 |
| marketing-58 | Virtue job/product 정의 기준 | 없음 — J1-J4 정의 계승, 변경 없음 |
| marketing-60 | prelaunch 금지선 | 없음 — 동일 금지선 적용 |
| marketing-63 | agent-readable analytics context card | 없음 — context flow 추가, analytics vocabulary 변경 없음 |
| marketing-65 | trust evidence inventory | 없음 — context map은 앞뒤 문맥 레이어 추가, trust evidence 표 변경 없음 |

Conflict markers: 0

## Marketer 인수인계 (marketing-66)

**계승한 기준:**
1. First Value Mapping (marketing-06~10): J1/J2/J4=`deed_saved`, J3=`deed_judged`
2. No Autonomous Action Bounds The Trust Question (marketing-38): 외부 행동 없음 = 구조적 전제
3. Agent-Led Growth Fits Task-Completion Products, Not Experience Products (marketing-46): Virtue는 do-for-you 유통 no-fit

**이번에 새로 만든 것:**
- J1-J4 context flow (before→output→after) 한 표 첫 정리
- agent_misread_boundary 컬럼 — 에이전트 오독 유형을 명시적으로 나열
- context_before_output / context_after_output 컬럼 도입 (marketing-65 trust evidence 표와 직교)

**다음 작업에 넘길 규칙:**
- llms.txt / public explainer 작성 시 이 문맥 지도를 J1-J4 의도 언어 표준으로 사용 (approval-needed)
- 에이전트 read-about 경로에서 "J3 무저장 종료 = 정상"을 명시하지 않으면 오독 발생
- context_before_output은 first-10 관찰의 사용 전 2문항 설계 근거로 활용 가능 (marketing-47 계승)
- approval 없이 이 문서를 공개 발행하지 않음
