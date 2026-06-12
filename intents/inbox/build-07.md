# build-07: Control Center Save/Publish Boundary

- id: build-07
- status: inbox
- projects: [infinity, personal-ops, infrastructure]
- task_type: design
- topics: [dashboard, cms, editing, deploy, security]
- owner: SAM
- display_name: Control Center Save/Publish Boundary
- created_at: 2026-06-12T09:38Z
- source: continuity follow-up from build-06 Draft Edit MVP
- predecessor: build-06

## User Request

사용자는 프로젝트성 작업이 Archive에서 끊기지 않고 이어지기를 원한다. build-06은 Control Center에 draft-only edit/diff preview를 배포했지만, 실제 저장·commit·publish는 아직 구현하지 않았다.

## Purpose

Control Center가 "수정 가능한 CMS"로 가기 위한 다음 경계, 즉 정본 파일 저장, commit/push, 배포 버튼, 토큰/권한 모델을 어떤 순서와 승인 단위로 열지 정한다.

## First Useful Action

write/publish 기능을 바로 열지 말고, 다음을 분리한 설계/승인 표를 만든다.

- local-only draft save
- server-side write API
- GitHub commit/push action
- GitHub Pages/AWS deploy action
- auth/permission
- audit log/change log
- rollback/revert path

## Approval Boundary

실제 write API, auth/permission, GitHub/AWS token server function, production deploy button, automatic commit/push, Terraform/AWS resource, cost-bearing or destructive action은 별도 승인 없이는 구현하지 않는다.

## Continuity

build-06은 draft editor MVP 완료 단계다. build-07은 실제 저장/배포 CMS로 가기 위한 승인 경계와 구현 순서를 잡는 후속 intent다.
