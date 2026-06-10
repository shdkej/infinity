# Virtue guided first-value 첫 세션 감사표

- intent: `marketing-51`
- source note: `/home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-10-ai-onboarding-guided-first-value.md`
- scope: docs-only / first-user observation
- status: internal criterion
- permission: L1 docs-only

## 0. 목적

AI 온보딩에서 빠른 산출은 필요하지만, Virtue의 첫 세션 가치는 "AI가 결과를 냈다"보다 "사용자가 무엇을 직접 해냈다고 느꼈는가"에 더 가깝다. 이 감사표는 첫 10명 관찰에서 사용자가 guided path를 어디서 잃는지 보기 위한 내부 수기 기준이다.

신규 이벤트, 속성, tracking/privacy, dashboard, session replay, 공개 카피, 배포는 만들지 않는다.

## 1. 계승 기준

| 기준 | 계승 내용 | 이번 문서의 위치 |
|---|---|---|
| First Value Mapping | J1/J2/J4 = `deed_saved`, J3 = `deed_judged` | 4구간 판독의 종료점 |
| First-User Learning Loop | invite -> pre -> post -> 자기 말 기록 | 세션 중 "안내가 끊긴 곳"을 보강 |
| Post-Response Flow | 결과 이벤트보다 직후 행동을 읽음 | 3구간/4구간 판독 |
| Decision-Control Frame | AI가 대신 정했는지, 사용자가 보라고 정리했는지 구분 | 수기 질문 2개 |
| Prelaunch Boundary | 첫 10명은 방향 재료, decision-grade 지표 아님 | 비율/합격선 산출 금지 |

## 2. 4구간 guided first-value 감사표

| 구간 | 사용자가 해야 할 일 | 좋은 guided 신호 | 끊김 신호 | 잡별 판독 | 손기록 문장 예시 |
|---|---|---|---|---|---|
| 1. 첫 입력 전 | 오늘 한 일을 한 줄로 떠올리고 입력을 시작한다. | "뭘 적으면 되는지 알겠다", 바로 한 가지 행동을 고른다. | 빈 입력을 오래 봄, 예시를 요구함, "좋은 일을 써야 하나요?"라고 묻는다. | J1/J4는 기록 재료 찾기, J2는 누적될 만한 반복 행동 찾기, J3는 AI가 읽을 재료 준비다. | "입력 전 20초 멈춤. '얼마나 대단해야 해요?'라고 물음." |
| 2. AI 판단 대기 | 결과가 나올 때까지 대기 의미를 이해한다. | 기다리는 동안 "AI가 어떻게 읽을지" 기대를 말한다. | 지연을 오류/평가 불안으로 읽음, 반복 클릭, 이탈. | J3는 대기가 가치 기대의 일부일 수 있다. J1/J4에서는 과하면 기록 흐름을 끊는 마찰이다. 지연/503/cap은 availability/friction이다. | "대기 중 '내가 심사받는 건가요?'라고 말함. 결과 전 불안." |
| 3. 결과 해석 | 결과를 읽고 자기 말로 받아들이거나 거절한다. | 자기 말로 다시 설명, 맞는/아닌 부분 선택, 재시도 이유 설명. | 수동 감탄만 하고 끝, 결과 의미를 못 읽음, AI가 대신 결론낸 것으로 느낌. | J3는 `deed_judged` 도착 자체가 first value일 수 있다. J1/J2/J4는 통과점이며 저장/다음 의도까지 본다. | "결과를 보고 '내가 오늘 이런 걸 한 거네'라고 바꿔 말함." |
| 4. 저장/종료 | 잡에 맞게 저장하거나 정상 종료한다. | J1/J2/J4는 저장, J3는 만족한 무저장 종료도 정상. 저장 전 바꾸고 싶은 점을 말하면 자기화 신호다. | J1/J2/J4가 저장 의미를 몰라 보류, J3에 저장을 강요해 흐름이 어긋남, `deed_save_capped`를 가치/업그레이드로 오독. | J1/J2/J4 first value = `deed_saved`. J3 first value = `deed_judged`; 저장은 선택 범퍼다. | "J3 사용자가 결과만 보고 닫음. 불만 없음. 정상 호기심 완료로 기록." |

## 3. 수기 관찰 질문 2개

첫 세션 직후 아래 2개만 짧게 묻는다. 답은 요약하지 말고 가능한 한 원문 그대로 남긴다.

1. "방금 흐름에서 '내가 직접 해냈다'고 느낀 순간이 있었나요? 있었다면 어디였어요?"
   - 읽는 것: 첫 입력, AI 대기, 결과 해석, 저장/종료 중 어떤 구간이 자기 효능감의 위치였는가.
2. "방금 AI가 대신 결정해준 느낌이었나요, 아니면 내가 보라고 정리해준 느낌이었나요? 왜 그렇게 느꼈어요?"
   - 읽는 것: 결정-위임 인지. 판결 프레임인지 관점 프레임인지 본다.

