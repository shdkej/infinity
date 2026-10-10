# Red 최종 검증 — acquisition-cashcow-research-20261010

검토 시각: 2026-10-10 UTC  
검토 범위: `candidate-ledger.md`, `fit-scoring.md`, `task-plan.md/json`, 최종 보고서, Context Pack  
외부 발송·구매·판매자 연락·계약·결제: 없음

## 최종 판정: FAIL(수정 필요)

별점 과장은 제거되었고 승인 경계도 지켜졌다. 그러나 후보별 source metadata는 직접 원문 재현 조건을 충족하지 못하고, Context Pack 연결은 경로·필드·후보별 증거까지 이어지지 않는다. 또한 task plan이 참조하는 `work/remote-proof.txt`가 없어 증거 체인이 종결되지 않았다.

## 요구사항별 검증

- **요청 일치 및 승인 경계 — PASS**
  - **직접 증거:** Context Pack의 `request`, `rules[4]` 및 최종 보고서가 공개 매물 조사, 1인 운영·현금흐름 비교, 구매·연락·계약·결제·비공개 요청 제외를 명시한다.
  - **반례 확인:** 외부 발송·판매자 접촉·구매 실행 증거 없음.
  - **다음 조치:** 없음.

- **후보별 출처 metadata 및 수치 재현성 — FAIL**
  - **직접 증거:** `candidate-ledger.md` metadata 표에 후보별 `source_url`, `checked_at_utc`, 통화, 기간/지표 정의, 출처/신뢰도, 짧은 원문 표시가 있고 확인 시각은 `2026-10-10T21:50Z`로 고정되어 있다.
  - **반례 확인:** 10개 중 8개 후보의 URL이 `https://quietlight.com/listings/` 목록 루트뿐이다. 따라서 `$43K MRR`, `9% YoY`, `~$46K SDE`, 매출·이익을 후보별 직접 원문에서 재현할 수 없다. `scope-and-rubric.md`의 후보별 직접 원문 링크 계약과 충돌하며, 대부분 통화도 `USD 표기 추정`, 기간·정의는 미확인이다.
  - **다음 조치:** 실제 listing URL 또는 접근 불가를 후보별로 명시하고 원문 인용·통화·기간·정의를 직접 연결한다. URL을 못 얻으면 수치를 보류한다.

- **별점 산식·상태 재현성 — PASS(조건부)**
  - **직접 증거:** `fit-scoring.md`가 5축 0~2점, `floor(S / 2)`, 근거 없는 축은 0이 아닌 `미평가`, 핵심 필드 누락 시 보류를 명시한다. 10개 후보가 모두 미평가/보류이고 4점 이상 확정 0개라는 결론도 일치한다.
  - **반례 확인:** 이전의 근거 없는 숫자 별점은 현재 파일에서 확인되지 않는다. 다만 축별 증거 URL·인용이 없어 실제 산출까지 완전 재현되지는 않는다.
  - **다음 조치:** 근거 추가 시 축별 원점수·인용·합계를 함께 기록한다.

- **사용자 근거 경로 및 필드 연결 — FAIL**
  - **직접 증거:** `fit-scoring.md`는 `intents/context/acquisition-cashcow-research-20261010.json`의 `request`, `evaluation_rubric.fit_stars`, `rules[0..4]`를 언급하며, Pack에는 `candidate_fields`(`owner_hours`, `transfer_scope`, `source_url`, `checked_at` 등)가 있다.
  - **반례 확인:** 후보별 표에 Context Pack 필드별 경로·값 연결이나 5축 증거 링크·인용이 없다. 자본·현재 역량이 Pack에 없다는 한계는 적었지만, 후보별 사용자 적합성 근거는 재현 불가하다.
  - **다음 조치:** 해당 JSON pointer/필드명을 명시하고 없는 자본·역량은 계속 미평가로 둔다.

- **task-plan JSON/MD 시각·증거·상태 일치 — FAIL**
  - **직접 증거:** JSON의 T2.2(22:02–22:20), T2.3(21:50:41–22:20:26), T2.4(active, 22:20:26~)와 MD의 상태 및 “다음 행동: T2.4”는 대체로 일치한다.
  - **반례 확인:** T2.4 evidence가 `work/red/final-review.md; work/red/final-review-r2.md; work/remote-proof.txt`인데 마지막 파일이 존재하지 않는다. 따라서 원격 반영 증명까지 완료된 상태로 볼 수 없다.
  - **다음 조치:** 실제 증거만 참조하거나 `remote-proof.txt`를 생성하고 JSON/MD의 T2.4 상태·완료 시각을 함께 갱신한다.

## 핵심 반박

1. metadata 표는 형식상 존재하지만 목록 루트 URL은 후보별 직접 출처가 아니므로 재현성 FAIL이다.
2. Context Pack 경로를 인용한 것과 후보별 필드·축별 증거를 연결한 것은 다르며 현재는 전자만 충족한다.
3. T2.4가 active인 것은 일관되지만 미존재 `remote-proof.txt`로 증거 체인이 끊겼다.

## 결론

승인 경계와 보수적 미평가 처리는 PASS다. 그러나 **source metadata/재현성, 사용자 근거 경로, task-plan 증거 종결이 FAIL**이므로 수정 후 재검증이 필요하다.
