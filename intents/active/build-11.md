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

## Current Progress (updated 2026-06-16T12:00Z)

**Prepare phase complete.**

- 3D CSS scene 설계 완료: moving perspective grid + glowing orbs + horizon fade
- Top floating nav rail: glass backdrop, overall status pill, UTC clock
- Bottom HUD grid: status.json surfaces + agent_lane 자동 파싱, compact dot+name tiles
- Right side drawer: live_checks, icon(●/◐/○)+name, mobile 숨김
- 초안 저장: `artifacts/build-11/status-page-draft.html`
- 리포트: `reports/build-11/2026-06-16T1200Z-prepare.html`

**다음 단계 (execute_local 필요):**
1. `sites/status/dist/index.html`을 draft로 교체
2. 브라우저에서 desktop + mobile 스크린샷 확인
3. `python3 scripts/build-status-json.py --resolve-aws --check` 실행
4. 커밋 + S3/CloudFront 배포
5. `https://status.aws.shdkej.com` 원격 확인 후 완료 처리

## Implementation Notes

- 인터넷/레퍼런스 확인은 `3D hero background`, `floating glassmorphism navigation`, `HUD overlay dashboard`, `web 3D background CSS/Three.js` 중심으로 다시 본다.
- 정적 Status 페이지라면 새 3D-like raster background 생성 또는 lightweight Three.js scene 중 하나를 선택한다.
- Three.js를 쓰면 모바일/데스크톱 canvas nonblank 검증이 필수다.
- raster background를 쓰면 `assets/`에 3D full-image를 두고, UI는 absolute/fixed overlay로 얹는다.
- `status.json` feed 구조는 유지하되 표시 계층을 메뉴형으로 바꾼다.
- **현재 draft는 순수 CSS 3D (Three.js 없음) — 가볍고 정적 S3 배포에 바로 사용 가능.**
- 실제 3D 이미지 에셋(bg.jpg)이 있으면 `.bg-scene` background-image로 교체해 더 강한 3D 연출 가능.

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
