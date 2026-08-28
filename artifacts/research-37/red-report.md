# Red 검증 — research-37

1. **PASS:** Chromium headless로 `reports/research-37/20260828T1908Z.html`을 실제 렌더했고, 15개 표 행은 RSS 원장과 같은 ID·형식·제목·게시일·공개 조회 수·링크를 정상 표시했다.
2. **PASS:** 공식 RSS 기반 15개 완전 원문 행과 ‘장소 + 직접 확인한 조건/선택’의 제한적 실험 하나가 있어 intent의 5개 이상 원문 근거 및 실행 가능 실험 조건을 충족한다.
3. **PASS:** 최신 15개 표본 한계, 장기 대표성·시청자 반응·영상 내용의 비추정, 로그인·쿠키·API key·우회·외부 발송 미사용이 보고서와 artifact에 명시돼 있다.
4. **PASS:** `Red: pending` 표기를 pass로 동기화한 뒤 intent/archive, 명시적 stage, commit/push, remote verify를 진행하는 것이 다음 액션이다.

- validator: `/root/red_research37`
- rendered_at: 2026-08-28T19:12Z
- red_status: pass
