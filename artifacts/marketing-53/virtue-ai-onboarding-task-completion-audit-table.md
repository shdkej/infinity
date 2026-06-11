# Virtue AI 온보딩 task-completion 감사표

- intent: `marketing-53`
- source note: `source/external-links/marketing/2026-06-11-ai-onboarding-intent-to-task.md` (로컬 부재 — intent rationale 요지 사용)
- scope: docs-only / proposal-only / no public copy, event, tracking, privacy, deployment, external message, cost change
- status: internal audit
- permission: L1 docs-only

## 0. 목적

AI 온보딩에서 중요한 것은 AI가 답변을 냈다는 사실이 아니라, **사용자가 자신의 의도를 작업 완료로 전환했는가**다. Virtue의 `/add` 첫 입력/결과 흐름을 다음 세 열로 읽는 감사표를 작성한다:

```
사용자 의도 → AI가 수행한 작업 → 사용자가 선택한 다음 행동
```

이 렌즈는 두 가지를 해결한다:
1. `deed_judged` **과대평가 방지** — AI가 판정을 냈다는 것(AI task 완료)이 사용자의 task-completion과 같지 않다.
2. **잡별 행동 증거 보강** — J1/J2/J4=`deed_saved`, J3=`deed_judged` first value 매핑을 사용자 행동 흐름으로 재확인한다.

신규 이벤트·속성·tracking/privacy·dashboard·session replay·공개 카피·배포·외부 발송·비용·권한 변경은 0이다.

## 1. 계승 기준

| 기준 | 계승 내용 | 이번 문서의 위치 |
|---|---|---|
| First Value Mapping | J1/J2/J4 = `deed_saved`, J3 = `deed_judged` | 각 잡의 task-completion 이벤트로 재확인 |
| AI Outcome Proxy Separation | "AI가 활동했다" ≠ "사용자가 결과를 인정했다" | AI task 완료(`deed_judged`) ≠ 사용자 task 완료의 구조적 근거 |
| Guided First-Value Is A Four-Stage Handoff | 첫 입력 → AI 대기 → 결과 해석 → 저장/종료 | 이 감사표는 전체 흐름을 "의도 → AI 작업 → 다음 행동" 단위로 다시 읽는 층 |
| Prompt Design Teaches Desired Result | 입력 prompt는 UI가 아니라 desired result를 가르쳐야 함 | "사용자 의도" 열이 무엇을 기대하고 입력을 시작하는지를 잡별로 명시 |
| Post-Response Flow Reveals Value | 결과 이벤트 발화가 아니라 직후 행동을 읽음 | "사용자가 선택한 다음 행동" 열이 이 흐름 |
| Prelaunch Decision Boundary | 첫 10명은 방향 재료, decision-grade 지표 아님 | 비율/합격선/전환율 산출 금지 |

## 2. 심장표: task-completion 3열 감사

> 첫 verification gate: 이벤트명 6개 확인 — `add_flow_started`(:72), `deed_judged`(:106), `deed_rerolled`(:149), `deed_save_capped`(:167), `deed_saved`(:183), `level_up_viewed`(:199). drift 0.

| 잡 | 사용자 의도 | AI가 수행한 작업 | task-completion 이벤트 | 사용자가 선택한 다음 행동 (정상) | `deed_judged` 과대평가 위험 | 수기 관찰 질문 |
|---|---|---|---|---|---|---|
| **J1 기록형** | "오늘 한 일을 기록으로 남긴다." 작은 행동이 영구적 기록이 되는 것을 원한다. | `/add`에서 사진·메모를 받아 AI가 행동을 판정·요약하고 결과 카드를 반환한다. (`deed_judged`:106) | **`deed_saved`:183** — 결과를 확인하고 저장하는 것이 기록이 "남은" 완료다. | 결과 카드를 읽고 저장(`deed_saved`). 저장 후 홈으로 돌아와 기록이 쌓인 것을 확인한다. | AI가 판정을 냈다고 J1 task가 완료된 것이 아니다. 저장 없이 닫혔다면 task 미완료 후보다(B-LOST 또는 B-MISMATCH 분리 필요). | "방금 저장했을 때, 기록이 남았다는 느낌이 들었나요? 어떤 순간이었어요?" |
| **J2 누적형** | "한 일이 쌓여서 나중에 흐름이 보인다." 오늘 한 줄이 더 큰 그림의 한 점이 되길 원한다. | `/add`에서 사진·메모를 받아 AI가 행동을 판정하고 결과 카드를 반환한다. (`deed_judged`:106) | **`deed_saved`:183** — 저장해야 누적 카운트·`level_up_viewed`(:199) 경로가 열린다. | 결과 카드를 읽고 저장, 홈의 누적 표시(`level_up_viewed` 조건 도달 시)를 확인한다. | J2에서 `deed_judged`만 발화되고 저장되지 않으면 누적 payoff가 열리지 않는다. 저장 없는 종료는 task 미완료 후보다. | "저장 후 홈으로 돌아왔을 때, 한 일이 쌓이는 느낌이 있었나요? 어디서였어요?" |
| **J3 AI 호기심형** | "AI가 내 행동을 어떻게 읽는지 본다." 판정/채점이 아니라 AI의 해석을 보는 것이 목적이다. | `/add`에서 사진·메모를 받아 AI가 행동을 읽고 결과 카드를 반환한다. (`deed_judged`:106) | **`deed_judged`:106** — 결과 카드를 받아 본 것 자체가 task 완료다. 저장은 선택 범퍼다. | 결과 카드를 읽는다. 저장 없이 닫거나, 재시도(`deed_rerolled`:149, 최대 3회)하거나, 저장하거나 — 모두 정상이다. | `deed_judged`가 J3의 first value이므로 이 잡에서는 `deed_judged` "과대평가"가 아니라 **정확한** 기준이다. 단, 저장 없는 종료를 이탈로 읽는 것이 오독이다. | "결과 카드를 봤을 때, AI가 어떻게 읽었다고 느꼈나요? '정해준 것' 같았나요, '보여준 것' 같았나요?" |
| **J4 회고형** | "지나간 일을 돌아보고 남겨두는 재료를 만든다." 나중에 다시 볼 수 있는 회고 재료로서 행동을 저장한다. | `/add`에서 사진·메모를 받아 AI가 행동을 판정하고 결과 카드를 반환한다. (`deed_judged`:106) | **`deed_saved`:183** — 결과가 회고 재료로 남으려면 저장이 필요하다. | 결과 카드를 읽고 저장. 홈으로 돌아와 과거 기록 목록 안에 오늘 것이 있는 것을 확인한다. | J4에서 `deed_judged`만 발화되고 저장되지 않으면 회고 재료가 생기지 않는다. 저장 없는 종료는 task 미완료 후보다. | "저장한 기록이 나중에 돌아볼 재료가 될 것 같았나요? 그 감각이 온 순간이 있었나요?" |

