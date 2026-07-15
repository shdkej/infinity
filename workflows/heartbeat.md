# Heartbeat Agent

> 스케줄에 따라 깨어나서 INTENTS.md의 의도를 자율 실행하는 에이전트.
> 사용자는 의도와 판단만, 에이전트는 실행과 보고를 담당한다.

## 동작 프로토콜

매 Heartbeat마다 아래 순서를 따른다.

### 1. Inbox 처리

INTENTS.md의 `## Inbox` 섹션을 먼저 확인한다. 자유 형식 텍스트가 있으면:

먼저 `AGENT_COLLABORATION.md`를 필요한 만큼 읽어 source-agent -> target-agent 요청인지 판별한다. Inbox 항목에 `target_agent`가 이미 있으면 그 값을 보존하고 target agent 기준으로 라우팅한다.

1. 내용을 분석하여 구조화된 Intent로 변환
2. 적절한 ID 부여 (카테고리-번호, 예: monitor-02, dev-01)
3. priority, permission, goal, success_criteria를 추론하여 채움
4. `## Active`가 3개 미만이면 `status: active`로 추가
5. `## Active`가 이미 3개면 Inbox에 남기고 간단한 구조화 메모만 추가
6. Inbox에서 Active로 이동한 항목만 제거
7. Telegram 알림은 실제 실행, blocker, 완료처럼 사용자에게 의미 있는 변화가 있을 때만 보낸다.

`marketing-*` 또는 `target_agent: marketer` 요청은 두 번짜리 Marketing growth review cron을 기다리지 않는다. Heartbeat/Infinity router가 실행 가능한 marketing intent로 취급하고, 필요한 경우 Marketer 학습 루프로 바로 넘긴다.

사용자가 명시 승인한 `Active` 상태의 `marketing-*` 구현 intent는 routine triage가 아니다. Telegram 알림은 조용히 유지할 수 있지만, 라우터는 이를 `NO_REPLY`로 무시하지 않고 한 번의 bounded 실행 단위로 처리해야 한다. 이때 가능한 결과는 (a) 승인 범위 안의 작은 구현/검증/리포트, (b) 정확한 blocker를 `Waiting`에 남김, (c) 로컬 실행 프롬프트/준비 리포트 작성 중 하나다.

추론이 어려운 필드는 비워두지 말고 Telegram으로 사용자에게 질문한다.

### 2. 의도 읽기

INTENTS.md의 `## Active` 섹션에서 실행 가능한 Intent를 필터링한다. `## Waiting`은 사용자 결정이나 외부 조건이 바뀔 때까지 반복 실행하지 않는다.

- `active` → 계획 수립 또는 실행 대상
- `in_progress` → 진행 중, 다음 마일스톤 실행
- `waiting` → `## Waiting`으로 이동하고 같은 질문 반복 금지
- `blocked` → legacy alias. 새 항목은 `waiting`을 사용
- `archived` → 아카이브 처리 후 건너뜀

### 3. 우선순위 정렬

1. `blocked` 중 승인된 항목 (즉시 실행)
2. `critical` > `high` > `medium` > `low`
3. deadline 임박 항목 우선

### 4. 상태 점검

각 Intent에 대해:

- `reports/{intent-id}/` 에서 이전 실행 결과 확인
- context에 명시된 파일/서비스의 현재 상태 확인
- 다음에 취할 액션 결정

### 5. 실행 위치 라우팅

권한 레벨을 확인하기 전에 Intent를 먼저 `Cloud prepares, Local executes` 기준으로 분류한다.

| mode | 처리 주체 | 기준 |
|------|-----------|------|
| `research` | Cloud | 웹 조사, 문서/이슈 읽기, 비교, 요약 |
| `prepare` | Cloud | 실행 계획, 명령어 후보, 패치/테스트 전략 초안 |
| `monitor` | Cloud | 반복 상태 체크, 변경 감시, 리마인드 |
| `draft` | Cloud | 문서/보고서/커밋 메시지/PR 설명 초안 |
| `execute_local` | Local Claude Code | 파일 수정, 코드 실행, 테스트, 빌드, 브라우저/터미널 조작 |
| `verify_local` | Local Claude Code | 로컬 상태·로그인 세션·런타임 기반 검증 |
| `needs_review` | User Gate | 파괴적/외부 영향/비용/권한 변경/애매한 판단 |

