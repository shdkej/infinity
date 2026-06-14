# Virtue Outcome-Readable Docs Audit

- intent_id: marketing-60
- status: completed
- permission: L1 docs-only
- source_note: source/external-links/marketing/2026-06-14-agentic-plg-outcome-docs.md
- predecessors: marketing-58, marketing-59
- scope: Infinity documentation artifact only

## 목적

Agentic PLG 학습을 Virtue prelaunch의 결과 중심 문서 감사표로 번역한다. 이 문서는 기능 설명을 늘리는 것이 아니라, 첫 10명의 사용자가 실제로 받은 결과가 좋은 결과인지, 나쁜 결과인지, 다음 행동이 분명한지 사람이 읽고 에이전트도 재사용할 수 있게 고정한다.

## 선행 기준 유지

- `marketing-58`의 first successful output 계약을 유지한다.
- `marketing-59`의 launch-ready signal gate를 유지한다.
- J1/J2/J4의 첫 성공 출력은 `deed_saved`로 본다.
- J3의 첫 성공 출력은 `deed_judged` 자체로 본다.
- Acquisition, PQL, retention, pricing, paid conversion 판단은 launch-after 영역으로 보류한다.
- 신규 이벤트, tracking, privacy, public copy, deploy, external message, cost-bearing action은 만들지 않는다.

## Outcome-Readable 감사표

| Job | 좋은 결과 기준 | 나쁜 결과 기준 | 다음 행동 기준 | first-10 수기 판독 칸 |
| --- | --- | --- | --- | --- |
| J1 | 사용자가 저장할 만한 덕행 문장이 자기 상황과 맞고, 저장 뒤 다시 볼 이유가 생긴다. | 문장은 그럴듯하지만 사용자의 실제 장면과 어긋나거나 저장 이유가 약하다. | 저장 후 오늘 다시 실천하거나 나중에 확인할 손잡이가 보인다. | `source_scene`, `saved_phrase_quality`, `reuse_reason`, `next_action_visible`, `offscreen_followup` |
| J2 | 사용자가 이미 한 행동을 덕행으로 이해하고, 기록이 자기효능감으로 이어진다. | 칭찬처럼 보이나 왜 덕행인지 설명되지 않거나 기록 가치가 낮다. | 저장 또는 공유 전 자기 언어로 한 번 더 다듬을 수 있다. | `actual_deed_fit`, `virtue_reason_clear`, `record_value`, `edit_needed`, `next_action_visible` |
| J3 | 판단 결과가 사용자의 고민을 줄이고, 저장하지 않아도 결정 또는 재시도 방향이 선명하다. | 판정이 모호하거나 사용자가 다시 질문해야만 의미가 생긴다. | 저장 없이 닫혀도 정상일 수 있으며, 재판정/재입력/실행 중 하나가 자연스럽다. | `judgment_clarity`, `decision_reduced`, `save_not_required_reason`, `reroll_reason`, `next_action_visible` |
| J4 | 장기적으로 쌓을 덕행 기록의 단위가 선명하고, 저장했을 때 누적 의미가 보인다. | 너무 추상적이거나 기록 단위가 커서 다음 입력이 막힌다. | 저장 후 다음 기록 주제나 반복 루프가 자연스럽다. | `accumulation_unit`, `saved_record_quality`, `next_deed_hint`, `repeat_loop_visible`, `offscreen_followup` |

## 공통 판독 규칙

1. 결과가 기능적으로 맞았는지보다 사용자가 받은 의미와 다음 행동을 먼저 본다.
2. `deed_judged`와 `deed_saved`를 같은 성공으로 합치지 않는다.
3. J3는 저장 없는 종료가 실패가 아닐 수 있으므로 `save_not_required_reason`을 별도 기록한다.
4. 나쁜 결과는 모델 실패만이 아니라, 좋은 문장인데도 사용자의 다음 행동을 만들지 못한 경우까지 포함한다.
5. first-10 단계에서는 자동 점수화보다 수기 판독 칸을 우선한다.

## 에이전트 판독용 상태값

| 상태 | 의미 | 사용처 |
| --- | --- | --- |
| `outcome_good` | 결과가 job과 맞고 다음 행동이 보인다. | first-10 관찰 메모 |
| `outcome_weak` | 결과는 생성됐지만 사용자 장면, 저장 이유, 다음 행동 중 하나가 약하다. | 개선 후보 |
| `outcome_bad` | 사용자가 받은 결과가 job과 어긋나거나 혼란을 만든다. | 재작성/UX 점검 후보 |
| `outcome_unclear` | 로그나 수기 메모만으로 판독 불가하다. | 추가 질문 또는 관찰 필요 |

## 충돌 방지

- `marketing-58`의 first successful output 정의를 바꾸지 않는다.
- `marketing-59`의 launch-ready 판단을 앞당기지 않는다.
- 결과 품질 문서화는 public copy가 아니라 내부 관찰 계약이다.
- 계측 이벤트 추가 없이 기존 이벤트와 first-10 수기 메모만 사용한다.

## 다음 행동

- 첫 10명 관찰표에 위 수기 판독 칸을 붙여 결과 품질을 사람이 먼저 읽는다.
- 반복적으로 `outcome_weak`이 나오는 job만 후속 UX/copy/product intent로 분리한다.
- launch 전에는 acquisition/channel/PQL 결론으로 확장하지 않는다.
