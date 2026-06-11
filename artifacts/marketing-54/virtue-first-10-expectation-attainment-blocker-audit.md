# Virtue 첫 10명 스크립트 기대-획득-막힘 루프 감사표

- intent: `marketing-54`
- source_note: `source/external-links/marketing/2026-06-11-onboarding-feedback-loop.md` (로컬 워크스페이스 / GitHub 미동기화)
- scope: docs-only / first-user observation audit
- status: internal audit
- permission: L1 docs-only
- 감사 대상: `artifacts/marketing-47/virtue-first-10-design-user-ask-script.md`

## 0. 목적

prelaunch 첫 사용자 관찰에서 작은 이벤트 숫자보다 "무엇을 기대했고(기대), 얻었고(획득), 무엇이 막았는지(막힘)"가 활성화 해석의 더 안전한 근거다.

기존 `first-10-design-user-ask-script`(marketing-47)가 이 3요소를 잡별(J1~J4)로 충분히 포착하는지 감사하고:
- `deed_judged`/`deed_saved` 숫자 과해석을 줄일 관찰 근거 보강
- 정상 종료 / 혼란 종료 / 가치 미전달 / 이미 충분해서 종료 4가지를 분리할 기준 추가

신규 이벤트, 인앱 서베이, tracking/privacy, 공개 카피, 배포, 외부 발송, 비용 변경 없음.

## 1. 계승 기준

| 기준 | 계승 내용 |
|---|---|
| First Value Mapping | J1/J2/J4 = `deed_saved`, J3 = `deed_judged` |
| Prelaunch Decision Boundary | 첫 10명은 방향 재료, 비율/합격선 아님 |
| First-User Learning Loop | invite → pre → post → 자기 말 기록 (m47 구조 유지) |
| Message Confusion As Evidence | 사용자 언어는 증거이지 결정이 아님 |
| Product Body vs Bumper By Job | 막힘의 성격은 B-LOST/B-MISMATCH/B-AVAIL/B-NORMAL로 분류 |

## 2. 기대-획득-막힘 3요소 정의

| 요소 | 정의 | Virtue 관찰에서 |
|---|---|---|
| 기대 | 사용자가 제품을 시작하기 전에 가진 결과 기대 | §B-2 "왜 이걸 써보려는지" — 잡 신호와 기대 읽기 |
| 획득 | 실제로 first value를 얻었는가 | §C-1 "어, 이거네 싶은 순간이 있었나" — 잡별 first value 도달 확인 |
| 막힘 | 기대와 획득 사이의 장애물 | §C-2 "부담스럽거나 멈칫한 곳" — friction/B-LOST/B-MISMATCH/B-AVAIL |

## 3. 기존 스크립트 대응 감사

### §B-2 기대 읽기

| 잡 | 기대 읽기 항목 | 현재 충족도 | 갭/강화 후보 |
|---|---|---|---|
| J1 기록 | "지금 이걸 써보려는 이유" — 기록을 원하는지 확인 | ✅ 잡 신호·기대를 함께 묻는다 | 기록이 쌓여야 한다는 기대인지(J2 혼재), 지금 당장 남기는 게 기대인지 구분 손기록 추가 가능 |
| J2 누적 | "첫날 한 번, 며칠 쌓이면" 기대 | ✅ J2 초대 문장에 누적 기대 명시 | 첫 세션만으로 "쌓이는 맛"을 얼마나 기대하는지 세분 가능 |
| J3 호기심 | "AI가 어떻게 읽는지 보고 싶다" 기대 | ✅ §B-2가 이 기대를 명시적으로 부름 | J3 기대가 "평가"인지 "AI 읽기"인지 구분 손기록 |
| J4 회고 | "돌아볼 재료를 남기고 싶다" 기대 | ✅ §B-2에서 "지금 이걸 써보려는 이유" | 회고 기대가 즉각적인지 나중인지 시점 구분 추가 가능 |

### §C-1 획득 읽기

