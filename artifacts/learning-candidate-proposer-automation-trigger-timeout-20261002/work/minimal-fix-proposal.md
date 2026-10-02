# T1.2 bounded read·timeout·실패 상태 보존 최소 수정안

실제 proposer runner가 현재 실행 저장소에 없으므로 외부 설정을 추정해 변경하지 않고, 정본 계약에 직접 대응하는 최소 수정 기준을 확정한다.

1. 감시 파일 읽기는 bounded read로 제한하고 읽기 실패·권한 오류를 `evaluation_error`로 보존한다.
2. 평가 subprocess에는 420초 상한을 적용하고 상한 초과는 `timeout` 상태로 닫는다.
3. `output`과 `stdout`이 모두 비면 `no_change`가 아니라 실패 상태로 기록한다.
4. 성공 checkpoint는 허용 쓰기와 각 저장소 `origin/main` SHA 검증 뒤에만 전진한다.
5. 실패·timeout·외부 차단에서는 checkpoint를 전진시키지 않아 다음 주기에 재시도한다.

실제 runner 파일·payload·10회 반복 실행 증거가 없으므로 외부 runtime 변경 완료로 간주하지 않는다.
