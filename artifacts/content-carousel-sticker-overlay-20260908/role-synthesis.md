# 역할 수렴 — 손글씨 훅·형광 메모형 캐러셀 1장

## Planner

- 정확히 한 장의 1080×1350 비공개 시안만 만들고, 제공 이미지 두 장은 스타일 참조로만 쓴다.
- 형광 연두는 훅과 단일 사각 메모의 제한적 예외이며, 둥근 테이블·새 여행 사실·공개 유도는 금지한다.

## Developer

- 기존 SVG 외부 참조 실패 이력을 피하기 위해 Pillow 직접 합성과 해시 manifest를 선택했다.
- 산출물은 단일 RGB PNG, 25% preview, 결정적 renderer·validator로 제한했다.

## Marketer

- 첫 시선은 훅, 둘째는 메모, 마지막은 기록 사진이 되도록 위계를 고정했다.
- 문구는 `LAYOUT ONLY · PRIVATE SAMPLE`과 시각 검수 설명으로 한정해 개인 경험·성과 주장을 만들지 않았다.

## Operator

- `origin/main`의 clean detached worktree에서만 생성·검증했다.
- 공개 게시·업로드·계정 변경은 전부 false이며, 원본 제공 경로는 style reference로만 manifest에 보존했다.

## 수렴 결정

실사진 기록 배경은 기존 로컬 source asset을 private layout fixture로만 사용했습니다. 제공된 두 이미지는 큰 검은 외곽선 라임 훅·검정 라벨+라임 메모의 **스타일 원칙**만 제공하며, 최종 파일에 복제·삽입하지 않았습니다.
