# Knowledge Lab 승격 피드백루프 구현 계획

## 목표

승격된 지식이 후속 Intent에 재사용되고 효과를 냈는지 추적하여 다음 승격 판단에 반영합니다.

## 작업

1. 기존 promotion-index와 knowledge-loop 읽기 모델의 경계를 확인한다.
2. promotion receipt·재사용·결과·재평가를 기록하고 조회하는 결정적 스크립트를 추가한다.
3. 데일리 Knowledge Lab promotion 크론이 새 승격을 기록하고 만기 항목을 재평가하도록 지시를 갱신한다.
4. 단위 fixture와 실제 dry-run으로 스키마·재평가·dashboard read model을 검증한다.

## 완료 기준

- 원장은 원격 Knowledge Lab에 커밋·푸시된다.
- 후속 Intent가 promotion id를 기록할 수 있다.
- 데일리 크론이 기존 1개 스케줄 내에서 재평가를 수행한다.
- 테스트와 원격 SHA 검증을 통과한다.
