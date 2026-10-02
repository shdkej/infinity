# T1.1 시작 조건 감사

## 확인한 공개 자료

- 저장소: `https://github.com/Kang-chen/Agent-skills`
- 대상 파일: `research-lookup/SKILL.md`
- README는 167개 skill의 통합 저장소라고 설명하고 clone·sync 절차를 안내한다.
- 대상 SKILL frontmatter는 `allowed-tools: Read Write Edit Bash`를 선언한다.
- 본문은 OpenRouter를 통한 Perplexity Sonar Pro/Reasoning Pro 호출과 학술 검색을 설명한다.
- 직접 `LICENSE` 페이지 확인은 오류로 실패했고, 저장소 루트의 재사용 라이선스를 확정하지 못했다.

## 판정

T1.1은 완료했지만 T1.2를 시작할 수 없다. repo/subfile 라이선스, 실제 의존성, 외부 egress·데이터 전송 경로가 모두 확정되지 않았고, 이는 승인 후에도 파일럿 시작 전 필수 조건이다. 따라서 clone/install/sync/script 실행 없이 파일럿을 Waiting으로 전환한다.
