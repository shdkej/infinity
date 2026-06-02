# Virtue 잡별 온보딩 체크리스트 감사표

> 작성 기준일: 2026-06-02  
> 범위: prelaunch 내부 문서. 코드·카피·계측·배포·외부발송·비용·권한 변경 0.

## §0 목적 및 범위

이 문서는 Appcues/Supademo/ProductLed의 온보딩 체크리스트 렌즈("체크리스트 = 기능 안내가 아닌 activation event까지의 3~5개 행동 경로")를 Virtue 잡별 내부 감사표로 번역한다.

**번역 핵심:** Virtue는 잡별로 first value가 다르기 때문에, 단일 체크리스트를 붙이면 J3 정상 종료(`deed_judged` 후 저장 없음)를 저장 실패로 오독할 위험이 있다. 체크리스트는 잡별로 분리해야 한다.

**이 문서가 답하는 질문:**

1. 잡별로 체크리스트에 포함할 수 있는 행동(checklist-eligible action)은 무엇인가?
2. 이탈 지점만 돕는 범퍼(product bumper) 후보는 무엇인가?
3. 사용자가 경로 밖으로 나갔을 때 문맥적 대응(contextual fallback)은 무엇인가?
4. 잡 충족을 실패로 오독할 수 있는 항목(do-not-include)은 무엇인가?

**출처:** Appcues/Supademo/ProductLed 온보딩 체크리스트 권고  
(참조 소스노트: `knowledge-lab/source/external-links/marketing/2026-06-02-action-oriented-onboarding-checklists.md`)

## §1 외부 렌즈 → Virtue 번역

| 외부 렌즈 (공통) | Virtue 번역 | 주의 |
|---|---|---|
| 체크리스트 = activation event까지의 3~5 행동 경로 | 잡별 first value(J1/J2/J4=`deed_saved`, J3=`deed_judged`)가 체크리스트 종착점 | J3는 `deed_saved` 종착점으로 설정하면 정상 종료를 실패로 오독 |
| 체크리스트 항목 = 동사-목적어 형식 (행동형) | 화면(S1~S4) 기반 행동을 동사-목적어로 표현 | "AI 채점 기능 알아보기" 같은 기능 설명형 항목 금지 |
| 범퍼 = 이탈 지점만 | 막힘 4분류(B-LOST/B-MISMATCH/B-AVAIL/B-NORMAL) 중 B-LOST에만 범퍼 | J3의 판정 후 비저장 종료 = B-NORMAL, 범퍼 없음 |
| 문맥적 fallback = 경로 이탈 시 비강요 복귀 | 잡별 첫 가치 미도달 시 낮은 압력 메시지 | 저장 강요 또는 AI 채점 강요 금지 |

## §2 심장표 — J1~J4 × 체크리스트 4항목

> **계승:** first value 매핑(J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106)은 `marketing-06`, `marketing-31`, `marketing-33` 기준 그대로 계승. 재정의 0.  
> **이벤트 화이트리스트:** `add_flow_started`:72 / `deed_judged`:106 / `deed_rerolled`:149 / `deed_save_capped`:167 / `deed_saved`:183 / `level_up_viewed`:199 — 기존 6 발화 이벤트만 인용, 신규 이벤트 0.

