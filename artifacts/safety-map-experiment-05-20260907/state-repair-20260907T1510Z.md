# 상태 복구 — 실행 leaf 완료 후 Archive gate 대기

## 관찰

T1.1–T5.3은 모두 `done`이지만 Intent가 `Active` lane에 남아 있어 dispatcher의 `task_plan_has_no_active_or_pending_task` 계약을 위반했다.

## 역할 판단

- **Planner:** 실행 leaf 종료와 Archive 승인을 분리한다. 최종 HTML report와 지식 판정이 없으므로 Active 유지나 완료 선언은 불가하다.
- **Developer:** T5.3의 구현·배포·라이브 검증 산출물은 보존한다. 새 코드·배포·rollback은 필요하지 않다.
- **Marketer:** 제한적 행동 보조 UI를 위험 지도·안전 추천으로 확대하지 않는다.
- **Operator:** Archive에 필요한 최종 report·원격 검증·지식 판정이 생길 때만 terminal lane 전이를 수행한다.

## 상태 전이

`Active → Waiting`

## 재개 조건

1. `reports/safety-map-experiment-05-20260907/{timestamp}.html` 최종 report를 만든다.
2. `knowledge_status`, `knowledge_decision`, `knowledge_targets`, `knowledge_reflection`, `knowledge_commit` 지식 판정을 기록한다.
3. Red PASS 및 원격 HEAD==origin/main을 재확인한 뒤 Archive를 검토한다.

현재는 이 조건이 없으므로 Archive 또는 완료를 주장하지 않는다.
