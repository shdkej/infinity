# build-14 Planner - Daily System Metrics Visualization

작성 시각: 2026-08-05T22:54Z 기준
역할: Planner
소유 범위: 사용자 목표, 첫 버전 완료 기준, 지표 우선순위, 첫 화면 정보 구조, 8시간 범위, Developer 데이터 계약

## 1. 사용자 목표

마스터가 매일 한 번 열어서 자신의 시스템이 어제부터 오늘까지 어떻게 움직였는지 그래프로 보고, 오늘 조정할 한 가지를 빠르게 잡을 수 있는 시각화 페이지를 만든다.

이 페이지는 완성형 observability 플랫폼이 아니라 Infinity의 일일 운영 상태판이다. 핵심은 지표 수를 늘리는 것이 아니라 다음 질문에 5초 안에 답하게 하는 것이다.

- 오늘 시스템은 정상인가?
- 어느 층이 흔들렸는가?
- 어제/최근 7일과 비교해 달라진 것은 무엇인가?
- 오늘 사람이 개입해야 할 다음 액션은 무엇인가?

사용자는 개발자이자 개인 운영 시스템의 오케스트레이터다. 따라서 첫 버전은 "인프라가 살아 있다"만 말하면 부족하고, `자동화가 돌았는가`, `사용자 요청이 닫혔는가`, `기억/지식 기반이 다시 꺼낼 수 있는 상태인가`, `Infinity 작업 큐가 흐르는가`를 한 판에서 보여줘야 한다.

매일 보는 성공 경험은 아래 한 문장으로 정의한다.

> 오늘 열었을 때, 어제와 달라진 위험 1개와 지금 건드릴 다음 행동 1개를 바로 안다.

## 2. 첫 버전 완료 기준

8시간 내 첫 버전은 아래 조건을 만족하면 완료로 본다.

- 최근 7일 또는 14일의 일일 시스템 지표를 날짜별 그래프로 볼 수 있다.
- 최소 3개 지표군이 실제 데이터 또는 명시적으로 표시된 sample/fallback 데이터로 렌더링된다.
- 첫 화면 상단에서 `정상 / 주의 / 확인 필요` 중 하나의 오늘 상태를 보여준다.
- 각 지표군은 전일 대비 또는 최근 평균 대비 변화를 함께 보여준다.
- 데이터 계약 문서 또는 타입이 있어 다음 지표군을 추가할 때 입력 구조를 바꾸지 않아도 된다.
- 로컬 preview 또는 배포 URL에서 실제 화면을 확인할 수 있다.
- 빈 데이터, 일부 누락, 오래된 데이터일 때 페이지가 깨지지 않고 `데이터 없음 / 갱신 필요` 상태를 보여준다.

완료로 보지 않는 경우:

- 숫자 카드만 있고 날짜별 추세 그래프가 없는 경우
- mock 데이터가 실제 데이터처럼 표시되는 경우
- 지표가 많지만 오늘 무엇을 봐야 하는지 알 수 없는 경우
- 데이터 추가 방식이 코드 내부 하드코딩에만 묶인 경우

## 3. 매일 볼 지표군 후보와 우선순위

### P0. Agent/Cron 실행 건강도

목적: 매일 돌아야 하는 자동화가 실제로 돌았는지 확인한다.

첫 버전 지표:

- 총 실행 수
- 성공 수 / 실패 수
- 실패율
- 최근 실패 job 이름 또는 실패 사유 요약

선정 이유: Infinity, 하트비트, 리뷰, 알림 같은 운영 루프의 바닥 건강도다. 실패가 쌓이면 다른 지표가 좋아 보여도 시스템을 믿기 어렵다.

### P0. 사용자-facing 응답성과 작업 처리량

목적: SAM/OpenClaw가 사용자 요청을 끊기지 않고 처리하고 있는지 본다.

첫 버전 지표:

