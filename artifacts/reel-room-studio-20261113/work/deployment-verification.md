# 승인된 운영 배포 검증 — 2026-11-13

사용자 “ㅇㅇ ㄱㄱ”는 직전 제시한 운영 배포·기존 두 진입 주소 전환과 이미지 2장·음성 1개·추천 1회 검증을 승인했다.

- 배포 전 상태: revision 71, ready 1, 활성 ffmpeg/node 프로세스 0.
- 복구 이미지: ghcr.io/shdkej/video-automation@sha256:b14727a531e797063e8677883ba09c4e10e528275f9177edb74681ec81cde44c.
- 대상 manifest의 Kubernetes server dry-run 통과. 기존 Basic Auth를 유지하며 외부 주소의 401 응답 확인.
- Argo CD는 기존 비공개 system-dashboard 서브모듈 인증 오류로 2026-11-06부터 ComparisonError. 전역 설정을 바꾸지 않고 원격 게시한 대상 Deployment만 직접 적용할 계획이다.
- 실제 OpenAI 호출은 운영 Secret을 메모리에서 읽고 동일 source a6c0164의 API 경로를 사용했다. 추천·이미지·음성 모두 상류 429(사용 한도/요청 빈도), 앱의 정제된 422로 전달. 생성 결과 0, 원문 보존 확인. 원본 키와 상류 본문을 로그에 남기지 않았다.
- 사용자에게 계정 크레딧·사용 한도 확인을 요청했다. 재호출·키 교체·결제 설정 변경은 하지 않았다.

당시 상태: 컨테이너 이미지 빌드 대기. 아래 최종 검증과 구분한다.

## 이미지 모델 수정

- 운영 키의 무료 모델 목록 조회 HTTP 200. 텍스트·음성 모델과 gpt-image-1.5를 확인했고 gpt-image-1은 목록에 없었다.
- 공식 Image API(https://developers.openai.com/api/reference/resources/images/methods/generate)는 gpt-image-1의 2026-10-23 종료와 1.5의 지원을 명시한다. 기본값을 1.5로 수정하고 운영 env에도 같은 값을 지정했다. 초기 구현의 누락이며 계정 한도 문제와 별개다.
- 기존 후보 생성 테스트에 현재 기본 모델 검증을 추가하여 RED→GREEN 확인, 공급자 테스트 50 passed. UI·합성 코드는 변경하지 않았다.

## 운영 1차 검증 및 패키지 보완

- 이미지 a6c0164 빌드 성공: https://github.com/shdkej/video-automation/actions/runs/43417940924 . Space bcddfc9 manifest를 원격 확인 후 대상 Deployment에 직접 적용했다. revision 72, ready 1, runtime digest sha256:772df48cab06e65828d3cddc656c1026b680ca540a85ce220fcfd625d6322bb9.
- 실제 운영 API로 이미지 2개·검증용 녹음 6초를 첨부하고 장면 2개를 합성했다. 1080×1920 영상+음성 스트림, 6.000000초, MP4/JPG/SRT/JSON 다운로드와 원문 보존·재열기를 확인했다. 운영 서비스 포트포워드의 브라우저 재생, 375/768/1440px 넘침·페이지 오류 없음. 외부 ingress는 기존 Basic Auth 401을 유지한다.
- 무료 참고 검색에서 운영 이미지의 직접 의존성 httpx 누락으로 500을 확인했다. 로컬 OpenAI 2.44.0/httpx 0.28.1과 Docker의 OpenAI 3.50.0/httpx 미설치 차이를 확인했다. requirements에 검증 버전을 명시하고 Docker import smoke를 추가했다. source b5d8b42의 원격 일치 검증 PASS.
- 현재 Pod에는 httpx 0.28.1을 임시 설치해 오류를 해소했고, 무료 검색에서 실제 이미지 8개와 capabilities HTTP 200을 확인했다. 영구 해결은 b5d8b42 이미지 교체 후 다시 확인한다. 임시 설치를 재시작 보존 증거로 취급하지 않는다.
- 사용자가 “AI 실호출 검증은 보류해”로 응답했다. 추가 유료 API 호출은 중단했다. 계정 한도와 성공 생성 품질은 미검증으로 남긴다.

## 최종 운영 결과

- source b5d8b42, 이미지 빌드 43421516272 성공. Space 2c2e592의 동일 manifest를 직접 적용했고 deployment revision 73 / ready 1이다. image digest와 pod는 deployment-final.json 참조.
- 새 이미지에서 OpenAI 2.44.0, httpx 0.28.1, gpt-image-1.5 설정을 확인했다. 임시 패키지 설치 없이 모듈 import와 무료 검색이 동작했다.
- Pod 교체 후 프로젝트 전체 JSON과 소재/출력 7개 파일의 SHA256 일치. 다시 생성한 MP4는 1080×1920·6초·음성 스트림 포함, 원문 보존. final-production-verification.json과 final-production-check.log 참조.
- 무료 Commons 참고 검색 10건(이미지·영상) 확인. 유료 API 재호출 없음.
- 기존 자동 컷 ?mode=cut에서 파일 업로드 화면과 페이지 오류 없음 확인. 기존 주소 3형태(독립 도메인, Infinity /instagram-maker/, /instagram-maker)가 실제 브라우저에서 보호된 Reel Room으로 이동했다. 정적 배포 43422740715와 43422987340 성공.
- 운영 배포·주소 통합·수동 제작·저장 보존 검증 완료. 유료 AI 실호출은 사용자가 보류했으며 계정 429와 성공 생성 품질은 남아 있다. 전역 Argo의 기존 서브모듈 인증 오류도 별도 운영 제약이다.
