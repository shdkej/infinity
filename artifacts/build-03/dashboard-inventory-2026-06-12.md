# artifacts/build-03: Dashboard Inventory Skeleton
> Intent: build-03 Control Center / Ops CMS
> Created: 2026-06-12 by Heartbeat Agent (Cloud pass)
> Status: 스켈레톤 — [로컬검증필요] 항목은 로컬 에이전트가 실제 값으로 채워야 함

---

## 인벤토리 방법론

각 대시보드/정적 페이지에 대해 아래 7개 필드를 수집한다:

| 필드 | 설명 |
|------|------|
| `public_url` | 공개 URL (없으면 내부 전용) |
| `local_path` | 로컬 파일 경로 또는 레포 루트 |
| `source_data` | 원장/데이터 파일 경로 |
| `build_cmd` | 빌드 명령 (없으면 정적) |
| `deploy_path` | 배포 경로 (GitHub Pages / ArgoCD / S3 / 수동) |
| `verify_method` | 배포 확인 방법 |
| `common_edits` | 반복되는 수정 작업 |
| `risk_boundary` | 변경 시 위험도 / 승인 필요 여부 |

---

## 1. Infinity Dashboard

- `display_name`: Infinity Dashboard
- `public_url`: [로컬검증필요] — `shdkej.github.io/infinity` 추정 (docs/index.html 존재)
- `local_path`: [로컬검증필요] — `~/dev/infinity` 또는 `/home/ubuntu/dev/infinity`
- `source_data`: `infinity/INTENTS.md`, `infinity/GATES.md`, `infinity/reports/`
- `build_cmd`: 없음 (정적 HTML — `docs/index.html`)
- `deploy_path`: GitHub Pages (`shdkej/infinity` → `docs/` branch)
- `verify_method`: `curl -sI https://shdkej.github.io/infinity/`
- `common_edits`:
  - INTENTS.md 업데이트
  - reports/ 추가
- `risk_boundary`: L1 — 커밋/push 후 자동 반영. 프로덕션 아님.

---

## 2. Travel Dashboard

- `display_name`: Travel Dashboard
- `public_url`: [로컬검증필요] — AWS S3/CloudFront 또는 GitHub Pages 추정
- `local_path`: [로컬검증필요]
- `source_data`: [로컬검증필요] — 여행 일정/지출 데이터 파일
- `build_cmd`: [로컬검증필요]
- `deploy_path`: [로컬검증필요] — S3 또는 GitHub Pages
- `verify_method`: [로컬검증필요]
- `common_edits`:
  - 여행 일정 데이터 업데이트
  - 지출 항목 추가
- `risk_boundary`: [로컬검증필요] — 공개 URL 있으면 L2, 내부 전용이면 L1

---

## 3. Status Dashboard

- `display_name`: Status Dashboard
- `public_url`: [로컬검증필요] — `oracle.shdkej.com` 계열 또는 별도 도메인 추정
- `local_path`: [로컬검증필요]
- `source_data`: [로컬검증필요] — 서비스 상태 레지스트리
- `build_cmd`: [로컬검증필요]
- `deploy_path`: [로컬검증필요] — Kubernetes/ArgoCD 또는 GitHub Pages
- `verify_method`: [로컬검증필요]
- `common_edits`:
  - 서비스 상태 업데이트
  - 신규 서비스 추가
- `risk_boundary`: [로컬검증필요]

---

## 4. Card News Library (카드라이브러리)

- `display_name`: Card News Library
- `public_url`: [로컬검증필요]
- `local_path`: [로컬검증필요]
- `source_data`: [로컬검증필요] — 카드 아이템 JSON 또는 MD 파일들
- `build_cmd`: [로컬검증필요]
- `deploy_path`: [로컬검증필요]
- `verify_method`: [로컬검증필요]
- `common_edits`:
  - 새 카드 콘텐츠 추가
  - 카드 메타데이터 수정
- `risk_boundary`: [로컬검증필요]

---

## 5. 결혼/가족 초대장 정적 페이지

- `display_name`: Wedding / Family Static Page
- `public_url`: [로컬검증필요] — 별도 도메인 또는 GitHub Pages
- `local_path`: [로컬검증필요]
- `source_data`: 없음 (정적 HTML/CSS)
- `build_cmd`: 없음 (정적)
- `deploy_path`: [로컬검증필요] — GitHub Pages 또는 S3
- `verify_method`: [로컬검증필요]
- `common_edits`:
  - 날짜/장소 정보 업데이트
  - 텍스트 수정
- `risk_boundary`: L1 — 공개 페이지지만 외부 알림 없는 수정이면 자율 가능

---

## 로컬 검증 체크리스트

다음 명령으로 실제 값을 채울 수 있다:

```bash
# GitHub Pages 확인
curl -sI https://shdkej.github.io/infinity/

# AWS S3 버킷 목록 (로컬 자격증명 필요)
aws s3 ls

# ArgoCD 앱 목록 (Kubernetes 접근 필요)
kubectl get applications -n argocd

# 로컬 레포 목록
ls ~/dev/
ls /home/ubuntu/dev/

# 최근 배포 이력 확인
git -C ~/dev/<repo> log --oneline -5
```

---

## 다음 Action

로컬 에이전트 실행 프롬프트:

```
Intent: build-03 Control Center / Ops CMS
Mode: verify_local
Goal: artifacts/build-03/dashboard-inventory-2026-06-12.md에서 [로컬검증필요] 항목을 실제 값으로 채운다.
Allowed: L0/L1 (읽기, 로컬 파일 확인, curl, git log)
Forbidden: 새 배포, 프로덕션 변경
Verification: 각 항목에 실제 URL/경로가 채워지면 완료
Report back: reports/build-03/2026-06-12T{timestamp}Z-local.html
```
