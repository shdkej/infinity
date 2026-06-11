# Virtue Task-Completion 감사표 (첫 입력/결과 직후)

**Intent:** marketing-53  
**Created:** 2026-06-11T11:00Z  
**Status:** docs-only, proposal-only

## 목적

Virtue 첫 입력/결과 직후를 `사용자 의도 → AI가 수행한 작업 → 사용자가 선택한 다음 행동`으로 읽는 손기록 관찰 프레임.

AI 온보딩에서 답변의 질이 아니라 **의도를 작업 완료로 바꾸는 흐름**이 핵심이다.

## 계승한 기준

- J1/J2/J4 first value = `deed_saved`, J3 first value = `deed_judged` ← First Value Mapping (m06~m29)
- 첫 10명 관찰은 손기록 중심, 성패율/activation rate/PMF 환산 금지 ← Prelaunch Decision Boundary (m08, m11, m47)
- 결과 카드 직후 30초는 수기 관찰 프레임 ← Post-Response Flow Reveals Value (m44)
- 4구간 handoff에서 사용자 행동권 보존 ← Guided First-Value Is A Four-Stage Handoff (m51)

## 기존 이벤트명 6개 확인 (first_verification_gate)

| 이벤트 | 발화 시점 |
|--------|----------|
| `add_flow_started` | 사용자가 /add 진입 |
| `deed_judged` | AI 판정 결과 카드 표시 |
| `deed_saved` | 사용자가 저장 선택 |
| `deed_rerolled` | 사용자가 재판정 선택 |
| `deed_save_capped` | 저장 한도 초과 |
| `level_up_viewed` | 레벨업 화면 진입 |

source_note 경로(`source/external-links/marketing/2026-06-11-ai-onboarding-intent-to-task.md`)는 현재 없음. 기존 MARKETING_LEARNINGS.md 기준으로 진행, conflict marker 0건.

## Task-Completion 감사표

### 관찰 구간 1: 첫 입력 직후 (add_flow_started → deed_judged 대기)

| 잡 | 사용자 의도 | AI가 수행한 작업 | 관찰할 다음 행동 | 주의 |
|---|-----------|----------------|----------------|-----|
| **J1** (일/성과) | 오늘 한 일/성과를 기록에 남기고 싶다 | 입력 수신 후 행동/업적 판정 시작 | 기다림 (AI 대기) | `add_flow_started` 후 미판정은 B-LOST/가용성/mock 제외 후 분류 |
| **J2** (성장 추적) | 꾸준히 쌓이는 기록을 만들고 싶다 | 입력 수신 후 누적 공정성 판정 시작 | 기다림 (AI 대기) | J2는 두 번째 저장 이후가 first-value 체감 시점 |
| **J3** (AI 관점) | AI가 이걸 어떻게 볼지 궁금하다 | 입력 수신 후 관점/판정 생성 시작 | 기다림 (기대감이 가장 큼) | J3 결과 카드 자체가 1차 완료; 저장 강요 금지 |
| **J4** (영구 기록) | 나중에 다시 볼 기록을 남기고 싶다 | 입력 수신 후 기록 정리 판정 시작 | 기다림 (AI 대기) | J4는 저장 후 누적 payoff 확인이 본체 |

손기록 질문: "이 입력을 보낼 때 무엇을 원했나요? (자기 말로)"

---

### 관찰 구간 2: AI 결과 카드 직후 (deed_judged 이후 30초)

