# PLG Signal Hierarchy (Prelaunch Reference)

- date: 2026-06-14
- source_type: synthesis (knowledge base)
- topics: [plg, activation, first-win, PQL, signal-hierarchy, prelaunch]
- related_intents: [marketing-59]

## 핵심 아이디어

PLG(Product-Led Growth)에서 신호를 측정하는 순서가 잘못되면 acquisition 문제를 activation 문제로 오해하거나, measurement-too-early 상태에서 잘못된 결론을 내린다.

## PLG Signal Hierarchy (단계별)

### Level 1: First Win Signals (가장 먼저 볼 것)

| 신호 | 설명 | 측정 시점 |
|------|------|----------|
| first_value_moment | 사용자가 처음으로 "아, 이게 되는구나"를 경험 | 첫 세션 |
| first_successful_output | 사용자가 실제로 뭔가를 만들어냄 (Virtue: deed_saved/deed_judged) | 첫 세션 |
| time_to_first_value | 가입에서 첫 성공 출력까지 걸린 시간 | 첫 세션 |

### Level 2: Activation Signals (두 번째로 볼 것)

| 신호 | 설명 | 측정 시점 |
|------|------|----------|
| return_visit | 두 번째 세션 여부 | D1-D7 |
| repeated_success | 같은 동작을 다시 성공적으로 수행 | D1-D14 |
| habit_signal | 규칙적 재방문 패턴 형성 | D7-D30 |

### Level 3: PQL Signals (launch 이후)

| 신호 | 설명 | 측정 시점 |
|------|------|----------|
| plan_page_visit | 유료 플랜 페이지 방문 | 첫 2주 내 |
| limit_hit | 무료 한도 도달 | 첫 2주 내 |
| upgrade_intent | 업그레이드 의도 표시 | 첫 2주 내 |

### Level 4: Expansion & Viral (launch 이후 측정)

| 신호 | 설명 |
|------|------|
| multi_job_use | 여러 job type 사용 |
| invite_sent | 초대장 발송 |
| viral_coefficient | k-factor |
| nps | 순추천지수 |

## 프리런치에서 흔한 실수

1. **측정 너무 이름**: PQL이나 viral을 첫 10명에게 측정하면 의미 없음
2. **activation 건너뜀**: first win 없이 retention 보면 원인 불명
3. **신호 혼동**: acquisition 실패를 activation 실패로 오인 (입구가 막힌 걸 내부 문제로 봄)

## Virtue 적용 맥락

- Virtue의 first win = deed_saved (J1/J2/J4) 또는 deed_judged (J3)
- Prelaunch 단계에서는 Level 1-2만 수기 관찰
- Level 3-4는 실제 launch 이후 계측 도구 갖춰진 후
