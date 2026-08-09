# build-17 — Spatial Type Status implementation

## Planner

- 목표: 5초 안에 현재 상태, 지금 읽을 것, 다음 행동을 파악하게 한다.
- 범위: Status 정적 표면의 첫 화면 구조·타입·행 문법과 디자인 문서 갱신. `status.json`, 상세 탭, 근거 모달 데이터 계약은 유지.
- 근거: `sites/status/DESIGN.md`, `DESIGN_SYSTEM.md`, Knowledge Lab의 `context-over-inventory` 및 운영 원칙. Spatial Type/BRAND 직접 정본은 공백으로 기록.
- 완료 기준: 모바일/데스크톱 텍스트 겹침 없음, 접근성 이름 유지, 라이브 URL 반영, Red pass report.

## Developer

- 구현: 기존 HTML/CSS 정적 산출물의 hero와 Now/Balance/Loop 표면을 글래스 카드에서 텍스트 우선 읽기 흐름으로 전환.
- 영향 경계: `status.json` fetch, `buildModel`, 상세 패널, 탭 이벤트, reason modal을 변경하지 않음.
- 롤백: `git revert`로 `index.html` 및 디자인 문서 변경만 되돌릴 수 있음.

## Marketer

- 판단: `All systems / quiet & running`의 큰 타입과 짧은 상태 문장은 운영 대시보드의 첫인상을 장식보다 판독 중심으로 만든다.
- 제안: 카드 제목을 긴 설명으로 늘리지 않고 수치·상태·행동을 짧게 유지한다. 외부 카피 발송은 해당 없음.
- 인계: 상세 화면에서만 세부 객체를 호출하는 현재 구조를 유지한다.

## Operator

- 판단: 정적 사이트라 배포 표면은 `sites/status/dist/`이며 GitHub Actions 경로와 라이브 URL을 확인해야 한다.
- 우려: 작업 트리에 기존 무관 변경이 많으므로 대상 파일만 커밋한다. CloudFront 직접 명령은 중복 배포를 피하고 저장소 Actions를 우선한다.
- 인계: push 후 Actions 및 `https://status.aws.shdkej.com` 응답/HTML 반영 확인.

## Workflow master decision

- 합의: 데이터 계약과 상세 기능을 보존하고 첫 화면의 표현 계층만 Spatial Type 방향으로 최소 변경한다.
- 기각: 새 컴포넌트 프레임워크 도입, status.json 스키마 변경, 기존 3D/마스코트 자산 제거, 외부 카피 발송.
- 최종 순서: Active 구조화 확인 → CSS/문서 구현 → 정적·접근성 검증 → 대상 파일 commit/push → 라이브 확인 → Red 검증 → Archive.
