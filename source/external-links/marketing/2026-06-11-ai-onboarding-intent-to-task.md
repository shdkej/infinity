# AI 온보딩: 의도를 작업 완료로 바꾸는 흐름

> 출처 노트. marketing-53 intent의 근거 자료.
> 2026-06-11T10:00Z

## 핵심 렌즈

AI 온보딩의 성공 지표는 "AI가 답변했는가"가 아니라 "사용자가 자신의 의도를 완료했는가"다.

AI-first 제품에서 onboarding은 세 단계 흐름이다:
1. **사용자 의도** — 사용자가 /add 진입 시 갖는 목표 (기록, 성장, 판단, 회고)
2. **AI 수행** — `add_flow_started` → `deed_judged` 구간에서 AI가 실행하는 작업
3. **사용자 선택** — 결과 직후 사용자가 선택하는 다음 행동 (저장, 재판정, 무저장 종료)

## Virtue 적용 맥락

Virtue는 잡별 first value가 다르다:
- J1(기록)/J2(성장)/J4(회고): `deed_saved` = first value 도달
- J3(판단): `deed_judged` = first value 도달, 저장은 선택

prelaunch 첫 10명 관찰에서 신규 계측 없이 이 흐름을 더 선명하게 보려면,
첫 입력/결과 직후 행동을 잡별 task-completion 3-컬럼으로 정리하면 된다.

## 기존 이벤트명 (6개)

이 노트는 아래 6개 이벤트명이 현재 Virtue 계측에 존재함을 전제한다:
1. `add_flow_started`
2. `deed_judged`
3. `deed_saved`
4. `deed_rerolled`
5. `deed_save_capped`
6. `level_up_viewed`

## 기대 산출

- `artifacts/marketing-53/task-completion-audit-table.md`: 잡별 3-컬럼 감사표
- 기존 marketing-47(first-user learning loop), marketing-51(guided first-value handoff), marketing-52(prompt design) 문서와 충돌 없이 보강
- 신규 계측·카피·이벤트 변경 0
