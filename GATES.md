# Approval Gates

> L2 권한이 필요한 액션의 승인 대기 큐.
> Heartbeat Agent가 추가하고, 사용자가 Telegram으로 응답한다.

## 대기 중

### [ops-01] weekly-main-workspace-autopush git sync를 결정적 스크립트로 이관
- requested: 2026-07-04 04:00 UTC
- action: openclaw workspace에 `system/scripts/weekly_workspace_sync.sh` 신규 생성 + 해당 크론 command payload를 스크립트 경로로 전환, 첫 실행 push 동반 테스트
- reason: self-healer가 동일 git diff exit-code 실패에 프롬프트 패치 5겹 누적; LLM 판단 불필요한 git sync를 결정적 스크립트로 교체하면 패치 루프 자체가 사라짐 (CRON_REDESIGN_2026-07-04.md 진단 5, 변경안 D-2)
- impact: 크론 설정 변경 + git push 동반 테스트 필요 — 롤백 가능 (크론 payload 복원)

### [ops-02] tool-curator 규칙 분산을 canonical 블록 1곳으로 통합
- requested: 2026-07-04 04:00 UTC
- action: openclaw workspace의 SKILL.md/workflow 문서/fixed template 중 1곳 canonical 지정 + 나머지 포인터 교체 diff 생성 및 적용, 링크 검증 조건을 canonical 위치에 통합
- reason: 반복 실행 규칙이 3곳 중복 → 드리프트; 링크 검증 조건이 실행 경로에 따라 누락 (EVALUATION_NOTES.md 미해결 감시 항목 2건)
- impact: 스킬/워크플로우 정본 문서 수정 — 롤백 가능 (git revert)

## 처리 완료

### [marketing-01] Virtue add-flow telemetry 머지/푸시 및 배포 승인
- requested: 2026-05-21 08:07 UTC
- resolved: 2026-05-21 10:17 UTC
- decision: approved
- action: `/home/ubuntu/dev/virtue-rebirth-app`의 로컬 브랜치 `marketing-01-add-flow-telemetry`(`b28d01f`)를 `master`에 fast-forward 머지 후 push하고, Kubernetes `deployment/virtue-rebirth` rollout restart로 프로덕션 반영
- result: GitHub `master`와 배포 pod `/app` HEAD 모두 `b28d01f719db344f4e76c5c7d32934617a2d0f28`; `https://virtue.oracle.shdkej.com` HTTP 200, `641`/`MOCK` 미노출, 빈 상태 카피 렌더 확인
- prepared_report: reports/marketing-01/2026-05-21T0807Z-local-execution.md
- completion_report: reports/marketing-01/2026-05-21T0950Z-approved-deploy.md

### [wiki-04] shdkej/agent-wiki에 자동 사이드바 파일 추가 및 푸시 (JS)
- requested: 2026-04-24 09:00
- resolved: 2026-04-25 (사용자 `/infinity 승인`)
- decision: approved
- note: JS 버전으로 진행. 다음 Heartbeat에서 실행
- draft: artifacts/wiki-04/auto-navigation.md

### [build-01] agent-wiki GitHub Pages 구현 (Jekyll 방식) — 취소
- requested: 2026-04-21 00:00
- resolved: 2026-04-21 00:30
- decision: cancelled
- note: build-01 완료 시 wiki-02/03에서 이미 Docsify로 GitHub Pages 구현 완료 확인. Jekyll 전환 불필요. Intent completed 처리.

### [wiki-03] 로컬 환경에서 agent-wiki push 수행
- requested: 2026-04-20 11:00 (T11:00 에스컬레이션)
- resolved: 2026-04-20 13:30
- decision: approved
- note: 사용자 `/infinity 승인 후 여기서 진행` — 로컬 SSH 인증으로 index.html push 완료 (commit d52641c). Intent completed → archive 이관

### [wiki-02] 재진행 승인 (환경 제약 blocked 해제)
- requested: 2026-04-19 02:40
- resolved: 2026-04-19 02:40
- decision: approved
- note: 사용자 `/infinity 승인` — wiki-02 blocked 해제, in_progress 전환. 다음 Heartbeat에서 실행 재시도

### [doc-01] lessons-learned.md 변경사항 푸시
- requested: 2026-04-08 13:00
- resolved: 2026-04-08 13:05
- decision: approved
- note: 사용자 승인

### [monitor-01] monitoring_personal 변경사항 커밋 & 푸시
- requested: 2026-04-08 11:00
- resolved: 2026-04-08 11:15
- decision: approved
- note: 사용자 승인

### [wiki-02] shdkej/agent-wiki 레포에 Docsify 파일 추가 및 GitHub Pages 활성화
- requested: 2026-04-18 09:00
- resolved: 2026-04-18 13:13
- decision: approved
- note: Telegram에서 사용자 승인

### [wiki-03] shdkej/agent-wiki index.html 교체 및 푸시
- requested: 2026-04-19 04:00
- resolved: 2026-04-19 12:36
- decision: approved
- note: Telegram에서 사용자 승인

### [wiki-03] GPG 서명 없이 agent-wiki 커밋 허용
- requested: 2026-04-19 13:00
- resolved: 2026-04-19 23:29
- decision: approved
- note: Telegram에서 사용자 승인
