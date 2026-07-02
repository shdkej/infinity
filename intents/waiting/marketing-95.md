# marketing-95 Virtue 홈 반환 상태 gating 라이브 반영 대기

- id: marketing-95
- status: waiting
- created_at: 2026-06-30T2200Z
- projects: [virtue, infinity]
- task_type: verification
- topics: [marketing, activation, deploy, return-state]
- source_note_path: /home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-29-return-state-gating-over-copy.md
- related_archive:
  - /home/ubuntu/workspace/knowledge-lab/infinity/intents/archive/marketing-92.md
- rationale: `marketing-92`는 로컬 코드 기준으로 return-state gating을 분리했지만, 2026-06-30 22:00 UTC 라이브 홈 HTML에는 여전히 retained proof(`612덕`)와 첫 방문 카피, `첫 기록이 여기에 쌓여요.` empty-state가 함께 노출된다. 현재 유용한 다음 행동은 새 카피 제안이 아니라 앱 업데이트/배포 반영을 기다린 뒤 라이브 표면만 재확인하는 것이다.
- expected_impact: 같은 상태 모순을 실패로 반복 보고하지 않고, 배포 반영 여부를 한 번의 verification gate로 관리할 수 있다.
- permission_level: Waiting
- owner_route: Infinity Waiting -> deploy/update 후 Claude Code 또는 SAM read-only 확인
- success_criteria: 라이브 홈에서 retained proof가 보이는 세션에는 first-visit hero copy와 `첫 기록이 여기에 쌓여요.` empty-state가 더 이상 함께 나타나지 않는다.
- first_verification_gate: 배포 후 `https://virtue.aws.shdkej.com`에서 recent empty-state가 returning branch(`최근 덕행을 불러오는 중이에요.`)로 바뀌었는지, 또는 최근 기록 목록이 실제로 채워졌는지 확인한다.

## Signal

- 2026-06-30 22:00 UTC 라이브 홈 HTML 관찰 결과:
  - hero score: `612덕`
  - CTA: `첫 덕 기록해보기`
  - recent empty-state: `첫 기록이 여기에 쌓여요.`
- 같은 시점 로컬 코드 `/home/ubuntu/dev/virtue-rebirth-app/apps/web/src/app/page.tsx`는 `stats.count > 0 && recent.length === 0`일 때 returning copy를 보여 주도록 이미 분기한다.
- 2026-07-02 03:37 UTC 사용자 정정으로 검증 도메인을 `https://virtue.aws.shdkej.com`로 수정했다. `https://virtue.aws` 자체는 DNS 해석되지 않으며, `virtue.aws.shdkej.com`은 HTTP 200으로 열렸다. Fresh state에서는 `612덕`과 `첫 기록이 여기에 쌓여요.`가 함께 보이고, 브라우저 localStorage에 검증용 deed 1개를 넣은 복귀 상태에서는 `나의 덕력 614덕`, `오늘 덕 쌓기`, 최근 덕행 리스트가 정상 표시됐다.

## Routing

- 현재 상태는 실패가 아니라 Waiting이다.
- 배포 또는 앱 업데이트 반영 전까지 같은 blocker를 반복하지 않는다.
- 반영 후 한 번만 라이브 검증하고, 통과 시 Archive 또는 후속 구현 검증으로 넘긴다.
