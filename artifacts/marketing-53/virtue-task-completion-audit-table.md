# Virtue task-completion audit table

- intent: `marketing-53`
- source_note: `source/external-links/marketing/2026-06-11-ai-onboarding-intent-to-task.md` (local; not accessible from cloud run — referenced by intent)
- scope: docs-only / no public copy change
- status: internal audit
- permission: L1 docs-only

## 0. Purpose

AI 온보딩 연구가 보여주는 핵심: 사용자가 제품에 오는 이유는 "답변을 받는 것"이 아니라 "의도한 작업을 완료하는 것"이다. Virtue의 첫 입력/결과 직후를 이 3단계 프레임으로 읽는다:

1. **사용자 의도** — 사용자가 `/add`에 오는 이유 (어떤 완료를 원하는가)
2. **AI가 수행한 작업** — Virtue의 AI가 실제로 하는 것 (`deed_judged` 반환)
3. **사용자가 선택한 다음 행동** — AI 결과 카드 이후 사용자의 행동 (first value 도착 여부)

이 테이블의 목표:
- `deed_judged` 이벤트 단독으로 "작업 완료"를 판정하는 과대평가 위험을 제거한다.
- J1/J2/J4와 J3의 "작업 완료" 기준이 다름을 잡별 행동 증거로 명확히 한다.
- 신규 이벤트/tracking/계측/코드/배포 없이 기존 이벤트 6개(`deed_judged`, `deed_saved`, `deed_rerolled`, `deed_save_capped`, `add_flow_started`, `level_up_viewed`)로만 읽는다.

변경 없음: 공개 카피, 이벤트, tracking/privacy, dashboard/session replay, 코드, 배포, 외부 발송, 비용, 권한.

## 1. 계승한 기준

| 기준 | 규칙 | 이번 감사에서 사용 |
|---|---|---|
| First Value Mapping | J1/J2/J4 = `deed_saved`; J3 = `deed_judged` | 작업 완료 이벤트 기준으로 그대로 적용 |
| Guided First-Value Is A Four-Stage Handoff | 첫 입력 전 → AI 대기 → 결과 해석 → 저장/종료 | 이번 테이블은 AI 결과 이후(3~4구간) 중심 |
| Post-Response Flow Reveals Value, Not The Result Event | `deed_judged` 발화만으로 가치 전달 확정 금지 | task-completion 3단계 틀의 직접 근거 |
| Session Value Is Read By Job, Not Event Count | 이벤트 수↑를 가치↑로 읽지 않음 | J3 짧은 무저장 세션 = 성공으로 유지 |
| Prelaunch Decision Boundary | 첫 10명·소표본은 방향 재료, 비율/PMF 확정 아님 | 이 감사표도 관찰 기준 제공이 목적 |

## 2. task-completion 3단계 × 잡 매핑

| 잡 | 1단계: 사용자 의도 | 2단계: AI가 수행한 작업 | 3단계: 사용자가 선택한 다음 행동 | 작업 완료 판정 이벤트 | 판정 방법 |
|---|---|---|---|---|---|
| **J1 기록형** | 오늘 한 행동을 작은 기록으로 남기고 싶다 | `deed_judged` 반환 — 점수+해석 카드 표시 | `deed_saved` (카드 저장) | `deed_saved` | `add_flow_started` → `deed_judged` → `deed_saved` 순서 확인 |
| **J2 누적형** | 이 행동이 지금까지의 흐름에 더해지는지 보고 싶다 | `deed_judged` 반환 — 점수+누적 맥락 표시 | `deed_saved` (다음 누적 진행) | `deed_saved` | `add_flow_started` → `deed_judged` → `deed_saved` + `level_up_viewed` 유무 관찰 |
| **J3 AI 호기심형** | AI가 이 행동을 어떻게 보는지 궁금하다 | `deed_judged` 반환 — 점수+해석 카드 표시 | 확인 후 저장 없이 닫기 **(정상 종료)** 또는 `deed_saved` | **`deed_judged`** | `add_flow_started` → `deed_judged` 발화 여부; 저장 없이 종료 = task complete |
| **J4 회고형** | 이 순간을 자기 말로 남겨 나중에 회고하고 싶다 | `deed_judged` 반환 — 점수+해석 카드 표시 | `deed_saved` (회고 맥락으로 저장) | `deed_saved` | `add_flow_started` → `deed_judged` → `deed_saved` 순서 확인 |

## 3. `deed_judged` 과대평가 분류표

이 테이블은 `deed_judged` 이벤트가 발화한 세션을 잡별로 재분류하기 위한 수기 관찰 기준이다.

