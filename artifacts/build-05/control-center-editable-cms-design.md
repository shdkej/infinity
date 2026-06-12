# build-05: Control Center Editable CMS — Editable Surface Schema & Draft Edit/Diff Preview 설계

- intent: build-05
- status: design (doc-only, 첫 안전 액션)
- created_at: 2026-06-12T07:30Z
- source_intent: build-04 (read-only Control Center MVP)
- scope: editable surface schema + field-level draft edit/diff preview 설계 (Family Wedding / Travel 등 작은 정적 표면)
- approval_level: L0/L1/L2 설계만. write API / auth / production deploy / token 서버 기능 / Terraform·AWS 리소스는 **본 문서에서 경계 텍스트로만 다룬다**.

## 1. 목적과 한 줄 요약

build-04의 Control Center는 상태판(read-only)이다. 사용자 피드백 **"CMS는 수정이 핵심"**을 충족하려면,
SAM이 이미 수동으로 돌리는 작은 수정 루프(예: Family Wedding 안내장 NOTICE 문구 교체)를
**스키마로 등록 → 필드 단위 입력 → diff preview → 검증 → 커밋 초안 → (승인형) 배포/검증 기록**의
재현 가능한 흐름으로 제품화하는 것이 첫 단계다.

이 문서는 그중 **승인 없이 진행 가능한 부분**, 즉 (a) editable surface 스키마와 (b) draft edit/diff preview 설계만 다룬다.
실제 쓰기 실행은 설계하지 않고 **경계로만 표시**한다.

## 2. 안전 경계 (이 문서가 설계하지 않는 것)

아래 항목은 **설계 경계(design boundary) 텍스트**로만 언급하며, 본 문서에서 구현·코드·실행 절차를 만들지 않는다.

| 경계 항목 | 본 문서에서의 취급 | 승인 단계 |
|-----------|--------------------|-----------|
| write API (정본 파일 직접 쓰기) | 인터페이스 형태만 named placeholder, 미구현 | 별도 승인 |
| auth / permission (다중 사용자 권한) | 단일 운영자(SAM) 가정, roles 미설계 | 별도 승인 |
| production deploy button | UI에서 draft와 분리된 approval-needed 자리로만 표시 | 별도 승인 |
| GitHub / AWS token 서버 function | 토큰을 쓰는 서버 기능 미설계, 수동 절차를 change-log로 기록만 | 별도 승인 |
| Terraform / AWS resource | 신규 리소스 0, 기존 Status 배포 레인 재사용 전제 | 별도 승인 |
| 비용 발생 / destructive / force-push | 없음. diff preview는 read-only 산출 | 별도 승인 |
| 외부 메시지 발송 / 공개 게시 | 없음 | 별도 승인 |
| 비밀값(secret) 편집 | editable field에서 원천 제외 | 원천 제외 |

원칙: **read-only view / draft edit / publish 를 UI와 데이터 모델에서 분리한다.** publish는 항상 승인 경계 뒤에 둔다.

## 3. editableSurfaces 스키마

Control Center가 읽는 선언적 registry. JSON/JS 객체로 표현하되, 본 단계에서는 **데이터 형상 정의**까지만 한다.

```jsonc
// editableSurfaces.schema (형상 정의 — 구현 아님)
{
  "id": "string",                  // 표면 고유 id (예: "family-wedding")
  "displayName": "string",         // Control Center 표시명
  "projects": ["string"],          // ARTIFACT_RULES project 태그와 정합
  "canonicalFile": "string",       // 정본 파일 경로 (소스 리포 기준, 표시용)
  "publicUrl": "string",           // 공개 검증 대상 URL
  "previewMode": "static-page",    // 첫 패스는 작은 정적 페이지만
  "editableFields": [
    {
      "key": "string",             // 필드 id (예: "notice")
      "label": "string",           // 사람이 읽는 이름
      "anchor": "string",          // 정본 파일에서 필드를 찾는 마커/주석/셀렉터
      "type": "text | richtext-line | meta",
      "maxLen": 0,                 // 검증용 최대 길이
      "multiline": false,
      "validation": ["non-empty", "no-secret-pattern", "len<=maxLen"],
      "example": "string"
    }
  ],
  "preview": {
    "buildCmd": "string|null",     // 정적 렌더 확인 명령 (표시용, 자동 실행 아님)
    "diff": "unified",             // diff preview 형식
    "write": "none"                // ★ draft 단계에서는 정본 파일에 쓰지 않음
  },
  "publish": {                     // ★ 전부 approval-needed 경계
    "approvalLevel": "L2",
    "commitMessageDraft": "template-string",
    "deployCmd": "approval-needed", // 실제 배포 명령은 placeholder, 미실행
    "verifyTarget": "string"        // 배포 후 확인할 공개 URL / 문자열
  },
  "changeLog": [                   // 4절 모델 참조
    { "field": "", "oldHash": "", "newHash": "", "commit": "", "deployRun": "", "url": "", "verifiedAt": "" }
  ]
}
```

설계 의도:

- `editableFields[].anchor`로 **필드 → 파일 내 위치**를 결정적으로 매핑한다. 전체 파일 재작성이 아니라 좁은 영역만 다룬다.
- `preview.write: "none"`이 핵심 안전 장치다. draft 단계에서 정본 파일은 절대 변경되지 않는다.
- `publish.*`는 전부 `approval-needed` placeholder로 두어, 스키마를 봐도 자동 배포가 일어날 수 없게 한다.

## 4. 첫 editable target — Family Wedding 안내장 (예시 인스턴스)

작고 검증 쉬운 정적 페이지를 1차 대상으로 삼는다. (필드 값/경로는 설계 예시이며, 정본 연결은 별도 단계.)

