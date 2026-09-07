# Slack 실패 메시지·원격 기준 검증 보호

- `safe_failure_alert.py`는 raw shell stderr를 읽더라도 allowlist된 한국어 상태 문구와 reason code/hash만 출력한다.
- `run_dispatcher_cycle.sh`는 failure를 안전 상태로 기록하고 nonzero shell 종료를 generic raw failure alert로 승격하지 않는다. raw detail은 0700 state directory의 run record에만 남는다.
- dispatcher plan과 terminal 점검은 `origin/main` detached worktree를 만들어 clean 상태에서 수행한다. 기존 로컬 main은 검증 기준으로 쓰지 않는다.
- `verify_origin_main_worktree.sh`는 fetch → detached worktree → clean assert → read-only command → clean assert를 제공한다.
