# marketing-92 Virtue 홈 반환 상태 gating 구현/검증

- id: marketing-92
- status: active
- created_at: 2026-06-29T10:00Z
- activated_at: 2026-06-29T11:15Z
- projects: [virtue, infinity]
- task_type: implementation-verification
- topics: [marketing, activation, return-state, gating]
- permission_level: L2 implementation-verification
- source_note: /home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-29-return-state-gating-over-copy.md
- current_mode: local-handoff-prepared

## Why This Is Active

최근 Virtue 관련 학습은 copy polish보다 gate 3 반환 상태 정합성이 더 우선이라는 점으로 수렴했다. 따라서 `retained proof`와 `first-visit empty-state` 동시 노출 금지 조건을 실제 코드/라이브 검증 조각으로 넘기는 일이 지금의 가장 작은 유효 작업이다.

## Current Cycle Result

- source note와 `marketing-89` source-of-truth를 다시 묶어 gating 계약은 이미 충분히 좁혀졌음을 확인했다.
- 다만 현재 로컬 `space/apps/virtue-rebirth` 경로에는 앱 소스 트리 대신 `README.md`, `deployment.yaml`, `ingress.yaml`, `service.yaml`만 존재해 즉시 코드 구현/검증은 진행할 수 없었다.
- 따라서 이번 사이클은 `reports/marketing-92/2026-06-29T1115Z-handoff.html`에 exact next scope, 확인 경로, 금지 조건, Claude Code 프롬프트 범위를 남기는 것으로 닫는다.

## Canonical Gate

- first-visit 판정 기준은 `stats.count === 0`
- recent empty-state는 `recent.length === 0`일 때만 섹션 단위로 다룬다
- `stats.count > 0` 또는 retained proof surface가 보이는 세션에서는 first-visit 카피가 금지된다

## Next Action

1. 실제 Virtue 앱 소스 저장소 또는 checkout 경로를 확인한다.
2. 홈 source file에서 `stats.count`, `recent.length`, retained proof surface 분기 지점을 캡처한다.
3. Claude Code로 gating 구현/검증을 한 번에 요청하되, copy polish와 리디자인은 범위에서 제외한다.
