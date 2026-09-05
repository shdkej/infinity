# Safety Map 대형 작업 실험 1·2차 아카이브 보고서

- 작성일: 2026-09-05
- 대상: `safety-map-correction-20260903`, `safety-map-experiment-02-20260904`
- 종료 결정: 사용자 명시 아카이브 요청
- 판정: **두 실험 모두 성공 완료가 아닙니다.** 1차는 `experiment_failed`, 2차는 `deadline_missed`로 보존합니다.

## 1차 — 2026-09-03 교정 실험

### 결과

- 초기 정적 배포본은 존재하지만, 사용자가 요구한 지도 중심 UX·디자인 정본 반영·실제 상호작용 검증의 교정에는 실패했습니다.
- 마감 뒤 실질 산출물 없이 dispatcher handoff가 반복됐고, 사용자가 실험 중단을 지시했습니다.

### 직접 원인

1. fixture/HTTP 200을 실제 사용자 화면 완료 증거로 과대 해석했습니다.
2. `BRAND → DESIGN → DESIGN_SYSTEM`을 구현과 Red 시각 검증의 선행 게이트로 연결하지 못했습니다.
3. 관리 브라우저 프로필 lock과 캡처 경로 제약을 대체 렌더 검증으로 충분히 전환하지 못했습니다.
4. 기능 완료 전 품질 반복 대신 빈 handoff가 누적됐습니다.

### 남긴 자산

- 대형 작업 시간 계측·Red 병목 관찰 계약
- Mapbox/Remotion 도구 사용 경계와 보호된 설정 참조 원칙
- 마감 hard-stop, 렌더 증거, terminal 알림 receipt를 분리한 개선 규칙

## 2차 — 2026-09-04 재실험

### 결과

- 실제 Mapbox canvas, Trevi 검색, 확대/이동, 주·야간 스타일, 1440px·390px 렌더, 접근성·focused Red 검토까지는 근거를 확보했습니다.
- 그러나 2026-09-05 06:00 UTC 마감 전 terminal Slack receipt가 없었고, 마감 후 terminal cycle도 3시간 이상 지연됐습니다.
- 따라서 제품 품질 증거와 별개로 운영 실험은 `deadline_missed`입니다.

### 직접 원인

1. terminal receipt의 사전 시간 게이트와 마감 후 terminal dispatch를 분리하지 못했습니다.
2. active leaf가 없는 `quality_iteration` 상태를 dispatcher가 30분마다 재인계해, 실제 작업 없는 handoff가 증가했습니다.
3. 계획·trace·카드 데이터가 분리돼 진행 수치 정합화가 늦었습니다.
4. 종료 알림은 발송됐지만 마감 후 receipt여서 성공 종료 조건을 충족하지 못했습니다.

### 검증된 자산

- `planner-prd.md`와 계층형 `task-plan.md`/`task-plan.json`
- 실제 화면 렌더와 focused Red 검토 근거
- AWS 라이브 경로와 지도 상호작용 확인 근거
- terminal learning report 및 원 Slack thread delivery receipt

## 공통 개선 사항

1. **실행 회차와 점검 회차를 분리**합니다. 새 artifact·테스트·렌더·커밋이 없는 handoff는 실행으로 세지 않습니다.
2. **계획은 leaf부터 활성화**합니다. active leaf가 없으면 다음 의존성 충족 leaf를 만들기 전에는 handoff하지 않습니다.
3. **모든 leaf에 예산과 의존성**을 둡니다. 기본 20–40분, 최대 60분이며 최대 시간에는 분할·대체 경로·외부 차단 중 하나를 기록합니다.
4. **마감 처리와 성공 처리 분리**합니다. deadline 직후 terminal reconciler는 반드시 한 번 실행하고, receipt가 마감 후면 `deadline_missed`로 고정합니다.
5. **시각 산출물의 완료 증거를 강화**합니다. 디자인 정본 읽기, desktop·390px 실제 렌더, 사용자 상호작용, Red의 직접 시각 판정이 모두 필요합니다.
6. **아카이브는 결과 보존 상태**입니다. 실패·마감 미준수 Intent도 사용자가 종료를 결정하면 Archive로 옮기되, 결과 판정은 바꾸지 않습니다.

## 다음 실험의 최소 시작 조건

- 제품 구현과 운영 실험을 분리한 새 Intent
- 고정 벤치마크 1개와 변경할 운영 규칙 1개
- PRD → 계층형 작은 leaf 계획 → 실행·점검·변경 이력의 단일 정본
- terminal receipt를 마감 전에 시험하는 별도 leaf

## 참조

- 1차 실패 보고: `reports/safety-map-correction-20260903/20260903T0840Z-experiment-failure.md`
- 2차 terminal 보고: `reports/safety-map-experiment-02-20260904/20260905T0901Z-terminal.md`
- 2차 실행 계획: `artifacts/safety-map-experiment-02-20260904/task-plan.md`
