# 최종 Red 검증 — acquisition-cashcow-infinity-monitor-20261011

## 최종 판정: FAIL(수정 필요)

### 요구사항별 검증

- 요구사항: `monitor_runner.py`가 후보 상세 URL 기반 fingerprint를 계산한다.
  - 판정: PASS(부분)
  - 직접 증거: `work/monitor_runner.py`의 `candidates` 추출과 `sha256(f"{site}|{x}")`; 실행에서 Fello 174개, Quiet Light 92개 후보 링크 fingerprint가 생성됨.
  - 반례 확인: 후보 상세 링크가 없는 source는 원본 source URL을 fallback key로 fingerprint한다.
  - 다음 조치: 상세 URL이 없을 때 source-level fallback을 후보 fingerprint로 취급하지 않도록 no-candidate로 분리한다.

- 요구사항: dry-run에서 대상 `fingerprints.json`을 변경하지 않는다.
  - 판정: PASS
  - 직접 증거: `py_compile` 성공; `--deadline 2099-01-01T00:00:00Z --dry-run` 종료 코드 0, `new_fingerprints=0`; 대상 파일 SHA-256이 전후 `e622e7687eaa4a6953259ab1f1da3a6e8bce599201e29a011c431924b5a06722`로 동일.
  - 반례 확인: dry-run은 `runs.jsonl`에는 append한다. fingerprint 상태 파일 불변과는 별개인 관측 로그 변경이다.
  - 다음 조치: 없음.

- 요구사항: fingerprint 상태 파일 경로가 Infinity 정본과 일치한다.
  - 판정: FAIL
  - 직접 증거: `ROOT=Path(__file__).resolve().parents[3]`는 이 파일 위치에서 `/home/ubuntu/workspace/knowledge-lab`을 가리킨다. 따라서 `STATE`는 `/home/ubuntu/workspace/knowledge-lab/data/.../fingerprints.json`이며 정본인 `infinity/data/.../fingerprints.json`과 다르다.
  - 반례 확인: non-dry-run 신규 fingerprint가 Infinity 정본을 갱신하지 않을 위험이 있다.
  - 다음 조치: `ROOT=Path(__file__).resolve().parents[2]` 등으로 고치고 정본 경로의 non-dry-run fixture를 검증한다. 이번 검증에서는 코드를 수정하지 않았다.

- 요구사항: T1.3의 실제 Notion 정규화 설명이 9개 필드/16개 행을 정확히 기술한다.
  - 판정: PASS
  - 직접 증거: `work/notion-database-verification.md`에 9개 필드와 2026-10-11 조회 16개 행이 기재되어 있다.
  - 반례 확인: owner hours·transfer scope·독립 검증 필드는 없고 일부 금액은 공개값/환율 가정임을 명시한다.
  - 다음 조치: 없음. schema 변경은 별도 승인 대상이다.

- 요구사항: 페이지·Notion·승인 경계가 지켜진다.
  - 판정: PASS
  - 직접 증거: 범위 문서와 `monitoring-verification.md`, `task-plan.md`에 공개 매물 조회, Notion 조회, 판매자 연락·구매·계약·결제·외부 발송·스케줄/schema/권한 변경 금지가 기록되어 있다. 코드에도 scheduler/Notion mutation/seller action이 없다.
  - 반례 확인: 외부 연락·구매·발송·스케줄 등록은 확인되지 않았다.
  - 다음 조치: 없음.

### 핵심 반박

1. 정본 상태 파일 경로가 잘못 계산되어 non-dry-run 중복 방지의 실제 효과를 PASS할 수 없다.
2. 일부 source는 상세 후보 URL이 없을 때 source URL fallback을 fingerprint하므로 상세 URL 계약을 엄밀히 충족하지 않는다.
3. 따라서 py_compile, dry-run 불변성, T1.3 설명과 경계는 통과하지만 전체 산출물은 FAIL이다.

검증 시각: 2026-10-11 UTC
