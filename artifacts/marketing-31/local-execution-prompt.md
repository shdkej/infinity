# marketing-31 로컬 실행 프롬프트

> 이 파일을 로컬 Claude Code(pt/purplemux pane 또는 `claude -p`)에 전달하세요.

---

```
Infinity Intent: marketing-31 Virtue 첫 세션 제품 본체/범퍼 경계표 작성
Mode: execute_local
Invocation: Prefer the existing pt/purplemux Claude pane via `tmux -L purple`; capture first, clear stale input, send this bounded prompt once, then capture the result. Fall back to a fresh bounded Claude Code call only if no usable pt pane exists.
Workflow: simple-doc — direct lightweight execution acceptable.

Goal:
virtue-rebirth-app의 `apps/web/docs/first-session-product-bumper-boundary.md` 파일을
아래 초안 경로 내용 그대로 생성하고, 기존 문서와 충돌 없이 commit & push한다.

Context:
- 레포: /home/ubuntu/dev/virtue-rebirth-app (또는 현재 virtue repo 경로)
- 초안 소스: /home/ubuntu/workspace/infinity/artifacts/marketing-31/first-session-product-bumper-boundary-draft.md
- 선행 참고: apps/web/docs/ 하위 기존 marketing docs

Prepared findings:
- 전체 초안: artifacts/marketing-31/first-session-product-bumper-boundary-draft.md
- 핵심: J1~J4 × S1~S4 × 본체/범퍼 역할 × 정상종료·막힘 판독 기준 표
- J3 핵심 갭: S1에서 AI 신호 부재 = 범퍼 누락이 아닌 본체 연결 실패

Allowed: L0/L1 actions only
Forbidden: 코드 수정, 이벤트/속성/카피 변경, 배포, 외부발송, 비용, 시크릿, 권한 변경

Verification (모두 PASS해야 완료):
1. conflict marker 0 (grep -r '<<<<' apps/web/docs/ = 0건)
2. 코드 diff 0 (git diff --name-only HEAD | grep -v 'apps/web/docs' = 0건)
3. 신규 이벤트/속성/카피/배포 0
4. J3 first value = deed_judged 재정의 없음 (문서에서 확인)
5. git HEAD == origin/master (fast-forward push)

Marketing learning context:
Marketer는 MARKETING_LEARNINGS.md를 먼저 읽고, 선행 docs와 J3 저장 없는 first value 원칙을 계승할 것.
계승한 기준, 이번에 새로 배운 것, 다음 Marketer에게 넘길 규칙을 report details에 포함할 것.

Report back to:
reports/marketing-31/{YYYYMMDDTHHMMZ}-local.html
(HTML report, 결론 2축: 🔴 무엇이 문제였나 / ✅ 어떻게 해결하나, ARTIFACT_RULES.md 참조)

HTML report contract:
- reports/_TEMPLATE.html 기반, 개선형 clay color (--a1:#a9745a; --a1-deep:#8a5c45;)
- axis ax1: 무엇이 문제였나
- axis ax2: 어떻게 해결하나
- details에: 계승한 기준, 이번에 새로 배운 것, 다음 Marketer 규칙
- 완료 전 검증: <html, <body, axis ax1, axis ax2, <details 존재 확인
- 완료 후 Infinity repo reports/marketing-31/ 에도 반영 필요 (별도 commit)
```