- 일일 세션/작업 수
- 완료 수
- 실패 또는 중단 수
- 평균 처리 시간 또는 p95 처리 시간

선정 이유: 사용자가 체감하는 시스템 품질에 가장 가깝다. 평균보다 p95를 우선하면 긴 꼬리 지연과 멈춤을 빨리 볼 수 있다.

### P1. Memory/Knowledge 상태

목적: 개인 운영 시스템의 맥락 회수 능력이 살아 있는지 본다.

첫 버전 지표:

- memory search/index 상태
- vector/FTS ready 여부
- 최근 색인 시각
- 검색 실패 수 또는 fallback 발생 수

선정 이유: 최근 memorySearch 장애가 있었고, 사용자의 운영은 기억과 재호출에 강하게 의존한다. 이 지표는 단순 인프라가 아니라 다음 대화 품질의 선행 신호다.

### P1. Infinity 의도 흐름

목적: 작업 큐가 쌓이고 닫히는 흐름을 본다.

첫 버전 지표:

- Active intent 수
- Waiting/Inbox 수
- Archive 전환 수
- 24시간 이상 정체된 intent 수

선정 이유: Infinity는 사용자의 핵심 작업 큐다. 매일 볼 페이지라면 시스템 자원보다 먼저 일이 흐르고 있는지 보여줘야 한다.

### MVP 핵심 3묶음

8시간 MVP에서 반드시 보장할 핵심 묶음은 아래 3개다. 데이터 원천이 부족하면 실제값 + sample/fallback을 섞을 수 있지만, 화면에는 반드시 `actual / estimated / sample`이 드러나야 한다.

1. `운영 루프 건강도`: cron/agent 실행 성공, 실패, stale 여부
2. `작업 흐름`: OpenClaw/SAM 작업 처리량, 완료/중단, p95 또는 longest duration
3. `지식/의도 흐름`: memory/index 상태와 Infinity active/waiting/archive 흐름

Gateway/runtime, 비용/토큰, 상세 agent breakdown은 같은 페이지의 후속 확장 후보로 남긴다. 첫 화면에서 5초 판단을 흐리면 8시간 MVP에서는 제외한다.

### P2. Gateway/Runtime 안정성

목적: OpenClaw gateway와 런타임이 재시작, 오류, 중단 없이 유지되는지 본다.

첫 버전 지표:

- gateway restart 수
- clean stop / abnormal stop 구분
- 최근 uptime
- 주요 error event 수

선정 이유: 전체 시스템의 바닥 레이어다. 다만 첫 화면에서는 Agent/Cron 건강도와 겹칠 수 있으므로 P2로 두고, 데이터가 바로 있으면 포함한다.

### P2. 비용/토큰 사용량

목적: 매일 운영 비용이 급증하지 않는지 본다.

첫 버전 지표:

- 일일 토큰 사용량 또는 요청 수
- 모델별 호출 수
- 오류 재시도 수
- 전일 대비 변화율

선정 이유: 장기 운영에는 중요하지만 첫 8시간 안에 데이터 원천 확인 비용이 클 수 있다. 가능하면 후순위로 붙이고, 없으면 후속 범위로 둔다.

## 4. 첫 화면 정보 구조

첫 화면은 `오늘 상태 -> 추세 -> 재진입` 순서로 구성한다.

### A. 상단 상태 요약

- 페이지 제목: `Daily System Metrics`
- 기준일과 데이터 최신 시각
- 오늘 상태 배지: `정상`, `주의`, `확인 필요`
- 한 줄 요약: 예) `Cron 실패가 2건 늘었고, Infinity Active가 5건으로 유지 중입니다.`
- 주요 액션 1개: 예) `실패 job 확인`

### B. 핵심 지표 3~4개

P0/P1 지표군을 작은 카드로 배치한다.

- Agent/Cron 건강도
- 응답성과 작업 처리량
- Memory/Knowledge 상태
- Infinity 의도 흐름

각 카드는 아래 정보를 가진다.

