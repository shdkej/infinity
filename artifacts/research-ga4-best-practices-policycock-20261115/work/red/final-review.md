# Red 독립 검토 — GA4 exploratory research

- 검토 일시: 2026-11-15 UTC
- 대상 보고서: `/home/ubuntu/workspace/infinity/artifacts/research-ga4-best-practices-policycock-20261115/work/candidate/ga4-best-practices-report.md`
- 대상 HTML: `/home/ubuntu/workspace/infinity/reports/research-ga4-best-practices-policycock-20261115/20261115T0401Z-final.html`
- 교차 검토 참고: `/home/ubuntu/workspace/infinity/artifacts/research-ga4-best-practices-policycock-20261115/work/roles/role-review.md`
- 원 요청: 기존 Active exploratory research Intent 보고서와 HTML을 읽기 전용으로 사실·근거·불확실성, 과장·누락, 인용 URL, out-of-scope, 이벤트·개인정보 해석 및 390px 렌더로 독립 검토한다.
- 제약: Google 설정·고객데이터·법률 자문·외부 메시지 금지. 지정 Red 리뷰 외 파일 수정 및 git 쓰기/commit/push 금지.
- 체크아웃: `/home/ubuntu/workspace/infinity`, `main...origin/main`. 기존 `M data/dispatcher-terminal-notifications.json`은 그대로 보존. 최종 상태 확인 때 `M data/traces/research-ga4-best-practices-policycock-20261115.json`도 추가로 관찰했으며, 발생 주체를 판별하지 못해 건드리지 않음. Intent/report 디렉터리들은 untracked 상태였으며 지정된 Red 리뷰 외에는 건드리지 않음.

## 최종 판정: UNCERTAIN (보류)

보고서 내용·범위·공식 링크 점검에서는 중대한 사실 오류를 찾지 못했고 validator도 통과했습니다. 다만 요청된 HTML의 390px 실제 렌더에서 핵심 정보의 가시성과 수평 overflow를 직접 판독하는 데 실패했습니다. 따라서 전체 PASS는 부여하지 않습니다.

## 요구사항별 검증

- 요구사항: 보고서가 프로젝트 사실과 예정 이벤트를 실제 운영·실측 증거와 구분한다.
  - 판정: PASS
  - 직접 증거: 후보 보고서 §1–6은 GA4/PostHog 미연결, 이벤트 정의는 계획, 수치는 미측정으로 명시. `/home/ubuntu/workspace/projects/policycock/docs/INTEGRATIONS.md`에는 도구 역할·이벤트 목록이 계획으로, 56행에는 아직 연결하지 않았다고 기록. `PROJECT.md` 22–25행은 대표 지표와 현재 수집값 부재를 명시.
  - 반례 확인: 보고서의 `next_action_completed`가 완료 실측처럼 기술되는지, 역할 보고가 해당 주장을 과장하는지 대조함. 역할 리뷰도 완료 증거·수치 미정으로 구분하며 충돌 없음.
  - 다음 조치: 없음.

- 요구사항: GA4 획득 범주, 검색 범주, 이벤트·전환 해석이 출처 및 사용 맥락과 맞는다.
  - 판정: PASS
  - 직접 증거: `https://support.google.com/analytics/answer/14731736?hl=en` 등 인용된 Google Help URL 10개를 확인. 모두 HTTP 200으로 응답했고 공식 문서 제목이 보고서의 주제와 일치. 확인 가능한 발췌에서 User acquisition 대 Traffic acquisition 차이, Search Console 연계, Enhanced Measurement, 추천 이벤트 자동 전송 아님, key event 설정, 24–48시간 처리, 데이터 필터의 생성 이후 적용, PII 금지, Consent Mode에 기존 동의 메커니즘 필요를 확인.
  - 반례 확인: Search Console 검색 질의와 내부 검색, 최초 사용자 유입과 세션 유입을 한 지표로 합치지 않았고, Ads conversion과 Analytics key event를 구분함. 외부 신청 클릭을 완료로 세지 않는다고 반복 명시.
  - 다음 조치: 없음.

- 요구사항: 개인정보·동의 설명이 위험을 드러내되 법률 결론을 만들지 않는다.
  - 판정: PASS
  - 직접 증거: 후보 보고서 §5–6은 검색어·URL·정책 주제 위험을 프로젝트 맥락상의 위험 추론으로 한정하고, 동의 요건·법적 적정성을 미확정/out-of-scope로 명시. Google PII 공식 가이드 `https://support.google.com/analytics/answer/6366371?hl=en-SD`에서 PII 전송 금지 정책을 확인.
  - 반례 확인: 분석 이벤트 예시(policy_id/category 등)를 허용된 실수집 데이터라고 단정하는지 점검. allowlist·민감도 판단 전 미확정으로 남김. Google Consent Mode를 법적 동의/배너 대체물로 오해하지 않도록 명시.
  - 다음 조치: 없음.

