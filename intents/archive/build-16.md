# build-16 — Instagram Maker 전면 재설계

- status: reopened
- target_agent: genie
- priority: high
- permission: workspace-local-only
- projects: infinity,static-sites
- task_type: redesign-and-verification
- topics: instagram-maker,layout,visual-hierarchy,responsive,red-team
- completed_at: 2026-08-07T13:15Z
- reopened_at: 2026-08-07T13:44Z
- reopen_reason: 사용자가 이전 완료 처리를 부정함. 기존 산출물·Red pass는 기준선으로만 보존하고 원본 대조 및 원격 반영 게이트를 포함한 재실행이 필요함.

## Planner

첫 화면의 주인공을 Instagram Story 제작 흐름으로 고정하고, “무엇을 만드는가 → 사진 업로드 → 저장”이 즉시 읽히는 것을 완료 기준으로 삼았다. Knowledge Lab README와 디자인·마케팅 근거의 정보 위계, 모바일 밀도, 안전 영역 원칙을 적용했다.

## Developer

기존 앱의 정적·로컬 처리 계약과 9:16/1080×1920, 이미지·영상 업로드, 3개 템플릿, 폰트·위치 선택, PNG/WebM 내보내기를 보존했다. 헤드라인·CTA 구조를 재정리하고 canvas 텍스트를 실제 측정 기반 자동 줄바꿈·축소로 교체했다. source와 artifact root 복사본을 동기화했다.

## Marketer

추상 카피 “사진 하나, 장면 하나”를 “사진을 올리면, 스토리 한 장”으로 구체화하고, 첫 CTA를 “사진을 올려 스토리 만들기”로 전진시켰다. 결과 CTA는 이미지 저장을 우선하는 현재 기능 구조에 맞춰 유지했다. 장식 추가는 기각했다.

## Operator

신규 도메인·AWS·외부 발송 없이 artifact 범위만 변경했다. Python 정적 서버로 로컬 HTTP 검증을 수행했고, index/CSS/overrides/JS 및 폰트의 상대 경로 200 응답, source/root SHA 동기화, `node --check`를 확인했다.

## Red

`red_status: pass`. 모바일·데스크톱 실제 렌더링, 텍스트 겹침·가로 넘침·캔버스 밖 표시, CTA 터치 높이, 외부 네트워크 의존성, `node --check`를 통과했다. Report: `artifacts/build-16/verification/red-report.html`.

## 결과 및 다음 액션

완료 기준을 충족해 Archive한다. 공개 배포는 이번 범위 밖이며, 별도 승인된 공개 대상이 생길 때 build-15 대기 intent에서 재평가한다.
