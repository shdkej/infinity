# build-03: Control Center / Ops CMS for Dashboards

- id: build-03
- status: active
- priority: medium
- permission: L0/L1
- projects: [infinity, personal-ops, infrastructure]
- task_type: design
- topics: [dashboard, workflow, automation]
- owner: SAM
- display_name: Control Center / Ops CMS
- created_at: 2026-06-11T23:03Z
- activated_at: 2026-06-12T06:00Z
- source: user request in Telegram direct chat

## Purpose

Travel Dashboard, Status Dashboard, Infinity Dashboard, Card News Library, wedding/static pages처럼 흩어진 대시보드와 정적 페이지를 한곳에서 관리하는 내부 운영 CMS를 설계한다.

핵심은 범용 글쓰기 CMS가 아니라 대시보드 운영용 Control Center다. 어디에 무엇이 있고, 어떤 원장/데이터에서 만들어지며, 공개 URL과 배포 상태가 어떤지 한 화면에서 확인하고 필요한 반복 수정만 안전하게 버튼화하는 방향이다.

## Current State

- 2026-06-12T06:00Z **Inbox → Active 이동. 대시보드 인벤토리 템플릿 준비 완료(Cloud L0).** 사용자 요청(대시보드들 관리하는 CMS)을 Ops CMS 설계 Intent로 구조화. 5개 대시보드/페이지 인벤토리 템플릿 초안 작성 완료. 산출물: `artifacts/build-03/dashboard-inventory-template.md`. 로컬 실행에서 실제 경로·URL·빌드커맨드 채우기 대기.

## Next Action

Local Claude Code 위임: `artifacts/build-03/dashboard-inventory-template.md`의 모든 `[FILL_LOCAL]` 항목을 실제 값으로 채운 뒤 `artifacts/build-03/dashboard-inventory.md`로 저장. 이후 MVP 정보구조(registry/editor panel/deploy status board/change log) 초안 작성.

## Goal

현재 운영 중인 모든 대시보드/정적 페이지 인벤토리를 완성하고, Control Center MVP 정보구조를 정의한다.

## Success Criteria

- [ ] 인벤토리 아티팩트 완성 (실제 경로/URL/빌드커맨드 포함)
- [ ] MVP 정보구조 정의 완료
- [ ] 데이터 수정 vs 배포 액션 경계 분리
- [ ] 첫 내부 페이지 구현 계획 (프로덕션 변경 없이)

## Approval Boundary

L0/L1 리서치·설계 허용. 내부 설계 아티팩트 생성 허용.
실제 구현·배포·레지스트리 변경·새 API·인증/권한 변경·외부-공개 변경은 별도 명시 승인 필요.
