# Virtue 신규 사용자 홈 화면 FAE 감사표

> **범위**: `/` 홈 화면이 J1~J4 신규 사용자를 First Activation Event(FAE)로 얼마나 잘 안내하는가.  
> 코드·카피·이벤트·대시보드 변경 0. 관찰 기준 정의 문서.

## 0. 전제

- **First Activation Event(FAE)**: 사용자가 처음으로 제품의 핵심 가치를 경험하는 이벤트.  
  J1/J2/J4 = `deed_saved`, J3 = `deed_judged`.
- 홈 화면(`/`)은 FAE 경로의 시작점이다. 신규 사용자가 홈에서 `/add`로 이동해야 FAE 경로가 열린다.
- 이 문서는 홈 화면이 각 J-유형에게 "무엇을 먼저 / 왜 지금 / 하면 무엇이 생김"을 얼마나 명확히 전달하는지를 내부 기준으로 고정한다.
- prelaunch 단계이므로 "충분하지 않음" 판정이 즉각적인 수정 지시는 아니다. 첫 10~20명 관찰 전 노이즈를 줄이는 기준선 확립이 목적이다.

## 1. FAE 방향판 감사표

| J-유형 | FAE 이벤트 | 홈 현재 신호 | 무엇을 먼저 | 왜 지금 | 하면 무엇이 생김 | FAE 방향 판정 |
|--------|-----------|------------|-----------|--------|---------------|------------|
| **J1 기록형** | `deed_saved` | 최근 덕행 카드(있음) · 빈 상태 CTA(미확인) | `/add`로 오늘 덕행 기록 | 오늘 한 일이 내 행적으로 쌓인다 | 첫 덕행 저장 → 기록 시작 | 🟡 보류 — 빈 상태 CTA 명확성 미확인 |
| **J2 누적형** | `deed_saved` | 최근 덕행 카드(있음) · 누적/환생종 신호(미확인) | `/add` + 반복 기록 | 쌓아야 진화가 보인다 | `deed_saved` → `level_up_viewed` 연결 | 🔴 갭 — 홈에서 누적·환생종 payoff 신호 미노출 가능성 |
| **J3 AI 호기심형** | `deed_judged` | AI 채점 신호 없음 | `/add`로 덕행 입력 → AI 채점 대기 | AI가 내 행동을 어떻게 평가할지 궁금 | `deed_judged` 결과 확인 | 🔴 갭 — "왜 지금"이 홈에서 전혀 전달되지 않음 |
| **J4 회고형** | `deed_saved` | 최근 덕행 카드(있음) | `/add`로 오늘 하루 회고 기록 | 오늘을 정리하고 싶다 | 기록의 완결감(`deed_saved`) | 🟡 보류 — 회고 맥락 명시 부재 |

**판정 기호**:
- ✅ 충분 — 현재 홈 화면이 FAE 방향을 명확히 전달
- 🟡 보류 — prelaunch 단계 미확인, 관찰 필요
- 🔴 갭 — 홈 화면이 FAE 방향을 전달하지 못하는 구조적 문제 확인

## 2. "무엇을 먼저 / 왜 지금 / 하면 무엇이 생김" 3문 기준

| 질문 | J1 기록형 | J2 누적형 | J3 AI 호기심형 | J4 회고형 |
|------|---------|---------|-------------|----------|
| **무엇을 먼저** | 덕행 기록 (`/add`) | 덕행 기록 (`/add`) | 덕행 입력 + AI 채점 (`/add`) | 오늘 회고 기록 (`/add`) |
| **왜 지금** | 오늘 한 일이 기록된다 | 쌓아야 진화를 볼 수 있다 | 지금 AI 채점이 가능하다 ⚠️ 홈 미전달 | 오늘을 정리할 수 있다 |
| **하면 무엇이 생김** | 첫 기록 완성(`deed_saved`) | 누적 + 레벨업 신호(`level_up_viewed`) | AI 채점 결과(`deed_judged`) | 회고 완결(`deed_saved`) |