## 3. `deed_judged` 과대평가 오독 목록

다음은 이 감사표가 막으려는 구체적 오독들이다.

| 오독 | 올바른 읽기 |
|---|---|
| `deed_judged` 발화 = 사용자 활성화 완료 | 활성화 완료는 잡별 task-completion 이벤트다. J1/J2/J4는 `deed_saved`, J3만 `deed_judged`. |
| judged−saved 갭 = J1/J2/J4 이탈 | 갭이 있으면 먼저 잡 분류, B-LOST/B-MISMATCH/B-AVAIL/B-NORMAL 성격을 분리한다. J3는 정상 종료 후보다. |
| judged−saved 갭 = J3 가치 부재 | J3의 task-completion은 `deed_judged`이므로 저장 없는 종료는 정상이다. |
| `deed_judged` → `deed_save_capped` = 저장 욕구 막힘 | `deed_save_capped`는 availability/friction 신호이며, 업그레이드 수요나 가치 신호가 아니다. |
| `deed_rerolled` = AI 불신 | 재시도는 불신, 호기심, 입력 조정 등 다의적이다. 재시도 이유를 관찰 전에 단정하지 않는다. |
| AI task 완료 = 사용자 task 완료 | AI가 `deed_judged`를 발화한 것은 AI의 작업이다. 사용자의 task는 잡별로 다르며, J3를 제외하면 여기서 끝나지 않는다. |

## 4. on-instrument vs 손기록 분리

| 관찰 대상 | 수집 방법 | 주의 |
|---|---|---|
| `deed_judged` 발화 여부 | on-instrument (기존 이벤트) | AI 작업 완료 신호. 사용자 task-completion과 동치화 금지. |
| `deed_saved` 발화 여부 | on-instrument (기존 이벤트) | J1/J2/J4 task-completion 신호. J3에 대해서는 선택 범퍼로만. |
| `deed_rerolled` 횟수 | on-instrument (기존 이벤트) | 재시도 신호. 이유는 손기록으로만. |
| `deed_save_capped` 발화 | on-instrument (기존 이벤트) | Availability/friction. 업그레이드/의도 신호로 환산 금지. |
| 결과 카드 읽기 방식 | 손기록만 | "판결로 읽었는가 vs 관점으로 읽었는가"는 on-instrument 불가. |
| task-completion 인지 | 손기록만 | "지금 내가 원하던 게 이루어졌다"는 감각은 on-instrument 불가. |
| guided break 위치 | 손기록만 | 어느 구간에서 "직접 해냈다" 감각이 왔는지. |

## 5. 기존 문서와의 보완 관계

| 선행 문서 | 그 문서의 역할 | 이번 문서가 추가하는 것 | 충돌 여부 |
|---|---|---|---|
| `first-real-user-baseline-template` | 사용자 1인 1행 기준선 기록표 | task-completion 3열(의도/AI작업/다음행동)을 수기 칸으로 추가 가능 | 충돌 없음 |
| `post-result-self-appropriation-reading-table` (m49) | 결과 직후 자기화 vs 수동 감탄 판독 | "사용자가 선택한 다음 행동" 열이 자기화 판독 단계의 앞 입력이 됨 | 충돌 없음 |
| `virtue-guided-first-value-session-audit` (m51) | 4구간 guided break 감사 | task-completion 렌즈는 구간을 합쳐 "의도→AI작업→다음행동" 단위로 읽는 보완 층 | 충돌 없음 |
| `virtue-add-first-input-prompt-design-audit` (m52) | 첫 입력 prompt design 3분류 감사 | "사용자 의도" 열이 prompt가 올바른 잡을 부르는지 확인하는 맥락이 됨 | 충돌 없음 |
| `ai-outcome-proxy-dictionary` (m29) | AI activity vs user acceptance proxy 사전 | task-completion 렌즈는 activity proxy(`deed_judged`) ≠ task-completion의 구조적 근거를 제공 | 충돌 없음 |

