# marketing-77 구현 패킷

Infinity Heartbeat Cloud Prepare — 2026-06-22T1230Z
승인 출처: user "마케팅 작업 승인" 2026-06-22T11:25Z

## 승인 범위

**승인됨:**
- Virtue 앱 내 product UI/copy 변경 (최소 범위)
- 로컬 build/test 검증
- 브랜치 생성 및 커밋

**승인되지 않음:**
- 외부 발표, 유료 행위
- tracking/privacy/analytics 신규 계측
- credential/permission 변경
- 되돌릴 수 없는 프로덕션 배포 (배포는 별도 L2 승인 필요)
- force push

## 로컬 실행 정보

- 앱 경로: `/home/ubuntu/dev/virtue-rebirth-app`
- 배포: kubernetes `deployment/virtue-rebirth`
- URL: `https://virtue.oracle.shdkej.com`

---

## P1: /add 첫 표면 기대 브리지 (최우선)

**근거:** marketing-74 Option B 승인, marketing-76 Gate Yes

**변경 내용:**
`/add` 페이지의 입력 폼 위(또는 아래)에 sample 결과 1줄 표시.

**추천 카피:**
```
예: AI가 오늘의 덕행을 정리했어요: 인내 × 3
```

대안:
```
"꾸준히 참았어요" → AI가 이렇게 읽어요: 인내 × 3, 자기조절 × 1
```

**구현 방향:**
- 입력 폼 위 또는 placeholder 근처 보조 텍스트 1줄
- 스타일: muted, 작은 폰트 (입력 UI 방해 금지)
- 조건: 항상 표시 (사용자 상태 분기 불필요)

**카피 원칙:**
- 관점 프레임: "AI가 본 오늘", "AI가 읽어요" 등
- 판결 동사 금지: "AI 채점", "AI가 판단", "AI가 평가" 사용 불가
- 1줄 이내

**되돌림:** 해당 텍스트 1줄 제거

---

## P2: 결과 카드 맥락형 안내 (두 번째)

**근거:** marketing-76 Gate Yes, marketing-74 J4 배치 권고

**변경 내용:**
AI 결과 카드 하단 footer에 관점/경계 안내 문구 1줄 추가.

**추천 카피:**
```
AI의 관점이에요 — 결정은 당신이 해요
```

대안:
```
이건 AI가 본 당신의 하루예요
```

**구현 방향:**
- 결과 카드 컴포넌트의 footer 영역 (카드 본문 아래)
- 스타일: muted/secondary, 작은 폰트
- 새 버튼, CTA, 링크 추가 금지

**카피 원칙:**
- 관점 제안형: AI가 옳다고 주장하지 않음
- J4 경계 자연스럽게 내재 (별도 경고 박스 아님)
- 1-2줄 이내

**되돌림:** footer 텍스트 제거

---

## P3: 홈 empty state ghost 카드 (선택, 낮은 우선순위)

**근거:** marketing-73 Option C, marketing-71 stacked card, marketing-70 gap 분석

**변경 내용:**
홈 `최근 덕행` 섹션이 비어 있을 때, ghost/sample AI 결과 카드 1개 조건부 표시.

**주의:**
- marketing-76 Gate: 홈 empty state 안내 문구는 No → ghost 카드 자체는 별개 (proof preview)
- ghost/sample 라벨 "샘플" 또는 "예시" **반드시** 표시

**추천 ghost 카드 내용:**
```
[샘플]
2024년 6월 21일
• 인내 × 3  |  자기조절 × 1
AI의 관점: "오늘 힘든 순간들을 조용히 넘겼어요"
```

**구현 방향:**
- 홈 컴포넌트에서 덕행 목록이 빈 경우 조건 분기
- ghost 카드: opacity 낮춤 + "샘플" 뱃지
- 실제 데이터가 있으면 숨김 (빈 상태일 때만 표시)
- marketing-71 stacked 카드 스타일 참고

**되돌림:** 조건 분기 제거 또는 빈 상태 컴포넌트 원복

---

## 구현 검증 게이트

모든 항목 통과 후 커밋:

- [ ] diff가 P1/P2/P3 표면으로만 제한됨
- [ ] 새로운 tracking/analytics/PostHog 이벤트 없음
- [ ] privacy/credential/permission 변경 없음
- [ ] ghost/sample 요소에 "샘플" / "예시" 라벨 표시 확인
- [ ] 카피에 판결 동사 없음 ("AI 채점", "AI 판단" 등)
- [ ] local build 통과
- [ ] local test 통과 (있으면)
- [ ] 390px viewport 스크롤 이슈 없음

---

## 완료 후 처리

1. 커밋 & 브랜치 생성 (예: `marketing-77-ui-copy`)
2. 배포는 별도 L2 승인 후 진행
3. 완료 리포트: `reports/marketing-77/{timestamp}.html`
4. INTENTS.md marketing-77 → archived 처리

---

## 참고 아카이브

| ID | 관련 내용 |
|----|-----------|
| marketing-74 | /add 입력 전 기대 형성 3안 — Option B 추천 |
| marketing-76 | 핵심 화면 안내 감사표 — /add Yes, 결과 카드 Yes, 홈 No |
| marketing-73 | J3 AI 브리지 3안 — Option C (ghost 카드) 추천 |
| marketing-71 | seeded proof 비교 — stacked card 구조 |
| marketing-70 | empty state gap 분석 — CTA보다 proof preview 부족 |
| marketing-75 | 변경 Tier 분류 — /add Tier 3, 결과 카드 Tier 3, 홈 Tier 2 |
