# [miniapp-image-tools-20261118-qa-01] 이미지 미니앱 보호 QA·연결 복구

- 상태: Waiting — WSL 실행자가 검증 가능한 범위의 로컬 QA와 소스 게시를 마쳤으나 PostHog 프로젝트 인증·안전한 라이브 배포 경로가 미확인입니다. 이 상태는 제품 출시·고객 성공이 아닙니다.
- 승인: plan revision 4, slot pilot-qa-01, 2026-11-18T10:40:05Z–11:00:05Z. 연장·재실행·새 cron 없음.
- 실제 실행자: WSL의 guarded Hermes child (지니). Ubuntu/server genie_direct가 아님. SAM Slack parent는 인계·검증·복구만 수행.
- 프로젝트: miniapp-image-tools; 소스: `shdkej/space`의 `infra-aws-static-sites/sites/miniapp-image-tools/`; KL WSL 라우트 커밋 `b60dec5805ca6408cf9c57e8be2226beed911a9b`; Space 소스 커밋 `93fb596` (원격 main merge `a6f6a4e1251ec97cda2910ae6ec04020c51dd61c`).
- Pack: `intents/context/miniapp-image-tools-20261118-qa-01.json`; trace: `data/traces/miniapp-image-tools-20261118-qa-01.json`.
- 검증: KL 3 unittest PASS, `zg status` 123/123 ready, Space Node header 3 PASS, 실제 Chromium desktop/390px 모바일과 다운로드·EXIF 90/270·흰 배경·오류·reset 확인. 합성 스크린샷과 열린 출력: `space/infra-aws-static-sites/sites/miniapp-image-tools/qa/evidence/`. 이 검증은 사용자 트래픽이 아닙니다.
- 차단: PostHog의 이 앱 전용 인증된 프로젝트·리전·브라우저 수집키와 동일 qa_run_id 서버 조회가 없음. `images.aws.shdkej.com/tools/image-converter/`는 403. 기존 이미지 사이트 루트와 `/sort/`는 200이어도 새 경로 소유·배포 권한 증거가 아님. 사용자 이미지/파일명/EXIF를 이벤트·Slack에 전송하지 않음.
- 원문 스레드: `#desk` channel `C0CE0DV9MM2`, thread `1794983278.888719`; 이 child는 Slack 발신·dispatcher activation을 하지 않음.
- 역할 QA 검토: independent `deleg_c72eb559`, cross-review `deleg_b55a3547`; 결론은 배포·분석 성공 주장 보류.
- 다음 행동: SAM이 앱 전용 PostHog 접근 및 새 정적 하위 경로 배포 소유·권한을 확인하고 별도 승인 슬롯을 배정해야만 라이브 계측/배포 검증을 재개합니다. 그 전에는 반복 실행하지 않습니다.
