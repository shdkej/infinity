# T2.1 반복 모니터링 실행 경로·중복 방지 검증

## 기존 실행 경로

- 소스: `/home/ubuntu/workspace/knowledge-lab/source/openclaw-system/scripts/monitor_acquisition_candidates.py`
- 공개 수집 범위: Fello, Sellernet, Flippa SaaS, Flippa apps 가격 필터 page 1–3 및 15k–49k 구간.
- Notion DB: `3f517bf7-599f-8176-8e1a-cddf002cf70b`.
- 자격증명 로드: 환경변수 우선, `~/.env` 또는 systemd override fallback. 값 자체는 기록/노출하지 않는다.
- 중복/실패: 현재 스크립트는 source별 status·bytes·sha256 또는 error를 JSONL에 기록하지만 후보 fingerprint 중복 방지는 구현하지 않는다. 따라서 이번 Infinity 경로의 중복 키는 `platform + direct_url/listing_id + normalized_title`로 별도 고정한다.

## 실행 검증 결과

1. 스크립트 소스에서 공개 URL 목록, DB ID, Notion query/update API, JSONL 실패 기록을 확인했다.
2. 실제 Notion API로 9개 필드와 16개 행을 조회했다.
3. 현재 날짜가 기존 스크립트의 hard-coded `DEADLINE=2026-10-11 08:00 KST` 이후라 스크립트 본 실행은 조기 종료한다. 이를 성공으로 가장하지 않고 `stale_deadline_guard`로 기록한다.
4. 새 schedule 등록·기존 scheduler 변경·외부 발송은 하지 않았다.

## 재실행 계약

다음 승인된 실행은 deadline을 실행 입력으로 받아야 하며, 각 source fetch 결과를 JSONL에 append하고 Notion 업데이트 전 `fingerprint`로 중복을 차단한다. API key 부재, HTTP 오류, JS/로그인 제한, Notion schema 불일치는 source별 실패로 남기고 전체 실행을 조용히 성공 처리하지 않는다.

## Infinity-local 보완 runner

`work/monitor_runner.py`를 추가했다. `--deadline` 실행 입력, 페이지에서 추출한 후보 상세 URL fingerprint, 응답 SHA-256, source별 오류/`no_candidate_links` JSONL을 제공하며 스케줄·Notion schema/권한·판매자 상호작용은 하지 않는다. 상태 파일은 이름이 `infinity`인 저장소 루트 아래에 두고, `--dry-run`에서는 fingerprint 상태 파일을 쓰지 않는다. 상세 후보 링크가 없는 source URL 자체는 fingerprint로 취급하지 않는다.

검증 명령: `python3 work/monitor_runner.py --deadline 2026-10-11T23:00:00Z --dry-run`

## 판정

기존 외부 스크립트의 고정 deadline·fingerprint 부재는 남아 있지만, Infinity 저장소 안의 수동 runner로 재실행 조건과 중복 방지·실패 기록을 검증할 수 있다. 기존 소스 저장소는 수정하지 않았고 새 schedule도 등록하지 않았다.
