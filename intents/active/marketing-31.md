# marketing-31: Virtue 첫 세션 제품 본체/범퍼 경계표 작성

- id: marketing-31
- status: in_progress
- updated: 2026-05-31T08:30Z
- next_action: Local Claude Code에 위임 → virtue-rebirth-app/apps/web/docs/first-session-product-body-bumper-map.md 작성·커밋·push

## 로컬 실행 프롬프트

```
Infinity Intent: marketing-31 Virtue 첫 세션 제품 본체/범퍼 경계표 작성
Mode: execute_local
Invocation: Prefer the existing pt/purplemux Claude pane via `tmux -L purple`; capture first, clear stale input, send this bounded prompt once, then capture the result. Fall back to a fresh bounded Claude Code call only if no usable pt pane exists.
Workflow: simple-doc — 단일 마케팅 문서 작성, workflow-master 불필요, direct execution 가능.
Goal: virtue-rebirth-app/apps/web/docs/first-session-product-body-bumper-map.md 작성 후 커밋·push (L2 agent-approved 조건 확인 후)
Context:
  - Infinity draft: artifacts/marketing-31/first-session-product-body-bumper-map-draft.md
  - 원본 소스: /home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-05-31-product-led-onboarding-bumpers.md
  - 선행 문서 (apps/web/docs/):
    - m06: first-session-jtbd-matrix.md
    - m16: three-screen-value-path-audit.md
    - m17: first-session-friction-observation-protocol.md
    - m19: home-screen-fae-audit.md
    - m21: add-input-output-balance-audit.md
Prepared findings: Cloud prepare 완료. 핵심 구조:
  §1 PLG 본체/범퍼 개념 (제품이 투어 없이 첫 가치로 이끄는 부분=본체, 이탈 지점 보조=범퍼)
  §2 Virtue 첫 세션 5개 표면: S1(/홈)·S2(/add 입력)·S3(결과카드)·S4(저장)·S5(홈복귀)
  §3 심장 표: J1~J4 × S1~S5 × 본체역할/범퍼역할/정상종료/막힘판독
  §4 본체 강화 vs 범퍼 배치 판단 기준 (관찰 신호 → 판독 → 조치 방향)
  §5 prelaunch 금지선
  §6 기존 문서 연결 (충돌 0)
Marketing learning context:
  - MARKETING_LEARNINGS.md 먼저 읽고 시작
  - 계승 기준: First Value Mapping / Prelaunch Decision Boundary / Availability And Friction Are Not Value
  - J3 deed_judged 후 저장 없음 = 정상 종료 (이탈 아님) 계승
  - deed_save_capped를 범퍼 배치 근거로 읽지 않음 (availability/friction)
  - report details에: 계승한 기준, 이번에 새로 배운 것, 다음 Marketer 규칙, durable learning candidate
Allowed: L0/L1 actions only
Forbidden: 코드 수정, 신규 이벤트/속성, 카피 반영, 계측 변경, 배포, 외부 발송, 비용, 시크릿, 권한 변경
Verification:
  - conflict marker 0
  - git diff --stat → doc 1파일만
  - 기존 6 이벤트(add_flow_started/deed_judged/deed_saved/level_up_viewed/deed_rerolled/deed_save_capped)만 인용
  - first value 매핑 계승 (J1/J2/J4=deed_saved, J3=deed_judged 재정의 없음)
  - 선행 6문서 충돌 0
  - HEAD==origin/master
Report back to: reports/marketing-31/{timestamp}.html
  (HTML 필수: <html><body>axis ax1>axis ax2><details 포함)
  (details 안에: 계승한 기준, 이번에 새로 배운 것, 다음 Marketer 규칙, durable learning candidate)
```
