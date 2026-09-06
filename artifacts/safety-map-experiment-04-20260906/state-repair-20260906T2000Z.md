# 상태 정정 — 완료 task plan과 Active lane 불일치

- 관찰: `task-plan.json`의 모든 leaf가 `done`이지만 intent는 `Active`에 남아 있었다.
- Archive 불충족: 최종 실행 HTML report와 Archive 필수 지식 판정(`knowledge_status`, `knowledge_decision`, `knowledge_targets`, `knowledge_reflection`, `knowledge_commit`)이 없다.
- 결정: 완료를 주장하거나 Archive하지 않는다. intent를 `Waiting`으로 옮겨 final report·지식 판정·Archive 원장 전이를 별도 재개 조건으로 남긴다.
- 유지 경계: 현재 라이브 UI의 `근거 없음`·적격 입력 0·no-render는 후보 적격성, 신호, 핀, 점수, 경로 또는 안전·위험 주장 권한을 만들지 않는다.
