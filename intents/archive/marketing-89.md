# marketing-89 Virtue 홈 반환 상태 source-of-truth 정렬 점검

- id: marketing-89
- status: archived
- completed_at: 2026-06-27T2236Z
- projects: [virtue, infinity]
- task_type: strategy
- topics: [marketing, activation, product]
- result_summary: `stats.total`, `stats.count`, `recent.length`의 역할과 Virtue 홈 반환 상태 empty-state 허용/금지 조건을 1페이지 계약으로 고정했다. 핵심 결론은 `stats.total`은 baseline 포함 누적치이므로 first-visit 판정 근거가 아니며, 반환 상태는 `stats.count > 0`일 때 first-visit 카피를 절대 노출하면 안 된다는 점이다.
- artifacts:
  - path: artifacts/marketing-89/return-state-source-of-truth.md
    role: strategy
    note: 홈 hero, CTA, 최근 덕행의 반환 상태 게이트와 금지 조합을 고정한 1페이지 계약
- reports:
  - path: reports/marketing-89/2026-06-27T2236Z.html
    role: final
- commits: []
- urls:
  - url: https://virtue.oracle.shdkej.com
    note: marketing-88에서 drift가 관측된 라이브 홈
- next_actions:
  - 후속 implementation/verification intent는 홈에서 `stats.count`를 canonical visit-state gate로 고정하고, `recent.length === 0` 예외를 섹션 단위 복구 상태로만 처리해야 한다.
  - retained proof 세션 검증은 `stats.count > 0`일 때 first-visit 카피가 하나라도 남아 있으면 실패로 판정해야 한다.
