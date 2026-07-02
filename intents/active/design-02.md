# [design-02] 카드뉴스 첫페이지 후킹 개선 실험

- id: design-02
- status: active
- priority: high
- target_agent: workflow-master
- schedule_window: 2026-07-02 05:00-08:00 KST
- projects: content, card-news, design-system
- task_type: design
- topics: card-news, hook, cover

## 목표
카드뉴스 첫 페이지가 스크롤을 멈추게 하는 힘을 높이기 위해 제목/이미지/여백/첫 문장 조합을 실험하고, 실험 결과와 다음 개선사항을 남긴다.

## 현재 상태
- Active 등록 완료 (2026-07-01)
- 실행 대기: **2026-07-02 05:00-08:00 KST** 윈도우 도래 시 시작
- 2026-07-01 22:07 UTC heartbeat에서 bounded triage 완료. 최근 카드뉴스 원본/preview 경로 확인이 이 사이클 범위를 넘어서므로, 다음 로컬 실행자가 바로 열 파일/판정축/금지사항을 `reports/design-02/2026-07-01T2207Z-handoff.html`에 고정했다.
- 2026-07-02 03:08 UTC heartbeat에서 현재 시각이 **2026-07-02 12:07 KST**로 실행 윈도우를 지난 상태임을 확인했다. 이번 사이클은 미실행 handoff로 닫고, 다음 실행 범위와 재개 조건을 `reports/design-02/2026-07-02T0308Z-handoff.html`에 추가 기록했다.
- 같은 heartbeat에서 `infinity` 로컬 커밋은 생성됐지만 `origin/main`이 선행되어 push가 fast-forward 거절되었다. 원격 동기화가 정리되기 전까지는 이 handoff를 완료/보관 처리하지 않고 Active로 유지한다.

## 다음 액션 (2026-07-02 05:00 KST 이후)
1. 최근 카드뉴스 3-5세트의 첫 페이지를 골라 `왜 멈추지 않는지 / 왜 읽히는지` 한 줄씩 판독
2. hook 가설 3개 이상 도출 (keyword-title / 이미지 구도 / 첫 문장 조합 기준)
3. 개선 후보 3개를 가독성/호기심/주제 명료성/브랜드 결/모바일 안전영역 기준으로 비교
4. 실험 결과 요약, 이긴 hook 원칙, 버린 원칙, 다음 카드뉴스에 바로 적용할 개선안 3개
5. 필요 시 샘플 preview 1개

## 연관
- design-01의 미감 감사 결과(실행 규칙 문서)를 기준으로 활용
- 카드 1 제목은 keyword-title 기준 통과 필수
- 첫 장은 기존 업로드 실사진 우선 사용

## 제약
- 2026-07-02 08:00 KST 전에 작업을 닫는다
- 승인 없이 공개 라이브러리 배포, 기존 카드뉴스 교체, 대량 재생성, 외부 비용, 이미지 임의 생성 대체 금지

## 완료 기준 (success_criteria)
- 실험 결과 요약 및 이긴 hook 원칙
- 다음 카드뉴스에 바로 적용할 개선안 3개
- HTML 리포트 (`reports/design-02/{timestamp}.html`)
