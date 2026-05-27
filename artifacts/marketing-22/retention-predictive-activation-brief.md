# Virtue 리텐션 예측 활성화 브리프

> Prelaunch 단계 첫 10-20명 관찰용 내부 문서.  
> 첫 행동(`add_flow_started`)에서 D7 재가치까지를 연결하는 신호 언어를 정의한다.  
> **신규 이벤트·계측·코드·카피·대시보드·배포 변경 없음. 기존 이벤트 6종 인용만.**

## 목적

Prelaunch 상태에서 표본이 10-20명으로 작을 때, 첫 세션의 어떤 행동이 7일 뒤 재방문(D7 재가치)을 예측하는 신호인지 미리 정의해 둔다. 이 브리프가 없으면 `add_flow_started` 이후 모든 미저장을 실패로 해석하거나, `deed_saved` 하나를 PMF 신호로 과대해석하게 된다.

두 가지 핵심 분리:
1. **First value** — 잡별로 "무엇이 첫 가치 순간인가"
2. **Retention-predictive depth signal** — 첫 세션에서 first value 이후 어떤 추가 행동이 D7 재방문 가능성을 높이는가

---

## 1. 잡(Job)별 첫 가치(First Value) 정의

| Job | 코드 | 첫 가치 순간 | 이벤트 | 비고 |
|-----|------|-------------|--------|------|
| J1 기록형 | 오늘 한 일을 남기고 싶다 | 덕행 저장 후 완료감 | `deed_saved` | |
| J2 누적형 | 쌓이는 것을 보고 싶다 | 저장 후 누적·레벨 확인 | `deed_saved` → `level_up_viewed` | `level_up_viewed` 없으면 first value 미달 가능 |
| J3 AI 호기심형 | AI가 내 행동을 어떻게 볼지 궁금하다 | AI 판정 결과 확인 | `deed_judged` | **저장 전 충족 가능** |
| J4 회고형 | 지난 일을 돌아보고 싶다 | 저장 후 목록 확인 | `deed_saved` + `/` 복귀 체류 | 첫 세션에 회고 대상 없음 → D7이 진짜 first value |

> **J3 주의**: `deed_judged` 후 `deed_saved` 없이 세션 종료는 **이탈 아님** — J3가 원하는 것(AI 판정)을 얻은 자연 종료다. 동일 패턴이 J1/J2/J4에서 발생하면 저장 전 이탈 후보로 분류한다.

> **J4 주의**: 첫 세션은 회고할 기록이 없어 `deed_saved`가 씨앗 역할. 진짜 회고 경험은 D3-D7 재방문 때 발생한다.

---

## 2. 리텐션 예측 Depth Signal

First value 이후 아래 신호가 추가로 관찰되면 D7 재방문 가능성이 높아진다고 가설을 세운다. **표본 10-20명에서는 가설 분류만, 통계 판정 금지.**

### J1 기록형

| Depth Signal | 설명 | 관찰 이벤트 |
|-------------|------|-------------|
| 동일 세션 내 `deed_saved` 2회 이상 | 기록 충동이 1개가 아닌 루틴 시작 신호 | `deed_saved` × 2+ |
| D1/D2 `add_flow_started` 재진입 | 루틴 첫 반복 — 습관 형성 가능성 가장 강한 신호 | `add_flow_started` (D2 기준) |

### J2 누적형

| Depth Signal | 설명 | 관찰 이벤트 |
|-------------|------|-------------|
| `deed_saved` 직후 `level_up_viewed` | 누적 payoff에 관심 있음 | `level_up_viewed` |
| 동일 세션 내 `deed_saved` 2회 이상 | 누적 감각 형성 | `deed_saved` × 2+ |

### J3 AI 호기심형