```jsonc
{
  "id": "family-wedding",
  "displayName": "Family Wedding 안내장",
  "projects": ["personal-ops"],
  "canonicalFile": "(source repo)/family-wedding/index.html",
  "publicUrl": "https://.../family-wedding/",
  "previewMode": "static-page",
  "editableFields": [
    { "key": "notice",      "label": "공지 문구(NOTICE)", "anchor": "<!-- NOTICE -->",
      "type": "text",          "maxLen": 120, "multiline": false,
      "validation": ["non-empty", "len<=maxLen"], "example": "주차 공간이 협소하니 대중교통 이용 부탁드립니다." },
    { "key": "body_intro",  "label": "안내 본문 도입",   "anchor": "<!-- BODY:INTRO -->",
      "type": "richtext-line", "maxLen": 300, "multiline": true,
      "validation": ["non-empty", "len<=maxLen"], "example": "저희 두 사람의 시작을 함께해 주세요." },
    { "key": "og_description", "label": "OG description (공유 미리보기)", "anchor": "meta[property='og:description']",
      "type": "meta",          "maxLen": 160, "multiline": false,
      "validation": ["non-empty", "len<=maxLen"], "example": "2026년 가을, 가족 결혼식에 초대합니다." }
  ],
  "preview": { "buildCmd": null, "diff": "unified", "write": "none" },
  "publish": {
    "approvalLevel": "L2",
    "commitMessageDraft": "chore(family-wedding): update {field} notice text",
    "deployCmd": "approval-needed",
    "verifyTarget": "https://.../family-wedding/ 에서 갱신 문구 + HTTP 200"
  },
  "changeLog": []
}
```

Travel Dashboard는 동일 스키마로 `travel-ops` 표면을 추가하면 된다(반복 수정 필드: 일정 요약 라인, 알림 배너 등). 본 단계는 스키마 일반성만 확인한다.

## 5. Draft Edit / Diff Preview 흐름 (read-only 산출)

```text
[입력]            [위치결정]            [검증]              [미리보기]           [초안]                 [경계]
field=notice  →  anchor로 정본의   →  validation 규칙  →  unified diff 생성  →  commit message 초안  →  publish/deploy
value="..."      해당 라인 탐색       (len/non-empty/      (정본은 미변경,        (changeLog row 후보)    ▶ approval-needed
                                      no-secret)           메모리상 비교만)                              (자동 실행 안 함)
```

단계별 설계:

1. **위치결정**: `anchor`(주석 마커 또는 셀렉터)로 정본 파일에서 바꿀 한 줄/한 블록을 찾는다. 못 찾으면 에러로 멈춘다(전체 재작성 금지).
2. **검증**: `validation` 규칙 통과 못 하면 diff를 만들지 않는다. `no-secret-pattern`으로 비밀값 유입을 원천 차단한다.
3. **diff preview**: "현재 라인 → 새 라인"을 **unified diff 텍스트로만** 산출한다. `preview.write: "none"` — 정본 파일은 디스크에서 바뀌지 않는다. 이것이 draft와 publish를 가르는 경계다.
4. **commit message 초안**: `commitMessageDraft` 템플릿에 `{field}`를 채워 제안만 한다. 실제 커밋/푸시는 하지 않는다.
5. **publish 경계**: deploy/verify는 SAM이 수동으로 수행하던 절차를 **change-log model로 기록**하는 자리로만 둔다. 버튼/명령은 approval-needed placeholder.

## 6. Change Log 모델

수정 이력을 commit SHA / deploy run / public URL 검증과 연결해 Control Center에서 추적 가능하게 한다.

| 컬럼 | 의미 | 채워지는 시점 |
|------|------|---------------|
| `field` | 어떤 editable field | draft 생성 시 |
| `oldHash` / `newHash` | 변경 전후 값 해시 | diff preview 시 |
| `commit` | 반영 커밋 SHA | (승인 후) publish 시 |
| `deployRun` | 배포 실행 식별자 | (승인 후) publish 시 |
| `url` | 공개 검증 URL | publish 시 |
| `verifiedAt` | 공개 URL 검증 시각 | verify 시 |

draft 단계에서는 `field/oldHash/newHash`까지만 채워지고, `commit` 이후 컬럼은 **승인 경계 뒤에서만** 채워진다.

## 7. 성공 기준 매핑 (build-05 intent)

| Intent 성공 기준 | 본 설계의 충족 방식 | 상태 |
|------------------|---------------------|------|
| 최소 1개 표면의 editable fields 표시 | Family Wedding 3필드 인스턴스(4절) | 설계 완료 |
| 입력값이 어떤 파일/라인/필드를 바꿀지 diff preview | anchor 기반 unified diff(5절) | 설계 완료 |
| publish/deploy가 read-only/draft와 분리·승인 경계 명확 | `preview.write:none` + `publish:approval-needed`(2·3·5절) | 설계 완료 |
| 변경 이력이 commit/deploy/URL과 연결 | change-log 모델(6절) | 설계 완료 |
| 사용자가 "여기서 수정 시작 가능"하다고 이해 | 표면 registry + 필드 + diff 흐름 가시화 | 설계 완료 |

## 8. 다음 단계 후보 (전부 별도 승인/단계)

1. Control Center read-only UI에 `editableSurfaces`를 바인딩해 필드 + diff preview를 **읽기 전용으로** 렌더.
2. diff preview 생성기(정본 미변경, unified diff만 산출)를 작은 스크립트로 구현 — write API 아님.
3. Family Wedding NOTICE 1필드를 실제 수동 수정 루프 2–3회 돌려 change-log 모델 검증.
4. 안정화 후, production deploy 버튼/토큰 서버 기능/배포 자동화는 **승인형 별도 intent**로 분리.
