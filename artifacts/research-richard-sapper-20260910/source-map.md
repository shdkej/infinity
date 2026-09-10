# 리차드 샤퍼 T1.1 — 출처·저작 범위 원장

- leaf: `T1.1 공식·기관 자료로 생애·대표작·기여 범위 수집`
- accessed_at: `2026-09-10T14:14:09Z`
- source policy: 공식 제조사·박물관·기관 기록만 확정 사실의 근거로 사용했습니다. 검색 요약과 개인/유산 사이트는 발견 단서이며, 이 원장의 확정 사실 근거가 아닙니다.
- boundary: 현대 제품·인터페이스에 대한 직접 영향이나 성능 효과는 이 leaf에서 주장하지 않습니다. 이는 T3에서 별도 해석/한계로 다룹니다.

## 확정 가능한 주장

| ID | 원자적 주장 | 직접 출처 | 출처 등급·접근 상태 | 기여/연도 경계 | 신뢰도 |
| --- | --- | --- | --- | --- | --- |
| SAP-001 | Richard Sapper는 1932년 뮌헨 출생이다. Vitra Design Museum의 연표는 그가 Marco Zanuso와 1958–1977년 작업했다고 표기한다. | [Vitra Design Museum — Richard Sapper](https://www.design-museum.de/en/about-design/biographies-of-designers/richard-sapper.html) | 기관 전기 · HTTP 200 확인 | MoMA 기관 자료는 협업을 1959–1978로 다르게 표기한다. 따라서 협업 기간은 단일 확정 연도로 사용하지 않으며, 이 기간의 결과물을 샤퍼 단독 저작으로 만들지 않는다. | 높음(출생) / 상충(기간) |
| SAP-002 | MoMA의 Tizio Table Lamp 기록은 Richard Sapper를 저자로, 작품 연도를 1971로 표기한다. | [MoMA — Tizio Table Lamp](https://www.moma.org/collection/works/2599) | 박물관 소장 기록 · 브라우저 원문 확인 | MoMA 원문은 1972년을 **첫 생산** 시점으로 설명합니다. 따라서 본 원장은 `1971 (소장기록) / 1972 (첫 생산)`으로 보존하며 단일 ‘설계 연도’로 환원하지 않습니다. | 높음 |
| SAP-003 | MoMA는 Tizio가 균형추로 네 방향 이동하고, 베이스의 변압기에서 팔을 통해 전류를 공급받는다고 설명한다. | [MoMA — Tizio Table Lamp](https://www.moma.org/collection/works/2599) | 박물관의 작품 설명 · 브라우저 원문 확인 | ‘혁명적’·시장 성공 같은 평가 문구는 이 기술 주장에 포함하지 않습니다. | 높음 |
| SAP-004 | MoMA의 TS 502 라디오 기록은 Marco Zanuso와 Richard Sapper를 공동 저자로, 1963년작·제조사 Brionvega로 표기한다. | [MoMA — Radio (model TS 502)](https://www.moma.org/collection/works/4034) | 박물관 소장 기록 · 브라우저 원문 확인 | 반드시 `Zanuso와 Sapper의 공동 설계`로 표기합니다. Sapper 단독 작품으로 쓰지 않습니다. | 높음 |
| SAP-005 | Lenovo는 최초 ThinkPad 700C가 Richard Sapper의 디자인 및 일본 Yamato Labs의 엔지니어링으로 1992-10-05 발표됐다고 기록한다. | [Lenovo — Happy 25th Birthday ThinkPad!](https://news.lenovo.com/pressroom/press-releases/happy-25th-birthday-thinkpad/) | 제조사 공식 보도자료 · HTTP 200/브라우저 원문 확인 | `designed by`와 `engineered in`을 분리합니다. Sapper가 ThinkPad를 단독 발명/개발했다는 주장은 뒷받침하지 않습니다. | 높음 |

## 확인 보류와 충돌 기록

| 항목 | 관측 | 처리 |
| --- | --- | --- |
| Tizio 연도 | Vitra Design Museum 연표는 제품명을 `Tizia`, 연도를 1970으로 표기하지만 MoMA는 `Tizio Table Lamp. 1971`, Artemide는 1972년 생산 개시를 기록한다. | Vitra의 `Tizia/1970` 표기는 MoMA·Artemide 기록과 상충하며 확인 불가로 남긴다. 본문의 확정 서술은 MoMA의 `1971 (소장기록) / 1972 (첫 생산)` 구분만 사용한다. |
| ADI 평생공로상 페이지 | ADI URL은 HTTP 200이었지만 이번 자동 브라우저 수집에서는 본문을 안정적으로 읽지 못했습니다. | 발견 단서로만 남기고, 이 leaf의 확정 근거에는 사용하지 않습니다. |
| 현대 제품/인터페이스 적용 | 지금 수집한 출처는 오늘날 UI에 대한 직접 계보·효과를 증명하지 않습니다. | T3에서 `해석/적용 가설`로 분리하기 전까지 주장하지 않습니다. |

## 재현 메모

- 링크 상태 확인: Design Museum Germany·Lenovo는 `HTTP 200`; MoMA는 일반 `curl`에서 403이지만 브라우저 수집으로 소장기록 본문을 직접 확인했습니다.
- 저작권 보호를 위해 원문 전문·이미지·스크린샷은 저장하지 않았습니다. URL, 접근 시각, 필요한 최소 요약만 보존합니다.
- 다음 leaf `T1.2`는 각 주장에 대한 교차 검증과 위 보류 항목의 수용/제외 결정을 수행합니다.
