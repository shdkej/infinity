# Knowledge Lab 체크포인트 저장 경로 — 실행 기록

## 범위
기존 사용자 변경을 건드리지 않는 targeted checkpoint commit/push 경로를 확인한다. 공개 발송·권한·시크릿 변경·강제 push는 범위 밖이다.

## 확인한 사실
- Infinity `origin/main` canonical revision: `4ed52ffe57aeddf46409280d9f135182e76b7e52`.
- 정본 Inbox card는 `permission_level: approval_required`이며 목표는 Knowledge Lab checkpoint 파일만 선택적으로 커밋하는 경로와 2회 scheduled 검증이다.
- 현재 세션에서 보이는 Gateway automation 목록에는 proposer job이 포함되지 않는다. 따라서 canonical job id/payload를 확인하거나 수정할 수 없다.
- 이 상태에서 job을 추정해 새로 만들거나 payload를 재생성하는 것은 중복·권한 경계 위반 위험이 있어 실행하지 않았다.

## 결과
- Context Pack 생성: `intents/context/learning-candidate-kl-checkpoint-dirty-20261004.json`
- Infinity 원장: Inbox → Active 전환 기록 완료.
- 실제 proposer payload 수정·scheduled 2회 검증: 미실행.
- 정확한 blocker: `external artifact blocker — proposer automation job/payload가 현재 인증 범위에 노출되지 않아 canonical job 확인·수정·실행 불가`.

## 재개 조건
1. proposer automation의 canonical job id와 payload가 현재 Genie 실행 범위에서 조회 가능해질 것.
2. job의 대상 저장소와 checkpoint 파일 목록을 확인할 것.
3. 해당 파일만 stage → non-force push → local/origin SHA 일치 확인을 2회 scheduled run에서 검증할 것.

## 보호 경계
기존 Knowledge Lab dirty 변경은 건드리지 않으며, job 재생성·스케줄 추가·공개 발송·권한/시크릿 변경을 하지 않는다.
