# Infinity Intent: marketing-26 — Virtue recovery-over-streak 리텐션 렌즈 작성

**Mode:** execute_local
**Required workflow:** Use workflow-master first. Find it under `~/.claude/skills/workflow-master/` and `~/.claude/agents/workflow-master.md` before falling back to repo-local `.agent/workflows/workflow-master.md` or `WORKFLOW-MASTER.md`. Do not proceed as a single direct executor unless workflow-master explicitly classifies the task as trivial and records that decision.

---

## Goal

`apps/web/docs/recovery-over-streak-retention-lens.md` 파일을 virtue-rebirth-app에 신규 추가.

- Recovery-over-streak 렌즈를 J1-J4 표로 정리
- Public copy/feature 변경은 §8 proposal-only로 분리
- 기존 3 선행 문서와 충돌 없음 확인

---

## Context

- **Repo**: `/home/ubuntu/dev/virtue-rebirth-app`
- **Target file**: `apps/web/docs/recovery-over-streak-retention-lens.md` (신규 1파일)
- **Source note**: `/home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-29-streak-flexibility-recovery-retention.md`
- **Existing related docs** (conflict check 필수):
  - `apps/web/docs/seven-day-deed-loop.md`
  - `apps/web/docs/first-week-activation-retention-bridge.md`
  - `apps/web/docs/retention-predictive-activation-brief.md`

---

## Prepared Findings (Cloud Draft)

Cloud 초안: `infinity/artifacts/marketing-26/draft.md`

초안 포함 섹션:
- §1 렌즈 배경 (Duolingo/Reforge/HabitBoard → Virtue 번역) — **source note에서 구체 수치 반영 필요**
- §2 핵심 표: J1-J4 × 4시나리오 (skip/recovery/monthly/comeback)
- §3 이벤트 근거 (기존 6개, 신규 0)
- §4 Skip vs. 정상 종료 구별
- §5 Monthly Completion 밀도 렌즈
- §6 Comeback Session 정의 및 관찰 포인트
- §7 선행 3문서 충돌 확인
- §8 Proposal-Only 섹션 (P1-P3)
- §9 Prelaunch 금지선

---

## Steps

1. **Source note 읽기**: `/home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-29-streak-flexibility-recovery-retention.md`
   - Duolingo/Reforge/HabitBoard 구체적 데이터 포인트 추출
   - §1에 수치/인용 반영

2. **선행 3문서 읽기** (충돌 확인):
   - `seven-day-deed-loop.md`: D1/D3/D7 루프와 호환 확인
   - `first-week-activation-retention-bridge.md`: first value 매핑 계승 확인
   - `retention-predictive-activation-brief.md`: depth signal 용어 충돌 없는지 확인

3. **초안(infinity/artifacts/marketing-26/draft.md) 기반** + source note 데이터 통합 → 최종 문서 작성

4. **`apps/web/docs/recovery-over-streak-retention-lens.md` 파일 저장**

5. **검증 게이트 4개 통과 확인**:
   - [ ] conflict marker 0 (`<<<<<<<` 없음)
   - [ ] 신규 이벤트명 0 (whitelist만: `add_flow_started`/`deed_judged`/`deed_saved`/`level_up_viewed`/`deed_rerolled`/`deed_save_capped`)
   - [ ] 코드 diff 0 (`apps/web/docs/` 외 파일 변경 없음)
   - [ ] first value 매핑 유지 (J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106)

6. **`git status` 확인** → `apps/web/docs/recovery-over-streak-retention-lens.md` 1파일만 변경

7. **git commit**: `feat(docs): add recovery-over-streak retention lens for J1-J4`

8. **git push** (L2 agent-approved 조건 확인: 일반 push, fast-forward, 타인 작업 덮어쓰기 없음)

---

## Allowed / Forbidden

**Allowed**: L0/L1 actions only

**Forbidden (절대 금지)**:
- 신규 이벤트·속성 추가
- 코드 파일 수정 (`.tsx`, `.ts`, `.js` 등)
- 카피/UI 텍스트 직접 변경
- 계측·대시보드·세션리플레이 설정 변경
- 외부발송·비용·시크릿·권한·개인정보 관련 변경
- 기존 3 선행 문서 수정

---

## Verification

완료 후 확인 사항:
- `git diff HEAD` → docs 1파일만 변경
- conflict marker grep: `grep -r '<<<<<<<' apps/web/docs/` → 0건
- 이벤트 whitelist 이탈 grep: `grep -E 'deed_[a-z_]+' apps/web/docs/recovery-over-streak-retention-lens.md` → whitelist 6개만
- `git log --oneline -3` → 커밋 정상 확인
- `git status` → `HEAD == origin/master` (또는 fast-forward)

---

## Report Back

완료 보고: `infinity/reports/marketing-26/{timestamp}-local.html` (결론 2축 양식, ARTIFACT_RULES.md 참조)

---

## After Completion

1. `infinity/INTENTS.md`에서 marketing-26 status → `archived` 처리
2. `infinity/intents/archive/marketing-26.md` 생성 (canonical final index, ARTIFACT_RULES.md 표준 포맷)
   - `result_summary`, `artifacts`, `reports`, `commits` 링크 포함
3. `infinity` 커밋 & 푸시 (L2 agent-approved: 일반 push)
