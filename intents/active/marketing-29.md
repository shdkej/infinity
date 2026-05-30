# marketing-29 Virtue AI outcome proxy dictionary 작성

- id: marketing-29
- status: in_progress
- priority: high
- permission: L2 agent-approved
- project: virtue
- type: strategy
- topics: ai-product,activation,trust,measurement,prelaunch
- goal: virtue-rebirth-app docs에 J1-J4 × 이벤트 × proxy type(activity/acceptance/curiosity/friction/retention) × quality condition × misread warning 표 추가
- success_criteria: 코드 diff 0, 신규 이벤트/속성 0, 기존 6개 이벤트 이름 drift 0, conflict marker 0, prelaunch decision-grade 금지선 포함
- context:
  - source: /home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-05-30-ai-outcome-proxy.md
  - artifacts: artifacts/marketing-29/
  - reference: Intercom outcome-based AI value framing, Reforge North Star quality 렌즈
- created_at: 2026-05-30T22:00Z
- prepare_report: reports/marketing-29/2026-05-30T2200Z-prepare.html

## 로컬 실행 프롬프트

```
Infinity Intent: marketing-29 Virtue AI outcome proxy dictionary 작성
Mode: execute_local
Required workflow: Use workflow-master first.
Find it under ~/.claude/skills/workflow-master/ and ~/.claude/agents/workflow-master.md
before falling back to repo-local .agent/workflows/workflow-master.md or WORKFLOW-MASTER.md.

Goal: virtue-rebirth-app/apps/web/docs/ai-outcome-proxy-dictionary.md 신규 작성

Prepared draft: infinity repo artifacts/marketing-29/ai-outcome-proxy-dictionary-draft.md
(로컬에서 git pull shdkej/infinity 또는 직접 읽기)

Context:
  - 이벤트 앵커: add_flow_started:72, deed_judged:106, deed_rerolled:149,
    deed_save_capped:167, deed_saved:183, level_up_viewed:199
  - J1 기록형 first value: deed_saved
  - J2 누적형 first value: deed_saved
  - J3 AI 호기심형 first value: deed_judged (저장 전 정상 종료)
  - J4 회고형 first value: deed_saved
  - 선행 문서: apps/web/docs/ 하위 (ai-judgment-trust-calibration-audit.md,
    onboarding-metrics-reading-table.md, traffic-source-reading-boundary-table.md 등)

Allowed: L0/L1 actions only (doc 1파일 추가)
Forbidden:
  - 신규 이벤트/속성/코드/계측 변경
  - 공개 카피/대시보드/세션리플레이 변경
  - 배포/외부발송/비용/시크릿/권한/개인정보 변경
  - 기존 first-value 매핑 재정의

Verification gates:
  1. 코드 diff 0 (apps/web/ 외 변경 없음)
  2. 신규 이벤트/속성 이름 0개
  3. 기존 6개 이벤트 이름 drift 0
  4. conflict marker 0
  5. prelaunch decision-grade 금지선 포함
  6. J1/J2/J4=deed_saved, J3=deed_judged first-value 재정의 0
  7. proxy type 5종(activity/acceptance/curiosity/friction/retention) 모두 등장
  8. misread warning 8개 이상

Report back to: reports/marketing-29/{timestamp}.html
(필수 HTML, 결론 2축 양식, ARTIFACT_RULES.md 참조)
```
