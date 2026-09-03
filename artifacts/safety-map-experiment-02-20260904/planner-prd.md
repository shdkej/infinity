# Safety Map Experiment 02 — Planner PRD

- intent: `safety-map-experiment-02-20260904`
- artifact role: `design`
- status: planning baseline; implementation is not authorized by this document alone
- canonical deadline: `2026-09-04T06:00:00Z` (`2026-09-04 08:00 Europe/Rome`)
- source of deadline: active canonical block in `INTENTS.md`
- context pack: `intents/context/safety-map-experiment-02-20260904.json`

## 1. 목표와 비목표

### 목표

로마에서 사용자가 **실제 Mapbox canvas**로 장소·도로·상대적 거리·현재 선택 위치를 탐색하고, 주야간 지도 레이어를 전환할 수 있는 최소 지도 경험을 만든다. 첫 화면은 사용자가 5초 안에 “로마의 장소 맥락을 지도에서 탐색한다”와 다음 행동 하나를 이해하게 해야 한다.

실험의 성공은 안전 점수를 생산하는 것이 아니라, 실제 지도 UX·디자인·운영·검증 게이트를 같은 실행 계약 안에서 증명하는 데 있다.

### 비목표

- 범죄·치안·위험도 등급, 안전 경로, 실시간 위험 예측, 여행 안전 보장
- fixture를 실제 안전 데이터 또는 사용자 수요 검증으로 표현하는 일
- Travel Ops 재사용, 공개 광고·결제·계정/권한/시크릿 변경
- 토큰 값의 소스·Terraform·로그·커밋 노출
- 이 PRD만으로 배포 또는 terminal Slack 발송을 승인하는 일

## 2. 사용자 경험과 Mapbox canvas 수용 기준

### 핵심 흐름

1. 사용자는 “로마 장소 탐색”이라는 한 문장과 하나의 시작 행동을 본다.
2. 실제 canvas에서 Trevi Fountain 등 장소를 검색·선택한다.
3. 선택 위치와 주변 도로·상대 거리 맥락을 읽고, zoom/pan으로 직접 탐색한다.
4. 주간/야간 레이어를 전환한다.
5. 안전 근거가 없는 영역은 의미를 꾸미지 않고 `no-data`와 짧은 이유를 본다.

### 필수 acceptance criteria

| ID | 수용 기준 | 통과 증거 |
| --- | --- | --- |
| UX-01 | 실제 Mapbox GL canvas가 390px와 desktop에서 렌더된다. 정적 이미지·HTTP 200·style API 응답은 대체 증거가 아니다. | 각 viewport의 실제 브라우저 capture 및 DevTools/테스트 기록 |
| UX-02 | 사용자가 zoom과 pan을 수행해 도로·장소 맥락의 변화를 확인한다. | 상호작용 전/후 capture 또는 재현 가능한 브라우저 테스트 |
| UX-03 | 장소 검색·선택으로 위치와 상대 거리 맥락을 읽는다. | 검색 결과와 선택 상태 capture |
| UX-04 | 주간/야간 레이어 전환이 실제 canvas에 반영된다. | 전환 전/후 capture |
| UX-05 | 390px에서 가로 overflow 없이 키보드/스크린리더 라벨로 검색·레이어 제어에 접근한다. | `scrollWidth <= innerWidth`, 접근성 이름 검사, mobile capture |
| UX-06 | 안전 등급·경로·예측을 주장하지 않는다. 근거 없는 안전 정보는 `no-data`와 출처 부족 사유로 표시한다. | 화면 capture 및 provenance 검사 |

## 3. 디자인 정본 매핑

`BRAND.md → DESIGN.md → DESIGN_SYSTEM.md` 순서로 적용한다. 아래는 구현 전 확인해야 할 화면 요소별 계약이다.

