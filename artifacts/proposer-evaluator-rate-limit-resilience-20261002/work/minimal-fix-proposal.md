# evaluator rate-limit 최소 수정안

## 제안

1. rate-limit 재시도는 고정 상한(예: 2회)과 backoff를 둔다.
2. 상한 도달 시 침묵 실패 대신 `rate_limit_exhausted` 구조화 결과를 남긴다.
3. 원래 평가 결과와 `failureAlert` 계약은 변경하지 않고, 진단 메타데이터만 별도 필드로 추가한다.
4. 외부 runtime에서 정상 경로·rate-limit 경로·alert 경로를 각각 fixture로 검증한다.

## 적용 경계

실제 runner와 automation payload가 확인되고 사용자 승인이 도착하기 전에는 구현·외부 호출·runtime 검증을 실행하지 않는다.
