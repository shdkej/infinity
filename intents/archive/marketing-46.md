# marketing-46 Virtue agent-led growth fit/no-fit 경계표

- id: marketing-46
- status: archived
- completed_at: 2026-06-08T10:07Z
- projects: [virtue]
- task_type: strategy
- topics: [prelaunch, agent-led-growth, distribution]
- result_summary: "AI 제품이면 agent-first 유통부터"라는 범주 오류를 막기 위해, 가치 완료 주체(task completion subject)를 기준으로 8개 판단 차원 fit/no-fit 경계표를 고정. Virtue는 사람 경험·선택이 본체라 do-for-you(MCP/API/agent onboarding)는 no-fit, read-about(설명)만 후보. launch/post-launch gate G1~G4 사전 정의. docs-only, 외부 행동·코드 변경 0.
- artifacts:
  - path: apps/web/docs/agent-led-growth-fit-no-fit-boundary-table.md
    repo: virtue-rebirth-app
    role: strategy
    note: Virtue 앱 레포 직접 생성 (Virtue 제품 내부 문서). 신규 1파일, docs-only.
- reports:
  - path: reports/marketing-46/2026-06-08T1007Z-local.html
    role: final
- commits:
  - repo: virtue-rebirth-app
    sha: (local agent 2026-06-08T10:07Z)
    note: docs-only artifact 생성 + MARKETING_LEARNINGS.md learning 승격
  - repo: infinity
    note: archive 생성 + inbox file cleanup (heartbeat 2026-06-09)
- urls: []
- next_actions:
  - agent-led growth / AI 유통 논의가 오면 "가치를 누가 완료하나"를 먼저 묻는다.
  - read-about 공개 표면(llms.txt 등)은 G1 실사용 신호 충족 후 별도 approval gate.
  - do-for-you(MCP/API/agent onboarding)는 G4 실사용 신호 충족 + approval 없이 열지 않는다.

## Result

Virtue prelaunch에서 agent-led growth의 fit/no-fit 경계를 **"가치를 누가 완료하나(task completion subject)"** 기준으로 8개 차원에서 가렸다. Virtue는 사람의 경험·선택이 본체이므로 do-for-you(MCP/API/agent onboarding) 유통은 제품 의미를 소거(성찰을 대행하면 성찰이 사라진다)하여 **no-fit**. agent-readable은 **read-about(설명)까지만** 후보, 재검토는 실사용 신호 기반 G1~G4 gate로만 연다.

## Verification

- HTML report: `reports/marketing-46/2026-06-08T1007Z-local.html` — `<html`, `<body`, `axis ax1`, `axis ax2`, `<details` 포함, 계승 기준·새 배운 것·다음 Marketer 규칙·승격 후보 포함 (PASS).
- docs-only: apps/web/docs 1파일(virtue-rebirth-app) + infinity report 1파일. code diff 0, event anchor drift 0, conflict marker 0.
- first value 매핑 재정의 0.
- robots/sitemap/llms.txt·API/MCP·공개 카피·tracking/privacy·배포·외부발송·비용·권한 변경: 0.

## Learning

`MARKETING_LEARNINGS.md`에 durable learning candidate `Agent-Led Growth Fits Task-Completion Products, Not Experience Products`를 승격했다.
