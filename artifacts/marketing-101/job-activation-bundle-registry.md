# Virtue 잡별 Activation 후보 묶음 레지스트리

> marketing-101 산출물 · 2026-07-06

## 이 레지스트리의 목적

Virtue prelaunch 저신호 환경에서 J1-J4 잡별 activation 판정을 단일 rate로 뭉치지 않고, 잡마다 다른 first value 이벤트·후보 묶음·관찰 window·판독 가능 여부·표본 부족 시 금지 해석을 1장으로 고정한다.

**전제**: 이 레지스트리는 측정 *가능* 상태(정의 완료)를 고정하는 것이지, 측정 *값의 성패*를 판정하지 않는다. (Measurement Readiness Is A Separate Gate, m34)

---

## 공통 제약

이 레지스트리의 모든 잡에 공통으로 적용한다.

### 표본 전제조건

- 분석 전 **제외 분리**: synthetic/mock/self-test 세션, `deed_save_capped`, 503/지연 세션을 먼저 분리한다.
- **표본 부족 시 기준선**: 첫 10명, 첫 7일은 비율·activation rate를 산출하지 않는다.
- **단일 이벤트 금지**: 어떤 single event도 단독으로 activation 확정, PQL, PMF 근거로 쓰지 않는다.

### 금지 해석 (모든 잡 공통)

| 관찰 | 금지 해석 |
|------|-----------|
| `deed_rerolled` | AI 불신 판정 금지 |
| `deed_save_capped` | Upgrade demand / value 판정 금지 |
| 짧은 세션 | 이탈 판정 금지 (J3 정상 종료 포함) |
| 저장 없음 | J3 실패 판정 금지 |
| D1 미방문 | 가치 없음·관심 없음 판정 금지 |
| judged-saved 갭 | 이탈 / 불신 판정 금지 |

---

## J1 기록형 Activation 레지스트리

**잡 정의**: 오늘 있었던 일을 남기고 싶은 사람. AI 판정은 기록 완성의 보조다.

| 항목 | 내용 |
|------|------|
| **First Value 이벤트** | `deed_saved` (최초 1회) |
| **Activation 후보 묶음** | `deed_saved` 1회 발화 (첫 세션 내) |
| **관찰 Window** | 첫 세션 (D0) |
| **이벤트 판독 가능 항목** | `deed_saved` 발화 여부 |
| **수기 관찰 항목** | 저장 직후 반응 (표정·발언); 재방문 의향 언급; 저장한 이유 자기 말 |
| **표본 부족 금지 해석** | J1 activation rate% 산출; deed_judged만으로 activation 판정 |
| **첫 검증 게이트 (출시 전)** | 첫 세션 내 `deed_saved` 1회 발화 확인 |
| **출시 후 확인 대상** | D7 재방문 + `deed_saved` 2회 이상 → J2 묶음 후보 확인 (별도 gate) |

---

## J2 누적형 Activation 레지스트리

**잡 정의**: 덕력·레벨·이번 달 집계가 쌓이는 걸 보고 싶은 사람. First value는 첫 저장이지만 재방문 누적이 가치 핵심.

| 항목 | 내용 |
|------|------|
| **First Value 이벤트** | `deed_saved` (최초 1회) |
| **Activation 후보 묶음** | `deed_saved` 2회 이상 OR D7 이내 재방문 + 저장 |
| **관찰 Window** | D0~D7 |
| **이벤트 판독 가능 항목** | `deed_saved` 누적 횟수; 재방문 여부 |
| **수기 관찰 항목** | "쌓인다"·"레벨 올랐다" 언급; `level_up_viewed` 확인; 집계 카드 주목 여부 |
| **표본 부족 금지 해석** | 단회 저장으로 J2 activation 확정; `level_up_viewed` 단독으로 완료 판정 |
| **첫 검증 게이트 (출시 전)** | D7까지 `deed_saved` 2회 이상 발화 OR D7 재방문 확인 |
| **출시 후 확인 대상** | D7+ `deed_saved` 반복 패턴 → Correlation Readiness gate(m37) 후 retention 대조 |

---

## J3 AI판정형 Activation 레지스트리

**잡 정의**: AI가 이 행동을 어떻게 보는지 궁금한 사람. First value는 결과 카드 도달이며 저장은 선택.

