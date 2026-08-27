# Video Overlay Object Prompt Spec — Field Receipt

## 왜 v1이 실패했나

- 너무 곧은 직사각형이라 영상 속 물건이 아니라 웹 UI 패널처럼 보였다.
- 종이의 두께, 찢김, 구김, 인쇄 번짐, 촬영 그림자가 부족했다.
- 선과 텍스트가 모두 너무 정렬되어 사람이 만든 흔적이 없었다.
- `FIELD RECEIPT`라는 개념은 좋았지만, 실제 브이로그 화면에 얹힐 소품으로는 물성이 약했다.

## 앞으로 필요한 프롬프트 블록

### 1. 객체 정체성

```text
object: a field receipt / museum field note / travel ephemera
purpose: YouTube travel vlog overlay, not a poster, not a web UI
screen role: small supporting object in the upper-left of a 16:9 video frame
```

### 2. 재질

```text
thin off-white thermal paper, sun-faded ivory tone,
slightly translucent fibers, uneven ink absorption,
fold marks running vertically, soft wrinkles, dusty surface,
rough torn top and bottom edge, small irregular side tears
```

### 3. 인쇄 방식

```text
imperfect one-color receipt printing,
slightly misregistered teal rules,
faded orange stamp ink,
small ink dropouts, low contrast aging,
not perfectly aligned, not vector-clean
```

### 4. 손으로 만든 흔적

```text
one tilted stamp in unused blank area,
one short handwritten-feeling Korean note,
not too decorative, not cute, not sticker-like,
some empty breathing room left on the paper
```

### 5. 영상 합성 조건

```text
transparent PNG with real alpha outside the object,
soft localized shadow only around paper,
no full-frame translucent rectangle,
readable when scaled to 330-430px wide in 1920x1080,
must not cover the main subject's face or the pyramid peak
```

### 6. 금지 요소

```text
no HTML card look,
no perfect rectangle,
no clean dashboard typography,
no fake transaction total,
no QR code or barcode unless the story needs it,
no glossy sticker shadow,
no tourist poster composition,
no overexplained labels
```

## 좋은 한 번짜리 생성 프롬프트

```text
Create a transparent PNG video overlay object for a YouTube travel vlog.
The object is a field receipt from Giza, Egypt: thin off-white thermal paper,
sun-faded, slightly translucent, with visible paper fibers, fold marks,
small wrinkles, dusty texture, rough torn top and bottom edges, and uneven
side tears. It should feel like travel ephemera found in a notebook, not a
web UI panel.

Layout: vertical receipt object, narrow and tall, supporting overlay for the
upper-left of a 16:9 video frame. Use imperfect receipt-style printing:
small teal location label, large serif title "FIELD RECEIPT", sparse field
rows for PLACE / AGE / TYPE, one short Korean note, and a faded orange
tilted stamp placed in empty space. Keep enough blank paper visible.

Visual behavior: ink is slightly faded and misregistered, lines are not
perfectly straight, paper has real creases and soft local shadow. Transparent
outside the object. No full-frame rectangle, no glossy card, no clean HTML
panel, no fake transaction details, no QR code. It must remain readable when
scaled to about 330-430px wide on a 1920x1080 video frame.
```

## v2 적용 기준

- 종이 외곽은 불규칙하게 찢긴 형태로 변경했다.
- 질감·주름·세로 접힘·미세한 인쇄 오차를 추가했다.
- 스탬프는 본문을 덮지 않도록 오른쪽 빈 공간에 배치했다.
- PNG 바깥쪽 알파가 남아 사각형처럼 보이는 문제를 제거했다.
- 프리뷰는 텍스트 없는 16:9 영상 프레임 위 합성 기준으로 다시 만들었다.
