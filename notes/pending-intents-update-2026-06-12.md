# INTENTS.md 로컬 업데이트 필요 (2026-06-12T0600Z)

이번 Heartbeat에서 INTENTS.md 업데이트를 자동화하지 못했습니다 (파일 크기 64KB 초과로 클라우드 환경에서 인라인 파라미터 업데이트 불가).

로컬에서 아래 두 가지 변경을 INTENTS.md에 적용해주세요:

## 1. Inbox 섹션 - build-03 제거

**찾기 (제거할 내용):**
```
<!-- build-03 inbox 2026-06-11T23:03Z → intents/inbox/build-03.md [display: Control Center / Ops CMS; ...
```

**교체:**
```
<!-- build-03 promoted to Active 2026-06-12T0600Z -->
```

## 2. Active 섹션 - build-03 추가

naver-shopping-01 주석 바로 다음 줄에 추가:

```
<!-- build-03 active 2026-06-12T0600Z → intents/active/build-03.md [display: Control Center / Ops CMS; projects: infinity,personal-ops,infrastructure; type: design; topics: dashboard,workflow,automation; status: active-inventory-research] (Inbox에서 승격. 대시보드/정적페이지 운영 CMS 설계 시작. 2026-06-12 이번 Heartbeat: 대시보드 inventory 초안 아티팩트 작성(cloud prepare 완료). 산출물 artifacts/build-03/dashboard-inventory-draft.md. 다음 액션: 로컬에서 실제 경로/URL 확인 후 inventory 완성, MVP 정보구조 설계.) -->
```

## 완료된 산출물

- `intents/active/build-03.md` - Active intent 파일
- `artifacts/build-03/dashboard-inventory-draft.md` - 대시보드 inventory 초안
- `reports/build-03/2026-06-12T0600Z.html` - build-03 리포트
- `reports/naver-shopping-01/2026-06-12T0600Z.html` - naver-shopping-01 소싱 스크린 리포트

이 파일은 INTENTS.md 업데이트 완료 후 삭제해도 됩니다.
