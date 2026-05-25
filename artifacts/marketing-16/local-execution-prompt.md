# Local Execution Prompt: marketing-16

Infinity Intent: marketing-16 Virtue 첫 세션 3-스크린 가치 경로 감사표  
Mode: execute_local  
Required workflow: Use workflow-master first. Read and follow `.agent/workflows/workflow-master.md` or `WORKFLOW-MASTER.md` when present before doing implementation work.

## Goal

`artifacts/marketing-16/three-screen-value-path-audit-draft.md` 초안을 그대로 `virtue-rebirth-app/apps/web/docs/three-screen-value-path-audit.md`로 작성하고, 커밋·push한다.

## Context

- Cloud draft 위치: `shdkej/infinity` 레포, `artifacts/marketing-16/three-screen-value-path-audit-draft.md`
- Output target: `/home/ubuntu/dev/virtue-rebirth-app/apps/web/docs/three-screen-value-path-audit.md`
- 기존 참조 문서: `virtue-rebirth-app/apps/web/docs/` 하위 `first-session-jtbd-matrix.md`, `activation-milestone-ladder.md`, `ios-activation-event-parity-brief.md`

## Prepared findings (Cloud 분석 요약)

- J1 기록형: ✅ 3화면 닫힘 (`add_flow_started` → `deed_saved`)
- J2 누적형: ⚠️ 조건부 닫힘 (`level_up_viewed` 임계값 조건)
- J3 AI 호기심형: ⚠️ 조건부 닫힘 (비동기 `deed_judged` 대기)
- J4 회고형: ❌ 구조적 미닫힘 (이력 없이 회고 불가)
- 기존 이벤트 4종 재사용. 신규 이벤트·속성·코드 변경 0

## Steps

1. `shdkej/infinity` 레포의 `artifacts/marketing-16/three-screen-value-path-audit-draft.md` 내용 확인
2. `virtue-rebirth-app/apps/web/docs/` 디렉토리 존재 확인
3. 기존 문서 3종 빠르게 열람: 충돌 마커 확인 (`grep -r "three-screen" apps/web/docs/`)
4. 충돌 없으면 draft 내용 그대로 `apps/web/docs/three-screen-value-path-audit.md`로 저장
5. `git add apps/web/docs/three-screen-value-path-audit.md`
6. `git commit -m "docs: add three-screen value path audit (marketing-16)"`
7. `git push origin HEAD`

## Allowed

L0/L1 작업만: 파일 쓰기, git add/commit/push

## Forbidden

- 신규 이벤트·속성 추가
- 기존 코드 수정
- 카피 앱 반영
- 대시보드 생성·수정
- 외부 발송·비용 집행

## Verification

- `git log --oneline -1` 으로 커밋 확인
- `git status` 가 clean 인지 확인
- HEAD가 origin과 일치하는지 확인

## Report back

완료 후 `shdkej/infinity` 레포의 `reports/marketing-16/{timestamp}-local.md`에 결과 기록  
(commit SHA, 파일 경로, 검증 결과 포함)
