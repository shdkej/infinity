# Infinity Artifact / Path Rules

> 의도(Intent), 산출물(Artifact), 실행 로그(Report)의 위치와 책임을 명확히 분리한다.
> 모든 Heartbeat 및 Local 실행은 이 규칙을 따르며, 완료 시 archive intent를 canonical index로 만든다.

## 디렉터리 책임

| 경로 | 역할 |
| --- | --- |
| `INTENTS.yaml` | Backlog·Inbox·Active·Waiting 상태 원장과 월별 Archive manifest |
| `intents/archive/YYYY-MM.yaml` | 대시보드가 읽는 완료 카드 원장 |
| `intents/active/{id}.md` → `intents/archive/{id}.md` | 현재 맥락·다음 행동 → 완료 상세와 결과 링크 인덱스 |
| `artifacts/{id}/work/` | 계획·근거·초안·역할 검토. 최종 후보는 `candidate/`, Red 판정은 `red/` |
| `artifacts/{id}/final/` | 사용자 질문에 답하는 최종 재사용 원문·구현물·데이터 |
| `reports/{id}/{timestamp}.html` | 실행별 결과 요약과 검증·메타·로그 |
| `data/traces/{id}.json` | 요청·실행·검증 이력 ([trace 계약](docs/intent-trace-contract.md)) |
| `../knowledge-lab/source/infinity/archive/{id}.md` | 지식으로 선별한 결과만 보관하는 KL source |

`reports/heartbeat/`는 의미 있는 전역 변화 기록에만 사용합니다. no-op 생존 확인 리포트는 만들지 않습니다. 개별 Markdown 상세는 YAML 상태 원장을 대신하지 않습니다.

## Archive Tag Standard

완료 항목은 세 축으로 분류합니다. 새 프로젝트 태그는 반복될 때만 추가하고, 일회성 이름은 본문이나 topics에 둡니다.

| 필드 | 개수 | 값 |
| --- | --- | --- |
| `projects` | 1~3 | `virtue`, `infinity`, `knowledge-lab`, `agent-wiki`, `openclaw`, `infrastructure`, `personal-ops`, `research-bank`, `naver-shopping` |
| `task_type` | 1 | `research`(조사), `strategy`(방향), `design`(설계), `implementation`(생성·수정), `verification`(검증), `maintenance`(정리·복구), `monitoring`(감시), `coordination`(인계) |
| `topics` | 0~3 | `growth`, `marketing`, `product`, `activation`, `retention`, `analytics`, `ai-agents`, `llm`, `wiki`, `automation`, `workflow`, `dashboard`, `infra`, `security`, `calendar`, `review`, `finance`, `health`, `content` |

태스크 성격은 최종 결과의 주된 책임으로 하나만 고르고, topics는 projects와 같은 뜻을 반복하지 않습니다. `title`과 `task_name`은 대상·행동·산출물이 보이는 동일한 한국어 제목으로 씁니다.

## 핵심 원칙

1. **Reports는 실행 로그이고 결과물이 아니다.** 동일한 결론을 두 번 찾기 위해 사람이 reports 디렉터리를 뒤져야 하면 운영 실패다. 결과는 archive intent에 요약하고, 산출물은 `artifacts/{id}/final/`에 둔다.
2. **중간 산출물과 최종 산출물을 섞지 않는다.** `T1.*`, source notes, 비교 작업지, 역할별 초안, Red 검토/재검토, task plan은 모두 `artifacts/{id}/work/`에 둔다. 사용자가 열어야 하는 답·권고·재사용 원문은 `artifacts/{id}/final/`에만 둔다. `work/` 문서는 최종 결과를 대체하거나 Archive의 대표 링크가 될 수 없다.
3. **Active intent는 짧게 유지한다.** 분석/결과를 본문에 누적하지 말고, 산출물은 `artifacts/{id}/work/` 또는 `artifacts/{id}/final/`에 만들고 active intent에서는 참조만 한다.
   - **상세 표시 계약:** Active Intent가 `work/`에 읽을 수 있는 중간 산출물을 만들면, `INTENTS.yaml` 카드와 해당 detail intent의 `artifact:`에 현재 사용자에게 의미 있는 Markdown 경로를 함께 열거한다. 대시보드가 GitHub 디렉터리 API 제한을 만나도 raw 경로로 중간 결과를 표시할 수 있어야 한다. 새 evidence leaf가 문서를 추가·대체하면 같은 커밋에서 이 목록도 갱신한다. 계획 JSON, 이미지 원본, 해시·원시 캡처만은 이 목록의 기본 대상이 아니다.
4. **완료 시 archive intent가 canonical index가 된다.** 사용자가 "그래서 뭐 했더라"를 찾을 때 한 파일만 봐도 최종 산출물 / 최종 리포트 / 커밋 / URL 까지 한 번에 도달해야 한다.
5. **`drafts/`는 폐기.** 과거 drafts 산출물은 모두 `artifacts/{id}/`로 이동했다. 모든 신규 detail 링크는 `artifacts/{id}/work/`, `artifacts/{id}/final/` 또는 `intents/archive/{id}.md`만 가리킨다.
6. **Archive는 프로젝트 종료와 다를 수 있다.** 프로젝트성 작업은 한 intent가 설계·조사·MVP 같은 한 단계를 끝내고 Archive로 가더라도, 원래 사용자 목표가 남아 있으면 반드시 다음 intent를 `Inbox`/`Active`/`Waiting` 중 하나로 연결한다. Archive 요약에는 `next` 또는 후속 intent id를 남긴다.

