# marketing-100 Virtue 홈 J1/J3 2갈래 시작선 검증 질문 1장

- id: marketing-100
- status: archived
- completed_at: 2026-07-03T2229Z
- projects: [virtue, infinity]
- task_type: strategy
- topics: [marketing, activation, onboarding, home]
- result_summary: J1/J3 2갈래 시작선을 실제 UI에 넣기 전 판정에 쓸 한 장을 고정했다. 초안에서는 첫 문장·버튼 문구·핵심 질문·보류 조건·preview안 차이를 정리했고, 후속 보강에서는 단일 CTA 대비 필요성 질문, pass/hold cutline, 채택 신호를 추가했다. 구현·배포·계측 변경은 범위에서 제외했다.
- artifacts:
  - path: artifacts/marketing-100/j1-j3-path-validation-sheet.md
    role: research
    note: 초안 기준의 J1/J3 2갈래 시작선 검증 질문 한 장
  - path: artifacts/marketing-100/j1-j3-start-path-validation-sheet.md
    role: strategy
    note: 보강본. 단일 CTA 대비 필요성 질문과 pass/hold 기준, 채택 신호까지 포함한 판정 시트
- reports:
  - path: reports/marketing-100/2026-07-03T1400Z.html
    role: final
  - path: reports/marketing-100/2026-07-03T2229Z.html
    role: refinement
- commits: []
- urls: []
- next_actions:
  - 실제 홈 목업 또는 카피 비교 시 이번 질문 세트로 pass/hold를 먼저 판정
  - 구현·배포·계측 변경은 approval-needed 후속 intent로 분리
  - preview안 검증은 `누구를 부르는가`가 아니라 `기대 결과가 먼저 보이는가` 축으로 따로 비교

## Result

- 권장 첫 문장은 `오늘을 남길지, AI 관점으로 먼저 볼지 고르세요.`로 고정했다.
- 버튼 문구는 J1 `오늘 기록하기`, J3 `AI 관점으로 보기`를 baseline으로 남겼다.
- 핵심 판정은 `단일 CTA보다 2갈래가 실제로 더 나은가`, `첫 화면만 보고 자기 길을 말할 수 있는가`, `설명보다 길이 먼저 보이는가`, `판결 위임이 아니라 관점 보기로 읽히는가`에 둔다.
- pass는 핵심 5문항 전부 충족과 보조 3문항 중 최소 2개 충족일 때만 인정한다.
- 최근 관찰에서 J3 홈 혼란 신호가 없거나 J1이 이미 잘 움직이면 이 안은 즉시 구현하지 않고 보류한다.
- J3 사용자가 홈에서 AI 길을 못 찾아 멈추는 관찰이 2회 이상 반복될 때 2갈래 시작선 재검토 우선순위를 높인다.

## Links

- artifact: `artifacts/marketing-100/j1-j3-path-validation-sheet.md`
- artifact: `artifacts/marketing-100/j1-j3-start-path-validation-sheet.md`
- report: `reports/marketing-100/2026-07-03T1400Z.html`
- report: `reports/marketing-100/2026-07-03T2229Z.html`
- prior_context: `intents/archive/marketing-99.md`, `intents/archive/marketing-97.md`, `intents/archive/marketing-93.md`, `source/external-links/marketing/2026-07-03-purpose-path-onboarding.md`
