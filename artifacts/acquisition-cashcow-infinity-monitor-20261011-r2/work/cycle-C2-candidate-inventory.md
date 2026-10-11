# C2 공개 후보 재순회 증거

- 확인 시각: 2026-10-11T11:31Z
- 범위: C1에서 보류된 Fello/Flippa 상세와 7개 공개 source의 page=2 또는 동일 공개 목록 URL
- 방식: 공개 HTTP GET만 수행; 로그인·판매자 연락·Notion 쓰기 없음

| source | HTTP | bytes | response SHA-256 | 판정 |
|---|---:|---:|---|---|
| Fello products page=2 | 200 | 639314 | `ece4ebc2894b590f636ca6480fd7883bd5a47f6f0f7f5cccd2401f42f8ad564b` | 기존 C1 후보 재확인, 신규 승격 0 |
| Fello 모바일 앱 상세 | 200 | 165448 | `5eac6ec2045989400330b38540a0350ffaf5e13b00e4c9edc1125d6f9b5bc961` | 가격·이전범위·운영시간 미확인, 보류 |
| Fello 퍼즐 상세 | 200 | 119903 | `7df5911fc7c1334c650622896afe0fb4151be14568f77a8d437d08516091ae87` | 가격·운영 부담 미확인, 보류 |
| Flippa search page=2 | 200 | 1422961 | `d5858e0f6e8d2722892545be48222e2851a621007e73762661d56bd0e8d24f80` | 가격 상한·독립 검증 미충족 |
| Flippa spyderads 상세 | 200 | 430785 | `2195ff72b3496dd4ee74d6c3796adc2199092a66ead4c9d44a9ea92a65a6633c` | 가격·운영 검증 미충족, 보류 |
| Sellernet page=2 | 200 | 606157 | `531db9bac0cf5f14ce626ef92d8cf21f7502cc07a38563049c77ecfe1bd3f32e` | 표시 가격 1억원, 예산 초과 |
| Listing page=2 | 200 | 130457 | `ed8934cae459a47c2efed814ab87080c1037c2922613408d214828f94244fd3c` | 가격 마스킹, 보류 |
| Quiet Light page=2 | 403 | 5431 | `d425992bb3a50423e41927fe4a5203727b6fbdf2090270bcb738794347ee34f1` | 접근 제한 |
| Acquire page=2 | 200 | 3203 | `ebb33f4a1eb2b2971c37975cb11ead69c9adbdb9c35f4de135862aa18c586151` | 동적 목록으로 상세·가격 재현 불가 |

## C2 판정

- 직접 링크·표시 가격·재무 수치·운영 부담·이전범위를 함께 확인한 신규 후보: **0건**
- 기존 16개 Notion 행과 중복되는 항목은 추가하지 않음
- 가격 상한을 환율 추정으로 판정하지 않음
