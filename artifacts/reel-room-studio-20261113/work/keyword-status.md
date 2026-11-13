# 키워드·참고 검색·클라이언트 AI 키 — 운영 확인

- 기준 시각: 2026-11-13T13:05:35Z
- 구현 source: f8d5edef7c2d1563c6edbc65ad24adbf5af04a18; 사용 문서 commit: 4ef64d2ec29c5b37a8260eb78065a129501376ce
- 배포 manifest: Space 35d738f7a0fcf183e5150b72e62d9740cdc654de, revision 74 ready 1. 이미지 빌드 43429546562 성공.
- 실제 운영: Naver SearchAd 후보 45개/전체872, YouTube 한국어 영상6, Commons 이미지8. 375/768/1440px 넘침/JS오류 없음; 선택·저장/복원 통과. 기존 샘플 파일14개 SHA256 동일. 기존 Basic Auth 유지.
- AI 키는 화면에서 입력 가능. 브라우저 저장소·프로젝트에 저장하지 않고 현재 탭의 AI 요청에만 헤더로 전달한다. 서버 요청별 키 사용과 원래 서버 키 복귀는 모의 SDK로 검증. UI에서는 가짜 키와 가로채기 요청으로 검증했으며 실과금 호출0회.
- 검증: 전체 Python212 pass/49 기존경고, TypeScript/Vite build, oxlint(기존경고8). 실제 공급자 키워드/참고 검색과 미리보기 로딩 확인.
- 남은 범위: 유료 AI 실호출은 사용자 지시로 계속 보류. 기존 OpenAI 계정429 해결/생성품질 미검증. YouTube 영상에 따라 임베드가 제한되면 원본 링크 사용. 전역 Argo 기존 서브모듈인증오류는 별도문제.
- 복구: 이전 source b5d8b42/digest7cce8be로 image를 되돌리고 studio 영구볼륨 유지. 신규 서버 검색 키는 같은 사용자 스킬계정에서 필요한4개 항목만 기존 Secret에 연결했고 비밀값은 로그/Git/브라우저에 출력하지 않았다.
