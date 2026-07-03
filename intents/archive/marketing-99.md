# marketing-99 Virtue 홈 첫 진입 `목적별 첫 길` 비교안 작성

- id: marketing-99
- status: archived
- completed_at: 2026-07-03T0000Z
- projects: [virtue, infinity]
- task_type: strategy
- topics: [marketing, activation, onboarding]
- result_summary: 홈 첫 방문자 단일 CTA 현황 기준으로 3안(A 현상유지·B J1/J3 2갈래·C 샘플preview)의 장단점·금지선·우선 실험 순서를 한 문서로 정리했다.
- artifacts:
  - path: artifacts/marketing-99/purpose-path-onboarding-compare.md
    role: design
    note: 3안 비교표, 우선 실험 순서, 금지선, 다음 마케터 인수인계
- reports:
  - path: reports/marketing-99/2026-07-03T0000Z.html
    role: final
- commits: []
- urls: []
- next_actions:
  - 첫 10명 관찰표(marketing-98 양식) 작성 후 J3 Gap G3 또는 J1 빈 화면 부담이 관찰되는지 확인
  - 관찰 결과에 따라 Option C(샘플 preview) 구현 여부 결정 — 구현 시 별도 L1 intent로 분리
  - Option B(2갈래 시작선)는 관찰 증거 확인 후에만 실험 고려

## Result

- `apps/web/src/app/page.tsx:106-112` (단일 CTA) · `:125-131` (빈 상태)를 기준 앵커로, 3안 비교표를 docs-only로 완성했다.
- **1순위**: Option C (샘플 결과 preview) — 낮은 실험 비용, 양쪽 잡 동시 신호. 금지: 실 데이터, mock 레이블.
- **2순위**: Option B (J1/J3 2갈래 시작선) — J3 Gap G3 직접 해소 효과 크지만 관찰 선행 필수.
- **유지 조건 (A)**: J3 Gap G3 + J1 빈 화면 부담 둘 다 관찰에서 주요 마찰로 안 나오면 현 상태 유지.
- marketing-93 · marketing-19 · marketing-98 · MARKETING_LEARNINGS.md 계승 충돌 0.

## Links

- artifact: `artifacts/marketing-99/purpose-path-onboarding-compare.md`
- report: `reports/marketing-99/2026-07-03T0000Z.html`
- prior_context: marketing-19 (홈 FAE 감사), marketing-70 (empty-state proof), marketing-93 (J1 language-market fit), marketing-98 (관찰표)
