---
작성일: 2026-06-11
Intent: marketing-53
Mode: 내부 기획 L1 (docs-only)
Status: complete
Owner: Marketer (Planner / Developer / Operator 관점 종합)
source_note: source/external-links/marketing/2026-06-11-ai-onboarding-intent-to-task.md (knowledge-lab 루트 기준; 로컬 존재 확인)
---

# Virtue 첫 입력/결과 직후 task-completion 감사표 (Intent → AI Task → Next Action Audit Table)

## §0 목적 + 전제

### 목적

AI 온보딩의 기준은 "AI가 답했다"가 아니라 **"사용자의 의도가 실제 작업 완료로 바뀌었는가"** 다(출처노트 §핵심요약·§왜중요한가). Virtue 첫 세션은 사용자가 한 일을 적고(`/add` 진입 → `add_flow_started`) AI 판정을 받아(`deed_judged`) 저장하거나(`deed_saved`) 닫는 흐름이다. 이때 activation을 "결과 카드가 떴다(`deed_judged`)"로만 읽으면 **`deed_judged`를 과대평가**할 위험이 있다.

본 문서는 첫 입력과 결과 직후를 `사용자 의도 → AI가 수행한 작업 → 사용자가 선택한 다음 행동` 세 칸으로 분해해, **답변형 온보딩(AI가 답하면 끝)** 과 **작업완료형 온보딩(의도가 다음 행동으로 전환되어야 끝)** 을 분리해 읽는 잡별 감사표를 고정한다. 검증 질문을 "결과 카드 수 세기"에서 "의도가 어떤 작업으로 바뀌고 어떤 다음 행동으로 닫혔는가"로 옮긴다.

### 전제 (못박기)

1. **판독 렌즈이지 행동 채점이 아니다.** prelaunch이므로 task-completion 점수·임계값·전환율·activation rate를 산출하지 않는다. 첫 10명 관찰 기준만 선명하게 만든다.
2. **신규 0.** 신규 이벤트·속성·코드·카피·대시보드·플래그·세션리플레이·tracking/privacy·타이머를 하나도 만들지 않는다. 이미 발화 중인 기존 6개 이벤트만 인용한다(§4).
3. **재정의 0.** first value 매핑(J1/J2/J4=`deed_saved`, J3=`deed_judged`), 잡 정의(J1~J4), 막힘 분류는 선행 문서가 소유한다. 본 문서는 그 위에 "의도→작업→다음 행동" 판독 층만 더한다(§5 충돌 점검).
4. **승인 전 Waiting.** 공개 카피·신규 tracking·대시보드·외부 모집·비용·배포는 본 Intent로 결정·구현하지 않으며 사용자 승인 전까지 Waiting 대상이다.

## §1 핵심 원칙 — 왜 "답변"이 아니라 "작업 완료"로 읽는가 (5원칙)

1. **`deed_judged` 발화 ≠ 의도 전환 완료.** 카드가 떴다는 사실은 AI가 판정을 *생성*했다는 뜻일 뿐, 사용자의 원래 의도가 충족됐는지는 **직후 행동**으로만 드러난다(activity ≠ acceptance).
2. **의도는 잡마다 다르고, 그래서 "작업 완료"의 정의도 잡마다 다르다.** J1·J2·J4의 의도는 "남긴다/쌓는다/돌아볼 걸 만든다" → 작업 완료는 **저장(`deed_saved`)**. J3의 의도는 "AI가 어떻게 보는지 본다" → 작업 완료는 **판정 확인(`deed_judged`)** 그 자체이고 저장은 선택.
3. **AI가 "대신 끝내는" 제품이 아니다.** Virtue는 사용자의 선택·성찰이 핵심이라(출처노트 §핵심요약 마지막 항목) task-completion을 "AI가 작업을 자동 완료"가 아니라 "사용자가 자기 의도를 말하고(입력) 결과를 보고 **스스로 다음 행동을 선택**"하는 선에서 정의한다.
4. **다음 행동의 대부분은 off-instrument다.** 근거 읽기·자기 말 재정리·비교·망설임·무저장 정상 종료는 화면 안에서 일어나며 이벤트로 환산되지 않는다. on-instrument 신호는 save/reroll/cap/(무행동=종료)뿐 → **다음 행동 증거는 손기록이 우선**이다.
5. **무저장 종료도 한 종류가 아니다.** J3에선 정상 종료(의도 충족 후 닫음), J1/J2/J4에선 작업 미완(저장 전 보류)이다. drop ≠ end를 의도 렌즈에서도 그대로 적용한다.

