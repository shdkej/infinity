# Pagination smoke — acquisition-cashcow-infinity-monitor-20261012-r3

확인 시각: 2026-10-12 UTC · adapter commit: `a3465333eff3a939d3d43c7a4456e4e6aa65832b`

| site | 실제 경로/방법 | page 1→2→3 | status / response SHA(앞 16자) | items | duplicate rate | 판정 |
|---|---|---|---|---:|---:|---|
| Fello | `prod-api.fello.io/api/v1/products?page=0..&size=24` GET | 0→1→2 | 200 / `0e3976bee0f4d6f0`, `64e9038ebb20dac2`, `79c9bc29c1fc8822` | 24/24/24 | 0/0/0 | 72개 fingerprint, 신규 승격 0, 보류 1 |
| Sellernet | `/products?page=N` GET | 1→2→3 | 200 / `cf7c4f32759ad666`, `925137f9a0f18ca8`, `e9c3c613b6cee41f` | 20/20/20 | 0/0/0 | 60개 fingerprint, 신규 0, 보류 1 |
| Flippa | filtered canonical `pagination=true&page=N` GET | 1→2→3 | 200 / `6463ea1046878646`, `78d7bf3cc72c6d1d`, `9dc7964ce45e2ef3` | 60/60/25 | 0/.1667/.4 | 필터 유지, 신규 0, 보류 1 |
| Empire Flippers | `admin-ajax.php?action=listing_fetch&page=N` POST | 1→2→3 | 200 / `8987cc12574f0945`, `592181a053ec2b7e`, `cefc9a1b285889d9` | 20/20/20 | 0/0/0 | 60개 fingerprint, 신규 0, 보류 1 |
| Quiet Light | `/listings/`, `/listings/page/2/` GET (우회 없음) | 1→2; page 2 반복 | 200 / `afd53015132d8052`, `9b22578f844e93fd` | 91/91 | 0/1 | 403은 이번 요청에서 관찰되지 않았으나 공개 pagination은 실패; 보류 1 |
| Listing | landing page GET | 미실행 | — | — | — | 공개 pagination endpoint 부재, 차단 1 |

각 page record는 adapter의 JSON 결과에 request URL, method(POST/GET), HTTP status, response SHA-256, item fingerprints, next URL/token, duplicate rate, item count/access status를 남겼다. 서로 다른 fingerprint가 실제로 나온 Fello/Sellernet/Flippa/Empire Flippers page만 읽은 것으로 계산했다. Empire의 `/page/N/`은 사용하지 않았다.

## 후보 판정

- **신규 승격 0건:** 3천만원 이하 가격·재무 신호·운영 부담·이전 범위·직접 상세 링크를 공개 원문에서 동시에 확인한 중복 없는 항목이 없었다.
- **보류 5건:** 각 source의 직접 상세 또는 가격/운영·이전 증거가 일부만 확인된 lead(Fello, Sellernet, Flippa, Empire Flippers, Quiet Light). 가격 초과 또는 핵심 운영 증거 공백은 보류 사유로 유지했다.
- **차단 1건:** Listing — 공개 listing/search pagination endpoint 부재. Quiet Light는 403 우회 없이 요청했으며 이번 smoke에서는 200이었으나 page 2가 page 1 반복되어 pagination 실패로 기록했다.

## 보류 lead 기록 보정

승격 0건과 lead capture를 분리했다. Listing을 제외한 Fello, Sellernet, Flippa, Empire Flippers, Quiet Light의 대표 보류 lead 5건은 직접 상세 URL·확인된 공개 신호·미확인 필드·보류 사유를 `work/notion-held-leads-update.md`에 기록하고 기존 스키마의 `신규 검토` 상태로 Notion에 추가했다. Notion은 16행에서 21행으로 검증됐다.
