# marketing-38 Virtue AI 판정 신뢰/제어권 관찰 경계표 작성

- id: marketing-38
- status: archived
- completed_at: 2026-06-04T10:07
- projects: [virtue]
- task_type: strategy
- topics: [ai-agents, activation, marketing]
- result_summary: EY·McKinsey 2026 AI-trust 렌즈를 J1~J4 첫 세션 관찰 신호로 번역한 신뢰/제어권 경계표를 작성했다. 핵심은 Virtue의 AI가 자율 외부 행동을 하지 않아 신뢰 문제가 "틀린 말" 영역으로 좁고 위험은 자기인식 오보정이라는 경계를 고정한 것이다.
- artifacts:
  - path: /home/ubuntu/dev/virtue-rebirth-app/apps/web/docs/ai-judgment-trust-control-observation-boundary-table.md
    role: strategy
    note: J1~J4 × 낮은 위험 경험 × 근거 가시성 × 사용자 선택권/제어권 × 과신/불신 신호 경계표. 기존 이벤트만 인용, m06/m20/m24/m31/m33 계승.
- reports:
  - path: reports/marketing-38/2026-06-04T1007Z-local.html
    role: final
- commits:
  - repo: virtue-rebirth-app
    sha: eca1d80
    note: docs-only AI 판정 신뢰/제어권 관찰 경계표 추가.
  - repo: infinity
    sha: 350a000
    note: marketing-38 archive + MARKETING_LEARNINGS durable learning 승격 + 보고서.
- urls: []
- next_actions:
  - AI 신뢰 작업은 `MARKETING_LEARNINGS.md`의 `No Autonomous Action Bounds The Trust Question` 기준을 먼저 확인하고, 자율 행동 없는 제품에 agentic guardrail 플레이북을 가져오지 않는다.
  - 결과 카드 신뢰 카피·마지막 선택권 가시화·출력 제어는 proposal-only이며 첫 사용자 관찰 비교 후 별도 승인 Intent에서 결정한다.

## Result

Virtue prelaunch 단계에서 AI 판정(`deed_judged`)이 "믿어라"가 아니라 "참고하고 근거를 보고 마지막 선택은 사람이 한다"로 읽히는지 한 장으로 고정했다. 산출물은 `apps/web/docs/ai-judgment-trust-control-observation-boundary-table.md` 1파일이며 제품 코드, 이벤트, 속성, 카피, PostHog 설정, dashboard, tracking/privacy, 배포, 외부 발송, 비용, 권한 변경은 0건이다.

핵심 결정은 출처 노트(EY·McKinsey)의 AI-trust 플레이북을 그대로 가져오지 않은 것이다. Virtue의 AI는 외부 자율 행동을 하지 않으므로 McKinsey 구분에서 "틀린 행동"이 아니라 "틀린 말" 영역에만 있다. 따라서 신뢰 질문이 "AI가 자동으로 무엇을 해도 되나"에서 "사용자가 출력을 조언(마지막 선택 내 것)으로 읽나, 판결(정체성 사실)로 읽나"로 수축하고, 위험의 본체는 행동적 해가 아니라 자기인식 오보정이며 agentic guardrail/monitoring 플레이북은 범위 밖이다. 낮은 위험 축은 Virtue에서 이미 구조적 최대치(저장 비강제·무시 비용 0·외부 효과 0)라, 관찰 과제는 위험을 낮추는 게 아니라 사용자가 그 낮은 위험·마지막 선택권을 인지하는지다.

first value 매핑은 J1/J2/J4=`deed_saved`(:183), J3=`deed_judged`(:106)로 계승했고, judged−saved 갭은 J3 정상 종료로 둔다. `deed_save_capped`(:167)는 availability/friction으로 분류하며 불신/가치로 환산하지 않는다. `deed_saved`를 판정 승인으로, 미저장 종료를 이탈로 단정하지 않는 신호 경계를 §4에 명시했다.

`MARKETING_LEARNINGS.md`에는 durable learning `No Autonomous Action Bounds The Trust Question`를 승격했다. 이는 `Trust Calibration By Job`를 보완하는 새 축으로, AI 제품의 신뢰 문제 모양이 그 AI가 자율 외부 행동을 하는지에 따라 갈린다는 규칙이다. "Virtue의 낮은 위험 축이 이미 구조적 최대치"라는 관측은 인스턴스 사실이라 원장에 올리지 않고 report에만 보류했다.

## Verification

- Source note `/home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-04-ai-trust-low-stakes-delegation.md` 존재 및 인용 확인(노트 Source Boundary 준수, 외부 설문 수치 미반입).
- 선행 문서 충돌 0: `first-session-jtbd-matrix.md`(m06), `ai-judgment-trust-calibration-audit.md`(m24), `first-60-second-value-observation-script.md`(m20), `product-body-vs-bumper-boundary-table.md`(m31), `activation-candidate-registry.md`(m33), `first-input-defaults-prompt-audit.md`(m32), `ai-outcome-proxy-dictionary.md`, `copy-spec.md`.
- First value mapping conflict 0: J1/J2/J4=`deed_saved`, J3=`deed_judged`.
- 이벤트 앵커 drift 0(rg 재확인: deed_judged:106, deed_rerolled:149, deed_save_capped:167, deed_saved:183).
- Conflict marker 0, 코드 diff 0, 신규 이벤트/속성/카피/dashboard/tracking/privacy/배포 변경 0.
- HTML report gate 통과: `<html`, `<body`, `axis ax1`, `axis ax2`, `<details` 포함.
