# Approval Gates

> L2 권한이 필요한 액션의 승인 대기 큐.
> Heartbeat Agent가 추가하고, 사용자가 Telegram으로 응답한다.

## 대기 중

## 처리 완료

### [ops-14] OpenClaw evaluator 읽기 예산 게이트 고정 — 로컬 실행
- requested: 2026-07-14T00:00Z
- resolved: 2026-07-14T00:00Z
- decision: agent-approved L2
- note: L2 자체 승인 조건 전부 충족. 읽기 예산 제한(EVALUATION_NOTES.md tail 120줄, OPERATING_LESSONS.md 관련 섹션, 최근 24시간 크론 요약)과 조기 종료 조건 추가는 가역적 프롬프트 수정이며 비용 증가 없음. 로컬 실행 프롬프트: artifacts/ops-14/local-execution-prompt.md.

### [ops-13] 마케팅 inbox 한국어 렌더 게이트 고정 — 로컬 실행
- requested: 2026-07-13T07:00Z
- resolved: 2026-07-13T07:00Z
- decision: agent-approved L2
- note: L2 자체 승인 조건 전부 충족. 로컬 실행 프롬프트: artifacts/ops-13/local-execution-prompt.md. 로컬 Claude Code가 마케팅 크론 저장 경로에 signal/diagnosis/action_candidate/measurement 영어 서술형 감지 게이트 추가 후 dry-run 검증 필요.

### [ops-12] 마케팅 크론 git 동기화 실패 gate 적용 — 로컬 실행
- requested: 2026-07-12T10:07Z
- resolved: 2026-07-12T10:07Z
- decision: agent-approved L2
- note: L2 자체 승인 조건 전부 충족. 로컬 실행 프롬프트: artifacts/ops-12/local-execution-prompt.md. 로컬 Claude Code가 Marketing-agent-growth-review 크론 프롬프트에 git failure gate 계약 추가 후 dry-run 검증 필요.

### [ops-09] 데일리 리뷰 Calendar Result 렌더 게이트 보강 구현 승인
- requested: 2026-07-09T07:00Z
- resolved: 2026-07-10T00:13Z
- decision: agent-approved L2
- note: L2 자체 승인 조건 전부 충족. 로컬 실행 프롬프트: artifacts/ops-09/local-execution-prompt.md. 로컬 Claude Code가 LOCAL_REVIEW_AUTOMATION.md 및 캘린더 스크립트에 적용 후 dry-run 검증 필요.

### [ops-08] 자동 리뷰 산출물 추적 경계 고정 구현 승인
- requested: 2026-07-07T07:00Z
- action: openclaw workspace에서 daily-reviews/ 및 monthly-review-sources/ 경로의 자동 생성 중간 산출물을 .gitignore에 추가하거나 ignored run/cache 경로로 분리하는 규칙 적용
- reason: 자동 생성 산출물이 여러 날짜에 걸쳐 untracked 누적, 정본 문서 수정과 중간 생성물이 같은 검토 층위에 섯임
- impact: openclaw workspace의 .gitignore 또는 review 스크립트 변경 — 롤백 가능 (git revert)
- resolved: 2026-07-09T03:58Z
- decision: completed (agent-approved L2 — infinity 리포 내 .gitignore 경계 패턴 추가. HTML report gate passed.)

### [ops-07] MEMORY/DREAMS 런타임 변경 경계 고정 구현 승인
- requested: 2026-07-07T07:00Z
- action: openclaw workspace에서 MEMORY.md/DREAMS.md 관련 런타임 중간 파일을 git status･evaluator 신호에서 분리하는 .gitignore 패턴 추가 또는 memory/dreams 처리 스크립트 보강
- reason: dreaming 단계 파일과 원장이 함께 dirty로 남아 정본 변경과 런타임 기록의 경계가 흐려짐
- impact: openclaw workspace의 .gitignore 또는 memory/dreams 스크립트 변경 — 롤백 가능 (git revert)
- resolved: 2026-07-09T03:29Z
- decision: completed (agent-approved L2 — infinity 리포 내 .gitignore 경계 패턴 추가. HTML report gate passed.)

### [ops-06] weekly_review same-week block replacement gate
- requested: 2026-07-07 00:07 UTC
- action: `system/data/weekly_review.md` 생성 흐름의 주차 키를 `YYYY-Www`로 고정하고, 같은 주 canonical heading은 append가 아니라 replace/dedupe해야 한다는 계약과 검증 helper를 추가
- reason: 2026-W10/W11/W13/W15 및 최신 2026-W27에서 같은 주 canonical 회고 블록이 중복 누적됨
- impact: 문서/검증 helper 변경 — 실제 OpenClaw 회고 파일이나 프로덕션 코드 변경 없음
- resolved: 2026-07-07
- decision: completed docs-only gate

### [ops-01] weekly-main-workspace-autopush git sync를 결정적 스크립트로 이관
- requested: 2026-07-04 04:00 UTC
- action: openclaw workspace에 `system/scripts/weekly_workspace_sync.sh` 신규 생성 + 해당 크론 command payload를 스크립트 경로로 전환, 첫 실행 push 동반 테스트
- reason: self-healer가 동일 git diff exit-code 실패에 프롬프트 패치 5겨 누적; LLM 판단 불필요한 git sync를 결정적 스크립트로 교체하면 패치 루프 자체가 사라짘
- impact: 크론 설정 변경 + git push 동반 테스트 필요 — 롤백 가능 (크론 payload 복원)
- resolved: 2026-07-04 (사용자 '승인')
- decision: approved

### [ops-02] tool-curator 규칙 분산을 canonical 블록 1곳으로 통합
- requested: 2026-07-04 04:00 UTC
- action: openclaw workspace의 SKILL.md/workflow 문서/fixed template 중 1곳 canonical 지정 + 나머지 포인터 교체 diff 생성 및 적용, 링크 검증 조건을 canonical 위치에 통합
- reason: 반복 실행 규칙이 3곳 중복 → 드리프트; 링크 검증 조건이 실행 경로에 따라 누락
- impact: 스킬/워크플로우 정본 문서 수정 — 롤백 가능 (git revert)
- resolved: 2026-07-04 (사용자 '승인')
- decision: approved

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
- requested: 2026-04-20 11:00 (T11:00 에스컈레이션)
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
