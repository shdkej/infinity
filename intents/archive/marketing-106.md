# marketing-106 첫 10명 retention 예측 신호 칸 보강

- id: marketing-106
- status: archived
- completed_at: 2026-07-17T10:07Z
- projects: [virtue, infinity]
- task_type: strategy
- topics: [marketing, activation, retention]
- permission_level: L1 docs-only
- result_summary: 첫 10명 관찰 companion에 `저장 여부`, `같은 job 재방문 근거`, `retention 예측 신호`, `첫 verification gate` 칸과 J1-J4 예시를 추가해 activation 후보와 retention 전조를 분리했다.
- artifacts:
  - path: artifacts/marketing-106/retention-prediction-signal-companion.md
    role: design
    note: marketing-79/104/105 관찰표와 병행하는 retention 예측 신호 companion
- reports:
  - path: reports/marketing-106/20260717T1007Z.html
    role: final
- commits:
  - repo: infinity
    sha: 202b923
    note: marketing-106 companion artifact, HTML report, and INTENTS archive update
- urls: []
- next_actions:
  - 첫 10명 기록에서 `저장 여부=예`지만 `같은 job 재방문 근거=없음/불명`이 반복되면 저장 후 누적 의미 또는 다음 행동 명료성 문제를 별도 UX intent로 분리

## Success Criteria

- [x] J1-J4별 retention 예측 신호 칸 추가
- [x] 예시 문장 추가
- [x] 첫 verification gate 추가
- [x] `저장 여부`와 `같은 job으로 재방문할 근거` 분리
- [x] HTML report gate 통과

## Safety

- production code changes: 0
- deploys: 0
- tracking/privacy changes: 0
- public copy changes: 0
- external messages: 0
- cost: 0
