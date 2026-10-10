# T1.1 범위·평가표·데이터 계약

## 목적과 연결
이 문서는 `acquisition-cashcow-research-20261010`의 T1.1 산출물이다. T1.2는 이 계약의 필드와 증거 규칙으로 공개 매물 목록을 만들고, T1.3은 같은 필드를 정규화한다. T2.1은 점수와 불확실성 표기를 입력으로 사용한다.

## 범위와 보호 경계
- 대상: Context Pack에 선언된 Hada 원문과 8개 공개 매물 사이트의 공개 목록.
- 허용: 로그인 없이 읽을 수 있는 페이지의 직접 원문 링크, 공개 가격·매출·이익·트래픽/사용자·운영 정보와 UTC 확인 시각 기록.
- 금지: 판매자 연락, 구매·계약·결제, 비공개 자료 요청, 계정 생성·로그인, 외부 발송·모집.
- 접근 제한·누락 수치는 빈칸으로 두며 추정값으로 채우지 않는다. 판매자 주장과 독립 확인값을 별도 표기한다.

## 후보 데이터 계약
각 후보는 최소 한 개의 직접 원문 링크와 UTC 확인 시각을 가져야 한다. 필드: `candidate_id`, `marketplace`, `listing_title`, `category`, `source_url`, `checked_at_utc`, `asking_price`, `currency`, `revenue`, `profit`, `traffic_or_users`, `owner_hours`, `transfer_scope`, `dependencies`, `growth_claim`, `seller_claims`, `independent_verification`, `confidence`, `unknowns`, `fit_stars`, `risks`.

금액은 원문 통화와 기간을 보존하고 환산 시 환율·기준일을 함께 쓴다. 매출·이익은 기간(월/연)과 정의(총액/순이익)를 보존한다. 수치가 없으면 `미공개`, 접근 불가면 `접근 제한`, 해당 없음은 `해당 없음`으로 구분한다. `checked_at_utc`는 실제 확인 시각이며 게시일과 혼동하지 않는다.

## 사용자 적합성 5점 기준
각 항목을 0~2점으로 평가하고 합계 0~10을 `floor(합계 / 2)`로 0~5점 별점으로 환산한다. 근거가 없는 항목은 0점이 아니라 `미평가`로 남기며 핵심 필드가 비어 있으면 보류한다.
1. 반복 현금흐름: 공개 이익·현금흐름 지속성 2, 매출만 확인 1, 근거 없음 0.
2. 1인 운영 가능성: 소유자 시간/업무와 작은 자동화·외주 범위 2, 일부 확인 1, 인력 의존/미공개 0.
3. 사용자 강점 활용: 제품·콘텐츠·자동화 역량의 구체적 개선 경로 2, 일부 1, 근거 없음 0.
4. 인수 후 개선 여지: 공개된 저활용 채널·가격·전환 여지 2, 가설 수준 1, 없음 0.
5. 검증 가능성: 가격·핵심 재무·이전 범위가 직접 원문 확인 2, 일부 1, 접근 제한/핵심 누락 0.

가격·필요 자본은 점수에 섞지 않고 `capital_risk`로 별도 기록한다. 별점 4 이상도 핵심 수치와 이전 범위가 공개 근거로 확인되고 1인 운영 조건을 충족할 때만 다음 검증 후보로 남긴다.

## 검증 및 연결
1. T1.2는 이 문서와 Context Pack search scope를 읽고 `marketplace-inventory.md`에 후보별 직접 링크·확인 시각·필드 누락을 기록한다.
2. T1.3은 원문을 다시 대조해 `candidate-ledger.md`에 기간·통화·정의를 정규화하고 판매자 주장/독립 확인을 분리한다.
3. T2.1은 `fit-scoring.md`에서 5개 항목별 점수, 근거 링크, 불확실성, 가격 민감도를 남긴다.
4. Red는 별점 계산, 출처 누락, 수치 혼동, 보호 경계 위반을 재현한다.

## 실행 검증 명령
```bash
test -s artifacts/acquisition-cashcow-research-20261010/work/scope-and-rubric.md
python -m json.tool artifacts/acquisition-cashcow-research-20261010/work/task-plan.json >/dev/null
rg -n "직접 원문 링크|checked_at_utc|1인 운영|구매·계약·결제|별점" artifacts/acquisition-cashcow-research-20261010/work/scope-and-rubric.md
git diff --check -- artifacts/acquisition-cashcow-research-20261010/work/scope-and-rubric.md
```

## 파일 경계와 롤백
이번 변경은 이 파일 하나에 한정한다. `INTENTS.md`, `task-plan.md/json`, trace, 다른 역할 산출물은 수정하지 않는다. 내용이 잘못되면 먼저 `git diff -- artifacts/acquisition-cashcow-research-20261010/work/scope-and-rubric.md`로 범위를 확인한 뒤 이 파일 변경만 복원한다. 후속 문서가 이미 계약을 참조했다면 차이를 deviation으로 기록하고 재검증한다.

## 완료 판정
`test -s`, JSON 문법 검사, `git diff --check`가 통과하고 필수 필드·점수 규칙·보호 경계·후속 연결이 모두 있으면 T1.1 증거가 충족된다. 이 문서만으로 후보 수집·재무 확인·인수 권고가 완료된 것은 아니다.