| 화면 요소 | 정본 원칙 | 구현 판단 |
| --- | --- | --- |
| 첫 화면/주요 행동 | BRAND: 시작 장벽을 낮추고 부드러운 한국어로 안내 | “로마 장소를 탐색해보세요” 한 행동만 전면 배치; 여러 동등 CTA 금지 |
| 제목·상태·출처 | DESIGN: Warm clarity, 구조가 카피보다 먼저 | `DisplayText`, `CurrentState`, `ContextLabel`로 지도 상태·데이터 한계를 분리 |
| 지도 | DESIGN_SYSTEM: Layer 2 `FocusField`, Layer 3 `DataObject` | canvas는 탐색의 중심 객체이며, 카드 격자나 장식용 미리보기가 아님 |
| 검색/레이어 전환 | DESIGN_SYSTEM: `ActionPrompt`, `Summon`, `Focus` | 지도 위 과도한 floating UI 대신 문장형 프롬프트와 접근 가능한 조작부 사용 |
| no-data | DESIGN: 따뜻함은 복구 경로를 제공 | 사용자 탓 없이 “이 구간은 확인 가능한 안전 근거가 없어요”와 탐색 지속 경로 제시 |
| 색·타입·접근성 | BRAND/DESIGN_SYSTEM: subtle sky, Pretendard, WCAG AAA 목표 | 라이트 기본, semantic token, 충분한 대비, 키보드 focus와 의미 있는 라벨 유지 |

## 4. 데이터·provenance 경계

### Map data

- Mapbox는 **지리적 탐색 맥락**(지도, 도로, 장소, 위치, 거리, 레이어)만 제공한다.
- 공개 클라이언트 요청에서 의도적으로 사용되는 도메인 제한 Mapbox public token도 값 자체는 이 artifact·코드·로그·커밋에 남기지 않는다.
- protected Gateway → ignored runtime config → client Mapbox GL 경로만 사용한다. 설정 변경·토큰 회전·권한 변경은 별도 승인이다.

### Safety data

- 검증되고 날짜가 명시된 출처가 없으면 모든 치안 신호는 `no-data`다.
- fixture는 UI 상태/데이터 한계를 설명할 수 있으나 실제 위험·범죄·안전 주장의 근거가 될 수 없다.
- 안전 점수, 위험 예측, 안전 경로와 같은 고위험 결정 UI는 본 실험 범위 밖이다.

### 개인정보·주장 경계

- 위치는 사용자가 검색·선택한 공개 장소 맥락으로 제한하며, 사용자 위치 수집·저장은 하지 않는다.
- “안전하다”, “안전한 경로”, “위험이 낮다” 같은 보증 표현을 쓰지 않는다.

## 5. 도구 역할

| 도구 | 허용 역할 | 금지 역할 |
| --- | --- | --- |
| Mapbox GL | 실제 지리 canvas, 장소/도로/거리 맥락, zoom/pan, 레이어 전환 | 안전 등급·예측·경로 보장 생성 또는 token 값 노출 |
| Gateway/runtime config | protected 설정을 ignored runtime artifact로 주입 | token을 소스·Terraform·로그·커밋으로 복사 |
| Remotion | 지도 UX를 대체하지 않는 설명/데모 영상 또는 정적 보조물 | 실제 canvas·상호작용·390px/desktop 검증의 대체 증거 |
| focused Red | 실제 렌더, provenance, 배포·주장 경계의 독립 검토 | timebox를 이유로 P0 또는 미응답을 pass 처리 |

## 6. 마일스톤·evidence 경로

| Milestone | 산출물/검증 | evidence path |
| --- | --- | --- |
| M0 Context & boundary | Context Pack 재확인, scope/approval/provenance lock | `intents/context/safety-map-experiment-02-20260904.json`, 이 PRD |
| M1 Planner | 본 PRD와 acceptance criteria | `artifacts/safety-map-experiment-02-20260904/planner-prd.md` |
| M2 Developer | 전용 safety-map 구현 및 local testable artifact | Space의 명시 safety-map 파일, 테스트 출력 경로를 실행 report에 기록 |
| M3 Marketer + Operator | 카피/위계 검토, 전용 배포·시크릿·Terraform 경계 검토 | role artifact 또는 HTML run report의 역할별 섹션 |
| M4 Render | 390px·desktop 실제 canvas 상호작용 capture | `artifacts/safety-map-experiment-02-20260904/evidence/` 아래 immutable capture/검증 파일 |
| M5 Red | core/render, provenance, deployment/claims focused review | `artifacts/safety-map-experiment-02-20260904/red-focused-*.md` |
| M6 Remote & terminal | push/remote proof, immutable Slack delivery receipt | HTML report 및 terminal receipt ledger reference |

각 stage transition은 새 artifact, test result, 실제 capture, source commit 또는 정확한 external blocker 중 하나를 `stage_evidence_at`과 함께 기록한다. handoff만으로는 진전이 아니다.

M4 evidence는 덮어쓰지 않는다. 파일명은 `YYYYMMDDTHHMMSSZ-{viewport}-{interaction}.{png|json|txt}`로 만들고, 실행 report에는 각 파일의 SHA-256과 해당 source commit을 기록한다. 예: `20260904T041500Z-mobile-390-layer-toggle.png`.

