# marketing-18 Intent Archive

- id: marketing-18
- title: Virtue AEO / Agent-ready 공개 표면 감사표
- status: archived
- priority: medium
- permission: L0/L1 내부 감사 + L2 agent-approved push
- created_at: 2026-05-26T00:07Z
- completed_at: 2026-05-26T00:07Z
- source_note: `/home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-26-aeo-agent-ready-research.md`

## Result Summary

Virtue가 **prelaunch** 상태에서 AI 답변엔진과 브라우징/코딩 에이전트에게 **어떤 제품으로 읽히는지**를 감사하는 내부 정본 브리프를 작성했다. GeekNews GN#354의 AEO(Agentic Engine Optimization)·Agent-ready·GEO·AAO 묶음(Addy Osmani / isitagentready.com / a16z / Search Engine Land 배경)을 렌즈로 삼되, **외부 노출을 키우는 게 아니라** "AI/에이전트가 Virtue를 어떤 문제의 해법으로 요약할 수 있는가"를 먼저 정의하는 데 초점을 뒀다.

5축 렌즈(발견 가능성·파싱 용이성·토큰 효율성·기능/가치 시그널링·접근 제어)로 성공기준이 지정한 8개 공개 표면 항목을 `이미 충분함 / 내부 문서 필요 / 공개 변경 필요 / 승인 필요`로 분류했다.

- **이미 충분함** — capability/value signaling(내부 정의): JTBD·경쟁 대안·MVA 등 7+ 선행 문서로 내부 정의는 충분, 부족한 건 기계 판독 표면화뿐.
- **내부 문서 필요(L1 즉시 가능)** — canonical product explainer · Markdown/llms.txt 후보 · agent answer snippet: 본 문서 §4가 1차 산출(무엇/누가 J1~J4/언제/왜 다른가 + 저토큰 1줄 요약).
- **공개 변경 필요(proposal-only)** — public homepage 파싱 가능화 · robots.txt · sitemap · structured metadata(OG/Twitter/JSON-LD/canonical/manifest): 전부 코드/공개 파일 변경이라 본 Intent 금지선, 권고만.
- **승인 필요(Waiting)** — 위 공개 변경의 production 배포 · 검색엔진/AI 디렉터리 외부 제출 · 비용 집행.

**핵심 발견:** `app/page.tsx`를 포함한 전 앱 페이지가 `"use client"`(rg 6매치)라 초기 서버 HTML 본문이 빈 셸이고, 봇/답변엔진은 `layout.tsx`의 `<title>`("덕 쌓기 · 환생")+`<meta description>` 2줄만 읽는다. robots/sitemap/llms.txt/JSON-LD/OG 모두 부재. 이 "도달 가능하지만 파싱 불가" 상태는 prelaunch 전략(노출 확대 안 함)과 *우연히* 정렬됐을 뿐, 의도된 접근 제어가 아니라 렌더링 방식의 부산물임을 명시했다. 따라서 prelaunch 1순위는 기계 표면을 손대는 게 아니라 launch 시 무엇을 보이게 할지의 *내용*을 내부에서 먼저 확정하는 것.

## Artifact

- repo: `virtue-rebirth-app`
- branch: `master`
- commit: `f74cf59` (이전 HEAD `2a8c694` fast-forward)
- path: `apps/web/docs/aeo-agent-ready-surface-audit.md` (신규 1파일)

## Scope

- robots.txt / sitemap / metadata(layout/head) / 공개 페이지 / 소스 코드 / 배포 / CI 트리거: 변경 0
- env / 시크릿 / 권한 / 애널리틱스 스키마 / 대시보드 / 신규 이벤트 / 플래그: 변경 0
- 외부 호출 / 검색엔진·AI 디렉터리 제출 / 발송 / 비용: 0 (배경 출처 링크 외부 fetch도 안 함)
- 라이브 공개 URL 능동 probe 미수행 (repo read-only 근거로 충분)
- iOS·`/deeds`·`/dex` 표면 감사: 범위 밖, 별도 Intent 후보

## Verification

- 변경이 `apps/web/docs/` 문서 1개로 한정 (`git status --short` 신규 doc만)
- `apps/web/src`·`apps/ios`·`next.config.ts`·`layout.tsx`·`public` 변경 0건 (`git diff --stat` 빈 출력)
- 실제 충돌 마커 0 (라인시작 앵커 무매치; 느슨한 검색 유일 매치는 문서 §7 self-check 명령 자기참조, 선행 marketing-16/17과 동일 관례)
- 문서가 공개 변경을 *했다고* 주장하지 않으며 내부/공개/승인 명확 분리 (§0 전제①·§2 분류·§5 경계·§7 Out of scope)
- 지정 선행 문서(`first-session-jtbd-matrix`/`competitive-alternatives-positioning-brief`/`three-screen-value-path-audit`/`first-impression-positioning-snapshot`/`minimum-viable-audience-brief`/`copy-spec`) + Infinity `research-08` 충돌 0 (§6)
- target repo push 후 local HEAD `f74cf59` == `origin/master` `f74cf59`, 워킹트리 clean

## L2 push 기록

- 승인: `agent-approved L2` (doc-only 1파일 추가, Intent permission과 정합)
- 영향: 내부 문서 1개 추가, 런타임/사용자 노출/공개 표면 영향 0
- 가역성: 높음 (`git revert f74cf59`로 즉시 복구, 단일 신규 파일)
- 비용: 0 / production·secrets·permissions: 변경 0 / 제3자 메시징 위험: 없음

## workflow-master

- target repo에 workflow-master 파일 부재(`.agent/workflows/workflow-master.md`·`WORKFLOW-MASTER.md` 무매치) → 부재 기록 후 게이트 수동 적용
- Planner/Developer/Marketer/Operator 4역할 병렬 합성 (marketing-16/17 관례 계승)

## Reports

- `reports/marketing-18/2026-05-26T0007Z-local.md`
