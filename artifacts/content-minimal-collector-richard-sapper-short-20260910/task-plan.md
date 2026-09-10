# 미니멀 모으기 1/100 — 리처드 사퍼 숏츠 첫 이미지 태스크 계획

## 범위

검증된 Richard Sapper 심층 리서치와 사용 조건을 확인할 수 있는 실제 인물 사진만 사용해, 사용자 레퍼런스의 세로형 타이포-초상 리듬을 재해석한 비공개 9:16 첫 이미지를 제작한다. 공개 게시·업로드·계정 조작은 범위에서 제외한다.

## 실행 leaf

1. **T1 — 사실·사진 provenance**: 리서치에서 사용할 수 있는 사실 한 문장과 실제 인물 사진 후보의 출처 URL·저작권/사용 조건을 기록한다. 조건을 확인할 수 없으면 이미지 제작을 Waiting으로 낮춘다.
2. **T2 — 첫 이미지 렌더**: 1080×1920 PNG로 상단 훅, 중앙 실제 사진, 하단 `미니멀 모으기 1/100`을 구성한다. 레퍼런스의 계정 UI·원문 카피·워터마크는 포함하지 않는다.
3. **T3 — 실제 렌더 검수**: Red가 원본 PNG와 390px 폭 프리뷰에서 훅 위계, 텍스트 충돌, 사진 provenance, 연구 사실 경계를 검사한다.

## 완료 기준

원본 PNG, 사진 출처/사용 조건 원장, 390px 프리뷰, 재현 정보와 Red PASS가 모두 있을 때만 비공개 결과로 보고한다. 이는 게시 허가가 아니다.

## 실행 기록 — T1.1 (2026-09-10T23:14:18Z)

- cycle_id: T1.1-photo-provenance
- cycle_goal: 실제 Richard Sapper 초상의 재사용 조건을 원문에서 재현 가능한지 확인한다.
- max_minutes: 30
- validation: 직접 연 후보 4건을 `photo-provenance-gate.md`에 기록했다. 초상·사용 조건이 함께 충족된 후보는 0건이다.
- closure_check: **Waiting**. T2/T3은 입력 사진의 권리 상태가 해결되기 전에는 시작하지 않는다.
- evidence: `artifacts/content-minimal-collector-richard-sapper-short-20260910/photo-provenance-gate.md`; `reports/content-minimal-collector-richard-sapper-short-20260910/20260910T2314Z-waiting.html`

## 실행 기록 — T1.2 (2026-09-10T23:19:00Z)

- cycle_id: T1.2-private-approval-sync
- cycle_goal: 사용자의 비공개 실제 인물 사진 시안 승인과 SAM의 별도 제작을 기록하고 중복 출력을 막는다.
- max_minutes: 30
- decision: Genie는 PNG·390px preview·새 사진 artifact를 만들지 않는다. SAM의 시안 인계 또는 사용자 피드백을 기다린다.
- boundary: 공개 게시·업로드는 금지이며, 공개·배포 전 사진 라이선스 확인 게이트는 유지한다. 기존 provenance Waiting 기록과 Red 범위는 역사 기록으로 보존한다.
- validation: intent-scoped render 파일을 추가하지 않고 trace만 Active 협업 상태로 동기화한다.
