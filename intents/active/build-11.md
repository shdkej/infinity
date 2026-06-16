# build-11: Status 3D Full-Image Floating Menu Redesign

- id: build-11
- status: in_progress
- projects: [infinity, personal-ops, infrastructure]
- task_type: implementation
- topics: [status, dashboard, ui, 3d-background, floating-menu]
- owner: Infinity
- display_name: Status 3D Full-Image Floating Menu Redesign
- created_at: 2026-06-16T11:30Z
- updated_at: 2026-06-16T12:30Z
- source: user correction after build-10 — "음 이 느낌이 아니야"
- predecessor: build-10
- target_repo: `/home/ubuntu/workspace/space/infra-aws-static-sites`
- target_surface: `https://status.aws.shdkej.com`
- target_files:
  - `sites/status/dist/index.html`
  - `sites/status/dist/assets/bg-3d.jpg` ← 신규 필요
  - `sites/status/dist/status.json`

## Current State (2026-06-16T12:30Z)

**Prepare 완료.** Cloud Heartbeat가 3D full-bleed background + floating HUD/nav 구조로 index-draft.html 초안 작성 완료.

- 초안: `artifacts/build-11/index-draft.html`
- 리포트: `reports/build-11/2026-06-16T1230Z-prepare.html`

**다음 단계 (execute_local)**: 로컬 Claude Code에서 아래를 순서대로 실행.

1. `artifacts/build-11/index-draft.html` → `sites/status/dist/index.html` 복사
2. 3D 배경 이미지 `sites/status/dist/assets/bg-3d.jpg` 생성/배치
   - 권장: AI 이미지 생성 (dark space, 3D abstract, depth) 또는 CC0 3D render
   - 최소 1920×1080, jpg/webp
3. `python3 scripts/build-status-json.py --resolve-aws --check` 로 status.json 최신화
4. Chromium screenshot — desktop 1440×1100, mobile 390×1200
   - 3D 이미지가 fullscreen 채우는지 확인
   - floating rail/HUD/cluster가 이미지 위에 overlay 되는지 확인
5. S3/CloudFront 배포 및 `https://status.aws.shdkej.com` 원격 확인
6. 결과 리포트: `reports/build-11/{timestamp}-deploy.html`
7. 이 파일의 status를 `completed`로 업데이트

## User Feedback (원본)

마스터가 `build-10` 결과에 대해 방향이 다르다고 피드백했다.

핵심 수정:

- 전체적인 메뉴 배치도 바뀌어야 한다.
- 포인트는 **3D 풀 이미지가 백그라운드에 있는 것**이다.
- 메뉴/상태 정보는 그 위에 **살짝 떠 있는 정도**여야 한다.
- 현재 build-10처럼 glass card와 hero copy가 전면에 오는 구성이 아니다.

## Design Direction (Cloud Prepare 산출물)

### 구조

```
[FULL VIEWPORT = 3D 배경 이미지/씬]
  ↑ z:100  nav-rail   — 상단 fixed 48px glass strip (브랜드 + 상태 chips)
  ↑ z:50   hud-pill   — center floating badge (Overall status + timestamp)
  ↑ z:50   cluster    — 하단 3-column glass tiles (Checks / Surfaces / Agents)
```

### CSS 핵심

- 배경: `url('assets/bg-3d.jpg') center/cover no-repeat fixed` + aurora gradient CSS fallback
- Glass: `backdrop-filter: blur(20px) saturate(1.5)` + `rgba(255,255,255,0.06)` bg
- Live dot: `animation: blink 2.4s ease-in-out infinite` (green glow)
- 3-column grid: `repeat(3,1fr)`, mobile → 1fr stack

### status.json 매핑

| json 필드 | 표시 위치 |
|-----------|----------|
| `issues[]` (active) | HUD pill 색상 + 라벨 |
| `checked_at` | HUD timestamp |
| `summary{}` | Rail chips |
| `checks[]` | 하단 Live Checks tile |
| `surfaces[]` | 하단 Surfaces tile |
| `agents[]` | 하단 Agent Lane tile |

## Boundaries

- Do not touch unrelated dirty files such as `sites/travel/dist/travel-data.json`.
- No Terraform/new AWS resource unless separately approved.
- No force-push.
- No secrets or credential changes.