## §2 first value 매핑 계승 (재정의 0 — 판독 기준점)

아래는 `first-session-jtbd-matrix.md`·`value-per-session-reading-table.md`·`seven-day-deed-loop.md`를 한 글자도 바꾸지 않고 가져온 기준점이다.

| 잡 | 의도 가설 | first value (계승) | 결과 카드(`deed_judged`)의 역할 |
|---|---|---|---|
| **J1 기록형** | "오늘 사소한 행동을 남기고 싶다" | 첫 `deed_saved` | 통과점 (저장 전, 가치 아직) |
| **J2 누적형** | "내가 얼마나 쌓았는지 게임처럼 보고 싶다" | 첫 `deed_saved`(총합↑) | 통과점 (누적 단위는 저장) |
| **J3 AI 호기심형** | "AI가 내 행동을 어떻게 해석하는지 보고 싶다" | 첫 `deed_judged`(저장 전 닫힘 정상) | **본체/도착점** (카드 자체가 first value) |
| **J4 회고형** | "나중에 돌아볼 개인 로그를 만들고 싶다" | 첫 `deed_saved`(로그 첫 항목) | 통과점 (돌아볼 로그는 저장돼야) |

## §3 잡별 task-completion 감사표 (본체)

각 행은 `의도 → AI가 수행한 작업 → 사용자가 선택한 다음 행동`을 한 줄로 읽고, 관찰 증거·기존 이벤트/문서 신호·오독 위험·첫 10명 관찰 질문·무계측 보장을 함께 못박는다.

| 잡 | 사용자 의도 | AI가 수행한 작업 | 사용자가 선택한 다음 행동(작업 완료 신호) | 관찰 가능한 증거 (observable evidence) | 기존 이벤트/문서 신호 | 오독 위험 (interpretation risk) | 첫 10명 관찰 질문 | 무계측 보장 (no-tracking-change) |
|---|---|---|---|---|---|---|---|---|
| **J1 기록형** | "오늘 한 일을 남기고 싶다" | 입력을 판정해 결과 카드 생성(`deed_judged`) | **저장**으로 "남겼다"를 확정 | 저장 이벤트 발화 + 손기록: 저장 후 홈 복귀/표정 | `deed_saved`(작업 완료=first value), `add_flow_started`(의도 진입) | `deed_judged`만으로 "남겼다"로 오독 → J1 의도는 *저장* 전엔 미완 | "이 문장을 입력할 때 '남기는 것'과 'AI 평가받는 것' 중 무엇이 목적이었나?" | 저장 여부는 기존 `deed_saved`로만 읽고 신규 타이머/속성 0 |
| **J2 누적형** | "얼마나 쌓였는지 보고 싶다" | 판정 후 덕력/환생종 진행에 반영될 입력 처리(`deed_judged`) | **저장**으로 총합↑, 부가로 누적/레벨 변화 확인 | `deed_saved` 발화 + (부가)`level_up_viewed` + 손기록: 누적 숫자 응시 | `deed_saved`(총합 증가), `level_up_viewed`(부가 동기) | 첫 세션 `count===0`이라 누적감이 늦게 도착 → "쌓는 재미 부재"를 의도 실패로 오독 | "결과를 본 뒤 '쌓인 숫자/진행'을 확인하고 싶었나, 아니면 판정 자체로 충분했나?" | `level_up_viewed`는 기존 발화만 인용, 도달률 신규 계측 안 만듦 |
| **J3 AI 호기심형** | "AI가 날 어떻게 보는지 보고 싶다" | 판정 결과·근거 카드 제시(`deed_judged`) | **판정 확인 자체가 작업 완료**; 무저장 종료 정상, 재시도(`deed_rerolled`)는 호기심 신호 | `deed_judged` 발화 + 손기록: 근거 읽기/다시 보기/무저장 닫힘 | `deed_judged`(=first value), `deed_rerolled`("다르게 보면?") | judged−saved 갭을 **이탈로 오독** → J3엔 무저장 종료가 정상. 반대로 reroll을 불만으로 오독 | "결과를 보고 저장하지 않고 닫았다면, 원하던 걸 얻고 닫은 건가 실망해서 닫은 건가?" | judged−saved 갭은 기존 두 이벤트 차이로만 읽고 신규 '이탈' 이벤트 0 |
| **J4 회고형** | "나중에 돌아볼 로그를 만들고 싶다" | 입력 판정 후 로그 항목 후보 생성(`deed_judged`) | **저장**으로 돌아볼 첫 항목 적립 | `deed_saved` 발화 + 손기록: 메모/태그로 항목 풍부화 | `deed_saved`(로그 첫 항목) | `deed_judged`를 "회고 가치 발생"으로 오독 → J4 가치는 *나중에 돌아볼 항목이 생김*(=저장) | "지금 결과가 좋아서 저장했나, 나중에 돌아보려고 저장했나?" | 덕행록 재방문은 첫 세션 밖 → 본 표는 첫 항목 저장까지만, 신규 retention 계측 0 |

