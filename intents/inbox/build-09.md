# build-09: Control Center Authenticated Publish + Rollback

- id: build-09
- status: inbox
- projects: [infinity, personal-ops, infrastructure]
- task_type: implementation
- topics: [dashboard, cms, auth, publish, deploy, rollback]
- owner: SAM
- display_name: Control Center Authenticated Publish + Rollback
- created_at: 2026-06-12T10:40Z
- source: continuity follow-up from build-08 shadcn UI + status composition CMS
- predecessor: build-08

## User Request

사용자는 단계 완료 후 작업이 끊기지 않고 이어지기를 원한다. build-08은 CMS 안에서 Status 구성/record를 만들고 저장하는 운영툴까지 완료했다. 다음은 그 구성을 실제 공개 페이지 정본으로 안전하게 내보내는 경계다.

## Purpose

CMS에서 만든 status 구성/record를 실제 publish 가능한 파이프라인으로 연결한다. build-08까지는 Supabase 안의 구성 데이터였고, 아직 공개 페이지 정본 반영은 열지 않았다.

## First Useful Action

가장 작은 안전 흐름 하나(예: 한 surface 또는 Family Wedding NOTICE)를 대상으로:

- CMS 구성/record 선택 → diff preview.
- 승인형 publish action (auth/permission 게이트).
- source repo write (또는 status feed 재생성).
- commit/push.
- deploy trigger 또는 기존 deploy lane 재사용.
- public URL 검증.
- audit log 기록 (이미 control_center_activity 존재 — publish action 추가).
- rollback handle.

## Approval Boundary

실제 production page write/deploy, GitHub/AWS token 확장, auth/permission 변경은 안전 설계와 사용자 확인 후 진행한다. destructive action, force-push, secret 노출, 비용 발생 리소스 추가는 제외한다.

## Continuity

build-08 archive와 report를 먼저 읽고, control_center_nodes/activity 모델 위에서 publish 경계를 설계한다.
