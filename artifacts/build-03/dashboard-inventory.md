# Dashboard & Static Pages Inventory

> build-03: Control Center / Ops CMS — 첫 번째 액션
> 작성일: 2026-06-12 | Mode: cloud prepare (L0)
> 확인 방법: Cloud에서 확인한 항목 ✓, 로컬 확인 필요 항목 [확인 필요]

---

## 1. Infinity Dashboard (Kanban)

| 항목 | 값 |
|------|----|
| 표시 이름 | Infinity Dashboard |
| 공개 URL | `https://infinity.oracle.shdkej.com` ✓ |
| Repo | shdkej/space (`apps/infinity-kanban/`) ✓ |
| 소스 데이터 | `shdkej/infinity/INTENTS.md`, `shdkej/infinity/GATES.md` (런타임 fetch) ✓ |
| 빌드 방법 | 빌드 없음 — nginx:alpine + ConfigMap 정적 HTML ✓ |
| 배포 방법 | space repo push → ArgoCD auto-sync → K8s ✓ |
| 검증 방법 | `curl -s https://infinity.oracle.shdkej.com` HTTP 200 확인 ✓ |
| 일반 수정 | INTENTS.md / GATES.md 변경 시 자동 반영 (별도 배포 불필요) ✓ |
| 위험/승인 경계 | L1: INTENTS.md·GATES.md 수정. L2: ConfigMap·ingress·ArgoCD 구조 변경 |

**메모**: 런타임 GitHub raw URL fetch 구조이므로 INTENTS.md 포맷 변경 시 클라이언트 파서에 영향을 줄 수 있음. detail modal 지원.

---

## 2. Agent Wiki

