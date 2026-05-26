# marketing-21 로컬 실행 위임 프롬프트

```
Infinity Intent: marketing-21 Virtue /add 입력-결과 균형 감사표 작성
Mode: execute_local
Required workflow: Use workflow-master first. Read and follow `.agent/workflows/workflow-master.md` or `WORKFLOW-MASTER.md` when present before doing implementation work. Do not proceed as a single direct executor unless workflow-master explicitly classifies the task as trivial and records that decision.

Goal:
/add 경로의 입력-결과 균형 감사표를 virtue-rebirth-app 내부 문서로 작성하고 push한다.

Context:
- cloud 드래프트: infinity repo artifacts/marketing-21/add-flow-input-output-balance-audit.md
- source_note (참고): /home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-26-ai-onboarding-input-output.md
  (AI 온보딩 입력-결과 균형 리서치 — 드래프트 보완용)
- 대상 repo: /home/ubuntu/dev/virtue-rebirth-app
- 대상 경로: apps/web/docs/add-flow-input-output-balance-audit.md
- 선행 문서 (충돌 확인):
  - apps/web/docs/first-session-jtbd-matrix.md
  - apps/web/docs/three-screen-value-path-audit.md
  - apps/web/docs/activation-path-friction-audit.md
  - apps/web/docs/first-60-second-value-observation-script.md
  - apps/web/docs/home-screen-fae-audit.md
  - apps/web/docs/copy-spec.md (금지어 확인)

Prepared findings:
cloud 드래프트 (artifacts/marketing-21/add-flow-input-output-balance-audit.md)에 이미 포함된 내용:
1. /add 8단계 흐름 표 (A1~A7) — 이벤트·입력 부담·결과 강도·click tax
2. J1-J4 잡별 first value 분석 및 J3 저장 전 정상 종료 판정 기준표
3. 입력 부담(Input Burden) §3
4. 결과 강도(Output Strength) §4
5. Click Tax §5
6. 기존 이벤트 발화 위치 §6
7. prelaunch 해석 금지선 §7
8. 첫 10-20명 관찰 게이트 §8
9. 검증 게이트 §9

작업 지시:
1. source_note 파일을 읽고 드래프트에 보강할 인사이트 있으면 반영 (선행 문서 충돌 없는 범위)
2. 선행 5개 문서와 충돌 마커(⚠️ conflict, TODO, FIXME) 없는지 확인
3. copy-spec.md 금지어와 메타맥락 외 충돌 없는지 확인
4. apps/web/docs/add-flow-input-output-balance-audit.md 신규 생성
5. git add apps/web/docs/add-flow-input-output-balance-audit.md
6. git commit -m "docs: add /add flow input-output balance audit"
7. L2 agent-approved push 조건 확인:
   - 목표 Intent와 직결 ✓
   - fast-forward 가능 (git pull --ff-only 먼저)
   - 비용 0
   - 프로덕션 데이터·시크릿 무관
   - 코드·카피·계측 변경 0건
8. 조건 충족 시 git push origin master

Allowed: L0/L1 액션 (문서 작성, git add/commit, push)
Forbidden:
- 신규 이벤트·속성 추가 금지
- 카피 반영 금지 (내부 문서만)
- 추적/프라이버시 변경 금지
- 배포·외부 발송·비용 금지
- 코드 수정 금지

Verification:
- [ ] 문서에 input burden, output strength, click tax, deed_judged, deed_saved, J3 저장 전 정상 종료 모두 명시
- [ ] 코드/카피/계측 변경 0건
- [ ] git status clean
- [ ] HEAD == origin/master
- [ ] 선행 문서 충돌 마커 없음

Report back to:
reports/marketing-21/{timestamp}-local.html
(결론 2축 HTML 양식, ARTIFACT_RULES.md 참조)

L2 push 기록:
approval: agent-approved L2
판단 근거: 문서 1개 신규 생성, 코드/계측 변경 0, fast-forward push, 비용 0
```
