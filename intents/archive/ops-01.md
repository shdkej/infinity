# ops-01 weekly-main-workspace-autopush git sync를 결정적 스크립트로 이관

- id: ops-01
- status: completed
- completed_at: 2026-07-04T1650Z
- projects: [openclaw, infinity]
- task_type: implementation
- topics: [automation, cron, reliability]
- proposed_by: sam-proposer
- source_signal: openclaw cron 실행 이력 — self-healer가 동일 git diff exit-code 실패에 프롬프트 패치 5겹 누적 (CRON_REDESIGN_2026-07-04.md 진단 5 / D-2)
- result_summary: openclaw workspace에 `system/scripts/weekly_workspace_sync.sh`를 만들어 안전 staging → commit → rebase pull → non-force push를 결정적으로 수행하게 하고, weekly-main-workspace-autopush 크론 payload를 agentTurn 프롬프트에서 command 실행으로 교체했다. 스크립트 직접 실행(19파일 커밋 453f22d, push 성공)과 크론 하네스 수동 run(ok, 2.3초)을 모두 검증했다. 프롬프트가 사라져 self-healer의 패치 누적 표면 자체가 제거됐다.
- artifacts:
  - path: openclaw workspace system/scripts/weekly_workspace_sync.sh
    role: implementation
    note: 결정적 git sync 스크립트 (크론이 직접 실행)
- reports:
  - path: reports/ops-01/2026-07-04T1650Z.html
    role: final
- commits: [openclaw 453f22d]
- next_actions:
  - 다음 일요일 03:30 UTC 정기 run의 ok 종료 확인 (failureAlert after:1이 감시, 실패 시 payload 복원 롤백)

## Result

- 크론 payload: agentTurn 장문 프롬프트 → `bash system/scripts/weekly_workspace_sync.sh` command 실행, timeout 240s, delivery/failureAlert 유지.
- 기존 프롬프트의 안전 규칙(ignored pathspec 제외, diff exit 1 = 변경 있음, no force-push, rebase 충돌 시 중단)은 스크립트 로직으로 이전.
