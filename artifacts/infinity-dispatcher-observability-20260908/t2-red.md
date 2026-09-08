# T2.2 Red — metrics and dashboard review

- **판정:** PASS (필수 수정 1건 반영 후 재검증)
- **수정:** exporter가 `git rev-parse`를 사용하지만 Alpine runtime에 Git이 없던 결함을 `RUN apk add --no-cache git`로 보완했다.
- **metric contract:** dashboard가 조회하는 recent run, revision mismatch, Active freshness와 source-invalid `snapshot_read_error`를 exporter가 실제로 노출한다. source parse 실패는 false 0/정지로 위장하지 않고 error/unknown으로 남긴다.
- **fixture:** 정상 metric, run record 부재, SHA mismatch, malformed trace fail-safe를 포함한 3개 테스트가 통과했다.
- **표현/경계:** dashboard는 read-only 다음 점검 위치만 제시하며 자동 복구·cron 전체 중단·알림 성공/유실·Grafana 효과를 주장하지 않는다. SHA·intent ID·사용자 텍스트는 labels로 노출하지 않는다.
- **미검증:** Docker CLI 부재로 compose config와 컨테이너 기동은 검증하지 못했다. 실제 배포·cron·notifier·alert·권한·시크릿 변경은 수행하지 않았다.
