# build-06: Control Center Draft Edit MVP

- id: build-06
- status: active
- projects: [infinity, personal-ops, infrastructure]
- task_type: implementation
- topics: [dashboard, cms, editing, diff-preview, deploy]
- owner: SAM
- display_name: Control Center Draft Edit MVP
- created_at: 2026-06-12T09:25Z
- source: follow-up from build-05 archive and user process feedback in Telegram direct chat
- predecessor: build-05

## User Request

사용자가 "Cms 만들던건 홀딩인가? 이거 마지막 5번이 아카이브 되어있는데 이어나가는 프로세스가 스킬에 있나? 아니면 내가 요청해야하는건가?"라고 물었다.

확인 결과 build-05는 실제 CMS 구현이 아니라 `editableSurfaces` 스키마와 diff preview 설계만 완료하고 Archive로 닫힌 상태였다. 사용자의 기대는 "CMS 수정 기능이 실제로 이어져야 한다"는 것이므로, 다음 구현 단계를 별도 active intent로 명시한다.

## Purpose

build-04의 read-only Control Center와 build-05의 schema/diff-preview 설계를 이어서, 사용자가 공개 Control Center 안에서 "수정 대상 필드 선택 → 새 문구 입력 → diff preview 확인"까지 볼 수 있는 첫 draft edit MVP를 만든다.

## Scope

### Include

- Control Center UI에 `Editable CMS` 또는 `Draft Editor` 섹션 추가.
- build-05의 `editableSurfaces` 설계를 정적 데이터로 바인딩.
- 첫 대상은 Family Wedding 안내장의 `NOTICE` 필드.
- 사용자가 새 문구를 입력하면 정본 파일을 쓰지 않고 unified diff preview를 보여준다.
- change log 모델에는 최근 수동 변경 예시(커밋/배포/검증 URL)를 read-only로 표시한다.
- 기존 Status 정적 사이트 배포 레인을 사용해 공개 URL에서 확인 가능하게 한다.

### Exclude For This MVP

- write API.
- auth / permission 변경.
- GitHub/AWS token 서버 기능.
- production deploy button.
- 자동 commit/push.
- Terraform/AWS 신규 리소스.
- 비용 발생 작업, force-push/destructive action, secret 편집.

## Success Criteria

- [ ] 공개 Control Center URL에서 editable target과 field 목록이 보인다.
- [ ] Family Wedding `NOTICE` 필드에 새 문구를 입력하면 diff preview가 즉시 나온다.
- [ ] preview 흐름이 정본 파일을 변경하지 않는다는 경계가 UI에 명확하다.
- [ ] 기존 Control Center registry/status 내용은 깨지지 않는다.
- [ ] 배포 후 공개 URL에서 `Draft Editor`, `Family Wedding`, `diff preview` 같은 확인 문자열이 보인다.

## Approval Boundary

이 intent는 기존 정적 Control Center 페이지에 draft-only UI를 추가하는 L2 구현으로 진행 가능하다. 정본 파일을 쓰거나 배포 버튼을 실행하는 기능은 만들지 않는다.

실제 수정 저장, commit/push 자동화, GitHub Pages/AWS 배포 버튼, 인증/권한/토큰 서버 기능은 다음 intent에서 별도 승인 또는 안전 설계가 필요하다.

## Notes

- build-05가 Archive로 닫힌 것은 "CMS 완성"이 아니라 "첫 설계 산출 완료"다.
- 이번 intent는 사용자가 다시 요청하지 않아도 이어지는 구현 단계를 원장에 남기기 위한 연결 고리다.
