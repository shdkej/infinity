# 카타니아 하루 캐러셀 — 사실·자산 감사

## 범위와 역할 수렴

- **Planner:** 6장의 리듬은 복잡함(1–2) → 정리됨(3–4) → 여백(5–6)입니다.
- **Developer:** 원본 사진 파일이 없으므로 사진 안전영역, 인물/위치 노출, EXIF 제거, 실제 crop을 검증할 수 없습니다.
- **Marketer:** 장소 소개·가격·교훈 대신 실제 하루에서 아쉬웠던 지점, 쉬었던 지점, 아낀 선택만 남깁니다. 형광색·스티커는 이 intent의 최소 흰색 오버레이 제약과 충돌하므로 채택하지 않습니다.
- **Operator:** private render only입니다. 원본 파일 부재 상태에서 생성 이미지나 stock 이미지로 대체하지 않고 Waiting으로 전이합니다.

## 확인 가능한 입력

| 카드 | 요구 사진 | 사진 설명(입력) | 사용할 수 있는 사용자 기록 |
| --- | --- | --- | --- |
| 1 | IMG_9028.jpg | 분수 | 카타니아 하루의 비용·휴식 기준을 여는 훅 |
| 2 | IMG_9035.jpg | 시장 생해산물 | 시장 생해산물을 덤탱이로 느꼈음; 점심 디저트 서비스가 아쉬웠음 |
| 3 | IMG_9049.jpg | 벨리니 공원 | 벨리니 공원에서 잘 쉬었음 |
| 4 | IMG_9067.jpg | 음료·종이봉투 | 자판기 음료를 덤탱이로 느꼈음 |
| 5 | IMG_9069.jpg | 서점 | 버스 티켓을 확인·구매해 절약 경험이 있었음. 사진과 티켓 사건의 직접 관계는 주장하지 않음 |
| 6 | IMG_9075.jpg | 저녁 식사 | 저녁 3코스가 만족스러웠음 |

## 고정 카피 방향

1. `카타니아 하루, / 돈을 쓸 때와 쉴 때를 나눠봤다`
2. `시장 생해산물은 / 덤탱이로 느꼈다`
3. `벨리니 공원에서는 / 잘 쉬었다`
4. `자판기 음료도 / 같은 기준으로 남았다`
5. `버스 티켓은 / 확인하고 사서 아꼈다`
6. `저녁 3코스는 / 만족스러웠다`

점심 디저트 서비스의 아쉬움은 카드 2의 작은 보조 기록으로만 사용할 수 있습니다. 가격·통화·상호·정확한 시간/위치·동행인 감정·장소 추천·원인 추정은 사용하지 않습니다.

## 자산 감사 결과

2026-09-08T22:18:00Z에 `/home/ubuntu/workspace`, `/home/ubuntu/.openclaw`, `/mnt`, `/tmp`와 `/home/ubuntu`를 대상으로 여섯 정확한 파일명을 검색했습니다. 원본 파일 또는 접근 가능한 첨부 경로는 발견되지 않았습니다.

따라서 다음 검증을 수행하지 않았습니다.

- 실제 사진 기반 1080×1350 crop·render
- 얼굴, 번호판, 영수증, timestamp, 정확한 장소 단서의 노출 검토
- 실제 사진에서 텍스트 안전영역·대비 검토
- EXIF 제거 export

## 재개 계약

여섯 원본을 다시 첨부하거나 접근 가능한 경로로 제공하면 각 이미지를 한 번씩만 사용해 1080×1350 private PNG/JPG로 렌더합니다. crop/resize 외 생성 fill이나 사실을 더하는 편집을 하지 않으며, 최소 흰색 텍스트 오버레이·안전 여백·EXIF 제거를 적용합니다.

## 근거

- `INTENTS.md` — canonical user record와 사진 매핑
- `intents/context/content-catania-day-carousel-20260908.json` — Context Pack
- `source/openclaw-system/docs/INSTAGRAM_CAROUSEL_PROMPT_SYSTEM.md` — 4:5, 사실성, 공개 안전 규칙
- `source/openclaw-system/docs/WORLD_TRAVEL_PROJECT.md` — 여행 관찰을 장소 소개보다 기준으로 편집하는 원칙
- `/home/ubuntu/workspace/prompt-archive/TASTE.md`, `Threads.md`, `Content_Strategy.md`, `BRAND.md`, `DESIGN.md`, `DESIGN_SYSTEM.md` — 담백한 기록, 최소 편집, 과장 금지
