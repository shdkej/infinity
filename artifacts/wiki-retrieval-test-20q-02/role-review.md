# 역할별 실행 기록

- execution_mode: `single_genie_roles`. 기존 질문을 동일 기준으로 재조회하는 소규모 로컬 검증이므로 네 역할을 지니 내부 독립 pass로 수행했다. 이 런타임에는 역할 세션 spawn 도구가 노출되지 않았다.
- 경계: `agent-wiki/content/docs/`만 근거. 위키 본문 변경·공개 배포·Slack 발송 없음.

## Planner
목표/완료 기준: Q1–Q20의 상태·locator/부재 감사·01 대비 변화와 원인을 동등 기준으로 기록한다. 새 위키의 raw 출처 설명을 답 근거로 과장하지 않는다.

## Developer
`7e2e3d3..HEAD`의 6개 변경과 20개 질문 표면을 대조했다. BRANDING/9월 refresh는 대상 질문의 answer/alias/정량 locator를 추가하지 않아 20개 모두 불변이다. intent 전용 파일만 커밋하므로 revert 가능하다.

## Marketer
“브랜딩 탐색면 추가”와 “이 테스트 회수성 무변화”를 분리해 전달한다. 다음 개선은 대분류 증설이 아닌 실패 질문의 검색어 표면 보강이다. 외부 공유는 하지 않는다.

## Operator
Agent Wiki는 읽기 전용이고 기존 dirty/untracked는 스테이징하지 않는다. Infinity intent 전용 파일만 push한 뒤 `verify_archive_remote.py` PASS를 완료 조건으로 둔다. 이 테스트는 미기록과 컴파일 누락을 구분하지 못한다.