### 리서치 최종본 품질 계약

리서치 최종본의 기본 흐름은 **`사용자 맥락 복원 → 핵심 발견 → 넓은 사례·인접 분야 지도 → 대안·반례·변화 신호 → 적용 가능성·열린 질문`**이다. `exploratory_research`는 사용자가 발산을 원할 때 여러 갈래를 충분한 분량과 실질적인 섹션으로 펼친다. 핵심 발견과 적용 해석을 앞에 두되, 단일 결론·실험·추천으로 성급히 수렴하지 않는다. 사용자가 지정한 출발 사례와 지역적 맥락을 우선 조사하고, 해외 사례는 비교 가지로 둔다. 사용자 맞춤 해석은 근거와 구분해 쓰고, 확인되지 않은 개인적 사실은 추정하지 않는다.

`exploratory_research`의 `final/`에는 주제 범위와 탐색 지도, 주요 갈래, 대표 사례, 발견 사이의 연결, 불확실성, 열어 둔 다음 질문을 둔다. 결론·추천·선택지 비교·버린 대안·사용자의 다음 행동은 요구하지 않는다. `decision_research`의 `final/`에는 원 질문에 대한 결론을 먼저 두고, 그 결론을 바꾸는 조건·핵심 발견·선택지 비교·버린 대안·다음 결정 하나를 분리한다. 의사결정형의 각 핵심 발견은 `주장 → 직접 근거 → 해석 → 한계/반증`을 한 덩어리로 남긴다. 어느 모드든 출처 수를 채우는 목적의 중복 자료, 조사 과정의 나열, 역할명·태스크 ID는 최종 본문에 넣지 않는다.

