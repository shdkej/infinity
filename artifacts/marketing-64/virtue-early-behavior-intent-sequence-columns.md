# Virtue Early Behavior Intent Sequence Columns

Status: internal docs proposal, docs-only.  
Date: 2026-06-16 22:00 UTC  
Source note: source/external-links/marketing/2026-06-16-plg-behavioral-intent-signals.md  
Predecessor: marketing-63 (Agent-Readable Analytics Context Card)

## Context

기존 Virtue first-10/activation 관찰 문서는 단일 활성화 이벤트(`deed_saved`, `deed_judged`)를 중심으로 first value 판독을 정의한다. PLG 행동 기반 의도 신호 관점에서 단일 이벤트만으로는 다음이 안 보인다:

- 활성화 이벤트에 **도달하기 전 어떤 행동 흔적**을 남겼는가
- 활성화 이벤트 **직후 어느 방향으로** 갔는가
- 어느 화면에서 **멈추거나 건너뛰었는가**

이 4열 묶음은 신규 이벤트나 tracking 변경 없이 first-10 수기 관찰 노트에 추가할 수 있는 관찰 컬럼을 제안한다.

## Activation Event vs Intent Sequence

| 개념 | 정의 | Virtue 사례 |
|------|------|------------|
| Activation Event | 잡별 first value 도달 이벤트 (단일, 이분법) | J1/J2/J4: `deed_saved` · J3: `deed_judged` |
| Intent Sequence | 활성화 이벤트 전·후의 행동 흔적 (수기 관찰) | 탐색 → 입력 → 대기 → 결과 → 저장/종료 중 어느 단계에서 무엇을 했나 |

Activation event는 "이 사용자가 first value에 도달했는가"를 답한다. Intent sequence는 "이 사용자가 어떻게 도달했는가 / 어디서 멈췄는가"를 답한다.

## Early Behavior Sequence Columns

first-10 수기 관찰 테이블에 추가하는 4열 묶음:

| 열 이름 | 관찰 대상 | 기록 방법 |
|---------|----------|---------|
| `first_feature_explored` | 첫 탐색 기능/화면: `/add` 이전에 어디를 먼저 봤는가? (홈, 과거 deeds, level_up, 통계 등) | 수기 한 줄 |
| `pause_screen` | 멈춘 화면: 어디서 시간을 보냈거나 머뭇거렸는가? | 수기 한 줄 |
| `skipped_action` | 건너뛴 행동: 무엇을 생략하거나 무시했는가? (툴팁, 저장 안내, level_up 확인 등) | 수기 한 줄 (없으면 "없음") |
| `post_save_action` | 저장 후 다음 행동: `deed_saved` 이후 무엇을 했는가? (J1/J2/J4 해당, J3는 선택) | 수기 한 줄 |

### Job별 해석 차이

| Job | 핵심 열 | 해석 주의 |
|-----|---------|----------|
| J1 (기록) | `pause_screen`(입력 전 망설임), `post_save_action` | `first_feature_explored`에서 탐색-first면 J1 확신도 낮음 |
| J2 (누적) | `post_save_action`(저장 후 level_up 확인 여부) | level_up 미확인이 J2 실패는 아님 (첫 세션) |
| J3 (AI 호기심) | `pause_screen`(결과 카드 체류), `skipped_action` | `post_save_action`은 optional (J3 first value = `deed_judged`) |
| J4 (회고) | `first_feature_explored`(과거 deeds 조회 여부), `post_save_action` | 회고 의도 사전 탐색이 J4 신호 |

## How This Extends Existing Docs

| 선행 문서 | 이 제안과의 관계 |
|----------|-----------------|
| marketing-44 (Post-Response Flow) | m44: 결과 직후 30초 관찰. 이 제안: 활성화 이벤트 전/후 전체 trail 추가 |
| marketing-42 (Session Value By Job) | m42: 세션 분류 방법. 이 제안: 분류를 위해 기록할 행동 열 추가 |
| marketing-63 (Agent-Readable Context Card) | m63: 이벤트 해석 계층. 이 제안: 이벤트 외 행동 시퀀스 관찰 열 추가 |
| marketing-47 (First-User Learning Loop) | m47: pre/post 질문. 이 제안: in-session 행동 관찰 열 추가 (질문이 아니라 관찰) |

## Conflict Check

- First Value Mapping (J1/J2/J4=`deed_saved`, J3=`deed_judged`): **충돌 없음** — 이 제안은 그 매핑을 변경하지 않는다
- Prelaunch Decision Boundary: **충돌 없음** — 관찰 결과를 비율/KPI/전환율로 환산하지 않는다
- Traffic Source Before Metrics: **충돌 없음** — 관찰 열에 traffic source/job도 함께 기록 권장
- Measurement Readiness: **충돌 없음** — 이 열들은 metric이 아니라 손기록 관찰이다
- Session Value Is Read By Job: **보완** — job별 first value 도달과 시퀀스를 함께 읽는다

## Inherited Assumptions

1. J1/J2/J4 first value = `deed_saved`, J3 first value = `deed_judged` (MARKETING_LEARNINGS.md 기준)
2. prelaunch first-10 관찰은 수기 중심, 전환율/retention%로 환산하지 않는다
3. synthetic/mock/self-test는 관찰 대상에서 제외·표시한다

## New Learning Candidate

prelaunch first-10 관찰에서 `early_behavior_sequence` 4열 묶음은 단일 활성화 이벤트로 놓치는 의도 신호(탐색 방향, 마찰 위치, 건너뜀 패턴)를 기록하는 데 유용하다. 향후 10명 이상의 관찰 데이터가 쌓이면 MARKETING_LEARNINGS.md에 승격 여부를 검토한다.

## Usage Note

- 신규 이벤트, tracking 속성, dashboard 위젯, privacy 변경: 없음
- 이 열들은 수기 관찰 노트(스프레드시트 또는 MD 표)에만 추가한다
- prelaunch first-10 단계의 소규모 표본에서만 사용하고, activation rate/conversion rate로 환산하지 않는다
- 열 데이터는 "패턴 가설 등록 후보"이지 "행동 증거 확정"이 아니다

## Verification

- 신규 이벤트·tracking·privacy·dashboard·public copy·deploy: 0
- marketing-55~63 충돌: 0
- synthetic/test 및 prelaunch low-signal 금지선 유지: 확인
- source note: 2026-06-16-plg-behavioral-intent-signals.md (source 명시됨)
