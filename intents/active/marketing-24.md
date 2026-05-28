# marketing-24 Virtue AI 판정 신뢰 보정 감사표 작성

- id: marketing-24
- status: in_progress
- priority: high
- permission: L2 (내부 문서 작업, agent-approved)
- mode: execute_local
- goal: J1~J4별 AI 판정 신뢰 설명·한계·제어권을 감사한 표를 apps/web/docs/ai-judgment-trust-calibration-audit.md 1파일로 작성
- project: virtue
- started_at: 2026-05-28T06:00Z
- success_criteria: |
    rg 'deed_judged|deed_saved|trust|신뢰|J1|J2|J3|J4' apps/web/docs/ai-judgment-trust-calibration-audit.md 핵심 매핑 전부 탐지
    git diff --stat 문서 1파일 변경만 표시
- artifact_draft: artifacts/marketing-24/ai-judgment-trust-calibration-audit.md
- source_note: /home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-28-ai-trust-calibration.md

## L2 agent-approved 판단 근거

- 목표 Intent와 직접 연결된 작업: YES (내부 문서 1파일 추가)
- 되돌림 가능: YES (git revert로 복원 가능)
- 예상 비용 없음: YES
- 프로덕션 데이터/시크릿/운영 권한 변경 없음: YES
- 타인에게 메시지 없음: YES
- 실행 전 상태 확인: YES (선행 문서 8종 충돌 0 확인)
- 검증 방법 명시: YES (rg gate + git diff --stat)

## 로컬 실행 지시

```
Infinity Intent: marketing-24 Virtue AI 판정 신뢰 보정 감사표 작성
Mode: execute_local
Goal: artifacts/marketing-24/ai-judgment-trust-calibration-audit.md 를
      /home/ubuntu/dev/virtue-rebirth-app/apps/web/docs/ai-judgment-trust-calibration-audit.md 로 복사 후 커밋·push

Context:
  - Target repo: /home/ubuntu/dev/virtue-rebirth-app
  - Source: infinity repo artifacts/marketing-24/ai-judgment-trust-calibration-audit.md
  - 선행 문서: apps/web/docs/ 내 다른 marketing-*.md 파일 (충돌 없음 확인됨)

Allowed: L0/L1 (내부 문서 파일 1개 추가)
Forbidden: 코드·카피·이벤트·배포·외부발송·비용·시크릿 변경

Verification:
  1. rg 'deed_judged|deed_saved|trust|신뢰|J1|J2|J3|J4' apps/web/docs/ai-judgment-trust-calibration-audit.md
  2. git diff --stat (1파일만 변경)
  3. Commit: "docs: Virtue AI 판정 신뢰 보정 감사표 추가 (marketing-24)"
  4. Push to origin master (L2 agent-approved)

After push:
  - Update infinity INTENTS.md: marketing-24 → archived
  - Create intents/archive/marketing-24.md
  - Send Telegram: ✅ marketing-24 완료
```
