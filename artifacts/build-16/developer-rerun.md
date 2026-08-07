# build-16 재실행 Developer

원본 tar는 `index.html`, `styles.css`, `app.js`, 동봉 폰트 3종으로 구성됨을 재확인했다. 기존 build-16은 원본 대비 전면 UI 재작성본이며, 이번 재실행에서는 artifact/source 정본에만 배치 보정을 적용했다.

- 모바일: 편집 패널을 먼저 노출하고 미리보기를 뒤로 보내 작업 순서(업로드→템플릿→문구→저장)가 화면 순서와 일치하도록 수정
- 데스크톱: 편집 패널을 sticky로 고정해 긴 폼에서 컨트롤이 화면 밖으로 사라지지 않도록 수정
- 동기화: `source/overrides.css`와 artifact root `overrides.css` 일치
- 검증: `node --check` 통과, 외부 fetch/URL 없음, 원본 파일명·상대 폰트 계약 보존
