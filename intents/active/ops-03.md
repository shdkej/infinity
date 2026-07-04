# [ops-03] 자동 데일리 리뷰 본문 시작부 렌더 게이트 고정

- id: ops-03
- status: active
- priority: medium
- mode: prepare (완료) → execute_local (대기 중)
- started: 2026-07-04T0700Z
- prepare_report: reports/ops-03/2026-07-04T0700Z.html

## 현재 상태

prepare 단계 완료. execute_local 프롬프트 준비됨. 로컬 Claude 실행 대기 중.

## execute_local 프롬프트

```
Infinity Intent: ops-03 자동 데일리 리뷰 본문 시작부 렌더 게이트 고정
Mode: execute_local
Goal:
  LOCAL_REVIEW_AUTOMATION.md 또는 daily review 생성 스크립트에 저장 직전 렌더 게이트를 추가한다.
  1. 생성된 리뷰 본문의 첫 3줄에 내부 점검 패턴
     ("중복 게이트", "확인 소스", "소스 한계", "## 중복", "## 소스")
     이 나타나면 해당 블록을 본문 하단으로 이동하거나 제거한다.
  2. 저장 전 첫 줄이 헤드라인/한 줄 요약인지 검증한다.
Context:
  - LOCAL_REVIEW_AUTOMATION.md (위치 확인 필요, OpenClaw workspace)
  - daily review 생성 스크립트
Prepared findings:
  - 반복 패턴 6일 연속 확인 (2026-06-24~29)
  - 수정 지점: 저장 직전 후처리 게이트가 프롬프트 수정보다 더 결정적
Allowed: L0/L1 (로컬 파일 수정, git commit)
Forbidden: L2/L3 actions without explicit approval
Verification: 다음 daily review 생성 샘플 첫 줄이 헤드라인으로 시작하는지 확인
Report back to: reports/ops-03/{timestamp}-local.html
```

## 다음 액션

1. 로컬 Claude가 LOCAL_REVIEW_AUTOMATION.md 및 생성 스크립트 위치 파악
2. 렌더 게이트 함수/로직 추가
3. 테스트 샘플로 검증
4. 성공 시 ops-03 archive 처리
