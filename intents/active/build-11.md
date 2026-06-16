# build-11: Status 3D Full-Image Floating Menu Redesign

- id: build-11
- status: in_progress
- projects: [infinity, personal-ops, infrastructure]
- task_type: implementation
- topics: [status, dashboard, ui, 3d-background, floating-menu]
- owner: Infinity
- display_name: Status 3D Full-Image Floating Menu Redesign
- created_at: 2026-06-16T11:30Z
- updated_at: 2026-06-16T11:30Z
- source: user correction after build-10 — "음 이 느낌이 아니야"
- predecessor: build-10
- target_repo: `/home/ubuntu/workspace/space/infra-aws-static-sites`
- target_surface: `https://status.aws.shdkej.com`
- target_files:
  - `sites/status/dist/index.html`
  - `sites/status/dist/status.json`
  - `sites/status/dist/assets/`

## User Feedback

마스터가 `build-10` 결과에 대해 방향이 다르다고 피드백했다.

핵심 수정:

- 전체적인 메뉴 배치도 바뀌어야 한다.
- 포인트는 **3D 풀 이미지가 백그라운드에 있는 것**이다.
- 메뉴/상태 정보는 그 위에 **살짝 떠 있는 정도**여야 한다.
- 현재 build-10처럼 glass card와 hero copy가 전면에 오는 구성이 아니다.
- Infinity로 업데이트해 달라고 요청했다.

## Design Direction

### Reject From build-10

- 밝은 wellness glass tone 자체는 참고 가능하지만, 현재 구조처럼 큰 headline + 큰 status card + panel grid가 주인공이면 안 된다.
- 배경 이미지는 장식이 아니라 첫 화면의 주된 시각 자산이어야 한다.
- 메뉴는 독립 섹션/카드 덩어리보다 floating overlay에 가까워야 한다.

### Target

- 첫 viewport는 3D full-bleed scene/image 중심.
- 3D object/image는 화면 대부분을 차지하고, operational status UI는 그 위에 얇게 레이어링.
- 메뉴 구조는 재배치:
  - 상단 또는 측면에 얇은 floating navigation/status rail.
  - 주요 상태는 compact HUD 형태.
  - Live Checks / Surfaces / Agent Lane은 하단 또는 측면의 floating drawer/tile cluster로 재구성.
- 레이아웃은 desktop과 mobile 모두에서 이미지의 존재감이 먼저 보여야 한다.
- 텍스트는 적게, 상태 정보는 스캔 가능한 메뉴처럼.

## Prepare Artifact (Cloud — 완료)

- **산출물**: `artifacts/build-11/index-prepare-v1.html`
- **내용**: CSS perspective grid full-bleed 배경 + floating nav rail (상단 pill) + center HUD (큰 ok/total 숫자 + spinning ring) + bottom drawer (Live Checks / Surfaces / Agent Lane 3개 tile 섹션)
- **상태**: 로컬 실행 대기. 아래 체크리스트 따라 배포하면 됨.

## Next Actions (Local Claude 실행)

1. `artifacts/build-11/index-prepare-v1.html` → `sites/status/dist/index.html` 복사
2. 로컬 브라우저에서 `python3 -m http.server` 미리보기
3. 데스크톱 + 모바일 스크린샷 촬영
4. 텍스트/메뉴 overlap 점검
5. `python3 scripts/build-status-json.py --resolve-aws --check`
6. 커밋 & 푸시
7. S3/CloudFront 배포 및 원격 https://status.aws.shdkej.com 확인
8. unrelated dirty files(`sites/travel/dist/travel-data.json` 등) 건드리지 않기

## Verification Required

- Local render check.
- Desktop screenshot.
- Mobile screenshot.
- Text/menu overlap check.
- `python3 scripts/build-status-json.py --resolve-aws --check`.
- Commit/push.
- Deploy to Status S3/CloudFront and verify remote markers.

## Boundaries

- Do not touch unrelated dirty files such as `sites/travel/dist/travel-data.json`.
- No Terraform/new AWS resource unless separately approved.
- No force-push.
- No secrets or credential changes.
