# Virtue Early Behavior Intent Sequence Columns

Status: docs-only proposal, internal. 신규 이벤트·속성·tracking/privacy·dashboard·공개 카피·배포 없음.
Date: 2026-06-17
Source note: `../../source/external-links/marketing/2026-06-16-plg-behavioral-intent-signals.md`
Predecessor: `marketing-63` (Virtue Agent-Readable Analytics Context Card)

## Purpose

Mixpanel 2026 PLG 행동 기반 의도 신호 렌즈를 Virtue prelaunch first-10 관찰 문맥으로 번역한다. 핵심 기여는 두 가지다:

1. **Activation event vs intent sequence** 구분을 기존 first-10/activation 관찰 문서에 추가
2. **early_behavior_sequence** 컬럼 묶음(4개)을 prelaunch 수기 관찰 양식 후보로 제안

신규 이벤트·속성·tracking/privacy·dashboard·공개 카피·배포 없음. 기존 marketing-55~63 activation 문서와 충돌 없음.

## 1. Activation Event vs Intent Sequence

### 기존 프레임 (single-event)

현재 Virtue 측정 문맥은 activation을 잡별 단일 이벤트로 읽는다:
- J1/J2/J4: `deed_saved` → activation
- J3: `deed_judged` → activation

이 방식은 **Measurement Readiness Is A Separate Gate** 전제로 맞고, launch-before/launch-after 경계도 유지한다.

### 추가 프레임 (intent sequence)

single-event 기록만으로는 activation 이벤트가 발화했지만 사용자의 의도나 마찰을 읽기 어려울 때가 있다.

Intent sequence는 single-event를 *대체*하지 않는다. 수기 관찰 맥락에서 **왜 그 이벤트에 도달했고, 어떤 경로를 거쳤는가**를 추가로 읽는 보조 렌즈다.

| 프레임 | 용도 | Virtue 적용 |
| --- | --- | --- |
| **activation event** | 잡별 first value 도달 판정 (계측 기반, 변경 없음) | J1/J2/J4=`deed_saved`, J3=`deed_judged` (고정) |
| **intent sequence** | 수기 관찰에서 경로·의도·마찰 읽기 (손기록 전용) | first-10 세션 손기록 보조 컬럼 4개 |

intent sequence는 새 이벤트가 아니라 **수기 관찰 양식의 보조 컬럼**이다. 계측 변경 없음.

## 2. Early Behavior Sequence Columns (수기 관찰 후보)

prelaunch first-10 수기 관찰에 추가할 수 있는 컬럼 4개. 신규 이벤트·속성·tracking이 아닌 수기 기입 메모 칸이다.

### Column 1: 첫 탐색 기능 (first_explored_feature)

| 항목 | 내용 |
| --- | --- |
| 질문 | 사용자가 `/add` 이전에 먼저 탐색한 UI 영역은 무엇인가? |
| 관찰 방법 | 수기 기록, 화면 관찰 |
| J별 해석 | J1/J2/J4는 홈/저장 영역 먼저 탐색이 정상. J3는 `/add` 직진이 정상(AI 판단 확인 목적). |
| 주의 | 탐색 순서를 점수·KPI·activation rate로 환산하지 않는다. |

### Column 2: 멈춘 화면 (stopped_at_screen)

| 항목 | 내용 |
| --- | --- |
| 질문 | 사용자가 처음 멈추거나 가장 오래 머문 화면은 무엇인가? |
| 관찰 방법 | 수기 기록, 화면 관찰 |
| J별 해석 | `/add` 입력 화면에서 멈춤 → B-LOST(길 잃음) 후보. 결과 카드 후 멈춤 → B-MISMATCH 또는 J3 정상 종료 후보. 홈에서 멈춤 → 탐색 중. |
| 주의 | B-LOST와 B-NORMAL(J3 정상 종료)를 구분하지 않으면 불필요한 넛지를 추가하게 된다. (Nudges Are Event-Triggered, And Show-Nothing Is The Default) |

### Column 3: 건너뛴 행동 (skipped_actions)

