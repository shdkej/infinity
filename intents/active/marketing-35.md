# marketing-35: Virtue 잡별 온보딩 체크리스트 감사표 작성

- id: marketing-35
- status: in_progress
- priority: medium
- permission: L1/L2 internal documentation only
- projects: [virtue]
- task_type: strategy
- topics: [onboarding, activation, checklist, prelaunch]
- goal: J1~J4 잡별로 checklist-eligible action, product bumper, contextual fallback, do-not-include 항목을 표로 정리한 내부 문서 1개 작성
- success_criteria: 신규 내부 문서 1개에 J1~J4별 체크리스트 항목을 분리 정리하고, 기존 first value/activation registry/product-body-vs-bumper 문서와 충돌 0
- context:
  - source: knowledge-lab/source/external-links/marketing/2026-06-02-action-oriented-onboarding-checklists.md
  - output_target: /home/ubuntu/dev/virtue-rebirth-app/apps/web/docs/job-onboarding-checklist-audit.md
  - related_docs: activation-candidate-registry.md (m33), product-body-vs-bumper-boundary-table.md (m31), first-session-jtbd-matrix.md (m06)
- current_state: Cloud prepare 완료. 문서 초안은 artifacts/marketing-35/job-onboarding-checklist-audit.md에 저장됨. 로컬 실행 대기.
- next_action: 로컬 Claude Code에서 artifacts/marketing-35/job-onboarding-checklist-audit.md 초안을 virtue-rebirth-app/apps/web/docs/job-onboarding-checklist-audit.md로 복사·정리·커밋·push
- prepared_at: 2026-06-02T06:00Z

## 로컬 실행 프롬프트

```
Infinity Intent: marketing-35 Virtue 잡별 온보딩 체크리스트 감사표 작성
Mode: execute_local
Workflow: simple-doc (단일 docs-only 파일 작성)

Goal: artifacts/marketing-35/job-onboarding-checklist-audit.md 초안을
      /home/ubuntu/dev/virtue-rebirth-app/apps/web/docs/job-onboarding-checklist-audit.md로
      복사하고, 기존 선행 문서들과 충돌이 없는지 확인 후 커밋·push.

Context:
  - 초안 위치: /home/user/infinity/artifacts/marketing-35/job-onboarding-checklist-audit.md
  - 출력 위치: /home/ubuntu/dev/virtue-rebirth-app/apps/web/docs/job-onboarding-checklist-audit.md
  - 관련 선행 문서 (충돌 확인 대상):
    - apps/web/docs/activation-candidate-registry.md
    - apps/web/docs/product-body-vs-bumper-boundary-table.md
    - apps/web/docs/first-session-jtbd-matrix.md
    - apps/web/docs/onboarding-metrics-reading-table.md
    - apps/web/docs/first-session-friction-observation-protocol.md

Allowed: L0/L1 actions (doc-only file write + git commit/push)
Forbidden: 신규 이벤트·속성·코드·카피·계측·배포·외부발송·비용·권한 변경 0

Verification:
  1. git diff --stat apps/web/src apps/ios/Sources → 빈 출력이어야 함
  2. git diff --stat HEAD → docs 1파일만이어야 함
  3. 충돌 마커 검색: grep -n "^<<<<<<\|^>>>>>>\|^======" 결과 0
  4. 이벤트 이름 drift 확인: deed_judged/deed_saved/add_flow_started/deed_rerolled/deed_save_capped/level_up_viewed 이름 일치

Report back to: reports/marketing-35/{timestamp}-local.html (HTML 필수, 결론 2축)
```
