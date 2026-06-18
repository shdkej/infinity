# 로컬 Claude Code 실행 프롬프트 — build-12

아래 내용을 로컬 Claude Code에 그대로 전달하세요.

---

**Infinity Intent: build-12 Status 3D Character Background Prototype**
Mode: execute_local
Invocation: Prefer the existing pt/purplemux Claude pane via `tmux -L purple`; capture first, clear stale input, send this bounded prompt once, then capture the result. Fall back to a fresh bounded Claude Code call only if no usable pt pane exists.
Workflow: Single-page HTML/CSS/JS modification. Direct execution acceptable.

**Target repo:** `/home/ubuntu/workspace/space/infra-aws-static-sites`
**Target surface:** `https://status.aws.shdkej.com`
**Target files:**
- `sites/status/dist/index.html` — 패치 대상
- `sites/status/dist/assets/spatial-presence.css` — 신규 생성
- `DESIGN.md` — `## Spatial Presence Layer` 섹션 추가
- `DESIGN_SYSTEM.md` — `SpatialPresence` 패턴 + CSS 토큰 추가

**Goal:** Status 페이지에 Option D(pre-rendered + CSS pointer parallax) 배경 레이어를 구현한다.
Cloud prepare(shdkej/infinity artifacts/build-12/)에 모든 구현 파일이 준비되어 있다.

**Prepared files (shdkej/infinity 레포에 있음):**
- `artifacts/build-12/spatial-presence.css` — CSS 전체 구현체 (토큰·스테이지·parallax·mobile·reduced-motion)
- `artifacts/build-12/index-html-patch.md` — HTML 패치 가이드 (각 Step에 코드블록 포함)

**Allowed:** L0/L1 actions only
**Forbidden:**
- `sites/travel/` 등 관련 없는 파일 수정
- Terraform, AWS resource creation
- force-push, credentials/secrets 변경

---

**Steps:**

1. `infra-aws-static-sites/sites/status/dist/index.html` 현재 구조 파악
   - 기존 HUD 카드 래퍼 클래스명 확인 (z-index 설정 여부)
   - `<body>` 첫 태그 위치 확인

2. `shdkej/infinity:artifacts/build-12/spatial-presence.css`의 내용을
   `sites/status/dist/assets/spatial-presence.css`로 저장
   (`assets/` 디렉토리가 없으면 생성)

3. `index.html` `<head>`에 CSS 링크 추가:
   ```html
   <link rel="stylesheet" href="assets/spatial-presence.css">
   ```

4. `<body>` 시작 직후에 `.character-stage` div 추가
   (`index-html-patch.md` Step 2 코드블록 그대로 사용)

5. 기존 HUD 카드 래퍼에 `hud-layer` 클래스 추가
   (또는 기존 z-index가 이미 10 이상이면 클래스 없이 확인만)

6. `</body>` 직전에 parallax JS 추가
   (`index-html-patch.md` Step 4 코드블록 그대로 사용)

7. `DESIGN.md`에 `## Spatial Presence Layer` 섹션 추가
   (`index-html-patch.md` Step 6 내용 사용)

8. `DESIGN_SYSTEM.md`에 `SpatialPresence` 패턴 + CSS 토큰 추가
   (`index-html-patch.md` Step 7 내용 사용)

9. 빌드 스크립트가 있으면 실행:
   ```bash
   python3 scripts/build-status-json.py --resolve-aws --check
   ```

10. 로컬 브라우저에서 검증 게이트 모두 확인

---

**Verification gates (모두 통과해야 완료):**
- [ ] 배경 레이어 표시 (placeholder gradient 또는 캐릭터 이미지)
- [ ] HUD 카드가 배경 위에 정상 표시 (z-index 충돌 없음)
- [ ] 마우스 이동 시 CSS parallax 동작 (배경이 ±8° 범위에서 반응)
- [ ] OS 접근성 "애니메이션 줄이기" ON → parallax 정지, static만 표시
- [ ] 390px viewport 가로 스크롤 없음
- [ ] `DESIGN.md`에 `## Spatial Presence Layer` 섹션 존재
- [ ] `DESIGN_SYSTEM.md`에 `SpatialPresence` 패턴 존재

---

**After all gates pass:**

1. `infra-aws-static-sites` 레포에 커밋 & 푸시
2. S3/CloudFront 배포 (빌드/배포 스크립트가 있으면 실행)
3. `shdkej/infinity`에 다음 업데이트:
   - `reports/build-12/{actual_timestamp}Z.html` — HTML report 작성 (ARTIFACT_RULES.md 준수, 결론 2축 필수)
   - `intents/active/build-12.md` — 모든 success criteria 체크 완료, status: waiting → 완료 기록
   - `INTENTS.md` — Waiting 섹션에서 제거, Archive 코멘트 추가:
     `<!-- build-12 completed {timestamp} → intents/archive/build-12.md [projects: personal-ops,infinity,design-system; type: implementation; topics: 3d-background,interactive-character,skill] (Option D pre-rendered+CSS parallax 구현 완료. 배경 레이어·HUD·parallax·reduced-motion·DESIGN.md·DESIGN_SYSTEM.md 반영.) -->`
   - `intents/archive/build-12.md` — 완료된 Intent 원장 생성
