# 모두의정책 GA4 베스트프랙티스 탐색 브리프

- 조사일: 2026-11-15 UTC
- 모드: exploratory_research
- 대상: 모두의정책 정적 랜딩 및 향후 서비스의 분석 설계 참고
- 범위: Google 공식 문서, 프로젝트 문서상 GA4/PostHog 역할, 획득·검색·재방문, 이벤트·핵심 이벤트, 데이터 품질, 개인정보·동의
- 제외: GA4/Google 계정 접근, 속성·태그·이벤트·코드 설정, 추적 활성화, 고객 데이터 수집, 광고 설정, 법률 자문

## 핵심 요약

모두의정책 프로젝트 문서는 GA4를 획득·검색·재방문 맥락, PostHog를 제품 내 행동·전환·오류에 쓰는 역할 구분을 계획하고 있습니다. 두 도구 모두 현재 미연결이며, 이벤트 계약과 대표 지표는 설계안이지 관측 증거가 아닙니다. 실제 방문·검색·전환 수치, 개인정보 처리 방식, 동의 요건은 이 조사에서 확인하지 않았습니다.

따라서 지금 할 수 있는 일은 측정 질문과 해석 경계를 정리하는 것까지입니다. 특히 정적 랜딩에서 외부 신청처로 이동한 클릭을 실제 신청 완료로 간주하지 말고, GA4의 사용자 최초 획득·세션별 유입·Search Console 검색어·사이트 내부 검색을 서로 다른 측정 범주로 구분해야 합니다. Google의 안내는 설정·정책을 설명하지만, 국내 법률 적합성 판단을 대신하지 않습니다.

## 1. 현재 프로젝트 맥락

PROJECT.md는 모두의정책을 정책을 찾고 변화·근거를 확인해 행동으로 연결하는 서비스로 설명합니다. 현재 운영 초기 범위는 창업·사업자 지원정책 탐색, 신청 준비, 후속 행동입니다. 정적 랜딩과 향후 앱의 측정 질문은 같지 않을 수 있습니다.

docs/INTEGRATIONS.md에는 다음 계획이 적혀 있습니다.

- GA4: 유입·검색·재방문
- PostHog: 제품 행동·전환·오류
- R2: 파일 저장 성공률·용량·오류
- 예정 이벤트: policy_viewed, policy_saved, next_action_started, next_action_completed, inquiry_submitted
- 대표 지표: 유효한 next_action_completed

같은 문서는 GA4/PostHog가 연결되지 않았고 실제 수집 이벤트나 고객 전환 수치가 없다고 기록합니다. CHANNELS.md의 고객 문의 채널과 전용 마케팅 지표 원천도 미확정이며, TASKS.md의 PC-001은 blocked입니다. 이 연구는 이를 바꾸거나 해결하지 않습니다.

## 2. 측정 질문을 도구별로 나누기

