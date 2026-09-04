# Safety Map 2차 실험 — 실행 태스크 목록

## 기준선

- **PRD:** [planner-prd.md](planner-prd.md)
- **현재 마감:** 2026-09-05 08:00 Europe/Rome (06:00 UTC)
- **현재 실행:** 4회차
- **상태 기준:** `task-plan.json`이 기계 판정 정본이고, 이 문서는 사람이 진행을 읽는 정본이다. 둘은 같은 변경에서 함께 갱신한다.

## 계획 태스크

| ID | 태스크 | 상태 | 완료/다음 증거 |
| --- | --- | --- | --- |
| T1 | PRD와 Mapbox·디자인·종료 수용 기준 고정 | 완료 | `planner-prd.md` |
| T2 | 실제 Mapbox canvas·장소/도로·주야간 레이어 구현 경로 검증 | 완료 | `evidence/20260903T140452Z-m4-rome-recovery-index.md` |
| T3 | desktop·390px 검색·zoom/pan·레이어 실제 렌더 증거 | 진행 중 | compositor-visible 상태 변화 capture가 필요 |
| T4 | focused Red의 실제 화면·provenance 재검토 | 대기 | T3 통과 뒤 `red-focused-final.md` |
| T5 | 배포·원격 동작·Slack terminal receipt 검증 | 대기 | T4 통과 뒤 원 스레드 receipt |
| T6 | 마감 전 디자인·접근성·품질 반복 | 대기 | T5 전후의 실제 렌더·접근성 evidence |

## 계획 변경 기록

변경은 기존 태스크를 지우지 않고 `—`로 append합니다.

- **2026-09-03 13:45 UTC — T3:** 관리 브라우저 프로필 lock/WebGL 제약으로 기본 렌더 경로를 격리 Chromium·software WebGL 검증으로 전환했습니다.
- **2026-09-04 07:43 UTC — T3–T6:** 이전 마감 실패 후, 사용자 승인으로 새 Italy 08:00 마감에서 T3부터 재검증하도록 재개했습니다.
- **2026-09-04 07:46 UTC — T3:** canvas/WebGL과 control state는 관측됐지만 화면 캡처 해시가 동일했습니다. 부분 증거로 보존하고 완료 판정을 보류했습니다.
- **2026-09-04 08:22 UTC — T3:** CDP window-surface 캡처도 동일 해시였습니다. compositor-visible capture 경로를 추가 조사 대상으로 넣었습니다.
- **2026-09-04 13:59 UTC — T3:** 사용자 지시로 Waiting을 종료하고, 관리 브라우저 프로필 복구와 OpenClaw browser capture를 추가 자율 대안으로 재개했습니다.

## 지금 다음 행동

1. OpenClaw 관리 브라우저의 프로필 시작 오류를 복구한다.
2. 실제 화면 변화가 보이는 desktop·390px capture를 확보한다.
3. T3가 통과할 때만 T4 Red → T5 배포/terminal receipt로 이동한다.

