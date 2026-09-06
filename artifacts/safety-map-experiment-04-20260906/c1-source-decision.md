# T1 · 로마 공식 공개 안전/범죄 데이터 후보 판정

- Intent: `safety-map-experiment-04-20260906`
- Cycle: `C1 / T1`
- 실행 시각: 2026-09-06T09:04:45Z 이후, 30분 한도 내
- 판정: **blocked — 지도 표시 데이터로 채택하지 않음**

## 계획

공식 기관 원문에서 후보 하나에 대해 기관성, 로마 관할 범위, 라이선스, 관측·발행·갱신일을 모두 확인한다. 하나라도 현재성 또는 주장 한계에 맞지 않으면 안전 점수·예측·안전 경로·실시간 사건·개인 위치 수집 없이 T1에서 멈춘다.

## 조사 결과: 후보 1건

| 항목 | 확인값 | 판정 근거 |
| --- | --- | --- |
| 후보 | `d108` — *Incidenti stradali nel territorio di Roma Capitale - Anno 2022* | [Roma Capitale Open Data CKAN API](https://dati.comune.roma.it/catalog/api/3/action/package_search?fq=groups%3Asicurezza-urbana&rows=20) 응답의 dataset `d108` |
| 기관 원문 | Roma Capitale Open Data, 조직: `Roma Capitale - AREA TEMATICA: SUPPORTO ALL'AMMINISTRAZIONE` | 동일 CKAN 메타데이터의 `organization.title` |
| 관할 범위 | `territorio di Roma Capitale` | 원문 설명은 Roma Capitale 시 영역에서 지방경찰(Polizia Locale) 순찰이 개입한 사고만 포함한다고 명시 |
| 관측 범위·결측 | 2022년 1–8월의 도로교통사고; **8월이 마지막 가용 월**. 당사자 합의 사고와 Roma Capitale 내 Grande Raccordo Anulare 사고는 제외 | 원문 `notes`의 “Ultimo mese disponibile Agosto”, 제외 조건 |
| 발행일 | dataset metadata 생성 `2022-08-30T08:25:34.539168Z` | CKAN `metadata_created` |
| 갱신일 | dataset metadata 변경 `2023-05-12T07:15:49.032506Z` | CKAN `metadata_modified` |
| 라이선스 | Creative Commons Attribution-ShareAlike (`CC BY-SA`), 메타데이터 URL: `http://www.opendefinition.org/licenses/cc-by-sa` | CKAN `license_title`, `license_url`; [Roma Capitale 라이선스 안내](https://dati.comune.roma.it/od/it/legal.page)는 개별 자원의 메타데이터 라이선스가 적용된다고 명시 |

## 판정과 이유

**차단**합니다. 후보는 공식 시 데이터이고 Roma Capitale 관할·라이선스·관측/발행/갱신일을 확인할 수 있으나, 범위는 범죄가 아니라 도로교통사고이며 마지막 관측이 2022년 8월, 메타데이터 마지막 변경이 2023-05-12입니다. 또한 기관 원문이 정보시스템 유지보수 때문에 갱신을 일시 중단했다고 명시합니다.

따라서 이 후보를 2026년의 범죄·위험·안전 상태 또는 장소별 안전 판단으로 표현할 수 없습니다. 이 T1에서는 데이터를 내려받거나 지도에 넣지 않았고, 위험 점수·예측·안전 경로·실시간 사건·개인 위치 수집을 만들지 않았습니다.

## 역할 관점 및 Red 마감 확인

- **Planner:** T1 완료 기준(기관성·범위·라이선스·날짜)은 충족했지만, 현재성/의미 범위가 제품의 치안 주장과 맞지 않아 다음 구현을 열지 않습니다.
- **Developer:** 외부 데이터 호출·다운로드·UI 변경을 하지 않았습니다. 후속은 갱신된 공식 범죄 또는 공공안전 원문이 확인될 때 별도 데이터 계약으로만 시작합니다.
- **Marketer:** “안전 지도”나 “안전한 지역” 같은 약속을 만들지 않습니다. 이 후보는 역사적 교통사고 기록으로도 현재 위험을 암시하지 않도록 표시 대상에서 제외합니다.
- **Operator:** 재현 가능한 API URL·메타데이터 시각을 남겼습니다. 갱신 중단 및 누락 구간 때문에 자동 새로고침/운영 데이터 소스로 등록하지 않습니다.
- **Red:** 독립 Red 역할 세션 실행 도구가 이번 런타임에 노출되지 않아 **Red pass를 주장하지 않습니다**. 위 차단 결론은 Red 재검증 대기이며, 이 사유로 T1 상태는 `blocked`입니다.

## 마감 확인 및 다음 입력

- 30분 한도 내 후보 1건을 기관 원문으로 판정했습니다.
- T1 상태: `blocked`.
- T2/T3는 시작하지 않습니다.
- 재개 조건: Roma Capitale 또는 관할 국가기관의 **로마 시 범위** 공식 공개 범죄/공공안전 데이터가 (1) 명시 라이선스, (2) 관측 단위·누락, (3) 발행·갱신일, (4) 현재성 기준을 함께 제공할 때, 새 T1 재판정 후 진행합니다.

## 재현 명령

```sh
curl -fsSL 'https://dati.comune.roma.it/catalog/api/3/action/package_search?fq=groups%3Asicurezza-urbana&rows=20'
```

조회 시각은 실행 로그 기준 2026-09-06 UTC입니다. 원문 데이터와 포털 메타데이터는 이후 변경될 수 있습니다.
