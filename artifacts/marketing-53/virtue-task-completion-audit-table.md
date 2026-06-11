# Virtue first input / result task-completion audit table

- intent: `marketing-53`
- source note: `source/external-links/marketing/2026-06-11-ai-onboarding-intent-to-task.md` (path noted; file unavailable in this cloud run — rationale confirmed from intent)
- scope: docs-only / proposal-only / no public copy change
- status: internal audit
- permission: L1 docs-only

## 0. Purpose

AI 온보딩을 읽는 렌즈를 "AI가 답변을 냈다"에서 "사용자 의도가 작업 완료로 바뀌었나"로 이동한다. Virtue에서 이는 `첫 입력 → deed_judged → 사용자가 선택한 다음 행동` 시퀀스를 다음 3축으로 읽는 것이다.

```
사용자 의도 (User's task intent)
   ↓
AI가 수행한 작업 (AI's contribution: deed_judged)
   ↓
사용자가 선택한 다음 행동 (User's chosen next action)
```

핵심 위험: `deed_judged` 발생을 J1/J2/J4 task completion으로 읽으면 over-count된다. AI의 기여는 완료됐지만 사용자의 작업은 deed_saved까지 미완료다. J3만 deed_judged가 task completion이다.

이 문서는 코드, 공개 카피, 이벤트, 트래킹, 개인정보, 대시보드, 세션리플레이, 배포, 가격, 외부발송, 계정 상태를 변경하지 않는다.

## 1. 계승한 기준

| 기준 | 계승 규칙 | 이 감사에서의 적용 |
|---|---|---|
| First Value Mapping | J1/J2/J4 = `deed_saved`; J3 = `deed_judged` | 잡별 task completion 정의의 원천 |
| Guided First-Value Is A Four-Stage Handoff | 첫 입력 → AI 대기 → 결과 해석 → 저장/종료 | Task completion은 handoff의 잡별 자연 종료점과 일치 |
| Prompt Design Teaches Desired Result | UI instruction ≠ judgment delegation ≠ desired-result teaching | AI의 작업은 원하는 결과를 보여주는 것; 사용자의 작업은 그것을 유지할지 결정하는 것 |
| Post-Response Flow Reveals Value | deed_judged 단독 ≠ value delivered; 다음 행동이 task 완료 여부를 보여준다 | 이 감사의 핵심 프레임 |
| Prelaunch Decision Boundary | 작은 표본은 결론이 아니다 | 모든 패턴은 관찰 기준이지 확정이 아니다 |

## 2. Task-completion frame

"Task completion"은 AI가 행동한 시점이 아니라 사용자가 AI가 제공한 것에 반응해 선택한 시점이다.

- J1/J2/J4: task completion = `deed_saved`. `deed_judged`는 AI의 기여이고, 사용자는 그것을 수락(저장), 재고(재판정), 차단(cap), 또는 반응 없이 이탈(exit) 중에서 고른다.
- J3: task completion = `deed_judged`. 사용자의 의도는 AI의 읽기를 보는 것이었고, 그것을 보는 것 자체가 완료다. 저장은 보너스 선택이다.

## 3. 잡별 task-completion 감사표

| Job | 사용자 의도 | AI가 수행한 작업 | deed_judged 단독 의미 | 사용자가 선택한 다음 행동 | Task complete 시점 | 관찰 메모 |
|---|---|---|---|---|---|---|
| **J1** 기록 | "이 행동을 기록으로 남긴다" | 오늘 행동에 점수/관점 제공 | AI 기여 완료; 사용자 작업 미완료 | `deed_saved` = 완료 / `deed_rerolled` = 더 나은 읽기 탐색 / `deed_save_capped` = 저장 차단(availability) / exit = 기록 안 함(이탈 후보) | `deed_saved` | judged→exit는 손기록 대상. 이탈 단정 금지. |
| **J2** 누적 | "이 행동을 쌓임의 일부로 만든다" | 오늘 행동을 평가하고 히스토리에 추가 | AI 기여 완료; 사용자 작업 미완료 | `deed_saved` = 완료 (+`level_up_viewed` 가능) / `deed_rerolled` = 오늘 읽기 재시도 / `deed_save_capped` = 저장 차단(availability) / exit = 쌓임에 추가 안 됨(이탈 후보) | `deed_saved` | J2 judged→exit는 "저장 전에 무엇이 막혔나" 손기록. |
| **J3** AI 호기심 | "AI가 이것을 어떻게 읽는지 본다" | AI의 관점/해석을 보여줌 | **사용자 작업 완료** | `deed_judged` 후 exit = 정상 종료(저장 강제 없음) / `deed_saved` = 읽기를 간직하려는 추가 선택 / `deed_rerolled` = 다른 입력으로 재탐색 | `deed_judged` | judged→exit는 J3 task success. judged→saved는 bonus. |
| **J4** 회고 | "이 순간이 내 말로 보존되게 한다" | AI가 기록의 의미를 포착해 보여줌 | AI 기여 완료; 사용자 작업 미완료 | `deed_saved` = "이 읽기가 보존할 만하다" = 완료 / `deed_rerolled` = 다른 포착 방식 탐색 / `deed_save_capped` = availability 차단 / exit = 보존 안 함(이탈 후보) | `deed_saved` | J4 judged→exit는 "AI 읽기가 사용자 말과 맞지 않았나" 손기록. |

