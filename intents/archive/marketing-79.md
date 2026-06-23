# marketing-79 Virtue 첫 10명 활성화 1장 관찰표

- id: marketing-79
- status: archived
- completed_at: 2026-06-23T1000Z
- projects: [virtue]
- task_type: strategy
- topics: [marketing, activation, prelaunch]
- permission_level: L1 docs-only
- result_summary: 출시 직후 첫 10명 활성화 관찰을 위한 1장 관찰표 초안 완성. 홈진입·/add·deed_judged·deed_saved·D1 재방문 5체크포인트, 세션 성격 4분류(성공/B-LOST/B-MISMATCH/B-AVAIL), 자기 말 기록칸 포함. J1/J2/J4=deed_saved·J3=deed_judged 기존 정의와 충돌 0.
- artifacts:
  - path: artifacts/marketing-79/week-one-activation-observation-table.html
    role: design
    note: 첫 10명 손기록용 1장 관찰표. 잡별 first value 가이드·세션 성격 4분류·10개 사용자 카드 포함.
- reports:
  - path: reports/marketing-79/2026-06-23T1000Z.html
    role: final
- commits: []
- urls: []
- next_actions:
  - 1주차 관찰 후 잡 분포 파악 → 잡별 first value 도달 정성 리뷰
  - RC-WARM(first value 도달 후 D1 미방문) 사용자는 marketing-43 기준으로 별도 메모
  - 표 사용 후 개선 필요 칸 발견 시 Inbox에 수정 intent 등록

## Goal

prelaunch 저신호 상태에서 첫 10명 사용자의 활성화 행동을 일관되게 읽기 위한 1장짜리 손기록 관찰표를 작성한다.

## Success Criteria (충족 여부)

- [x] 홈 진입, `/add` 시작, `deed_judged`, `deed_saved`, D1 재방문 5개 체크포인트 포함
- [x] J1/J2/J4=`deed_saved`, J3=`deed_judged` 기존 정의와 충돌 없는지 검토 완료 (충돌 0)
- [x] 세션 종료 성격 4분류 포함
- [x] 자기 말 기록칸 포함 (손기록 전용)
- [x] HTML report gate 통과

## Inherited Learning

- First Value Mapping (m06): J1/J2/J4=deed_saved, J3=deed_judged — 체크포인트 순서 기준
- First-User Learning Loop (m47): 자기 말 4지점 루프 — 자기 말 칸 설계 근거
- Session Value Is Read By Job (m42): J3 무저장 정상종료 구분 — 결과 칸 설계
- First-Week Non-Return (m43): D1 재방문은 KPI가 아니라 RC 분류 출발점
- Guided First-Value Is A Four-Stage Handoff (m51): 홈진입→/add→judged→saved/exit 4구간 — 체크포인트 순서

## Safety

- production code changes: 0
- deploys: 0
- tracking/privacy changes: 0
- public copy changes: 0
- external messages: 0
- cost: 0
