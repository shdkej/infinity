# marketing-32 Virtue 첫 입력 기본값/예시/placeholder 감사표

- id: marketing-32
- status: archived
- completed_at: 2026-06-01T10:07
- projects: [virtue]
- task_type: strategy
- topics: [onboarding, activation, ai-product]
- result_summary: Amplitude agent default-prompt 렌즈를 Virtue `/add` 첫 입력 유도의 잡별 내부 감사로 번역. Virtue 첫 입력 기본값은 예시·추천 질문 0의 "질문형 placeholder + 빈 슬롯" 단일 패턴이라 support-bot 유도 위험은 0이나 잡별 조향도 0이며, 첫 입력 단계에서 J3·J2가 가장 약하게 불린다.
- artifacts:
  - path: apps/web/docs/first-input-defaults-prompt-audit.md (virtue-rebirth-app)
    role: design
    note: J1~J4 × 첫 입력 기본값 감사표 + 후속 행동 번역 + prelaunch 금지선 (신규 1파일)
- reports:
  - path: reports/marketing-32/2026-06-01T1007Z-local.html
    role: final
- source:
  - path: source/external-links/marketing/2026-06-01-agent-default-prompts-retention.md
    note: Amplitude default-prompts/agent-retention 출처노트
- commits:
  - repo: virtue-rebirth-app
    sha: aabf565
    note: docs: add first-input defaults/prompt audit (marketing-32)
  - repo: infinity
    sha: this commit
    note: INTENTS/archive/report/learnings 업데이트
- verification:
  - 코드 diff 0 (apps/web/docs 1파일만)
  - 신규 이벤트/속성 0
  - conflict marker 0
  - source note 경로 + first value 매핑(J1/J2/J4=`deed_saved`, J3=`deed_judged`) 인용 확인
  - 인용 이벤트 앵커 현행 일치: `deed_judged`:106 / `deed_rerolled`:149 / `deed_saved`:183 / `deed_save_capped`:167 / `level_up_viewed`:199
  - HTML 보고서 `<html`/`<body`/axis ax1/axis ax2/`<details` 포함
  - 선행 6문서 + copy-spec 충돌 0
- next_actions:
  - 첫 10~20명 손기록 표에 "첫 입력 출처"·"후속 행동" 칸을 baseline/60초 양식에 증설(관찰 양식, 코드 속성 아님)
  - J3가 첫 입력 단계에서 반복적으로 약하게 불리는 패턴이 보이면 잡별 예시 조향을 별도 Intent(approval-needed)에서 검토
  - mock/ai 라벨 분기가 J3 첫 인상을 낮추는 문제는 런타임 모드 정책으로 proposal-only 기록만