| 항목 | 내용 |
| --- | --- |
| 질문 | 사용자가 예상 경로 중 건너뛰거나 무시한 단계는 무엇인가? |
| 관찰 방법 | 수기 기록 |
| J별 해석 | J3가 저장을 건너뜀 → 정상 종료(J3 first value는 `deed_judged`). J1/J2/J4가 저장을 건너뜀 → B-LOST 또는 B-MISMATCH 후보. |
| 주의 | 건너뜀 자체를 이탈·불신·마찰로 단정하지 않는다. (Session Value Is Read By Job, Not Event Count) |

### Column 4: 저장 후 다음 행동 (post_save_next_action)

| 항목 | 내용 |
| --- | --- |
| 질문 | 첫 `deed_saved` 또는 `deed_judged` 이후 사용자가 바로 한 행동은 무엇인가? |
| 관찰 방법 | 수기 기록, first value 직후 30초 손기록 |
| J별 해석 | 종료 → 정상 종료 후보. 재방문(`/add` 재시작) → J2 second value 후보. 저장 확인(홈 이동) → J4 reflection 후보. 결과 탐색 → J3 정상. |
| 주의 | `post_save_next_action`을 PQL·유료화 신호·retention%로 환산하지 않는다. (PQL Is A Bundle, Not A Single Event) |

## 3. 기존 activation 문서와의 위치

이 제안이 기존 문서와 충돌하지 않는 이유:

- **marketing-55~63**: 각 activation 이벤트 해석·측정 가능성·기준선 정의 유지. 이 컬럼들은 수기 관찰 보조이며 계측 기준을 바꾸지 않는다.
- **marketing-63 (context card)**: 고정 이벤트 어휘(`deed_judged`/`deed_saved`/`deed_rerolled`/`deed_save_capped`) 유지. intent sequence는 새 이벤트가 아닌 수기 관찰 컬럼이다.
- **Measurement Readiness Is A Separate Gate**: 측정 가능성 게이트를 통과하지 못하면 이 컬럼들로 대체하지 않는다.
- **Traffic Source Before Metrics**: 이 컬럼 기록 전 synthetic/mock/self-test 분리 규칙 그대로 적용.

## 4. 사용 방법 요약

```
prelaunch first-10 수기 관찰 시트에 아래 보조 컬럼 추가:
- [ ] first_explored_feature: ___
- [ ] stopped_at_screen: ___
- [ ] skipped_actions: ___
- [ ] post_save_next_action: ___

activation event는 기존 기준 그대로:
- J1/J2/J4 = deed_saved 발화 여부
- J3 = deed_judged 발화 여부
```

## Verification

- Source note: `../../source/external-links/marketing/2026-06-16-plg-behavioral-intent-signals.md` ✓
- 신규 이벤트·속성: 0
- tracking/privacy/dashboard/public copy/deploy 변경: 0
- synthetic/test 금지선: 유지 (Traffic Source Before Metrics)
- prelaunch low-signal 금지선: 유지 (Prelaunch Decision Boundary)
- 기존 marketing-55~63 activation 문서 충돌: 0
- 기존 MARKETING_LEARNINGS.md 기준 상충: 0
- conflict markers: 0

## Inherited Bases

- **First Value Mapping** — J1/J2/J4=`deed_saved`, J3=`deed_judged` 고정값 유지
- **Session Value Is Read By Job, Not Event Count** — 컬럼 해석에서 이벤트 수 → 가치 오독 방지
- **Post-Response Flow Reveals Value, Not The Result Event** — column 4 관찰 프레임
- **Nudges Are Event-Triggered, And Show-Nothing Is The Default** — 멈춘 화면에서 B-LOST만 넛지 후보
- **Prelaunch Decision Boundary** — 컬럼 관찰값을 비율·임계값으로 환산하지 않음
- **Traffic Source Before Metrics** — 컬럼 기록 전 synthetic/mock 분리

## New Learning Candidate (보류)

**Intent Sequence Supplements, Not Replaces, Activation Events**
- activation event(계측)와 intent sequence(수기 관찰)는 같은 층이 아니라 다른 용도다. 계측 기반 activation event는 고정하고, 수기 관찰 컬럼은 why/how를 읽는 보조다.
- 이번 artifact만으로는 반복 사례가 부족. 실제 first-10 관찰 후 사례가 쌓이면 MARKETING_LEARNINGS.md 승격 후보.
