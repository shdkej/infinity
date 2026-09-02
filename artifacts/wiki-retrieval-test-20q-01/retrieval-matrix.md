# Agent Wiki 20문항 회수성 검증

## 범위와 방법

- 기준 시각: 2026-09-02 UTC
- 근거 범위: `agent-wiki/content/docs/`만 사용. raw source·외부 웹·일반 지식 보강은 사용하지 않았다.
- 판정: **Found**는 질문에 필요한 답과 locator가 모두 있는 경우, **Partial**은 일부만 있거나 정확한 수치·구체 항목이 없는 경우, **Not found**는 위키 근거가 없는 경우다.
- 도달 경로: `중앙`은 `index → source-category-map → 축 → 노드`, `검색`은 content/docs 전수 키워드 검색이다.

## 회수 매트릭스

| Q | 판정 | 위키로 확인한 답 | 근거 locator | 검색어·도달 |
| --- | --- | --- | --- | --- |
| Q1 | Found | 어시스턴트=규칙 기반, 에이전트=단일 목표의 넓은 작업, 에이전틱=완전 자율·다중 에이전트 | `mapped/deep-knowledge/ai.mdx` §생성형 AI의 진화 방향, L68–70 | `LLM 이후`, `어시스턴트`, `에이전틱`; 중앙·검색 |
| Q2 | Not found | GPT-5의 정확한 컨텍스트 길이·학습 cutoff은 기록되지 않았다 | `ai.mdx` §컨텍스트 길이에 대한 태도 L221–225는 일반 원칙뿐 | `GPT-5`, `context window`, `cutoff`; 검색 |
| Q3 | Not found | G.S.T.A.R의 각 요소는 기록되지 않았다 | 검색 결과 0 | `G.S.T.A.R`, `GSTAR`, 각 영문 요소; 검색 |
| Q4 | Partial | 역전파는 ML 기초 항목으로만 언급되며 작동 원리는 설명하지 않는다 | `mapped/deep-knowledge/ai.mdx` §왜 기초 ML 메모가 이 노드 안에 남아 있는가 L293, §남겨둘 기초 축 L301 | `역전파`, `back propagation`; 검색 |
| Q5 | Not found | PyPy/CPython/JIT의 두 핵심 기술은 기록되지 않았다 | 검색 결과 0 | `PyPy`, `CPython`, `JIT`; 검색 |
| Q6 | Found | 중심 정책·기준선은 먼저 고정하고, 세부 구현은 늦춰 교체 가능하게 남긴다 | `mapped/Fundamental/Architecture.mdx` §정책과 세부사항을 분리하려는 태도 L120–127; `insights/change-friendly-operating-structure.mdx` L33–35 | `policy`, `detail`; 중앙·검색 |
| Q7 | Not found | 외부 네트워크/로컬 파일 로딩의 각 기준 시간은 기록되지 않았다 | 관련 Architecture·Infra·Network 노드에 수치 없음 | `external network time`, `local file loading`; 검색 |
| Q8 | Partial | 쓰기·진실 기록 층과 빠른 읽기·조회/파생 판단 층을 분리한다. 조회 부하 격리·검색/추천 읽기 모델에서 유용하다는 근거가 있다 | `mapped/deep-knowledge/data.mdx` L250–251; `mapped/Fundamental/Architecture.mdx` L240–248; `insights/structure-before-scale.mdx` L19–24 | `CQRS`; 중앙·검색 |
| Q9 | Not found | Netflix MSA의 Junk food 4항목은 기록되지 않았다 | `Netflix`, `junk food` 검색 결과에 관련 항목 없음 | `Netflix`, `junk food`; 검색 |
| Q10 | Not found | Kubernetes의 정확한 4개 계층 추상화/패턴 목록은 기록되지 않았다 | `mapped/deep-knowledge/container.mdx` L215–224는 5개 운영 문제 구분, `mapped/Fundamental/Infra.mdx` L210–216은 운영 부담 | `Kubernetes`, `abstraction`, `hierarchy`; 중앙·검색 |
| Q11 | Found | 심플함은 공백 자체가 아니라 필요한 것만 남긴 의도·리듬·조화이며, 휑함과 다르다 | `mapped/Human/Balance.mdx` §조화는 깔끔함보다 의도된 다양성에 가깝다 L140–147 | `심플`, `휑`, `simple vs neat`; 검색 |
| Q12 | Partial | 구체 사례는 없지만, 규칙은 자율의 내면화가 가능한 환경이어야 하며 맥락·예외·관계 비용을 지우거나 위축시키면 한계가 있다 | `mapped/Human/Balance.mdx` L131–138, L221–229; `mapped/Human/Standard.mdx` L99–108 | `3만원`, `부정청탁`, `휴대폰 감시`, `통제 vs 자율`; 검색 |
| Q13 | Partial | 고정 주제는 8개다. 다만 단일 문서의 줄 수·리딩 시간 정확 기준은 없다 | `mapped/Communication/Blogging.mdx` L38–60, L88–96 | `만다라트 블로그`, `고정 주제`, `리딩 시간`; 검색 |
| Q14 | Not found | 반팔·팬티·양말·수건의 각 제한 수량은 기록되지 않았다 | 검색 결과에 수량 근거 없음 | `반팔`, `팬티`, `양말`, `수건`; 검색 |
| Q15 | Found | Work Log는 완료 목록이 아니라 판단 인터페이스다. 결정 맥락을 남겨야 평가·자기설명·다음 업무 산정·회고에 재사용된다 | `mapped/Integration/Work.mdx` §7. Work Log L123–139, §반복 판단 모델 L149–156 | `Work Log`, `의사결정 맥락`; 검색 |
| Q16 | Partial | TLS/HTTPS는 우선 상대 서버의 신원을 확인하는 표면으로 설명된다. 대칭키·공개키의 역할 분담까지는 기록되지 않았다 | `mapped/Fundamental/Architecture.mdx` §보안 메모는 신원과 책임 위치를 묻는 아키텍처 질문이다 L231–238 | `HTTPS`, `TLS`, `대칭키`, `공개키`; 검색 |
| Q17 | Partial | SSH는 서버가 공개키, 클라이언트가 비밀키를 갖는 책임 배치만 기록되어 있다. CI에서 GitHub의 정확한 등록 위치/방식은 없다 | `mapped/Fundamental/Architecture.mdx` L205–210, L231–234 | `CI`, `SSH`, `public key`, `private key`, `GitHub`; 검색 |
| Q18 | Found | 현업 문제를 문제은행에 많이 등록 → 해결 가능한 사람이 참여 → 큰 모수를 퍼널처럼 압축 → 고객 페르소나로 현장 감각 학습. 현장 경험자가 AI를 배우는 경로도 강조한다 | `mapped/Integration/Business.mdx` §대기업 혁신 사례도 결국 현장성과 문제 수집 구조로 해석된다 L206–212 | `GS그룹`, `이노베이션`, `퍼널`; 중앙·검색 |
| Q19 | Not found | 한강 작가의 도서정가제 옹호 논리와 근거는 기록되지 않았다 | `도서정가`, `한강`, `정가` 검색 결과 0 | `도서정가제`, `한강`; 검색 |
| Q20 | Found | Carrying Capacity는 유입보다 이탈·유지를 먼저 보게 해 제품 가치와 마케팅 투자 방향을 정하는 지표다 | `mapped/deep-knowledge/product.mdx` §Carrying Capacity는 유입보다 누수를 먼저 보게 만든다 L219–224 | `Carrying Capacity`; 중앙·검색 |

