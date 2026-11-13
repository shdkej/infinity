# Reel Room 통합 스튜디오 — 운영 검증 결과

기록 시각: 2026-11-13T12:21:57Z. 운영 배포·기존 주소 연결 완료. 유료 AI 실호출 검증은 사용자 요청으로 보류.

## 현재 결과

- 운영: https://reel.oracle.shdkej.com/ . 기존 Basic Auth 유지.
- 운영에 사용한 source `b5d8b42e49280ff68fc45c078ada23916c8b5efa`, 배포 시 master 원격 SHA 일치 PASS. 이후 배포 주석만 수정한 문서 커밋 `4baee7e83fab00f34d07127e5c38dbddfb17eb6c`도 master 원격 검증 PASS. 최종 컨테이너 빌드: https://github.com/shdkej/video-automation/actions/runs/43421516272 .
- 운영 manifest: Space `2c2e5923033a2d832592a5dc84670ceb4f474270`. Deployment revision 73, ready 1, digest `sha256:7cce8be049cbda86880ca48940f8839b82b9d361ac8e02074439d92830c5c2b8`.
- Instagram Maker 독립 주소와 Infinity 내 주소(슬래시 유무 포함)가 스튜디오로 이동한다. Space 정적 배포 43422740715·43422987340 성공, 실제 브라우저 이동 검증 PASS.

## 확인한 동작

- 전체 Python 테스트 186 passed / 49 deprecation warnings. 모델·패키지 수정 뒤 공급자 테스트 50 passed. TypeScript/Vite build, 대상 lint, Docker의 Studio import 검증 PASS.
- 운영 API에서 대본 저장 → 이미지 2개·녹음 6초 업로드 → 자막 2장면 → 실제 1080×1920 MP4(영상·음성) → 저장/재열기·다운로드 PASS. 테스트 소재와 음성은 합성 fixture이며 실제 사용자 녹음이나 AI 생성물이 아니다.
- 운영 브라우저에서 MP4 재생, 375/768/1440px 넘침·페이지 오류 없음, 기존 자동 컷 업로드 화면 확인.
- 새 이미지로 Pod 교체 후 프로젝트 전체 JSON 및 소재·출력 7개 파일 SHA256 일치. 교체한 이미지에서 다시 MP4 출력 PASS.
- 실제 Commons 참고 검색에서 이미지·영상 10개 확인.

## 수정과 남은 한계

초기 기본 이미지 모델의 종료와 컨테이너의 httpx 의존성 누락을 운영 검증에서 찾았다. gpt-image-1.5로 변경하고 OpenAI 2.44.0/httpx 0.28.1을 명시했으며 Docker import 검증을 추가했다. 중간 Pod의 임시 패키지 설치는 최종 검증으로 취급하지 않았고, 새 이미지에서 다시 확인했다.

운영 키의 무료 모델 목록 조회는 인증 성공했지만 추천·이미지·음성 생성 요청은 상류 429로 실패했다. 이후 사용자가 “AI 실호출 검증은 보류해”라고 응답했다. 추가 유료 호출·키 교체·결제 설정 변경은 하지 않았다. 성공 생성 품질은 미검증이다. 자막은 장면 단위이며 자동 발화 정렬은 제공하지 않는다.

Argo CD는 기존 다른 비공개 서브모듈 인증 실패로 자동 동기화가 멈춰 있다. 이번에는 원격 게시한 동일 대상 Deployment만 직접 적용했다. 전역 설정은 변경하지 않았고 운영·복구 절차는 Space apps/reel-room/README.md에 기록했다.

## 실행·맥락·상태

Codex 세션 01a1d48d-86d8-70d0-94e3-a36084a5dde5, purplemux ws-E3W-XA/tab-hMqhUf가 실행했다. 기존 Context Pack 두 개는 intents/context/reel-room-studio-20261113.json 및 reel-room-studio-20261113-product.json이다. 별도의 Genie 구현 인계나 외부 메시지를 만들지 않았다. notification_channel delivery_unknown은 발송 불가 예약값이다.

사용자의 “ㅇㅇ ㄱㄱ”로 배포·주소 전환·실호출 검증을 승인받았고, 이후 유료 검증만 명시적으로 보류됐다. 원장은 Waiting/user를 유지하며 기다리는 대상은 AI 검증 재개 결정이다. 운영 배포의 재승인을 요구하지 않는다. 상세 증거: deployment-verification.md, final-production-verification.json, deployment-final.json, browser-redirects.json, browser-production.log, pytest.log.