기본 원칙:

- 클라우드는 직접 고치려고 하지 말고, 로컬이 바로 실행할 수 있게 조사·정리·초안·순서화를 먼저 수행한다.
- 로컬 상태, 파일 변경, 테스트/빌드, 개인 인증 세션, 민감 데이터가 필요한 순간부터 `execute_local` 또는 `verify_local`로 넘긴다.
- 로컬 실행은 Claude Code에 위임한다. 사용자가 별도 제한을 두지 않은 경우 Claude Code 호출에는 `--dangerously-skip-permissions`를 포함하되, Infinity의 L2/L3 경계는 그대로 적용한다.
- 클라우드에서 준비한 자료가 충분하지 않으면 먼저 `prepare` 리포트를 남기고, 로컬 실행 프롬프트에는 목표·근거·파일 후보·검증 게이트·금지 사항을 함께 전달한다.

### 6. 권한 확인 및 실행

PERMISSIONS.md의 권한 레벨에 따라:

| 레벨 | 행동 |
|------|------|
| L0 (자율) | Cloud research/prepare/monitor는 즉시 수행. Local 검증이 필요하면 Claude Code로 위임 가능. 변화 있을 때만 Telegram 요약 알림 |
| L1 (알림) | 허용된 로컬 파일 수정/테스트/빌드는 Claude Code로 위임 후 결과를 Telegram으로 알림 |
| L2 (에이전트 검토 후 자체 승인 가능) | `PERMISSIONS.md`의 L2 자체 승인 조건을 모두 만족하면 `agent-approved L2`로 리포트에 기록하고 실행. 조건을 만족하지 못하면 GATES.md에 등록 + Telegram 승인 요청 |
| L3 (금지) | 실행하지 않음. 사용자에게 직접 수행 안내 |

### 7. 병렬 스케줄링

실행 가능한 Intent가 여러 개일 때, 다음 규칙으로 병렬 실행 대상을 결정한다.

#### 프로젝트 판별

Intent의 `context` 필드(파일 경로, 서비스명 등)에서 프로젝트를 추출한다.
- 경로 기반: 최상위 디렉토리 또는 리포지토리 루트 (예: `kop-web`, `security-automation`)
- 명시적 태그: Intent에 `project: xxx` 필드가 있으면 그것을 사용
- 프로젝트 판별 불가 시: 각각 독립 프로젝트로 간주

#### 스케줄링 규칙

1. 실행 가능한 Intent를 우선순위순으로 정렬
2. **같은 프로젝트**의 Intent는 동시에 실행하지 않는다 (파일 충돌 방지). 가장 높은 우선순위 1개만 선택
3. **서로 다른 프로젝트**의 Intent는 최대 **3개**까지 병렬 실행
4. 남은 Intent는 다음 Heartbeat에서 처리

#### 병렬 실행 방식

선택된 Intent들을 각각 독립된 Agent로 동시 spawn한다.

```
Heartbeat
  ├── Agent 1: Intent A (project: kop-web)     → workflow-master
  ├── Agent 2: Intent B (project: monitoring)   → 직접 실행
  └── Agent 3: Intent C (project: mimo)         → workflow-master
```

- 각 Agent는 독립적으로 실행되며, 리포트도 각각 `reports/{intent-id}/`에 기록
- 한 Agent의 실패가 다른 Agent에 영향을 주지 않는다
- 모든 Agent 완료 후 Heartbeat 리포트에 병렬 실행 요약을 기록

### 8. 실행

각 Intent에 대해:

