# Virtue 결과 카드 직후 30초 행동 감사표 (Draft)

> Cloud prepare artifact for marketing-44.
> Local Claude Code가 이 파일을 참조해 `/home/ubuntu/dev/virtue-rebirth-app/apps/web/docs/post-response-flow-audit.md`를 생성한다.

## 작성 배경

AI 판정 결과 카드(`deed_judged` 발화) 직후 30초 내 사용자 행동을 이벤트 수가 아닌 **잡별 흐름 패턴**으로 분류하기 위한 감사표가 필요하다. 특히:

- J3 미저장 정상 종료 ≠ 이탈 (J3에서 `deed_judged` 자체가 first value)
- J1/J2/J4 저장 없는 종료 = 보류 (first value 미달)
- `deed_save_capped` = 가용성/마찰 (upgrade demand 아님)
- `deed_rerolled` = 의도 관찰 보류 (불신 아님)

이 표가 없으면 prelaunch 첫 10명 관찰에서 같은 "저장 없는 종료"를 J3에서는 성공으로, J1에서는 이탈로 다르게 읽어야 한다는 기준이 없어 오독이 발생한다.

## 계승한 기준 (from MARKETING_LEARNINGS.md)

| # | 기준 | 이번 적용 |
|---|------|----------|
| 1 | **First Value Mapping**: J1/J2/J4=`deed_saved`, J3=`deed_judged` | 분류의 기준축 |
| 2 | **Session Value Is Read By Job**: fewer actions가 더 빠른 가치일 수 있다 | J3 짧은 무저장 세션 = 정상 |
| 3 | **AI Outcome Proxy Separation**: `deed_saved`≠AI 동의, judged-saved 갭≠불신 | 분류 주의사항 |
| 4 | **Nudges Are Event-Triggered, Show-Nothing Is Default** | do-not-send 조건 설계 |
| 5 | **Availability And Friction Are Not Value**: `deed_save_capped`=마찰 | friction 분류 기준 |
| 6 | **Prelaunch Decision Boundary**: 첫 10명/7일 관찰은 비율/retention 결론 금지 | 관찰표 사용 범위 |

## 이벤트 앵커 (고정 — drift 금지)

| 이벤트 | 앵커 # | 해석 가이드 |
|--------|--------|-------------|
| `deed_judged` | 106 | AI 판정 완료, 결과 카드 표시 (시작점) |
| `deed_rerolled` | 78 | 결과 재판정 요청 |
| `deed_saved` | 183 | 결과 저장 |
| `deed_save_capped` | 199 | 저장 상한 도달 (availability/friction) |

## 분류 기준

| 분류 | 정의 | 주의 |
|------|------|------|
| **activation** | 잡별 first value 이벤트가 deed_judged 기준 30초 내 발화됨 | J3: deed_judged 이미 발화됨 → 이후 행동은 normal/hold/friction |
| **normal** | 잡의 예상 완료 패턴 | J3 저장 없는 종료 = normal. 이탈과 혼동 금지 |
| **hold** | 의도 파악 전 보류, 결론 내지 않음 | 이탈·불신·불만으로 단정 금지 |
| **friction** | 가용성/마찰 신호 | upgrade demand, value, 불신으로 단정 금지 |

## 잡별 행동 분류표

### J3 — 결과 판정 중심 (first value: `deed_judged`)

> J3의 결과 카드 자체가 first value다. `deed_judged` 발화 시점에 이미 activation. 이후 30초는 post-first-value 행동이다. **저장 없는 종료는 정상이다.**

| # | deed_judged 이후 30초 시퀀스 | 분류 | 보내면 안 되는 조건 |
|---|------------------------------|------|---------------------|
| J3-1 | → [종료] (즉시 또는 30초 내) | **normal** | 저장 독촉 금지, 이탈로 단정 금지 |
| J3-2 | → `deed_rerolled` → [종료] | **normal** | 불신으로 단정 금지 |
| J3-3 | → `deed_rerolled` × 2+ → [종료] | **hold** | 불만으로 단정 금지, 의도 관찰 |
| J3-4 | → `deed_saved` | normal (추가 가치 도달) | 저장 강제 아님; J3에서 저장은 선택(범퍼) |
| J3-5 | → `deed_save_capped` | **friction** | availability/friction. 업그레이드 수요 금지 |
| J3-6 | → [30초+ 무행동 후 종료] | **hold** | 마찰/이탈 단정 금지 |

### J1 — 저장 중심 (first value: `deed_saved`)

> J1에서 `deed_judged` 발화 = 결과 카드 표시. first value는 아직 안 왔다. 30초 내 `deed_saved` 발화 여부가 핵심. **저장 없는 종료는 J1에서 이탈 후보(hold), J3 정상 종료와 혼동 금지.**