작업 중 생기는 `T1`/`T1.1` 메모와 Red 문서는 증거 추적에는 필요하지만 **최종 답이 아니다**. 모든 리서치는 원 질문에 답하는 **전체 Markdown 원문**을 `artifacts/{id}/final/{slug}-report.md`에 반드시 보존하고, 동일 내용을 읽기 좋게 요약한 `reports/{id}/{timestamp}.html`을 함께 만든다. 2026-11-14 이후 Archive하는 탐색형·의사결정형 리서치는 모두 HTML report, research-report validator, Red `PASS`를 거친다. 탐색형 Red는 사실 근거·범위·불확실성·가독성·화면 표시를 확인하며, 의사결정형 추천이나 결론 수렴을 강제하지 않는다. 변경일 이전 Archive 기록은 당시 상태 그대로 보존하고 PASS를 소급 생성하지 않는다. 네 역할 참여는 [Execution Mode 기록](#execution-mode-기록)을 따른다. `decision_research`의 최종 후보는 먼저 `work/candidate/`에 만들고, Red는 그 후보와 최종 HTML Report를 함께 검토한다. Red 문서는 `work/red/`에 판정·차단 사유·재검토 범위를 기록한다. PASS 뒤에만 검토한 동일 원문을 `final/`로 이동(또는 내용 동일성이 검증된 복사)하며, 최종 HTML 리포트는 이 MD 원문을 축약·표시하는 읽기 표면일 뿐 원문을 대체하지 않는다. 두 모드 모두 쉬운 한국어로 쓰고, 필요한 전문어는 짧은 뜻이나 예시로 풀어 쓴다.

**리서치 보존 게이트:** 2026-09-13 이후 Archive하는 리서치는 `final_artifact: artifacts/{id}/final/{slug}-report.md`를 명시하고, 그 파일이 비어 있지 않으며 원격 `main`의 **동일 Archive 원장**도 같은 경로를 가리켜야 한다. `work/candidate/*.md`, `work/` 문서, HTML report만으로는 리서치 완료·Archive를 인정하지 않는다. 이 규칙은 `exploratory_research`와 `decision_research` 모두에 적용한다. 이전 Archive는 경로 체계가 달라 자동 실패시키지 않으며, 수정·재검증 시 이 형식으로 이관한다.

### 광범위 사례·SNS 리서치 수집 프로토콜

커뮤니티·SNS·언론에 걸친 사례 조사(예: 특정 지원사업 기수의 참가 사례)에 적용한다. 2026-11-10 Kimi 지시로 SAM 설계안과 Hermes 레드팀 검증을 합쳐 정본화했다. 기존 리서치 품질 계약·보존 게이트를 대체하지 않고 수집 단계만 구체화한다.

1. **목적을 먼저 고정한다.** 사례 발굴(참고용, `exploratory_research`)인지 전체에 대한 판단(대표성 필요, `decision_research`)인지 Intent에 적는다. 불명확하면 접수 단계에서 한 번만 묻는다. 발굴이면 검색·스노볼을, 전체 판단이면 표본 틀과 분모 확인을 필수로 적용한다.
2. **판단형은 표본 틀(sampling frame)부터 만든다.** 공식 선정 목록·참여기관 자료로 전체 N을 확정하고, 팀별 공개 흔적(공식·언론·SNS·커뮤니티) 유무를 역으로 확인한다. 흔적이 없는 팀은 `확인 가능한 공개 자료 없음`으로 남긴다. 종료 기준은 `N 중 몇 확인`처럼 분모가 있는 숫자로 쓴다. 목록이 비공개이면 이를 한계로 명시하고 발굴형으로 격하한다.
3. **발굴형은 검색 시작 + 스노볼 확장을 쓴다.** 키워드 조합(기수명·후기·선정·탈락·중도 포기·데모데이·팀명)으로 시작하고, 발견한 사례의 링크·태그·언급을 따라 확장한다. 긍정·부정·무응답을 같은 기준으로 찾는다.
4. **출처를 층으로 나눈다.** 공식 / 언론·전문매체 / 커뮤니티 / SNS(Instagram·Threads·YouTube 등). 공식 발표와 개인 경험을 분리하고, 같은 사례의 중복 인용은 한 건으로 센다.
5. **SNS 한계를 결과물에 명시한다.** Instagram·Threads는 로그인 벽·알고리즘 필터로 검색 커버리지의 분모를 알 수 없다. 공개 게시물만 수동 확인하고, 자동 대량 수집·비공개 계정은 쓰지 않는다. 개인 식별 인용은 피하거나 익명화한다. 채널별로 `확인 범위·기간·방법·막힌 지점`을 final에 적는다.
6. **생존자·발화자 편향을 선언한다.** 검색 포화는 `검색 방식의 포화`일 뿐 사례 전체의 포화가 아니다. 조용히 끝낸 팀은 검색에 안 잡힌다는 점과, 결론을 전체 참가자의 여론으로 일반화하지 않는다는 점을 final에 쓴다.
7. **최소 DB로 시작한다.** 필드는 `팀/사례·출처 URL·작성 주체(공식/당사자/제3자)·주장 요약·근거 수준`부터 시작하고, 분석 질문이 요구할 때만 늘린다. 수집 시간 상한을 정해 해석 시간을 확보한다.
8. **LLM 보조 규칙.** 요약·분류는 맡길 수 있으나 인용·수치는 원문 URL을 열어 확인한다. 확인하지 않은 항목은 `미확인`으로 표시한다.
9. **final 구성.** 사례 목록 + 반복 패턴 + 반례·예외 + 출처별 한계 + 아직 모르는 것. `흥미로운 후기 모음`과 `전체 대표 결론`을 섞지 않는다.

### 완료 전달 체크리스트 (Intent · Dashboard · Skill)

Archive 전에는 다음 여섯 항목을 한 번에 확인한다. 이는 파일 존재 여부만 보는 검사가 아니라, 사용자가 대시보드에서 결과를 다시 찾고 이해할 수 있는지 확인하는 전달 계약이다.

| 항목 | 필수 범위 | 원장 기록 | 대시보드 기대 표시 |
|---|---|---|---|
| 요약 HTML | 모든 리서치, 구현·디자인·운영 산출물 | `reports/{id}/{timestamp}.html` | Report 링크와 iframe 미리보기 |
| 전체 Markdown | 모든 리서치 | `final_artifact: artifacts/{id}/final/{slug}-report.md` | Final Artifact 링크·본문 |
| zg 검색 매핑 | Context Pack v3+ Intent | `context_pack`, `context_documents_checked`, `context_searches`, trace `wiki_pages` | `조회한 경로 · Context Map`의 zg 쿼리·방식·선택 경로 |
| 리포트 길이 | 모든 사용자-facing 최종본 | `report_length`(문자 수), `report_length_judgment`(`too_short|fit|too_long`) | 원장/Report 메타에서 확인 가능해야 함 |
| 리포트 흐름 품질 | 모든 리서치, HTML이 있는 산출물 | `report_flow_check` | 탐색형은 주제 범위/지도 → 발견·사례 → 불확실성·열린 질문, 의사결정형은 결론 → 근거/비교 → 한계 → 다음 행동 순서가 보이고 내부 로그가 본문을 대체하지 않음 |
| 활용 스킬 | 해당 작업에서 스킬을 실제 사용했거나 특정 스킬이 요구된 경우 | `skills_used: [{name, purpose, evidence_path}]` | 상세의 `사용한 스킬`에서 이름·용도·근거가 보임 |

- **길이는 분량 목표가 아니다.** `report_length`는 과도하게 짧거나 긴 결과를 발견하는 관측값이다. `report_length_judgment`는 탐색형에서는 범위·발견·불확실성·열린 질문이, 의사결정형에서는 결론·근거·한계·다음 행동이 독해 가능한 밀도로 들어 있는지를 기준으로 작성자가 판정하고, Red가 필요한 작업에서는 재검토한다. 글자 수만 채우기 위한 반복은 실패다.
- **흐름 검사는 모드에 맞춘다.** 탐색형은 주제의 넓은 지도를 먼저 펼치고 발견과 열린 질문으로 끝낸다. 의사결정형은 결론, 근거/비교, 한계/반증, 다음 행동이 서로 섞이거나 빠지지 않아야 한다. 이 규칙은 `Report 양식`의 구조·Red 검토와 함께 적용한다.
- **스킬은 자동으로 추측해 적지 않는다.** 실제로 읽고 사용한 스킬만 남긴다. 단순 도구 호출은 스킬 사용이 아니다. 작업에 적용 가능한 스킬이 없으면 `skills_used: []`와 사유를 기록한다.
- Dashboard 구현은 위 필드를 숨기거나 축약하지 않는다. 현재 `Context Map`, Artifact, Report는 표시하지만 `report_length`, `report_flow_check`, `skills_used` 전용 행은 구현 대상이다. 이 체크리스트를 만족한다고 주장하려면 해당 행을 실제 화면에서 확인해야 한다.

## 대형 작업 태스크 계획

PRD가 필요한 대형 작업은 PRD가 승인·고정된 직후, 구현 전에 `artifacts/{intent-id}/work/task-plan.json`을 만든다. 이 파일은 실행 원장이 아니라 **계획 기준선**이며, 대시보드 카드가 다음을 읽는 유일한 구조화 입력이다.

### 양식 발견 preflight

계획을 작성·재계획하기 전에는 `ARTIFACT_RULES.md`의 이 섹션과 가장 가까운 기존 `task-plan.md` 예시를 실제로 읽는다. Intent에는 `task_plan_template: ARTIFACT_RULES.md#대형-작업-태스크-계획`을 기록한다. 이 preflight 없이 임의 JSON 구조, 표, 문서 형식을 새로 만들면 계획은 무효이며 실행으로 진행하지 않는다.

동시에 사람이 읽는 `artifacts/{intent-id}/work/task-plan.md`도 만든다. 이 문서는 PRD 링크, 태스크별 상태·완료 증거·다음 행동, 그리고 append-only `— 계획 변경` 기록을 담는다. `INTENTS.yaml`의 `task_plan_doc`으로 연결하며, JSON 상태나 deviation이 바뀌면 같은 커밋에서 함께 갱신한다. **트리 본문(`● Tn`부터 `└─ — 보호 경계`까지)은 반드시 ` ```text ` fenced code block 안에 둔다.** 대시보드 Markdown renderer가 공백과 `│` 연결선을 일반 문단으로 접지 않게 하는 표시 계약이다.

사람이 읽는 계획은 **`치안 지도 3차 실험 — 실행 타임라인`의 구조를 정본**으로 사용한다. 부모 `T1`은 기능 단위 미니 사이클이고, 그 아래 `T1.1…`에 계획·구현/조사·Red·마감 확인을 들여쓴다. 제목은 `# {작업명} — 실행 타임라인`, 첫 줄은 반드시 ``마감 · 실행 · 태스크: 완료/미완료 집계``, 각 leaf는 `상태 · 예상/최대 · 의존`, `증거:`, `시작/완료/실제:`를 차례로 둔다. 연결선·`● / ◐ / ○` 상태, 중간 `├─ — {시각} · {변경 대상}`의 append-only 계획 변경 기록, 마지막 `└─ — 보호 경계`와 `**지금 다음 행동:**`을 생략하지 않는다.

### 타임라인을 읽고 쓰는 법

- **첫 줄**은 마감·실제 실행 회차·leaf 완료량을 한눈에 보여준다. 실행 회차는 handoff 수가 아니라 새 증거를 만든 실행만 센다.
- **부모 `Tn`**은 사용자 가치가 있는 하나의 미니 사이클이며, **leaf `Tn.1~Tn.3`**은 각각 작업, Red 검증, 마감 확인이다. 각 leaf는 최대 30분이며 다음 부모는 이 세 단계가 닫힌 뒤 시작한다.
- **기호**는 `● 완료`, `◐ 진행`, `○ 미완료/대기`다. 상태만 쓰지 않고 모든 leaf에 계획치·의존성·증거·실제 시간을 붙여, 늦어진 이유와 다음 병목을 드러낸다.
- **변경 기록**은 기존 계획을 지우지 않는다. 범위·순서·대체 경로가 바뀌면 `├─ —` 분기에 시각과 이유를 누적한다. 마지막 **보호 경계**는 이번 실험에서 절대 넘지 않는 선이고, **지금 다음 행동**은 단 하나의 즉시 실행 leaf다.

새 계획은 아래 골격을 복사해 채운다.

```text
# {작업명} — 실행 타임라인
`마감: {local + UTC}` · `실행: N회차` · `태스크: X개 중 Y개 완료 · Z개 미완료`

● T1  {사용자 가치 미니 사이클}                                      완료
│  ● T1.1  {작업/조사}                                                 완료 · 예상/최대 20/30분 · 의존 없음
│           증거: `{artifact}`
│           시작/완료/실제: {UTC} / {UTC} / {N}분
│  ● T1.2  {Red 검증}                                                  완료 · 예상/최대 10/30분 · 의존 T1.1
│           증거: `{red artifact}` · Red PASS/FAIL
│           시작/완료/실제: {UTC} / {UTC} / {N}분
│  ● T1.3  {마감 확인}                                                 완료 · 예상/최대 5/30분 · 의존 T1.2
│           증거: `{closure artifact}`
│           시작/완료/실제: {UTC} / {UTC} / {N}분
│
├─ — {UTC} · {변경 대상}
│     {변경 이유와 영향}
│
└─ — 보호 경계
      {표시·데이터·권한·배포 등 금지선}
```

**지금 다음 행동:** `{다음 leaf 하나}`

이 문서는 임의의 “유사한 트리”가 아니라 고정된 표시 계약이다. dispatcher는 deadline Active Intent의 `task-plan.md`가 위 필수 필드 또는 트리 fenced code block을 빠뜨리면 실행하지 않고 `task_plan_format_violation`으로 되돌린다. 새 양식을 제안하려면 기존 양식을 바꾸기 전에 이 섹션·검증기·예시를 같은 커밋에서 먼저 갱신해야 한다.

- `tasks`: 작고 검증 가능한 태스크의 `id`, `title`, `status`, `evidence`를 둔다. 상위 단계는 그대로 하나의 태스크로 쓰지 않고 **3~7개의 독립 완료 단위**로 먼저 나눈다. 각 단위는 하나의 화면 변화, 데이터 계약, 검토, 배포 검증처럼 증거 하나로 닫혀야 한다. 사람이 읽는 타임라인에는 반드시 부모 `T3` 뒤에 들여쓴 `T3.1`, `T3.2` 형식으로 계층을 보인다. `status`는 `pending | active | done | skipped`만 쓴다.
- **장기 자동 확장:** automatic evidence-leaf replenishment additionally requires an explicitly user-provided, timezone-aware timestamp in the canonical Intent `deadline` field, with dispatcher time before that deadline. Never infer or invent a deadline. Without a valid future `deadline`, finish only leaves already in the plan and terminalize after they complete; do not replenish. For eligible deadline-bound work, only tasks where 50~60 leaves are appropriate may declare `expansion_policy`: `enabled: true`, `target_total_tasks: 50..60`, `batch_size: 1..10`, `min_ready_tasks: 1..10`, and an `expansion_brief` describing scope, evidence, and boundaries. The dispatcher may propose one batch only when pending+active leaves are below `min_ready_tasks` and total leaves are below target. Never alter or remove completed leaves; record new leaves in both JSON and `task-plan.md`. Markdown entries must include leaf ID, status, `예상/최대`, dependencies, and `증거:`, plus an append-only `— 계획 변경` entry naming added IDs. Post-handoff verification enforces the contract. If the deadline is absent, invalid, or reached, no batch is eligible and completed plans follow normal terminalization.
- **마감 예산과 반복 사이클:** 자동 반복 실행/leaf 추가는 사용자가 명시한 canonical Intent `deadline`이 유효하고 현재 시각보다 미래일 때만 설계한다. `deadline`까지 남은 시간이 현재 leaf의 `max_minutes` 합계보다 2배 이상 길고, `task_type: monitoring`이거나 원문에 “계속/반복/마감까지”가 있으면 단발성 계획으로 닫지 않는다. `task-plan.json`에 `cycle_policy`를 둔다: `mode: repeat`, `cycle_minutes`, `next_cycle_trigger`, `final_deadline`, `dedupe_key`, `minimum_cycles`. `task-plan.md` 첫 줄에는 `반복: C1/C2… · 다음 사이클 조건 · 최종 마감`을 표시하고, 각 반복 수집은 부모 `Tn` 미니 사이클과 실제 증거를 가진 leaf로 기록한다. 같은 수집을 다시 하는 경우에도 기존 leaf의 시간을 늘리지 않고 새 `C2`, `C3` 사이클을 append하며 `— 계획 변경`에 추가 이유·새 범위·예상 시간을 남긴다. 완료 leaf가 남아 있어도 유효한 canonical `deadline` 전에는 다음 사이클을 Active로 만들고, 마감 시점에만 Red·최종 보고·Archive로 닫는다. 명시적 deadline이 없으면 반복 leaf를 추가하지 않는다.
- `deviations`: 원래 계획에 없던 작업·순서 변경·대체 경로를 `{at, reason, impact, task_ids}`로 append-only 기록한다. 카드에서는 `— 계획 변경 N건`으로 분리 표시한다.
- `INTENTS.yaml`에는 `task_plan`과 `trace` 경로를 함께 남긴다. `trace`의 `dispatcher_handoff` 수는 카드의 **실행 회차**이며, 진전 수가 아니다.
- 각 cycle은 태스크 상태 또는 deviation을 바꿀 때에만 계획 파일을 갱신한다. handoff만으로 `done`을 올릴 수 없다.
- 완료 전에는 `done/total`, 현재 `active` 태스크, deviation 근거가 acceptance evidence와 일치해야 한다. 새 태스크가 필요하면 기존 태스크를 숨기거나 덮어쓰지 말고 deviation을 남긴다.

## 문서 역할 표준

문서 역할·경로는 위 [디렉터리 책임](#디렉터리-책임)을 따릅니다. 같은 결과를 `detail`, `draft`, `summary copy` 이름으로 다시 만들지 않습니다.

- 완료 상세는 `intents/archive/{id}.md` 하나로 연결합니다. UI에서 같은 경로가 archive/detail 양쪽에 있으면 한 항목으로 표시합니다.
- Active의 중간 결과는 상세 또는 `work/`에 한 번만 쓰고 링크합니다. 완료 카드의 대표 artifact는 `final/`이며 `work/`는 필요한 검토 근거만 `supporting_work`로 연결합니다.
- `result_summary`, 결과·리포트·커밋·URL·다음 행동은 완료 상세에서 찾을 수 있어야 합니다.
- 실행 Report는 HTML 하나로 둡니다. 전체 Markdown 원문은 리서치의 최종 artifact이고, 과거 Markdown Report는 이력입니다. 명시된 마감이 있는 작업은 성공·`deadline_missed`·명시 중단 모두 `reports/{id}/{timestamp}-terminal.md`를 남깁니다. 완료/미완료 leaf, 차단 원인·시도한 대안, 자율 재시도/사용자 결정, 구체적 개선을 담고 최종 상태·원 대화 알림에 연결합니다([KL 마감 기록 계약](../knowledge-lab/source/openclaw-system/docs/INFINITY_OPERATING_RULES.md#lifecycle-archive-and-records)).

## Archive Intent 표준 포맷

완료된 Intent를 archive로 옮길 때 최소 아래 필드를 포함한다.

```md
# [intent-id] 제목

- id: {intent-id}
- status: archived
- completed_at: YYYY-MM-DDTHH:MM:SSZ
- projects: [virtue]
- task_type: strategy
- topics: [activation, analytics]
- result_summary: 한 줄 결과
- artifacts:
  - path: artifacts/{id}/final/foo.md
    role: design | research | implementation | data
    note: 짧은 설명
  - path: artifacts/{id}/work/red/final-review.md
    role: supporting_work
    note: Red 판정 근거 (선택)
- reports:
  - path: reports/{id}/{timestamp}.html
    role: final | run | heartbeat
- commits:
  - repo: prompt-archive | space | ...
    sha: 894c3f8
    note: 짧은 설명
- urls:
  - url: https://...
    note: 라이브/배포 위치
- next_actions:
  - 후속 작업 / 권장 다음 Intent
```

### Archive Card 표준 템플릿

사람이 대시보드 Archive 카드만 보고도 "무엇이 끝났고, 어떤 상태이며, 어떤 기준으로 다음에 이어지는지" 알 수 있도록 신규 archive intent는 아래 블록을 포함한다. 이 블록은 `result_summary`보다 더 사용자-facing인 요약 카드이며, 대시보드와 후속 intent 자동 승격이 우선 참조한다.

지식 승격 판정은 일반화 가능성만으로 닫지 않는다. 해당 결과가 사용자의 장기 의사결정·사업·생활 지식으로 재진입할 가치가 있고, 다음 판단의 기준이나 검증 프레임을 보존한다면 탐색형 리서치도 `knowledge_status: promoted`와 `knowledge_decision: promote` 대상으로 삼는다. 단순 실행 로그와 일회성 후보는 제외한다.

```md
## Archive Card

[프로젝트]
토스 쉐어링크 Threads 테스트

[상태]
실행 준비 완료

[결과 기준]
7일간 게시물 21개 테스트

[다음 행동]
내일 첫 상품 3개 게시
```

자동화 호환을 위해 같은 내용을 아래 key 필드로도 남길 수 있다. 둘 다 있으면 `[프로젝트]` 형식의 사람이 읽는 블록을 우선한다.

```md
- archive_project: 토스 쉐어링크 Threads 테스트
- archive_state: 실행 준비 완료
- result_criteria: 7일간 게시물 21개 테스트
- next_action: 내일 첫 상품 3개 게시
- next_action_intent: marketing-123
```

`next_action`이 비어 있지 않고 `없음`, `완료`, `no continuation`이 아니면 Heartbeat는 같은 목적의 열린 intent가 있는지 확인한 뒤 후속 intent를 만든다. 공개 게시, 광고, DM/댓글, 계정 연결, 비용, 권한, 자격증명, 파괴적 변경이 포함된 다음 행동은 `Inbox` 또는 `Waiting`에 등록하되 실제 외부 실행은 사용자 승인 전까지 하지 않는다.

기존 archive 문서(`build-01.md`, `research-06.md` 등)는 형식이 일관되지 않지만 이 패스에서는 마이그레이션하지 않는다. **신규 archive부터** 이 포맷을 따른다.

### Execution Mode 기록

신규 Archive intent는 실행 방식이 검증 가능해야 한다.

- `execution_mode: single_genie_roles` — 과거 Archive의 호환용 값이다. 신규 Genie 실행에는 사용하지 않는다.
- `research_mode: exploratory_research` — 사례·시장 지형·트렌드를 설명하는 기본 리서치. 출처 확인, 전체 Markdown 브리프, 검증된 HTML report, 2026-11-14 이후 Archive 시 Red `PASS`를 요구한다. 추천/결정용 Deep Research는 요구하지 않지만, 결과물을 만드는 실제 요청이면 네 역할 세션과 간결한 교차 검토를 요구한다. 변경일 이전 Archive의 `not_required` 판정은 역사 기록으로 보존하며 소급 변경하지 않는다.
- `research_mode: decision_research` — 투자·도입·구매·출시·가격/수익성·법률 또는 명시적 검증을 위한 의사결정 리서치. Deep Research와 역할·Red 게이트를 적용한다.
- `execution_mode: multi_subagent_roles` — 모든 신규 Genie Intent/실행의 기본값. Planner, Developer, Marketer, Operator가 각기 임시 서브에이전트로 실행되며 간단 작업도 산출물 분량만 줄인다. SAM이 Genie Intent를 만들지 않고 직접 반환하는 읽기 전용 상태 답변만 역할 세션을 생략한다.
- `execution_mode: multi_subagent_roles_blocked` — 네 역할 중 하나라도 실행되지 못한 경우. 완료로 Archive하지 않고 복구 또는 재개 조건과 함께 Waiting에 둔다.
- `execution_mode: single_genie_roles_fallback_user_approved` — 역할 세션을 실제로 실행할 수 없고 사용자가 이번 작업의 직접 실행 fallback을 명시 승인한 경우에만 사용한다.

신규 작업은 `complexity_tier: simple|medium|complex`를 기록한다. 간단은 각 역할 1–3개 bullet과 한 차례 짧은 상호 검토, 중간은 근거·위험·다음 행동을 포함한 각 역할 섹션과 한 차례 반박·응답, 복잡은 역할별 독립 산출물과 필요한 조정 라운드를 사용한다. Genie는 근거로 결론을 통합하며 다수결로 결정하지 않는다.

`multi_subagent_roles` 완료 원장에는 `role_subagents`에 planner/developer/marketer/operator의 각각의 session id, 1차 판단, 교차 검토 상태와 결론을 남긴다. 네 역할 중 하나라도 증거가 없으면 Archive 완료로 보지 않는다.

### 프로젝트 연속성 게이트

아래 중 하나라도 참이면 archive 전환 전에 후속 상태를 명시해야 한다.

- 원래 사용자 요청이 배포/사용 가능한 기능인데 현재 intent가 설계·조사·인벤토리만 완료했다.
- `next_actions`가 실제 구현/배포/검증 단계를 요구한다.
- 사용자가 "계속", "프로젝트", "CMS", "앱", "대시보드", "사이트"처럼 장기 산출물을 기대했다.
- 완료 요약에 "미구현", "approval-needed", "별도 intent" 같은 문구가 들어간다.

후속 상태는 다음 중 하나로 남긴다.

- `Active`: 다음 단계가 명확하고 안전하며 바로 진행 가능하다.
- `Inbox`: 다음 단계는 필요하지만 슬롯/우선순위 정리가 필요하다.
- `Waiting`: 사용자 결정, 외부 계정, 비용, 권한, 시크릿, 공개 발송, destructive action이 필요하다.
- `No continuation`: 원래 목표가 실제로 끝났거나 사용자가 명시적으로 중단했다.

## Heartbeat가 지켜야 할 흐름

실행 순서는 [heartbeat의 종료 절차](heartbeat.md#6-결과와-archive를-함께-닫는다)를 따릅니다. 완료 상세를 만든 뒤 열린 lane에서 제거하고 **월별 YAML 카드**를 같은 변경에 기록합니다. `INTENTS.yaml`의 `archive.files`에는 `intents/archive/YYYY-MM.yaml`만 넣습니다. Markdown 상세·artifact·report 경로를 manifest에 직접 등록하거나 완료 주석만 남기지 않습니다.

월별 카드의 최소 연결 예시입니다. 값은 실제 결과와 검증 증거로 채우며, `remote_verified: pass`는 원격 검증 이후에만 기록합니다.

```yaml
archive:
  - id: example-01
    title: 대상 작업의 결과를 확인한다
    task_name: 대상 작업의 결과를 확인한다
    status: archived
    completed_at: '2026-01-01T00:00:00Z'
    detail: intents/archive/example-01.md
    artifact: artifacts/example-01/final/result.md
    report: reports/example-01/20260101T000000Z.html
    trace: data/traces/example-01.json
    red_status: pass
    remote_verified: pass
    notification_channel: <접수 때 기록한 채널>
    notification_target: <접수 때 기록한 대상>
```

리서치는 같은 카드·상세에 `final_artifact`를 기록합니다. 태그·후속 Intent·thread/reply 메타도 보존합니다. 상세 원장에는 아래 지식 판정을 함께 남깁니다.

| `knowledge_status` / `knowledge_decision` | 조건 |
| --- | --- |
| `raw` / `retain_in_infinity` | 단순 실행 기록·일회성 결과. `knowledge_reflection`에 보존 이유 기록 |
| `promoted` / `promote` | 장기 판단에 재사용할 지식. KL source·ingest 등록과 필요한 실제 반영 완료 |
| `superseded` / `supersede` | 기존 지식으로 대체. ingest `integrated`와 대체 근거 기록 |

`knowledge_targets`, `knowledge_reflection`, `knowledge_commit`을 기록하며 `candidate`로 Archive하지 않습니다. Context Pack v3+는 `knowledge_log: logs/agent-wiki-query.md#{id}`와 KL의 `[id]` 검색 영수증이 필요합니다. 영수증에는 질문·검색·결과·선택된 Wiki 경로·사용한 운영 로그를 남깁니다. 실제 ingest/승격 작업은 `artifacts/{id}/knowledge-flow.md`에 source·ingest 상태·대상·저장소별 commit을 연결합니다. 세부 지식 승격 경계는 [KL 운영 계약](../knowledge-lab/source/openclaw-system/docs/INFINITY_OPERATING_RULES.md#lifecycle-archive-and-records)을 따릅니다.

검증 진입점은 `check_intents_consistency.py INTENTS.yaml`, `validate_intent_trace.py`, `check_knowledge_promotion.py <intent-id>`, 리서치의 `validate_research_report.py <report.html>`입니다. push 후 `verify_archive_remote.py <intent-id>`와 실제 대시보드 카드·링크를 확인합니다. 실패는 근거와 재개 조건으로 남기며, 내부 마감 누락은 지니가 마칩니다.

## Report 양식 (HTML, 결론 2축)

`reports/_TEMPLATE.html`의 `rich-v1` 구조를 사용합니다. 맨 위에 맥락과 결과를 한 줄씩 쓰고, 본문에는 사용자가 읽을 핵심 내용을 넣으며 상세·실행 메타는 접습니다. 리포트는 최종 원문을 대체하지 않습니다.

작성 전에 발견·근거·제약·다음 질문/결정이 겹치지 않게 나눕니다. 탐색형은 탐색 지도와 열린 질문, 의사결정형은 결론과 선택 근거를 중심으로 씁니다. 내부 로그나 링크 목록만으로 본문을 대신하지 않습니다.

### 결론 2축 (필수)

모든 Report/원장은 아래 2축을 한 줄(또는 짧게)로 반드시 채운다. 작업하면서 이 두 질문의 답을 먼저 정하고 보고를 쓴다.

- **축1 = 맥락/대상/문제** — 왜 이 작업을 했나, 무엇에 대한 것인가
- **축2 = 결과/해법/발견** — 그래서 어떻게 됐나

축 라벨은 Intent id의 prefix로 작업 성격을 판별해 자동 선택한다.

| 성격 | id prefix | 축1 라벨 | 축2 라벨 |
|------|-----------|----------|----------|
| **조사형** | `research`, `wiki`, `doc` | 🔍 무엇을 조사/정리했나 | 📊 핵심 결과 |
| **개선형** | `marketing`, `product`, `dev`, `build`, `pages` | 🔴 무엇이 문제였나 | ✅ 어떻게 해결하나 |
| **감시형** | `monitor`, `maintenance`, `router` | 🟡 무엇을 점검했나 | ✅ 이상 여부·조치 |
| **범용(폴백)** | 그 외 / 분류 불가 | 무엇을 했나 | 결과 |

새 카테고리가 생기면 가장 가까운 성격에 매핑하고, 애매하면 범용 라벨을 쓴다.

### 작성 규칙

- `reports/_TEMPLATE.html`을 복사해 `{{...}}`를 치환합니다. `<html`, `<body`, `axis ax1`, `axis ax2`, `<details`와 반응형 CSS를 보존합니다. `_`로 시작하는 파일은 대시보드가 숨깁니다.
- 모든 리서치는 `final/{slug}-report.md`의 전체 원문과 HTML 요약을 함께 제공합니다. HTML에는 실질 발견 3개 이상, 연결된 출처 3개 이상, 근거·해석 구분, 다음 탐색 또는 판단을 담고 `python3 scripts/validate_research_report.py reports/{id}/{timestamp}.html`을 통과해야 합니다. 수를 채우려고 같은 내용을 반복하지 않습니다.
- 탐색형에 추천·결론·Red를 억지로 요구하지 않습니다. 의사결정형은 근거·비교·버린 대안·다음 판단을 담고, Red가 원문과 HTML을 직접 읽어 요청 부합·발견의 구체성·근거와 해석·다음 판단을 검증합니다.
- 위임 결과에 Report가 빠졌으면 관측한 결과로 보강한 뒤 닫습니다. 조사 원문·HTML·검증 중 누락된 것을 채팅 요약으로 대체하지 않습니다.
- 마케팅 Report의 상세에는 계승한 기준·새로 배운 점·다음 실행에서 바꿀 규칙을 남깁니다. 반복 가능한 판단만 해당 마케팅 정본에 승격합니다.
- 대시보드는 `iframe sandbox="allow-same-origin"`을 사용합니다. JS나 외부 리소스에 의존하지 않고 인라인 `<style>`과 `<details>`로 작성합니다.
- 모바일 390px에서 긴 URL·코드·경로가 줄바꿈되고 표가 가로 넘침을 만들지 않아야 합니다. 브라우저에서 `document.documentElement.scrollWidth <= window.innerWidth`, 제목·두 축·핵심 본문을 확인합니다. 브라우저 검증을 못 했으면 CSS 점검과 실제 렌더 미검증을 구분합니다.
- 디자인은 템플릿의 Quiet Note를 유지합니다. 배경 `#f4f2ea`, 축2 sage는 고정하고 `--a1` / `--a1-deep`만 성격별로 바꿉니다: 조사 `#5a6f8a` / `#3f536e`, 개선 `#a9745a` / `#8a5c45`, 감시 `#b08545` / `#8a6633`.
- 순서는 `id·상태 → 제목·dek → 두 축 → 핵심 내용 → 상세 → 메타`입니다. 같은 실행의 Markdown·HTML Report를 중복 생성하지 않습니다. 기존 두 형식이 함께 있으면 HTML을 우선 표시합니다.

## Migration Note (현 상태)

- `drafts/` → `artifacts/{id}/`로 전부 이관 완료. archive intent 참조 경로도 함께 갱신했다.
- 이 `work/`·`final/` 경계는 이 규칙 반영 뒤 생성·수정하는 Intent부터 적용한다. 기존 root-level `artifacts/{id}/...` 경로는 legacy이며, Archive 재작성 또는 후속 수정 때만 이동한다.
- `reports/` 하위 디렉터리는 그대로 둔다. 신규 final 결과는 reports가 아니라 archive intent + artifacts 조합으로 표현한다.
- 대시보드는 archive intent 본문과 `artifacts/{id}/` 디렉토리를 우선 로드하고, 마지막 fallback으로 reports 최신 1건을 표시한다.