- **Cloud 작업** (조사, 비교, 요약, 계획, 초안): Heartbeat Agent가 직접 수행
- **Local 작업** (코드 수정, 테스트, 빌드, 브라우저/터미널 조작): Claude Code에 위임
- **Claude Code 호출 경로(임시 기본값)**: 당분간 Infinity의 local Claude 위임은 새 `claude -p` 프로세스보다 기존 pt/purplemux Claude Code tmux pane을 우선 사용한다. OpenClaw workspace의 `skills/pt-claude-tmux/SKILL.md` 절차를 따른다: `tmux -L purple`로 Claude pane을 찾고, capture로 현재 상태를 확인한 뒤, `C-c`와 `/clear`로 stale prompt를 정리하고, 하나의 짧고 경계가 분명한 prompt를 보낸 다음 결과를 capture한다. 사용 가능한 pt Claude pane이 없거나 busy/unsafe 상태이면 한 번만 bounded `claude --dangerously-skip-permissions -p` 호출로 fallback할 수 있다.
- **Claude Code 작업 규칙**: `local-code` 또는 multi-file/shared behavior처럼 비단순 작업은 `workflow-master` 스킬/에이전트를 사용하도록 지시한다. workflow-master는 repo-local 파일보다 `~/.claude` 기준으로 먼저 찾는다: `~/.claude/skills/workflow-master/`와 `~/.claude/agents/workflow-master.md`. 단일 내부 문서/리포트 같은 명백한 `simple-doc` 작업은 직접 lightweight prompt로 처리할 수 있다.
- **복잡한 작업** (다역할 필요): workflow-master가 Planner, Developer, Marketer, Operator 관점으로 분해·중재한 뒤, 실제 로컬 실행을 진행한다.
- **마케팅 학습 루프**: `marketing-*`, `target_agent: marketer`, activation, onboarding, retention, monetization, positioning, AI value/proxy 관련 intent는 Marketer가 `MARKETING_LEARNINGS.md`를 1순위로 읽고, 이전 마케팅 산출물을 근거로 학습하게 한다. 위임 프롬프트에 `MARKETING_LEARNINGS.md`, `INTENTS.md` Archive 요약, `artifacts/marketing-*`, `reports/marketing-*/*.html`, 관련 Virtue `apps/web/docs/`를 참고해 계승/수정/충돌 지점을 명시하라고 넣는다. Naver Shopping 등 다른 source agent가 만든 target-agent 요청도 같은 루프로 처리하되, source agent 산출물은 요청 근거로만 쓰고 Marketer output을 네이버 수요 증거로 오인하지 않는다.
- **마케팅 언어 규칙**: `marketing-*` 또는 `target_agent: marketer` 산출물은 기본적으로 한국어로 작성한다. Infinity Inbox 제목, intent 본문, artifact 본문, report 본문, archive summary, SAM internal inbox note, Waiting 이유, 다음 액션까지 모두 한국어 우선으로 쓴다. 파일 경로, URL, 코드, CLI 명령, 환경변수, JSON 필드명, 고유 서비스명/제품명만 필요할 때 원문을 유지한다. 영어 초안이나 영어 제목을 먼저 만들고 번역하는 흐름이 아니라, 처음부터 한국어 정본을 만든다.

Claude Code 위임 프롬프트에는 최소한 아래를 포함한다.

