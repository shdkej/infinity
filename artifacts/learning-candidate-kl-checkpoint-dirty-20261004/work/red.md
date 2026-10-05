# Red 검증

- red_status: fail
- 판정: Waiting 전환은 타당하지만 완료/Archive 조건은 충족하지 않음.
- 통과: 요청 일치, dirty 변경 보호, Planner·Developer·Marketer·Operator 기록, 외부 proposer artifact blocker의 구체성.
- 실패: 기존 report의 원격 SHA가 현재 `origin/main` 및 `ls-remote`와 불일치했고, trace가 `active`/빈 verification으로 남아 있었음.
- 현재 read-only 원격 확인: `HEAD=7cab7042c78832e71170e7e006067067502cf91c`, `origin/main=7528157b036f63c8f69f44eb4613f33f89066862`, `ls-remote=7528157b036f63c8f69f44eb4613f33f89066862`.
- 재개 조건: proposer canonical job/payload 접근 권한 확보 후 대상 경로를 확인하고, 승인된 targeted checkpoint 실행과 2회 scheduled 검증을 수행한 뒤 Red 재검증.
