# build-17 Marketer

- 판단: 모바일 첫인상은 preview가 바로 보이고, 제목·상태·작업 surface가 viewport 밖으로 밀리지 않아야 한다. preview 선배치가 이 목표에 부합한다.
- 우려: 390px 캡처에서 canvas 내부 제목이 좌우 끝에 닿아 읽기 여백이 좁다. 이는 사용자의 직접 요청인 CSS 미적용/페이지 가로 overflow 해결 이후의 콘텐츠 안전영역 개선 과제다.
- 제안: 후속 작업에서 canvas 텍스트 자동 축소 또는 안전 폭(max line width)을 별도 intent로 검토한다. 이번에는 문구·브랜드 카피를 변경하지 않는다.
- 인계: Operator와 Red는 실제 화면에서 주요 조작 영역과 preview가 함께 접근 가능한지 확인한다.
