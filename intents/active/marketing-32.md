# marketing-32: Virtue `/add` 첫 입력 기본값/예시 감사표 작성

- id: marketing-32
- status: in_progress
- priority: medium
- permission: L1
- project: virtue
- added: 2026-06-01T10:07Z

## 현재 상태

coud draft 완료. §4 심장표 [CODE_CHECK] 칸은 local Claude Code가 virtue-rebirth-app 코드 확인 후 채울 예정.

산출물 위치:
- `artifacts/marketing-32/first-input-defaults-prompt-audit.md` (cloud draft)
- `source/external-links/marketing/2026-06-01-agent-default-prompts-retention.md` (source note)

## 다음 액션 (local Claude Code)

1. `virtue-rebirth-app/apps/web/app/add/page.tsx` 의 placeholder, example text, CTA label 확인
2. `artifacts/marketing-32/first-input-defaults-prompt-audit.md` §4 심장표 [CODE_CHECK] 칸 채우기
3. 최종 문서를 `apps/web/docs/first-input-defaults-prompt-audit.md` 에 작성 (코드 diff 0, doc만)
4. HTML report `reports/marketing-32/{timestamp}-local.html` 작성 (template: reports/_TEMPLATE.html)
5. virtue-rebirth-app에 commit & push (L2 agent-approved 조건 확인)

## 성공 기준

- `virtue-rebirth-app/apps/web/docs/first-input-defaults-prompt-audit.md` 신규 1파일
- J1~J4 × 현재 첫 입력 유도 표 (§4 심장표 [CODE_CHECK] 모두 채워짐)
- 후속 행동 후보, prelaunch 금지선, 기존 이벤트 매핑 포함
- 코드 diff 0, 신규 이벤트/속성 0, conflict marker 0
- source note 경로 인용, first value 매핑 명시
