# Virtue Agent-Readable Surface Audit

- intent: marketing-68
- created_at: 2026-06-19T00:00Z
- type: docs-only (L1)
- permission_level: L1 docs-only

## Scope

**허용:** live site와 repo의 public metadata/readme/docs read-only 확인, 기존 marketing artifacts 참조, L1 내부 감사표 작성.

**금지:** production code 변경, deploy, public copy 반영, robots/llms 실제 배포, privacy/tracking/PostHog 설정 변경, 외부 발송(external message), 비용(cost) 발생.

---

## 계승 기준

- **marketing-65** Trust Evidence Inventory: 신뢰 증거의 구조적·행동적·언어적 분류 계승
- **marketing-66** Agentic Context Map: J1-J4별 agent_misread_boundary 계승 — "J3 무저장 종료 = 정상", "저장 ≠ AI 판정 동의"
- **marketing-67** AI Authorization Boundary Table: J1-J4별 virtue_must_not_do / human_decision_required 계승
- **m46 (MARKETING_LEARNINGS)** Agent-Led Growth: read-about vs do-for-you 분리; Virtue = 사람 경험 본체 → do-for-you no-fit
- **m45 (MARKETING_LEARNINGS)** Decision-Delegation Risk: 판결 프레임 vs 관점 프레임 동사 구분 계승

---

## Surface Audit Table

| Surface | current evidence | agent may read | agent must not infer | human handoff wording (proposal-only) | launch-after reuse |
|---------|-----------------|----------------|---------------------|--------------------------------------|-------------------|
| Landing metadata (og:title, meta description, og:image alt) | 형태 예상: "매일의 행동을 기록하고 AI 관점을 받는 앱" — 직접 확인 미가능 (prelaunch) | 제품 목적 (행동 기록 + AI 관점 제공), 비자율 AI 설명 | 도덕 판단 자동 대행, 사용자 행동 결정 자동화, AI가 사용자 대신 저장 | "AI가 정리한 관점 — 마지막 저장은 내 선택" | SEO / AI search answer card 재사용 가능 (반영은 approval-needed) |
| Public README / repo docs | infinity 레포 존재 (private). virtue 레포 공개 여부 미확인. 공개 시 기술 스택·제품 개요 포함 예상 | 기술 스택, 제품 개요, 오픈소스 여부 | 사용자 데이터 구조 추론, 감정 패턴 파악, AI 자율 행동 가능 여부 | "AI는 판정·저장 모두 사용자 선택으로만 작동" | developer docs 기반 재사용 가능 (공개 여부 별도 확인 필요) |
| llms.txt 후보 | 미배포 (approval-needed). 이 표 공통 경계로 초안 작성 가능 | 제품 목적 요약, J1-J4 잡 설명 (read-about only), AI 비자율·비행동 명시 | 사용자 프라이빗 기록 접근 가능, 자동 행동 허용, 외부 에이전트 API 경로 존재 | "Virtue AI provides perspective on user-recorded actions. All saving and sharing decisions remain with the user. No autonomous action is taken on behalf of the user." | launch 후 AI search 가시성 draft로 재사용 (실제 배포는 approval-needed) |
| In-app 카피 (버튼·결과 카드·헤더) | marketing-67 / m45 확인: "AI 채점" 판결 프레임 vs "AI가 본 오늘" 관점 프레임 불일치. 에이전트 크롤 시 판결 프레임 그대로 노출 | 앱 내 결과 카드 텍스트 (read-only), UI 흐름 설명 | AI 채점 = 사용자 자기평가 합의, 저장 = 판정 승인, AI가 사용자 행동 결정·평가 | "AI가 본 오늘" 관점 프레임 일관 사용 (판결→관점 정렬은 proposal-only, m45 계승) | FAQ, public explainer "Virtue가 하지 않는 것" 섹션에 재사용 가능 |

---

## 공통 경계 (전 표면 적용)

### Agent May Read (공통)

- 제품이 무엇을 하는지: 행동 기록 후 AI 관점 제공
- 저장 여부가 사용자 결정임을 나타내는 설명
- AI가 외부 자율 행동을 하지 않는다는 사실

### Agent Must Not Infer (공통)

- AI가 사용자의 도덕 판단을 자동 대행한다
- 저장 = AI 결과에 동의 또는 AI 판정 승인
- Virtue가 사용자 행동·성격·감정을 자동 분류·저장한다
- 외부 API/MCP를 통한 에이전트 자율 실행이 가능하다

---

## Human Handoff Wording 후보 (proposal-only, 공개 반영은 approval-needed)

1. "AI가 본 오늘 — 마지막 저장은 내 선택" (관점 프레임, m45 계승)
2. "AI 판정이 아니라 AI 관점. 저장은 내 결정." (판결/관점 구분 명시)
3. "AI는 정리하고, 나는 선택한다." (최소 표현)
4. llms.txt 후보 문장 (EN): "Virtue AI provides perspective on user-recorded actions. All saving and sharing decisions remain with the user. No autonomous action is taken on behalf of the user."

---

## 구조적 제약 요약 (변경 금지, 이미 설계에 내재)

1. **외부 자율 행동 없음** (m38): 에이전트가 읽어도 "AI가 대신 뭔가를 하는 경로" 자체가 없음 → 오독 위험은 언어 레이어에만 존재
2. **사람 마지막 선택** (m45, marketing-67 human_decision_required): 저장·공유·재시도는 전부 사용자 결정 — 결과 후 선택 affordance로 구조적 보장
3. **Do-for-you 경로 없음** (m46): 현재 Virtue = read-about 전용 표면만 후보. API/MCP/programmatic auth는 approval-needed

---

## Zero-Change Confirmation

production code 변경: 0건. deploy 변경: 0건. public copy 반영: 0건. robots/llms 실제 배포: 0건. tracking/privacy/PostHog 변경: 0건. external message 발송: 0건. cost 발생: 0건.

---

## Marketer 인수인계

**계승한 기준:** marketing-65 신뢰 증거 분류, marketing-66 agent_misread_boundary, marketing-67 virtue_must_not_do / human_decision_required, m46 read-about vs do-for-you, m45 판결/관점 동사 프레임

**이번에 새로 배운 것:** agent may read / agent must not infer 경계는 표면마다 달라질 필요가 없다. Virtue의 구조적 보호(외부 자율 행동 없음, 사람 마지막 선택)가 이미 작동하므로, 공통 경계 1세트가 전 표면에 적용된다. 표면별 차이는 "현재 content 확인 가능 여부"와 "launch-after 재사용 경로"뿐이다.

**다음 작업에 넘길 규칙:**
- llms.txt 초안 작성은 이 표의 공통 경계를 그대로 사용 가능 (작성 L1, 실제 배포 approval-needed)
- In-app 카피 판결→관점 프레임 정렬은 이 표 "In-app 카피" 행을 근거로 proposal 작성 (공개 변경 approval-needed)
- llms.txt 배포·robots.txt 변경 시 "Do-for-you 경로 없음" 구조적 제약을 명시해야 함
