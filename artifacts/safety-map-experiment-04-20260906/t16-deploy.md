# T16.1 3차 배포본 갱신·rollback

## 검증한 배포 상태

- Space 정본: `8ecae7ce2396337250839840f2ec9c1d7c98d0e7` (`feat(safety-map): add Rome evidence-empty state`).
- 배포 run: GitHub Actions **Deploy static site to AWS** `34050034361`, 성공, 같은 SHA.
- live URL: `https://safety-map-experiment-03.aws.shdkej.com/` — HTTP 200.
- 라이브 HTML은 `NO SCORE · NO ROUTE · NO TRACKING`을 표시한다.

## 경계와 rollback

이번 cycle은 새 배포나 rollback을 실행하지 않았다. 이번 cycle에서 확인·검증한 상호작용 네트워크 호출은 사용자가 명시적으로 제출한 장소 검색의 Mapbox geocoding 요청이다. 이 관찰은 라이브 앱의 전체 네트워크 요청에 대한 포괄적 감사가 아니다. telemetry SDK·쿠키·localStorage·원격 telemetry 전송은 이번 cycle에서 추가하지 않았다.

Rollback이 필요할 때는 Space의 현재 배포 SHA를 기준으로 변경 원인을 먼저 격리하고, 보호된 runtime config를 보존한 상태에서 승인된 이전 배포 SHA로 되돌린 뒤 HTTP 200, `근거 없음`, `NO SCORE · NO ROUTE · NO TRACKING`, 390px/키보드 흐름을 재검증한다. 이 cycle에는 실패 징후가 없으므로 rollback은 수행하지 않는다.
