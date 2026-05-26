# Virtue `/add` 입력-결과 균형 감사표

> 선행 문서: jtbd-matrix.md · three-screen-value-path-audit.md · activation-path-friction-audit.md · first-60-second-value-observation-script.md · home-screen-fae-audit.md  
> 목적: prelaunch 첫 10-20명 관찰 전에 `/add` 경로의 입력 부담·결과 강도·click tax·저장 전 정상 종료 기준을 분리해 작은 표본 해석 오류를 줄임  
> 제약: 신규 이벤트·카피 반영·계측·배포·외부 발송·비용 변경 **0건**

---

## 1. `/add` 경로 단계 개요

| 단계 | 화면/UI | 발화 이벤트 | 입력 부담 | 결과 강도 | Click Tax (누적) |
|------|---------|------------|---------|---------|------------------|
| A1. 진입 | `/add` 라우트 첫 로드 | `add_flow_started` | 낮음 (탭 하나) | 없음 (준비 단계) | +1 |
| A2. 사진/메모 입력 | 카메라·텍스트 입력 UI | — (중간 이벤트 없음) | 중간~높음 (촬영 or 텍스트) | 없음 (AI 미실행) | +1~3 |
| A3. AI 판정 대기 | 로딩/처리 화면 | — | 없음 (대기) | 낮음 (기대감) | 0 |
| A4. 결과 카드 | deed 판정 결과 표시 | `deed_judged` | 없음 | **높음** (J3 first value) | 0 |
| A5. 재판정 선택 (선택적) | 재판정 버튼 | `deed_rerolled` | 낮음 | 중간 (다른 결과 확인) | +1 |
| A6. 저장 | 저장 확인 | `deed_saved` | 낮음 | **높음** (J1/J2/J4 first value) | +1 |
| A6'. 저장 상한 도달 | 저장 불가 안내 | `deed_save_capped` | 없음 | 낮음~없음 | — |
| A7. 저장 전 이탈 | 뒤로가기 or 닫기 | — (이탈) | 없음 | 없음 (J3는 정상 종료) | — |

**누적 Click Tax 요약:**
- J3 (A1→A4 이탈): 최소 2~4 click
- J1/J2/J4 (A1→A6 저장): 최소 3~5 click

---

## 2. J1-J4 잡별 first value 분석

| 잡 | 유형 | First Value 정의 | First Value 이벤트 | 가치 발현 단계 | 저장 전 이탈 해석 |
|----|------|-----------------|-------------------|--------------|------------------|
| J1 기록형 | 오늘 한 일을 남기고 싶다 | 행동이 기록됨 | `deed_saved` | A6 | ❌ 미완료 — 저장 필수 |
| J2 누적형 | 쌓이는 것을 보고 싶다 | 누적치 증가 확인 | `deed_saved` | A6 | ❌ 미완료 — 저장 필수 |
| J3 AI 호기심형 | AI가 어떻게 판단하는지 궁금하다 | AI 판정 확인 | `deed_judged` | A4 | ✅ **정상 종료** — A4 이후 이탈 허용 |
| J4 회고형 | 나의 패턴을 돌아보고 싶다 | 회고 기록 저장 | `deed_saved` | A6 | ❌ 미완료 — 저장 필수 |

### J3 저장 전 정상 종료 정의

J3 사용자는 `deed_judged` 발화(A4 결과 카드 확인) 순간 first value를 얻는다.  
따라서 A4 이후 저장 없이 이탈 = **마찰이 아닌 성공적 종료**다.

**판정 기준표:**

| 이벤트 시퀀스 | J3 해석 | J1/J2/J4 해석 |
|-------------|--------|---------------|
| `add_flow_started` → `deed_judged` → 이탈 | ✅ 정상 종료 (first value 달성) | 🟡 관찰 (저장 포기 — 미완료) |
| `add_flow_started` → `deed_judged` → `deed_saved` | ✅ 정상 + 추가 행동 | ✅ 정상 종료 |
| `add_flow_started` → `deed_judged` 미발화 → 이탈 | ❌ 미완료 (A1-A3 단계 이탈) | ❌ 미완료 |
| `add_flow_started` → `deed_judged` → `deed_rerolled` → 이탈 | ✅ 탐색 후 정상 종료 | 🟡 저장 포기 |

---

## 3. 입력 부담 분석 (Input Burden)

입력 부담: 사용자가 `deed_judged`(AI 판정)까지 도달하기 위해 소비해야 하는 노력

| 입력 방식 | 부담 수준 | 이유 | 잡별 영향 |
|----------|---------|------|----------|
| 사진 촬영 | 중간 | 카메라 허용 + 피사체 프레이밍 필요 | 모든 잡 동일 |
| 텍스트 메모 | 낮음 | 키보드 입력만 필요 | 모든 잡 동일 |
| A2→A3 로딩 대기 | 낮음 | 사용자 액션 없음, 대기만 필요 | 모든 잡 동일 |

