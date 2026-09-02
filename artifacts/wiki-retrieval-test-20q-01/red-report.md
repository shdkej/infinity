# Red 검증 — wiki-retrieval-test-20q-01

- 판정: **PASS**
- 확인: Agent Wiki `content/docs/`만 근거로 사용했고, 20개 문항의 답변·부분 답변·미확인을 구분했다.
- 수정: 최초 집계 오류를 Found 6 / Partial 6 / Not found 8 (30% / 30% / 40%)으로 바로잡았고, 미확인 항목은 문서 근거가 아닌 검색 감사 흔적으로 표현을 낮췄다.
- 요청 적합성: 8×8 목차의 실제 회수 성능과 병목을 보여 주며, 외부 지식으로 빈칸을 채우지 않았다.
- 다음 액션: alias·FAQ·evidence locator를 작은 Retrieval Card로 보강하는 별도 Intent를 검토한다.
