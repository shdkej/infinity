# Dashboard Inventory Draft — build-03

생성: 2026-06-12T00:03Z (Heartbeat L0 Research)
상태: draft — local 현장 확인 필요

## 현재 파악된 대시보드 / 정적 페이지

| 이름 | Public URL | Local 경로 | 레포 | 배포 방법 | 소스 데이터 |
|------|-----------|------------|------|-----------|------------|
| Travel Dashboard | 확인 필요 | 확인 필요 | 확인 필요 | GitHub Pages/S3 추정 | 여행 일정·지출 데이터 |
| Status Dashboard | 확인 필요 | 확인 필요 | 확인 필요 | 확인 필요 | Status registry |
| Infinity Dashboard | 확인 필요 | shdkej/infinity | shdkej/infinity | GitHub Pages 추정 | INTENTS.md, reports/ |
| Card News Library | 확인 필요 | 확인 필요 | 확인 필요 | 확인 필요 | Card Library items |
| Family Wedding | 확인 필요 | 확인 필요 | 확인 필요 | GitHub Pages/S3 | Static HTML |

## Local 확인 필요 항목 (per 대시보드)

- [ ] Public URL
- [ ] 로컬 경로 및 레포
- [ ] 빌드 명령어
- [ ] 배포 명령어 / GitHub Actions / ArgoCD 경로
- [ ] 소스 데이터 파일 경로
- [ ] 일반적인 수정 작업 패턴
- [ ] 위험/승인 경계

## MVP 정보구조 초안

### Control Center 4가지 뷰

1. **Registry 뷰**: 모든 대시보드/페이지 목록 + URL + 상태 한눈에
2. **데이터 편집 뷰**: 소스 데이터 파일로 바로 이동/편집 링크
3. **배포 상태 뷰**: 마지막 커밋, 빌드, URL 확인 시각
4. **변경 로그 뷰**: 언제 무엇이 바뀌었는지

### 권한 경계 (설계안)

- L0: 읽기, registry 조회, 상태 확인
- L1: 소스 데이터 파일 수정, 커밋, 일반 push
- L2: 배포 트리거 (에이전트 자체 승인 가능 조건 충족 시)
- L3: 프로덕션 데이터 삭제, 인증/권한 변경

### 안전 원칙

- 수정→빌드→push→URL 확인 흐름에서 각 단계를 명확히 분리
- deploy-action은 data-edit과 분리된 별도 승인 단계
- 반복 수정만 버튼화 (매뉴얼 흐름이 안정된 후)

## 다음 단계

Local Claude에서:
1. `find ~/dev -name '*.json' -o -name '*.yaml'` 등으로 실제 경로 탐색
2. 각 대시보드의 빌드/배포 방식 확인
3. 이 draft의 빈 칸 채우기
4. 완성된 inventory를 바탕으로 MVP 정보구조 확정

## Source

- build-03.md inbox 원본 (2026-06-11T23:03Z)
- Heartbeat L0 research (2026-06-12T00:03Z)
