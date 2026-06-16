# Status Hers-Inspired Operations Glass Redesign

Status 페이지를 Behance Hers 레퍼런스의 밝은 헬스케어 SaaS 감각으로 재구성했다.

## Applied

- 실제 배경 이미지 레이어를 추가하고 그 위에 `backdrop-filter: blur(...) saturate(...)` glass cards를 배치.
- 상단 hero를 `Space Status / operations glass` 브랜드 pill, 큰 serif headline, system health card로 변경.
- 기존 운영 데이터는 `status.json` feed를 그대로 사용.
- Live Checks, Surfaces, Agent Lane은 낮은 밀도의 반복 확인용 glass panels로 유지.
- 모바일 390px에서 headline과 score summary overflow를 보정.

## Sources

- Behance: Hers Healthcare App & Branding.
- MDN: `backdrop-filter` requires transparency so the element can show filtered pixels behind it.
- Josh Comeau: frosted glass quality depends on the relationship between background content and the glass surface.

## Verification

- `python3 scripts/build-status-json.py --resolve-aws --check`
- Chromium screenshot check: desktop 1440x1100, mobile 390x1200.