| 항목 | 내용 |
|------|------|
| **First Value 이벤트** | `deed_judged` (최초 1회) |
| **Activation 후보 묶음** | `deed_judged` 1회 발화 (첫 세션 내). 저장 미발화는 정상 종료 가능 |
| **관찰 Window** | 첫 세션 (D0) |
| **이벤트 판독 가능 항목** | `deed_judged` 발화 여부; `deed_rerolled` 발화 여부 (참고용, 불신 판정 금지) |
| **수기 관찰 항목** | 결과 카드 읽는 시간; 반응(공유·반박·놀람·보여주기); 재판정 의향; 저장 여부와 무관한 만족 신호 |
| **표본 부족 금지 해석** | `deed_saved` 미발화→실패 판정; judged-saved 갭→이탈; `deed_rerolled`→불신 |
| **첫 검증 게이트 (출시 전)** | 첫 세션 내 `deed_judged` 1회 발화 확인 |
| **출시 후 확인 대상** | D7 이내 재방문 + `deed_judged` 반복 → 기록형 전환 신호 여부 별도 관찰 |

---

## J4 회고형 Activation 레지스트리

**잡 정의**: 나중에 다시 보려고 기록하는 사람. 과거 기록 참조·회고가 핵심 가치.

| 항목 | 내용 |
|------|------|
| **First Value 이벤트** | `deed_saved` (최초 1회) |
| **Activation 후보 묶음** | `deed_saved` 1회 + 재방문 의향 OR 홈 최근 덕행 열람 확인 |
| **관찰 Window** | D0~D7 |
| **이벤트 판독 가능 항목** | `deed_saved` 발화; D7 재방문 여부 |
| **수기 관찰 항목** | "나중에 보려고" 언급; 이전 기록 열람 언급; 회고 목적 발언 |
| **표본 부족 금지 해석** | 단회 저장으로 회고 활성화 확정; 저장 횟수를 회고 빈도로 환산 |
| **첫 검증 게이트 (출시 전)** | 첫 세션 내 `deed_saved` 1회 + D7 재방문 의향 손기록 |
| **출시 후 확인 대상** | D7 재방문 + 홈 최근 덕행 열람 여부 → 회고형 second value 확인 |

---

## 충돌 검증 결과

- **marketing-79 기준표**: `deed_saved`(J1/J2/J4) / `deed_judged`(J3) first value 정의 계승. 충돌 없음.
- **marketing-98 독립 2판정**: 가치 발견 신호와 activation 판정 독립 2칸 구조를 레지스트리 항목에도 적용 (이벤트 판독 vs 수기 관찰 분리). 충돌 없음.
- **marketing-93 언어 적합성 판독표**: J1 기록형 중심 현재 Virtue 언어에서 J3 판정형 표면이 약하다는 판독을 이 레지스트리의 J3 관찰 항목에 반영. 충돌 없음.
- **MARKETING_LEARNINGS.md Measurement Readiness (m34)**: 측정 가능 상태와 측정값 성패를 분리하는 원칙을 레지스트리 전제로 명시. 충돌 없음.

### 미검증 항목 (로컬 파일 필요)

`source_signal: 2026-06-01-activation-metric-bundles.md`의 후속 실험 후보 1번 연결을 확인하지 못했다.
로컬에서 해당 파일을 읽고 이 레지스트리의 J1~J4 묶음 정의와 겹침/충돌 여부를 추가 확인해야 한다.

---

## 다음 판단

1. `source_signal` 파일 로컬 확인 후 후속 실험 후보 1번과 레지스트리 연결 완료
2. 첫 실사용자 세션 후 이 레지스트리의 잡별 게이트를 실제로 사용해보고 빠진 항목을 Inbox에 등록
3. 5명 이상 관찰 누적 후 잡 분포 → Correlation Readiness gate(m37) 진입 여부 판단

---

## 계승한 기준

1. **First Value Mapping (m06)**: J1/J2/J4=deed_saved, J3=deed_judged — 레지스트리 전 항목의 first value 기준
2. **Measurement Readiness Is A Separate Gate (m34)**: 이 레지스트리는 "측정 가능 상태" 고정이지 성패 판정이 아님
3. **Prelaunch Decision Boundary (m08)**: 첫 10명 표본은 정성 손기록 중심, 비율 산출 금지

## 이번에 새로 배운 것

- J1-J4 잡별 레지스트리를 하나의 문서로 통합하니, 잡별 판독 차이(J3 무저장 정상 종료 vs J1 저장 필수)가 대비되어 오독 경로가 명확해진다.
- 이벤트 판독 가능 항목과 수기 관찰 항목을 분리하면 instrument 의존도를 낮추고 prelaunch 저신호 관찰 정밀도를 높인다.

## 다음 작업에 넘길 규칙

- 이 레지스트리를 marketing-79 관찰표와 함께 사용할 때: 관찰표의 체크포인트 = 이벤트 판독 가능 항목, 자기 말 칸 = 수기 관찰 항목으로 매핑한다.
- `source_signal` 파일의 후속 실험 후보 1번과 연결이 완료되면 J1~J4 묶음 정의에 추가 이벤트/시그널이 있는지 확인 후 레지스트리를 갱신한다.
