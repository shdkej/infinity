# Virtue first-value path onboarding audit companion

- intent: `marketing-108`
- source note: `/home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-07-18-product-led-onboarding-system.md`
- scope: docs-only / first-10 observation companion
- permission: L1 docs-only
- status: internal companion

## 0. Purpose

Appcues의 제품 주도 온보딩 노트는 온보딩을 툴팁·체크리스트·문구 조합이 아니라 사용자가 자기 목표에서 첫 가치까지 이동하는 제품 내부 시스템으로 본다. Virtue prelaunch에서는 새 UI나 tracking을 만들기보다, 첫 10명 관찰 companion이 그 경로를 제대로 읽는지 확인하는 편이 맞다.

이 companion은 기존 `marketing-47` 첫 10명 ask script와 `marketing-51` guided first-value 감사표 옆에 붙는 수기 감사표다. 신규 이벤트, 속성, tracking, dashboard, session replay, 공개 카피, 배포는 만들지 않는다.

## 1. Inherited Criteria

| 기준 | 계승 내용 | 이번 문서의 적용 |
|---|---|---|
| First Value Mapping | J1/J2/J4 = `deed_saved`, J3 = `deed_judged` | 첫 가치 도달 화면을 잡별로 다르게 기록한다. |
| First-User Learning Loop | 첫 10명은 비율이 아니라 문제 언어와 자기 말 가치로 읽는다. | 표본을 activation rate로 환산하지 않고 경로 판독만 남긴다. |
| Guided First-Value | 첫 입력 전, AI 대기, 결과 해석, 저장/종료 4구간 handoff를 본다. | 가치 직전 막힘을 구간과 성격으로 동시에 기록한다. |
| Product Body vs Bumper | 제품 본체와 범퍼는 잡별로 다르다. | J3에 저장 안내를 first value로 강제하지 않는다. |
| Nudges Default To Show-Nothing | 도움은 B-LOST일 때만 후보가 된다. | 막힘 발견을 곧바로 넛지·카피·계측으로 옮기지 않는다. |

## 2. First-Value Path Audit Table

기존 첫 10명 관찰표나 design-user ask script의 사용자별 행 옆에 아래 칸을 수기로 붙인다. 자동 수집 필드가 아니다.

| 칸 | 적는 값 | 읽는 법 | 금지선 |
|---|---|---|---|
| user_goal_before_session | 사용자가 들어온 이유를 원문으로 적는다. | 기능 목록이 아니라 사용자의 목표에서 경로가 시작되는지 본다. | 목표를 잡 확정이나 세그먼트 결론으로 환산하지 않는다. |
| expected_first_value_by_job | J1/J2/J3/J4와 예상 도착점: J1/J2/J4 `deed_saved`, J3 `deed_judged` | 사용자가 기대한 가치와 Virtue의 잡별 도착점이 맞는지 본다. | 모든 잡을 `deed_judged` 또는 `deed_saved` 하나로 통일하지 않는다. |
| first_value_screen_reached | `/add`, AI 결과 카드, 저장 후 홈, 기록 목록 등 실제 도달 화면 | Appcues 노트의 "첫 가치까지의 시스템" 관점으로 화면들을 한 경로로 묶는다. | 화면 방문을 곧 가치 이해나 activation으로 확정하지 않는다. |
| pre_value_blocker | first_input / ai_wait / result_interpretation / save_or_exit / none + B-LOST/B-MISMATCH/B-AVAIL/B-NORMAL | 가치 직전 막힘이 길 잃음인지, 결과 기대 불일치인지, 가용성인지, 정상 종료인지 분리한다. | 막힘 하나로 retention, PMF, 가격 수요, upgrade demand를 판단하지 않는다. |
| next_action_clarity_quote | "이제 뭐 하면 되는지" 사용자가 말한 문장 원문 | time-to-next-value가 이어졌는지 본다. J3는 멈춰도 됨/한 번 더/저장 선택 언어를 본다. | 다음 행동이 불명확하다고 곧바로 UI 변경, 넛지, 공개 카피로 옮기지 않는다. |
| path_reading | pass / observe / friction / normal_stop | 한 세션의 경로 판독. 다음 관찰을 위한 후보일 뿐이다. | 비율화, 점수화, 성공/실패 판정 금지. |

## 3. Job-Specific Reading Rules

