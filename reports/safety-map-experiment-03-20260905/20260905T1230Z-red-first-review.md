# Red 1차 검증 — 수정 필요

## 판정

`RED_STATUS: fail`

## 확인된 통과 항목

- 라이브 지도 캔버스, 장소 검색, 기본·위성 레이어 전환, 390px 가로 넘침 없음은 확인되었습니다.
- experiment-03 전용 사이트, runtime 설정 생성 스크립트, registry, runtime 파일 무시 규칙이 Space 원격에 있으며 legacy `sites/safety-map/**`는 e03 커밋 범위에서 변경되지 않았습니다.

## 수정 필요 항목

- `events.mapbox.com` 성능 측정 전송이 관찰되어 `NO TRACKING` 경계와 충돌했습니다.
- Red가 읽은 Infinity 원격 정본은 T3.3 차단과 T4·T5 대기를 기록해 실제 배포 증거와 동기화되지 않았습니다.

## 보완과 재개 조건

- 지도 생성 옵션에 `performanceMetricsCollection:false`를 적용해 성능 측정 전송을 차단했습니다.
- 보완 커밋 배포 성공과 브라우저 네트워크 재검사 뒤 별도 Red 재검증을 요청합니다.
- runtime 설정 값은 계속 어떤 보고서·추적 파일에도 기록하지 않습니다.
