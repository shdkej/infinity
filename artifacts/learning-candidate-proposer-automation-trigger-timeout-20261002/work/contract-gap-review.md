# T1.1b runtime 경로와 timeout·checkpoint 계약 대조

## 대조 기준

`source/openclaw-system/docs/SIGNAL_TO_INTENT_PROPOSER.md`의 정본 계약을 T1.1a runtime 인벤토리와 대조했습니다.

| 계약 | 확인 가능한 사실 | 판정 |
|---|---|---|
| timeout 420s | 정본 문서에 선언됨 | 계약 확인 |
| stdout/output 모두 공백이면 실패 | 정본 문서에 선언됨 | 계약 확인 |
| 실패 시 checkpoint 보존 | 정본 문서에 선언됨 | 계약 확인 |
| 실제 runner/payload 구현 | 현재 Infinity 실행 저장소에 없음 | 외부 artifact 필요 |
| 10회 연속 runtime 검증 | runner 부재로 실행 불가 | 미검증 |

## 검증된 대체 경로

실제 runtime을 추정하거나 외부 설정을 바꾸지 않고, 정본 계약 자체를 최소 수정안의 기준으로 채택합니다. 다음 T1.2는 이 기준으로 bounded read, timeout 종료, 실패 상태 보존을 명시한 수정안만 작성하며, 실제 적용·10회 실행은 runner artifact가 확보될 때까지 미검증으로 남깁니다.
