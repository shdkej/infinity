# Red 재검증 — commit 고정 근거·안전 경계

**판정: PASS** · **판정 시각:** 2026-09-12T23:53:43Z

## 검증한 사실

- 여섯 후보 모두 같은 commit에 고정된 README와 실제 `SKILL.md`의 링크·locator가 근거표에 있다.
- 라이선스는 파일 링크가 있거나, commit tree와 GitHub metadata 기준의 **명시적 부재**로 구분된다.
- 각 후보의 default branch, HEAD SHA, 관찰 시각(`2026-09-12T23:26:54Z`), GitHub REST 확인 방법이 기록됐고 표의 SHA와 동치다.

근거 상세: [candidate evidence](../github-candidate-evidence.md)의 “T1.2A 재현 레코드” 절.

## 결론의 허용 범위

- 기본 설치 추천은 **0개**다.
- Kang-chen은 저장소 라이선스, 외부 의존성, 승인된 격리 환경을 다시 확인하기 전 **hold**다.
- 설치·`sync`·실행·계정 연결·시크릿 입력은 수행하지 않았다.

이 판정은 설치 적합성이나 성능 개선을 보장하지 않는다. 부분 기능 파일럿은 승인, 격리, no-secret, egress deny-by-default 조건을 별도로 확인하기 전 실행하지 않는다.
