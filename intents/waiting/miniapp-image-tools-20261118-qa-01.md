# [miniapp-image-tools-20261118-qa-01] 이미지 미니앱 보호 QA·연결 복구

- 상태: Waiting — 라이브 하위 경로·합성 브라우저 다운로드는 검증했으나 앱 전용 PostHog 수집·조회는 미검증입니다. 사용자 트래픽·계측 완료가 아닙니다.
- 새 인증·계측 task `miniapp-image-tools-20261118-posthog-01`, plan revision 7, slot `pilot-posthog-01` (2026-11-18T11:55:26Z–12:15:26Z hard stop). 동일 Intent의 후속 슬롯이며 deadline·재개·병렬 인스턴스가 아닙니다. 사용자가 `~/.env` 확인과 브라우저 Google 로그인을 허용했습니다.
- 이번 호스트별 확인: WSL `/home/sam/.env` 존재, 관련 키 이름은 `POSTHOG_ACCESS_TOKEN`; `/home/ubuntu/.env` 없음, Windows `/mnt/c/Users/msi/.env` 없음(다른 시스템 사용자 홈에서도 없음). 값은 저장·게시하지 않았습니다. 기존 개인 API 토큰은 US PostHog 인증에 성공(조직 `sam`, org ID `019e2686-843b-0000-2617-45fd00eb5b46`), EU는 401입니다. MFA나 로그인 부재가 현재 차단 원인은 아닙니다.
- 기존 조직의 프로젝트 목록은 `Default project` 하나(ID `424014`, 2026-05-14 생성, 기존 이벤트 수집 이력 있음)이고 계정의 `organizations_projects` 한도가 1개입니다. 해당 프로젝트는 미니앱 전용으로 검증되지 않아 재사용·이름 변경하지 않았고, 새 조직/계정·유료 한도 변경·Virtue 키 사용도 하지 않았습니다. 전용 공개 브라우저 키를 앱에 연결하거나 배포하지 않았습니다.
- 따라서 이번 슬롯의 브라우저 5종 이벤트 요청·동일 `qa_run_id` 서버 조회·사용자 지표에서 `synthetic` 제외 검증은 수행 불가입니다. 합성 테스트를 사용자 성공으로 계상하지 않습니다. 보고: `reports/miniapp-image-tools-20261118-qa-01/20261118T1201Z.html`.
- 좁은 4역할 독립 검토 `deleg_193bd07f`, 교차 검토 `deleg_578069ed`: 인증된 앱 전용 프로젝트가 없으면 배포·수집 성공을 주장하지 말고 동일 ID 5종/필터 의미를 실제 조회로 입증해야 한다는 결론. 지니는 프로젝트 한도 때문에 안전하게 Waiting 유지.
- 승인: plan revision 4, slot pilot-qa-01, 2026-11-18T10:40:05Z–11:00:05Z. 연장·재실행·새 cron 없음.
- 최초 인테이크 실제 시각: 2026-11-18T10:56:36Z. 위 시간은 Intent deadline이 아니라 원래 QA 슬롯 범위입니다. 동일 Intent에 plan revision 5, 릴리스 task `miniapp-image-tools-20261118-release-01`, slot `pilot-release-01` (2026-11-18T11:02:00Z–11:22:00Z hard stop)을 연결했습니다. 새 Intent나 자동 재시도는 없습니다.
- 연결 체크포인트: Space `infra-aws-static-sites/sites/miniapp-image-tools/qa/connection-checkpoint.md`, commit `cb55c7856fec37b2895538712c45605dc2eb9104`. PostHog 브라우저는 `/login`으로 이동했고 저장된 로그인과 로컬 kubeconfig는 없습니다. Virtue 키를 전용 앱 키로 사용하지 않습니다.
- 릴리스 증거: Space UI/격리 workflow `a8e26d8ac2ca60babf0b339e19b3f538765f3d42`, Action `44292646921` 성공, 증거 게시 `da30854ae59c8d1ae2a205935ab7cf549b7a4fe1`. 라이브 `https://images.aws.shdkej.com/tools/image-converter/` HTTP 200·브라우저 합성 PNG→WebP 저장/열기 160×80, 기존 `/`·`/sort/` 200. 상세 `infra-aws-static-sites/sites/miniapp-image-tools/qa/release-checkpoint.md`; 보고 `reports/miniapp-image-tools-20261118-qa-01/20261118T1116Z.html`. 새 계측 키·IAM·Terraform·전체 버킷 배포 없음.
- 실제 실행자: WSL의 guarded Hermes child (지니). Ubuntu/server genie_direct가 아님. SAM Slack parent는 인계·검증·복구만 수행.
- 프로젝트: miniapp-image-tools; 소스: `shdkej/space`의 `infra-aws-static-sites/sites/miniapp-image-tools/`; KL WSL 라우트 커밋 `b60dec5805ca6408cf9c57e8be2226beed911a9b`; Space 소스 커밋 `93fb596` (원격 main merge `a6f6a4e1251ec97cda2910ae6ec04020c51dd61c`).
- Pack: `intents/context/miniapp-image-tools-20261118-qa-01.json`; trace: `data/traces/miniapp-image-tools-20261118-qa-01.json`.
- 검증: KL 3 unittest PASS, `zg status` 123/123 ready, Space Node header 3 PASS, 실제 Chromium desktop/390px 모바일과 다운로드·EXIF 90/270·흰 배경·오류·reset 확인. 합성 스크린샷과 열린 출력: `space/infra-aws-static-sites/sites/miniapp-image-tools/qa/evidence/`. 이 검증은 사용자 트래픽이 아닙니다.
- 차단: 기존 US 조직 1프로젝트 한도가 이미 사용 중이어서 앱 전용 프로젝트·브라우저 수집키와 동일 qa_run_id 서버 조회가 없음. 합성 트래픽의 사용자 지표 제외도 서버에서 미확인. 사용자 이미지/파일명/EXIF를 이벤트·Slack에 전송하지 않음.
- 원문 스레드: `#desk` channel `C0CE0DV9MM2`, thread `1794983278.888719`; 이 child는 Slack 발신·dispatcher activation을 하지 않음.
- 역할 QA 검토: independent `deleg_c72eb559`, cross-review `deleg_b55a3547`; 결론은 배포·분석 성공 주장 보류.
- 다음 행동: 사용자가 기존 앱 전용 PostHog 프로젝트 접근을 제공하거나 현 조직의 프로젝트 한도 해소 방식을 결정합니다. 이번 보호 계측 슬롯 종료 후 자동 재시도하지 않습니다.