| 잡 | first value 도달 확인 | 현재 충족도 | 갭/강화 후보 |
|---|---|---|---|
| J1 | `deed_saved` 후 "어, 이거네" 순간 | ✅ "어, 이거네 싶은 순간"을 묻는다 | 저장 전 결과 화면에서 "이거네" 구분 손기록 추가 |
| J2 | `deed_saved` + `level_up_viewed` 순간 | ⚠️ 첫 세션에서 누적 payoff는 즉시 발화 안 할 수 있음 | 두 번째 저장 이후 확인 필요 |
| J3 | `deed_judged` 화면 도착 | ✅ §C-1이 "어디서였어요"를 묻고, J3에서는 결과 카드가 위치 | 결과 카드 후 "AI가 읽어줬다" 느낌 확인 강화 가능 |
| J4 | `deed_saved` (회고 재료로) | ✅ J1과 동일한 흐름 | "나중에 돌아볼 수 있겠다" 느낌 구분 손기록 추가 가능 |

### §C-2 막힘 읽기

| 잡 | 막힘 유형 | 현재 충족도 | 갭/강화 후보 |
|---|---|---|---|
| J1 | B-LOST: 무엇을 적어야 하는지 모름 / B-MISMATCH: 기록이 남지 않는다는 느낌 | ✅ "멈칫하거나 부담스러운 곳"을 묻는다 | 막힘 성격 4분류 수기 레이블링 칸 추가 가능 |
| J2 | B-LOST: 쌓이는지 모름 / B-MISMATCH: 첫날 저장만으로 부족 | ⚠️ 첫날 §C-2 답이 "없었다"면 J2 막힘이 보이지 않을 수 있음 | 두 번째 세션 후 질문 추가 (proposal-only) |
| J3 | B-AVAIL: 대기 중 불안 / B-MISMATCH: AI 결과가 기대와 다름 | ✅ §C-3에서 평가 불안이 더 잘 잡힌다 | 대기 시간 불안 명시 추가 (proposal-only) |
| J4 | B-LOST: 회고 재료 충분한지 모름 / B-MISMATCH: 저장했지만 돌아볼 것이 없다는 느낌 | ⚠️ J4 특유의 막힘이 현재 질문에서 잘 드러나지 않을 수 있음 | "저장했지만 나중에 돌아볼 만한 것이 생겼다고 느꼈나요?" 손기록 칸 (proposal-only) |

## 4. 기대-획득-막힘 잡별 충족도 요약

| 잡 | 기대 (§B-2) | 획득 (§C-1) | 막힘 (§C-2 + §C-3) | 전체 |
|---|---|---|---|---|
| J1 기록 | ✅ | ✅ | ✅ (B-MISMATCH 구분 강화 가능) | 양호 |
| J2 누적 | ✅ | ⚠️ (첫 세션 이후가 main value) | ⚠️ (두 번째 세션 관찰 없음) | 부분 충족 |
| J3 AI호기심 | ✅ | ✅ | ✅ (평가 불안은 §C-3에서 포착) | 양호 |
| J4 회고 | ✅ | ✅ | ⚠️ (회고 재료 불충분 느낌 명시적 캡처 약함) | 부분 충족 |

## 5. 종료 성격 4분류

| 종료 성격 | 정의 | 스크립트에서 읽는 위치 |
|---|---|---|
| 정상 종료 (B-NORMAL) | 의도한 first value를 얻고 닫음 | §C-1에서 "어, 이거네" 있음 + 막힘 없음 |
| 혼란 종료 (B-LOST) | 무엇을 해야 하는지 몰라서 닫음 | §C-2에서 "멈칫, 길 잃음" 신호 |
| 가치 미전달 (B-MISMATCH) | 기대한 결과와 실제 결과가 달라서 닫음 | §C-1 "어, 이거네" 없음 + §C-2 기대 불일치 |
| 이미 충분해서 종료 (B-DONE) | 원하는 것을 얻었고 더 볼 이유 없음 (J3에서 가장 흔함) | §C-1에서 first value 명확 + §C-2 막힘 없음 + 저장 없이 종료 |

