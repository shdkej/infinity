# [miniapp-image-tools-20261118-qa-01] 이미지 미니앱 보호 QA·연결 복구

- 상태: Waiting — 라이브 하위 경로·합성 브라우저 다운로드는 검증했으나 앱 전용 PostHog 수집·조회는 미검증입니다. 사용자 트래픽·계측 완료가 아닙니다.
- 승인: plan revision 4, slot pilot-qa-01, 2026-11-18T10:40:05Z–11:00:05Z. 연장·재실행·새 cron 없음.
- 최초 인테이크 실제 시각: 2026-11-18T10:56:36Z. 위 시간은 Intent deadline이 아니라 원래 QA 슬롯 범위입니다. 동일 Intent에 plan revision 5, 릴리스 task `miniapp-image-tools-20261118-release-01`, slot `pilot-release-01` (2026-11-18T11:02:00Z–11:22:00Z hard stop)을 연결했습니다. 새 Intent나 자동 재시도는 없습니다.
- 연결 체크포인트: Space `infra-aws-static-sites/sites/miniapp-image-tools/qa/connection-checkpoint.md`, commit `cb55c7856fec37b2895538712c45605dc2eb9104`. PostHog 브라우저는 `/login`으로 이동했고 저장된 로그인과 로컬 kubeconfig는 없습니다. Virtue 키를 전용 앱 키로 사용하지 않습니다.
- 릴리스 증거: Space UI/격리 workflow `a8e26d8ac2ca60babf0b339e19b3f538765f3d42`, Action `44292646921` 성공, 증거 게시 `da30854ae59c8d1ae2a205935ab7cf549b7a4fe1`. 라이브 `https://images.aws.shdkej.com/tools/image-converter/` HTTP 200·브라우저 합성 PNG→WebP 저장/열기 160×80, 기존 `/`·`/sort/` 200. 상세 `infra-aws-static-sites/sites/miniapp-image-tools/qa/release-checkpoint.md`; 보고 `reports/miniapp-image-tools-20261118-qa-01/20261118T1116Z.html`. 새 계측 키·IAM·Terraform·전체 버킷 배포 없음.
- 실제 실행자: WSL의 guarded Hermes child (지니). Ubuntu/server genie_direct가 아님. SAM Slack parent는 인계·검증·복구만 수행.
- 프로젝트: miniapp-image-tools; 소스: `shdkej/space`의 `infra-aws-static-sites/sites/miniapp-image-tools/`; KL WSL 라우트 커밋 `b60dec5805ca6408cf9c57e8be2226beed911a9b`; Space 소스 커밋 `93fb596` (원격 main merge `a6f6a4e1251ec97cda2910ae6ec04020c51dd61c`).
- Pack: `intents/context/miniapp-image-tools-20261118-qa-01.json`; trace: `data/traces/miniapp-image-tools-20261118-qa-01.json`.
- 검증: KL 3 unittest PASS, `zg status` 123/123 ready, Space Node header 3 PASS, 실제 Chromium desktop/390px 모바일과 다운로드·EXIF 90/270·흰 배경·오류·reset 확인. 합성 스크린샷과 열린 출력: `space/infra-aws-static-sites/sites/miniapp-image-tools/qa/evidence/`. 이 검증은 사용자 트래픽이 아닙니다.
- 차단: PostHog의 이 앱 전용 인증된 프로젝트·리전·브라우저 수집키와 동일 qa_run_id 서버 조회가 없음. 합성 트래픽의 사용자 지표 제외도 서버에서 미확인. 사용자 이미지/파일명/EXIF를 이벤트·Slack에 전송하지 않음.
- 원문 스레드: `#desk` channel `C0CE0DV9MM2`, thread `1794983278.888719`; 이 child는 Slack 발신·dispatcher activation을 하지 않음.
- 역할 QA 검토: independent `deleg_c72eb559`, cross-review `deleg_b55a3547`; 결론은 배포·분석 성공 주장 보류.
- 다음 행동: SAM이 앱 전용 PostHog 접근을 명시적으로 배정합니다. 이번 보호 릴리스 슬롯의 결과는 trace/report에 기록하며, 종료 후 자동 재시도하지 않습니다.
