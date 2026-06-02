# marketing-34 — Virtue PLG Foundation exit gate 문서

- id: marketing-34
- status: active
- priority: medium
- permission: L1/L2 internal-doc only
- mode: prepare (cloud done) → execute_local
- goal: `apps/web/docs/plg-foundation-exit-gate.md` 한 장 추가 — Foundation→Activation 전환 기준을 잠그는 exit gate 체크리스트
- success_criteria:
  - apps/web/docs/에 Foundation exit gate 문서 생성
  - 기존 first value/activation candidate/baseline/TTV/D7 문서만 인용
  - 신규 이벤트·속성·카피·계측·대시보드 0
  - 외부 벤치마크 수치를 Virtue 합격선으로 쓰지 않음
  - conflict marker 0, git diff doc/report 범위에만
- context: virtue-rebirth-app `apps/web/docs/`
- draft: artifacts/marketing-34/plg-foundation-exit-gate-draft.md
- prepare_report: reports/marketing-34/2026-06-02T0000Z-prepare.html
- next: 로컬 Claude Code가 초안 기반으로 docs 파일 생성 → 검증 게이트(conflict marker 0 / 코드 diff 0 / 이벤트 anchor 현행 일치) PASS → 커밋·push → Heartbeat HTML report 작성 후 archive