## 2026-11-19 일일 계획 · revision 1

- plan_id: `miniapp-image-tools-20261119`; plan_revision: 1; 생성: `2026-11-19T01:04:00Z` (10:04 KST). 기존 Waiting Intent 하나에 연결하며 새 Intent/큐를 만들지 않는다.
- 근거: 라이브 하위 경로와 합성 브라우저 다운로드는 전일 확인됐지만 앱 전용 PostHog 계측은 사용자 프로젝트 한도 때문에 미검증이다. 오늘의 지표는 사용자 세션/수집 이벤트를 실제 관측할 수 있는지와 그 출처·QA 제외 여부다. 관측 전 숫자 목표나 0건 성공 판정은 두지 않는다.

### 슬롯

| task_id | slot_id/revision | start_at–end_at (UTC; KST) | 절차·증거·정책·결과 |
| --- | --- | --- | --- |
| `miniapp-image-tools-20261119-observe-01` | `clockin-observation-01` / 1 | `2026-11-19T01:05:00Z`–`01:20:00Z` (10:05–10:20) | Windows 검증 실행 진입점에서만 현재 앱 지표·데이터 원천을 읽기 전용으로 조회한다. 각 지표의 실제 관측 시각, 표본/분모, QA 제외 방법, 프로젝트 귀속·조회 경로를 보고하고 미수집·접근 불가와 0을 구분한다. 자격증명·이미지 메타데이터를 출력하지 않는다. 결과는 원문 Slack thread와 이 Intent에 둔다. |
| `miniapp-image-tools-20261119-plan-01` | `clockin-plan-01` / 1 | `2026-11-19T01:20:00Z`–`01:40:00Z` (10:20–10:40) | 관측 결과 및 전일 라이브/QA 증거를 회수해 오늘 목표·우선순위·예상 결과·반증 기준을 정하고 Infinity에 기록한다. 관측이 없으면 측정 공백을 근거로 삼고 숫자 목표를 만들지 않는다. SAM 계획만 수행하며 프로젝트 실행은 하지 않는다. 결과는 원문 Slack thread와 이 Intent에 둔다. |

- action_policy: 관측은 검증된 Windows guarded 실행 경로, 읽기 전용·최초 end_at 고정·중복이면 중지. SAM 계획은 결과/원격 증거 회수 및 계획 기록만 허용. 추가 비용, 권한, PostHog 프로젝트 변경, 앱 변경·배포는 금지.
- result_destination: 이 detail 파일과 원문 Slack thread `C0CE0DV9MM2/1794983278.888719`.
- 판정 기준: 실제 사용자 지표의 원천·표본·관측시각·합성 제외를 입증할 수 있을 때만 지표 기반 목표를 세운다. 근거가 없으면 해당 공백을 기록하고 계측 접근 가능 범위의 다음 절차만 제안한다.

- 10:06 KST handoff status: Slack 전송 영수증과 Windows `U0CHX8QA7S8`의 실제 ACK를 확인했다 ([handoff](https://shdkej.slack.com/archives/C0CE0DV9MM2/p1795050316300149), [guard ACK](https://shdkej.slack.com/archives/C0CE0DV9MM2/p1795050359542979)). guard 상태는 `running`, 최초 종료 시각 `2026-11-19T01:20:00Z` 유지다. 결과는 아직 대기 중이며 미수집/0으로 간주하지 않는다.
- 10:20 SAM 계획 예약: `f94e2c4f-b3b8-49d3-a17e-3e488809c5a4`, declarationKey `miniapp-image-tools:20261119:clockin-plan-01`, agent `main`, isolated, 단발 `2026-11-19T01:20:00Z`, delete-after-run, delivery none. 저장 후 `cron get`에서 시각·소유자·본문·활성 상태를 재확인했다.
