# Virtue Prelaunch 분석 Skill Sheet

> 이 문서는 에이전트와 내부 분석자가 Virtue prelaunch 단계 데이터를 읽을 때 반드시 확인하는 1-page 참조다.  
> 매 분석 실행 전 이 문서를 먼저 읽으면 product taxonomy, 쿼리 금지선, activation 정의를 재발견하는 비용을 없앤다.

---

## §0 First Value Mapping (불변 기준)

| 잡 | 코드명 | First Value 이벤트 | 앵커 | 설명 |
|----|--------|------------------|------|------|
| J1 기록형 | `deed_saved` | `deed_saved` | :183 | 저장 후 기록이 쌓임 |
| J2 누적형 | `deed_saved` | `deed_saved` | :183 | 저장 후 누적/환생종 payoff |
| J3 AI 호기심형 | `deed_judged` | `deed_judged` | :106 | 저장 **없이** 판정에서 가치 완결 |
| J4 회고형 | `deed_saved` | `deed_saved` | :183 | 저장 후 회고 맥락 완성 |

> **J3 핵심 규칙**: `deed_judged` 후 `deed_saved` 없이 세션이 끝나는 것은 이탈이 아니라 **정상 종료**다. J3에서 저장을 강제하지 않는다.

---

## §1 핵심 이벤트 화이트리스트

| 이벤트 | 앵커 | 주요 역할 | 주의 |
|--------|------|-----------|------|
| `add_flow_started` | :72 | TTV 시작점, 진입 의도 (J1~J4 공통) | vanity: 첫 행동이지 first value 아님 |
| `deed_judged` | :106 | J3 first value / J1·J2·J4 통과점 | judged−saved 갭: J3=정상, J1/J2/J4=저장 전 이탈 후보 |
| `deed_rerolled` | :149 | 호기심·재시도 (최대 3회) | 불신 단정 금지, acceptance 신호 아님 |
| `deed_save_capped` | :167 | 30덕 상한 early-return, `deed_saved` 미발화 | **availability/friction 신호. upgrade demand·monetization 환산 절대 금지** |
| `deed_saved` | :183 | J1/J2/J4 first value, TTV 종료점 | 저장수=만족도 환산 금지 |
| `level_up_viewed` | :199 | 누적 payoff 인지 (J2 depth) | 1회로 리텐션 확보 단정 금지 |

보조 참조용 (사실 확인만, 쿼리 중심 사용 금지):
- `add_flow_abandoned` :78 — 미저장 이탈 짝 (코드 사실 참조만)
- `deed_judge_attempted` :135 — 판정 시도 선행 단계, first value 아님

---

## §2 Activation 후보 묶음 (등록부 A1~A4, marketing-33 기준)

| 등록 ID | 잡 | First Value | 후보 묶음 | 관찰 Window | 주의 |
|---------|----|-------------|-----------|-------------|------|
| A1 | J1 기록형 | `deed_saved`:183 | `deed_saved` ≥1, `add_flow_started` | W-IMM (첫 세션) | 저장수로 quality 단정 금지 |
| A2 | J2 누적형 | `deed_saved`:183 | `deed_saved` ≥2 (distinct day), `level_up_viewed` | W-CONF (D7) | `level_up_viewed` 1회로 확보 단정 금지 |
| A3 | J3 AI 호기심형 | `deed_judged`:106 | `deed_judged`, `deed_rerolled` (선택) | W-IMM (첫 세션) | `deed_saved` 없음이 정상. 묶음에 `deed_saved` 필수 포함 안 함 |
| A4 | J4 회고형 | `deed_saved`:183 | `deed_saved` ≥1 (맥락 있는 저장) | W-IMM (첫 세션) | 저장수로 회고 품질 단정 금지 |

**Window 정의**:
- **W-IMM**: 첫 세션 내 — 즉각 가치 확인용
- **W-CONF**: D7 내 — 장기 리텐션 예측 가능성 신호 (가능성이지 확보 아님)

> 이 묶음은 출시 전 사전 등록(pre-register)한 기준이다. 데이터를 보고 사후에 묶음·window를 고르는 cherry-pick 금지.

---

## §3 Availability vs Value 분리 (분석 전 필수 선분류)

