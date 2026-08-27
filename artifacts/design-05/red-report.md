# Red 시각 검증 — design-05

PASS. 실제 산출물은 720×1800 RGBA이며 알파 0 픽셀이 36.46%로 확인되어, 종이 가장자리·뜯긴 하단·외곽 여백이 투명하게 남아 영상 오버레이로 바로 사용할 수 있습니다.

1920×1080 합성 프리뷰에서 영수증은 좌상단에 세로로 안정적으로 배치되고, 제목·장소·연대·한국어 설명은 축소 상태에서도 판독되며 피라미드 주 피사체를 가리지 않습니다.

청록 선·잉크색, 오렌지 포인트, 아이보리 종이와 낮은 정보 밀도는 참조 Giza context-card의 팔레트·위계·grain 언어와 일치하고, 관광 포스터보다 B-roll 정보 오브젝트로 읽힙니다.

## 근거

- 소스: `artifacts/design-05/egypt-giza-field-receipt-overlay.png`
- 합성: `artifacts/design-05/egypt-giza-field-receipt-overlay-preview-1920x1080.png`
- 참조: `source/openclaw-system/reports/youtube-explainer/egypt-giza-context-card.html`
