# Virtue AI Authorization Boundary Table
> marketing-67 | docs-only | prelaunch | 2026-06-18

Lens: WEF/Capgemini ACAP "무엇을 허용할 것인가" 관점 → Virtue J1-J4별 권한 경계.  
Source note: `source/external-links/marketing/2026-06-18-agent-authorization-boundary.md`

**목적**: Virtue AI의 권한 경계를 J1-J4 잡별로 고정하여, 첫 사용자의 AI 판정 과신/오해 위험을 줄이고 prelaunch first-10 관찰에서 "AI에게 무엇을 맡긴다고 느꼈는가"를 더 선명하게 읽기 위한 내부 기준 문서.

## 전제 (계승)

- **No Autonomous Action** (marketing-38): Virtue AI는 외부 자율 행동 없음. 모든 최종 선택은 사용자에게 있음
- **Trust Evidence Inventory** (marketing-65): J1-J4별 신뢰 증거 표준 — 이 권한 경계표는 그 증거를 실행 경계로 구체화
- **Agentic Context Map** (marketing-66): J1-J4별 user_intent·문맥 흐름 — 이 표는 그 흐름에서 AI가 할 수 있는/없는 경계를 고정
- **Decision-Delegation Risk Rides The Verb** (marketing-45): 판결 vs 관점 프레임 적용

## J1-J4 AI 권한 경계표

| Job | user_delegates | virtue_may_do | virtue_must_not_do | human_decision_required | evidence_to_show |
|-----|----------------|---------------|--------------------|--------------------------|------------------|
| **J1 — 행동 기록 저장** | 기록한 행동의 AI 관점 해석 보조 | `deed_judged` 카드 제공, 저장 선택 안내, 판정 근거 문장 표시 | 저장 강요, 도덕적 단정, 기록 외부 전송, 자동 저장 | 저장 여부 — 저장 = 명시적 수용(선택) | 저장 전 취소·재시도 가능, 외부 전송 없음, 판정 = 관점(결론 아님) |
| **J2 — 누적 레벨 패턴** | 반복 기록 기반 패턴·레벨 해석 보조 | 누적 저장 집계, 레벨 패턴 피드백 제공, 누적 기준 공개 | 단기 표본으로 성격·능력 결론, 자동 행동 지시, 누적 데이터 외부 공유 | 계속 기록할지 여부 — 반복 저장은 선택 | 레벨·누적 맥락 공개, "표본 적을 때 패턴 미확정" 명시 |
| **J3 — AI 판정 보기** | 특정 행동의 AI 관점 확인 (저장은 선택) | `deed_judged` 카드 제공, 판단 한계 표시, 재판정 안내 | 무저장 종료를 이탈·실패로 처리, 판정 결과 외부 공유, 판정을 사실·결론으로 제시 | 저장/건너뛰기 — J3 무저장 종료 = 정상 완료 | "판정 = 관점, 결론 아님" 명시, 판단 한계 문장, 무저장 종료 비용 0 |
| **J4 — 영구 주석** | 선택한 기억에 AI 주석 영구 저장 보조 | `deed_judged` + 영구 저장 제공, 수정·삭제 옵션 안내 | 자동 공유·외부 전송, 민감 정보 자동 저장, 타인 관련 자동 주석 | 공유·삭제·보관 여부 — 영구 저장 전 명시 선택 | 수정·삭제 가능성 표시, privacy boundary 명시, 저장 전 선택 affordance |

## 공통 구조적 경계

Virtue AI는 어떤 잡에서도:
- **자율 외부 행동 없음** — API 발신, 외부 메시지, 타인 전송 없음
- **마지막 선택권은 사용자** — 저장 비강제, 무시 비용 0, 외부 효과 0
- **판정 = 관점, 결론 아님** — AI 판정을 도덕적 단정·사실·전문가 판단으로 제시 금지
- **에이전트 오독 경계 유지** — J3 무저장 종료를 실패로, `deed_judged`를 승인/만족으로 읽지 않음 (marketing-66 계승)

## 선행 문서와의 관계

| 선행 문서 | 이 표에서의 역할 |
|-----------|----------------|
| marketing-65 (Trust Evidence) | `evidence_to_show` 컬럼의 기준 — 잡별 신뢰 증거를 권한 경계로 구체화 |
| marketing-66 (Context Map) | `user_delegates` 컬럼의 기준 — 잡별 user_intent에서 위임 범위 도출 |
| marketing-38 (No Autonomous Action) | `virtue_must_not_do` 공통 전제 |
| marketing-45 (Decision-Delegation) | `virtue_must_not_do` — 판결 프레임 금지 |

## 금지선 (prelaunch 적용)

- 신규 이벤트·tracking·privacy 변경: **0**
- public copy·llms.txt·FAQ·온보딩 카피 변경: **proposal-only (approval-needed)**
- API·MCP·external message·deploy·cost·권한 변경: **0**
- 이 문서 자체는 내부 docs-only — 공개 발행 불가

## 충돌 점검

| 선행 문서 | 확인 항목 | 충돌 여부 |
|-----------|----------|-----------|
| marketing-65 | J1-J4 신뢰 증거 표준 | 없음 — evidence_to_show에 계승 |
| marketing-66 | J1-J4 user_intent·문맥 흐름 | 없음 — user_delegates에 계승 |
| marketing-38 | No Autonomous Action | 없음 — 공통 전제로 유지 |
| marketing-45 | Decision-Delegation Risk | 없음 — virtue_must_not_do에 반영 |
| marketing-60 | prelaunch 금지선 | 없음 — 동일 금지선 적용 |

Conflict markers: 0  
신규 이벤트·tracking·privacy·public copy·deploy·external message·cost 변경: 0건

## Marketer 인수인계 (marketing-67)

**계승한 기준:**
1. Trust Evidence Inventory (marketing-65): J1-J4 잡별 신뢰 증거 → `evidence_to_show` 컬럼으로 실행 경계화
2. Agentic Context Map (marketing-66): J1-J4 user_intent·문맥 흐름 → `user_delegates` 컬럼의 위임 범위 근거
3. No Autonomous Action (marketing-38): 외부 행동 없음 = `virtue_must_not_do` 공통 전제

**이번에 새로 만든 것:**
- J1-J4별 5컬럼 권한 경계표 첫 정리 (user_delegates / virtue_may_do / virtue_must_not_do / human_decision_required / evidence_to_show)
- WEF/Capgemini ACAP "무엇을 허용할 것인가" 관점을 Virtue 내부 docs로 번역한 첫 문서

**다음 작업에 넘길 규칙:**
- onboarding·FAQ·public explainer 작성 시 이 표의 `virtue_must_not_do`와 `human_decision_required`를 사용자 안내 기준으로 사용 (approval-needed)
- first-10 관찰에서 "AI에게 무엇을 맡긴다고 느꼈는가" 질문 설계 시 이 표의 `user_delegates`를 잡별 기대 기준으로 사용
- llms.txt·public explainer에서 Virtue AI 설명 시 이 표의 `virtue_may_do`/`virtue_must_not_do` 경계를 기준으로 삼되 approval-needed 항목은 별도 승인 후 진행
- approval 없이 이 표 내용을 공개 발행하지 않음
