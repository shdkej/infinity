# Operator
- 기존 `data/dispatcher-terminal-notifications.json`은 staging 금지.
- 현재 로컬은 origin/main보다 뒤처져 있으므로 local branch에서 push하지 않는다.
- 재개 시 fetch → clean temporary checkout → exact-path stage → non-force push → `HEAD`, `origin/main`, `ls-remote` SHA 비교 순서로 실행한다.
- job/payload가 현재 인증 범위에 없으므로 스케줄 추가·재생성·권한 변경은 하지 않는다.
