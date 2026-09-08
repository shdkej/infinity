# 손글씨 훅·형광 메모형 캐러셀 1장 시안

- 납품물: `card-01.png` 한 장(1080×1350 RGB)과 25% 검수용 `preview-25pct.png`
- 배경: 로컬 기존 기록 사진을 비공개 레이아웃 fixture로만 사용했습니다. 제공된 두 이미지는 스타일 참조일 뿐 최종 이미지에 복제·삽입하지 않았습니다.
- 예외: 형광 연두는 Intent가 명시한 단일 훅·단일 메모 블록에만 사용했습니다. 나머지는 어두운 저채도 기록 톤입니다.
- 공개 경계: `public_posted=false`, `external_uploaded=false`, `profile_changed=false`. 공개 가능성·저작권·원 장면의 사실성은 판정하지 않았습니다.

재현/검증:

```bash
python3 generate_assets.py
python3 validate_assets.py
```