## 7. 마감과 quality iteration

- hard deadline은 `2026-09-04T06:00:00Z`이다. 이전 `20260903T1105Z-deadline-missed.md`의 과거 마감 기록은 재개 전 상태의 기록이며, 현재 canonical Intent가 우선한다.
- 기능이 조기 동작해도 Archive하지 않는다. deadline 전에는 디자인·실제 렌더·접근성·운영 품질을 quality iteration으로 개선한다.
- 새 실질 evidence가 없는 dispatcher cycle이 한 번이면 `stale_progress`, 두 번 연속이면 정확한 blocker와 함께 Waiting으로 전이한다.
- deadline을 넘기면 반복 handoff·Active 유지·terminal completion을 하지 않는다. `deadline_missed` report와 마지막 evidence를 남기고 Waiting으로 전이한다.

## 8. Red와 Slack terminal gate

### Red gate

Archive 또는 terminal completion 전에 focused Red가 아래를 직접 검토해 `pass`를 남겨야 한다.

1. 실제 desktop·390px canvas에서 장소/도로, zoom/pan, 거리/위치, 레이어 상호작용
2. `no-data` 안전 경계, 출처·날짜·신뢰도, 개인정보 및 과장 없는 표현
3. 전용 safety-map 배포 경로, token 비노출, remote proof, claims/광고 분리

P0, timeout, 미응답은 pass가 아니라 Waiting blocker다. remediation은 해당 lane만 수행하고 targeted rerun 및 cross-check를 남긴다.

### Slack terminal gate

- Intake의 `notification_channel`, `notification_target`, `notification_reply_to`를 immutable하게 보존한다.
- 원 대화 destination의 delivery receipt(또는 명시적 `delivery_unknown`) 없이는 terminal로 닫지 않는다.
- quality iteration 중에는 원 스레드에 한 번의 비종결 진행 알림만 허용하며, 중복 발송하지 않는다.
- 공개 발송·배포는 별도 승인 경계를 따른다. 본 PRD는 발송 승인이 아니다.

## 9. 역할 수렴과 다음 실행

| 역할 | 판단·우려 | 다음 인계 |
| --- | --- | --- |
| Planner | 지도 탐색과 안전 주장을 분리하고, 실제 canvas 증거를 완료 기준으로 고정 | M1 PRD 후 M2 구현은 새 deadline/재개 승인 범위에서만 시작 |
| Developer | protected runtime config와 전용 배포 경계를 보존해야 함 | 안전 데이터 없이 no-data UI를 유지하고, 실제 interaction test를 준비 |
| Marketer | 최소 카피와 하나의 주요 행동이 첫인상을 좌우 | 과장 없는 no-data 문구와 텍스트 우선 위계를 구현 검토 |
| Operator | Space worktree가 dirty하므로 명시 safety-map 파일만 stage; token/Travel Ops 재사용 금지 | deploy 전 Terraform no-change, live capture, remote proof, Slack receipt를 확인 |

**다음 행동:** 이 PRD의 필수 항목을 Active Intent와 execution ledger에 연결한 뒤에만 구현을 재개한다. 새 deadline 또는 재개 권한이 사라지거나 만료되면 즉시 Waiting으로 전이한다.

### Implementation readiness hold

현재 canonical Intent는 Waiting이며, blocker 본문에 이전에 만료된 마감이 남아 있다. Developer 구현을 시작하기 전에 다음을 모두 충족해야 한다.

1. `INTENTS.md`와 execution ledger의 blocker/next retry condition을 현재 canonical deadline `2026-09-04T06:00:00Z` 및 사용자의 명시 재개 승인과 일치시킨다.
2. 전용 `safety-map` 배포 경로와 protected runtime config가 유지되는 것을 읽기 전용으로 확인한다.
3. M4 capture의 timestamp·hash·source commit 기록 경로를 먼저 만든다.

이 세 항목 중 하나라도 누락되면 구현·배포·terminal notification을 시작하지 않고 정확한 blocker를 유지한다.

## Sources applied

- `intents/context/safety-map-experiment-02-20260904.json`
- `INTENTS.md`
- `ARTIFACT_RULES.md`
- `EXECUTION_LEARNING_CONTRACT.md`
- `reports/safety-map-experiment-02-20260904/20260903T1105Z-deadline-missed.md`
- `prompt-archive/BRAND.md`, `DESIGN.md`, `DESIGN_SYSTEM.md`
