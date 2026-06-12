# build-05: Control Center Editable CMS

- id: build-05
- status: inbox
- projects: [infinity, personal-ops, infrastructure]
- task_type: implementation
- topics: [dashboard, cms, editing, deploy, automation]
- owner: SAM
- display_name: Control Center Editable CMS
- created_at: 2026-06-12T07:18Z
- source: user request in Telegram direct chat

## User Request

사용자가 배포된 Control Center CMS에 대해 "Cms는 수정이 핵심인데 수정 돼? 안되면 되게 인피니티에 등록해줘"라고 요청했다.

현재 `build-04`의 Control Center는 `https://status.aws.shdkej.com/control-center/index.html`에 배포된 read-only MVP이며, 대시보드/정적 페이지 registry와 운영 경계만 보여준다. 실제 수정 UI, write API, auth, 배포 버튼은 아직 없다.

## Purpose

Control Center를 단순 상태판이 아니라 실제 운영 수정 진입점으로 확장한다. 사용자가 Travel Dashboard, Family Wedding 안내장, Card News Library, Status registry 같은 반복 수정 대상을 한곳에서 고르고, 안전한 필드 단위 수정과 preview, commit/push, 배포/검증 흐름까지 따라갈 수 있게 만든다.

## Scope

### Include

- Editable surface registry: 각 표면별 수정 가능한 필드, 정본 파일, preview/build/deploy/verify 명령.
- First editable target selection: Family Wedding 안내장 notice 문구처럼 작고 검증 쉬운 static page edit을 1차 대상으로 삼는다.
- Draft edit flow: 수정 입력 → diff preview → validation → commit message 초안 → deploy/verify 상태 기록.
- Change log: 어떤 필드가 언제 어떤 커밋/배포 URL로 반영됐는지 Control Center에서 볼 수 있게 한다.
- Safety boundary: read-only view, draft-only edit, publish/deploy action을 UI와 코드에서 분리한다.

### Exclude For First Pass

- 범용 블로그/WYSIWYG CMS.
- 다중 사용자 권한/복잡한 roles.
- 비밀값 편집.
- 무승인 Terraform/AWS 리소스 추가.
- 외부 메시지 발송, 비용 발생 작업, force-push/destructive rewrite.

## First Useful Action

`build-04` read-only Control Center를 기준으로, 다음을 설계/구현 가능한 작은 단위로 쪼갠다.

1. `editableSurfaces` schema를 정의한다.
2. Family Wedding 안내장의 `NOTICE`/본문/OG description처럼 반복 수정 가능한 필드 3~5개를 첫 editable target으로 등록한다.
3. 로컬 파일 수정은 직접 적용하지 않고 먼저 diff preview를 만드는 방식으로 시작한다.
4. publish/deploy 버튼은 approval-needed 단계로 남기되, 이미 SAM이 수동으로 수행하는 commit/push/GitHub Pages verification 절차를 change-log model로 기록한다.

## Success Criteria

- [ ] Control Center에서 최소 1개 표면(Family Wedding 또는 Travel Dashboard)의 editable fields를 볼 수 있다.
- [ ] 입력값이 어떤 파일/라인/필드를 바꿀지 diff preview로 확인할 수 있다.
- [ ] publish/deploy는 read-only/draft edit과 분리되어 있고 승인 경계가 명확하다.
- [ ] 변경 이력이 commit SHA, deploy run, public URL verification과 연결된다.
- [ ] 공개 URL을 받은 사용자가 "여기서 수정 작업을 시작할 수 있다"고 이해할 수 있다.

## Approval Boundary

L0/L1/L2 범위에서 설계, schema, read-only/draft UI, diff preview, 내부 change-log 기록은 진행 가능하다.

실제 write API 노출, auth/permission 변경, production deploy 버튼, GitHub/AWS 토큰을 쓰는 서버 기능, Terraform/AWS 리소스 추가, 비용 발생 작업은 구현 전에 별도 승인 또는 명확한 안전 설계가 필요하다.

## Notes

- 사용자의 핵심 피드백: "CMS는 수정이 핵심"이다. Control Center가 상태판으로만 남으면 목적을 충족하지 못한다.
- 시작점은 큰 CMS가 아니라 SAM이 이미 수동으로 처리하는 작은 수정 루프를 제품화하는 것이다.
