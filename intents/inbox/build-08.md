# build-08: Control Center Authenticated Publish Pipeline

- id: build-08
- status: inbox
- projects: [infinity, personal-ops, infrastructure]
- task_type: implementation
- topics: [dashboard, cms, auth, publish, deploy]
- owner: SAM
- display_name: Control Center Authenticated Publish Pipeline
- created_at: 2026-06-12T10:05Z
- source: continuity follow-up from build-07 Next.js Supabase CRUD MVP
- predecessor: build-07

## User Request

사용자는 프로젝트성 작업이 단계 완료 후 끊기지 않고 이어지기를 원한다. build-07은 웹에서 CMS 데이터를 생성, 수정, 삭제하는 MVP까지 완료했지만, 실제 공개 페이지 정본 반영은 아직 열지 않았다.

## Purpose

Control Center CMS를 scratch data CRUD에서 실제 publish 가능한 운영 도구로 확장하기 위한 다음 경계와 구현 단계를 만든다.

## First Useful Action

Family Wedding NOTICE를 첫 대상으로 삼아 다음 흐름을 작게 설계하고 구현한다.

- CMS record 선택.
- diff preview.
- 승인형 publish action.
- source repo write.
- commit/push.
- deploy trigger or existing deploy lane reuse.
- public URL verification.
- audit log.
- rollback handle.

## Approval Boundary

실제 production page write/deploy, GitHub/AWS token expansion, auth/permission 변경은 안전 설계와 확인 후 진행한다. destructive action, force-push, secret 노출, 비용 발생 리소스 추가는 제외한다.

## Continuity

build-07은 웹 데이터 조작 완료 단계다. build-08은 "데이터를 실제 공개 산출물로 반영하는 CMS"로 넘어가는 다음 intent다.