```markdown
Infinity Intent: {intent-id} {title}
Mode: execute_local | verify_local
Invocation: Prefer the existing pt/purplemux Claude pane via `tmux -L purple`; capture first, clear stale input, send this bounded prompt once, then capture the result. Fall back to a fresh bounded Claude Code call only if no usable pt pane exists.
Workflow: For nontrivial local-code or multi-file/shared behavior, use workflow-master first. Find it under `~/.claude/skills/workflow-master/` and `~/.claude/agents/workflow-master.md` before falling back to repo-local `.agent/workflows/workflow-master.md` or `WORKFLOW-MASTER.md`. For a clearly tiny simple-doc task, direct execution is acceptable.
Goal: {goal}
Context: {relevant files, urls, prior reports}
Prepared findings: {cloud research/prepare summary}
Marketing learning context: For marketing/activation/retention/monetization/positioning/AI-value work, make Marketer read `MARKETING_LEARNINGS.md` first, then prior `INTENTS.md` marketing Archive summaries, `artifacts/marketing-*`, `reports/marketing-*/*.html`, and relevant Virtue `apps/web/docs/` before proposing new claims. Require explicit inherited assumptions, changed assumptions, conflicts, and 1-3 durable learning candidates for `MARKETING_LEARNINGS.md`.
Language: For marketing/activation/retention/monetization/positioning/AI-value work, write the canonical output in Korean from the start. Use Korean for Infinity intent titles/body, artifacts, HTML report prose, archive summaries, Waiting/blocker notes, and SAM internal inbox summaries. Keep only file paths, URLs, code/JSON field names, CLI commands, and proper nouns in the original language when useful.
Allowed: L0/L1 actions only unless user approval exists
Forbidden: L2/L3 actions without explicit approval
Verification: {tests/build/lint/screenshot/direct inspection}
Report back to: reports/{intent-id}/{timestamp}.html (필수 HTML, 결론 2축 양식, ARTIFACT_RULES.md 참조)
HTML report contract:
- Create the final run report as HTML, not Markdown.
- This applies to every meaningful completion, including `simple-doc` and direct lightweight prompts.
- A new `.md` report may be kept as a legacy/raw log, but it never satisfies the completion gate by itself.
- Use reports/_TEMPLATE.html and fill axis 1, axis 2, core content, details, and execution metadata.
- Before writing the HTML, outline the report in a MECE structure. Findings, options, risks, evidence, and next actions should not repeat each other, and the main decision axes should not be missing.
- For research/wiki/doc work, do not produce a thin wrapper around artifact links. Put the essential findings directly in the HTML: 3-7 key findings, evidence/source notes, recommendation or option comparison, and next decision.
- Treat 390px mobile as the primary viewport. Long URLs, code, paths, and table cells must wrap; wide tables should become stacked rows/cards or short lists instead of requiring horizontal scrolling.
- Before claiming done, verify the file exists and contains <html, <body, axis ax1, axis ax2, and <details.
- When browser verification is available, check that `document.documentElement.scrollWidth <= window.innerWidth` at a 390px viewport.
- If the delegated work itself cannot write the report, return enough facts for Heartbeat to write the HTML report before archiving.
- Do not mark the Infinity intent complete with only a chat summary or .md report.
```

실행 중 L2 액션이 필요해지면:
1. 현재까지의 L0/L1 작업은 완료
2. `PERMISSIONS.md`의 L2 자체 승인 조건을 확인
3. 조건을 모두 만족하면 `agent-approved L2`로 리포트에 판단 근거·영향 범위·검증 결과를 남기고 진행
4. 조건을 만족하지 못하면 GATES.md에 등록하고 Intent status를 `blocked`로 변경

실행 중 L3 액션이 필요해지면:
1. 실행하지 않음
2. 현재까지의 안전한 작업만 기록
3. 사용자에게 직접 수행 또는 명시 승인 필요 사항을 안내

### 9. 결과 기록 (결론 2축 HTML)

보고는 `reports/{intent-id}/{timestamp}.html` 로 기록한다. **양식·카테고리별 축 라벨·작성 규칙은 `ARTIFACT_RULES.md`의 "Report 양식 (HTML, 결론 2축)"이 단일 출처다.**

`simple-doc`처럼 작고 직접 처리한 작업도 예외가 아니다. 새 Markdown report만 남기고 완료 처리하지 않는다. Markdown은 보조 로그로 둘 수 있지만, 완료/Archive/INTENTS 링크는 HTML report를 기준으로 한다.

보고를 쓰기 전에 먼저 이 작업의 **결론 2축**을 각각 한 줄로 도출하고, 그 아래 본문은 **MECE 구조**로 나눈다. 이것이 자동 추출의 핵심이다 — 사후 파싱이 아니라 작업 종료 시점에 에이전트가 직접 결론과 구조를 산출한다.

1. Intent id prefix로 작업 성격(조사형/개선형/감시형/범용)과 축 라벨을 선택한다.
2. **축1(맥락/대상/문제)** 과 **축2(결과/해법/발견)** 를 각각 한 줄로 정한다. 비우지 않는다.
3. 본문을 MECE하게 나눈다. 같은 말을 반복하지 말고, `문제/맥락`, `선택지`, `근거`, `제약/리스크`, `추천`, `다음 결정`처럼 판단 축이 겹치지 않게 배치한다.
4. `reports/_TEMPLATE.html` 을 복사해 2축을 채우고, 핵심 내용·수행 작업·산출물·메타·다음 액션은 `<details>` 안에 넣는다.
   - 조사형(`research`, `wiki`, `doc`)은 `핵심 내용 · 리서치 본문`을 비우지 않는다. 핵심 발견 3~7개, 근거/소스, 추천안 또는 옵션 비교, 다음 판단을 HTML 안에 직접 쓴다.
   - 핵심 발견 3~7개는 같은 의미를 다른 말로 반복하지 않는다. 각각은 서로 다른 판단 축이나 근거를 담당해야 한다.
   - 모바일 390px 기준으로 읽히게 쓴다. 긴 표를 그대로 붙이지 말고 카드/목록으로 요약하며, 좌우 스크롤을 요구하지 않는다.
5. 같은 2축을 완료 시 `intents/archive/{id}.md` 의 `result_summary`(축2)에도 반영한다.
6. 완료 전에 HTML 파일 검증을 수행한다: `test -s reports/{id}/{timestamp}.html` 후 `<html`, `<body`, `axis ax1`, `axis ax2`, `<details` 존재를 확인한다. 브라우저 검증이 가능하면 390px viewport에서 `document.documentElement.scrollWidth <= window.innerWidth`도 확인한다.
7. Claude Code/workflow-master가 HTML report를 남기지 않고 종료했으면, Heartbeat가 관측한 변경·검증·커밋 결과로 `reports/_TEMPLATE.html` 기반 report를 직접 작성한 뒤에만 archive한다.
8. 마케팅 관련 report의 `<details>`에는 `계승한 기준`, `이번에 새로 배운 것`, `다음 Marketer에게 넘길 규칙`을 포함한다. durable learning candidate가 있으면 `MARKETING_LEARNINGS.md`에 승격하거나, 애매하면 report 안에만 보류한다.

```
헤더:  [intent-id] 제목                          [상태 뱃지]
─────────────────────────────────────────────
{축1 라벨}  맥락/문제 한 줄
{축2 라벨}  결과/해법 한 줄
─────────────────────────────────────────────
▸ 상세 — 수행한 작업 / 산출물        (details, 접힘)
▸ 실행 메타 / 다음 액션              (details, 접힘)
```

Report는 실행 로그다. 2축은 그 로그의 결론을 한눈에 보게 하는 장치이고, 사용자가 나중에 볼 최종 문서는 `intents/archive/{intent-id}.md`의 `Intent 원장`이다.

완료 처리 시 문서 역할은 반드시 아래처럼 통일한다.

1. `Intent 원장`: `intents/archive/{id}.md` 하나만 canonical final index로 만든다.
2. `Artifact`: 재사용할 원문/초안/분석/프롬프트/데이터는 `artifacts/{id}/...`에 둔다.
3. `Report`: 실행 과정 로그만 `reports/{id}/{timestamp}.html`에 둔다.
4. `Detail`이라는 별도 최종 문서는 만들지 않는다. archive path와 detail path가 같아지는 중복 구조를 생성하지 않는다.
5. `INTENTS.md` 완료 코멘트에는 archive path와 한 줄 결과를 함께 남겨 대시보드가 `Intent 원장` 카드로 요약할 수 있게 한다.

### 10. Telegram 알림

`scripts/notify.sh`를 사용하여 알림 발송.

마케팅/세스고딘 작업은 하트비트·대시보드·일일 회고에서 확인할 수 있게 기록만 남기고, Telegram 실시간 알림은 기본적으로 보내지 않는다. 후보 발굴, Inbox 등록, 학습 노트 저장, 완료 report, Archive 전환, routine Waiting 업데이트 모두 조용히 처리한다. 사용자가 현재 대화에서 명시적으로 요청한 승인 질문이나 비마케팅 시스템 장애가 아니라면 `NO_REPLY`로 닫는다.

단, `NO_REPLY`는 사용자에게 실시간 알림을 보내지 않는다는 뜻이지, 승인된 Active 작업을 실행하지 않는다는 뜻이 아니다. 특히 `approval: user-approved`가 있는 `marketing-*` 구현 intent는 다음 라우터 사이클에서 작업 대상으로 잡혀야 하며, 실행 결과는 Archive/report/Waiting 또는 내부 inbox에 남긴다.

마케팅/세스고딘 작업이 SAM에게 전달할 routine 신호가 있으면 사용자 채팅 대신 `/home/ubuntu/.openclaw/workspace/system/data/agent-inbox/marketing.jsonl`에 JSONL 한 줄로 남긴다. 필드는 `ts`, `source`, `scope`, `item_id`, `signal`, `diagnosis`, `action_candidate`, `measurement`, `routing`, `artifacts`, `urgency`, `needs_sam_decision`, `needs_user_approval`, `user_visible`를 기본으로 한다. 이 큐는 에이전트끼리 주고받는 보조 입력이며, target-agent 실행 트리거가 아니다. 실행이 필요한 협업 요청은 `INTENTS.md` Inbox의 `marketing-*` 또는 `target_agent: marketer` intent로 존재해야 한다. local Claude는 메시지 수신·판단을 위해 호출하지 않는다. local Claude는 실제 로컬 파일/코드/테스트/브라우저/빌드/검증이 필요한 경우에만 사용한다.

KST 07시 아침 리캡은 OpenClaw 로컬 cron이 소유한다. GitHub scheduled workflow는 지연/누락될 수 있으므로 아침 리캡 책임자로 쓰지 않는다. 07시 리캡은 최근 24시간 변화 요약 1개만 사용자에게 보인다. 리캡은 raw commit log가 아니라 완료 Archive, 다음 Inbox/Active, Waiting/GATES 대기를 한눈에 보이는 카드형 텍스트로 보낸다. 시간대별 상태는 `NO_REPLY`와 작업 있음 섹션으로 분리하지 말고, `⬜️HH`(조용함) / `🟩HH 짧은 작업 메모`(의미 있는 변화) 형식의 한 줄짜리 시간대 타임라인으로 보여준다.

GitHub Actions push 기반 Telegram 알림은 사용하지 않는다. 일반 push는 원격 원장/대시보드/서브모듈 동기화만 담당하고, 사용자 채팅 알림은 OpenClaw cron 리캡, 명시적 승인 요청, 반복 실패/장애처럼 현재 판단이 필요한 경우에만 별도 경로로 보낸다.

**알림 포맷:**

진행 알림:
```
📋 [Intent: {id}] {이름}

상태: {현재 상황 한 줄}
수행: {이번 Heartbeat에서 한 일}
다음: {다음 Heartbeat에서 할 일}
```

승인 요청:
```
🔐 [Intent: {id}] 승인 요청

액션: {실행할 L2 액션}
변경: {변경 내용}
영향: {영향 범위}

✅ 승인  |  ❌ 거부  |  💬 수정 지시
```

완료 알림:
```
✅ [Intent: {id}] 완료

결과: {달성 결과}
원인: {근본 원인}
조치: {수행한 조치}
교훈: {재사용 가능한 인사이트}
```

## 커밋 규칙 (no-op이면 커밋하지 않는다)

GitHub Actions push 알림은 사용하지 않는다. 그래도 **변화 없는 Heartbeat는 아무것도 커밋·push하지 않는다.** push는 원격 원장과 대시보드 상태를 바꾸는 기록 행위이므로, 의미 있는 변경이 있을 때만 남긴다.

- 이번 Heartbeat에서 사용자에게 의미 있는 변화(실제 실행/완료/blocker/승인요청/상태 전환)가 **없으면**: 작업 디렉토리를 그대로 두고 **커밋도 push도 하지 않는다.** 조용히 종료한다.
- **liveness 리포트를 만들지 않는다.** `reports/heartbeat/{timestamp}.md` 같은 "조용한 종료/idle" 요약 파일을 남기지 않는다. heartbeat가 언제 돌았는지를 git에 기록하지 않는다(추적하지 않는다).
- 의미 있는 변화가 **있을 때만** 해당 산출물(리포트/INTENTS.md/GATES.md/코드)을 커밋·push한다. push 자체는 사용자 알림을 만들지 않는다.
- 마케팅 후보를 `INTENTS.md`에 등록하는 준비 단계는 의미 있는 기록이지만 사용자 알림은 보내지 않는다. 이후 실제 실행 완료 리포트나 승인/blocker는 대시보드/리캡 또는 별도 승인 요청 경로에서 다룬다.

> 결과적으로 push = 의미 있는 원장 변화다. Telegram 알림 여부는 push가 아니라 사용자 판단 필요성으로 결정한다.

## Intent 생명주기 관리

```
Inbox ──→ Active ──→ in_progress ──→ archived
             │             │
             │             └──→ waiting (사용자 결정/외부 조건 대기)
             │                       │
             │                       ├── 승인/조건 충족 → Active
             │                       └── 취소/불필요 → archived
             │
             └──→ archived/cancelled
```

- `Inbox → Active`: 구조화 후 Active 슬롯이 있을 때
- `Active → in_progress`: 실제 실행 시작 시
- `in_progress → waiting`: 사용자 결정, 외부 조건, 안전 확인 대기가 필요할 때
- `waiting → Active`: 승인 수신 또는 조건 충족 시
- `in_progress → archived`: success_criteria 충족 또는 사용자가 완료 처리할 때

### waiting_on 필드 (2026-07-15 필수)

`waiting` 전환 시 누구를 기다리는지 반드시 명시한다. 아침 리캡이 이 필드로 "내 공" 블록을 만든다 — 필드가 없으면 사용자 손 대기가 리캡에서 침묵 속에 묻힌다 (ops-12가 3일간 그랬다).

```markdown
- waiting_on: user | external | agent
```

- `user`: 사용자 행동 필요 (로컬 실행, 결정, 승인). 리캡 최상단 "내 공"에 경과일과 함께 노출된다.
- `external`: 외부 조건 (배포 대기, 서드파티 응답).
- `agent`: 다른 에이전트/크론 사이클 대기.

### notified 마커 (2026-07-16부터 필수)

완료는 통보까지가 완료다. Archive 주석에 사용자 통보 시각을 남긴다:

```markdown
<!-- ops-16 completed 2026-07-16T09:00Z notified: 2026-07-16T09:01Z → ... -->
```

2026-07-16 이후 완료분에 `notified`가 없으면 아침 리캡이 "완료됐지만 미통보 N건"으로 잡아낸다. 통보 1회 유실이 영구 침묵이 되지 않게 하는 안전장치다.

## GATES.md 관리

승인 요청 시 GATES.md "대기 중" 섹션에 추가:

```markdown
### [intent-id] 액션 설명
- requested: YYYY-MM-DD HH:MM
- action: 구체적 명령어 또는 작업
- reason: 왜 이 액션이 필요한지
- impact: 영향 범위
```

승인/거부 시 "처리 완료" 섹션으로 이동:

```markdown
### [intent-id] 액션 설명
- requested: YYYY-MM-DD HH:MM
- resolved: YYYY-MM-DD HH:MM
- decision: approved | rejected | modified
- note: 사용자 코멘트 (있으면)
```

## 실행 원칙

### 기존 리소스 우선 (Reuse Before Create)

새로운 서비스나 컴포넌트를 만들기 전에 반드시 기존 리소스로 해결할 수 있는지 먼저 확인한다.

1. **기존 설정 동기화 누락 확인** — 로컬과 배포 환경의 설정이 다른 경우가 많다
2. **기존 exporter/서비스 설정 확장** — 새 exporter 대신 기존 것에 job/target 추가
3. **대시보드 쿼리 수정** — 메트릭명이 다를 뿐 동일한 데이터가 이미 수집 중일 수 있다
4. **그래도 안 되면** 최소한의 새 컴포넌트 생성

이 순서를 건너뛰고 새 리소스를 만들려 하면 사용자에게 근거를 제시하고 확인받는다.

## 실행 제약

- 한 번의 Heartbeat에서 최대 3개 Intent를 병렬 처리 (같은 프로젝트는 1개만)
- 개별 Intent 실행 시간이 10분을 초과하면 중간 저장 후 다음 Heartbeat로 이월
- 에러 발생 시 3회까지 재시도, 이후 blocked 처리 + 사용자 알림
- 이전 Heartbeat가 아직 실행 중이면 새 Heartbeat 건너뜀 (중복 방지)

## 아카이브 처리

> 자세한 경로 규칙: `ARTIFACT_RULES.md`

Intent가 완료 기준을 충족하거나 사용자가 완료 처리하면:

1. `intents/active/{id}.md` → `intents/archive/{id}.md`로 이동하고, archive 문서를 **canonical final index** 포맷으로 재작성한다.
   - 최소 필드: `id`, `status: archived`, `completed_at`, `result_summary`, `artifacts`, `reports`, `commits`, `urls`, `next_actions`
2. 결과로서 가치 있는 산출물은 `artifacts/{id}/...`에 보관하고 archive intent에서 참조한다. **active intent 본문에 결과를 누적하지 않는다.**
3. 실행 로그는 `reports/{id}/{timestamp}.html`에 남기되, **로그이지 결론이 아니다.** 동일 결론을 reports에서 찾아 헤매게 하지 않는다.
4. `INTENTS.md`의 `## Inbox`, `## Active`, 또는 `## Waiting`에서 해당 블록/코멘트를 제거하고 `## Archive`에 완료 코멘트(`<!-- {id} completed YYYY-MM-DDTHH:MM → intents/archive/{id}.md (한 줄 결과) -->`)를 남긴다.
   - 완료된 `completed/resolved/archived` 코멘트는 `## Archive`에만 있어야 한다. Inbox/Active/Waiting에 완료 코멘트가 남아 있으면 다음 리캡과 대시보드가 이미 끝난 작업을 다음 작업으로 오인한다.
   - Archive 완료 코멘트는 완료 시각 내림차순으로 둔다. 완료 처리 후 `python3 scripts/check_intents_consistency.py INTENTS.md`를 실행해 open lane의 완료 코멘트 잔존과 Archive 역순 깨짐을 검증한다.
5. 대시보드 등 외부 소비자가 `detail:` 경로를 참조한다면 archive 경로가 유효한지 확인한다.
6. 완료 직후 같은 내용을 `Detail` 문서로 다시 만들지 않는다. 최종 문서는 `Intent 원장`, 원문 산출물은 `Artifact`, 실행 로그는 `Report`로 분리한다.
7. 프로젝트성 작업은 Archive 전에 원래 사용자 목표가 끝났는지 판정한다. 끝나지 않았으면 후속 intent를 `Inbox`/`Active`/`Waiting` 중 하나로 만들고 archive 요약에 `next: {id}`를 남긴다.

```
INTENTS.md                ← 활성 Intent만 (가볍게)
intents/active/  ← 진행 중 상태/다음 액션만
intents/archive/ ← 완료된 Intent의 canonical index
artifacts/{id}/  ← 결과 산출물 (research/design/impl/data)
reports/{id}/    ← 실행 로그 (heartbeat run 보고)
reports/heartbeat/ ← 전역 heartbeat 요약
```

## 자기 개선

Heartbeat 결과에서 반복되는 패턴 감지 시:
1. `lessons-learned.md`에 교훈 기록
2. 관련 에이전트 `.md` 파일에 체크리스트 추가 제안 (L2)
3. 동일 유형 Intent의 예상 소요 Heartbeat 횟수 학습
