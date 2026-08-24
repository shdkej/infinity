# research-32 수집·분석·결과 페이지 계약

## 이벤트 레코드

```json
{
  "event_id": "string",
  "stage": "problem|validation|build|launch|distribution|iteration|current",
  "occurred_at": "YYYY-MM-DD|null",
  "source_url": "string",
  "source_type": "video|description|official-web|social|secondary",
  "source_locator": "string|null",
  "published_at": "YYYY-MM-DD|null",
  "retrieved_at": "YYYY-MM-DDTHH:mm:ssZ",
  "quote": "<=25 words|null",
  "quote_word_count": "integer|null",
  "evidence_strength": "A|B|C|D",
  "directness": "direct_source|official_transcript|official_current_copy|secondary|unavailable",
  "claim_kind": "observed|reported|reported_plan|executed_observed|inference",
  "observed_metric": {
    "name":"string",
    "value":"string",
    "period":"string|null",
    "currency":"string|null",
    "unit":"string|null",
    "channel":"string|null",
    "metric_definition":"string|null",
    "gross_net":"gross|net|unknown|null",
    "as_of":"YYYY-MM-DD|null"
  },
  "interpretation": "string",
  "uncertainty": "string|null"
}
```

`source_locator`는 공식 페이지의 섹션·문단·transcript 문맥처럼 사람이 같은 근거를 다시 찾을 수 있는 위치다. 확인하지 못한 경우 `null`로 두고 추정하지 않는다. `quote_word_count`는 인용을 저장할 때 계산하며, 25단어 초과 인용은 저장하지 않는다.

`claim_kind`가 `reported` 또는 `reported_plan`이면 사례 당사자의 주장/계획이고, 독립적으로 실행됐다고 해석하지 않는다. `inference`는 원문 이벤트와 별도 표시한다. 숫자는 `metric_definition`, `period`, `channel`, `gross_net`, `as_of`가 채워지지 않으면 합산·성장률·MRR·순이익으로 변환하지 않는다.

## 최소 샘플

```json
{
  "event_id": "toneadapt-revenue-4-week-reported",
  "stage": "current",
  "occurred_at": null,
  "source_url": "https://www.starterstory.com/stories/i-turned-my-hobby-into-a-25k-month-app",
  "source_type": "video",
  "source_locator": "official transcript: revenue dashboard section, exact locator pending source export",
  "published_at": "2026-06-14",
  "retrieved_at": "2026-08-24T00:00:00Z",
  "quote": null,
  "quote_word_count": null,
  "evidence_strength": "A",
  "directness": "official_transcript",
  "claim_kind": "reported",
  "observed_metric": {
    "name": "recent four-week revenue",
    "value": "25000+",
    "period": "recent four weeks at interview time",
    "currency": "USD",
    "unit": "revenue claim",
    "channel": "web + mobile",
    "metric_definition": "interview-reported aggregate; gross/net unknown",
    "gross_net": "unknown",
    "as_of": null
  },
  "interpretation": "The figure is a reported observation, not independently verified MRR or net profit.",
  "uncertainty": "Exact dashboard date, gross/net definition, refunds, fees, and source screenshot are unavailable."
}
```

## 결과 페이지 업로드 계약

- 경로: Infinity가 생성하는 내부 결과 페이지(이번 범위에서는 구현/업로드하지 않음).
- 필수 섹션: 요약, 타임라인, 제품/가격, 분배 루프, 숫자 정의, 출처 목록, 미확인/Waiting, 재현용 다음 액션.
- 필수 메타데이터: `intent_id`, `source_video`, `retrieved_at`, `transcript_status`, `social_status`, `official_web_status`, `evidence_coverage`, `blockers`.
- 공개 경계: 원문 링크만 표시. 로그인 URL, 쿠키, API 키, 비공개 export, 개인 연락처는 저장/렌더링하지 않는다.
- 품질 게이트: 날짜 없는 주장은 날짜 있는 이벤트처럼 표시하지 않음; 매출 기간·채널·정의를 함께 표기; 해석과 원문 인용을 다른 블록으로 렌더링; blocker가 있으면 `partial/waiting` 배지.

## AI 분석 규칙

AI는 원문 이벤트를 먼저 추출한 뒤 연결·가설을 생성한다. 가설은 `inference`로 태그하고 A/B 근거와 혼합하지 않는다. 숫자 합산은 같은 기간·통화·채널일 때만 수행하며, 순매출/MRR/이익을 원문이 말하지 않으면 계산하지 않는다. “바이럴이 매출을 만들었다”는 인과가 아니라 순서상 관찰로만 기술한다.
