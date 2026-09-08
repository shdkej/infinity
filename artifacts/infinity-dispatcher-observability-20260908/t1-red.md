# T1.2 Red — 원인·범위 검증

- **판정:** PASS
- **검증 대상:** `root-cause.md`, `INTENTS.md`, `task-plan.json`, `task-plan.md`, trace
- **요청 일치:** dispatcher의 post-handoff notifier 관측 결함만 다룬다.
- **표현 경계:** cron 전체 중단, 사용자 알림 성공·유실, 전체 알림 시스템 장애, Grafana 효과는 증명하지 않는다고 명시돼 있다.
- **L0 경계:** dispatcher run record와 canonical Git ref를 read-only로 읽는 지표 계약만 허용한다. cron·배포·권한·시크릿·자동 알림 발송은 제외한다.
- **사용자 표시:** scrape 실패, 최근 실행 기록 없음, revision 불일치, Active 갱신 지연을 각각 다음 점검 위치로만 제시한다.
- **필수 수정:** 없음.

다음 leaf는 각 지표의 값·신선도·결정 규칙을 고정해야 하며, 이 PASS를 구현 또는 운영 개선 효과의 증거로 해석하지 않는다.
