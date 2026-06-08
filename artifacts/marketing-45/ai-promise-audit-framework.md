# marketing-45 — AI 약속 문장 decision-control 감사 프레임워크

> Cloud prepare 단계 산출물. Local Claude Code가 virtue-rebirth-app docs에 최종 감사표를 작성할 때 이 프레임워크를 기반으로 한다.
> Source: Gartner 2026 AI Shopping Survey — 사용자는 AI의 완전한 결정 대행보다 조사·비교·선택권 강화에 더 열려 있다.

---

## 1. 분류 기준 (Classification Guide)

### Autonomy-Overclaim (위험 신호)

AI가 최종 결정권자로 읽힐 수 있는 언어 패턴:

| 패턴 | 예시 | 위험 이유 |
|------|------|-----------|
| 단정형 동사 | "~입니다", "~한 덕목입니다" | AI가 덕목을 확정짓는 것으로 오해 |
| 판정/결정 명사 | "AI 판정", "AI 결정", "AI 평가" | verdict/judgment 뉘앙스, 사용자 개입 여지 없어 보임 |
| 의무형 조동사 | "~해야 합니다", "~이 맞습니다" | 선택 아닌 지시로 읽힘 |
| 최상급/절대어 | "확실히", "반드시", "분명히" | AI 분석을 사실로 과장 |

### Choice Empowerment (안전 신호)

사용자가 판단 주체로 읽히는 언어 패턴:

| 패턴 | 예시 | 이유 |
|------|------|------|
| 제안형 동사 | "~로 보입니다", "~일 수 있습니다" | AI는 의견, 사용자가 결정 |
| 보조 명사 | "AI 분석", "AI 의견", "AI 참고" | 분석 도구로 포지셔닝 |
| 사용자 주도 동사 | "확인해보세요", "저장하시겠어요?" | 선택권을 사용자에게 |
| 불확실성 표현 | "데이터 기준으로는", "이 기준에서 보면" | AI 한계 명시 |

---

## 2. 표면별 감사 체크리스트

### 2-1. 홈 페이지 (Home)

감사 항목:
- [ ] 랜딩 헤드라인: AI가 "판정"하는가 vs "도움"을 주는가?
- [ ] 가치 제안 문장: 사용자가 선택 주체인가?
- [ ] CTA 버튼: 지시형인가 제안형인가?

J3 (deed_judged) 연관 위험:
- J3 사용자는 first value가 AI 판정 자체. "판정"을 강조하면 AI 권위로 오해 가능.
- 안전 방향: "AI가 당신의 덕목을 분석해 보여드립니다" (보조 도구)

J1/J2/J4 연관 고려:
- first value는 deed_saved. 홈에서 AI를 너무 강조하면 저장 행동까지 가는 여정을 축소 가능.

### 2-2. /add 페이지

감사 항목:
- [ ] 입력 폼 안내 문구: AI가 분석할 것임을 어떻게 설명하는가?
- [ ] 제출 버튼 주변 텍스트: AI 판정 결과에 대한 기대를 어떻게 세우는가?
- [ ] 결과 대기 메시지: AI가 "결정 중"인가 "분석 중"인가?

위험 패턴: "AI가 판정합니다" → 권위 프레임
안전 패턴: "AI가 함께 살펴봅니다" → 협업 프레임

### 2-3. 결과 카드 (deed_judged 후)

이것이 핵심 감사 대상. J3는 deed_judged가 first value이므로 결과 카드 문장이 trust에 직결.

감사 항목:
- [ ] AI 판정 결과 제목: 단정인가 제안인가?
- [ ] 덕목 분류 문장: "~입니다" vs "~로 보입니다"
- [ ] 점수/평가 설명: 절대값인가 참고값인가?
- [ ] "저장" 이전 문장: 저장 행동을 강요하는가 제안하는가?