| 세션 패턴 | J3 판정 | J1/J2/J4 판정 | 라우팅 |
|---|---|---|---|
| `deed_judged` → 저장 없이 종료 | **task complete** (first value = `deed_judged`) | 보류 — 저장 전 이탈 후보 | J3: B-NORMAL, J1/J2/J4: B-LOST or B-NORMAL 분리 필요 |
| `deed_judged` → `deed_saved` | task complete (저장은 선택 범퍼) | **task complete** (first value = `deed_saved`) | 전 잡 완료 |
| `deed_judged` → `deed_rerolled` → `deed_saved` | 더 깊은 탐색 후 완료 | 재시도 후 완료 | 완료; 단 `deed_rerolled` 반복 = 의도 관찰 대상 |
| `deed_judged` → `deed_rerolled` → 저장 없이 종료 | 충분히 탐색 후 종료 (정상) | 보류 — 결과 기대 불일치(B-MISMATCH) 후보 | J3 정상 종료 / J1~4 B-MISMATCH 후보 분리 |
| `deed_judged` → `deed_save_capped` | 가용성/마찰 문제 | 가용성/마찰 문제 | **B-AVAIL (availability/friction), task incomplete** — upgrade demand가 아님 |
| `add_flow_started` → 미`deed_judged` 종료 | 진입 후 조기 이탈 | 진입 후 조기 이탈 | B-LOST(입력 불명확) or B-AVAIL(503/지연) 분리 필요 |

## 4. 잡 신호 없을 때 관찰 방법

초기 사용자는 잡을 명시하지 않는다. 잡 신호가 없을 때 수기 관찰 기준:

| 관찰 포인트 | J1 신호 | J2 신호 | J3 신호 | J4 신호 |
|---|---|---|---|---|
| 첫 입력 내용 | 구체적 행동 기술 ("~했다") | 반복 패턴 기술 ("또 ~했다") | 궁금증/가설 ("~은 어떨까") | 감정/의미 기술 ("~느낀 날") |
| AI 결과 직후 행동 | 빠른 저장 | 저장 + 홈 재방문 | 확인 후 닫기 or reroll | 저장 후 상세 읽기 |
| 저장 없이 닫기 | 보류 후보 | 보류 후보 | **정상 종료** | 보류 후보 |
| 두 번째 세션 | 다른 날 행동 추가 | 연속 행동 추가 | 다른 행동으로 재시험 | 저장 내용 회고 |

## 5. first-user 관찰에서 이 테이블 사용 방법

첫 10명 관찰 시:
1. 세션별로 3단계(`사용자 의도` → `AI 수행` → `다음 행동`)를 손기록한다.
2. "AI가 수행한 작업 = 작업 완료"로 기록하지 않는다. **3단계 다음 행동까지 확인한다.**
3. `deed_judged` 발화 후 다음 행동이 없으면 잡 신호를 먼저 읽는다 (J3 정상 종료 vs J1/2/4 보류).
4. 수기 기록만. 신규 이벤트/속성/tracking/dashboard/session replay 변경 없음.
5. 작업 완료율(%)이나 activation rate로 환산하지 않는다.

## 6. 검증 게이트

- 출처노트 경로: `source/external-links/marketing/2026-06-11-ai-onboarding-intent-to-task.md` (로컬 파일 참조; 클라우드 접근 불가, intent에서 확인 필요)
- 기존 이벤트명 6개 사용: `deed_judged` ✓, `deed_saved` ✓, `deed_rerolled` ✓, `deed_save_capped` ✓, `add_flow_started` ✓, `level_up_viewed` ✓
- 신규 이벤트/속성: 0
- 공개 카피/코드/배포 변경: 0
- 기존 문서(marketing-51 guided-first-value, marketing-52 prompt-design-audit, marketing-47 first-10-script)와 충돌: 0
- conflict marker: 0건

## 7. 변경한 가정과 충돌

### 계승한 기준
- J1/J2/J4 = `deed_saved` first value; J3 = `deed_judged` first value — 변경 없음
- J3 judged-save 갭은 이탈이 아닌 정상 종료 — 변경 없음
- `deed_save_capped`, 503, 지연 = availability/friction (not value or upgrade demand) — 변경 없음

### 변경한 기준
없음. 기존 mapping을 task-completion 3단계 렌즈로 재정리한 것이며 새로운 판단을 추가하지 않는다.

### 충돌
- marketing-51 (guided first-value four-stage): 층이 다름 — m51이 4구간 전체를 다루고 이 테이블은 AI 결과 이후(3~4구간)를 task-completion 언어로 재서술. 충돌 없음.
- marketing-52 (prompt design audit): 층이 다름 — m52가 1구간(첫 입력) 프롬프트를 다루고 이 테이블은 3단계 완료 기준을 다룸. 충돌 없음.
- marketing-47 (first-10 ask script): 층이 다름 — m47이 초대/질문 스크립트를 다루고 이 테이블은 세션 완료 판독 기준을 다룸. 충돌 없음.

## 8. 다음 Marketer 규칙

1. activation 리포트에서 `deed_judged` 수를 "작업 완료" 지표로 단독 사용하지 않는다. 잡 신호와 3단계 다음 행동을 함께 확인한다.
2. J3 세션에서 저장 없이 종료한 사용자를 "이탈/미완료"로 분류하지 않는다.
3. `deed_save_capped`를 "더 쓰고 싶다 = 완료 욕구"로 읽지 않는다. availability/friction 칸으로만 분류한다.
4. 첫 10명 관찰 기록은 이 테이블의 3단계를 기준으로 손기록한다. 비율/통계로 환산하지 않는다.

## 9. MARKETING_LEARNINGS.md 승격 후보

보류 — 이 테이블은 기존 first-value mapping과 post-response-flow 기준의 재정리이다. 단일 실행이고 새로운 empirical claim이 없으므로 report에 보류하고 실제 first-user 관찰 후 learning을 발굴한다.
