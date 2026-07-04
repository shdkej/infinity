# [ops-04] OpenClaw evaluator 경고성 탐색 템플릿 축소

- id: ops-04
- status: active
- priority: medium
- mode: prepare (완료) → execute_local (대기 중)
- started: 2026-07-04T0700Z
- prepare_report: reports/ops-04/2026-07-04T0700Z.html

## 현재 상태

prepare 단계 완료. execute_local 프롬프트 준비됨. 로컬 Claude 실행 대기 중.

## execute_local 프롬프트

```
Infinity Intent: ops-04 OpenClaw evaluator 경고성 탐색 템플릿 축소
Mode: execute_local
Goal:
  OpenClaw evaluator cron payload 또는 evaluator 정본 절차에서
  기본 탐색을 git status --short + 필요한 절대경로 파일 읽기로 제한한다.
  제거 대상:
    - ~ 경로 search (절대경로로 대체)
    - agent-scoped git ls-files (git status --short로 대체)
    - agent-scoped 전역 search (특정 절대경로 읽기로 대체)
    - 2>/dev/null literal target (no-match를 data로 처리)
  no-match/optional search는 실패가 아닌 데이터로 처리하도록 변경.
  미해결 신호가 없을 때는 짧게 NO_REPLY로 종료.
Context:
  - OpenClaw evaluator cron payload (~/.openclaw/workspace 또는 ~/.claude/ 확인)
  - evaluator SKILL.md 또는 evaluator 정본 절차 파일
  - EVALUATION_NOTES.md (OpenClaw workspace)
Prepared findings:
  - 경고 패턴 4종 식별: ~ 경로 search, agent-scoped git ls-files,
    agent-scoped 전역 search, 2>/dev/null literal target
  - 모두 절대경로 파일 읽기로 대체 가능
  - NO_REPLY 루프 비용 및 diagnostics 소음이 반복 누적됨
Allowed: L0/L1 (로컬 파일 수정, git commit)
Forbidden: L2/L3 actions without explicit approval
Verification: evaluator 수동 실행 또는 다음 정기 실행 diagnostics에 search warning 없어야 함
Report back to: reports/ops-04/{timestamp}-local.html
```

## 다음 액션

1. 로컬 Claude가 evaluator cron payload 및 정본 절차 파일 위치 파악
2. 경고성 탐색 패턴 4종 절대경로/no-match 처리로 교체
3. evaluator 수동 실행으로 warning 소멸 확인
4. 성공 시 ops-04 archive 처리
