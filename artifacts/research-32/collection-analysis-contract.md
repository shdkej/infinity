# research-32 수집·분석·결과 페이지 계약

## 이벤트 레코드

```json
{
  "event_id": "string",
  "stage": "problem|validation|build|launch|distribution|iteration|current",
  "occurred_at": "YYYY-MM-DD|null",
  "source_url": "string",
  "source_type": "video|description|official-web|social|secondary",
  "quote": "<=25 words",
  "evidence_strength": "A|B|C|D",
  "observed_metric": {"name":"string","value":"string","period":"string|null"},
  "interpretation": "string",
  "uncertainty": "string|null"
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