⚠️ J3의 "왜 지금"은 현재 홈 화면에서 전달되지 않음. `three-screen-value-path-audit` §3-A J3 앞단 끊김과 동일 구조.

## 3. 기존 이벤트 관찰 게이트

코드·이벤트 변경 없이 기존 4개 이벤트로 FAE 달성 여부를 관찰한다.

| 이벤트 | 관찰 시점 | FAE 판독 방법 |
|--------|---------|------------|
| `add_flow_started` | `/add` 진입 시 | 홈 → add 이동 확인 (FAE 경로 진입 신호) |
| `deed_judged` | AI 채점 완료 시 | J3 FAE 달성 지표 |
| `deed_saved` | 덕행 저장 시 | J1/J2/J4 FAE 달성 지표 |
| `level_up_viewed` | 레벨업 화면 조회 시 | J2 second value 확인 (FAE 이후) |

**prelaunch 해석 금지선**:
- 전환율이 낮아도 FAE 방향이 나쁘다는 판정 금지. 샘플 부족 단계.
- `deed_judged` 없이 `deed_saved`만 있어도 J3 실패 단정 금지. J1/J4 가능성 존재.
- `add_flow_started` 부재를 홈 화면 문제라고 단정 금지. 직접 `/add` 진입 가능성 고려.

## 4. 선행 문서 정합 확인

| 선행 문서 | 관계 | 충돌 여부 |
|---------|-----|----------|
| `three-screen-value-path-audit` | S1 홈 FAE 방향 포함. 본 문서는 홈만 심화. J3 앞단 끊김 계승. | ✅ 충돌 없음 |
| `first-session-friction-observation-protocol` | F7=J3 앞단 끊김, F8+F6=J2 뒷단 누출. 🔴 갭 판정과 정합. | ✅ 충돌 없음 |
| `aeo-agent-ready-surface-audit` | 봇/AI 파싱 표면 감사. 본 문서는 사용자 FAE 방향. 범위 분리. | ✅ 충돌 없음 |
| `first-session-jtbd-matrix` | J1~J4 정의 원천. 본 문서는 홈 화면 적용. | ✅ 충돌 없음 |
| `competitive-alternatives-positioning-brief` | J1~J4 차별 속성 정의. 본 문서는 UX 방향 적용. | ✅ 충돌 없음 |
| `first-week-activation-retention-bridge` | FAE → 7일 second value. 본 문서는 FAE 진입 전 단계(홈). | ✅ 충돌 없음 |

**범위 한정 확인**: 본 문서는 "홈 화면 FAE 방향판"으로 한정. `/add` 내부 흐름, AI 채점 대기 UX, 저장 후 경험은 선행 문서에 위임.

## 5. 경계 (Out of Scope)

- 코드/카피/이벤트/대시보드 변경: 0
- 공개 카피 반영, 배포, 새 트래킹/프라이버시 변경, 외부 발송: Waiting/approval-needed
- `/add` 내부 UX, S2/S3 화면 분석: `three-screen-value-path-audit`·`first-session-friction-observation-protocol` 위임
- iOS 홈 화면 분석: 별도 Intent 후보

## 6. 첫 관찰 검증 게이트 (첫 3명)

- [ ] J3 사용자가 홈에서 AI 채점 방향을 이해하고 `/add`로 진입했는가?
- [ ] J2 사용자가 홈에서 누적 payoff 신호를 인지했는가?
- [ ] 빈 상태 홈에서 J1/J4 사용자가 `/add` CTA를 즉시 찾았는가?
- [ ] `add_flow_started` 발화가 홈 → add 경로로 추적되는가?

---

*Infinity Heartbeat Agent 생성 · 2026-05-26 · 선행 문서 기반 내부 감사, 외부 발송·배포·코드 변경 0*
