# Virtue 첫 세션 정성 마찰 관찰 프로토콜

> prelaunch / 초기 출시 단계 · 첫 10–20명 관찰용  
> 작은 수치를 과대해석하지 않고, 관찰된 행동 증거를 제품·카피·온보딩 개선 후보로 변환한다.

## 0. 이 문서의 위치

- 선행 문서: `first-session-jtbd-matrix.md`, `three-screen-value-path-audit.md`, `ios-activation-event-parity-brief.md`, `activation-path-friction-audit.md`, `first-real-user-baseline-template.md`, `first-week-activation-retention-bridge.md`
- 이 문서는 **정성 관찰 구조**를 정의한다. 정량 이벤트를 바꾸지 않는다.
- 신규 이벤트·속성·코드·카피·대시보드·배포 변경 없음.

## 1. 왜 정성 마찰 관찰이 필요한가

첫 실사용자 표본이 3–20명일 때:
- `deed_judged` / `deed_saved` 전환율은 분모가 작아 해석 불가
- 단 한 명의 이탈·재시작·망설임이 패턴의 전부일 수 있음
- 행동 증거(반복 클릭, 입력 보류, 결과 이해 실패)가 숫자보다 더 빨리 마찰 원인을 알려준다

**이 프로토콜의 목적**: J1–J4 잡별 첫 가치 경로에 대한 정성 마찰 태그를 정의하고, 관찰자가 일관된 기준으로 기록할 수 있게 한다.

## 2. 정성 마찰 태그 정의

관찰 가능한 행동 증거를 **태그**로 고정한다. 이탈·재시도·혼란을 동일 언어로 기록하기 위함이다.

| 태그 | 코드 | 관찰 기준 | 주요 발생 지점 |
|------|------|-----------|----------------|
| 반복 클릭 | `tap-repeat` | 같은 버튼/영역을 2회 이상 탭 | S2 입력, S3 채점 |
| 입력 보류 | `input-pause` | 입력 필드 포커스 후 5초 이상 정지 | S2 `/add` 입력 |
| 저장 전 이탈 | `pre-save-exit` | `deed_saved` 발화 전 앱 이탈 또는 뒤로가기 | S3 → S2/S1 |
| 결과 이해 실패 | `result-confusion` | `deed_judged` 발화 후 채점 결과 화면을 5초+ 관찰하며 반응 없음 | S3 결과 카드 |
| 재시작 | `restart` | add_flow 중 `/`로 복귀 또는 앱 재시작 | S1 ← S2/S3 |
| CTA 미인지 | `cta-miss` | 화면 내 주요 행동 유도 버튼을 지나치거나 오래 탐색 | S1, S2 |
| 채점 재시도 | `rejudge` | `deed_rerolled` 발화 — deed_judged 후 재채점 요청 | S3 |
| 저장 상한 혼란 | `cap-confusion` | `deed_save_capped` 화면에서 정지 또는 이탈 | S3 |
| 복귀 없음 | `no-return` | 첫 세션 완료 후 7일 내 재방문 없음 (정량 보조 지표) | Post-S3 |

> **주의**: 태그는 관찰 분류이지 결함 판정이 아니다. `tap-repeat`이 J3에서는 "AI 채점이 흥미로워 더 보고 싶다"는 긍정 신호일 수 있다. `rejudge`도 마찬가지.

## 3. J1–J4 첫 가치 경로 × 마찰 태그 분류

### 3-1. 분류 기준

| 분류 | 정의 | 우선순위 |
|------|------|----------|
| `value-critical` | 마찰이 지속되면 첫 세션 가치 이벤트(`deed_judged` 또는 `deed_saved`)가 발화되지 않는 지점 | 즉각 개선 후보 |
| `value-adjacent` | 첫 가치 이벤트는 발화되지만, 경험 품질·2차 가치·리텐션에 영향을 주는 마찰 | 관찰 후 개선 검토 |
| `non-critical` | 첫 세션 가치 경험과 무관한 UX 마찰 (또는 긍정 참여 신호) | 기록 유지, 우선순위 낮음 |

