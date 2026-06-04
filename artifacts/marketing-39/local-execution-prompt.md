# Local Execution Prompt — marketing-39

## Infinity Intent
marketing-39: Virtue Human-AI readiness trace map 작성

## Mode
execute_local

## Invocation
Prefer the existing pt/purplemux Claude pane via `tmux -L purple`; capture first, clear stale input, send this bounded prompt once, then capture the result. Fall back to a fresh bounded Claude Code call only if no usable pt pane exists.

## Workflow
simple-doc: direct lightweight execution acceptable (단일 내부 문서 1파일 작성).

## Goal
`infinity/artifacts/marketing-39/human-ai-readiness-trace-map.md`의 초안을 읽고,
`virtue-rebirth-app/apps/web/docs/human-ai-readiness-trace-map.md`에 최종 파일로 저장한다.

## Context
- infinity/artifacts/marketing-39/human-ai-readiness-trace-map.md (초안 전체)
- virtue-rebirth-app/apps/web/docs/ 선행 문서:
  - ai-judgment-trust-control-observation-boundary-table.md
  - activation-candidate-registry.md
  - first-real-user-baseline-template.md
- MARKETING_LEARNINGS.md 핵심 기준 계승 확인

## Prepared findings
초안: `infinity/artifacts/marketing-39/human-ai-readiness-trace-map.md`

- first value 매핑 계승: J1/J2/J4 = deed_saved:183, J3 = deed_judged:106 (재정의 0)
- 선행 3문서 충돌 0 확인 필요
- source note (`/home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-04-human-ai-readiness-traces.md`) 로컬 참조 가능 시 §0 rationale 보강 가능

## Marketing learning context
MARKETING_LEARNINGS.md를 먼저 읽고 다음 기준 계승 확인:
1. First Value Mapping
2. No Autonomous Action Bounds The Trust Question
3. Trust Calibration By Job

## Allowed
L1 docs-only: 파일 생성, 커밋, push (virtue-rebirth-app)

## Forbidden
신규 이벤트·속성·PostHog·tracking/privacy·카피·배포·외부 발송·비용·권한·개인정보 변경 ✗

## Verification
1. `test -s virtue-rebirth-app/apps/web/docs/human-ai-readiness-trace-map.md` → 파일 존재
2. 코드 diff 0: `git diff --stat apps/web/src apps/ios/Sources` 빈 출력
3. conflict marker 0: `grep -c "^<<<" apps/web/docs/human-ai-readiness-trace-map.md` → 0
4. 선행 3문서 충돌 0 확인
5. first value 매핑 인용 확인: deed_saved/deed_judged 키워드 존재
6. 신규 이벤트 추가 0 확인

## Report back to
`reports/marketing-39/{timestamp}-local.html` (HTML 필수)
- reports/_TEMPLATE.html 기반, 개선형(clay: `--a1:#a9745a`) 색상
- axis ax1 label: "무엇이 문제였나"
- axis ax2 label: "어떻게 해결하나"
- details에 계승한 기준·이번에 새로 배운 것·다음 Marketer 규칙 포함
- HTML gate 확인: `<html`, `<body`, `axis ax1`, `axis ax2`, `<details`

## 완료 후 처리
1. INTENTS.md Active에서 marketing-39 블록 제거
2. Archive에 추가: `<!-- marketing-39 completed {timestamp} → reports/marketing-39/{timestamp}-local.html [projects: virtue; type: strategy; topics: ai-trust,activation,onboarding,prelaunch] (한 줄 결과) -->`
3. intents/archive/marketing-39.md 작성 (canonical final index)
4. MARKETING_LEARNINGS.md에 durable learning 승격 검토: "Readiness Trace Before Metrics" (실사용 대조 후 결정)
