# T15.1 개인식별·위치 없는 telemetry 계약

## 현재 결정

이 cycle은 **문서 계약만** 만든다. telemetry는 기본값 `off`이며, SDK·쿠키·localStorage·네트워크 전송·원격 콘솔 전송·배포를 추가하지 않는다. 기존 `NO TRACKING` 표현과 provenance의 telemetry 금지는 유지한다.

## 목적과 허용 후보

향후 명시적 opt-in, 개인정보 검토, Red PASS, 승인 및 별도 배포가 모두 완료된 경우에만 제품 사용성·오류 개선을 위한 **배포본/일 단위 집계**를 검토할 수 있다. 후보는 `ui_control_activated`, `search_submitted`, `search_no_result`, `client_error_class`, `a11y_focus_reached`의 결과 카운트로 제한한다.

허용 최소 필드 후보: `event_name`, UTC 일 단위 `occurred_at_bucket`, `release_id`, `surface`(`desktop`/`mobile`), 제한된 `result`, `privacy_version`. 원본 이벤트 보존은 0이며, 작은 표본은 억제하고 데이터가 없으면 `no_evidence`로 표시한다.

## 금지와 분리

IP, 계정·쿠키·광고·세션·기기 식별자, fingerprint, 검색어·자유 입력·지역명, URL query, 원문·작성자 데이터, 주소·좌표·위치·지도 viewport, 재식별 가능한 timestamp 조합, 제3자 전송 및 출처 간 결합을 금지한다.

telemetry 동의·상태는 근거 적격성, 신호 렌더, 핀, 집계, 점수, 경로, 안전·위험 주장 권한을 만들지 않는다. 거부·철회는 핵심 기능에 불이익 없이 즉시 미수집 상태를 유지해야 한다. ‘익명’ 또는 ‘추적하지 않는다’ 같은 절대 표현은 사용하지 않는다.

## 향후 release gate

별도 T15.2 Red, 사용자 승인, opt-in UI와 목적·보존·철회 경로, feature flag default-off, 최소 권한·삭제 절차, T16의 배포/rollback·라이브 검증 전에는 이 계약을 구현하거나 활성화하지 않는다.

## 역할 수렴

- Planner: 운영 건강 목적 외 추론 금지, raw event 미보존.
- Developer: 최소 스키마만 정의하고 코드·전송을 만들지 않음.
- Marketer: 동의가 안전 추천이나 개인화로 읽히지 않도록 목적·거부·철회를 명확히 함.
- Operator: SDK·저장소·전송·배포는 별도 승인·Red·rollback gate 전까지 금지.
