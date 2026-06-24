# Virtue 홈 반환형 Empty-State Gating 정렬 제안서

- id: marketing-83
- created: 2026-06-24T2300Z
- type: proposal-only (L1 docs)
- based_on: marketing-80, marketing-81, marketing-70, MARKETING_LEARNINGS.md

## 목적

첫 저장/첫 판단 뒤 홈 복귀 사용자에게 누적/요약 신호와 `아직 기록이 없어요.` empty-state가 동시에 보이는 충돌을 제거한다.

## 계승한 기준

- **marketing-80**: 요약/점수 신호와 empty-state 공존이 첫 저장 이후 신뢰를 깎는다. safest next step은 홈 empty-state gating 정렬.
- **marketing-81**: 가장 위험한 충돌은 누적/요약 신호와 `아직 기록이 없어요.` empty-state가 같은 반환 세션에서 함께 보이는 상태.
- **MARKETING_LEARNINGS — Nudges Are Event-Triggered**: 기본값은 "띄우지 않음". B-LOST 이외에는 넛지를 띄우지 않는다.
- **MARKETING_LEARNINGS — Product Body vs Bumper By Job**: 홈은 J2에서 본체(누적 payoff), J1에서 범퍼(다음 행동 안내).
- **MARKETING_LEARNINGS — First Value Mapping**: J1/J2/J4=deed_saved, J3=deed_judged.

## 충돌 진단

| 표면 | 현재 상태 | 충돌 조건 | 위험도 |
|------|-----------|-----------|--------|
| 홈 hero | 일반 환영 문구 항상 노출 | 반환 세션에서도 신규 문구 | 중간 |
| 요약/누적 카드 | 카드 + empty-state 공존 | deed_saved ≥ 1인데 `아직 비어있어요` | 높음 |
| 최근 덕행 섹션 | `아직 기록이 없어요.` | deed_saved ≥ 1인데 첫 방문 empty-state | 높음 |

## Gating 규칙

### Gate 조건 (잡별)

| 잡 | Gate ON 조건 | 이유 |
|----|--------------|------|
| J1 기록형 | deed_saved ≥ 1 | 저장 한 번 이상 |
| J2 누적형 | deed_saved ≥ 1 | 누적 payoff 시작점 |
| J3 AI판단형 | deed_judged ≥ 1 | deed_saved 아님 — 별도 분기 필요 |
| J4 영구주석형 | deed_saved ≥ 1 | J1과 동일 |

### 표면 1: 홈 hero 반환형 문장 후보

| 잡 | 반환형 문장 후보 | 설계 의도 |
|----|-----------------|-----------|
| J1/J4 | 이어서 기록해볼까요? | 저장 행동 연속성 강조 |
| J2 | 오늘의 덕행을 이어서 쌓아봐요 | 누적 payoff 연결 |
| J3 | 지난 AI 판정이 기다리고 있어요 | 저장 안내 없이 판정 recall |

> 전역 단일 문장 최적화 금지. 잡별 분기로만 사용. 공개 카피 배포는 approval-needed.

### 표면 2: 요약·누적 카드

| 상태 | 현재 | 제안 |
|------|------|------|
| deed_saved ≥ 1 | 카드 + empty-state 공존 | empty-state 숨김, 카드만 표시 |
| deed_saved = 0 | empty-state만 | 변경 없음 (신규 정상) |

### 표면 3: 최근 덕행 섹션 (핵심 충돌 지점)

| 상태 | 현재 | 제안 |
|------|------|------|
| deed_saved ≥ 1, 오늘 저장 없음 | `아직 기록이 없어요.` | `오늘은 아직 기록이 없어요.` |
| deed_saved ≥ 1, 오늘 저장 있음 | 정상 표시 | 변경 없음 |
| deed_saved = 0 | `아직 기록이 없어요.` | 변경 없음 (신규 정상) |

> 핵심: "전체 이력 0건"과 "오늘 이력 0건"을 구분하지 않는 것이 충돌의 구조적 원인.

## 구현 금지 항목 (approval-needed)

- deed_count 기반 분기 코드 production 배포
- tracking/analytics 이벤트 추가
- 공개 카피 배포
- A/B 테스트 설정

## 이번에 새로 배운 것

- 반환형 gating의 핵심 분기는 "신규 vs 복귀"가 아니라 "**첫 가치 도달 전 vs 이후**"다.
- 최근 덕행 섹션의 `아직 기록이 없어요.`는 전체 이력 0건과 오늘 이력 0건을 구분하지 않는 것이 충돌의 본체다.
- J3는 deed_judged로 gate를 여는 게 일관성상 맞다 (deed_saved 아님).

## 다음 작업에 넘길 규칙

- 홈 표면 gating 구현 시 J3의 deed_judged gate를 J1/J2/J4의 deed_saved gate와 별도로 처리한다.
- hero 반환형 문장은 proposal-only 유지. A/B 없이 production 적용 금지.
- gating 분기 구현 시 J2 누적 payoff 표면이 J2 본체임을 명심한다.
