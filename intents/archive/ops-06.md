# ops-06 weekly_review same-week block replacement gate

- id: ops-06
- status: archived
- completed_at: 2026-07-07T00:07
- projects: [openclaw, infinity]
- task_type: maintenance
- topics: [automation, workflow, review]
- result_summary: `weekly_review.md` 생성 흐름이 같은 주 canonical 블록을 새로 붙이지 않고 replace/dedupe해야 한다는 계약과 검증 helper를 추가했고, 2026-W27 dry-run에서 canonical count 1을 확인했다.
- artifacts:
  - path: artifacts/ops-06/weekly-review-replacement-contract.md
    role: implementation
    note: canonical heading 기준, manual-note 보존 규칙, replace/dedupe gate 계약
  - path: scripts/weekly_review_block_gate.py
    role: implementation
    note: 기존 weekly_review.md와 생성 블록을 입력받아 같은 주 canonical 블록이 1개인지 검증하는 helper
- reports:
  - path: reports/ops-06/2026-07-07T0007Z.html
    role: final
- commits:
  - repo: infinity
    sha: pending
    note: commit after report gate
- urls: []
- next_actions:
  - OpenClaw weekly review 생성기 본체가 확인되는 다음 사이클에서 `scripts/weekly_review_block_gate.py`의 동일 계약을 직접 호출하거나 동등 로직으로 이식한다.

## Notes

- 축1: `system/data/weekly_review.md`에 같은 ISO week의 canonical 회고 블록이 반복 append되는 문제.
- 축2: `YYYY-Www`를 키로 canonical heading만 replace/dedupe하고, 수동 메모는 보존하는 gate를 문서화 및 helper로 고정.
