# marketing-83 Virtue 홈 반환형 empty-state Gating 정렬 제안서

Date: 2026-06-24
Scope: 홈 3표면 × J1-J4 기준 반환형 문장 후보 + gating 규칙
Method: marketing-80/81 결론 기반 docs-only proposal.
변경: production/tracking/privacy/code deploy/외부 메시지 변경 0.

## Inherited Learning

- **marketing-80**: 홈 요약 카드·최근 덕행·저장 후 복귀 지점 감사. 결론: empty-state gating이 safest next step.
- **marketing-81**: 첫 저장/첫 판단 뒤 홈 복귀 secondary onboarding 감사. 결론: `deed_saved ≥ 1` 이후에도 empty-state가 남아있으면 신뢰를 가장 크게 깎는다.
- **marketing-81 Handoff Rule**: 홈 전체 리디자인이 아니라 hero 보조문구, summary card 보조문구, `최근 덕행 empty-state gating` 세 표면만 범위로 제한한다.
- **marketing-79**: J1/J2/J4의 first value = `deed_saved`, J3의 first value = `deed_judged`.

## J1-J4 정의

| 코드 | deed_saved | deed_judged | 설명 |
|------|-----------|-------------|------|
| J1 | 0 | 0 | 첫 방문, 아직 아무것도 하지 않음 |
| J2 | 0 | 0 | 홈에서 탐색 중, 아직 저장 없음 |
| J3 | 0 | ≥1 | /add에서 AI 판단 확인 후, 아직 저장 미완료 가능 |
| J4 | ≥1 | any | 최소 1개 덕행 저장 후 홈 복귀 |

## 표면 1: Hero Headline

**현재**: `오늘 1덕만 쌓아볼까요?`

| J | deed_saved | 제안 동작 |
|---|---|---|
| J1 | 0 | 현재 유지 |
| J2 | 0 | 현재 유지 |
| J3 | 0 | 현재 유지 (/add 결과에서 처리됨) |
| J4 | ≥1 | **반환형 문장으로 분기** |

**J4 반환형 문장 후보**:
- A: `방금 남긴 흐름 이어서 하나 더 쌓아볼까요?` ← **추천**
- B: `이미 한 걸음 내딛었어요. 오늘도 하나 더 남겨볼까요?`
- C: `첫 기록이 쌓였어요. 오늘도 이어가볼까요?`

**추천 이유**: A는 '방금'으로 직전 가치를 명시하고, '이어서'로 연속성을 강조하며, 기존 문장 구조(`~까요?`)를 유지해 UI 맥락 충돌이 없다.

**gating 조건 (구현 참고, proposal-only)**:
```
if deed_saved >= 1:
  hero_text = "방금 남긴 흐름 이어서 하나 더 쌓아볼까요?"
else:
  hero_text = "오늘 1덕만 쌓아볼까요?"  // 현재 유지
```

## 표면 2: 요약/Summary 카드 보조문구

**현재**: 누적 수치만 있고, next-step bridge 보조문구 없음.

| J | deed_saved | 제안 동작 |
|---|---|---|
| J1/J2/J3 | 0 | 현재 유지 (수치만 혹은 빈 상태) |
| J4 | ≥1 | **next-step bridge 보조문구 추가** |

**J4 카드 보조문구 후보**:
- A (범용): `하나 더 남겨 흐름을 이어가요.` ← **추천**
- B (누적형): `기록이 쌓일수록 내 덕의 패턴이 보여요.`
- C (AI형): `다른 사례도 AI로 다시 보면 내 기준이 선명해져요.`
- D (성취형): `이번 기록으로 한 걸음 더 이어졌어요.`

**추천 이유**: A는 Job 구분 없이 J1/J2/J3/J4 모두에 안전하며 행동 유도가 가장 직접적이다. Job별 분기가 가능해지면 B/C/D를 적용한다.

**gating 조건 (proposal-only)**:
```
if deed_saved >= 1:
  show card_subtitle = "하나 더 남겨 흐름을 이어가요."
else:
  // 현재 상태 유지
```

