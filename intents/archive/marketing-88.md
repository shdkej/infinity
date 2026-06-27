# marketing-88 Virtue 홈 반환 상태 live/canonical drift audit

- id: marketing-88
- status: archived
- completed_at: 2026-06-27T1007Z
- projects: [virtue, infinity]
- task_type: strategy
- topics: [marketing, activation, product]
- permission_level: L1 docs-only
- result_summary: 라이브 홈, 로컬 홈 코드, 최근 canonical 제안서를 대조해 반환 세션 state drift를 한 장으로 정리했다. 핵심 결론은 라이브가 `612덕` retained proof와 `아직 기록이 없어요` 계열 empty-state를 함께 보여 주는 점이며, 다음 조치는 copy 추가가 아니라 home return-state gating 구현/검증 1조각이다.
- artifacts:
  - path: artifacts/marketing-88/live-canonical-drift-audit.md
    role: strategy
    note: home hero, 누적 카드, 최근 덕행, CTA의 live/local/canonical 차이와 권장 source-of-truth 표
- reports:
  - path: reports/marketing-88/2026-06-27T1007Z.html
    role: final
- commits: []
- urls:
  - url: https://virtue.oracle.shdkej.com
    note: 2026-06-27 observed live home
- next_actions:
  - follow-up implementation intent should inspect the saved-history source behind `stats.total`, `stats.count`, and `recent.length`, then align return-state gating across home surfaces.
  - verification should fail if any retained-score home session still renders `아직 기록이 없어요`-equivalent copy without proving total saved history is zero.
