# Virtue 잡별 온보딩 체크리스트 감사표

> **용도**: 출시 전 내부 참조용. 체크리스트 항목을 잡별로 분리해 첫 10~20명 관찰 시 "어디서 길을 잃었는가"를 명확히 판독한다.
> **관련 문서**: first-session-jtbd-matrix.md · activation-candidate-registry.md · product-body-vs-bumper-boundary-table.md · first-input-defaults-prompt-audit.md
> **금지**: 이 문서를 UI/코드/카피/계측에 즉시 반영하지 않는다. 관찰 후 별도 Intent로 처리.

---

## §0 출처 해석

Appcues, Supademo, ProductLed가 공통으로 권고하는 온보딩 체크리스트 원칙:
- 체크리스트는 **기능 안내**가 아니라 **activation event까지의 3~5개 행동 경로**로 제한한다
- 항목 수가 많을수록 완료율이 낮아지고 사용자가 체크리스트 자체를 목표로 삼는 역효과가 생긴다
- 각 항목은 "이 행동을 하면 무엇이 생기는가"를 체험하는 단계로 표현한다 (기능 설명 나열 금지)
- 체크리스트는 제품 본체의 보조 범퍼이지 본체 자체가 아니다 (product-body-vs-bumper-boundary-table 계승)

**Virtue 적용 주의점**:
- J1/J2/J4 first value = `deed_saved`:183 / J3 first value = `deed_judged`:106
- J3는 `deed_judged` 후 `deed_saved` 없이 세션을 닫는 것이 **정상 종료**
- 단일 체크리스트를 쓰면 J3 정상 종료를 "저장 실패·미완료"로 잘못 읽을 위험이 있다
- 따라서 체크리스트 항목·완료 기준·범퍼를 잡별로 분리해야 한다

---

## §1 정의

| 용어 | 정의 |
|------|------|
| **Checklist-eligible action** | 사용자가 스스로 완료했다고 알 수 있고 activation event에 직결된 행동. 기능 소개나 설정이 아니라 잡별 first value까지의 경로 단계. |
| **Product bumper** | 특정 행동을 유도하거나 이탈을 막기 위해 배치한 제품 표면 요소 (CTA, 빈 상태 메시지, 후속 화면 전환). 체크리스트 자체가 bumper가 될 수 있다. |
| **Contextual fallback** | 사용자가 막혔을 때 제품이 제공하는 보조 경로 (재시도 버튼, 안내 힌트, 잡 전환 제안 등). |
| **Do-not-include** | 이 잡의 체크리스트에 넣으면 잘못된 완료 신호·다른 잡 흐름 침범·정상 종료를 이탈로 오독하게 만드는 항목. |

**3~5개 제한 원칙**: 체크리스트 항목은 최대 5개. J3는 4단계(진입→입력→AI 요청→결과 확인), J1/J4는 4단계(진입→입력→결과→저장), J2는 첫 세션 3단계 + 재방문 단계를 별도 표기.

---

## §2 잡별 온보딩 체크리스트 감사표 (핵심)

인용 이벤트: `add_flow_started`:72 / `deed_judged`:106 / `deed_rerolled`:149 / `deed_save_capped`:167 / `deed_saved`:183 / `level_up_viewed`:199
신규 이벤트·속성·카피·계측 0. 기존 이벤트만 사용.

