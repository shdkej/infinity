# marketing-92 Virtue 홈 반환 상태 gating 구현/검증 intent 초안 작성

- id: marketing-92
- status: inbox
- created_at: 2026-06-29T10:00Z
- projects: [virtue, infinity]
- task_type: implementation-verification
- topics: [marketing, activation, return-state, gating]
- permission_level: L2 implementation-verification
- source_note: /home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-29-return-state-gating-over-copy.md

## Why This Now

최근 마케팅 학습은 첫 세션의 가장 약한 구간이 gate 3 반환 일관성이라는 점으로 수렴했다. 현재 필요한 다음 조치는 새 카피를 더 쌓는 일이 아니라, 홈 반환 상태에서 retained proof와 first-visit empty-state가 동시에 노출되지 않도록 state gating을 작게 정의하고 검증하는 것이다.

## Task

Virtue 홈 반환 상태의 gating 구현/검증 intent 초안을 만든다.

- 범위는 홈 반환 표면 한 조각으로 제한한다.
- `stats.total`, `stats.count`, `recent.length` 조합에 따라 어떤 카드/문구/섹션이 보여야 하는지 조건표를 만든다.
- retained proof가 보이는 세션에서 first-visit empty-state 문구가 함께 남지 않도록 한다.
- copy polish는 본 intent의 주제가 아니다. gating 기준과 구현/검증 경계를 먼저 고정한다.

## Rationale

- source note path: `/home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-29-return-state-gating-over-copy.md`
- expected impact: 반환 상태 문제를 카피 실험이 아닌 상태 계약 검증으로 축소해, 더 작은 구현/검증 조각으로 라우팅할 수 있다.
- owner route: Infinity Inbox -> Claude Code

## Success Criteria

- 홈 반환 상태에서 retained proof와 empty-state 동시 노출 금지 조건이 문서 또는 코드 근거와 함께 정리된다.
- 라이브 홈과 로컬 홈 기준으로 현재 깨진 gating 여부를 재현 가능한 문장으로 설명할 수 있다.
- 후속 카피 실험이 필요하더라도, gating 통과 이후 별도 intent로 분리된다.

## First Verification Gate

라이브 홈과 로컬 홈 코드를 나란히 보고, 어떤 데이터 조합에서 어떤 블록이 보이면 안 되는지 5줄 이내로 설명할 수 있으면 통과다.
