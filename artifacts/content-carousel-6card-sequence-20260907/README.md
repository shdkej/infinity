# Instagram 6장 기록형 시퀀스 — 비공개 렌더 시안

## 범위

`content-carousel-6card-sequence-20260907`의 실제 렌더 시안입니다. 모든 카드는 1080×1350(4:5) 단일 PNG이며, 공개 게시·업로드·계정 변경은 수행하지 않았습니다.

## 시퀀스

| 카드 | 리듬 | 역할 |
|---|---|---|
| 1–2 | dense | 메모·기록 조각이 많은 시작 |
| 3–4 | organized | 한 문장으로 정리, 4번은 거의 검정 서사 전환 |
| 5–6 | spacious | 여백을 넓혀 판단과 질문만 남김 |

## 고정값

- 1080×1350, 좌우 84px·하단 110px 안전 여백
- 사진 카드: 좌하단 흰색 제목/본문, 검정 35%·2px blur 그림자
- 카드 4: `#121212` 배경과 중앙 정렬 서사
- 저채도·무지점·무인물의 합성 기록 fixture만 사용

## 재현

```bash
python3 generate_assets.py
python3 render_assets.py
```

렌더러는 로컬 Chromium입니다. Snap Chromium의 `/tmp` 접근 제약 때문에 SVG를 `/home/ubuntu/carousel-render.O5mG3A/`의 일시 scratch로 복사해 렌더한 뒤 결과 PNG만 이 artifact 경로에 저장합니다.

## 안전 경계

- 여행 장소·숙소·사람·플랫폼·안전 정보·수치·성과를 주장하지 않습니다.
- 이 카피는 시각 시스템 검증용 `layout-only` 문구이며 공개용 콘텐츠 근거가 아닙니다.
- `public_posted`, `external_uploaded`, `profile_changed`는 모두 `false`입니다.
