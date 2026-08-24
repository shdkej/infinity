# research-32 Planner PRD — Starter Story 사례 깊은 복원

## 1. 목표

지정 영상 [The First App I Ever Built Makes $25K/Month](https://youtu.be/Q4k8JNYKJT0)의 사례를 Kyan/ToneAdapt의 문제 인식 → 검증 → V1 제작 → 최초 공개 → 초기 유입 → 반복 개선 → 최근 상태 순으로 복원한다. 각 사실은 원문 URL·게시일/시점·짧은 인용·근거 강도(A 원자료, B 공식 2차 원문, C 보조자료, D 추정 금지)로 표시한다.

## 2. 수집 계약

| 소스 | 수집 항목 | 판정 |
|---|---|---|
| YouTube 지정 URL | 제목, 디스크립션, 챕터, 영상 본문/자막 | 영상 페이지는 확인. yt-dlp는 봇 로그인 차단. Starter Story 공식 페이지가 동일 transcript를 노출하므로 본문은 교차확인하되, 직접 영상 재생/파일 확보는 blocker로 기록 |
| Starter Story 공식 원문 | 게시일, 디스크립션, 챕터, transcript, 숫자·인용 | 확보. 2026-06-14 게시, 15:05 길이/챕터, transcript |
| Kyan X | 최초 공개일, 게시물·조회/반응·콘텐츠 포맷 타임라인 | 프로필 HTML 접근 시 0 lines. 원문 게시물은 확인 불가. 추정 금지, SNS 원자료 blocker |
| ToneAdapt 공식 웹 | 현재 제품 설명·기능·사회적 증거·앱 상태 | 확보. 현재 페이지에는 150,000+ guitarists, 4.9 rating, iOS, 기능 설명이 있으나 시점/누적 정의는 별도 확인 불가 |
| 보조 검색 결과 | Podscan 등 transcript/수치 교차검증 | 보조 근거로만 사용. 공식 원문과 충돌 시 공식 우선 |

## 3. 산출물

1. `artifacts/research-32/starter-story-toneadapt-deep-reconstruction.md`: 근거표, 단계별 타임라인, 실패/불확실성, AI 분석.
2. `artifacts/research-32/collection-analysis-contract.md`: 재사용 가능한 수집/분석 스킬과 결과 페이지 업로드 데이터 계약.
3. `reports/research-32/20260824T-research.md`: 역할별 실행·검증·상태 보고.

## 4. 범위와 완료 기준

- 영상 요약, 디스크립션, 챕터, transcript를 확보하고 원문 링크를 남긴다.
- 문제 인식부터 최근까지 최소 4개 핵심 단계(문제/제작/공개·유입/반복·현재)를 1차 원문으로 재현한다.
- SNS 원문이 막히면 확보 가능한 사실만 쓰고 `Waiting` blocker와 재개 조건을 명시한다.
- 매출·사용자·구독자 숫자는 영상에서 주장된 관측값으로 표기하며 지속적 MRR/순이익으로 과대해석하지 않는다.
- 공개 게시, 로그인/자격증명, 유료 API, 외부 발송, 페이지 실제 업로드는 실행하지 않는다. 결과 페이지는 요구사항·계약만 만든다.

## 5. 분석 질문

- 개인 사용 문제와 시장 검증은 어떤 순서로 이어졌나?
- 웹 V1 일주일, AI 코딩, 구독 가격과 어떤 분배 루프가 결합했나?
- 첫 바이럴 이후 무엇을 반복/확대했나?
- 5개월/25K 주장은 어떤 기간·채널·정의의 숫자인가?
- 확인되지 않은 SNS 날짜·반응·실패는 무엇이며, 그것을 모르는 것이 결론을 어떻게 제한하나?

## 6. 역할 인계

- Developer: 공식 페이지 transcript/디스크립션과 공식 웹을 구조화하고 출처·시점 필드를 보존한다.
- Marketer: 사례의 첫인상(“작은 문제 + 빠른 공개 + 얼굴을 건 분배”)과 재사용 가능한 콘텐츠 벤치마크를 분리한다.
- Operator: 접근 실패(YouTube bot, X empty HTML), 재현성, remote upload 승인 경계를 기록한다.
- Red: 요청 일치성, 추정 유입 여부, 숫자 정의, blocker와 페이지 계약의 완결성을 검사한다.

## 7. 최종 상태 정책

영상 원본 파일과 X 게시물 원문을 직접 확인할 수 없으므로 완전 복원은 `Waiting/부분 완료`다. Starter Story 공식 transcript와 공식 웹 근거로 준비 가능한 분석은 닫고, 재개 조건은 YouTube 자막/영상 파일 또는 Kyan의 X 게시물 export/URL 제공이다.