## 표면 3: `최근 덕행` Empty-State

**현재**: `아직 기록이 없어요.` (deed_saved와 무관하게 항상 렌더됨)

**이것이 가장 위험한 표면** (marketing-80/81 동일 결론): deed_saved ≥ 1인데도 이 문구가 보이면 저장 성공 신뢰를 즉각 훼손한다.

| J | deed_saved | 현재 동작 | 제안 |
|---|---|---|---|
| J1 | 0 | `아직 기록이 없어요.` | 유지 |
| J2 | 0 | `아직 기록이 없어요.` | 유지 |
| J3 | 0 | `아직 기록이 없어요.` | 유지 (저장 전이므로 정확함) |
| J4 | ≥1 | `아직 기록이 없어요.` ❌ | **숨김** (방안 A 추천) |

**방안 비교**:

| | 방안 A (최소·추천) | 방안 B (과도형) | 방안 C (샘플) |
|---|---|---|---|
| 구현 | deed_saved≥1이면 empty-state 숨김 | 대체 메시지: "방금 저장한 기록이 여기 나타나요" | deed_saved=0일 때만 ghost 카드 |
| 경험 | 로딩 전 빈 공간 가능 (skeleton 병행 권고) | 과도 상태 명시 | proof preview 제공 |
| 위험 | 로딩 중 빈 화면처럼 보일 수 있음 | 구현 복잡도 중간 | ghost/sample 구분 표시 필요 |
| 연관 | — | — | marketing-71/78 proof 전략 연계 시 |

**추천**: 방안 A. `deed_saved >= 1`이면 empty-state 문구를 숨긴다. loading skeleton과 함께 고려하면 완성도가 높다.

**gating 조건 (proposal-only)**:
```
if deed_saved >= 1:
  hide empty_state_message  // `아직 기록이 없어요.` 숨김
  show loading_skeleton_or_real_list
else:
  show empty_state_message  // 현재 유지
```

## 통합 Gating Rule 요약

```
// deed_saved = 저장된 덕행 수 (서버에서 받아오는 값)
if (deed_saved >= 1) {
  // 표면 1: hero 반환형 문장
  hero = "방금 남긴 흐름 이어서 하나 더 쌓아볼까요?"
  // 표면 2: 요약 카드 보조문구
  card_subtitle = "하나 더 남겨 흐름을 이어가요."
  // 표면 3: 최근 덕행 empty-state 숨김
  show_empty_state = false
} else {
  // J1/J2/J3: 현재 상태 유지
  hero = "오늘 1덕만 쌓아볼까요?"
  card_subtitle = ""
  show_empty_state = true
}
```

## marketing-80/81 충돌 검증

| 기준 | marketing-80 결론 | marketing-81 결론 | 이 제안 |
|------|---|---|---|
| empty-state gating | safest next step | deed_saved 이후가 가장 위험 | 방안 A로 직접 해결 ✅ |
| hero 분기 | 직접 언급 없음 | 반환형 분기 권장 | J4 분기 문장 후보 제시 ✅ |
| 요약 카드 | next-step bridge 검토 표면으로 분류 | 누적 카드 보조문구 우선 검토 | 보조문구 후보 제시 ✅ |
| 구현 범위 | proposal-only | 신규 이벤트/tracking/배포 없이 | 동일 제약 적용 ✅ |
| **충돌** | | | **0 충돌** |

## 다음 판단

1. hero/카드 보조문구 문안 중 하나를 최종 선택한다.
2. empty-state gating(방안 A)을 approval-needed implementation intent로 등록한다.
3. hero 분기 구현도 같은 intent에 포함하거나 별도 scope로 분리한다.
4. 구현 시: tracking/privacy/배포/external message 변경 없이 문장·상태 분기만 적용한다.
5. 구현 후 loading skeleton 동작과 deed_saved 값 로딩 타이밍을 함께 검증한다.