**입력 부담 해석 원칙:**
- 입력 방식 자체가 마찰인지는 prelaunch 소표본에서 판정 금지
- A2 단계 보류/이탈을 관찰하되, `add_flow_started` 발화 후 `deed_judged` 미발화를 수기로 기록
- 입력 방식별 이탈 차이는 표본 10명 이상 확보 전까지 통계 해석 금지

---

## 4. 결과 강도 분석 (Output Strength)

결과 강도: AI 판정 결과가 사용자에게 전달하는 가치의 선명도

| 결과 요소 | 강도 | 잡별 주효 |
|---------|------|----------|
| deed 레이블 (카테고리명) | 중간 | 공통 |
| AI 판정 문구 (왜 이 판정인가) | 높음 | J3 최강 (first value 핵심) |
| 저장 후 누적 수치 반영 | 높음 | J2 최강 |
| 저장 후 `level_up_viewed` (조건부) | 높음 | J2 강 |

**결과 강도 해석 원칙:**
- `deed_judged` 이후 이탈 비율이 높아도 J3 정상 종료와 결과 불명확 구분 불가 → 소표본 판정 금지
- 관찰자가 직접 "결과 카드 보고 어떤 느낌이었나요?" 허용 질문으로 보조 (friction-observation-protocol F4 태그와 연계)

---

## 5. Click Tax 분석

Click Tax: 사용자가 first value를 얻기까지 누적 클릭·탭·액션 수

```
J3 경로 (최소):
  [앱 진입] → [/add 탭] → [입력 제출] → [AI 판정 대기] → [deed_judged 결과 확인]
  = 최소 3~4 action

J1/J2/J4 경로 (최소):
  J3 경로 + [저장 버튼 탭]
  = 최소 4~5 action
```

**Click Tax 해석 원칙:**
- 절대값 측정은 신규 계측 없이 관찰자 수기 카운트
- A2 단계에서 반복 탭/오류가 발생하면 friction-observation-protocol F1(반복클릭) 태그로 기록
- prelaunch 단계 click tax 감소 조치는 L2 이상 → 별도 Intent 필요

---

## 6. 기존 이벤트 발화 위치 확인

| 이벤트명 | 발화 시점 | 플랫폼 | 감사 비고 |
|---------|---------|-------|----------|
| `add_flow_started` | A1. `/add` 진입 직후 | 웹 | iOS 미확인 (parity-brief 참조) |
| `deed_judged` | A4. 결과 카드 렌더 시 | 웹+iOS | J3 first value 기준 이벤트 |
| `deed_saved` | A6. 저장 완료 시 | 웹+iOS | J1/J2/J4 first value 기준 이벤트 |
| `deed_rerolled` | A5. 재판정 클릭 시 | 웹 | 보조 이벤트, J3 탐색 의도 신호 |
| `deed_save_capped` | A6'. 저장 상한 도달 시 | 웹 | 보조 이벤트, early-return 코드 반영 |

**신규 이벤트·속성·계측 변경: 0건**

---

## 7. prelaunch 해석 금지선

| 금지 해석 | 근거 |
|---------|------|
| `deed_judged` 이후 이탈 = 불만족 | J3 정상 종료와 구분 불가 (소표본) |
| `deed_saved` 도달률로 전체 활성화 성패 판단 | J3는 `deed_judged`가 first value 기준 |
| `deed_rerolled` 발화 = 마찰 신호 | J3 탐색 의지의 긍정 신호일 수 있음 |
| `deed_save_capped` 발화 = 버그 | 의도된 저장 상한 early-return 코드 |
| 전환율·% 산출 | 표본 10-20명 단계에서 통계 해석 금지 |
| A2 입력 방식 차이로 마찰 판정 | 동일 사용자 복수 방식 미확인, 혼재 |

---

## 8. 첫 10-20명 관찰 게이트

**관찰 시 수기 기록 항목:**
- [ ] A2 단계 보류·이탈 발생 여부 및 방식 (사진 vs 텍스트)
- [ ] `add_flow_started` 대비 `deed_judged` 미발화 케이스 (PostHog 육안 또는 수기)
- [ ] `deed_judged` 이후 행동: 저장 / 재판정 / 이탈
- [ ] J3로 추정되는 사용자의 이탈 타이밍 (A4 이후 = 정상 종료로 기록)
- [ ] `deed_save_capped` 발화 여부

**연계 문서:**
- `first-session-friction-observation-protocol.md` F1~F9 태그 연계
- `first-60-second-value-observation-script.md` 60초 타이머 연계
- `activation-path-friction-audit.md` 잡별 마찰 분류 연계

---

## 검증 게이트

| 항목 | 확인 |
|------|------|
| `input burden` 명시 | ✅ §3 |
| `output strength` 명시 | ✅ §4 |
| `click tax` 명시 | ✅ §5 |
| `deed_judged` 명시 | ✅ §1, §2, §6 |
| `deed_saved` 명시 | ✅ §1, §2, §6 |
| `J3 저장 전 정상 종료` 정의 | ✅ §2 |
| 코드/카피/계측 변경 | ✅ 0건 |
| 신규 이벤트 | ✅ 0건 |
| 선행 문서 충돌 마커 | ✅ 없음 |
