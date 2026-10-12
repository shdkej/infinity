# r3 후속 — 보류 lead Notion 기록

확인 시각: 2026-10-12 UTC  ·  정책: 승격 여부와 별개로 공개 원문에서 발견한 lead를 `신규 검토` 상태로 기록하고, `플랫폼` rich-text에 `검증 필요`/`보류`와 사유를 표시한다.

## Notion 검증

- DB: `3f517bf7-599f-8176-8e1a-cddf002cf70b`
- 기존 행: 16
- 신규 생성: 5
- 생성 후 총 행: 21
- 생성된 행의 기존 스키마: 9개 필드 유지
- 기존 16행: 유지 확인(기존 page ID·제목·출처 불변; 신규 5개는 2026-10-12 생성)
- 신규 write: 5회 성공, update/delete/schema/권한/스케줄 변경 0회

## 추가된 lead

| 제목 | 상태 | 직접 URL | 페이지 | 공개 확인 신호 | 미확인/보류 사유 | Notion |
|---|---|---|---|---|---|---|
| KnowYourHue | 검증 필요 | https://knowyourhue.com/ko/ | Fello page 1 (API page 0) | 가격 80만원, 매출·이익 0, 344페이지/8개 언어, 소스·도메인·Analytics/Search Console·30일 이메일 지원 공개 | 실제 트래픽/매출 검증 전; 승격 기준의 재무 성과 미충족 | https://app.notion.com/p/KnowYourHue-3f717bf7599f81b0a65fff4eca2c4001 |
| 급)3개월/펀딩3번 매출2.24억원 순수익 약8,200만원 / 건강식품 | 보류 | https://sellernet.kr/product/df01f138-caf1-4735-9b19-b559f3b955e2 | Sellernet page 1 | 가격 4,500만원, 상반기 매출 224,410,900원, 순수익 약 82,000,000원, 온라인 자산·광고 데이터·재펀딩 연계 지원 | 가격이 3천만원 한도 초과; 상세 브랜드명/재무·자산 목록은 NDA 후 | https://app.notion.com/p/3-3-2-24-8-200-3f717bf7599f81f29de6f28af970201b |
| Doctor veterinarian | 검증 필요 | https://flippa.com/13479402-doctor-veterinarian | Flippa page 1 | USD 6,700, 월매출/월이익 USD 290, 10M+ 다운로드, 2018년부터 운영, zero-maintenance/fully passive 공개 | 인수·소스 이전 범위와 상세 운영 부담 미확인; 환율 적용은 별도 검증 필요 | https://app.notion.com/p/Doctor-veterinarian-3f717bf7599f818ea66ad226520fa936 |
| Empire Flippers #97751 · Hobbies/Outdoors Amazon FBA | 보류 | https://empireflippers.com/listing/97751/ | Empire page 1 AJAX | 가격 USD 654,855, 순이익 USD 242,540/10개월, 매출 USD 739,905/10개월, Amazon FBA, 2.7x | 가격이 3천만원 한도 초과; 상세 listing은 unlock 필요, 이전 범위 미확인 | https://app.notion.com/p/Empire-Flippers-97751-Hobbies-Outdoors-Amazon-FBA-3f717bf7599f81988e66e285219cff18 |
| Business Education Platform · Quiet Light #18829636 | 보류 | https://quietlight.com/listings/18829636/ | Quiet Light page 1 | 공개 카드에 매출 USD 45,161,452, income USD 10,843,118, $10M+ EBITDA/100+ members 표기 | 가격·규모가 한도 초과; page 2가 page 1 반복되어 pagination 실패, 운영·이전 범위 미확인; 403 우회 없음 | https://app.notion.com/p/Business-Education-Platform-Quiet-Light-18829636-3f717bf7599f8168bc43d3e433a82aef |

Listing은 공개 pagination endpoint 부재이므로 Notion 후보로 만들지 않았다. 위 5건은 확정 인수 후보가 아니라 `신규 검토` 상태의 보류 lead다.
