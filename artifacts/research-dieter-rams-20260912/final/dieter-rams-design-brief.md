# 디터 람스: 앱·카드·공간형 UI 적용 브리프

**결론:** 람스의 핵심은 미니멀한 외형이 아니라 목적·이해·정직성·수명에 대한 설계 책임입니다. 마스터님의 UI에는 “덜 보여주기”가 아니라 **사용자의 다음 행동에 필요한 것만, 충분히 명확하게 보여주기**로 채택해야 합니다. 신뢰도는 높음(10원칙 원문과 Rams의 1976년 연설), 다만 디지털 전환 규칙은 W3C/FTC를 근거로 한 적용 해석입니다.

## 바로 쓸 기준

### 앱
- **채택:** 첫 화면에 하나의 목적과 다음 행동을 우선순위로 둡니다.
- **보류:** 새로운 제스처·AI 기능은 기존 흐름보다 성공률 또는 시간 절감 증거가 있을 때만 넣습니다.
- **제외:** 아이콘만으로 중요한 설정·삭제·결제를 표현하는 방식, 저대비 보조 텍스트, 숨겨진 구독 해지 경로.

### 카드
- **채택:** 제목 → 한 문장 결론 → 근거/다음 행동의 고정 위계를 씁니다.
- **보류:** 장식 이미지와 모션은 핵심 정보를 가리지 않을 때만 씁니다.
- **제외:** 분위기 때문에 출처·날짜·핵심 조건을 생략하는 카드.

### 공간형 UI
- **채택:** 공간은 정보의 관계와 이동 경로를 드러낼 때만 씁니다.
- **보류:** 깊이·패럴랙스·3D는 방향 감각과 조작성을 실제로 높일 때만 씁니다.
- **제외:** 탐색·복귀·상태 확인을 어렵게 만드는 ‘전시형’ 공간.

## 출시 전 6문항

1. 사용자는 5초 안에 이 화면의 목적과 다음 행동을 말할 수 있는가?
2. 핵심 행동의 이름·결과·되돌릴 수 없음이 보이는가?
3. 레이블·오류·로딩·빈 상태·키보드/모바일 경로가 모두 있는가?
4. 일반 텍스트 대비가 최소 4.5:1인가?
5. 화면을 덜어낸 뒤에도 과업 성공률이 떨어지지 않는가?
6. 이 요소가 유행이 아니라 장기 유지보수·사용자 신뢰에 기여하는가?

## 출처와 한계

- [Vitsœ의 10가지 원칙](https://www.vitsoe.com/us/about/good-design)과 [1976년 Rams 연설](https://www.vitsoe.com/rw/voice/design-by-vitsoe)을 원문 근거로 사용했습니다.
- [Design Museum](https://designmuseum.org/designers/dieter-rams)은 독립 기관 맥락을 보강합니다.
- 디지털 UI 적용의 안전선은 [W3C labels/instructions](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html), [W3C contrast](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum), [FTC dark patterns](https://www.ftc.gov/news-events/news/press-releases/2022/09/ftc-report-shows-rise-sophisticated-dark-patterns-designed-trick-trap-consumers)입니다.
- 원칙은 제품 설계의 철학이며 접근성·사용성 테스트를 대체하지 않습니다.