## 6. 기존 스크립트 수정 없이 보완하는 수기 칸 (proposal-only)

| 칸 이름 | 설명 | 허용 값 |
|---|---|---|
| `expectation_type` | 진입 기대의 성격 | record / accumulate / ai_curiosity / retrospective / unclear |
| `attainment_confirmed` | first value 도달 여부 | yes / no / partial |
| `blocker_type` | 막힘 성격 | B-LOST / B-MISMATCH / B-AVAIL / B-NORMAL / B-DONE |
| `exit_character` | 종료 성격 | normal_exit / confused_exit / value_miss / done_no_need |

## 7. 기존 문서와의 보완 관계

| 선행 문서 | 역할 | 이번 문서 추가 | 충돌 |
|---|---|---|---|
| `first-10-design-user-ask-script` (m47) | 초대·질문·기록 루프 전체 | 기대-획득-막힘 3요소 잡별 충족도 감사 + 수기 칸 4개 추가 제안 | 없음 |
| `virtue-guided-first-value-session-audit` (m51) | 4구간 guided break 찾기 | 관찰 결과의 종료 성격 4분류와 연결 | 없음 |
| `virtue-task-completion-audit` (m53) | task-completion 3열 | 막힘 분류(B-LOST/B-MISMATCH/B-AVAIL/B-NORMAL)와 직접 연결 | 없음 |

## 8. 해석 금지선

- J1/J2/J4 first value는 `deed_saved`, J3 first value는 `deed_judged`. 재정의 0.
- J3 저장 없는 종료는 B-DONE 후보이며 가치 미전달로 읽지 않는다.
- `deed_judged`/`deed_saved` 숫자를 기대-획득-막힘 결론으로 환산하지 않는다.
- 막힘 분류 결과를 전환율/retention%/PMF/activation rate로 환산하지 않는다.
- 신규 이벤트·인앱 서베이·tracking/privacy·공개 카피·배포·외부 발송·비용 변경은 모두 approval-needed다.

## 9. 가정 분리

### 계승한 기준
- J1/J2/J4 first value = `deed_saved`; J3 first value = `deed_judged` — 재정의 0.
- 첫 10명은 방향 재료이지 decision-grade 지표가 아니다.
- 막힘은 B-LOST/B-MISMATCH/B-AVAIL/B-NORMAL로 분류하고, 넛지·카피·계측으로 곧바로 연결하지 않는다.

### 변경한 가정
- 없음. J2의 첫 세션 이후 막힘은 현재 스크립트 범위 밖임을 인식하고 "부분 충족"으로 표기하지만, 스크립트를 수정하지는 않는다.

### 충돌
- 없음.

### MARKETING_LEARNINGS.md 승격 후보
- **Expectation-Attainment-Blocker Is A Safer Prelaunch Frame Than Event Counts** — prelaunch 첫 사용자 관찰에서 `deed_judged`/`deed_saved` 숫자보다 "무엇을 기대했고, 얻었고, 무엇이 막았는지"로 먼저 읽어야 한다. 막힘의 성격은 B-LOST/B-MISMATCH/B-AVAIL/B-DONE(J3 정상)으로 분류하고, 종료 성격은 정상·혼란·가치 미전달·이미 충분해서 4칸으로 가른다. J2 첫 세션의 막힘은 누적 second value 이후에야 드러나므로 첫 날 스크립트만으로는 부분 충족이다.

## 10. 검증 게이트

- 소스 노트 경로: 로컬 워크스페이스, GitHub 미동기화 — 경로 확인 부분 통과.
- J1/J2/J4=`deed_saved`, J3=`deed_judged` first-value 매핑 유지: ✅
- 신규 이벤트·인앱 서베이·tracking/privacy·공개 카피·배포·외부 발송·비용: 변경 0.
- Conflict marker: 0건.