| Job | 목표 시작점 | 첫 가치 도착점 | 다음 행동 명료성 판독 |
|---|---|---|---|
| J1 기록형 | 오늘 한 일을 남기고 싶다. | `deed_saved` 후 기록이 남았다는 확인 | "내일 또 적으면 된다", "저장된 걸 볼 수 있다" 같은 저장 후 언어가 나오면 pass 후보 |
| J2 누적형 | 쌓이는 보상을 보고 싶다. | 첫 `deed_saved`는 누적의 시작점 | "며칠 더 쌓이면 보겠다" 같은 두 번째 가치 언어가 나오면 observe/pass 후보 |
| J3 AI 호기심형 | AI가 내 일을 어떻게 읽는지 보고 싶다. | `deed_judged` 결과 카드 | "여기서 닫아도 됨", "한 번 더 넣어봄", "저장할 수도 있음"이 자연스러우면 normal_stop/pass 후보 |
| J4 회고형 | 나중에 돌아볼 재료를 남기고 싶다. | `deed_saved` 후 회고 재료가 남음 | "나중에 다시 볼 수 있다", "오늘 걸 남겨뒀다" 같은 회고 언어가 나오면 pass 후보 |

## 4. Sample Readings

### J1 기록형 샘플

- user_goal_before_session: "오늘 한 거 하나 남겨보고 싶어요."
- expected_first_value_by_job: J1 / `deed_saved`
- first_value_screen_reached: AI 결과 카드까지 봤지만 저장 전 멈춤
- pre_value_blocker: save_or_exit + B-LOST
- next_action_clarity_quote: "이 점수를 보고 뭘 눌러야 끝난 거예요?"
- path_reading: observe
- 판독: 결과 카드는 통과점이고 J1 first value는 저장 후다. Appcues식으로 보면 기능 안내가 부족한 문제가 아니라 "첫 가치 도착까지의 마지막 행동"이 사용자 목표와 이어지지 않은 상태다. 다만 이 한 건만으로 저장 CTA 변경이나 넛지 발동을 결정하지 않는다.

### J3 AI 호기심형 샘플

- user_goal_before_session: "AI가 이걸 어떻게 보는지 궁금해요."
- expected_first_value_by_job: J3 / `deed_judged`
- first_value_screen_reached: AI 결과 카드
- pre_value_blocker: none + B-NORMAL
- next_action_clarity_quote: "봤으니까 됐고, 다음에 다른 것도 넣어볼 수 있겠네요."
- path_reading: normal_stop
- 판독: 저장 없이 종료해도 J3 경로에서는 first value에 도달했다. 저장 미발화를 이탈이나 가치 부재로 읽지 않는다. 다음 행동은 저장 강요가 아니라 멈춤/재시도/선택 저장이 모두 가능하다는 언어가 자연스러운지 본다.

### J4 회고형 샘플

- user_goal_before_session: "나중에 돌아볼 만한 걸 남기고 싶어요."
- expected_first_value_by_job: J4 / `deed_saved`
- first_value_screen_reached: 저장 후 홈
- pre_value_blocker: none + B-NORMAL
- next_action_clarity_quote: "며칠치가 있으면 나중에 돌아볼 수 있겠네요."
- path_reading: pass
- 판독: 저장 후 홈이 첫 가치 도착점이자 두 번째 가치 예고로 작동했다. 이 경우에도 표본은 비율이 아니라 반복되는 언어 후보로만 남긴다.

## 5. How This Connects To The Appcues Note

- 사용자 목표에서 시작한다: `user_goal_before_session`이 기능 설명보다 먼저 온다.
- 첫 가치 도착점을 분리한다: `first_value_screen_reached`는 가입, 클릭, 튜토리얼 완료가 아니라 잡별 핵심 효용 위치를 적는다.
- 시스템 경로로 본다: `/add`, AI 결과 카드, 저장 후 홈, 종료/재시도 선택을 개별 문구가 아니라 한 first-value path로 묶는다.
- 다음 행동을 확인한다: `next_action_clarity_quote`는 time-to-value 이후 다음 가치로 이어지는 언어가 있는지 본다.
- prelaunch 경계를 지킨다: 모든 값은 수기 관찰이며, 새 계측·대시보드·프로덕션 변경 없이 companion에만 남긴다.

## 6. Approval Boundary

- 허용: 내부 문서, 수기 관찰 칸, synthetic sample reading, 기존 companion 보조.
- 금지: 공개 발송, 프로덕션 카피, UI 변경, 신규 이벤트/속성/tracking/privacy/dashboard/session replay, 배포, 비용, 권한 변경.
- 보류: 반복 관찰에서 같은 blocker가 쌓이면 별도 proposal intent로 다룬다.

## 7. Learning Note

이번 작업은 기존 durable learning을 바꾸지 않는다. 새 후보는 다음과 같이 report에만 보류한다.

> Product-led onboarding audit for Virtue should read first value as a path from user goal to job-specific value screen to pre-value blocker to next-action language. In prelaunch, this is a manual observation companion, not an instrumentation or UI-change trigger.
