# Safety Map 2차 실험 — 실행 타임라인

`PRD: planner-prd.md` · `마감: 2026-09-05 08:00 Europe/Rome (06:00 UTC)` · `실행: 4회차`

```text
● T1  PRD와 Mapbox·디자인·종료 수용 기준 고정                         완료
│     └ planner-prd.md
│
● T2  실제 Mapbox canvas·장소/도로·주야간 레이어 구현 경로 검증        완료
│     └ evidence/20260903T140452Z-m4-rome-recovery-index.md
│
├─ — 2026-09-03 13:45 UTC · T3
│     관리 브라우저 lock/WebGL 제약 → 격리 Chromium·software WebGL 경로로 전환
│
◐ T3  desktop·390px 검색·zoom/pan·레이어 실제 렌더 증거              진행 중
│     └ 현재 기준: 화면 변화가 독립적으로 보이는 capture
│
├─ — 2026-09-04 07:43 UTC · T3–T6
│     이전 마감 실패 뒤 새 Italy 08:00 마감으로 재개. T3부터 다시 검증
│
├─ — 2026-09-04 07:46 UTC · T3
│     canvas/WebGL과 control state는 확인됐지만 capture hash가 동일함 → 부분 증거 보존
│
├─ — 2026-09-04 08:22 UTC · T3
│     CDP window-surface capture도 동일 hash → compositor-visible capture 경로 추가
│
├─ — 2026-09-04 13:59 UTC · T3
│     사용자 지시로 Waiting 종료 → 관리 브라우저 프로필 복구와 OpenClaw capture 재시도
│
○ T4  focused Red의 실제 화면·provenance 재검토                      T3 통과 뒤
│     └ red-focused-final.md
│
○ T5  배포·원격 동작·Slack terminal receipt 검증                     T4 통과 뒤
│
○ T6  마감 전 디자인·접근성·품질 반복                                T5 전후
```

**지금 다음 행동:** 관리 브라우저 프로필 시작 오류를 복구한 뒤, desktop·390px에서 실제 화면 변화가 보이는 capture를 확보한다.
