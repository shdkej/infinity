# r2 신규 수집 범위와 기준선

## 기준선

- 기존 Notion DB `인수 후보 데이터베이스 — 3천만원 이하`의 16개 행은 보존한다.
- 기존 행의 플랫폼·후보명·출처·가격을 deduplication 기준으로 먼저 읽고, 기존 후보의 값은 r2에서 임의로 덮어쓰지 않는다.
- 신규 행은 공개 원문에서 직접 재현 가능한 정보가 있을 때만 추가·갱신 대상으로 삼는다.

## 수집 범위

- 대상 공개 목록: Fello, Listing, Sellernet, Flippa, Empire Flippers, Quiet Light, Acquire.
- 가격 상한: 공개 가격이 30,000,000원 이하로 확인되는 후보. 통화 환산이 필요한 값은 환율을 추정하지 않고 `capital_risk`/보류로 남긴다.
- 필수 근거: 후보별 직접 상세 URL 또는 안정적인 listing ID, 확인 시각(UTC), 가격, 공개된 매출·이익, 운영 부담, 적합도 근거, 검증 공백.
- fingerprint: `platform + direct_listing_url_or_listing_id + normalized_title`; 목록 루트 URL이나 직접 링크가 없는 후보를 신규 fingerprint로 만들지 않는다.
- 접근 제한·JS 렌더링 실패·목록 루트만 확인된 경우는 후보 수와 증거 공백으로 기록하고 Notion 신규 행으로 승격하지 않는다.

## 보호 경계와 완료 기준

- 구매, 판매자 연락, 계약, 결제, 로그인, 비공개 자료 요청, 외부 발송, 스케줄/cron 변경, Notion 스키마·권한 변경은 수행하지 않는다.
- 기존 16행 보존, 순회한 페이지와 접근 제한 기록, 신규 후보의 직접 링크·핵심 수치·운영 부담·적합도·검증 상태 기록이 T1.1 기준이다.
- T1.2에서는 신규·중복·보류를 구분해 `new-candidate-inventory.md`와 `notion-update-proof.md`에 남긴다.
