# 공개 인수 후보 재조사 r3

## 결론 (정정: 2026-10-12 live Notion verification)

이 보고서의 기존 `기준선 16행 → 21행`, `Notion 신규 write 5건` 서술은 이전 대표/보류 lead 단계의 잔존 기록이며, 이후 full-pagination write 결과와 충돌한다. 실제 Notion API를 다시 pagination query한 현재 상태는 **382행**이다: 기존/legacy 21행과 full-pagination 표식이 있는 신규 **361행**(Fello 69, Sellernet 59, Flippa 114, Empire Flippers 29, Quiet Light 90)이다. 이전 5건 축약은 잘못된 중간 결과였으며 완료 주장에 사용하지 않는다.

신규 361행은 모두 live query에 존재하고 source URL도 361/361 채워져 있다. 다만 source URL 고유값은 351개이며 list-root URL을 공유하는 10개 중복 행이 확인되어, “URL 기준 완전 중복 제거” 주장은 철회한다. Empire Flippers listing ID는 29행/29개 고유다. 독립적인 361-item 원본 manifest가 저장소에 없어 raw-pagination과 DB 행의 일대일 완전성까지는 입증하지 않는다. 상세 증적은 [`work/notion-live-verification-20261012.md`](../work/notion-live-verification-20261012.md)다.

## 결론 (이전 대표 샘플 서술)

실제 site-specific pagination adapter로 Fello·Sellernet·Flippa·Empire Flippers를 page 1→2→3에 해당하는 실제 endpoint까지 읽었고, Quiet Light·Listing의 공개 접근 한계도 확인했습니다. 기존 Notion 16행과 중복되지 않으면서 **직접 상세 링크·3천만원 이하 가격·핵심 재무 신호·운영 부담/이전 범위**를 모두 공개 원문에서 확인한 신규 승격 후보는 **0건**입니다. 이 문단은 full-pagination write 전의 대표/보류 lead 판단을 설명하는 역사적 기록이며, 현재 DB 행수의 근거가 아닙니다.

## 판정 요약

| 구분 | 수 |
|---|---:|
| 신규 승격 | 0 |
| 보류 | 5 |
| 차단/endpoint 부재 | 1 |
| Notion 신규 write | 5 (보류 lead) |

보류는 Fello·Sellernet·Flippa·Empire Flippers·Quiet Light의 source-level lead입니다. 가격 초과, 직접 상세/운영·이전 범위 공백, 또는 반복 pagination 때문에 승격하지 않았습니다. Listing은 공개 pagination endpoint가 없어 차단으로 기록했습니다. Quiet Light는 403 우회를 하지 않았고 이번 요청에서는 200이었지만 page 2가 page 1을 반복해 pagination 실패입니다.

## 실제 페이지 경로와 증거

상세 page별 URL·HTTP 방법·status·response SHA-256 prefix·item fingerprints·next URL/token·duplicate rate는 [`work/pagination-smoke.md`](../work/pagination-smoke.md)에 보존했습니다. 핵심 경로는 Fello API `page=0..2&size=24`, Sellernet `/products?page=1..3`, Flippa 필터 유지 `pagination=true&page=1..3`, Empire Flippers WordPress AJAX `listing_fetch&page=1..3` POST입니다. Empire `/page/N/` fallback은 사용하지 않았습니다.

## 역할 판단

- Planner: r2의 16행을 기준선으로 고정하고 중복 없는 신규 승격만 허용했다.
- Developer: adapter commit `a3465333eff3a939d3d43c7a4456e4e6aa65832b`와 실제 page fingerprint 전이를 확인했다.
- Marketer: 공개 주장과 확정 후보를 분리해 0건을 추천처럼 포장하지 않았다.
- Operator: 이 문서가 처음 작성될 때의 대표 단계에서는 5건 create를 실행·검증했다. 이후 full-pagination write의 live 결과는 위 정정 섹션과 `work/notion-live-verification-20261012.md`가 정본이며, schema/권한/스케줄 및 외부 연락·구매는 변경하지 않았다.

## r3 후속 정책 보정 및 Notion 기록

승격 후보는 0건으로 유지한다. 아래 5개 lead 기록은 full-pagination write 이전의 역사적 단계다. 당시에는 기존 스키마를 유지하고 `신규 검토` 상태와 플랫폼 설명의 `검증 필요`/`보류` 표기로 5개 lead를 추가했으며, 기준선 16행에서 21행으로 보였다. 이후 현재 live DB는 382행으로 정정되었고, URL 중복 caveat 및 스키마 검증은 [`work/notion-live-verification-20261012.md`](../work/notion-live-verification-20261012.md)에 기록했다. 각 역사적 lead의 상세는 [`work/notion-held-leads-update.md`](../work/notion-held-leads-update.md)에 남아 있다.

- 검증 필요: KnowYourHue, Doctor veterinarian
- 보류: Sellernet 건강식품, Empire Flippers #97751, Quiet Light #18829636
- Listing: 공개 pagination endpoint 부재로 Notion 후보에서 제외

## 다음 판단

다음 실행은 신규 상세 URL에서 가격·재무·운영/이전 증거가 동시에 공개되면 승격하고, 그렇지 않더라도 중복 없는 발견 lead는 `신규 검토`로 기록합니다.
