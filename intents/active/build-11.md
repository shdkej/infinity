# build-11: Status 3D Full-Image Floating Menu Redesign

- id: build-11
- status: in_progress
- projects: [infinity, personal-ops, infrastructure]
- task_type: implementation
- topics: [status, dashboard, ui, 3d-background, floating-menu]
- owner: Infinity
- display_name: Status 3D Full-Image Floating Menu Redesign
- created_at: 2026-06-16T11:30Z
- updated_at: 2026-06-16T12:00Z
- source: user correction after build-10 — "음 이 느낙이 아니야"
- predecessor: build-10
- target_repo: `/home/ubuntu/workspace/space/infra-aws-static-sites`
- target_surface: `https://status.aws.shdkej.com`
- target_files:
  - `sites/status/dist/index.html`
  - `sites/status/dist/status.json`
  - `sites/status/dist/assets/`

## Current State (2026-06-16T12:00Z)

Heartbeat Agent가 prepare mode를 완료했다.

- **산출물**: `artifacts/build-11/prepare-3d-floating-status.md`
  - 전체 HTML/CSS/JS 구현 초안 (Option A: raster 3D 이미지, Option B: Three.js canvas)
  - 로컬 실행 명령 및 검증 게이트 포함
- **보고서**: `reports/build-11/2026-06-16T1200Z-prepare.html`

## 다음 단계 (execute_local)

로컬 컴퓨터에서 수행해야 할 작업:

```bash
cd /home/ubuntu/workspace/space/infra-aws-static-sites

# 1. artifacts/build-11/prepare-3d-floating-status.md의 HTML을
#    sites/status/dist/index.html에 적용

# 2. 배경 이미지 생성
magick convert -size 1920x1080 \
  -define gradient:angle=140 \
  gradient:"#050510-#1a0535" \
  -blur 0x6 \
  sites/status/dist/assets/status-3d-bg.jpg

# 3. status.json 재생성
python3 scripts/build-status-json.py --resolve-aws --check

# 4. 로컬 검증
python3 -m http.server 8123 --directory sites/status/dist
chromium --headless --screenshot=/tmp/status-desktop.png --window-size=1440,1100 http://localhost:8123
chromium --headless --screenshot=/tmp/status-mobile.png --window-size=390,844 http://localhost:8123

# 5. 커밋 + S3 배포
git add sites/status/dist/index.html sites/status/dist/assets/ sites/status/dist/status.json
git commit -m "build-11: 3D full-bleed background + floating HUD status redesign"
```

## User Feedback

마스터가 `build-10` 결과에 대해 방향이 다르다고 피드백했다.

핵심 수정:

- 전체적인 메뉴 배치도 바뀑어야 한다.
- 포인트는 **3D 풀 이미지가 백그라운드에 있는 것**이다.
- 메뉴/상태 정보는 그 위에 **살짝 떠 있는 정도**여야 한다.
- 현재 build-10첫럼 glass card와 hero copy가 전면에 오는 구성이 아니다.
- Infinity로 업데이트해 달라고 요청했다.

## Design Direction

### Reject From build-10

- 밀은 wellness glass tone 자체는 참고 가능하지만, 현재 구조첫럼 큰 headline + 큰 status card + panel grid가 주인공이면 안 된다.
- 배경 이미지는 장식이 아니라 첫 화면의 주된 시각 자산이어야 한다.
- 메뉴는 독립 섹션/카드 덧어리보다 floating overlay에 가까워야 한다.

### Target

- 첫 viewport는 3D full-bleed scene/image 중심.
- 3D object/image는 화면 대부분을 차지하고, operational status UI는 그 위에 업네 레이어링.
- 메뉴 구조는 재배치:
  - 상단 또는 측면에 업는 floating navigation/status rail.
  - 주요 상태는 compact HUD 형태.
  - Live Checks / Surfaces / Agent Lane은 하단 또는 측면의 floating drawer/tile cluster로 재구성.
- 레이아웃은 desktop과 mobile 모두에서 이미지의 존재감이 먼저 보여야 한다.
- 텍스트는 적게, 상태 정보는 스캔 가능한 메뉴처럼.

## Verification Required

- Local render check.
- Desktop screenshot (1440x1100).
- Mobile screenshot (390x844).
- Text/menu overlap check.
- `python3 scripts/build-status-json.py --resolve-aws --check`.
- Commit/push.
- Deploy to Status S3/CloudFront and verify remote markers.

## Boundaries

- Do not touch unrelated dirty files such as `sites/travel/dist/travel-data.json`.
- No Terraform/new AWS resource unless separately approved.
- No force-push.
- No secrets or credential changes.
