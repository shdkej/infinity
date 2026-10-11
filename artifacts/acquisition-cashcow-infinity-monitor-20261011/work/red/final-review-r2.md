# Red 최종 재검증 r2 — acquisition-cashcow-infinity-monitor-20261011

검토 시각: 2026-10-11 UTC

## 최종 판정: FAIL(수정 필요)

공개 페이지·기존 Notion 조회·3천만원 기준·승인 경계·task-plan 상태와 Infinity-local runner의 기본 실행 증거는 확인된다. 그러나 runner의 fingerprint는 후보 단위(`platform + direct_url/listing_id + normalized_title`)가 아니라 source URL 단위이며, `--dry-run`도 fingerprint 상태 파일을 쓸 수 있다. 따라서 후보 중복 차단과 진정한 dry-run 완료를 PASS로 판정할 수 없다.

## 요구사항별 검증

- 요구사항: `monitor_runner.py`가 deadline 입력을 받는가
  - 판정: PASS
  - 직접 증거: `work/monitor_runner.py`의 필수 `--deadline`, ISO 시각 파싱 및 `now >= deadline` 조기 차단; `work/monitoring-verification.md`에 실행 명령이 기록됨.
  - 반례 확인: 과거 deadline은 blocked/exit 2로 처리된다.
  - 다음 조치: 없음.

- 요구사항: fingerprint·오류 JSONL·dry-run 증거가 실제 구현·실행에 있는가
  - 판정: FAIL
  - 직접 증거: runner는 응답 SHA-256과 source URL fingerprint 및 source별 `error`를 `runs.jsonl`에 기록한다. `runs.jsonl`에 `2026-10-11T07:34:10Z`, `dry_run: true`, 7개 source 결과가 있다.
  - 반례 확인: fingerprint는 `site|url`뿐이라 후보 단위 중복 키 계약과 불일치한다. `dry_run`이어도 `new`가 있으면 `fingerprints.json`을 쓴다. 후보 추출/Notion update 전 중복 차단 테스트도 없다.
  - 다음 조치: 후보 fingerprint를 실제 계산·비교하는 승인된 구현과, dry-run에서 상태 파일을 쓰지 않는 테스트 증거를 남긴다.

- 요구사항: 공개 페이지 순회·접근 제한과 예산 기준이 일치하는가
  - 판정: PASS
  - 직접 증거: `work/paginated-marketplace-inventory.md`에 7개 사이트, 페이지/필터 종료·접근 제한, 마스킹·동적 값 보류가 기록됨. `work/scope-and-boundary.md`에 원문 통화 확인 시에만 3천만원 이하 판정, 환율 추정 보류가 명시됨.
  - 반례 확인: Acquire 동적/접근 제한과 Flippa JS 제한을 우회하지 않았고, 초과·불명확 가격을 확정하지 않았다.
  - 다음 조치: 없음.

- 요구사항: Notion 9개 필드·16개 행과 task-plan 설명이 일치하는가
  - 판정: UNCERTAIN(부분 불일치)
  - 직접 증거: `work/notion-database-verification.md`는 실제 DB ID, 9개 필드, 16개 행 조회를 기록한다. 필드는 후보명·플랫폼·출처·매입가·월매출·월이익·적합도·상태·최종 확인이다.
  - 반례 확인: `task-plan.json` T1.3 validation은 운영 부담·검증 상태·원문 링크가 실제 필드인 것처럼 적혀 있으나, 검증 문서는 owner hours·transfer scope·independent verification이 스키마에 없다고 명시한다.
  - 다음 조치: schema 변경 없이 T1.3 validation을 실제 9개 필드와 맞게 정정한다. 필드 추가는 별도 승인 전 금지한다.

- 요구사항: 승인 경계·task-plan 상태가 실제 상태와 일치하는가
  - 판정: PASS
  - 직접 증거: `task-plan.md`와 `task-plan.json` 모두 T1.1~T2.1 완료, T2.2 진행/active로 기록한다. `work/remote-proof.txt`는 목록에만 있고 존재하지 않는다.
  - 반례 확인: 구매·계약·결제·판매자 연락·외부 발송·스케줄·schema/권한 변경을 했다는 증거가 없고, 원격 반영 완료를 주장하지 않는다.
  - 다음 조치: 원격 proof가 실제 생성되기 전 T2.2를 완료로 바꾸지 않는다.

## 핵심 반박

1. source URL fingerprint는 후보 중복 방지 계약을 충족하지 않는다.
2. `dry-run` 플래그가 상태 파일 쓰기를 막지 않아 증거 의미가 약하다.
3. T1.3 task-plan의 필드 설명이 실제 9개 Notion 필드와 어긋난다.

외부 발송·구매·연락·스케줄 등록·schema 변경은 수행하지 않았다.