- 오늘 값
- 전일 대비 변화
- 상태 색상
- 작은 sparkline 또는 7일 mini chart
- 데이터 없음/오래됨 상태

### C. 날짜별 그래프 영역

첫 버전은 상세 분석보다 추세 비교가 중요하다.

- 기본 기간: 최근 14일
- 기본 그래프: 지표군별 line/bar chart
- 기간 선택: 7일 / 14일 / 30일 중 7일과 14일만 우선 구현
- y축 단위는 지표군마다 다르게 두되, hover tooltip에서 원값을 보여준다.

### D. 오늘의 확인 목록

그래프 아래에 오늘 개입할 가능성이 있는 항목만 짧게 둔다.

- 실패 job
- 오래된 데이터 원천
- 정체된 Infinity intent
- memory/index fallback

첫 버전에서는 상세 drilldown 대신 해당 원천 파일/로그/명령으로 이어질 수 있는 label 또는 path hint만 둔다.

### 첫 화면 우선순위

첫 viewport 안에서 반드시 보이는 순서는 아래로 고정한다.

1. `오늘 상태`: 정상/주의/확인 필요, 기준일, freshness
2. `왜 그런가`: 가장 큰 원인 1개와 전일 대비 변화 1개
3. `무엇을 할까`: 다음 액션 1개
4. `어디가 흔들렸나`: 핵심 3묶음 카드

그래프는 첫 viewport 아래로 내려가도 된다. 매일 여는 화면의 첫 임무는 분석이 아니라 상태 판독과 재진입이다.

## 5. 8시간 내 줄일 범위

### 오늘 만들 것

- 단일 페이지
- 최근 7~14일 일일 집계
- 3개 MVP 핵심 지표군과 가능하면 1개 보조 지표군
- 한 화면 상태 요약
- line/bar 중심의 기본 그래프
- 데이터 계약 파일 또는 타입 정의
- empty/stale/error 상태
- 로컬 또는 배포 URL 확인
- sample/fallback 데이터의 명시 라벨링
- 첫 데이터 원천 path 또는 생성 명령 힌트

### 오늘 만들지 않을 것

- 실시간 streaming
- 세부 로그 검색 UI
- trace/drilldown 화면
- 알림 발송 자동화
- 임계치 편집 UI
- 사용자별 권한/멀티테넌시
- 복잡한 상관관계 분석
- 모바일 전용 복잡 인터랙션
- 모든 지표 원천의 완전 자동 ETL
- agent별 상세 페이지
- 공개 공유용 리포트 카피 최적화

### 나중으로 미룸

- Grafana/Prometheus/Loki/ClickHouse 등 외부 observability stack 연동
- 비용/토큰 상세 리포트
- Slack/Telegram alert routing
- 원인 분석 자동 요약
- 주간/월간 리포트 생성
- 지표별 SLO와 alert policy 편집
- agent별 상세 breakdown
- publication용 리포트/카드뉴스 변환

## 6. Developer에게 넘길 데이터 계약 요구사항

Developer는 구현 대상 repo를 선정한 뒤, 아래 형태를 유지하는 일일 metric snapshot을 기준으로 페이지를 만든다. 저장 위치와 포맷은 repo 상황에 맞춰 정하되, 화면 컴포넌트는 이 계약만 읽도록 분리한다.

