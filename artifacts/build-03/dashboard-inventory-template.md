# Dashboard Inventory Template — build-03

> Control Center / Ops CMS 첫 단계: 현재 대시보드/정적 페이지 현황 파악  
> `[FILL_LOCAL]` 항목은 로컬 Claude Code가 실제 파일·설정을 보고 채운다.

## 대시보드 인벤토리

| 항목 | Travel Dashboard | Status Dashboard | Infinity Dashboard | Card News Library | Wedding/Static Page |
|------|-----------------|-----------------|-------------------|-------------------|---------------------|
| **표시 이름** | Travel Dashboard | Status Dashboard | Infinity Dashboard | Card Library | Wedding Page |
| **공개 URL** | [FILL_LOCAL] | [FILL_LOCAL] | [FILL_LOCAL] | [FILL_LOCAL] | [FILL_LOCAL] |
| **로컬 경로** | [FILL_LOCAL] | [FILL_LOCAL] | [FILL_LOCAL] | [FILL_LOCAL] | [FILL_LOCAL] |
| **레포지토리** | [FILL_LOCAL] | [FILL_LOCAL] | [FILL_LOCAL] | [FILL_LOCAL] | [FILL_LOCAL] |
| **소스 데이터** | [FILL_LOCAL] | [FILL_LOCAL] | [FILL_LOCAL] | [FILL_LOCAL] | [FILL_LOCAL] |
| **빌드 커맨드** | [FILL_LOCAL] | [FILL_LOCAL] | [FILL_LOCAL] | [FILL_LOCAL] | [FILL_LOCAL] |
| **배포 방식** | [FILL_LOCAL] | [FILL_LOCAL] | [FILL_LOCAL] | [FILL_LOCAL] | [FILL_LOCAL] |
| **검증 방법** | [FILL_LOCAL] | [FILL_LOCAL] | [FILL_LOCAL] | [FILL_LOCAL] | [FILL_LOCAL] |
| **자주 하는 수정** | [FILL_LOCAL] | [FILL_LOCAL] | [FILL_LOCAL] | [FILL_LOCAL] | [FILL_LOCAL] |
| **위험/승인 경계** | L1 safe | L1 safe | L2 (운영 상태) | L1 safe | L2 (공개 페이지) |
| **마지막 배포** | [FILL_LOCAL] | [FILL_LOCAL] | [FILL_LOCAL] | [FILL_LOCAL] | [FILL_LOCAL] |

## 로컬 실행 지시

```
Infinity Intent: build-03 Dashboard Inventory Fill
Mode: execute_local
Goal: 위 테이블의 [FILL_LOCAL] 항목을 실제 값으로 채워서
      artifacts/build-03/dashboard-inventory.md 로 저장

찾아야 할 경로:
- ~/dev/ 또는 ~/repos/ 하위에서 travel, status, infinity, card-library, wedding 관련 디렉토리
- 각 레포의 package.json, Makefile, Dockerfile, .github/workflows에서 빌드/배포 커맨드
- DNS / GitHub Pages / Kubernetes 설정에서 공개 URL

각 항목에 대해:
1. local path 확인
2. public URL 확인 (curl -I 또는 브라우저)
3. build command 확인
4. deploy mechanism 확인 (GitHub Actions / ArgoCD / manual push)
5. 소스 데이터 파일 경로 확인

결과: artifacts/build-03/dashboard-inventory.md (완성된 버전)
Allowed: L0/L1 only — 실제 배포·프로덕션 변경 금지
```

## 다음 단계

인벤토리 완성 후:
1. MVP 정보구조 정의: registry view / editor panel / deploy status board / change log
2. 반복 수정이 가장 잦은 대시보드 1개 선정 → Control Center 첫 내부 페이지 대상
3. 구현 계획 작성 (프로덕션 변경 없이 테스트 가능한 방식)
