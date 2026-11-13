# 승인된 운영 배포 검증 — 2026-11-13

사용자 “ㅇㅇ ㄱㄱ”는 직전 제시한 운영 배포·기존 두 진입 주소 전환과 이미지 2장·음성 1개·추천 1회 검증을 승인했다.

- 배포 전 상태: revision 71, ready 1, 활성 ffmpeg/node 프로세스 0.
- 복구 이미지: ghcr.io/shdkej/video-automation@sha256:b14727a531e797063e8677883ba09c4e10e528275f9177edb74681ec81cde44c.
- 대상 manifest의 Kubernetes server dry-run 통과. 기존 Basic Auth를 유지하며 외부 주소의 401 응답 확인.
- Argo CD는 기존 비공개 system-dashboard 서브모듈 인증 오류로 2026-11-06부터 ComparisonError. 전역 설정을 바꾸지 않고 원격 게시한 대상 Deployment만 직접 적용할 계획이다.
- 실제 OpenAI 호출은 운영 Secret을 메모리에서 읽고 동일 source a6c0164의 API 경로를 사용했다. 추천·이미지·음성 모두 상류 429(사용 한도/요청 빈도), 앱의 정제된 422로 전달. 생성 결과 0, 원문 보존 확인. 원본 키와 상류 본문을 로그에 남기지 않았다.
- 사용자에게 계정 크레딧·사용 한도 확인을 요청했다. 재호출·키 교체·결제 설정 변경은 하지 않았다.

현재: 컨테이너 이미지 빌드 대기, 운영 검증 진행 중. 성공으로 기록하지 않는다.

## 이미지 모델 수정

- 운영 키의 무료 모델 목록 조회 HTTP 200. 텍스트·음성 모델과 gpt-image-1.5를 확인했고 gpt-image-1은 목록에 없었다.
- 공식 Image API(https://developers.openai.com/api/reference/resources/images/methods/generate)는 gpt-image-1의 2026-10-23 종료와 1.5의 지원을 명시한다. 기본값을 1.5로 수정하고 운영 env에도 같은 값을 지정했다. 초기 구현의 누락이며 계정 한도 문제와 별개다.
- 기존 후보 생성 테스트에 현재 기본 모델 검증을 추가하여 RED→GREEN 확인, 공급자 테스트 50 passed. UI·합성 코드는 변경하지 않았다.
