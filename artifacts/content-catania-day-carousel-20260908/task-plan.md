# 카타니아 하루의 비용·휴식 기준 6장 캐러셀 — 실행 타임라인

`마감: 없음` · `실행: 1회차` · `태스크: 4개 중 0개 완료 · 4개 미완료`

```text
◐ T1  실제 기록 기반 비공개 캐러셀 렌더                                 진행
│  ◐ T1.1  원본 사진·사실 경계·카드 시퀀스 고정                           진행 · 예상/최대 20/30분 · 의존 없음
│           증거: `artifacts/content-catania-day-carousel-20260908/fact-and-asset-audit.md`
│           시작/완료/실제: 2026-09-08T22:14:28Z / missing / missing
│  ○ T1.2  6장 4:5 private render 생성                                   대기 · 예상/최대 30/30분 · 의존 T1.1
│           증거: `artifacts/content-catania-day-carousel-20260908/card-01.png` … `card-06.png`
│           시작/완료/실제: missing / missing / missing
│  ○ T1.3  Red 실제 렌더·사실성 검증                                    대기 · 예상/최대 20/30분 · 의존 T1.2
│           증거: `artifacts/content-catania-day-carousel-20260908/red-report.md` · Red PASS/FAIL
│           시작/완료/실제: missing / missing / missing
│  ○ T1.4  HTML report·원격 검증·Archive 준비                           대기 · 예상/최대 20/30분 · 의존 T1.3
│           증거: `reports/content-catania-day-carousel-20260908/{timestamp}.html`
│           시작/완료/실제: missing / missing / missing
│
└─ — 보호 경계
      제공 사진만 카드별 시각 입력으로 사용한다. 실제 기록 밖 가격·상호·타인 감정·장소 평가는 만들지 않는다. 공개 게시·업로드·외부 발송은 하지 않는다.
```

**지금 다음 행동:** `T1.1 원본 사진·사실 경계·카드 시퀀스 고정`
