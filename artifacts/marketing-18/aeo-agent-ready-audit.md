# Virtue AEO / Agent-ready 공개 표면 감사표

> **생성**: 2026-05-26T07:00Z | **Intent**: marketing-18 | **모드**: cloud research/prepare

## 배경

GeekNews GN#354의 AEO/Agent-ready/GEO/AAO 흐름 — 검색 순위보다 AI·에이전트가 제품을 찾고, 읽고, 요약하고, 선택할 수 있는 공개 표면이 중요해졌다. Virtue는 prelaunch 단계이므로 공개 노출 확대보다 공개 설명면과 기계 판독 가능성을 먼저 감사한다.

## 조사 방법

- `https://virtue.oracle.shdkej.com` 직접 접근 → **403 Forbidden** (prelaunch 보호 확인)
- Infinity 아카이브 컨텍스트 (marketing-01~17): Virtue = Next.js 앱, apps/web/, J1~J4 JTBD, 핵심 이벤트 4개
- 기존 docs/ 9개 문서 참조 (정합성 확인)
- AEO/GEO/Agent-ready 모범 사례 기반 (research-08 GEO/LLMO 체크리스트 참조)

## 감사표

| # | 항목 | 현재 상태 | 분류 | 우선순위 | 비고 |
|---|------|-----------|------|----------|------|
| 1 | 공개 홈페이지 접근성 | 403 Forbidden (prelaunch 보호) | 🔧 공개 변경 필요 (보류) | 출시 P0 | prelaunch 해제는 사용자 결정 |
| 2 | robots.txt | 403으로 미확인 | 🔧 공개 변경 필요 (보류) | 출시 P0 | Disallow:/ → Allow 변경 필요 |
| 3 | sitemap.xml | 존재 미확인 | 🔧 공개 변경 필요 (보류) | 출시 P1 | Next.js App Router sitemap.ts 또는 next-sitemap |
| 4 | 페이지 title | 미확인 (403) | 📝 내부 문서 필요 | P1 | "Virtue – AI 덕행 기록" 형식으로 layout.tsx에 |
| 5 | meta description | 미확인 (403) | 📝 내부 문서 필요 | P1 | 120~160자, J1~J4 첫 가치 한 줄 |
| 6 | OG tags (og:title, og:description, og:image) | 미확인 (403) | 📝 내부 문서 필요 | P1 | Next.js 14 metadata API로 layout.tsx에 추가 |
| 7 | Twitter/X 카드 | 미확인 (403) | 📝 내부 문서 필요 | P2 | twitter:card: summary_large_image |
| 8 | Canonical URL | 미확인 (403) | 📝 내부 문서 필요 | P1 | alternates.canonical in layout.tsx |
| 9 | JSON-LD 구조화 데이터 | 없음 추정 | 📝 내부 문서 필요 | P1 | SoftwareApplication schema |
| 10 | llms.txt | 없음 | 📝 내부 문서 필요 | P1 | /public/llms.txt 초안 (이 문서에 포함) |
| 11 | Canonical 제품 설명 (공개 URL) | 내부 docs만 존재 | 🔧 공개 변경 필요 (보류) | 출시 P1 | /about 또는 /llms.txt로 외부 노출 필요 |
| 12 | Agent answer snippet (H1/hero 카피) | 미확인 (403) | 📝 내부 문서 필요 | P1 | "Virtue는 무엇인가" 1~2문장 명확화 |
| 13 | 가치 시그널링 (capability signals) | 내부 JTBD 문서 있음 | 📝 내부 문서 필요 | P1 | J1~J4를 agent-readable 형식으로 정리 |
| 14 | Positioning 내부 문서 9종 | virtue-rebirth-app docs에 있음 | ✅ 이미 충분함 | — | 내부 전략 문서, 공개 불필요 |
| 15 | JTBD 매트릭스 (first-session-jtbd-matrix) | virtue-rebirth-app docs에 있음 | ✅ 이미 충분함 | — | AEO hero 카피 및 가치 시그널 베이스로 활용 가능 |
| 16 | Activation 측정 기준 (activation-milestone-ladder) | virtue-rebirth-app docs에 있음 | ✅ 이미 충분함 | — | agent answer snippet 참조 가능 |

## 분류 요약

| 분류 | 항목 수 | 현 단계 액션 |
|------|---------|-------------|
| ✅ 이미 충분함 | 3 | 기존 docs/ 9종 유지, 공개 불필요 |
| 📝 내부 문서 필요 | 8 | title/meta/OG/Twitter/canonical/JSON-LD/llms.txt/hero — 즉시 준비 가능 |
| 🔧 공개 변경 필요 (보류) | 4 | 홈페이지·robots·sitemap·공개URL — **출시 결정 시 함께 처리** |
| 🔐 승인 필요 | 0 | (출시 결정 자체는 사용자 판단) |

> **prelaunch 원칙**: "공개 변경 필요" 4개는 현 단계에서 실행 금지. "내부 문서 필요" 8개 준비가 우선 액션.

## 기존 문서 정합성 확인

