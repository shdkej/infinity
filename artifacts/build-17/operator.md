# build-17 Operator

- 운영 범위: 로컬 정적 서버에서만 검증했으며 공개 배포·AWS registry·도메인·권한·비용 변경은 실행하지 않았다.
- 반복 운영: CSS/JS/font의 상대경로 200 응답과 두 dist 복사본 동기화를 확인했다. 390px/1440px 캡처를 `artifacts/build-17/`에 남겼다.
- 원격 게이트: 현재 `space` 저장소에 기존 사용자 변경이 다수 존재하므로 build-17 변경만 선별해 commit/push해야 한다. `knowledge-lab`은 infinity submodule pointer 갱신이 필요한 구조다.
- 우려: 기존 dirty 파일을 포함한 일괄 commit은 금지한다. 원격 push가 실패하거나 parent pointer를 확인할 수 없으면 Waiting으로 남긴다.
- 인계: Red가 코드·렌더·완료 기준을 독립 검증한 후에만 report/archive를 진행한다.
