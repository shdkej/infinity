# Dashboard Inventory v1 — Control Center / Ops CMS

> 생성: 2026-06-12T06:00Z | Heartbeat 클라우드 조사 기반 초안
> **미확인 항목은 로컬에서 채워야 한다.**

## 목적

현재 운영 중인 대시보드/정적 페이지의 원장·데이터·배포 경로를 한곳에 정리하여
Control Center MVP 설계의 입력 데이터로 사용한다.

---

## 1. Infinity Kanban Dashboard

| 항목 | 값 |
|------|---|
| 공개 URL | `https://infinity.oracle.shdkej.com` |
| 로컬 경로 | `space repo: apps/infinity-kanban/` |
| 레포 | space (private, ArgoCD 관리) |
| 원장 데이터 | shdkej/infinity `INTENTS.md`, `GATES.md` (GitHub raw fetch) |
| 빌드 명령 | 없음 (ConfigMap 정적 HTML, nginx:alpine) |
| 배포 경로 | ArgoCD auto sync (prune, selfHeal) |
| 검증 방법 | HTTP 200, TLS Ready, 칸반 4단 렌더 확인 |
| 일반 편집 작업 | INTENTS.md / GATES.md push → 자동 반영 |
| 리스크 | INTENTS.md 포맷 변화 시 클라이언트 파서 오류 가능 |

---

## 2. Infinity GitHub Pages

| 항목 | 값 |
|------|---|
| 공개 URL | `https://shdkej.github.io/infinity/` (확인 필요) |
| 로컬 경로 | `shdkej/infinity: docs/index.html` |
| 레포 | shdkej/infinity (GitHub Pages, docs/) |
| 원장 데이터 | 동일 레포 `reports/`, `intents/archive/` (GitHub raw fetch 추정) |
| 빌드 명령 | 없음 (정적 HTML) |
| 배포 경로 | GitHub Pages (docs/ 브랜치) |
| 검증 방법 | URL HTTP 200 확인 |
| 일반 편집 작업 | docs/index.html 수정 → push → 자동 배포 |
| 리스크 | 로컬 미확인 |

---

## 3. Agent Wiki

| 항목 | 값 |
|------|---|
| 공개 URL | `https://shdkej.github.io/agent-wiki/` |
| 로컬 경로 | `/home/ubuntu/.openclaw/workspace/` (추정) |
| 레포 | shdkej/agent-wiki |
| 원장 데이터 | `diary/` 디렉토리 (MkDocs Material, `docs_dir: diary`) |
| 빌드 명령 | GitHub Actions (push → 자동 빌드) |
| 배포 경로 | GitHub Pages (GitHub Actions) |
| 검증 방법 | URL HTTP 200, sidebar 렌더 확인 |
| 일반 편집 작업 | diary-sync.sh push → 자동 트리거 |
| 리스크 | GitHub Pages 활성화는 웹 UI 필수 (L3) |

---

## 4. Virtue App

| 항목 | 값 |
|------|---|
| 공개 URL | `https://virtue.oracle.shdkej.com` |
| 로컬 경로 | `/home/ubuntu/dev/virtue-rebirth-app` |
| 레포 | (private, K8s deployment) |
| 원장 데이터 | React/Next.js 앱 (소스 코드) |
| 빌드 명령 | 로컬 확인 필요 |
| 배포 경로 | Kubernetes `deployment/virtue-rebirth`, rollout restart |
| 검증 방법 | HTTP 200, 기능 확인 |
| 일반 편집 작업 | 코드 수정 → 빌드 → push → K8s rollout |
| 리스크 | 프로덕션 배포 (L2/L3) |

---

## 5. Travel Dashboard ⚠️ 미확인

| 항목 | 값 |
|------|---|
| 공개 URL | **로컬 확인 필요** |
| 로컬 경로 | **로컬 확인 필요** |
| 레포 | **로컬 확인 필요** |
| 원장 데이터 | 여행 일정/지출 데이터 (경로 미확인) |
| 빌드 명령 | **로컬 확인 필요** |
| 배포 경로 | **로컬 확인 필요** |
| 검증 방법 | **로컬 확인 필요** |
| 일반 편집 작업 | **로컬 확인 필요** |
| 리스크 | 미확인 |

---

## 6. Status Dashboard ⚠️ 미확인

| 항목 | 값 |
|------|---|
| 공개 URL | **로컬 확인 필요** |
| 로컬 경로 | **로컬 확인 필요** |
| 레포 | **로컬 확인 필요** |
| 원장 데이터 | Status 레지스트리 데이터 (경로 미확인) |
| 빌드 명령 | **로컬 확인 필요** |
| 배포 경로 | **로컬 확인 필요** |
| 검증 방법 | **로컬 확인 필요** |
| 일반 편집 작업 | **로컬 확인 필요** |
| 리스크 | 미확인 |

---

## 7. Card News Library ⚠️ 미확인

| 항목 | 값 |
|------|---|
| 공개 URL | **로컬 확인 필요** |
| 로컬 경로 | **로컬 확인 필요** |
| 레포 | **로컬 확인 필요** |
| 원장 데이터 | Card Library 아이템 데이터 (경로 미확인) |
| 빌드 명령 | **로컬 확인 필요** |
| 배포 경로 | **로컬 확인 필요** |
| 검증 방법 | **로컬 확인 필요** |
| 일반 편집 작업 | **로컬 확인 필요** |
| 리스크 | 미확인 |

---

## 8. Family Wedding/Static Invitation Page ⚠️ 미확인

| 항목 | 값 |
|------|---|
| 공개 URL | **로컬 확인 필요** |
| 로컬 경로 | **로컬 확인 필요** |
| 레포 | **로컬 확인 필요** |
| 원장 데이터 | 정적 초대장 데이터 (경로 미확인) |
| 빌드 명령 | **로컬 확인 필요** |
| 배포 경로 | AWS S3 / GitHub Pages 중 하나 추정 |
| 검증 방법 | **로컬 확인 필요** |
| 일반 편집 작업 | **로컬 확인 필요** |
| 리스크 | 미확인 |

---

## 요약

| 이름 | URL 상태 | 로컬 경로 상태 | 배포 방식 |
|------|----------|----------------|----------|
| Infinity Kanban | ✅ 확인 | ✅ space repo | K8s/ArgoCD |
| Infinity GitHub Pages | ⚠️ 추정 | ✅ docs/ | GitHub Pages |
| Agent Wiki | ✅ 확인 | ⚠️ 추정 | GitHub Pages/Actions |
| Virtue App | ✅ 확인 | ✅ 확인 | K8s rollout |
| Travel Dashboard | ❌ 미확인 | ❌ 미확인 | 미확인 |
| Status Dashboard | ❌ 미확인 | ❌ 미확인 | 미확인 |
| Card News Library | ❌ 미확인 | ❌ 미확인 | 미확인 |
| Wedding/Static | ❌ 미확인 | ❌ 미확인 | 미확인 |

**다음 액션:** 로컬에서 미확인 4개 항목을 채우고, 이 inventory를 기반으로 MVP 정보구조 설계 진행.
