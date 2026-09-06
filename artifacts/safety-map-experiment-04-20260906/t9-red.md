# T9.2 Red — 공통 데이터 계약

- 판정 시각: 2026-09-06T13:32:00Z
- 판정: **PASS — 공통 데이터 계약에 한함**

## 확인

- official/community source_class가 명시적으로 분리되어 있다.
- access_decision·review_state·eligibility_state는 출처 간 추론·전이가 금지된다.
- 원문·댓글·작성자·이미지·정확 주소/좌표·텔레메트리·단일 게시물 핀을 금지한다.
- 기본값은 no-render이며 적격 상태도 hold_no_render 또는 reject만 허용한다.
- 계약은 렌더·집계·핀 권한을 만들지 않고, 이후 별도 집계·표현·provenance·독립 Red 게이트를 요구한다.

필수 수정 없음.
