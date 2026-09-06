# T8.1 — 공식 자료 병행 후보·메타데이터

- 수집 시각: 2026-09-06T12:52:00Z
- 목적: 공식 자료의 공개 provenance를 분리 확인한다. 위험 신호·안전 판단·지도 표시에는 사용하지 않는다.
- 결과: **모든 후보 `hold_no_render`**

## 후보

| ID | 공식 출처 URL | 공개 메타데이터 | 공간 단위 | 판정 |
| --- | --- | --- | --- | --- |
| O-01 | https://www.comune.roma.it/web/it/dettaglio.page?contentId=PAG1305954 | Roma Capitale Annuario statistico 2024에 `Sicurezza urbana` CSV가 목록화됨; 개별 표의 발행일·필드·공간 단위는 이 단계에서 미확인 | 미확인 | `hold_no_render` |
| O-02 | https://dati.comune.roma.it/catalog/dataset/4c042b38-ce18-4643-9b5f-7ef7bb574275/resource/02971256-8491-4d36-bc5f-97895f97a71f | Roma Capitale 2021 도로교통사고 CSV; 마지막 수정 2021-12-14, CC BY 4.0 메타데이터 관찰 | 레코드에 좌표·도로 필드가 존재하나 사용 금지 | `reject` |
| O-03 | https://www.comune.roma.it/web/it/open-data.page | Roma Capitale 공식 Open Data 포털; 도시 안전 주제를 포함한 공개 데이터 카탈로그와 출처 표기 재이용 조건을 안내 | 후보 자체 아님 | provenance 참조만 허용 |

## 경계

- O-01은 공식성만 확인됐으며, 최근성·정확한 지역 단위·필드·집계 적합성을 확인하기 전에는 표시할 수 없다.
- O-02는 오래된 교통사고 자료이고 정밀 위치 필드를 포함하므로 위험 회피 보조나 지도 핀에 사용하지 않는다.
- 이번 단계에서 데이터 파일·레코드·정확 좌표·개인식별 정보는 내려받거나 보존하지 않았다.
- 공식성은 안전 보장·범죄 사실 확정·현재 장소 위험 판단의 근거가 아니다. 이후 T8.2 독립 Red 전까지 `근거 없음`/no-render를 유지한다.