| 잡 | 첫 약속 | Checklist-eligible actions (최대 5단계, 순서 있음) | Product bumper 후보 | Contextual fallback | Do-not-include |
|----|--------|--------------------------------------------------|-------------------|-------------------|---------------|
| **J1** 기록형 | 오늘 한 덕행을 저장해 기록으로 남긴다 | ① `/add` 진입 (`add_flow_started`:72) → ② 덕행 메모 입력 → ③ AI 결과 카드 확인 (`deed_judged`:106) → ④ **저장 완료** (`deed_saved`:183) | 저장 후 홈 복귀 CTA; 빈 상태 홈 "첫 덕행을 기록해보세요"; 결과 카드 아래 저장 버튼 강조 | 저장 전 이탈 감지 시 "저장하면 기록에 남아요" 힌트 (B-LOST 라우팅) | 재판정(`deed_rerolled`:149)을 필수 단계로 포함하지 않음; `deed_save_capped`:167을 완료 기준으로 쓰지 않음; J3 체크리스트 항목(`deed_judged` 단독 완료) 적용 금지 |
| **J2** 누적형 | 꾸준히 쌓아 레벨업·성장을 확인한다 | ① `/add` 진입 → ② 덕행 입력 → ③ **저장 완료** (`deed_saved`:183) ▸ (재방문 후) ④ 두 번째 저장 → ⑤ 누적 payoff 확인 (`level_up_viewed`:199) | 저장 후 홈 누적 현황 표시; 레벨업 시 축하 화면; 다음 방문 동기 부여 빈 상태 카피 | 첫 저장 후 "다음에도 기록하면 레벨이 올라요" 힌트 (재방문 유도) | `level_up_viewed`:199를 첫 세션 필수 완료 항목으로 포함하지 않음 (두 번째 이상 세션에서 가능); 첫 세션에서 누적 payoff를 성공 지표로 읽지 않음 |
| **J3** AI 호기심형 | AI가 내 덕행을 어떻게 평가하는지 본다 | ① `/add` 진입 (`add_flow_started`:72) → ② 덕행 입력 → ③ AI 판정 요청 (채점 버튼) → ④ **결과 카드 확인** (`deed_judged`:106) | 결과 카드 자체가 본체; 재판정 버튼 (`deed_rerolled`:149 최대 3회); AI 채점 대기 중 소요 시간 힌트 | 결과 카드 이해 안 됨(B-MISMATCH): 점수·코멘트 부연 설명; 재판정 권유 | **`deed_saved`를 J3 체크리스트 완료 기준으로 포함하지 않음**; 저장 없이 닫힘=정상(B-NORMAL), 미완료 표시 금지; "저장해야 완료"라는 범퍼 자동 삽입 금지; judged−saved 갭을 이탈·가치 부재로 기록하지 않음 |
| **J4** 회고형 | 지난 덕행을 돌아보며 의미를 정리한다 | ① `/add` 진입 (`add_flow_started`:72) → ② 덕행 입력 (과거 회고 내용) → ③ AI 결과 확인 (`deed_judged`:106) → ④ **저장 완료** (`deed_saved`:183) → ⑤ 홈에서 기록 목록 확인 | 저장 후 홈 복귀; 이전 기록 목록 노출; "오늘의 회고를 저장해두세요" 힌트 | 저장 전 이탈 시 "기록으로 남겨두면 나중에 볼 수 있어요" 힌트 | `deed_rerolled`:149를 J4 필수 단계로 포함하지 않음; AI 평가 집중 카피를 J4 체크리스트 최종 단계로 설정하지 않음; `deed_save_capped`:167을 저장 완료로 읽지 않음 |

---

## §3 잡별 경계 해설

### J3 특별 경계 (핵심 — 이 표의 존재 이유)

J3 activation event = `deed_judged`:106.

| 상황 | 해석 |
|------|------|
| `deed_judged` 후 저장 없이 세션 종료 | **정상 종료 (B-NORMAL)** — 체크리스트 완료로 기록 |
| `deed_judged` 후 `deed_saved` 있음 | 추가 행동 (선택), 완료 기준 밖 |
| `deed_judged` 없이 세션 종료 | 이탈 후보 (B-LOST 또는 B-AVAIL 분류 필요) |

**단일 "저장" 기준 체크리스트를 J3에 적용하면**:
- 정상 종료 사용자에게 잘못된 "미완료" 상태 표시 → 불필요한 nudge 발생
- J3 정상 사용자가 저장을 강요받는다고 느낄 수 있음
- 관찰 데이터에서 J3 "완료율"이 0에 가깝게 나와 활성화 실패로 오독될 위험

### J1/J2/J4 vs J3 분기 요약

| | J1 기록형 | J2 누적형 | J3 AI 호기심형 | J4 회고형 |
|--|----------|----------|--------------|----------|
| **체크리스트 완료 기준** | `deed_saved` | `deed_saved` | `deed_judged` | `deed_saved` |
| **저장 범퍼 적합성** | 적합 (B-LOST 시) | 적합 (B-LOST 시) | **부적합** (정상 종료 방해) | 적합 (B-LOST 시) |
| **재판정 bumper** | 불필요 | 불필요 | 적합 (호기심 강화) | 불필요 |
| **레벨업 bumper** | 비적합 (첫 세션) | 재방문 후 적합 | 비적합 | 비적합 |

### 막힘 분류 라우팅 (product-body-vs-bumper 계승)

체크리스트 미완료 원인을 무조건 "bumper 추가"로 해결하지 않는다.

1. **B-LOST (길을 잃음)**: 범퍼 후보 → 잡별 contextual fallback 적용
2. **B-MISMATCH (기대 불일치)**: 제품 약속·결과 화면 문제 → 별도 Intent
3. **B-AVAIL (가용성 차단)**: 503·지연·`deed_save_capped`:167 → 가용성 이슈, bumper 아님
4. **B-NORMAL (정상 종료)**: 이탈 아님 → 체크리스트 완료로 기록 (J3에서 자주 발생)

---

## §4 관찰 기준 (prelaunch 손기록)

첫 10~20명 관찰 시 이 표 사용법:
1. 유입 문장·traffic source로 잡(J1~J4)을 먼저 분류한다 (판독에 앞서 분류 선행)
2. 잡별 체크리스트 도달 여부를 손기록한다 (완료/미완료/분류 불명)
3. **J3에서 `deed_judged` 후 저장 없이 종료 → "완료"로 기록**
4. 미완료는 B-분류(LOST/MISMATCH/AVAIL/NORMAL) 중 하나로 먼저 구분
5. 체크리스트 완료율을 activation rate, 전환율, 리텐션으로 환산하지 않음