| 잡 | Activation event | Checklist-eligible actions | Product bumper 후보 | Contextual fallback | Do-not-include |
|---|---|---|---|---|---|
| **J1 기록형** | `deed_saved`:183 | ① `/` 홈 방문 → ② `/add` 진입 (`add_flow_started`:72) → ③ 덕행 입력 → ④ 저장 (`deed_saved`:183) ← activation | S3→S4 전환: 결과 확인 후 저장 망설임 → 낮은 압력 안내 (proposal-only) | `add_flow_started` 후 이탈 → "언제든 기록할 수 있어요" (비강요) | `deed_judged` 체크 항목 추가 금지 (J3 혼합); `deed_save_capped` 저장 실패 취급 금지 |
| **J2 누적형** | `deed_saved`:183 (1st) | ① `/` 홈 방문 → ② `/add` 진입 (`add_flow_started`:72) → ③ 덕행 입력 → ④ 첫 저장 (`deed_saved`:183) ← activation | 홈 빈 상태: J2 누적 약속 선제 안내 (proposal-only) | 첫 저장 후 홈 복귀 시 누적 수치 없음 → "첫 기록이 남았어요" (도달 확인) | `level_up_viewed` 단독 activation 선언 금지 (두 번째 저장 필요); 첫 저장 전 payoff 강조 금지 |
| **J3 AI 호기심형** | `deed_judged`:106 | ① `/add` 진입 (`add_flow_started`:72) → ② 덕행 입력 → ③ AI 채점 트리거 → ④ 결과 카드 확인 (`deed_judged`:106) ← activation | AI 채점 전 입력 망설임 → 채점 기준 안내 (proposal-only) | `deed_judged` 후 저장 없이 닫힘 → **아무것도 하지 않는다** (J3 정상 종료) | **`deed_saved`를 J3 종착점으로 추가 금지**; `judged−saved` 갭을 이탈 표시 금지; J1/J2/J4와 동일 저장 완료 게이트 금지 |
| **J4 회고형** | `deed_saved`:183 | ① `/` 홈 방문 → ② `/add` 진입 (`add_flow_started`:72) → ③ 과거 덕행 입력 → ④ 저장 (`deed_saved`:183) ← activation | S2: 과거 기억 입력 망설임 → "오래된 일도 기록할 수 있어요" (proposal-only) | 저장 망설임 → "기록은 나만 볼 수 있어요" (비강요) | J3와 동일 체크리스트 사용 금지 (J4=`deed_saved` first value); AI 판정 결과에 과도한 기댓값 설정 금지 |

## §3 잡별 체크리스트 설계 제약

### J3 특별 제약 (단일 체크리스트 위험의 핵심)

J3 체크리스트를 설계하거나 J3 사용자 관찰에 체크리스트를 적용할 때 반드시 지켜야 할 제약:

1. **종착점은 `deed_judged`다.** 마지막 체크 항목은 "결과 카드 확인" 또는 "AI 판정 결과 보기"로 끝난다.
2. **`deed_saved`는 J3 체크리스트에 포함하지 않는다.** 저장은 J3에서 선택이며, 저장 없이 닫아도 first value 달성이다.
3. **`deed_rerolled`:149 재시도는 deep engagement 신호이지 체크리스트 필수 항목이 아니다.** 선택 사항으로만 언급 가능.
4. **J3 fallback은 저장 유도가 아니다.** `deed_judged` 후 비저장 종료는 범퍼나 fallback 없이 그냥 닫히는 것이 올바른 경험이다.

### J1/J2/J4 공통 제약

1. `deed_save_capped`:167은 30덕 상한 early-return이다. 체크리스트에서 저장 성공/실패 게이트로 쓰지 않는다.
2. `level_up_viewed`:199는 J2의 depth signal이지 J1/J4의 체크리스트 항목이 아니다.
3. 저장 강요 범퍼는 J3 흐름을 방해한다. 범퍼 위치는 B-LOST(길 잃음) 지점만 선택한다.

### 범퍼 위치 선택 기준

이 표는 `marketing-31` product-body-vs-bumper 4분류를 체크리스트 맥락으로 재적용한 것이다.

| 막힘 분류 | 체크리스트 연결 | 범퍼 여부 |
|---|---|---|
| B-LOST (길 잃음) | `/add` 진입 전 CTA를 못 찾는 경우 | 범퍼 O (안내) |
| B-MISMATCH (결과 불일치) | 결과 카드가 기대와 다른 경우 | 제품 약속/결과 수정 대상 (범퍼 아님) |
| B-AVAIL (가용성) | 503, 지연, `deed_save_capped` | 가용성 문제 처리 (범퍼 아님) |
| B-NORMAL (정상 종료) | J3 비저장 종료 | 아무것도 하지 않음 (범퍼 없음) |

## §4 첫 검증 게이트

첫 10~20명 관찰 시 이 체크리스트 표의 유효성 확인 항목:

