# Virtue Agent-Led Growth Fit/No-Fit 경계표

작성: 2026-06-08 | Source: marketing-46 | 반영 기준: MARKETING_LEARNINGS.md m45/m38/m08/m25

## 읽기 전 공통 전제

- Virtue는 prelaunch 인간-우선 성찰 앱이다. AI는 외부 행동 없이 판정만 보여준다.
- Agent-led growth: AI 에이전트(LLM, MCP 클라이언트, automation tool)가 Virtue를 직접 호출하거나 Virtue 결과를 배포 채널로 사용하는 성장 방식
- 이 표는 docs-only이며, 공개 카피·API/MCP 배포·tracking 변경은 모두 approval-needed다.

## 1. 지금 맞는 것 (Fit Now)

| 항목 | 설명 | 근거 |
|------|------|------|
| 수동 발견 가능성 | `llms.txt`에 Virtue가 무엇인지·무엇이 아닌지 설명 (이미 있으면 현행 유지) | AI가 사용자에게 Virtue를 설명할 때 정확한 언어를 쓰게 함 |
| OG/공유 메타데이터 | 사용자가 deed 결과를 공유할 때 AI가 URL 내용을 요약·인용할 수 있게 하는 기본 OG | passive discoverability, 자율 행동 없음 |
| 자연어 포지셔닝 문서 | "Virtue는 AI가 자동으로 결정하지 않고 사람이 마지막 선택권을 갖는다"를 명시한 내부 docs | m38/m45 계승: non-autonomous 포지션을 AI가 올바르게 요약하게 함 |
| AEO 설명 텍스트 (passive) | AI Search/Overview가 Virtue를 질문받았을 때 인간-우선 성찰 앱으로 설명하도록 지원하는 FAQ/docs | passive, 사람 방문 전제, 자동 API 호출 없음 |

## 2. 지금 맞지 않는 것 (No-Fit Now)

| 항목 | 이유 | 주의 |
|------|------|------|
| 외부 에이전트가 호출할 API 엔드포인트 | 인간 first value가 아직 실 사용자로 검증 안 됨; 에이전트 트래픽이 섞이면 사람 신호 분리 불가 | m25 Traffic Source Before Metrics |
| MCP server 구현 | Virtue의 non-autonomous trust 프레임을 "에이전트가 Virtue를 대신 쓴다"로 뒤집음 | m38 No Autonomous Action Bounds The Trust Question |
| 에이전트 배치 처리 / 자동 스케줄링 | 사용자가 아닌 에이전트가 deed를 제출하면 J1~J4 first value 매핑 전체가 오염 | m06 First Value Mapping |
| API 접근 과금 / 유료화 | retention 기준선도 없는데 API 수요 측정 불가 | m28 Monetization Boundary |
| 에이전트 온보딩 문서 | 지금 쓰는 사람이 없는 기능을 문서화하면 혼란 + 사람-first 메시지 희석 | m08 Prelaunch Decision Boundary |
| `robots/sitemap/llms.txt`에서 에이전트 호출 허용 명시 | llms.txt는 발견 가능성이지 실행 허가가 아니다; 혼동 위험 | m38, m45: verb frame 위험 |

## 3. 나중에 재검토할 조건 (Launch/Post-Launch Gate)

아래 조건이 모두 충족되면 agent-led growth 가능성을 재검토한다.

| 조건 | 체크 |
|------|------|
| 실 사용자 50명+ first value (J1/J2/J4 `deed_saved`, J3 `deed_judged`) 도달 확인 | □ |
| D7 retention 관찰 창 확보 (m37 Correlation Readiness) | □ |
| J1~J4 분포 파악 (어떤 잡이 반복 사용 가능성이 높은가) | □ |
| synthetic/mock/self-test 완전 분리 기준 확립 (m25) | □ |
| 에이전트 트래픽과 사람 트래픽을 구별할 측정 계획 수립 (approval-needed) | □ |
| 적어도 1개 잡에서 "에이전트가 부르면 인간-우선 trust 프레임이 유지되는가" 설계 검토 | □ |

## 4. 금지선 (Forbidden)

- 에이전트가 사람 대신 deed를 제출하는 흐름 (trust 프레임 파괴)
- "AI가 Virtue를 통해 자동 스케줄링한다"는 약속 문장 (m45 verb frame 위험)
- API/MCP 배포 없이 API를 있다고 표현하거나 암시하는 카피
- 에이전트 호출 허용을 approval 없이 llms.txt에 추가
- API 수요를 선 측정 없이 "AI 제품이면 당연히 API 필요"로 가정

## 5. 기존 기준 계승 체크

| 기준 | 충돌 여부 |
|------|----------|
| Decision-Delegation Risk Rides The Verb (m45) | 계승 — agent-led 마케팅 카피에서 판결 동사 사용 금지 |
| No Autonomous Action Bounds The Trust Question (m38) | 계승 — API/MCP 추가 = non-autonomous 프레임 훼손 |
| Prelaunch Decision Boundary (m08/m11/m14/m22/m23) | 계승 — 인간 first value 미검증 전 에이전트 기능 금지 |
| Traffic Source Before Metrics (m25) | 계승 — 에이전트 트래픽 추가 전 분리 계획 필수 |

---
_이 표는 proposal-only 분석이며, 공개 카피·API·MCP·tracking·배포·외부발송·비용·권한 변경은 approval-needed_