> **공통 읽기:** ① `add_flow_started` = "의도가 입력 표면에 진입"(작업 시작), `deed_judged` = "AI가 작업 수행", `deed_saved`/무저장 종료/`deed_rerolled` = "사용자가 선택한 다음 행동"(작업 완료 또는 정상 종료). ② `deed_save_capped`는 저장(작업 완료)이 *차단된* availability/friction 구간이지 의도 실패가 아니다.

## §4 인용한 기존 이벤트 6개 (사실 확인 — 신규 정의 0)

선행 문서(`post-response-30-second-action-audit-table.md`, `value-per-session-reading-table.md`, `first-session-jtbd-matrix.md`)가 소유·앵커링한 **이미 발화 중인** 6개 이벤트만 인용한다.

| # | 이벤트 | 본 표에서의 역할(의도→작업→다음 행동) | 비고 |
|---|---|---|---|
| 1 | `add_flow_started` | 의도가 입력 표면에 진입(작업 시작) | `/add` 진입 |
| 2 | `deed_judged` | AI가 작업 수행(판정 생성), J3에선 작업 완료=도착점 | 결과 카드 |
| 3 | `deed_saved` | 사용자가 선택한 다음 행동 = 작업 완료(J1/J2/J4 first value) | 저장 |
| 4 | `level_up_viewed` | J2 부가 동기(누적/진화 확인) | 부가 신호 |
| 5 | `deed_rerolled` | J3 호기심 신호(다르게 보기) | 재채점 |
| 6 | `deed_save_capped` | 작업 완료(저장)가 차단된 availability/friction | 상한 도달 |

> 신규 이벤트·속성·코드·카피·대시보드·tracking/privacy·타이머·세션리플레이·외부 발송·비용·권한 변경 **0건**.

## §5 선행 문서 충돌 점검 (conflict 0)

| 선행 문서 | 충돌 여부 | 관계 |
|---|---|---|
| `post-response-30-second-action-audit-table.md` (m44) | **없음** | 그 문서는 "결과 직후 30초 행동"을 활성화/정상/보류/마찰로 읽는다. 본 문서는 그 위에 **의도(입력 동기)→작업→다음 행동**의 task-completion 분해 층을 더한다. 부호 뒤집힘(같은 행동이 잡별로 다름) 원칙을 그대로 계승. |
| `first-session-jtbd-matrix.md` | **없음** | J1~J4 잡 정의·first value 매핑을 인용만. 재정의 없음. |
| `value-per-session-reading-table.md` (m42) | **없음** | 세션당 first value 판독을 계승. 본 문서는 "의도가 작업으로 전환되는 흐름"만 분리. |
| `seven-day-deed-loop.md` | **없음** | `deed_saved` 중심 활성화 정의 계승. judged−saved 갭의 J3 한정 해석 계승. |
| `ai-judgment-trust-control-observation-boundary-table.md` (m38) | **없음** | "AI 판정을 믿어라가 아니라 사람이 마지막 선택" 원칙과 정합(다음 행동=사용자 선택). |
| `copy-spec.md` | **없음** | 공개 카피 금지어 0, 신규 문구 확정 0. |

## §6 첫 10명 관찰 적용 (proposal-only)

- 첫 10명 관찰표에 컬럼 1개를 **proposal-only**로 추가 검토: "사용자의 입력 의도가 어떤 작업으로 바뀌었고, 어떤 다음 행동으로 닫혔는가"(출처노트 §후속실험 1·3).
- 이 컬럼은 **수기 관찰 항목**이며 신규 계측이 아니다. 사후 질문 "무엇을 하려고 이 문장을 입력했는가" 1개 추가는 승인 전까지 proposal-only로 둔다.
- 본 문서는 그 관찰의 **읽기 기준**(의도→작업→다음 행동, 잡별 오독 위험)만 고정하고, 채택·발송·계측은 사용자 승인 사항으로 남긴다.
