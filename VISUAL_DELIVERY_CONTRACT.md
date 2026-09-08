# 사용자용 비주얼 납품 계약

참조 이미지가 있는 캐러셀·카드·썸네일·사진 편집 Intent는 이 계약을 따른다. 목적은 텍스트가 읽히는 *레이아웃 샘플*을 통과시키는 것이 아니라, 사용자가 준 참조의 시각 언어를 실제 결과에 반영하는 것이다.

## 1. 두 산출물을 섞지 않는다

| 구분 | `delivery_class` | 허용 범위 | 사용자에게 납품 |
| --- | --- | --- | --- |
| 사용자용 시안 | `user_preview` | 실제 이미지 생성 또는 이미지 편집, 최종 카피 | 가능 |
| 내부 레이아웃 fixture | `internal_scaffold` | Pillow/SVG/placeholder, 검수 문구 | 불가 |

- `LAYOUT ONLY`, `PRIVATE SAMPLE`, `fixture`, `placeholder`, `검수용` 등 내부 표기는 `user_preview`의 카드 픽셀·카피·캡션에 남길 수 없다.
- 참조의 형식·구도·타이포·색·질감이 요청의 핵심이면, 단순 Pillow/SVG 합성으로 사용자용 시안을 대신하지 않는다. 실제 이미지 생성/편집 경로를 쓴다.
- 코드로 만든 최종 카드가 꼭 필요한 경우(정확한 도표, 데이터 시각화 등)는 Intent에 `code_native_final_approved: true`와 이유를 남긴다. 이 예외는 사진형 참조의 분위기 재현에는 적용하지 않는다.

## 2. 생성 전 아트디렉션

`artifacts/{intent-id}/visual-brief.json`을 먼저 만든다. `user_preview`마다 아래를 모두 기록한다. 원본 참조는 작업 후에도 확인할 수 있도록 `artifacts/{intent-id}/references/`에 읽기 전용 사본과 SHA-256을 남긴다.

```json
{
  "delivery_class": "user_preview",
  "reference_inputs": [
    {"path": "...", "role": "style_and_typography_reference"}
  ],
  "art_direction": {
    "scene": "실제 장면과 오브젝트 밀도",
    "camera": "시점·거리·프레이밍",
    "copy_hierarchy": "훅·메모·본문의 위치와 크기",
    "palette": "정확한 핵심 색과 사용 범위",
    "must_keep": ["..."],
    "must_avoid": ["..."]
  }
}
```

- 제공 참조는 텍스트 설명만으로 치환하지 않는다. 생성/편집 도구에 실제 입력으로 전달하고, 경로·역할·사용 여부를 manifest에 남긴다.
- 카피는 최종 문장으로 고정한다. 검수용 문구·임시 제목·가짜 사실을 넣지 않는다.
- 카드마다 장면·구도·오브젝트·텍스트 점유율을 적는다. 시퀀스라면 앞 카드와 달라지는 이유도 적는다.

## 3. 생성·반복

1. 참조 입력 + visual brief로 첫 렌더를 만든다.
2. 참조와 후보를 나란히 보고, 장면성·타이포 리듬·색·구도·물건 밀도를 비교한다.
3. 하나라도 핵심 요소가 빠지면 후보를 사용자용 결과로 내보내지 않고 재생성한다.
4. 최종 `render-manifest.json`에 `renderer_mode`, SHA-256이 붙은 `reference_inputs`, 실제 생성/편집 도구의 요청·응답 영수증, 최종 후보와 후보-참조 비교 이미지, `rendered_copy`, 최종 파일 SHA-256에 묶인 OCR 증거, `iteration_count`, `visual_review`, Red 보고서와 항목별 시각 검수 증거 경로를 남긴다. 이 파일들이 실제로 존재·연결되지 않으면 납품을 진행하지 않는다.

## 4. Red PASS 조건

Red는 실제 PNG/JPG를 열어 다음을 모두 판정한다.

- 참조 충실도: 참조의 시각 언어가 보이는가. 키워드만 복사한 일반 카드가 아닌가.
- 장면·구도: brief에서 약속한 시점·밀도·금지 요소가 실제로 보이는가.
- 카피·색: 훅/메모/본문 위계와 지정 색의 사용 범위가 맞는가.
- 사용자용 완결성: `LAYOUT ONLY`, `PRIVATE SAMPLE`, fixture/placeholder 등 내부 문구가 없는가.
- 카드 묶음이면 시퀀스: 프레임 간 리듬·연속성·마지막 감정 착지가 있는가.

위 항목 중 하나라도 `fail`이면 `red_status: pass`가 아니다. `scripts/validate_visual_delivery.py --manifest artifacts/{intent-id}/render-manifest.json --require-user-preview`를 통과하고, Red 보고서에 비교 근거와 재생성 횟수를 남겨야 한다. 검증기는 실제 참조/후보/비교/Red/OCR 증거 경로와 도구 요청 안의 참조 전달을 함께 확인한다.
