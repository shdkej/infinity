# build-14 - Daily System Metrics Visualization

Status: Withdrawn
Created: 2026-08-05T21:58:20Z
Deadline: 2026-08-06T05:58:20Z

## User Intent

마스터는 자신의 시스템 지표를 그래프로 매일 볼 수 있는 시각화 페이지를 원한다. 작업은 Infinity를 중심 공유 상태판으로 두고, Planner / Developer / Marketer / Operator 4개 서브에이전트가 각자의 워크플로우를 수행하도록 위임한다. 중간 산출물은 Knowledge Lab에 남긴다. 메인 에이전트는 장시간 블록되지 않아야 한다.

## Working Scope

- Center of record: `/home/ubuntu/workspace/knowledge-lab/infinity`
- Intermediate outputs: `artifacts/build-14/`
- Execution reports: `reports/build-14/`
- Potential implementation target: to be selected by Developer after repo inspection. Existing dirty worktree changes must not be reverted.

## First-Version Goal

8시간 이내에 "매일 볼 수 있는 첫 시각화 페이지"를 만든다.

Minimum useful version:

- 최근 N일의 시스템 지표를 날짜별로 볼 수 있다.
- 최소 3개 이상의 일일 지표군을 그래프로 보여준다.
- 데이터 계약이 문서화되어 다음 지표 추가가 쉽다.
- 로컬 또는 배포된 URL에서 실제 화면을 확인할 수 있다.
- 운영자가 매일 갱신/확인할 수 있는 경로가 문서화되어 있다.

## Role Ownership

- Planner: 지표 정의, 정보 구조, 첫 버전 범위, 사용 시나리오.
- Developer: 구현 대상 repo 선정, 데이터 계약, 페이지 구현, 테스트/스크린샷 검증.
- Marketer: 화면 이름, 첫 화면 카피, 사용자가 매일 보고 싶어지는 표현.
- Operator: 데이터 갱신 경로, 배포/검증, 장애/롤백/비용 리스크.

## Coordination Rules

- 각 역할은 자기 산출물을 `artifacts/build-14/{role}.md`에 쓴다.
- 구현 파일은 Developer만 수정한다. 다른 역할은 제안 문서만 쓴다.
- 공통 상태는 `artifacts/build-14/STATUS.md`에 짧게 갱신한다.
- 외부 발송, 공개 권한 변경, 비용 발생 설정, 자격증명 변경은 사용자 승인 전 실행하지 않는다.
- 사이트/대시보드 변경은 사용자가 로컬만이라고 제한하지 않았으므로 최종 목표는 라이브/원격 가시성까지 포함한다. 단, 기존 dirty worktree와 배포 권한 리스크가 있으면 먼저 보고한다.

## Completion Gates

- 4개 역할 산출물 존재.
- Developer 구현 또는 구현 불가 시 명확한 blocker와 다음 첫 액션.
- 화면 검증 결과 또는 로컬 preview 스크린샷.
- Operator가 배포/운영 경로를 확인.
- Infinity HTML report contract를 만족하는 최종 report.

## Closure

- 2026-08-06: 사용자 판단으로 시각화 결과물을 철회하고 공개 `build-14` 경로를 제거했다. 현재 라이브 경로는 Infinity Kanban fallback이며, sample metrics는 운영 화면으로 유지하지 않는다.