| 항목 | 값 |
|------|----|
| 표시 이름 | Agent Wiki |
| 공개 URL | `https://shdkej.github.io/agent-wiki/` ✓ |
| Repo | shdkej/agent-wiki (`diary/*.md`) ✓ |
| 소스 데이터 | `diary/YYYY-MM-DD.md` (30분마다 자동 커밋) ✓ |
| 빌드 방법 | MkDocs-Material (`mkdocs.yml`, `docs_dir: diary`) ✓ |
| 배포 방법 | GitHub Actions (push → build → GitHub Pages) ✓ |
| 검증 방법 | `https://shdkej.github.io/agent-wiki/` 접속 확인 ✓ |
| 일반 수정 | diary/*.md 추가/수정 → push 시 자동 반영 ✓ |
| 위험/승인 경계 | L1: diary 파일 수정. L2: mkdocs.yml·GitHub Actions 변경 |

---

## 3. Virtue App

| 항목 | 값 |
|------|----|
| 표시 이름 | Virtue |
| 공개 URL | `https://virtue.oracle.shdkej.com` ✓ |
| Repo | 로컬 `/home/ubuntu/dev/virtue-rebirth-app` [확인 필요: GitHub repo name] |
| 소스 데이터 | 앱 코드 (React/Next.js 등) |
| 빌드 방법 | 앱 빌드 (로컬) [확인 필요] |
| 배포 방법 | K8s `deployment/virtue-rebirth` rollout restart ✓ |
| 검증 방법 | `https://virtue.oracle.shdkej.com` HTTP 200 ✓ |
| 일반 수정 | 앱 코드 수정 → 빌드 → K8s rollout |
| 위험/승인 경계 | L2: 프로덕션 배포 (사용자 승인 필요) |

**메모**: 앱(동적 서비스)이므로 CMS 1차 MVP에서는 배포 상태 모니터링 항목으로만 포함. 편집/빌드는 CMS 범위 밖.

---

## 4. Travel Dashboard

| 항목 | 값 |
|------|----|
| 표시 이름 | Travel Dashboard |
| 공개 URL | [확인 필요] |
| Repo | [확인 필요] |
| 소스 데이터 | 여행 일정·경비 데이터 파일 [확인 필요] |
| 빌드 방법 | [확인 필요] |
| 배포 방법 | [확인 필요] |
| 검증 방법 | [확인 필요] |
| 일반 수정 | 여행 데이터 파일 수정 [확인 필요] |
| 위험/승인 경계 | [확인 필요] |

**로컬 확인 필요**: 실제 URL, 레포, 소스 데이터 경로.

---

## 5. Status Dashboard

| 항목 | 값 |
|------|----|
| 표시 이름 | Status Dashboard |
| 공개 URL | [확인 필요] |
| Repo | [확인 필요] |
| 소스 데이터 | 상태 레지스트리 파일 [확인 필요] |
| 빌드 방법 | [확인 필요] |
| 배포 방법 | [확인 필요] |
| 검증 방법 | [확인 필요] |
| 일반 수정 | 상태 데이터 수정 [확인 필요] |
| 위험/승인 경계 | [확인 필요] |

**로컬 확인 필요**: 실제 URL, 레포, 소스 데이터 경로.

---

## 6. Card News Library

| 항목 | 값 |
|------|----|
| 표시 이름 | Card News Library |
| 공개 URL | [확인 필요] |
| Repo | [확인 필요] |
| 소스 데이터 | 카드 뉴스 콘텐츠 파일 [확인 필요] |
| 빌드 방법 | [확인 필요] |
| 배포 방법 | [확인 필요] |
| 검증 방법 | [확인 필요] |
| 일반 수정 | 카드 데이터 추가/수정 [확인 필요] |
| 위험/승인 경계 | [확인 필요] |

**로컬 확인 필요**: 실제 URL, 레포, 소스 데이터 경로.

---

## 7. Family/Wedding Static Page

| 항목 | 값 |
|------|----|
| 표시 이름 | Family/Wedding Invitation Page |
| 공개 URL | [확인 필요] |
| Repo | [확인 필요] |
| 소스 데이터 | 정적 HTML/데이터 [확인 필요] |
| 빌드 방법 | 정적 HTML 직접 (빌드 없음) [확인 필요] |
| 배포 방법 | [확인 필요] |
| 검증 방법 | URL 접속 확인 [확인 필요] |
| 일반 수정 | HTML 직접 편집 [확인 필요] |
| 위험/승인 경계 | [확인 필요] |

---

## 인벤토리 요약 (2026-06-12 기준)

| # | 이름 | URL 확인 | 소스 데이터 확인 | 배포 방식 확인 | 비고 |
|---|------|----------|-----------------|---------------|------|
| 1 | Infinity Dashboard | ✓ | ✓ | ✓ ArgoCD | MVP CMS 적합 |
| 2 | Agent Wiki | ✓ | ✓ | ✓ GitHub Pages | MVP CMS 적합 |
| 3 | Virtue App | ✓ | △ | ✓ K8s | 모니터링 only |
| 4 | Travel Dashboard | [필요] | [필요] | [필요] | 로컬 확인 |
| 5 | Status Dashboard | [필요] | [필요] | [필요] | 로컬 확인 |
| 6 | Card News Library | [필요] | [필요] | [필요] | 로컬 확인 |
| 7 | Family/Wedding Page | [필요] | [필요] | [필요] | 로컬 확인 |

## 다음 단계

1. **로컬 확인 필요**: 항목 4-7의 URL, 레포, 배포 경로를 로컬에서 확인 후 이 인벤토리 업데이트
2. **MVP 정보구조 설계**: 확인된 항목 기준으로 Control Center의 첫 페이지 설계 (registry view + deploy status view)
3. **우선순위**: 항목 1(Infinity) + 2(Agent Wiki)만으로도 MVP Control Center 시범 운영 가능. 나머지는 로컬 확인 후 추가.

## 편집 분류 (초안)

| 편집 타입 | 대상 | 승인 경계 |
|-----------|------|----------|
| 소스 데이터 수정 | INTENTS.md, diary/*.md | L1 |
| 배포 상태 모니터링 | 모든 URL ping | L0 |
| 빌드·배포 트리거 | ArgoCD sync, GitHub Actions | L2 |
| 구조/인프라 변경 | ConfigMap, Ingress, Pages 설정 | L2-L3 |