| # | deed_judged 이후 30초 시퀀스 | 분류 | 보내면 안 되는 조건 |
|---|------------------------------|------|---------------------|
| J1-1 | → `deed_saved` (즉시 또는 30초 내) | **activation** | — |
| J1-2 | → `deed_rerolled` → `deed_saved` | **normal** | 재판정 = 마찰로 단정 금지 |
| J1-3 | → `deed_rerolled` × 2+ → `deed_saved` | **normal** | — |
| J1-4 | → `deed_rerolled` × N → [종료] | **hold** | 이탈 확정 금지, 관찰 보류 |
| J1-5 | → [종료] (저장 없음, 30초 내) | **hold** | J3 정상 종료와 혼동 금지. J1에서는 저장 이탈 후보 |
| J1-6 | → `deed_save_capped` | **friction** | upgrade demand 금지 |

### J2 — 누적 저장 중심 (first value: `deed_saved`, second value: 두 번째 저장)

> J2 결과 카드 직후 30초 행동은 J1과 동일 패턴으로 읽는다. 차이는 두 번째 세션/저장에서 나타난다.

| # | deed_judged 이후 30초 시퀀스 | 분류 | 보내면 안 되는 조건 |
|---|------------------------------|------|---------------------|
| J2-1~6 | J1과 동일 패턴 | J1 기준 동일 | J1 기준 동일 |

*두 번째 저장 관찰은 당일 세션 내가 아니라 D3/D7 재방문 시 확인한다.*

### J4 — 재판정/영구 주석 중심 (first value: `deed_saved`)

> J4는 AI 판정을 영구 주석으로 누적하는 잡이다. 결과 카드 직후 재판정이 많을 수 있으며 이는 정제 행동이다.

| # | deed_judged 이후 30초 시퀀스 | 분류 | 보내면 안 되는 조건 |
|---|------------------------------|------|---------------------|
| J4-1 | → `deed_saved` (즉시) | **activation** | — |
| J4-2 | → `deed_rerolled` × N → `deed_saved` | **normal** (주석 정제) | 재판정 반복 = 불신으로 단정 금지 |
| J4-3 | → `deed_rerolled` × N → [종료] | **hold** | — |
| J4-4 | → [종료] (저장 없음) | **hold** | J3 정상 종료와 혼동 금지 |
| J4-5 | → `deed_save_capped` | **friction** | upgrade demand 금지 |

## 보내면 절대 안 되는 조건 요약

| 조건 | 금지 이유 | 근거 |
|------|----------|------|
| J3 저장 없는 종료 → 저장 독촉/알림 | J3 정상 종료를 마찰로 만듦 | First Value Mapping, Session Value |
| `deed_save_capped` → 업그레이드 메시지 | 가용성/마찰을 upgrade demand로 오독 | Availability And Friction Are Not Value |
| `deed_rerolled` 반복 → 불신/이탈 알림 | 의도 파악 전 결론 | AI Outcome Proxy Separation |
| J1/J4 저장 없는 종료 → J3 정상 종료로 오분류 | 다른 잡의 부호 혼동 | Session Value Is Read By Job |
| 첫 10명/7일 내 비율/retention/activation rate 결론 | Prelaunch Decision Boundary 위반 | Prelaunch Decision Boundary |
| first value 도달 직후 전환/공유/유료 넛지 삽입 | Nudge trigger 오용 | Nudges Are Event-Triggered |

## 관찰표 (첫 10명 / 첫 7일)

> 비율, retention%, activation rate, churn 결론 없이 행 단위로 채운다. 이것은 "분류 가능성 확인"이다.

| 날짜 | 사용자 ID (익명) | 잡 추정 | deed_judged 이후 시퀀스 | 분류 | 메모 |
|------|-----------------|---------|------------------------|------|------|
| | | | | | |
| | | | | | |
| | | | | | |

*traffic source 분리 먼저: synthetic/mock/self-test는 관찰표에 포함하지 않는다.*

## 작성 규칙 (Local Claude Code용)

1. 기존 이벤트 앵커만 인용한다 (`deed_judged`:106, `deed_rerolled`:78, `deed_saved`:183, `deed_save_capped`:199)
2. 신규 이벤트·속성·카피·tracking/privacy·대시보드·세션리플레이·외부발송·비용·권한 변경 없음
3. code diff 0, conflict marker 0
4. 저장 후 파일 경로: `apps/web/docs/post-response-flow-audit.md`
5. 완료 후 HTML report 작성 → `infinity:reports/marketing-44/{timestamp}.html`
6. MARKETING_LEARNINGS.md에서 새 durable learning candidate가 있으면 report details에 기록

## 새 Durable Learning Candidate

> Report 완료 시 평가하여 MARKETING_LEARNINGS.md 승격 여부 결정

**후보:** "Post-Response 30s Window Is Job-Specific, Not Event-Count-Specific"
- 결과 카드 직후 30초 행동은 이벤트 수나 클릭 수가 아니라 잡별 first value 기준으로 분류해야 한다.
- J3 미저장 종료 = 정상(first value 이미 도달), J1/J2/J4 미저장 종료 = hold(first value 미달)
- `deed_rerolled` = 의도 관찰(불신 아님), `deed_save_capped` = friction(value 아님)
- [[Session Value Is Read By Job, Not Event Count]]를 결과 카드 직후 30초 관찰 시점으로 좁힌 하위 축
