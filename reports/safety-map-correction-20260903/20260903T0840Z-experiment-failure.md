# Safety Map 1차 실험 실패 분석

- 판정: failed / user-terminated
- 절대 마감: 2026-09-03T05:00:00Z
- 종료: 2026-09-03T08:40:40Z

## 관측된 실패

1. 최초 Intent는 fixture-only 화면을 실제 지도 MVP로 잘못 Archive했다.
2. 교정 Intent는 20:30 UTC 이후 실질 artifact·render·Red 결과 없이 dispatcher handoff만 반복했다.
3. `BRAND.md`·`DESIGN.md`·`DESIGN_SYSTEM.md`의 필수 읽기와 실제 화면 반영을 완료 gate로 연결하지 못했다.
4. Mapbox style HTTP 응답을 실제 인터랙티브 지도·도로/거리 UX 검증으로 잘못 대체했다.
5. 최초 Archive에서 notification metadata가 terminal notifier가 읽는 원장에 보존되지 않아 Slack 완료 알림이 발송되지 않았다.
6. deadline이 지나도 Active 상태가 유지되어 종료 보호가 hard-stop으로 작동하지 않았다.

## 원인

- **완료 증거 정의 오류:** HTTP 200·fixture 렌더를 핵심 제품 경험의 증거로 취급했다.
- **진행 증거 정의 오류:** dispatcher handoff를 실제 stage 완료로 취급해 stale Active를 재개하지 못했다.
- **컨텍스트 게이트 누락:** 디자인 정본 읽기·화면 반영·실제 렌더 검토가 Developer/Red exit criterion에 없었다.
- **terminal 계약 단절:** Inbox의 notification 필드가 Archive의 notifier 입력까지 보존되는 불변 계약이 아니었다.
- **마감 상태 모델 부재:** deadline은 안내문이었고, deadline 이후 자동 Waiting 전환·사후 실패 리포트가 없었다.

## 재개 전 필수 개선

1. `stage_evidence_at`가 새 artifact/test/render/commit 중 하나를 가리키지 않으면 handoff를 liveness로 인정하지 않는다.
2. deadline 이후 Active Intent는 자동 Waiting으로 전환하고 실패 리포트·다음 승인 조건을 남긴다.
3. 사용자-facing 디자인 작업은 BRAND → DESIGN → DESIGN_SYSTEM 읽기 증거, 구현 mapping, 390px/desktop screenshot, Red 직접 시각 판정을 모두 통과해야 한다.
4. 지도 제품은 실제 Mapbox canvas, zoom/pan, 위치·거리 맥락, 레이어 상호작용의 브라우저 검증 없이는 완료할 수 없다.
5. Archive용 terminal notifier 입력은 notification channel/target/reply metadata를 원 Intent에서 immutable하게 보존하며, Slack delivery receipt까지 검증한다.
6. 기능 완주는 `quality_iteration_active`일 뿐 Archive가 아니다. deadline 또는 명시 조기 종료만 terminal 전환 조건이다.

## 재개 조건

새 Intent에서 시간 예산·Mapbox protected configuration·브라우저 렌더 경로·실제 지도 UX 범위를 다시 잠그고, 위 여섯 개선을 먼저 구현·검증한 뒤에만 제품 교정을 재개한다.
