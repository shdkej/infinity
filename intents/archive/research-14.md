# research-14: 모놀리스 아키텍처 보완 맥락 조사

- id: research-14
- status: archived
- completed_at: 2026-06-16T00:02Z
- projects: [infinity, research-bank]
- task_type: research
- topics: [software-architecture, history, systems-design]
- result_summary: 모놀리스는 특정 새 아키텍처의 발명품이라기보다 분산 실행·분산 데이터·독립 배포가 만들 복잡도를 피하는 응집형 기본값이었고, 이후 규모가 커지며 그 응집이 병목으로 바뀌었다.
- artifacts:
  - path: artifacts/research-14/monolith-architecture-context.md
    role: research
    note: 모놀리스가 보완한 문제, 얻은 장점, 이후 한계, 사후적 명명 맥락 정리
- reports:
  - path: reports/research-14/2026-06-16T0002Z-local.html
    role: final
- commits:
  - repo: infinity
    sha: 2b8c333
    note: research-14 artifact/report/archive update
- urls:
  - url: https://martinfowler.com/articles/microservices.html
    note: microservices와 monolithic style 대비 근거
  - url: https://martinfowler.com/bliki/MonolithFirst.html
    note: monolith-first 전략과 초기 경계 불명확성 근거
  - url: https://martinfowler.com/articles/microservice-trade-offs.html
    note: microservices trade-off 근거
  - url: https://www.ibm.com/think/topics/monolithic-architecture
    note: monolithic architecture 정의 근거
  - url: https://csrc.nist.gov/pubs/sp/800/204/final
    note: microservices의 독립 개발·배포·확장 장점과 대비 근거
- next_actions:
  - No continuation: 조사형 질문에 대한 재사용 가능한 답변 산출물이 완성되었고 추가 구현·배포·승인 단계는 없다.

## Result

모놀리스는 "무엇을 보완하기 위해 달성되었나"라는 질문에 대해, **분산 시스템을 감당하기 전 단계의 복잡도 흡수 장치**로 보는 것이 가장 정확하다. 초기에는 네트워크·데이터 일관성·배포 자동화·운영 관측·팀 조율 비용을 한 실행 단위 안으로 접어 넣어 개발과 배포를 단순하게 만들었다. 나중에는 같은 특성이 전체 재배포, 독립 확장 어려움, 팀 간 충돌, 내부 결합 누적으로 바뀌었다.

## Gates

- concise Korean answer: pass
- 3-5 key points: pass
- comparison section `보완한 것 / 얻은 것 / 나중에 생긴 한계`: pass
- historical framing note: pass
- reliable source-backed reasoning: pass
- no code/deploy/public/external action: pass
- HTML report gate: pass
