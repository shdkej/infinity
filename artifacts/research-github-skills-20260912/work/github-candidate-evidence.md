# GitHub 공개 리서치 스킬 — 직접 열람 근거표

**조사 질문:** 현재 `deep-research`(질문 구체화·출처 가중·불일치 해소·한계 보고)와 `agent-reach`(웹/GitHub 탐색) 위에, 반복 리서치 품질을 검증 가능하게 보완할 공개 스킬이 있는가?

**판정 기준:** 각 후보에서 README, 실제 `SKILL.md`, 저장소 라이선스·최근 HEAD를 직접 열었다. 설치·스크립트 실행·계정 연결은 하지 않았다. `keep`은 기존 기능과 다른 검증 가능한 능력, 명확한 라이선스, 안전한 의존성 표면을 모두 요구한다. 하나라도 없으면 `hold` 또는 `reject`다.

| 후보 | 직접 연 commit (UTC) | 실제 파일 | 라이선스 표면 | 기존 기능과의 비교 | 판정 |
|---|---|---|---|---|---|
| [PracticalSwan/agent-skills](https://github.com/PracticalSwan/agent-skills) | `4c6cabc` (2026-09-12) | [`research/SKILL.md`](https://github.com/PracticalSwan/agent-skills/blob/4c6cabc08893e64993f888fd652efcef006409a6/research/SKILL.md) | repo `LICENSE.txt`: MIT; skill도 MIT 표기 | 1차 출처·단일 근거 문서·fallback은 이미 `deep-research`와 중복. background agent 지시는 현재 Infinity role/trace 계약과 충돌 가능 | **reject — 중복** |
| [pbi-agent/skills](https://github.com/pbi-agent/skills) | `3f38f81` (2026-05-19) | [`skills/research-lab/SKILL.md`](https://github.com/pbi-agent/skills/blob/3f38f81e4b16f5de1612ab18e9d78d76f826986c/skills/research-lab/SKILL.md) | GitHub repo metadata에 LICENSE 없음 | phase/state/decision 산출물은 Infinity task-plan·trace·HTML report와 중복, 별도 `research/<slug>` 상태 원장 요구 | **reject — 라이선스 부재·상태 계약 충돌** |
| [drader/researcher_agent](https://github.com/drader/researcher_agent) | `d9937f6` (2026-05-23) | [`skills/research/SKILL.md`](https://github.com/drader/researcher_agent/blob/d9937f6e5f223efca7ac239d464bf4d455a415c1/skills/research/SKILL.md) | README/`LICENSE`는 CC BY-NC 4.0 | 문헌 검색·검증·주석서지 7 모드가 넓지만, 사용자에게 실질 판단을 유보해 autonomous dispatcher와 맞지 않음 | **reject — 비상업 라이선스·운영 모델 불일치** |
| [CODE-SAURABH/OpenSkills](https://github.com/CODE-SAURABH/OpenSkills) | `71d3c6d` (2026-07-26) | [`research-agent/SKILL.md`](https://github.com/CODE-SAURABH/OpenSkills/blob/71d3c6d75f504b3693a93e3dada42207b1a6d221/research-agent/SKILL.md) | repo MIT | 시작 구분자가 YAML `---`가 아니라 `/---`; 범용 primary-source/cross-reference 흐름도 `deep-research`와 중복 | **reject — 형식 불확실·중복** |
| [Kang-chen/Agent-skills](https://github.com/Kang-chen/Agent-skills) | `45c9293` (2026-08-17) | [`literature-review/SKILL.md`](https://github.com/Kang-chen/Agent-skills/blob/45c9293ecc1b4f8bd262c83bfecdfa962a50a908/literature-review/SKILL.md), [`research/searching-literature/SKILL.md`](https://github.com/Kang-chen/Agent-skills/blob/45c9293ecc1b4f8bd262c83bfecdfa962a50a908/research/searching-literature/SKILL.md), [`research/traversing-citations/SKILL.md`](https://github.com/Kang-chen/Agent-skills/blob/45c9293ecc1b4f8bd262c83bfecdfa962a50a908/research/traversing-citations/SKILL.md) | skill frontmatter에는 MIT지만 repo LICENSE는 GitHub metadata상 없음 | 다중 학술 DB·DOI 중복 제거·screening rubric·citation traversal은 문헌 체계적 검토에 한해 비중복. 하지만 필수 AI 도식 생성·`Read Write Edit Bash`·여러 보조 스킬/외부 API를 전제 | **hold — 좁은 문헌 파일럿 후보** |
| [krzysztofdudek/ResearcherSkill](https://github.com/krzysztofdudek/ResearcherSkill) | `87acc90` (2026-09-12) | [`skills/researcher/SKILL.md`](https://github.com/krzysztofdudek/ResearcherSkill/blob/87acc9097dd111fc8647e02326266e884aaa0979/skills/researcher/SKILL.md) | repo MIT | 반복 실험·branch·`.lab/` 운영은 공개정보 리서치보다 코드 최적화 실험용이며, 무기한 iteration·repo write를 요구 | **reject — 작업 범위·운영 비용 불일치** |

## 직접 관찰한 근거와 한계

1. **PracticalSwan**은 “고신뢰 1차 출처”와 검증 프로토콜을 명시하지만, 현재 `deep-research`도 직접 열람·출처 등급·한계 보고를 이미 강제한다. 보완 능력이 확인되지 않아 설치 이유가 없다.
2. **pbi-agent**는 단계·상태·decision 산출물을 요구한다. 그 체계 자체는 재현 가능하지만, Infinity는 이미 plan/trace/Red/HTML report 계약을 갖고 있어 두 상태 머신을 병렬 도입하면 충돌한다.
3. **drader**는 공개된 문헌 작업에는 유용할 수 있으나, README가 CC BY-NC 4.0을 명시하고 SKILL은 인간의 실질 판단을 필수로 둔다. 이번 autonomous research dispatcher에는 맞지 않는다.
4. **OpenSkills**는 연구 원칙이 유사하나, 해당 파일의 frontmatter 형식이 Agent Skills 명세의 YAML 구분과 다르다. `SKILL.md` 존재만으로 호환을 주장할 수 없다.
5. **Kang-chen**은 문헌검토의 DOI 중복 제거·screening·citation graph 기능을 문서상 제시한다. 다만 현재 공개 repo의 최상위 라이선스가 확인되지 않고, 필수 도식 생성과 다수 외부 도구 의존을 같이 요구한다. 따라서 일반 리서치에 도입하지 않으며, 별도 승인 후 no-secret·network deny-by-default 격리 환경에서 **학술 문헌 1건**을 대상으로 부분 기능만 검증할 때만 재검토한다.
6. **ResearcherSkill**은 MIT이고 최근 갱신됐으나, `.lab/`·브랜치·자율 실험을 중심으로 한다. 현재 요청의 공개 자료 조사와는 목적이 다르다.

## 현재 기능 유지 결정

- **retain:** `deep-research` + `agent-reach` + Infinity의 plan/trace/Red/HTML report.
- **conditional pilot:** Kang-chen의 문헌 검색·screening·citation traversal 중 필요한 부분만, 라이선스와 실제 의존성·egress를 재확인한 별도 승인 후 격리 검증.
- **do not install:** 나머지 5개. 이번 조사에서 어떤 후보도 설치·동기화·실행하지 않았다.

## 역할 검토 수렴

- **Planner:** 일반 research skill 기본 설치는 0개가 적절하며, Kang-chen만 문헌검토 한정 조건부 후보.
- **Developer:** README·실제 `SKILL.md`·LICENSE·실행 표면을 같은 commit에 고정해야 하며, 미확인 네트워크·키·frontmatter는 hold/reject.
- **Marketer:** “빠른 결론”보다 “신뢰/보류 이유를 남기는 도구”를 기준으로 삼고 도구 나열을 피한다.
- **Operator:** 설치 전에는 commit 고정, 정적 스크립트/Actions 검토, egress 기본 차단, 라이선스·의존성·롤백 절차를 모두 요구한다.

## 무엇이 결론을 바꾸는가

Kang-chen 저장소의 repo-level 라이선스와 사용하려는 특정 하위 스킬의 스크립트·외부 호출·데이터 전송 경로가 명확히 확인되고, 격리된 no-secret 시험에서 Infinity의 근거 추적을 실제로 개선한다면 그 **부분 기능**만 조건부 채택으로 바뀔 수 있다. 현재 기록만으로는 설치 권고를 정당화하지 못한다.