### 3-2. J1 기록형 (첫 가치: `deed_saved`)

목표: 오늘 한 일을 기록하고 저장한다.

| 경로 단계 | 관련 태그 | 분류 | 관찰 노트 |
|-----------|-----------|------|-----------|
| S1 `/` 진입 | `cta-miss` | value-critical | `/add`로 가는 CTA를 찾지 못하면 flow 시작 불가 |
| S2 `/add` 입력 | `input-pause` | value-critical | "무엇을 써야 하는지" 모를 때 발생 |
| S2 → S3 채점 대기 | `result-confusion` | value-adjacent | J1은 deed_judged가 목적이 아님. 채점 대기 중 이탈 위험 |
| S3 저장 | `pre-save-exit` | value-critical | `deed_saved` 전 이탈 = 첫 가치 미달성 |
| S3 저장 상한 | `cap-confusion` | value-adjacent | 첫 기록에서 cap 노출 가능성 낮지만 발생 시 혼란 |

**J1 관찰 우선순위**: `cta-miss` → `input-pause` → `pre-save-exit`

### 3-3. J2 누적형 (첫 가치: `deed_saved`)

목표: 첫 `deed_saved` 완료 후 반복 누적의 가치를 기대하게 한다.

| 경로 단계 | 관련 태그 | 분류 | 관찰 노트 |
|-----------|-----------|------|-----------|
| S1 `/` 진입 | `cta-miss` | value-critical | J1과 동일 |
| S2 입력 | `input-pause` | value-critical | "쌓인다"는 약속이 보이지 않으면 입력 동기 약함 |
| S3 저장 후 복귀 | `no-return` | value-adjacent | 누적 payoff는 `/` 복귀 또는 `level_up_viewed`에 의존. 첫 세션 후 복귀 없음이 조기 신호 |
| S3 레벨업 탐색 | `tap-repeat` | non-critical | level_up 화면 반복 탐색은 긍정 참여 신호일 수 있음 |

**J2 관찰 우선순위**: `input-pause`(S2) + `no-return`(7일 내)

### 3-4. J3 AI 호기심형 (첫 가치: `deed_judged`)

목표: AI 채점 결과를 받아보고 "흥미롭다"는 경험을 한다.

| 경로 단계 | 관련 태그 | 분류 | 관찰 노트 |
|-----------|-----------|------|-----------|
| S1 `/` — AI 약속 가시성 | `cta-miss` | value-critical | S1에서 AI 채점 약속을 보지 못하면 진입 동기 없음 (three-screen-audit 핵심 발견) |
| S2 입력 | `input-pause` | value-adjacent | J3는 결과 기대가 동기. 입력 자체보다 "AI가 판단하게 하겠다"는 의도 확인 |
| S3 채점 결과 | `result-confusion` | value-critical | `deed_judged` 발화 후 결과 이해 실패 = 첫 가치 미달성 |
| S3 재채점 | `rejudge` | non-critical | `deed_rerolled`는 J3에서 흥미 있는 참여 신호. 부정이 아닌 긍정으로 별도 기록 |

**J3 관찰 우선순위**: S1 AI 약속 가시성(`cta-miss`) + S3 결과 이해(`result-confusion`)

### 3-5. J4 회고형 (첫 가치: `deed_saved`)

목표: 오늘 하루를 덕행으로 돌아보고 저장한다.

| 경로 단계 | 관련 태그 | 분류 | 관찰 노트 |
|-----------|-----------|------|-----------|
| S1 `/` 진입 | `cta-miss` | value-critical | J1과 동일 |
| S2 입력 | `input-pause` | value-adjacent | 회고 의도가 강해 보류가 "생각하는 중"일 수 있음. 기준 완화 (5초 → 10초) 검토 |
| S2 입력 중 | `restart` | value-critical | 입력 중 재시작 = 무엇을 써야 하는지 모름 |
| S3 채점 대기 | `result-confusion` | value-adjacent | J4에서 AI 채점은 보조. 채점 대기 중 이탈보다 저장 전 이탈이 더 위험 |
| S3 저장 | `pre-save-exit` | value-critical | J1과 동일 |