```ts
type DailySystemMetricSnapshot = {
  date: string; // YYYY-MM-DD, KST 기준 권장
  generatedAt: string; // ISO timestamp
  freshness: "fresh" | "stale" | "missing" | "partial";
  visibility: "private" | "restricted" | "public_safe";
  overallStatus: "ok" | "warning" | "needs_attention";
  summary: string;
  nextAction?: {
    label: string;
    target?: string; // file path, command hint, report URL, or route
  };
  metricGroups: MetricGroup[];
  issues: MetricIssue[];
  sources: MetricSource[];
};

type MetricGroup = {
  id: string;
  label: string;
  priority: "P0" | "P1" | "P2";
  status: "ok" | "warning" | "needs_attention" | "unknown";
  unit: "count" | "percent" | "ms" | "boolean" | "score" | "currency";
  value: number | boolean | null;
  previousValue?: number | boolean | null;
  delta?: number | null;
  trend: Array<{
    date: string;
    value: number | null;
    status?: "ok" | "warning" | "needs_attention" | "unknown";
  }>;
  description?: string;
};

type MetricIssue = {
  id: string;
  severity: "info" | "warning" | "critical";
  title: string;
  detail?: string;
  metricGroupId?: string;
  sourceId?: string;
  target?: string;
};

type MetricSource = {
  id: string;
  label: string;
  kind: "file" | "command" | "api" | "manual" | "generated";
  location?: string;
  lastUpdated?: string;
  confidence: "actual" | "estimated" | "sample";
  containsSensitiveData?: boolean;
};
```

필수 계약:

- `date`는 일일 그래프의 기본 join key다.
- sample/mock/fallback 데이터는 `sources[].confidence`로 반드시 표시한다.
- 일부 지표가 비어도 페이지 전체가 실패하면 안 된다.
- `overallStatus`는 가장 높은 심각도의 P0/P1 issue를 기준으로 계산한다.
- 모든 지표군은 `trend`를 가져야 한다. 첫날 데이터만 있으면 길이 1 배열로 둔다.
- KST 하루 경계와 UTC 생성 시각을 분리해 기록한다.
- 개인 운영 지표가 외부 URL에 노출될 수 있으므로 `visibility`와 `containsSensitiveData`를 렌더링/배포 판단에 사용한다.

## 7. 열린 질문

- 첫 구현 대상은 기존 Infinity report/static page인지, 별도 app repo인지 Developer가 repo를 본 뒤 확정해야 한다.
- 실제 데이터 원천은 cron history, OpenClaw session logs, memory status, Infinity intent files 중 어디까지 바로 읽을 수 있는지 확인이 필요하다.
- 공개 배포 시 개인 운영 지표가 노출될 수 있으므로 Operator가 접근 범위와 URL 공개 수준을 결정해야 한다.

## 8. Planner 판정

첫 8시간 MVP의 충분선은 "완전한 관측성"이 아니라 "매일 다시 열 이유가 있는 상태판"이다. 따라서 Developer는 그래프 수를 늘리기보다 아래 4가지를 먼저 통과시키는 편이 맞다.

- 지표별 최신성/fallback 여부가 숨겨지지 않는다.
- 오늘 상태가 가장 높은 P0/P1 issue와 연결된다.
- 모든 핵심 지표가 날짜 축 trend를 가진다.
- 다음 액션이 없으면 `오늘 개입 없음`이 명시된다.

## 9. 참조한 문서

- `/home/ubuntu/workspace/knowledge-lab/infinity/intents/active/build-14.md`
- `/home/ubuntu/workspace/knowledge-lab/infinity/artifacts/build-14/STATUS.md`
- `/home/ubuntu/workspace/knowledge-lab/agent-wiki/README.md`
- `/home/ubuntu/workspace/knowledge-lab/agent-wiki/content/docs/syntheses/observable-feedback-systems.mdx`
- `/home/ubuntu/workspace/knowledge-lab/agent-wiki/content/docs/mapped/deep-knowledge/monitoring.mdx`
- `/home/ubuntu/workspace/knowledge-lab/agent-wiki/content/docs/mapped/blog/Life_Tracking.mdx`
- `/home/ubuntu/workspace/knowledge-lab/agent-wiki/content/docs/syntheses/sufficient-boundary-for-next-action.mdx`
- `/home/ubuntu/workspace/prompt-archive/DESIGN.md`
- `/home/ubuntu/workspace/prompt-archive/DESIGN_SYSTEM.md`
- `/home/ubuntu/workspace/prompt-archive/BRAND.md`