| 질문 | 프로젝트 문서상 담당 후보 | 읽는 법과 경계 |
|---|---|---|
| 어떤 경로로 첫 방문자가 왔나? | GA4 | User acquisition은 사용자 최초 획득 기준, Traffic acquisition은 세션별 유입 기준입니다. 이름이 비슷한 source/medium 값도 집계 범위가 다르므로 같은 축의 수치처럼 직접 비교하지 않습니다. [Google: acquisition 보고서 범위](https://support.google.com/analytics/answer/14731736?hl=en) |
| Google 검색에서 어떤 검색어/페이지가 노출·클릭됐나? | Search Console 데이터와 GA4 연계(계획 후보) | 검색 질의 보고서는 Search Console 속성과 GA4 웹 스트림을 연결해야 합니다. 데이터는 수집 후 GA4 보고에 최대 48시간 걸릴 수 있고 최대 16개월 범위입니다. 연동 여부·권한은 확인하지 않았습니다. [Google: Search Console 연동](https://support.google.com/analytics/answer/10737381?hl=en) |
| 방문자가 사이트 내부에서 무엇을 검색했나? | 사이트 검색 이벤트(향후 제품 기능이 있을 때) | Enhanced Measurement의 view_search_results는 URL의 q/s/search/query/keyword 같은 query parameter를 기준으로 작동하고 search_term을 기록할 수 있습니다. 현재 내부 검색 기능과 URL 구조는 이번 조사에서 확인하지 않았습니다. 원문 검색어는 개인 상황이나 민감한 관심을 드러낼 수 있으므로 raw term 수집은 별도 검토가 필요합니다. [Google: Enhanced Measurement](https://support.google.com/analytics/answer/9216061?hl=en) |
| 어떤 정책 상세·저장·준비 행동을 했나? | PostHog(프로젝트 계획) | policy_viewed/policy_saved/next_action_started는 제품 행동을 진단할 후보입니다. 현재 이벤트 정의·허용 속성·도구 연동은 확인되지 않았으며, 이벤트 계약은 구현으로 간주하지 않습니다. |
| 신청이나 준비를 실제로 완료했나? | PostHog 우선, 필요 시 후속 데이터 설계 | next_action_completed는 프로젝트 대표 지표지만 외부 포털의 실제 접수 상태를 확인하는 연동·증거는 확인되지 않았습니다. 외부 신청 링크 클릭은 이동/시작 신호일 뿐 완료가 아닙니다. 현재 완료 수치는 미측정입니다. |
| 사용자가 다시 돌아와 다음 행동을 했나? | GA4 재방문 맥락 + PostHog 행동 | 재방문 사용자·세션은 관심/행동의 맥락이지 가치나 만족 자체가 아닙니다. 어떤 정보 확인 후 어떤 다음 행동이 발생했는지 연결되는 경우에만 가치 신호로 해석합니다. |

이 구분은 프로젝트 고유 역할을 설명한 것입니다. GA4가 반드시 해당 역할에 최선이라는 기술 선택이나 연결 승인을 의미하지 않습니다.

## 3. 이벤트와 전환 용어

Google은 이벤트를 자동 수집, Enhanced Measurement, 추천 이벤트, 사용자 정의 이벤트로 구분합니다. 추천 이벤트는 필요한 맥락이 있어 자동으로 전송되지 않으며, 의미와 권장 매개변수가 실제 행동과 일치할 때 사용하는 방식입니다. 예를 들어 실제 사이트 내 검색이 있으면 search, 사용자가 계정을 만들면 sign_up, 문의 양식을 제출하면 generate_lead가 의미상 후보가 될 수 있지만, 현재 기능에 존재하거나 수집된다고 가정하면 안 됩니다. [Google: 추천 이벤트](https://support.google.com/analytics/answer/9267735?hl=en)

프로젝트 고유 행동인 policy_saved나 next_action_started/completed는 이벤트 정의가 별도로 필요한 후보입니다. Google Analytics에서 중요한 비즈니스 이벤트는 key event로 표시할 수 있습니다. key event로 표시한 시점부터 보고에 반영되며 과거 이벤트를 소급해서 바꾸지 않습니다. Google Ads 캠페인 최적화 등에 쓰는 Ads conversion과 Analytics key event는 동일한 설정 개념으로 섞지 않습니다. 이번 Intent에서는 어느 이벤트도 생성·표시하지 않습니다. [Google: key event](https://support.google.com/analytics/answer/13128484?hl=en)

완료 판정은 분석 도구보다 먼저 정의되어야 합니다. 정책 상세 보기, 저장, 외부 신청 링크 클릭, 신청서 제출은 서로 다른 단계입니다. 확인 가능한 실제 완료 증거가 없는 동안 next_action_completed는 측정값이 아니라 미확정 목표로 남깁니다.

## 4. 데이터 품질과 보고 한계

- **이벤트 확인:** Google은 Realtime과 DebugView를 수집 확인·개발 검증에 안내합니다. Realtime은 최근 30분, DebugView는 debug mode가 켜진 기기의 이벤트를 확인합니다. 이는 향후 승인된 측정 설정을 검증할 방법이며, 현재 데이터 수집 증거가 아닙니다.
- **보고 지연:** 많은 표준 보고서와 탐색은 처리에 24–48시간이 걸릴 수 있습니다. Search Console 연계 보고도 수집 이후 48시간 지연될 수 있으므로, 초기 실시간 숫자를 최종 성과로 단정하지 않습니다. [Google: 수집 확인](https://support.google.com/analytics/answer/9333790?hl=en)
- **테스트/내부 트래픽:** 향후 측정이 승인되면 고객 트래픽과 개발·테스트 트래픽을 구별할 기준이 필요합니다. GA4 데이터 필터는 생성 이후 들어오는 데이터에만 적용되고, 활성 제외 필터의 영향은 영구적이며 과거 기록을 바꾸지 않습니다. 따라서 이번 탐색에서 필터나 설정을 적용하지 않습니다. [Google: Data filters](https://support.google.com/analytics/answer/13296761?hl=en-GS)
- **측정 정의:** 이벤트 이름·트리거·중복 억제·허용 속성·실패 기준을 하나의 정본으로 유지해야 합니다. 동일 행동을 GA4와 PostHog 양쪽에 둘 경우 목적과 판독 기준을 분리해야 수치 불일치를 오류로 오해하지 않습니다.
- **아직 없는 기준선:** 유입, 검색, 재방문, 이벤트 수, 전환율, 수익, 유지율은 모두 미측정입니다. 이 보고서에는 값이나 목표 실적을 만들어 넣지 않았습니다.

## 5. 개인정보와 동의

Google은 개인 식별정보(PII)를 Google Analytics로 보내지 말 것을 요구하고, URL 경로·query parameter·페이지 제목, 사용자가 입력한 검색어와 폼 값 등을 주요 누출 경로로 안내합니다. 이름·이메일·전화번호 외에 캠페인 파라미터나 사용자 검색어도 검토 대상입니다. [Google: PII 방지 가이드](https://support.google.com/analytics/answer/6366371?hl=en-SD), [Google: 데이터 보호](https://support.google.com/analytics/answer/6004245?hl=en)

정책 서비스는 검색·저장한 주제가 사용자의 사업·가족·재정·건강·지역 상황을 드러낼 수 있습니다. 이는 프로젝트 맥락에서의 위험 추론이지 확인된 수집 사실이나 법률 분류가 아닙니다. 향후 설계 때는 다음을 확인할 수 있습니다.

- 문의 원문·개인 프로필·자유 검색어·연락처를 이벤트 매개변수로 보내지 않기
- policy_id, category, source, action_type처럼 계획된 속성은 허용 목록과 공개/민감도 판단을 먼저 문서화하기
- save_reason 등 자유입력일 수 있는 값의 정의 확인; 허용되지 않으면 수집하지 않기
- URL, 제목, UTM, 외부 링크에 개인정보나 사용자가 입력한 문자열이 들어가지 않는지 점검하기
- 실제 데이터 보존·삭제 기간과 접근 소유자는 설정을 확인하기 전까지 미정으로 두기

Google Consent Mode는 웹사이트의 기존 동의 메커니즘에서 선택 상태를 Google 태그로 전달하는 기술입니다. 기본 모드는 사용자의 선택 전 태그를 차단하고, 고급 모드는 거부 상태에서도 cookieless ping을 보낼 수 있는 등 동작이 다릅니다. 이 기능은 동의 배너/기반을 대신하지 않으며 한국 법률 준수 여부를 결정해주지 않습니다. 실제 동의 방식·고지 문구·보존 정책의 법적 적정성은 본 Intent 범위 밖이며 미확정으로 둡니다. [Google: Consent Mode](https://support.google.com/analytics/answer/14009635?hl=en)

## 6. 현재 미확정 사항

다음은 이번 조사에서 확인하지 않았고 설정·추정하지 않았습니다.

1. GA4 계정·속성·웹 스트림의 존재 여부, 소유자·접근 권한·Measurement ID
2. Google Search Console 소유권 및 GA4와의 연계 상태
3. 정적 랜딩/향후 서비스에서 실제 제공되는 검색·문의·신청 흐름과 각 이벤트의 완료 조건
4. PostHog 프로젝트/키/연결 상태와 역할별 이벤트 정본
5. URL·검색어·사용자 입력·정책 메타데이터의 민감도 및 허용 속성
6. 개발·내부 트래픽 식별 기준, UTM 규칙, 데이터 보존/삭제 설정
7. 동의 요구와 고지 내용의 법적 판단, 향후 담당자·운영 주기

## 열어 본 Google 공식 자료

모두 Google Analytics Help / Google for Developers 문서이며 2026-11-15 UTC에 열어 확인했습니다.

- [User acquisition와 Traffic acquisition의 범위 차이](https://support.google.com/analytics/answer/14731736?hl=en)
- [Search Console을 Google Analytics에 연결](https://support.google.com/analytics/answer/10737381?hl=en)
- [Enhanced Measurement 이벤트와 수집 매개변수](https://support.google.com/analytics/answer/9216061?hl=en)
- [GA4 추천 이벤트](https://support.google.com/analytics/answer/9267735?hl=en)
- [GA4에서 key event 표시](https://support.google.com/analytics/answer/13128484?hl=en)
- [수집 확인: Realtime와 DebugView](https://support.google.com/analytics/answer/9333790?hl=en)
- [GA4 데이터 필터와 영구 제외 영향](https://support.google.com/analytics/answer/13296761?hl=en-GS)
- [PII 전송 방지 모범 사례](https://support.google.com/analytics/answer/6366371?hl=en-SD)
- [Analytics 데이터 보호와 사용자 선택](https://support.google.com/analytics/answer/6004245?hl=en)
- [Consent Mode 설정 안내](https://support.google.com/analytics/answer/14009635?hl=en)

## 내부 문서 근거

- 프로젝트 등록: /home/ubuntu/workspace/projects/PROJECTS.md
- 목적·현재 제품 범위·대표 지표: /home/ubuntu/workspace/projects/policycock/PROJECT.md
- 접점/미확정 지표 원천: /home/ubuntu/workspace/projects/policycock/CHANNELS.md
- PC-001 상태와 기존 시장/검증: /home/ubuntu/workspace/projects/policycock/TASKS.md
- 프로젝트 승인 경계: /home/ubuntu/workspace/projects/policycock/AGENTS.md
- 현재 GA4/PostHog 역할 및 이벤트의 설계 상태: /home/ubuntu/workspace/projects/policycock/docs/INTEGRATIONS.md
- Context Pack 및 검색 결과: /home/ubuntu/workspace/infinity/intents/context/research-ga4-best-practices-policycock-20261115.json
- 선택된 Agent Wiki: Note_Management, Data, Blogging, Integration/Marketing (context pack locator 참조)
- 운영 로그에서 확인한 범위: /home/ubuntu/workspace/knowledge-lab/logs/agent-wiki-query.md#L112-L122

## 한계와 다음 열린 질문

이번 작업은 공식 자료와 프로젝트 문서의 정합성을 조사한 보고서입니다. 계정·속성·랜딩 소스·실제 이벤트·동의 동작·고객 데이터는 확인하지 않았으므로 현재 추적 상태, 분석 성과, 개인정보 법적 적합성을 판단하지 않습니다.

후속 측정 설계가 승인될 경우 먼저 답해야 할 질문은 세 가지입니다. (1) 정적 랜딩에서 의사결정에 필요한 가장 작은 획득 질문은 무엇인가, (2) next_action_completed는 어떤 관찰 가능한 증거가 있을 때만 완료로 셀 것인가, (3) 정책 주제·검색어·저장 정보에서 어떤 속성을 수집하지 않을 것인가. 이 질문에 대한 결정 전에는 설정·계측 작업이 이 보고서의 결론으로부터 자동 승인된 것으로 해석되지 않습니다.