| 신호 | 종류 | 올바른 읽기 | 잘못된 읽기 (금지) |
|------|------|-------------|--------------------|
| `deed_save_capped`:167 | Availability/Friction | 30덕 상한 early-return, `deed_saved` 미발화 | upgrade demand, monetization intent, TTV 종료 |
| HTTP 503 | Availability | 서버 가용성 문제 | activation 실패 |
| 판정 지연 | Availability | AI 응답 지연 | trust 문제, friction |
| `deed_judged` 후 `deed_saved` 없음 (J3) | 정상 종료 | J3 first value 달성, 이탈 아님 | 저장 실패, 이탈 |

`deed_save_capped` 발생 시: TTV 계산에서 제외, activation 집계에서 제외.  
**순서**: Availability 선분류 → activation/TTV/retention 읽기.

---

## §4 Prelaunch 쿼리 금지선

prelaunch 단계 (첫 10~20명)에서 절대 쿼리하거나 결론 내리지 않는 항목:

| 금지 항목 | 이유 |
|-----------|------|
| activation rate %, conversion rate % | 표본 부족, prelaunch noise |
| PMF score 결론 | 소표본 외삽 금지 |
| D7 retention % (외부 벤치마크 대비) | 외부 수치 복사 금지 |
| 1명 신호로 확정 | 단일 사례는 방향 재료이지 결론 아님 |
| judged−saved 갭 → J3 이탈 단정 | J3는 정상 종료 가능 |
| `deed_save_capped` → upgrade demand | Availability/Friction 신호 |
| synthetic/mock/self-test → 사람 증거 혼입 | 트래픽 분류 선행 필수 |
| Activation 후보를 사후 cherry-pick | 등록부 A1~A4 사전 등록이 원칙 |

---

## §5 Traffic Source 선분류 (분석 전 필수)

트래픽 종류를 먼저 분리한 뒤 activation/TTV/retention을 읽는다.

| 종류 | 처리 |
|------|------|
| A 사람 실사용 | baseline 본행, 분석 대상 |
| B 메이커 self-test | 표시 후 집계에서 제외 |
| C synthetic/mock (641 시드, mock 폴백, `임시 판정` 라벨) | J3 first value 부적합, 집계 제외 |
| D 플랫폼 차이 (web vs iOS) | platform 분리 후 최소공약수 비교 |
| E 장래 agent/API | 미발생, 규칙 별도 수립 필요 |

---

## §6 핵심 참고 문서 인덱스

| 문서 | 경로 | 주요 내용 |
|------|------|----------|
| JTBD 매트릭스 | `apps/web/docs/first-session-jtbd-matrix.md` | J1~J4 기본 정의 |
| Marketing Learnings 원장 | `infinity/MARKETING_LEARNINGS.md` | 이벤트 매핑·판단 기준 |
| Activation 후보 등록부 | `apps/web/docs/activation-candidate-registry.md` | A1~A4 + W-IMM/W-CONF |
| PLG Foundation Exit Gate | `apps/web/docs/plg-foundation-exit-gate.md` | 측정 가능 상태 게이트 G1~G7 |
| Onboarding 지표 판독표 | `apps/web/docs/onboarding-metrics-reading-table.md` | activation/TTV/D7 종합 |
| Traffic Source 경계표 | `apps/web/docs/traffic-source-reading-boundary-table.md` | 트래픽 분류 A~E |
| Onboarding 체크리스트 감사표 | `apps/web/docs/onboarding-checklist-audit-table.md` | 잡별 체크리스트 4분류 |
| AI Outcome Proxy 사전 | `apps/web/docs/ai-outcome-proxy-dictionary.md` | activity/acceptance/proxy 분리 |
| Product Body vs Bumper | `apps/web/docs/product-body-vs-bumper-boundary-table.md` | 표면 본체/범퍼 잡별 분류 |

---

## §7 에이전트 사용 패턴

이 skill sheet를 사용하는 에이전트는 아래 순서를 따른다:

1. **분석 전**: §0 first value mapping → §3 availability 선분류 → §5 traffic 선분류
2. **쿼리 전**: §4 금지선 확인
3. **activation 판단 전**: §2 등록부 A1~A4와 window 확인, 사후 cherry-pick 금지
4. **의문이 생기면**: §6 인덱스에서 원본 문서 참조

---

*Virtue prelaunch 분석을 위한 에이전트 참조 sheet. 코드·이벤트 속성·공개 카피·계측·배포·외부 발송·비용·권한·개인정보 변경을 포함하지 않는다.*  
*출처: marketing-06~35 (infinity/MARKETING_LEARNINGS.md 계승). 생성: 2026-06-03.*
