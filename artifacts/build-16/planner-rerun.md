# build-16 재실행 Planner

- 대상: 원본 `instagram-maker` 번들과 기존 build-16 산출물의 재대조
- 문제: 이전 완료는 사용자 지적 배치 문제와 원격 게이트를 닫지 못함
- 기준: 9:16 Story 제작 흐름, 모바일에서 편집 단계가 미리보기보다 먼저 읽히고 데스크톱에서는 편집 패널이 화면에 남아야 함
- 제외: 신규 도메인·AWS·공개 발송. build-15 공개 배포는 URL/registry/인프라 부재로 별도 Waiting
- 근거: `agent-wiki/README.md`의 관찰 가능성·변경 가능성·공개 인터페이스 분리 원칙, 원본 tar 목록 및 build-15 보고서

완료 기준은 실제 산출물 수정, 모바일·데스크톱 렌더 확인, 역할별 기록, Red pass, HTML report, 두 저장소 원격 반영 확인이다.
