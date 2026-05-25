# [marketing-17] Virtue 첫 세션 정성 마찰 관찰 프로토콜

- id: marketing-17
- status: in_progress
- priority: high
- permission: L1 문서 작성 + L2 agent-approved push
- created_at: 2026-05-25T12:00Z
- mode: cloud prepare 완료 → execute_local 대기
- artifact: artifacts/marketing-17/first-session-qualitative-friction-protocol.md
- next_action: 로컬 Claude Code로 artifact 초안을 virtue-rebirth-app/apps/web/docs/first-session-qualitative-friction-protocol.md에 추가·커밋·push

## 로컬 Claude Code 실행 프롬프트

```
Infinity Intent: marketing-17 Virtue 첫 세션 정성 마찰 관찰 프로토콜
Mode: execute_local
Required workflow: Use workflow-master first. Read and follow `.agent/workflows/workflow-master.md` or `WORKFLOW-MASTER.md` when present before doing implementation work. Do not proceed as a single direct executor unless workflow-master explicitly classifies the task as trivial and records that decision.
Goal: infinity repo의 artifacts/marketing-17/first-session-qualitative-friction-protocol.md 초안을 virtue-rebirth-app/apps/web/docs/first-session-qualitative-friction-protocol.md 로 추가. 신규 이벤트·속성·코드·카피·대시보드·배포 변경 금지 — 문서 추가만 허용.
Context: /home/ubuntu/dev/virtue-rebirth-app, apps/web/docs/, source_note: /home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-25-first-session-friction-evidence.md
Prepared findings: infinity repo artifacts/marketing-17/first-session-qualitative-friction-protocol.md (J1-J4 정성 마찰 태그 9종, 3분류 기준, 첫 3/10명 검증 게이트 초안). source_note 파일 내용으로 보완 후 최종 작성.
Allowed: L0/L1 — docs 파일 추가, 커밋, push
Forbidden: 신규 이벤트·속성·코드·카피·대시보드·외부발송·비용·시크릿·권한 변경 절대 금지
Verification: ①충돌 마커 없음 ②신규 이벤트/속성/코드 변경 없음 ③git clean 확인 ④기존 선행 문서(first-session-jtbd-matrix.md, three-screen-value-path-audit.md, ios-activation-event-parity-brief.md)와 충돌 없음
Report back to: infinity reports/marketing-17/{timestamp}Z-local.md 에 완료 기록 후 Heartbeat가 archive 처리
```

## 컨텍스트

- source_note: `/home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-25-first-session-friction-evidence.md`
- 초안: `artifacts/marketing-17/first-session-qualitative-friction-protocol.md`
- 선행 문서 (충돌 확인 필요):
  - `apps/web/docs/first-session-jtbd-matrix.md`
  - `apps/web/docs/three-screen-value-path-audit.md`
  - `apps/web/docs/ios-activation-event-parity-brief.md`
  - `apps/web/docs/activation-path-friction-audit.md`
  - `apps/web/docs/first-real-user-baseline-template.md`
  - `apps/web/docs/first-week-activation-retention-bridge.md`

## Success Criteria

- J1-J4별 첫 가치 경로에 적용할 수 있는 정성 마찰 태그 정의
- value-critical / value-adjacent / non-critical at activation 분류
- 첫 3명 / 첫 10명 검증 게이트
- 선행 문서와 충돌 없음 (기존 이벤트만 인용)
- 신규 이벤트·속성·코드·배포 변경 0