| 잡 | 사용자 의도 | AI가 수행한 작업 | 관찰할 다음 행동 | 완료 신호 |
|---|-----------|----------------|----------------|----------|
| **J1** (일/성과) | 성과 기록을 확정하고 싶다 | 행동/업적 점수 + 판정 텍스트 표시 | `deed_saved` | ✅ `deed_saved` = first value |
| **J2** (성장 추적) | 누적 기록에 이번 것을 추가하고 싶다 | 누적 판정 + (level_up 트리거 가능) 표시 | `deed_saved` → `level_up_viewed` | ✅ `deed_saved` = first value |
| **J3** (AI 관점) | AI의 관점을 받았다 (완료) | 관점/판정 카드 표시 ← 도착점 | 무저장 종료 OR `deed_rerolled` | ✅ `deed_judged` = first value (무저장 정상 종료) |
| **J4** (영구 기록) | 판정을 확인하고 기록에 저장하고 싶다 | 기록 판정 표시 | `deed_saved` | ✅ `deed_saved` = first value |

손기록 질문: "결과 카드를 보고 나서 무엇을 했나요? 왜 그 선택을 했나요?"

---

### 관찰 구간 3: deed_judged 과대평가 방지 체크

`deed_judged`는 결과 카드가 표시됐다는 사실이지, 아래를 확정하지 않는다:

| 잘못된 읽기 | 올바른 읽기 |
|-----------|------------|
| `deed_judged` = AI 판정 동의/수용 | J3에서는 first value(도착점), J1/J2/J4에서는 통과점 |
| `deed_judged` 후 무저장 = 이탈 | J3 정상 종료(저장 불필요) |
| judged−saved 갭 = 가치 부재 | J3에서는 정상 패턴, J1/J2/J4에서만 보류 신호 |
| `deed_rerolled` = 불신 | 의도 재확인 욕구(판단 보류) |
| `deed_save_capped` = 가치/upgrade demand | availability/friction 신호 |

---

## 첫 10명 손기록 양식

```
[관찰 세션 번호]: ___  [일시]: ___  [추정 잡]: J1 / J2 / J3 / J4
─────────────────────────────────────────────
구간1 – 첫 입력 직후
  의도 (자기 말): ___________________________________
  관찰: 대기 / 추가입력 / 취소 / 기타: ___

구간2 – AI 결과 카드 직후 (30초)
  AI 작업 요약 (판정 내용 한 줄): ___________________
  다음 행동: 저장 / 재판정 / 무저장종료 / 기타: ___
  자기 말 설명: ____________________________________
  완료 신호: deed_saved / deed_judged / 보류 / 마찰

구간3 – 종료 성격
  성공 / 정상 / 보류 / 마찰
  근거: ____________________________________________
─────────────────────────────────────────────
```

---

## 기존 문서 충돌 없음 확인 (conflict marker: 0건)

| 기존 문서 | 관계 |
|---------|-----|
| `first-real-user-baseline-template` | 보완 (baseline 측정 + 구간 감사) |
| `first-10-design-user-ask-script` | 보완 (질문 스크립트 + 행동 감사) |
| `post-result-self-appropriation-reading-table` | 보완 (자기 귀인 + 구간 감사) |
| `virtue-guided-first-value-session-audit.md` (m51) | 보완 (4구간 전체 + 입력/결과 직후 특화) |
| `virtue-add-first-input-prompt-design-audit.md` (m52) | 보완 (prompt 설계 + 행동 관찰) |

---

## 다음 Marketer 체크리스트

- **계승한 기준:** First Value Mapping (m06~m29), Prelaunch Decision Boundary (m08), deed_judged 과대평가 방지(m44, m51, m52)
- **이번에 새로 배운 것:** 구간별 행동 감사표가 이벤트 집계보다 먼저 필요. 특히 구간2(결과 카드 직후 30초)는 잡별로 완료 신호가 다름. task completion subject(누가 완료하는가)가 AI 온보딩 판독 기준
- **다음 작업에 넘길 규칙:** J3에서 무저장 종료는 항상 정상 완료로 처리. 30초 관찰 프레임은 신규 tracking 없이 손기록으로만

## 제약 사항

- 공개 카피, 이벤트, tracking/privacy, dashboard, session replay, 배포, 외부 발송, 비용, 권한 변경: 0
- 모든 문구는 proposal-only (내부 관찰 도구)
- 신규 이벤트/속성 추가 없음
