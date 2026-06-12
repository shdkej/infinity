# build-03: Dashboard & Static Page Inventory (초안)

> Cloud prepare 단계 초안 — 로컬 확인 없이 known context에서 추출.
> 로컬 실행 시 실제 경로/URL로 채우고 artifacts/build-03/dashboard-inventory.md로 저장.

생성: 2026-06-12T0600Z
방법: Infinity 리포지토리 컨텍스트, GATES.md, intents/archive 참조

---

## 1. Virtue App (virtue.oracle.shdkej.com)

| 항목 | 값 |
|------|-----|
| 공개 URL | https://virtue.oracle.shdkej.com |
| 유형 | Web App (Next.js 또는 React) |
| 로컬 경로 | `/home/ubuntu/dev/virtue-rebirth-app` (추정) |
| 레포 | 별도 private repo (추정) |
| 배포 방식 | Kubernetes / ArgoCD (deployment/virtue-rebirth rollout) |
| 데이터 소스 | TBD — 로컬 확인 필요 |
| 마지막 배포 | 2026-05-21 (master b28d01f, GATES.md 참조) |
| 공개 URL 확인 방법 | HTTP 200 체크 |
| 편집 대상 | 앱 소스코드 |
| 위험/승인 경계 | L2 (프로덕션 배포) |
| 상태 | ✅ 운영 중 |

---

## 2. Infinity Dashboard

| 항목 | 값 |
|------|-----|
| 공개 URL | TBD (oracle.shdkej.com 하위 또는 GitHub Pages) |
| 유형 | Static HTML / Agent dashboard |
| 로컬 경로 | `/home/ubuntu/.openclaw/workspace/` (추정) |
| 레포 | shdkej/infinity |
| 배포 방식 | GitHub Pages 또는 로컬 서버 |
| 데이터 소스 | INTENTS.md, reports/, GATES.md |
| 마지막 배포 | TBD |
| 편집 대상 | INTENTS.md, reports/ |
| 위험/승인 경계 | L1 (파일 수정 + push) |
| 상태 | ⚠️ 로컬 확인 필요 |

---

## 3. Travel Dashboard

| 항목 | 값 |
|------|-----|
| 공개 URL | TBD |
| 유형 | Static HTML (여행 일정/비용 표시) |
| 로컬 경로 | TBD — 로컬 확인 필요 |
| 레포 | TBD |
| 배포 방식 | TBD (GitHub Pages / oracle.shdkej.com) |
| 데이터 소스 | Travel itinerary/expense 파일 (TBD) |
| 마지막 배포 | TBD |
| 편집 대상 | 여행 일정 데이터 파일 |
| 위험/승인 경계 | L1 (파일 수정) |
| 상태 | ⚠️ 로컬 확인 필요 |

---

## 4. Status Dashboard / Personal Homepage

| 항목 | 값 |
|------|-----|
| 공개 URL | TBD (shdkej.com 또는 oracle.shdkej.com 추정) |
| 유형 | Static page |
| 로컬 경로 | TBD |
| 레포 | TBD |
| 배포 방식 | TBD |
| 데이터 소스 | 개인 상태 레지스트리 (TBD) |
| 마지막 배포 | TBD |
| 위험/승인 경계 | L1 |
| 상태 | ⚠️ 로컬 확인 필요 |

---

## 5. Card News Library

| 항목 | 값 |
|------|-----|
| 공개 URL | TBD |
| 유형 | Static HTML (카드뉴스 라이브러리) |
| 로컬 경로 | TBD |
| 레포 | TBD |
| 배포 방식 | GitHub Pages 추정 |
| 데이터 소스 | Card library items (TBD) |
| 마지막 배포 | TBD |
| 위험/승인 경계 | L1 |
| 상태 | ⚠️ 로컬 확인 필요 |

---

## 6. Agent Wiki (shdkej.github.io/agent-wiki)

| 항목 | 값 |
|------|-----|
| 공개 URL | https://shdkej.github.io/agent-wiki (Docsify) |
| 유형 | Docsify Static Docs |
| 로컬 경로 | TBD |
| 레포 | shdkej/agent-wiki |
| 배포 방식 | GitHub Pages (index.html, Docsify) |
| 데이터 소스 | Markdown 문서 |
| 마지막 배포 | 2026-04-20 (commit d52641c, GATES.md 참조) |
| 편집 대상 | .md 문서 파일 |
| 위험/승인 경계 | L1 (일반 push) |
| 상태 | ✅ 운영 중 (로컬 SSH 인증 필요) |

---

## 7. Wedding / Static Invitation Page

| 항목 | 값 |
|------|-----|
| 공개 URL | TBD |
| 유형 | Static HTML |
| 로컬 경로 | TBD |
| 레포 | TBD |
| 배포 방식 | TBD (GitHub Pages / AWS S3 추정) |
| 데이터 소스 | 정적 콘텐츠 |
| 마지막 배포 | TBD |
| 위험/승인 경계 | L1 |
| 상태 | ⚠️ 로컬 확인 필요 |

---

## 다음 단계 (로컬 확인 항목)

```bash
# 1. 로컬 경로 확인
ls ~/dev/
ls ~/

# 2. 공개 URL 확인
curl -I https://virtue.oracle.shdkej.com

# 3. GitHub Pages 레포 확인
# gh repo list shdkej --limit 30

# 4. 완성된 inventory 저장
# artifacts/build-03/dashboard-inventory.md
```

## Control Center MVP 정보구조 (초안)

```
Control Center
├── Registry (레지스트리)
│   ├── 이름 / 유형 / 상태
│   ├── 공개 URL + 마지막 HTTP 체크
│   └── 레포 + 로컬 경로 + 배포 방식
├── Data Sources (데이터 소스)
│   ├── 원장 파일 경로
│   └── 마지막 수정일
├── Deploy Log (배포 이력)
│   ├── 마지막 커밋 / 빌드 / 배포
│   └── 변경 내역
└── Quick Actions (빠른 액션)
    ├── [확인] 공개 URL 체크
    ├── [편집] 데이터 소스 열기
    └── [배포] push → verify (L2 승인 필요)
```
