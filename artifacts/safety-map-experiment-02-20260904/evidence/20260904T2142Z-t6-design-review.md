# T6.1 디자인 품질 반복

- 확인 시각: `2026-09-04T21:42Z`
- 대상: `https://safety-map.aws.shdkej.com/`
- browser viewport: 1440×900 (관리형 Chromium)
- 캡처: `20260904T2142Z-t6-design-desktop.png` (tool-delivered raster 780×493)
- SHA-256: `4e68d7befa18b6269e408bda101a4264d02fd77f925b8b8c5c5b8ab793f6b890`

## 시각 검토

- `PLACE CONTEXT / ROME` eyebrow, 큰 제목, `현재 검증된 데이터 없음` 배지가 검색·지도보다 먼저 읽힌다.
- 장소 검색 입력과 야간 basemap이 실제 지도 영역에 붙어 있으며, 지도 맥락을 안전 등급·경로 추천으로 오인하게 하는 표현이 없다.
- 어두운 basemap 위 도로선과 지도 라벨은 읽히고, 밝은 패널·제목·입력 영역의 대비와 위계가 유지된다.
- 이번 반복에서는 변경이 필요한 시각 결함을 찾지 못했다. 안전 경계와 provenance 고지는 유지한다.

## 범위

이 문서는 desktop 디자인 반복의 evidence다. 모바일 접근성은 별도 T6.2에서 점검하며, terminal Slack·Archive는 수행하지 않는다.
