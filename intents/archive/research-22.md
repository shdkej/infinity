# research-22 — AI 자료수집·정리·관리 운영법 조사

- id: research-22
- status: archived
- completed_at: 2026-06-24T0800Z
- projects: [infinity, research-bank, personal-ops, knowledge-management]
- task_type: research
- topics: [ai-research, information-management, knowledge-base, source-verification, workflow]
- owner: Infinity
- requested_by: SeongHo Noh
- created_at: 2026-06-23T23:34Z
- permission_level: L1 research-only

## 결과 요약 (result_summary)

소스 코퍼스 사전 정의 + 최소 정보 단위(URL·날짜·판단메모) 유지가 "AI가 정리했지만 나중에 못 믿는 자료" 문제의 구조적 해법. 도구는 역할별 분리(수집→하이라이트→연결→문답→인용→공유), 루프는 일 5분·주 30분·월 2시간이 개인 현실 최소치.

## 핵심 발견

1. 소스 코퍼스를 먼저 정의하지 않으면 AI는 임의 출처를 혼합한다 — 허용 소스 목록이 신뢰의 시작점
2. 도구마다 한 단계만 담당해야 중복·충돌이 줄어든다
3. 정보 최소 단위 = 원문URL + 날짜 + 요약 + 신뢰도 + 판단메모
4. 중복·갱신 루프는 추가 시점이 아니라 주간 리뷰에 내장해야 함
5. 일 5분 캡처 + 주 30분 리뷰 + 월 2시간 합성이 지속 가능한 최소 구조
6. "못 믿는 자료" 5대 경고 신호: URL 없음·단일 소스·날짜 없음·AI 단독 요약·판단 맥락 없음

## 도구 역할 매핑

| 도구 | 담당 단계 | 핵심 강점 |
|------|----------|----------|
| Perplexity | 수집·발견 | 실시간 웹, 인용, Spaces 코퍼스 제한 |
| Readwise | 하이라이트 수집·복습 | Kindle/웹/PDF 통합, Obsidian 동기화 |
| Obsidian | 연결·장기 보관 | 오프라인, 그래프 링크, 공식 CLI |
| NotebookLM | 문답·합성 | 코퍼스 내 출처 인용 명확 |
| Zotero | 학술 인용 관리 | 메타데이터 완벽, 형식화 자동 |
| agent-wiki | 에이전트 공유 | SAM/Infinity 쿼리 가능 |

## 산출물

- reports: reports/research-22/2026-06-24T0800Z.html

## 다음 액션

- 실제 Obsidian 설정 적용: 사용자 판단
- agent-wiki 소스 신뢰도 기준 등록: 별도 intent 고려
- research-bank 운영 템플릿 추가: 별도 intent 고려
