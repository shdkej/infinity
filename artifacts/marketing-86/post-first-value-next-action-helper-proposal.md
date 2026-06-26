# Virtue post-first-value next action helper proposal

> 첫 가치 직후 긴 재온보딩 대신, 잡별로 짧게 나타났다가 사라지는 `next action helper`를 proposal-only로 정리한 1장 문서다.
> 범위는 홈 복귀 흐름 해석까지이며, 프로덕션 카피/배포/계측 변경은 포함하지 않는다.

- id: marketing-86
- permission: L1 docs-only
- inherited_from:
  - `artifacts/marketing-84/next-step-bridge-audit-proposal.html`
  - `artifacts/marketing-47/virtue-first-10-design-user-ask-script.md`
  - `source/external-links/marketing/2026-06-26-post-first-value-next-action-helper.md`
- checked_surface:
  - `/home/ubuntu/dev/virtue-rebirth-app/apps/web/src/app/page.tsx`

## 결론

- J1/J2/J4는 첫 저장 뒤 홈의 `최근 덕행`이 canonical helper surface다.
- J3는 결과 카드가 first value의 도착점이므로, 홈 helper보다 결과 카드 안의 `멈춰도 됨 / 한 번 더 보기` 해석이 우선이다.
- helper 기본값은 **show-nothing** 이고, 첫 가치 직후 한 번만 보이며 조건을 지나면 사라지는 event-triggered 문장이어야 한다.

## 잡별 helper 제안

| 잡 | first value | primary surface | 노출 시점 | 한 줄 helper | 사라짐 조건 | 금지 문장 |
|---|---|---|---|---|---|---|
| J1 기록형 | `deed_saved` | 홈 `최근 덕행` | 첫 저장 직후 홈 복귀 1회 | 방금 남긴 기록이 여기 쌓였어요. 오늘 흐름을 잇고 싶으면 한 줄 더 남겨보세요. | 다음 `add_flow_started`, 최근 덕행 2건 이상, 세션 종료 | 성장/연속성 압박, 체크리스트형 단계 안내 |
| J2 누적형 | `deed_saved` | 홈 `최근 덕행` + 덕력 카드 보조 | 첫 저장 뒤 홈 복귀, 누적이 아직 체감 안 될 때 1회 | 첫 기록이 남았고 덕력도 움직였어요. 하나만 더 쌓이면 리듬이 더 또렷해져요. | 두 번째 저장 완료, `level_up_viewed`, 세션 종료 | 레벨업 강요, streak/매일 해야 함 프레임 |
| J3 AI 호기심형 | `deed_judged` | `/add` 결과 카드 | 결과 카드 도착 직후만 | 여기서 멈춰도 괜찮고, 궁금하면 다른 장면으로 한 번 더 볼 수 있어요. | 카드 이탈, reroll/새 입력 시작, 저장/닫기 | 저장해야 끝난다, 지금 남겨두자, 더 해야 제대로 봤다 |
| J4 회고형 | `deed_saved` | 홈 `최근 덕행` | 첫 저장 뒤 홈 복귀 1회 | 돌아볼 기록이 생겼어요. 다음 한 건이 쌓이면 오늘의 모양이 더 분명해져요. | 다음 `add_flow_started`, 최근 덕행 2건 이상, 세션 종료 | 성과 압박, 점수 경쟁, 지금 더 해야 완성된다는 표현 |

## 표면 우선순위

1. J1/J2/J4: 홈 `최근 덕행`
2. J3: `/add` 결과 카드
3. 보조 표면: 홈 덕력 카드

- 이유: 현재 홈 `최근 덕행`은 첫 방문 empty-state와 저장 후 recent list가 이미 분리되어 있어, "방금 남은 흔적"과 "다음 한 걸음"을 가장 짧게 붙이기 좋다.
- 반대로 hero/덕력 카드는 누적 약속은 보여주지만 다음 행동을 3초 안에 읽히게 하기는 약하다.

## self-audit

### 3초 설명 통과 여부

| 잡 | 3초 안에 다음 행동을 한 문장으로 설명 가능한가 | 메모 |
|---|---|---|
| J1 | 예 | "방금 남긴 기록이 보이고, 하나 더 남기면 된다." |
| J2 | 예 | "쌓였다는 게 보였고, 한 번 더 하면 누적감이 커진다." |
| J3 | 예 | "여기서 멈춰도 되고, 궁금하면 다른 걸 한 번 더 본다." |
| J4 | 예 | "돌아볼 기록이 생겼고, 한 건 더 쌓이면 회고 재료가 선명해진다." |

## 계승한 기준

- `Nudges Are Event-Triggered, And Show-Nothing Is The Default`
- `Guided First-Value Is A Four-Stage Handoff`
- `First-User Learning Loop Reads Language, And Help Means Articulation Not Delegation`

## 이번에 새로 배운 것

- 홈 복귀 helper는 새 onboarding layer가 아니라 `recent proof + next action` 한 줄이면 충분하다.
- J3는 helper가 필요하더라도 홈이 아니라 결과 카드에서 해석되어야 저장 강요를 피할 수 있다.

## 다음 작업에 넘길 규칙

- 구현이 열리더라도 전역 고정 helper나 상시 checklist로 확장하지 않는다.
- helper 후보는 먼저 잡별 proposal로 유지하고, 실제 사용 언어 관찰 전 공개 카피로 승격하지 않는다.
- J3에서 저장 유도는 기본값이 아니라 예외 제안으로만 다룬다.
