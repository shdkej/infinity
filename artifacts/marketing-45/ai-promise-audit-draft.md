# marketing-45 · AI 약속 문장 decision-control 감사표 — 구조 초안

> Cloud prepare 단계에서 작성한 감사표 구조. Local이 source note를 읽고 실제 카피를 채운다.

## 배경

Gartner 2026 AI shopping survey: 사용자는 AI의 완전한 결정 대행보다 조사·비교·선택권 강화에 더 열려 있다.
Virtue의 AI 판정 문장이 "AI가 덕을 결정한다"로 읽히면 신뢰/제어권 리스크 발생.

Source note: `/home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-07-ai-control-not-decision.md`

**핵심 구분:**
- 결정 대행 = AI가 당신의 행동을 판정한다 / AI가 옳고 그름을 결정한다
- 선택권 강화 = AI가 참고 관점을 제공한다 / 당신이 최종 판단한다

## 분류 기준

| 유형 | 정의 | 위험 신호 | 선택권 강화 예시 |
|------|------|-----------|------------------|
| 결정 대행 (위험) | AI가 덕/비덕을 단정하는 주체 | "AI가 판단했습니다", "덕스럽지 않습니다" | — |
| 선택권 강화 (목표) | AI가 관점 제공, 사용자가 최종 결정 | — | "AI 관점으로 보면 ~", "참고해보세요" |
| 경계 (approval-needed) | 판단 주체가 불명확한 문장 | 수동태 + AI 주어 조합 | 구체적 주어 명시로 해결 |

## 제품 표면별 감사표

### 홈 (Home)

| 표면 위치 | 현재 카피 | 분류 | autonomy-overclaim 위험 | 선택권 강화 후보 | approval 필요 |
|-----------|----------|------|------------------------|-----------------|---------------|
| 히어로 헤드라인 | [local 조회 필요] | | | | |
| 서브헤드 / 설명 | [local 조회 필요] | | | | |
| AI 기능 설명 문구 | [local 조회 필요] | | | | |

### /add 페이지

| 표면 위치 | 현재 카피 | 분류 | autonomy-overclaim 위험 | 선택권 강화 후보 | approval 필요 |
|-----------|----------|------|------------------------|-----------------|---------------|
| 입력 안내 문구 | [local 조회 필요] | | | | |
| AI 판정 트리거 전후 | [local 조회 필요] | | | | |
| 결과 예고 / 로딩 문구 | [local 조회 필요] | | | | |

### 결과 카드 (deed_judged:106 직후)

| 표면 위치 | 현재 카피 | 분류 | autonomy-overclaim 위험 | 선택권 강화 후보 | approval 필요 |
|-----------|----------|------|------------------------|-----------------|---------------|
| 판정 결과 헤드라인 | [local 조회 필요] | | | | |
| AI 근거 설명 | [local 조회 필요] | | | | |
| 저장 CTA (deed_saved:183) | [local 조회 필요] | | | | |

### Agent answer snippet (내부)

| 표면 위치 | 현재 카피 | 분류 | autonomy-overclaim 위험 | 선택권 강화 후보 | approval 필요 |
|-----------|----------|------|------------------------|-----------------|---------------|
| 판단 문장 시작부 | [local 조회 필요] | | | | |
| 근거 인용 패턴 | [local 조회 필요] | | | | |
| 확신 강도 표현 | [local 조회 필요] | | | | |

## 기존 기준 (재정의 금지)

- first value 매핑: J1/J2/J4=deed_saved, J3=deed_judged
- trust-control 경계: m24/m38 (MARKETING_LEARNINGS.md)
- event anchor (drift 0): add_flow_started:72, deed_judged:106, deed_saved:183

## 검증 게이트

- [ ] source note path 인용
- [ ] 기존 이벤트 앵커 drift 0
- [ ] 공개 앱 카피/코드 diff 0
- [ ] conflict marker 0
- [ ] 승인 없이 배포/외부 메시지 없음
- [ ] 기존 first value 매핑 재정의 없음
