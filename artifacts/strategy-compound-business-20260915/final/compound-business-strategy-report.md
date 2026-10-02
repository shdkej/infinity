# 여행·큐레이션·AI 자산의 복리 루프: 첫 30일 판단

**결론:** 새 앱이나 수익 채널을 추가하기보다, 여행 관찰 한 건을 `scene_card`로 고정해 콘텐츠 씨앗과 선택/문제 증거로 동시에 재사용하는 루프를 먼저 검증합니다. 30일 동안 10–12장의 비공개 카드를 만들고, 재사용률·다음 선택 기여·안전 경계를 통과할 때만 다음 단계를 검토합니다.

## 왜 이 루프인가

현재 여행 프로젝트의 핵심은 장소 목록이 아니라 현장 감각·운영 실패·도시 해석을 다음 판단으로 회수하는 데 있습니다. 콘텐츠도 직접 본 장면을 채널별로 복사하는 것이 아니라, 한 문장 판단과 다음 행동으로 번역해야 합니다. scene-card는 이 두 기준을 하나의 작은 입력 단위로 연결하며, 공개 게시·판매·개인정보 수집 없이 시험할 수 있습니다.

## 후보 비교

| 후보 | 축적물 | 잠재 수익 경로(후속) | 누적 우위 | 지금의 반증 조건 | 우선 |
|---|---|---|---|---|---:|
| scene-card 의사결정 라이브러리 | 장면 → 콘텐츠 씨앗 + 선택/문제 증거 | 큐레이션 참조물·라이선스 가능성 | 한 관찰이 두 독립 산출물에 쓰임 | 카드당 유효 산출물 2개 미만 | 1 |
| 여행 마찰 코퍼스 | 독립 장면의 `problem_key` | 반복 증거 뒤의 좁은 도구 | 문제 정의가 장면과 함께 선명해짐 | 3회 독립 반복 없음 | 2 |
| REEL ROOM 제작 로그 | 편집 결정·제작시간 | 내부 dogfooding 뒤 제품화 | 매 제작이 다음 workflow를 개선 | 시간/품질 결정 변화 없음 | 3 |
| 취향 기반 동선·큐 라이브러리 | 기준 태그가 붙은 장소·선택 | 후속 큐레이션 가이드 | 다음 선택의 비교 비용 감소 | 다음 여행 선택을 못 바꿈 | 4 |
| AI 문제 언어 사전 | 장면과 연결된 문제 표현 | 조사·보조 기능 가능성 | 분류·발견 비용 감소 | 라벨이 일반적이거나 미사용 | 5 |

## 30일 private-card 실험

카드마다 `직접 본 장면`, 선택 압력, 콘텐츠 씨앗, `choice_rule` 또는 `problem_key`, 다음 선택, 민감정보 검사를 기록합니다.

- **Continue:** 10장 이상 완성, 70% 이상이 두 표면으로 분화, 2장 이상이 다음 선택을 바꿈, 안전 실패 0건.
- **Hold:** 위 조건 하나라도 미달. 카드 스키마만 수정하고 새 앱·채널·과금 실험은 열지 않습니다.
- **제품 후보 승격:** 동일 `problem_key`가 독립 장면 3회에 도달할 때만 별도 Intent 후보가 됩니다.

## 한계

이 결과는 수요·가격·구독·제휴·시장 적합을 입증하지 않습니다. 후속 수익 경로는 카드가 실제로 재사용되고 다음 결정을 바꾼 뒤에만 검토할 가설입니다.

## 근거

- `artifacts/strategy-compound-business-20260915/work/asset-and-case-evidence.md`
- `artifacts/strategy-compound-business-20260915/work/compound-loop-scorecard.md`
- `artifacts/strategy-compound-business-20260915/work/private-card-experiment.md`
- `source/openclaw-system/docs/WORLD_TRAVEL_PROJECT.md`
- `agent-wiki/content/docs/outputs/Idea/Travel.mdx`
- `agent-wiki/content/docs/outputs/Communication/Blogging.mdx`
