# [research-13] 콘텐츠 제작 최소 설정 체크리스트

- id: research-13
- status: archived
- completed_at: 2026-06-15T23:47Z
- projects: [infinity, research-bank, personal-ops]
- task_type: research
- topics: [content, workflow]
- result_summary: 콘텐츠 제작 전 최소 설정을 `target_reader`, `reader_state`, `reader_problem`, `content_goal`, `core_message`, `angle`, `tone_voice`, `format_channel` 8개 필수값과 evidence/CTA/boundary/success 보조값으로 정리했다.
- artifacts:
  - path: artifacts/research-13/content-minimum-settings-checklist.md
    role: research
    note: 콘텐츠 초안 생성 직전 필요한 최소 브리프 필드, YAML 스키마, 기본값, 검수 질문, 출처 메모
- reports:
  - path: reports/research-13/2026-06-15T2347Z-local.html
    role: final
    note: 조사형 결론 2축 HTML report
- commits:
  - repo: infinity
    sha: (이 커밋)
    note: research-13 산출물·원장·보고서·INTENTS 정리
- urls: []
- next_actions:
  - 콘텐츠 생성 Intent를 만들 때 이 artifact의 `content_brief` 스키마를 기본 입력값으로 사용한다.
  - 실제 Threads/블로그/유튜브별 generator를 만들 때는 `format_channel.structure`만 채널별 preset으로 분리한다.

## 성공 기준 충족

- [x] 타겟 독자, 독자 상태, 문제, 목적, 핵심 메시지, 관점, 톤/보이스, 형식/채널을 최소 필수 설정으로 정리.
- [x] 근거, 다음 행동, 금지선, 성공 신호는 거의 필수 보조값으로 분리해 입력 부담을 낮춤.
- [x] Infinity에서 바로 재사용 가능한 YAML schema와 한 줄 브리프 템플릿 작성.
- [x] Content Marketing Institute, HubSpot, Mailchimp, NN/g 자료를 참고해 source memo 작성.
- [x] 산출물 `artifacts/research-13/content-minimum-settings-checklist.md`
- [x] HTML report `reports/research-13/2026-06-15T2347Z-local.html` + report gate 통과 대상.

## 경계 준수

- 공개 발송·콘텐츠 게시·브랜드명/카피 확정·외부 계정 액션 0.
- 코드·배포·비용·시크릿·권한 변경 0.
- 기존 dirty 파일 `EVALUATION_NOTES.md`는 staging 제외.