**J4 관찰 우선순위**: `restart`(S2) + `pre-save-exit`(S3)

## 4. 관찰 기록 양식

아래 표를 `first-real-user-baseline-template.md`와 연계 사용. 한 명당 한 행을 채운다.

| 관찰자 | 사용자 # | 잡 분류 | 관찰된 태그 | 발생 단계 | 분류 | 메모 |
|--------|---------|---------|-------------|-----------|------|------|
| (이름) | U01 | J1 | `input-pause` | S2 | value-critical | "뭘 써야 하지"라고 말함 |
| (이름) | U02 | J3 | `cta-miss` | S1 | value-critical | AI 채점 버튼 20초 탐색 |
| ... | | | | | | |

### 관찰 방법 우선순위

개인정보·트래킹 코드 변경 없이 관찰한다.

1. **동석 관찰**: 사용자 옆에서 화면·말·행동 직접 관찰 (가장 정확)
2. **통화/화면공유**: 원격으로 화면 보며 실시간 관찰
3. **자기 보고**: 사용 직후 "어디서 막혔나요?" 질문

> session replay 도구 도입, 개인정보·트래킹 코드 변경은 이 프로토콜 범위 밖. 별도 Intent로 처리.

## 5. 검증 게이트

### 5-1. 첫 3명 검증 게이트

| 체크 | 기준 |
|------|------|
| 관찰 기록 양식 1행 이상 채워짐 | 최소 한 태그 기록 |
| value-critical 태그 1개 이상 발견 또는 없음 확인 | 있으면 개선 후보 등록, 없으면 "마찰 없음" 기록 |
| J 분류 가능 (J1–J4 중 하나) | 분류 불가 시 J0(분류 대기)로 기록 |
| 정량 이벤트와 정성 태그 불일치 기록 | 예: deed_saved 발화했는데 `result-confusion` 관찰 → 불일치 메모 |

### 5-2. 첫 10명 검증 게이트

| 체크 | 기준 |
|------|------|
| 가장 많이 관찰된 태그 top-3 도출 | 절대 빈도 기준 (전환율 아님) |
| J1–J4 분포 파악 | 어느 잡이 가장 많은지 확인 |
| value-critical 태그가 특정 잡에 집중되는지 확인 | 집중 시 해당 잡의 첫 화면·카피·흐름 개선 우선 |
| 동일 태그가 3명 이상 반복 시 개선 후보 등록 | INTENTS.md Inbox에 후속 Intent로 추가 |
| "관찰 없음" vs "태그 없음" 구분 | 관찰 기회 없었던 것과 마찰이 없었던 것을 혼동하지 않음 |

### 5-3. 판정 금지선 (prelaunch)

- 전환율(deed_judged ÷ add_flow_started 등) 수치로 성패 판정 금지 (표본 < 20명)
- "J3 사용자가 1명이라 AI 관심 없음"으로 결론 금지
- 관찰된 마찰이 없을 때 "온보딩 완벽"으로 결론 금지 (관찰 기회가 적었을 수 있음)
- synthetic/test 트래픽 포함 금지

## 6. 선행 문서 연계

| 이 프로토콜 | 연계 선행 문서 | 관계 |
|-------------|----------------|------|
| J1–J4 잡 정의 | `first-session-jtbd-matrix.md` | 계승 |
| S1→S2→S3 경로 | `three-screen-value-path-audit.md` | 계승 |
| 이벤트 발화 위치 | `ios-activation-event-parity-brief.md` | 참조 |
| 마찰 good/bad 분류 방식 | `activation-path-friction-audit.md` | 계승 |
| 관찰 기록 행 | `first-real-user-baseline-template.md` | 연계 |
| 7일 복귀 판단 | `first-week-activation-retention-bridge.md` | 참조 |
| setup/aha/habit 사다리 | `activation-milestone-ladder.md` | 참조 |

---

*이 문서는 관찰 프레임워크다. 관찰 결과에 따른 제품·카피·코드 변경은 별도 Intent로 처리한다.*