## 4. baseline에 붙이는 수기 칸

기존 `first-real-user-baseline-template` 또는 `first-10-design-user-ask-script` 기록 칸 옆에 아래 값을 손으로 붙일 수 있다. 자동 수집 필드가 아니다.

| 칸 | 허용 값 | 주의 |
|---|---|---|
| guided_break_stage | first_input / ai_wait / result_interpretation / save_or_exit / none | 여러 개면 첫 번째 끊김만 우선 기록 |
| self_done_moment | 원문 또는 구간명 | "직접 해냈다"의 위치, 비율화 금지 |
| delegation_reading | ai_decided / ai_organized / mixed / unclear | 사용자의 말 기준, 관찰자 추정 금지 |
| next_action_meaning | save / reroll / explain / normal_exit / passive_wow / friction | `marketing-49` 태그와 연결 |

## 5. 기존 문서와의 보완 관계

| 선행 문서 | 그 문서의 역할 | 이번 문서가 추가하는 것 | 충돌 여부 |
|---|---|---|---|
| `first-real-user-baseline-template` | 첫 10~20명 1인 1행 기준선 | 같은 행에 guided break 위치를 손기록 | 충돌 없음 |
| `first-10-design-user-ask-script` | 초대 -> pre -> post -> 자기 말 기록 루프 | 세션 중 4구간에서 안내가 끊긴 위치를 보강 | 충돌 없음 |
| `post-result-self-appropriation-reading-table` | 결과 직후 자기화 vs 수동 감탄 판독 | 결과 전의 첫 입력/AI 대기와 저장/종료까지 확장 | 충돌 없음 |

## 6. 해석 금지선

- first value 매핑을 바꾸지 않는다. J1/J2/J4 = `deed_saved`, J3 = `deed_judged`.
- `deed_judged`만으로 모든 잡의 activation을 확정하지 않는다.
- J3의 저장 없는 종료를 이탈이나 가치 부재로 읽지 않는다.
- `deed_save_capped`, 503, 지연은 availability/friction이지 value, retention, upgrade demand가 아니다.
- 빈 입력, 대기 불안, 결과 오해, 저장 보류를 전환율/retention%/PMF/가격 수요로 환산하지 않는다.
- maker self-test, synthetic, mock은 사람 실사용 근거와 섞지 않는다.
- 신규 이벤트/속성/tracking/privacy/dashboard/session replay, 공개 카피, 외부 발송, 배포, 비용, 권한 변경은 모두 approval-needed다.

## 7. 가정 분리

### 계승한 기준

- J1/J2/J4 first value는 `deed_saved`, J3 first value는 `deed_judged`다.
- 첫 10명은 비율이 아니라 문제 언어, 자기 말 가치, 결정-위임 인지로 읽는다.
- AI 결과 직후 행동은 자기화/정상 종료/수동 감탄/마찰로 분리한다.
- 도움은 사용자의 성찰을 대신하지 않고, 사용자가 무엇을 해야 하는지 잃지 않게 하는 범퍼다.

### 이번에 새로 배운 것

- guided onboarding의 핵심 단위는 기능 설명이 아니라 "첫 입력 전 -> AI 판단 대기 -> 결과 해석 -> 저장/종료" 4구간에서 사용자가 자기 행동권을 잃지 않는지다.
- 같은 도움도 구간마다 부호가 다르다. AI 대기는 J3에는 기대 형성일 수 있지만, J1/J4에는 기록 흐름을 끊는 마찰일 수 있다. 저장 안내는 J1/J2/J4에는 first value 경로지만, J3에는 선택 범퍼다.

### 변경한 가정

- 없음. 기존 first value, post-response, first-user learning, no-new-instrumentation 경계를 재정의하지 않는다.

### 충돌

- 없음. 선행 3문서와 역할이 다르다. baseline은 기록표, ask script는 인터뷰 루프, post-result table은 결과 직후 판독이고, 본 문서는 세션 경로의 guided break 위치를 찾는 감사표다.

### 다음 Marketer에게 넘길 규칙

- AI 온보딩 감사는 "빠른 결과가 나왔는가"보다 "어느 구간에서 사용자가 직접 해냈다고 느꼈는가"를 먼저 묻는다.
- guided break를 발견해도 곧바로 넛지/카피/계측으로 옮기지 않는다. 먼저 B-LOST, B-MISMATCH, B-AVAIL, B-NORMAL 성격을 분리한다.
- 수기 질문은 자기 효능감 위치와 결정-위임 인지 2개면 충분하다. 더 많은 질문으로 첫 세션 성찰을 대신하지 않는다.

### MARKETING_LEARNINGS.md 승격 후보

- Guided first-value onboarding is a four-stage handoff, not a faster AI output: first input, AI wait, result interpretation, and save/exit must each preserve user agency, and each job has a different endpoint. J1/J2/J4 close at `deed_saved`; J3 closes at `deed_judged`, so save guidance is optional there.