m24/m38 경계 준수:
- m24: trust-control 최초 정의 — AI 판정을 권위로 포장하지 않는다
- m38: trust-control 재확인 — 사용자 선택권이 명시적이어야 한다
- **재정의 금지**: 이 감사표가 m24/m38 경계를 변경하면 안 된다. 경계를 적용하는 표다.

J3 특이사항:
- J3에서 저장 없이 닫히는 것이 **정상**일 수 있음 (marketing-44 결론 계승)
- 결과 카드가 J3에서 deed_judged = first value → 카드가 너무 강하게 저장을 유도하면 J3의 정상 종료를 friction으로 오해할 위험

### 2-4. Agent Answer Snippet (내부 AI 응답 표시)

감사 항목:
- [ ] 응답 prefix: "AI" vs "AI가 생각하기에"
- [ ] 확신도 표현: 단정인가 추정인가?
- [ ] 사용자에게 선택을 돌리는 문장이 있는가?

내부 표시지만 tone 일관성이 외부 표면에 영향. "agent answer"가 "AI 명령"처럼 읽히면 안 됨.

---

## 3. 승인 필요 경계 (Approval-Needed Boundary)

이 감사표는 docs-only. 아래 항목은 이 감사표 범위 밖이며 별도 승인 필요:

| 항목 | 이유 |
|------|------|
| 실제 앱 카피 변경 | 배포 승인 필요 (L2 이상) |
| 이벤트/속성 신규 추가 | tracking 변경 → L2+ |
| A/B 테스트 트리거 | 배포/비용 변경 가능 |
| 재활성화 메시지 발송 | 외부 발송 → L2 명시 승인 |
| m24/m38 경계 재정의 | 사용자 명시 승인 없이 불가 |

---

## 4. 로컬 실행 프롬프트 (Local Claude Code용)

```
Infinity Intent: marketing-45 Virtue AI 약속 문장 decision-control 감사표
Mode: execute_local
Workflow: simple-doc (신규 docs 파일 1개, 멀티파일 변경 없음)

Goal:
virtue-rebirth-app의 apps/web/docs/ai-promise-audit-table.md를 신규 작성한다.
이 파일은 홈·/add·결과 카드·agent answer snippet 표면의 AI 약속 문장을
decision-control 관점으로 분류한 감사표다.

Context:
- Source note: /home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-07-ai-control-not-decision.md
- Framework: Infinity artifacts/marketing-45/ai-promise-audit-framework.md
- Prior boundaries: m24/m38 trust-control (재정의 금지)
- First value: J1/J2/J4=deed_saved:183, J3=deed_judged:106

Allowed:
- virtue-rebirth-app apps/web/docs/ 내 신규 파일 1개 작성
- source note path 인용
- L2 agent-approved (docs-only, 되돌림 가능, 비용 0, 배포/외부 발송 0)

Forbidden:
- 앱 카피 실제 변경
- 신규 이벤트/속성/tracking 추가
- m24/m38 재정의
- 배포, 외부 메시지

Verification gate:
- source note path 인용 확인
- 이벤트 앵커 drift 0 (deed_judged:106, deed_saved:183 등 변경 없음)
- 공개 앱 카피/코드 diff 0
- conflict marker 0

Report back to: reports/marketing-45/{timestamp}.html
```

---

## 5. 완료 기준 체크리스트

- [ ] `apps/web/docs/ai-promise-audit-table.md` 파일 생성
- [ ] 4개 표면(홈·/add·결과 카드·agent snippet) 전부 행 있음
- [ ] 각 행: autonomy-overclaim 위험 등급 + 현재 문구 패턴 + 선택권 강화 후보 + approval-needed 조건
- [ ] m24/m38 경계 재정의 없음
- [ ] first value 매핑 J1/J2/J4=deed_saved, J3=deed_judged 재정의 없음
- [ ] source note path 인용
- [ ] 신규 이벤트/카피/코드/배포/외부 발송 0
- [ ] HTML report `reports/marketing-45/{timestamp}.html` (gate 통과)
