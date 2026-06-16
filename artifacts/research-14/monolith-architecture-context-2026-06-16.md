# 모놀리스 아키텍처 보완 맥락 조사

*research-14 | 2026-06-16 | Infinity Heartbeat*

## 핵심 답변

"모놀리스 아키텍처"는 의도적으로 설계된 아키텍처 패턴이 아니다. 초기 소프트웨어 시대(1960–1990년대)에는 분산 시스템이 일반적이지 않았기 때문에 단일 프로세스에서 실행되는 소프트웨어가 기본값이었고, "모놀리스"라는 명칭은 마이크로서비스 운동이 부상한 2012–2014년경 사후에 붙여진 대비 용어다.

## 5가지 핵심 포인트

### 1. "모놀리스"는 사후 명명이다
초기 소프트웨어 개발자들은 "모놀리스를 선택"한 것이 아니었다. 단일 프로세스로 작동하는 방식이 당시의 자연스러운 기본값이었다. Sam Newman(*Building Microservices*, 2015), Martin Fowler 등이 마이크로서비스를 설명하면서 기존 방식을 "monolith"로 소급 명명했다. Netflix, Amazon 등이 2010년대 초반 분산 아키텍처로 전환하면서 이 용어가 대중화되었다.

### 2. 분산 시스템의 복잡성을 원천 제거했다
분산 시스템에서 발생하는 네트워크 지연, 부분 장애(partial failure), 직렬화/역직렬화 오버헤드, 서비스 간 인증이 모놀리스에는 없다. 모든 컴포넌트가 같은 메모리 공간에서 직접 함수 호출로 통신하므로 응답 속도와 안정성이 높다.

### 3. 트랜잭션과 데이터 일관성 관리가 단순하다
하나의 데이터베이스, 하나의 트랜잭션 매니저로 ACID 속성을 쉽게 구현할 수 있다. 분산 트랜잭션(2PC, Saga 패턴 등)의 복잡성이 없다.

### 4. 배포·운영 단위가 하나다
빌드 아티팩트가 하나이므로 배포 파이프라인이 단순하다. 로깅, 모니터링, 디버깅, 트레이싱 모두 단일 프로세스를 대상으로 하면 된다.

### 5. 팀 규모가 작을 때 개발 속도가 빠르다
공유 코드베이스에서 직접 함수를 호출하므로 인터페이스 설계·버전 관리 오버헤드 없이 빠르게 개발할 수 있다. IDE 디버거가 전체 스택에 즉시 적용된다.

## 비교: 보완한 것 / 얻은 것 / 나중에 생긴 한계

| 구분 | 내용 |
|------|------|
| **보완한 것** | 분산 실패·네트워크 오버헤드·데이터 불일치 위험·배포 복잡도·개발 도구 분산 |
| **얻은 것** | 단순한 개발 모델, 빠른 함수 호출 성능, ACID 트랜잭션, 단일 배포 파이프라인, 쉬운 디버깅 |
| **나중에 생긴 한계** | 선택적 확장 불가(전체만 확장), 기술 스택 고정, 배포 단위가 커서 배포 위험 증가, 대형 팀에서 코드 충돌(Conway's Law), 모듈 간 경계 없이 커지면 인지 부하 급증, 장애 시 전체 다운 위험 |

## 사후 명명에 대한 역사적 맥락

"모놀리스"는 **목표 아키텍처가 아니라 대비 개념**으로 등장했다.

- 1990년대까지: SOA 논의가 시작되었지만 대부분의 엔터프라이즈 시스템은 단일 WAR 배포 모델로 운영됨
- 2004–2008: SOA가 ESB(Enterprise Service Bus)와 함께 확산되었으나 복잡성 문제로 비판받음
- 2012–2014: Netflix, Amazon, Twitter가 분산 아키텍처로 전환 성공 사례를 발표하면서 "마이크로서비스"가 업계 트렌드로 부상. 이 시점에 기존 방식을 "monolith"로 명명하는 담론이 형성됨
- 2016–현재: "Modular Monolith" 개념이 등장. 모놀리스를 의도적 선택으로 보는 시각이 재평가됨. Shopify, Stack Overflow 등이 모놀리스의 장점을 재조명

### 핵심 인용
> "Most of what the industry calls microservices is really just distributed monoliths."

> "Don't start with a microservices architecture. Start with a monolith, and only decompose it when you have a clear need." — Martin Fowler

## 출처 근거

- Martin Fowler, "MonolithFirst" (martinfowler.com, 2015)
- Sam Newman, *Building Microservices* (O'Reilly, 2015, 2nd ed. 2021)
- Eric S. Raymond, *The Art of Unix Programming* (2003)
- Adrian Cockcroft, Netflix 기술 블로그 (2012–2014)
- Shopify Engineering Blog, "Deconstructing the Monolith" (2019)
- Stack Overflow Engineering Blog, "Stack Overflow: The Architecture" (ongoing)

---
*산출 범위: 코드 변경·배포·외부 발송·계정 액션 0. 순수 조사 아티팩트.*