**관찰 손기록 칸** (기존 baseline template 재사용 + 아래 칸 추가):
- `잡 분류 (J1~J4)` / `체크리스트 완료 여부 (완료/미완료)` / `미완료 원인 (B-코드)` / `J3 정상 종료 여부`

---

## §5 Proposal-Only (관찰 후 별도 Intent로 처리)

이 문서에서 제안만 하며, 반영·구현 0:
- 잡별 분기 체크리스트 UI 구현
- J3 전용 "AI 결과를 보셨나요?" 완료 CTA
- 잡 감지 로직 (J1~J4 자동 분류)
- 체크리스트 완료율 계측 이벤트 추가
- 사용자에게 체크리스트 노출 여부 A/B 테스트
- 체크리스트 항목별 카피 확정

---

## §6 계승·변경·충돌·승격

### 계승한 기준

1. **First Value Mapping**: J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106 (marketing-06, 21, 31, 33 계승)
2. **Product Body vs Bumper By Job**: 체크리스트는 bumper이며 본체(first value)가 없으면 범퍼로 못 가림; J3에 저장 유도 범퍼를 자동으로 붙이면 첫 가치 흐름 방해 (marketing-31 계승)
3. **Prelaunch Decision Boundary**: 체크리스트 완료율을 activation/PMF 지표로 읽지 않음 (marketing-08, 23, 34 계승)
4. **Traffic Source Before Metrics**: 잡 분류가 판독에 선행 (marketing-25 계승)

### 이번에 새로 배운 것

- 단일 체크리스트가 잡별로 다른 activation event(deed_judged vs deed_saved)를 무시하면 J3 정상 종료를 이탈로 오독할 구조적 위험이 있다.
- 체크리스트 완료 기준은 잡별 activation event와 1:1 대응해야 한다. J3의 최종 항목은 `deed_judged`(결과 확인)이며 `deed_saved`는 체크리스트 항목에서 제외하거나 선택 표기해야 한다.
- J2의 경우 레벨업 등 누적 payoff는 첫 세션 체크리스트 항목이 아니라 재방문 후 단계로 분리해야 한다.

### 다음 Marketer에게 넘길 규칙

- **J3 체크리스트의 완료 기준은 `deed_judged`이며 `deed_saved`는 포함하지 않는다.** 저장 없이 닫힘은 B-NORMAL(정상 종료)로 기록한다.
- 체크리스트 설계 전에 반드시 잡별 activation event를 확인하고, 단일 "저장" 기준을 J3에 적용하지 않는다.
- 체크리스트 항목 수는 3~5개로 제한하며 기능 소개가 아닌 activation 경로 단계로 표현한다.
- 체크리스트는 bumper이므로 본체(first value 화면/경로)가 약하면 범퍼로 못 가린다 — 본체 강화가 우선.

### 선행 문서 충돌 확인

- first-session-jtbd-matrix.md: 충돌 0 (J1~J4 first value 계승, 재정의 0)
- activation-candidate-registry.md: 충돌 0 (J3 activation bundle=deed_judged 계승)
- product-body-vs-bumper-boundary-table.md: 충돌 0 (J3 저장 bumper≠본체 원칙 계승, B-분류 계승)
- first-input-defaults-prompt-audit.md: 충돌 0 (J3 deed_judged 후 저장 강요 금지 계승)
- copy-spec 금지어: 신규 공개 카피 0 (메타 문서 내 예시만)

### Durable Learning 후보

"체크리스트 완료 기준은 잡별 activation event와 1:1 대응해야 한다. J3(AI 호기심형)의 체크리스트 완료 기준은 deed_judged이고, deed_saved 없이 닫힘은 정상 종료(B-NORMAL)이다." — marketing-35 단일 사례이므로 이번에는 report 내 보류. 실사용 관찰 후 MARKETING_LEARNINGS.md 승격 재검토.

---

## 금지선 (prelaunch 절대 금지)

- 체크리스트 완료율을 activation rate, PMF, 전환율, 리텐션, 벤치마크로 환산하지 않음
- J3에서 `deed_judged` 후 저장 없는 종료를 "체크리스트 미완료"·"이탈"로 기록하지 않음
- `deed_save_capped`:167은 availability/friction이며 체크리스트 완료 실패로 읽지 않음
- synthetic/mock/self-test 세션의 체크리스트 완료를 사람 사용자 증거로 섞지 않음
- 신규 이벤트, 속성, 카피, 계측, 대시보드, 세션리플레이, 배포, 외부발송, 비용, 권한, 개인정보 변경 0
- 체크리스트 항목을 즉시 제품 UI/코드에 구현하지 않음 (관찰 후 별도 Intent 처리)
- 잡 분류 없이 activation rate/drop-off를 단일 수치로 합산하지 않음
