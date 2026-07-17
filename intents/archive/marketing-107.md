# [marketing-107] 첫 10명 관찰표에 작은 관객 적합도 칸 추가

- id: marketing-107
- status: archived
- completed_at: 2026-07-17T22:14
- projects: [virtue]
- task_type: implementation
- topics: [marketing, activation, retention]
- result_summary: 첫 10명 관찰표 companion에 `smallest_audience_fit`, fit 근거 원문, 다시 돌아올 상황, fit confidence 칸을 추가해 J1-J4 관객 가설을 activation/retention 판정 전에 분리하도록 했다.
- artifacts:
  - path: artifacts/marketing-107/smallest-audience-fit-addendum.md
    role: implementation
    note: 기존 관찰표와 marketing-104 companion에 붙이는 작은 관객 적합도 보강안
- reports:
  - path: reports/marketing-107/20260717T2214Z.html
    role: final
- commits:
  - repo: infinity
    sha: 700c2cb
    note: completion artifact/report/archive commit
- urls: []
- next_actions:
  - 실제 첫 사용자 세션에서 같은 `다시 돌아올 상황`이 반복될 때만 후속 관찰 질문 또는 UX intent로 분리한다.

## Completion Notes

- Success criteria: PASS. 관찰표만 보고 각 첫 사용자 세션이 J1/J2/J3/J4/혼합/불명 중 어디에 가까운지와 같은 job으로 재방문할 상황을 별도 칸에 기록할 수 있다.
- First verification gate: PASS. 새 칸은 `첫 주 재방문 이유`나 `retention 예측 신호`가 아니라 선행 관객 가설 분류로 정의했다.
- Boundaries: 신규 이벤트, 속성, 대시보드, 공개 카피, 발송, 배포는 하지 않았다.