1. 각 잡별로 체크리스트 종착점이 올바른가 (J3 사용자가 `deed_saved` 없이도 완료 판정되는가)
2. 각 범퍼 후보가 B-LOST 지점에서만 발동하는가 (B-NORMAL에서 범퍼 발동 금지)
3. `deed_save_capped` 발생 시 체크리스트에서 "저장 실패"로 표시하지 않는가
4. 잡 판별 없이 단일 체크리스트를 모든 사용자에게 적용하지 않는가

**관찰 기록 방법:** 기존 `first-60-second-value-observation-script.md` (marketing-20) 양식 재사용, 신규 표·컬럼 0.

## §5 prelaunch 금지선

- 이 문서의 체크리스트 후보는 **proposal-only**다. 실제 UI 구현·배포·외부발송 금지
- 범퍼 후보는 관찰 후 별도 Intent로 구현 검토
- 전환율, completion rate, activation %, retention, PMF/벤치마크 결론 도출 금지
- 1명 관찰로 체크리스트 유효성 단정 금지
- synthetic/mock/self-test 세션에서 체크리스트 경로 검증 금지
- `deed_save_capped` → 유료화 신호 환산 금지 (availability/friction)
- 신규 이벤트·속성·카피·계측·대시보드·세션리플레이·배포 0

## §6 계승·변경·충돌·다음 Marketer

### 계승한 기준

1. **First Value Mapping** (MARKETING_LEARNINGS.md §First Value Mapping): J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106. 재정의 0.
2. **Product Body vs Bumper By Job** (marketing-31): 막힘 4분류 라우팅. B-NORMAL에는 범퍼 없음. J3 비저장 = B-NORMAL.
3. **Prelaunch Decision Boundary** (MARKETING_LEARNINGS.md §Prelaunch Decision Boundary): 소표본은 방향 재료이지 결정 지표 아님.

### 이번에 새로 배운 것

- 단일 체크리스트의 가장 큰 위험은 `deed_saved`를 universal activation gate로 두는 것이다.
- J3 체크리스트는 `deed_judged` 종착점을 명시하지 않으면, 관찰자가 비저장 종료를 "체크리스트 미완성"으로 잘못 읽는다.
- 범퍼 후보와 체크리스트 항목을 동일시하면, B-NORMAL 지점에도 범퍼를 붙이는 오류가 생긴다.

### 다음 Marketer에게 넘길 규칙

1. 체크리스트를 관찰 도구로 쓸 때는 잡 판별이 선행해야 한다 (traffic source 분류와 동일 원칙).
2. J3 관찰에서 "체크리스트 완료 = `deed_judged` 확인"이고, 저장 없음은 실패 판정이 아니다.
3. 범퍼 구현 전에 B-LOST vs B-NORMAL 분류를 먼저 확인한다.

### 충돌 확인

| 선행 문서 | 관련 내용 | 충돌 여부 |
|---|---|---|
| activation-candidate-registry.md (marketing-33) | first value 매핑, 잡별 묶음, window 정의 | 충돌 0 |
| product-body-vs-bumper-boundary-table.md (marketing-31) | 막힘 4분류, B-NORMAL 범퍼 금지 | 충돌 0 |
| first-session-jtbd-matrix.md (marketing-06) | J1~J4 first value 정의 | 충돌 0 |
| onboarding-metrics-reading-table.md (marketing-23) | activation event, drop-off 해석 주의 | 충돌 0 |
| first-session-friction-observation-protocol.md (marketing-17) | 마찰 태그 F-시리즈 | 충돌 0 |

### Durable learning 후보

**"Job-Split Checklist Gate"**: 온보딩 체크리스트의 종착점은 잡별로 다르다. 단일 저장 게이트는 J3 정상 종료를 실패로 오독한다. 체크리스트를 설계·적용하기 전에 잡별 first value 매핑으로 종착점을 분리해야 한다.

→ 이번 단독 문서이므로 다음 관찰 적용 후 확인이 필요하다. MARKETING_LEARNINGS.md 승격은 실제 관찰 후 판단.