| Depth Signal | 설명 | 관찰 이벤트 |
|-------------|------|-------------|
| `deed_rerolled` 발화 (AI 판정 재시도) | AI 결과에 적극적 호기심, 결과를 탐색하는 행동 | `deed_rerolled` |
| 동일 세션에서 `deed_judged` 2회 이상 | 다른 덕행으로 AI 판정 반복 — 탐색 지속 | `deed_judged` × 2+ |

### J4 회고형

| Depth Signal | 설명 | 관찰 이벤트 |
|-------------|------|-------------|
| `deed_saved` 후 `/` 복귀 체류 | 저장된 목록 즉시 확인 행동 | 정성 관찰 (이벤트 직접 매핑 불가) |
| D7 자발적 재방문 자체 | 첫 세션의 기록이 돌아올 이유가 됨 | `add_flow_started` (D7 기준) |

### Depth 아님 (주의)

- `add_flow_started` 단독: 의도만, 완료 없음
- `deed_save_capped` 단독: 의도된 마찰(저장 전 early return 캡) 발화이지 저장 실패 아님
- `deed_save_capped` 후 이탈: J1/J2/J4에서 저장 전 이탈 후보 가능 — 단정 금지

---

## 3. D7 재가치 정의

D7(첫 사용 7일 후)에 사용자가 돌아왔을 때 어떤 가치를 경험하는지를 잡별로 정의한다.

| Job | D7 재가치 순간 | 관찰 이벤트 | 정성 확인 방법 |
|-----|--------------|-------------|---------------|
| J1 기록형 | 새 덕행을 추가하거나 일주일치 기록 확인 | `deed_saved` (D7) 또는 `add_flow_started` | "지난 주에 다시 열어봤나요? 어떤 이유로?" |
| J2 누적형 | 레벨 변화 또는 누적 수 확인 | `level_up_viewed` (D7) 또는 `/` 복귀 체류 | "저장한 덕행들을 다시 봤나요? 쌓이는 느낌이 있었나요?" |
| J3 AI 호기심형 | 새 행동에 대해 AI 판정 재요청 | `deed_judged` (D7) | "AI 판정을 다시 받아보고 싶었던 행동이 있었나요?" |
| J4 회고형 | 지난 주 덕행 목록 훑어봄 | `/` 복귀 후 체류 (이벤트 직접 확인 불가) | "지난 주 기록 중 기억에 남는 것이 있었나요?" |

> D7 재가치는 반드시 새 `deed_saved`일 필요가 없다. **앱에 돌아온 것 자체**가 J4에게는 충분한 재가치 신호일 수 있다. 재방문 이유를 먼저 확인하고 잡을 재분류한다.

---

## 4. D7 재가치 확인 질문 (정성 관찰용)

첫 10-20명 관찰 시 D7 시점에 아래 질문으로 재가치를 확인한다. 허용된 대화(초대한 사용자 한정)에만 적용.

**공통 (모든 Job)**
1. "지난 주에 Virtue를 다시 열어봤나요? 어떤 이유로?"
2. "Virtue가 없었다면 그 행동 기록을 어떻게 했을 것 같아요?"

**잡별 추가 질문**
- (J1/J4) "저장한 덕행을 다시 본 적 있나요? 어땠나요?"
- (J2) "쌓이는 느낌이 있었나요? 레벨 변화 확인했나요?"
- (J3) "AI 판정을 다시 받아보고 싶었던 행동이 있었나요?"

**D7 재방문 없을 때**
- 물어보지 않는다. 표본이 너무 작아 인터뷰 한 건이 결론을 바꿀 수 있다.
- 재방문 없음 = 잡 분류 재확인 (원래 J4였는데 실제로는 J3였을 수 있음)

---

## 5. 기존 이벤트 증거 매핑

이 브리프에서 사용하는 이벤트는 **기존 발화 이벤트만**이다. 신규 이벤트·속성 추가 없음.