## 6. 해석 금지선

- first value 매핑을 바꾸지 않는다. J1/J2/J4 = `deed_saved`, J3 = `deed_judged`.
- `deed_judged` 발화를 모든 잡의 activation으로 확정하지 않는다.
- judged−saved 갭을 J3에서 이탈/가치 부재로 읽지 않는다.
- `deed_save_capped`, 503, 지연은 availability/friction이지 value/upgrade demand가 아니다.
- task-completion 3열을 전환율/retention%/PMF/활성화율로 환산하지 않는다.
- maker self-test, synthetic, mock 데이터를 사람 실사용 근거와 섞지 않는다.
- 신규 이벤트/속성/tracking/privacy/dashboard/session replay, 공개 카피, 외부 발송, 배포, 비용, 권한 변경은 모두 approval-needed다.

## 7. 가정 분리

### 계승한 기준

- J1/J2/J4 first value는 `deed_saved`, J3 first value는 `deed_judged`다. 재정의 없음.
- `deed_judged`와 `deed_saved`는 각각 AI task 완료와 사용자 task 완료(J1/J2/J4)를 나타내는 분리된 신호다.
- `deed_save_capped`(:167)은 availability/friction이며 업그레이드 수요가 아니다.
- 첫 10명 관찰은 비율이 아니라 문제 언어, task-completion 위치, 결정-위임 인지로 읽는다.

### 이번에 새로 배운 것

- "AI 온보딩" 렌즈를 `의도 → AI 작업 → 다음 행동` 3열로 읽으면, `deed_judged` 과대평가가 왜 일어나는지 구조적으로 드러난다. AI의 task(판정 반환)는 항상 `deed_judged` 하나이지만, 사용자의 task는 잡에 따라 거기서 끝나거나(J3) 거기서 시작되거나(J1/J2/J4) 다르다.
- J3만이 AI task completion = 사용자 task completion이 일치하는 잡이다. 나머지 세 잡에서 `deed_judged`는 AI가 자신의 작업을 마친 신호이지, 사용자가 원하던 것을 얻은 신호가 아니다.

### 변경한 가정

- 없음. 기존 first value 매핑, AI Outcome Proxy Separation, Guided First-Value 경계를 재정의하지 않는다.

### 충돌

- 없음. 선행 5문서와 역할이 다르다. 이 문서는 흐름 전체를 "의도-AI작업-다음행동"으로 보는 감사 층이며, 기존 4구간(guided break), prompt design, post-result, proxy 문서를 보완한다.

### 다음 Marketer에게 넘길 규칙

- AI 온보딩 판독에서 "AI가 결과를 냈는가"(`deed_judged` 발화)와 "사용자가 원하던 것을 얻었는가"(task-completion)를 먼저 분리한다.
- J3를 제외한 모든 잡에서 `deed_judged` 발화는 AI의 작업 완료이며, 사용자의 task-completion은 `deed_saved`에서 읽는다.
- judged−saved 갭이 있을 때는 잡을 먼저 확인하고 J3라면 정상 종료 후보, J1/J2/J4라면 B-LOST/B-MISMATCH/B-AVAIL/B-NORMAL을 분리한다.

### MARKETING_LEARNINGS.md 승격 후보

`deed_judged` Is AI's Task, Not User's Task-Completion For J1/J2/J4 — AI 온보딩에서 `deed_judged` 발화는 AI가 자신의 작업(판정 반환)을 마친 신호이며, 사용자의 task-completion과 동치가 아니다. J3만이 AI task completion = 사용자 task completion이 일치하는 잡이고, J1/J2/J4의 task-completion은 `deed_saved`에서 읽어야 한다. `사용자 의도 → AI가 수행한 작업 → 사용자가 선택한 다음 행동` 3열 렌즈가 이 분리를 구조화한다.

## 8. First verification gate 결과

- 출처노트 경로 인용: yes (`source/external-links/marketing/2026-06-11-ai-onboarding-intent-to-task.md`, 로컬 부재 명시, intent rationale 요지 사용)
- 이벤트명 6개 인용 및 앵커 일치:
  - `add_flow_started`:72 — 이 문서에서 직접 인용하지 않음(범위 밖); heartbeat 참조만
  - `deed_judged`:106 ✓
  - `deed_rerolled`:149 ✓
  - `deed_save_capped`:167 ✓
  - `deed_saved`:183 ✓
  - `level_up_viewed`:199 ✓
- conflict marker: 0
- 신규 이벤트/속성/tracking/privacy/공개 카피/배포/외부발송/비용/권한 변경: 0