## 4. deed_judged 과대평가 패턴

| 과대평가 패턴 | 실제 의미 | 올바른 읽기 |
|---|---|---|
| deed_judged 발생 = J1/J2/J4 task complete | AI의 기여는 완료됐지만 사용자 작업은 미완료 | deed_judged는 중간 단계; deed_saved까지 봐야 완료 |
| judged→exit = J3 task failed | J3 사용자의 task는 deed_judged에서 완료됨 | 저장 없는 종료는 J3 task success |
| deed_save_capped = user chose not to save | 저장하고 싶었지만 차단됨 | availability/friction. 의사 판단 아님 |
| deed_rerolled = task failed / user unhappy | 더 나은 읽기를 원하는 호기심 또는 재시도 | task failure로 단정 금지 |
| high deed_judged count = good activation | AI가 자주 판정했다는 것; 사용자가 저장했는지는 다른 질문 | count 자체가 아니라 judged→next_action 흐름을 본다 |

## 5. 첫 10명 관찰 기준 (신규 계측 0)

손기록 관찰 기준을 잡별 task-completion 흐름으로 구체화한다:

| 관찰 질문 | 언제 기록 | 무엇을 보는가 |
|---|---|---|
| 이 사용자는 어떤 잡 의도로 들어왔나? | 세션 전 또는 사용 후 1문항 | J1/J2/J3/J4 사전 분류 |
| deed_judged 직후 어떤 행동을 했나? | deed_judged 관측 후 | save / reroll / cap / exit 중 어느 것 |
| J3 사용자: deed_judged 후 종료했을 때 만족해 보였나? | 첫 세션 후 1문항 | 정상 종료(task success) 여부 확인 |
| J1/J2/J4 사용자: deed_saved가 "완료됐다"고 느끼는 지점이었나? | 첫 세션 후 1문항 | task completion perception 확인 |
| deed_save_capped 발생 시: 저장하려 했던 것이 맞나? | 해당 경우에만 | availability 분리 확인 |

관찰은 신규 이벤트·속성·대시보드·세션리플레이 없이 수기로만 진행한다.

## 6. 가정 변경 및 충돌

### 계승한 가정
- J1/J2/J4 first value = `deed_saved`; J3 first value = `deed_judged` (재정의 없음)
- `deed_save_capped` = availability/friction (재정의 없음)
- `deed_rerolled` = 다의적 행동, 불신으로 단정 금지 (재정의 없음)
- 첫 10명은 task-completion rate를 결론으로 내지 않고 행동 패턴 언어만 수집 (재정의 없음)

### 변경한 가정
- 없음. 이 감사표는 기존 first-value mapping을 task-completion 읽기 프레임으로 재번역한 것이다.

### 충돌
- marketing-51 (four-stage handoff)과 충돌 없음: handoff 4구간과 3축 chain은 같은 직선이다.
- marketing-52 (prompt design audit)과 충돌 없음: 이 표는 첫 입력 이후 흐름 읽기, 52는 첫 입력 전 prompt design이다.
- marketing-44 (post-response 30초 audit)과 충돌 없음: 같은 흐름을 task-completion 언어로 재구성한 것이다.

## 7. Next Marketer rules

- deed_judged 발생을 J1/J2/J4 task completion으로 읽지 않는다. AI의 기여가 완료된 시점이다.
- J3 judged→exit는 정상 task success다. 저장을 독촉하거나 이탈로 읽지 않는다.
- deed_save_capped는 task 포기가 아니라 availability 차단이다.
- 첫 10명 관찰에서 "deed_judged 몇 번" 대신 "judged 후 어떤 행동을 선택했나"를 손기록한다.
- 신규 이벤트·속성·tracking·dashboard·session replay·공개 카피·배포·비용·권한 변경 0.

## 8. MARKETING_LEARNINGS.md promotion candidate

"Task completion in AI onboarding is not when the AI acted, but when the user chose to act on what the AI offered." deed_judged는 AI의 기여 완료이고, 사용자의 task completion은 J1/J2/J4에서 deed_saved, J3에서 deed_judged다. 이 프레임은 first-value mapping을 신규 계측 없이 잡별 행동 증거로 보강한다.

## 9. 검증 게이트

- 출처노트 경로 명기: yes (cloud run에서 파일 미존재; intent 본문 rationale로 확인).
- 이벤트명 6개 (add_flow_started, add_flow_abandoned, deed_judged, deed_rerolled, deed_save_capped, deed_saved) — 앵커 변경 0 (인용만).
- 신규 계측/tracking/privacy 변경: 0.
- 공개 카피/코드/배포 변경: 0; 모든 관찰 기준은 내부 proposal-only.
- Conflict marker: 0.