- 요구사항: 보고서와 산출물 범위가 exploratory research 및 명시된 금지 조건을 지킨다.
  - 판정: PASS
  - 직접 증거: 보고서 범위 머리말 및 결론은 계정·속성·태그·코드·고객데이터·법률 판단을 제외한다고 명시. 지정 validator 실행 결과: `PASS research report quality: reports/research-ga4-best-practices-policycock-20261115/20261115T0401Z-final.html`.
  - 반례 확인: 역할 리뷰는 계획 중 하나를 설정 승인으로 승격하지 않았고, 계정/태그/고객데이터 접근이나 외부 메시지 수행 기록을 포함하지 않음. 이번 검토에서 git 쓰기·commit/push하지 않았으며 기존 unrelated 수정 파일을 보존.
  - 다음 조치: 없음.

- 요구사항: 390px 화면에서 제목, 두 핵심 축, 핵심 발견 진입점이 보이고 수평 overflow가 없는지 확인한다.
  - 판정: UNCERTAIN
  - 직접 증거: HTML 소스에서 `<meta name="viewport">`, 반응형 제목, 두 `.axis`, 첫 번째 열린 `<details>`, `.find` 핵심 발견 목록을 확인. CSS는 `table`을 640px 이하에서 block 변환하고 URL/본문 wrap 규칙을 둠. Chromium headless로 390×844 스크린샷 `/tmp/ga4-report-390.png`을 생성해 390×844 PNG 생성은 확인했으나, 이미지 판독/렌더 페이지의 `scrollWidth` 대조는 완료하지 못함. Browser 도구는 `file:` 미지원, localhost 페이지 탐색은 정책 차단으로 실패.
  - 반례 확인: `overflow-x:hidden`은 화면 밖 내용을 잘라 숨길 수 있어 그것만으로 overflow 부재 증거가 되지 않음. 소스 구조상 긴 URL·테이블이 줄바꿈/모바일 블록화되도록 되어 있으나, 실제 렌더를 직접 관찰하지 못했으므로 가시성·잘림을 PASS할 수 없음.
  - 다음 조치: HTML을 브라우저에서 390 CSS px로 열어 제목·축 01/02·‘핵심 발견’ 목록이 처음 화면 흐름에서 읽히는지와 `document.documentElement.scrollWidth <= document.documentElement.clientWidth`를 한 번 직접 확인.

## 핵심 반박

- 중요한 내용 누락·과장 또는 이벤트/개인정보 해석에서 수정이 필요한 finding은 확인하지 못했습니다.
- 유일한 미해결은 시각 QA 증거입니다. validator PASS는 구조 검사 증거이지 요청된 390px 실제 가시성/overflow 검증의 대체물이 아닙니다.

## 실행 범위 기록

읽기만 수행하고 지정된 `final-review.md`만 작성 대상으로 삼았습니다. 체크아웃 상태의 기존 `data/dispatcher-terminal-notifications.json`, 최종 확인 때 보인 `data/traces/research-ga4-best-practices-policycock-20261115.json` 수정 및 다른 untracked 산출물은 변경하지 않았습니다. trace 수정의 출처는 확인하지 않았습니다. Git 쓰기·commit·push는 수행하지 않았습니다.


## 최종 보완 검토 — 390px 실제 렌더

- 보완 시각: 2026-11-15 04:16 UTC
- 보완 대상: 위 대상 HTML의 실제 390 CSS px 렌더
- Red 보완 판정: **PASS**
- Red가 직접 확인한 PNG: `artifacts/research-ga4-best-practices-policycock-20261115/work/red/ga4-report-390x844.png` (390×844)
- Red 확인: 제목과 두 핵심 축이 보이며, ‘핵심 발견’ 제목과 첫 목록 항목이 화면 하단에서 잘리지 않음.
- 독립 측정 보강: Chromium DevTools의 390×844 CSS viewport에서 `innerWidth=390`, `documentElement.clientWidth=390`, `documentElement.scrollWidth=390`, `body.scrollWidth=390`. 제목 y=132–203, 축 01 y=355–498, 축 02 y=524–667, ‘핵심 발견’ y=746–764, 첫 항목 시작 y=780. 모든 요소의 가로 경계가 viewport 안에 있음.
- 이전 UNCERTAIN은 이미지 전달 capability 문제로 생겼으며, PNG를 `image()`의 base64 data URI로 전달한 뒤 Red가 직접 판독하여 해소함.
- 최종 전체 판정: **PASS** (내용·공식 출처·범위·validator 및 390px 실제 렌더 통과).
- 원격 반영, Intent/trace/dispatcher 갱신, Git 쓰기·commit/push는 하지 않음.

### 최종 HTML 메타 갱신 후 재렌더 확인

- 확인 시각: 2026-11-15 04:18 UTC
- Red PASS 상태를 HTML에 표시하고 난 뒤 최종 파일을 다시 390×844로 렌더함.
- 최종 스크린샷: `artifacts/research-ga4-best-practices-policycock-20261115/work/red/ga4-report-390x844.png`
- Chromium 재측정 결과는 동일: viewport/client/scroll/body 너비 모두 390px. 제목·두 축·핵심 발견 제목·첫 목록 항목의 좌표와 가로 경계도 동일하며 화면 잘림·수평 overflow 없음.
- 최종 스크린샷은 제품실 PO가 직접 재확인함. 수정은 상태 표시/메타 문구와 canonical Markdown 경로이며 조사 내용은 바꾸지 않음.