| 기존 문서 | 충돌 여부 | AEO 활용 가능성 |
|-----------|-----------|----------------|
| competitive-alternatives-positioning-brief | ✅ 없음 | hero 카피 후보 직접 활용 가능 |
| first-session-jtbd-matrix | ✅ 없음 | J1~J4 가치 시그널링 베이스 |
| activation-milestone-ladder | ✅ 없음 | agent answer snippet 참조 |
| three-screen-value-path-audit | ✅ 없음 | 제품 설명 흐름 참조 |
| first-session-friction-observation-protocol | ✅ 없음 | 별도 scope |
| marketing-09~17 (기타) | ✅ 없음 | 별도 scope |

**코드·카피·배포·robots/sitemap/metadata 실제 변경 0건. 충돌 없음.**

## 즉시 준비 가능 초안 (내부 문서)

### llms.txt 초안 (`/public/llms.txt`)

```
# Virtue
Virtue는 AI가 채점하는 덕행 기록 앱입니다.

## 제품 설명
- 덕행(deed)을 기록하면 AI가 가치를 판정합니다 (deed_judged)
- 저장된 덕행이 누적되어 성장을 추적합니다 (deed_saved, level_up_viewed)
- 반복과 누적을 통해 자기 발전을 가시화합니다

## 대상 사용자 (JTBD)
- J1 기록형: 매일 행동을 기록하고 싶은 사람
- J2 누적형: 성장을 수치로 추적하고 싶은 사람
- J3 AI 호기심형: AI 판정이 궁금한 사람
- J4 회고형: 과거 행동 패턴을 돌아보고 싶은 사람

## URL
- 앱: https://virtue.oracle.shdkej.com

## 제약
- prelaunch 단계 운영 중
- 개인 데이터는 로그인 사용자에게만 노출
```

### JSON-LD 초안 (Next.js layout.tsx 또는 page.tsx)

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Virtue",
  "description": "AI가 채점하는 덕행 기록 앱. 매일의 행동을 기록하면 AI가 가치를 판정하고 성장을 추적합니다.",
  "applicationCategory": "LifestyleApplication",
  "operatingSystem": "Web, iOS",
  "url": "https://virtue.oracle.shdkej.com"
}
```

### meta description 후보

- **J1/J4 중심**: `매일의 덕행을 기록하고 AI 채점으로 자기 발전을 추적하는 앱`
- **J3 중심**: `AI가 당신의 행동을 덕행으로 판정해 주는 실험적 앱`
- **통합 (권장)**: `Virtue는 AI가 덕행을 채점하는 기록 앱 — 행동을 입력하면 가치를 판정하고 누적 성장을 추적합니다`

### Agent Answer Snippet / Hero 카피 후보

> **권장**: "Virtue는 AI가 덕행을 채점하는 기록 앱입니다. 매일의 행동을 입력하면 AI가 가치를 판정하고, 누적된 덕행으로 성장을 추적합니다."

- competitive-alternatives-brief의 positioning 4종과 J1~J4 JTBD를 베이스로 도출
- 기존 copy-spec 금지어와 충돌 없음 확인

## 로컬 실행 프롬프트 (Claude Code 위임)

```
Infinity Intent: marketing-18 Virtue AEO / Agent-ready 공개 표면 감사표
Mode: execute_local
Required workflow: Use workflow-master first. Read .agent/workflows/workflow-master.md before proceeding.
Goal: virtue-rebirth-app/apps/web/docs/에 AEO 감사 브리프를 추가하고 커밋/푸시
Context:
  - 로컬 경로: /home/ubuntu/dev/virtue-rebirth-app/apps/web/docs/
  - 감사표 원본: infinity repo의 artifacts/marketing-18/aeo-agent-ready-audit.md
  - 기존 docs/ 9종과 충돌 없음 확인 완료
Prepared findings:
  - 16개 항목 4분류 감사표 완성
  - 내부 문서 필요 8개: title/meta/OG/Twitter/canonical/JSON-LD/llms.txt/hero 카피
  - 공개 변경 필요 4개: 출시 시 처리 (현 단계 실행 금지)
  - llms.txt 초안, JSON-LD 초안, meta description 후보, hero 카피 후보 포함
Allowed: L0/L1 (docs/ 파일 추가, 커밋, 푸시)
Forbidden:
  - robots.txt/sitemap/metadata 실제 변경
  - 배포, 외부 발송, 비용 집행
  - 공개 URL 변경
Action:
  1. infinity/artifacts/marketing-18/aeo-agent-ready-audit.md 내용 읽기
  2. apps/web/docs/aeo-agent-ready-audit.md 작성 (감사표 + 초안 포함)
  3. git add apps/web/docs/aeo-agent-ready-audit.md
  4. git commit -m "docs: add AEO agent-ready audit table (marketing-18)"
  5. git push origin master (또는 현재 브랜치)
Verification:
  - git diff 확인 — docs/ 파일 1개만 변경
  - 기존 docs/ 파일 변경 없음 확인
  - 코드/카피/배포 변경 0건 확인
Report back to: infinity/reports/marketing-18/{timestamp}.html
```