## 결과

- Found: 6/20 (30%)
- Partial: 6/20 (30%)
- Not found: 8/20 (40%)
- 답변 근거 또는 검색 감사 흔적: 20/20 (Not found는 답변 locator가 아니라 해당 키워드의 `content/docs/` 전수 검색 범위를 기록)
- 중앙 경로로도 노드까지 재현 가능한 Found: Q1, Q6, Q18, Q20. 나머지는 직접 키워드 검색이 핵심 진입점이었다.

## 결론과 개선 우선순위

1. **8×8의 문제는 노드 수가 아니라 query surface 부족**이다. 축과 노드는 존재하지만 Q2·Q3·Q5·Q7·Q9·Q10·Q14·Q19처럼 고유명사·정확 수치·정형 목록 질문을 받을 alias·FAQ·evidence locator가 없다.
2. 각 mapped 노드에 `질문별 alias → 답변 → source locator → 상태`를 갖는 작은 Retrieval Card를 추가하는 것이 우선이다. 새 대분류를 늘리기보다 검색어-문장 접점을 늘린다.
3. 수치·목록 질문은 `not-recorded`를 명시적으로 유지하되, 원문 검증 뒤 보강할 때에는 항목·단위·기준 시점과 함께 넣는다. 추론으로 채우면 이 테스트의 목적이 무너진다.
