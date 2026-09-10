# Red 검증 — Waiting/provenance 범위

- 검수 시각: 2026-09-10T23:16:00Z
- verdict: **PASS (Waiting 전환)**
- 범위: 렌더 승인 검수가 아니라 실제 인물 초상 사진의 provenance 하드 게이트와 Waiting 기록만 검수했다.

## 직접 확인한 파일

- `INTENTS.md`
- `traces/content-minimal-collector-richard-sapper-short-20260910.json`
- `artifacts/content-minimal-collector-richard-sapper-short-20260910/photo-provenance-gate.md`
- `artifacts/content-minimal-collector-richard-sapper-short-20260910/task-plan.md`
- `reports/content-minimal-collector-richard-sapper-short-20260910/20260910T2314Z-waiting.html`

## 검증

1. `python3 -m json.tool traces/content-minimal-collector-richard-sapper-short-20260910.json` 통과.
2. `python3 scripts/check_intents_consistency.py` 통과.
3. `git diff --check` 통과.
4. intent-scoped 1080×1920 원본 PNG/JPEG/WebP와 390px preview가 존재하지 않음을 확인했다.
5. provenance 원장은 실제로 연 후보·명시 이용조건 부재·재개 대안을 기록한다.
6. 공개 게시·업로드·계정 변경·생성 인물 대체가 모두 없고, Slack `channel:C0BR41W31MM` / `replyTo:1789072321.275899` metadata가 보존된다.

## 한계와 재개 조건

이 PASS는 렌더 승인이 아니다. 실제 인물 사진의 원본 URL, 명시된 재사용 조건, 귀속/편집 조건이 재현 가능하게 제공되면 provenance 게이트를 새로 통과한 뒤에만 원본·390px preview를 만들고 별도의 실제 렌더 Red 검수를 받아야 한다.