| 이벤트 | 발화 위치 | 이 브리프에서의 역할 |
|--------|----------|---------------------|
| `add_flow_started` | `/add` 진입 시 | 의도 신호. Depth signal은 D2 이후 재발화 때만. |
| `deed_judged` | AI 판정 완료 시 | J3 First value + Depth signal (2회 이상) |
| `deed_saved` | 저장 완료 시 | J1/J2/J4 First value + Depth signal (2회 이상) |
| `level_up_viewed` | 레벨업 화면 노출 시 | J2 First value 보완 + Depth signal |
| `deed_rerolled` | AI 판정 재시도 시 | J3 Depth signal |
| `deed_save_capped` | 저장 전 캡 발화 시 | Depth 아님 — 의도된 마찰. 이후 이탈은 J1/J2/J4 후보 |

---

## 6. Prelaunch 해석 금지선

표본 10-20명 단계에서 아래 해석을 내리면 안 된다.

- **가용성 ≠ 가치**: 503, AI 판정 지연, 저장 캡 등 서버/UX 제약이 있을 때는 행동 해석 보류
- **J3 자연 종료 ≠ 이탈**: `deed_judged` 후 `deed_saved` 없는 세션 종료는 J3 잡 충족 가능성 먼저 확인
- **전환율·리텐션·PMF·% 산출 금지**: 표본이 통계적으로 유의미하지 않음
- **synthetic/mock 제외**: 641 시드 데이터, MOCK 계정, 개발팀 내부 사용은 제외
- **갭 잡 분리 없이 이탈 단정 금지**: 잡별 first value 정의를 먼저 확인하고 해석
- **D7 도달 ≠ 리텐션 확정**: D7 한 번 재방문이 habit을 의미하지 않음. 관찰 기준으로만 사용

---

## 7. 첫 검증 게이트

이 문서를 virtue-rebirth-app에 커밋하기 전 아래를 확인한다.

- [ ] 신규 문서 1개(`apps/web/docs/retention-predictive-activation-brief.md`)만 변경되었는가
- [ ] `deed_judged` 문자열 존재하는가
- [ ] `deed_saved` 문자열 존재하는가
- [ ] `level_up_viewed` 문자열 존재하는가
- [ ] `D7` 문자열 존재하는가
- [ ] `prelaunch` 문자열 존재하는가
- [ ] 신규 이벤트·속성·코드·카피·계측·대시보드·배포 변경 없음
- [ ] synthetic/mock 데이터 인용 없음

---

## 로컬 실행 프롬프트 (virtue-rebirth-app 커밋용)

```
Infinity Intent: marketing-22 Virtue 리텐션 예측 활성화 브리프 작성
Mode: execute_local
Required workflow: workflow-master (없으면 4역할 병렬 합성으로 진행)
Goal: infinity/artifacts/marketing-22/retention-predictive-activation-brief.md 내용을
      virtue-rebirth-app/apps/web/docs/retention-predictive-activation-brief.md로 작성·커밋·push
Context:
  - 선행 문서: apps/web/docs/ 내 jtbd-matrix, three-screen-value-path-audit,
               first-week-activation-retention-bridge, activation-milestone-ladder
  - source note: /home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-27-retention-predictive-activation.md
    (있으면 내용을 추가 반영, 없으면 artifact 초안 그대로 사용)
Allowed: L0/L1 + L2 agent-approved push
Forbidden: 신규 이벤트·속성·코드·카피·계측·대시보드·배포 변경
Verification:
  - 신규 문서 1개만 변경 (git diff --name-only)
  - deed_judged, deed_saved, level_up_viewed, D7, prelaunch 문자열 grep 확인
  - HEAD == origin/master 확인
Report back to: infinity/reports/marketing-22/{timestamp}.html
```

---

*작성: 2026-05-27 | Infinity Heartbeat marketing-22 (cloud draft)*  
*참조: jtbd-matrix, first-session-jtbd-matrix, first-week-activation-retention-bridge,*  
*three-screen-value-path-audit, activation-milestone-ladder, add-input-output-balance-audit*
