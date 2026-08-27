# design-05 — 이집트 여행 브이로그용 세로 영수증 B-roll 오버레이

- id: design-05
- status: archived
- completed_at: 2026-08-27T00:15Z
- projects: [knowledge-lab, infinity]
- task_type: design
- topics: [content, marketing]
- result_summary: Giza Context Card의 색·위계를 잇는 720×1800 투명 PNG 영수증 오버레이와 1920×1080 합성 프리뷰를 제작했고 Red 시각 검증을 통과했다.
- artifacts:
  - path: artifacts/design-05/egypt-giza-field-receipt-overlay.png
    role: design
    note: 영상 좌상단용 RGBA 세로 영수증 오버레이
  - path: artifacts/design-05/egypt-giza-field-receipt-overlay-preview-1920x1080.png
    role: verification
    note: 1920×1080 합성 가독성 프리뷰
  - path: artifacts/design-05/red-report.md
    role: verification
    note: Red 시각 검증 PASS
- reports:
  - path: reports/design-05/20260827T0015Z.html
    role: final
- red_status: pass
- red_report: artifacts/design-05/red-report.md
- role_sessions: planner=/root/planner_egypt_receipt; developer=/root/developer_egypt_receipt; marketer=/root/marketer_egypt_receipt; operator=/root/operator_egypt_receipt; red=/root/red_egypt_receipt
- knowledge_status: used
- knowledge_decision: retain-as-operating-principle
- knowledge_targets: agent-wiki README; DESIGN_SYSTEM.md; TASTE.md; BRAND.md; source/openclaw-system/reports/youtube-explainer/egypt-giza-context-card.html
- knowledge_reflection: 여행 B-roll 정보물은 장식된 기념품보다 장소·연대·한 문장만 남긴 낮은 정보 밀도의 ContextObject가 영상 위에서 더 읽힌다.
- knowledge_commit: no-promotion-needed
- next_actions:
  - Remotion 또는 편집 타임라인에서 좌상단 x=80,y=76,w=330 내외로 배치한다.

## 2026-08-27 V2 Revision

- trigger: 사용자가 v1이 너무 HTML틱해서 YouTube 영상용 디자인 객체로 쓰기 어렵다고 피드백.
- diagnosis: v1은 반투명 직사각형, 정렬된 선·텍스트, 깨끗한 패널감이 강해서 영상 안의 물건보다 UI 캡처처럼 보였다.
- decision: 영수증을 정보 패널이 아니라 `현장 메모지 / 여행 소품 / field ephemera`로 재정의.
- changes:
  - 찢긴 상하단과 불규칙한 좌우 가장자리 추가.
  - 종이 섬유, 세로 접힘, 구김, 미세한 프린트 번짐 추가.
  - 스탬프는 본문을 덮지 않도록 오른쪽 빈 공간으로 이동.
  - 투명 PNG 바깥쪽에 남던 사각형 질감/알파 번짐 제거.
  - 텍스트 없는 16:9 영상 프레임 프리뷰 추가.
- artifacts:
  - path: artifacts/design-05/egypt-giza-field-receipt-overlay-v2.png
    role: design
    note: 영상용 투명 PNG 오버레이 v2
    url: https://img.shdkej.com/derived/2026/08/27/bd741a89-d38b-4f21-8b6f-d3ef9e50a51f.webp
  - path: artifacts/design-05/egypt-giza-field-receipt-overlay-v2-preview-1920x1080.png
    role: verification
    note: 텍스트 없는 16:9 영상 프레임 합성 프리뷰
    url: https://img.shdkej.com/derived/2026/08/27/d52b3585-b5f0-42ed-8a0c-decfa824cb92.webp
  - path: artifacts/design-05/video-overlay-object-prompt-spec.md
    role: reusable_prompt_spec
    note: 영상 오브젝트를 일관되게 만들기 위한 프롬프트 구성요소
  - path: artifacts/design-05/red-report-v2.md
    role: verification
    note: v2 실제 렌더 검증 PASS

## Archive Card

[프로젝트]
이집트 여행 브이로그 B-roll

[상태]
제작·시각 검증 완료

[결과 기준]
720×1800 투명 PNG, 영상 좌상단 합성 가독성, Red PASS

[다음 행동]
편집 타임라인에 오버레이 삽입
