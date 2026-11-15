# GA4 Intent 역할 검토 통합 기록

- Intent: research-ga4-best-practices-policycock-20261115
- 검토 일시: 2026-11-15 UTC
- 작업 모드: multi_subagent_roles
- 성격: 읽기 전용 역할 검토. 계정·속성·코드·설정·고객 데이터는 접근/변경하지 않음.

## 역할별 1차 판단

### Planner — /root/planner_ga4
- 정적 랜딩에서 관측 가능한 유입·콘텐츠 탐색과 향후 서비스의 신청 준비·완료를 한 단계로 섞지 않도록 제안.
- 프로젝트 대표 지표 next_action_completed를 유지하되 실제 완료 판정 증거는 미정. 상세 보기나 외부 신청 링크 클릭은 완료가 아님.
- GA4와 PostHog 역할 구분을 유지하고, 이벤트 중복 시 의미·정의의 단일 정본이 필요.
- policy_id/source/category/action_type은 허용값·누락 규칙·민감정보 포함 가능성 미정. 자유 입력·개인 프로필은 보내지 않도록 제안.
- 관측 데이터가 없으므로 기준선·전환율은 미측정. 개발/내부 테스트 이벤트를 고객 행동에서 분리.
- 개인정보·동의는 Google 기술 제약 설명에 그치고 법률 결론은 별도 판단.

### Developer — /root/developer_ga4
- GA4와 PostHog는 모두 미연결이며, INTEGRATIONS.md 이벤트 계약은 구현 증거가 아닌 계획임.
- GA4 추천 이벤트는 자동 수집된다고 가정할 수 없으며, 실제 의미가 일치할 때만 검토. Enhanced Measurement는 URL/referrer·외부 링크 URL·검색어 등도 수집할 수 있음.
- User acquisition과 Traffic acquisition은 집계 범위가 달라 같은 지표처럼 비교 불가.
- Google Analytics의 key event와 Google Ads conversion을 분리. 외부 행동의 완료 추적이나 Ads 설정은 범위 밖.
- Realtime/DebugView는 검증 보조, 표준 보고는 24–48시간 처리 지연 가능. Data filter는 활성화 뒤 데이터가 영구 제외될 수 있음.
- PII, URL/query/search term, 자유 텍스트, UTM 유입문자열 위험과 동의/법률 미확정 상태를 명시해야 함.

### Marketer — /root/marketer_ga4
- 측정 질문을 유입원, 적격 정책 상세/저장, 재방문 후 실제 다음 행동으로 묶되 현재 모두 미측정임을 강조.
- Google 유기 검색어는 GA4 기본 획득 보고와 구분하고 Search Console 연동 데이터로 설명.
- 방문/재방문 증가를 수요·만족으로 승격하지 않음. 외부 신청 링크 클릭은 신청완료가 아님.
- 현재 초기 창업·사업자 정책탐색 범위와 생활·복지 확장 가설을 혼합하지 않음.
- 정책 주제·개인식별자·raw search를 이벤트에 덧붙이는 위험을 제시.

### Operator — /root/operator_ga4
- 현재 문서상 GA4/PostHog 미연결, 실제 이벤트·전환값 없음. 문의/마케팅 채널 원천 PC-001도 blocked.
- GA4 first user와 session acquisition 범위를 분리하고, 수집 확인은 향후 별도 승인 후 Realtime/DebugView 등으로 검증 가능.
- 개발/테스트 트래픽 식별, 이벤트 실제 완료 기준, UTM 규칙, 보존·삭제 기간은 미확정.
- 외부 신청처의 완료 상태를 확인하는 연결이 없으므로 next_action_completed는 실제 완료 증거가 있을 때만 사용.

## 교차 검토와 통합

Planner가 세 역할의 독립 결과를 검토했다. 실질 충돌은 없었다. 통합 판단:
1. GA4=획득·검색유입·재방문 맥락, PostHog=제품 행동·전환·오류라는 프로젝트 문서상 역할을 유지한다.
2. GA4의 사용자 최초 유입, 세션별 유입, Search Console의 검색 질의, 사이트 내부 검색 이벤트를 각각 다른 데이터 질문으로 표기한다.
3. 관심/상세보기/저장/외부이동은 신청완료와 분리하며, 완료 증거가 없으면 대표 지표는 미측정이다.
4. 현재 이벤트 계약·도구 분담은 예정 설계로만 다루고 실제 연결/수집 증거로 표현하지 않는다.
5. PII·raw search·문의 원문·개인 프로필의 외부 전송을 피한다. Consent Mode는 기술적 상태 전달일 뿐 법률 적합성 결론이 아니다.
6. 본 Intent에서는 분석 권한·속성·태그·이벤트·동의 설정·코드·고객 데이터·법률 판단을 하지 않는다.

## 검토 근거

- 프로젝트 문서: /home/ubuntu/workspace/projects/policycock/PROJECT.md, CHANNELS.md, TASKS.md, AGENTS.md, docs/INTEGRATIONS.md
- 공식 Google 자료: 획득 보고 범위, Search Console 통합, 추천 이벤트, Enhanced Measurement, key events, 데이터 수집 검증, 데이터 필터, PII 방지, Consent Mode
- 역할 검토 세션: planner_ga4, developer_ga4, marketer_ga4, operator_ga4
