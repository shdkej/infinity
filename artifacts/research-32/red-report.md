# research-32 Red 검증 보고

검증 대상: `planner-prd.md`, `starter-story-toneadapt-deep-reconstruction.md`, `collection-analysis-contract.md`, `reports/research-32/20260824T-research.md`, `INTENTS.md`의 `research-32` 항목

## 네 문장 판정

- 방향이 맞나? **대체로 맞다.** 지정 영상의 사례를 문제→제작→공개·유입→반복·현재로 복원하고, YouTube/X 원문 접근 차단을 사실로 남긴 방향은 요청과 Knowledge Lab의 근거 제한 원칙에 맞다.
- 다음 액션이 있나? **있다.** YouTube 자막/영상 export와 Kyan X 게시물 URL 또는 export를 요청해 이벤트 레코드의 날짜·게시물 ID·반응·CTA를 보강한 뒤 재검증하면 된다.
- 선택이 맞나? **수정 필요다.** 공식 Starter Story transcript와 공식 웹을 부분 대체 근거로 선택한 것은 합리적이지만, PRD의 “각 사실에 URL·시점·인용” 계약을 실제 표의 행 단위로 구현하지 않았고, 인용·숫자 정의를 자동 검증할 필드가 부족하다.
- 요청과 맞나? **부분적으로 맞다.** 깊은 복원·재사용 계약·Waiting 경계는 제공했지만, 원문이 막힌 상태에서 완전 복원이나 Archive를 주장하지 않은 만큼 현재 산출물의 올바른 상태는 `waiting-partial`이며 Red 통과/Archive로 올리면 요청과 어긋난다.

## 핵심 반박과 작은 수정안

1. **행 단위 출처 계약 미충족**
   - `starter-story-toneadapt-deep-reconstruction.md`의 표는 `lines 212–224`처럼 비공식 위치 표기만 있고 행별 원문 URL, 게시일/검색일, 짧은 인용이 없다. PRD가 약속한 추적성을 충족하지 못한다.
   - 수정: 각 행에 `source_url`, `published_at|null`, `retrieved_at`, `quote`를 직접 추가하고, transcript는 공식 페이지의 섹션/문맥 앵커를 함께 기록한다. URL이 같은 공식 transcript라도 숫자·주장을 한 행씩 원문 문장에 연결한다.

2. **숫자·인용 검증 스키마가 약하다**
   - 계약의 `observed_metric`은 이름·값·기간만 있어 통화, 채널, 단위, gross/net, active/user 정의를 강제하지 않는다. `quote <=25 words`도 기계적으로 확인할 수 있는 언어·토큰 기준이 없다. 이 상태에서는 `$25K/month`, `100,000+`, `150,000+`, `4.9 rating`, `397명`이 서로 다른 정의라는 경계가 문서 밖 규칙에 머문다.
   - 수정: `currency`, `unit`, `channel`, `metric_definition`, `gross_net|null`, `as_of|null`, `quote_word_count`, `claim_kind: observed|reported|inference`를 추가하고, 합산 가능 조건을 동일 기간·통화·채널뿐 아니라 동일 정의로 명시한다.

3. **원문 사실과 해석의 경계는 좋지만 일부 문장이 앞선다**
   - 본문은 대부분 `해석(사실과 분리)`를 사용하고 “바이럴→매출” 인과를 피했지만, 한 문장 요약의 “반복해 … 5개월 안에”는 인터뷰 주장과 분석적 연결이 한 문장에 결합된다. `UGC 크리에이터 60회/월`, `Meta/TikTok 광고`도 실제 실행 로그가 아니라 인터뷰의 playbook/제안임을 표면에서 더 강하게 구분해야 한다.
   - 수정: 요약을 `인터뷰에서 Kyan은 …라고 말했다`와 `분석상 관찰되는 순서`로 분리하고, 이벤트 `claim_kind=reported_plan|executed_observed`를 사용한다. 실행 증거가 없으면 “계획/제안”으로만 표시한다.

## 추가 점검

- **인용/근거 강도:** A/B/C/D 라벨은 방향은 좋다. 다만 A가 “인터뷰 transcript”인지 “영상 화면에 보였다고 한 대시보드”인지 한 라벨 안에 섞여 있으므로 `source_type`과 `directness`를 분리해야 한다. 공식 웹의 현재 카피는 B로 남기되, 영상 시점 사실과 섞지 않는다.
- **추정과 사실 분리:** 전반적으로 양호하다. “정확한 날짜 미공개”, “독립 검증하지 않음”, “현재 상태와 영상 시점 성장률을 계산하지 않음”은 정직하다. 다만 위의 한 문장 요약과 “전환된 포맷은 공격적으로 확대” 같은 표현은 `reported`인지 `inference`인지 태그를 붙이는 편이 안전하다.
- **숫자 정의:** 가장 큰 수정 필요 지점이다. 최근 4주 매출, 최근 3개월 매출, 활성 구독자, 누적 사용자, 평점, 데이터베이스 수, 30초 응답은 기간·분모·측정 방식이 제각각이다. 원문이 정의하지 않은 값은 계산·성장률·MRR·순이익으로 변환하지 않는 현재 태도는 유지한다.
- **Waiting blocker의 정직성:** 통과. `reports/...`가 `red_status: pending`, `INTENTS.md`가 `status: waiting`, artifact가 `Waiting/부분 완료`를 유지하며 YouTube/X 차단을 숨기지 않는다. 사용자가 원자료를 제공하기 전에는 `red_status: pass`, `archived`, `Archive`로 바꾸지 않는다.
- **PRD·스킬 계약 재사용성:** 결과 페이지 필수 섹션과 공개 경계는 재사용 가능하다. 그러나 이벤트 스키마에 `retrieved_at`, `claim_kind`, 숫자 정의 필드와 원문 locator가 없어 다른 사례에 적용할 때 같은 추적성 문제가 반복된다. 위 필드를 계약에 추가하고 샘플 레코드 1개를 `reported metric`과 `inference` 각각으로 넣으면 충분하다.
- **시각 검증:** 결과 페이지가 구현·업로드되지 않았으므로 렌더링, 레이아웃, 배지 표시를 검증하지 않았다.

## 상태

판정: **수정 필요** (단, 원문 접근 blocker 자체는 정직하게 기록되어 `waiting` 유지)

권장 후속 순서: 계약 필드 보강 → 사용자 원자료 수령 → 이벤트 행별 locator/인용 보강 → Red 재검증 → 그 후에만 Archive 여부 판단.
