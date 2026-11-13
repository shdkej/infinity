# 에이전트 간 작업 인계

다른 에이전트에게 실제 작업을 요청할 때는 Infinity의 기존 Intent를 재사용하거나, 독립된 결과가 필요한 후속 Intent를 연결합니다. 보조 inbox나 메모만 남겨 실행 요청이 접수됐다고 보지 않습니다.

## 책임과 경로

`source agent → Infinity Inbox → 지니 실행·검증 → 결과와 source Intent 연결`

상태 원장은 `INTENTS.yaml`입니다. 지니가 실행 결과를 통합하고, 고객·시장·브랜드 방향은 CMO, 접수·목표 충돌·승인 경계는 SAM이 맡습니다. 역할과 임시 세션 계약은 [OpenClaw 공통 계약](../knowledge-lab/source/openclaw-system/docs/OPENCLAW_COMMON.md#2-역할과-4층-구조)과 [지니 workflow](../../.openclaw/workspace-genie/GENIE_WORKFLOW.md)를 따릅니다.

- 먼저 Backlog·Inbox·Active·Waiting·Archive에서 중복을 확인합니다. 같은 결과를 여러 역할별 Intent로 복제하지 않습니다.
- 실제 실행 target은 `genie`입니다. 과거 `target_agent: marketer` 같은 역할 이름은 필요한 경우 `delegated_role`로 보존합니다.
- 임시 역할 세션은 같은 Intent 안에서 기록합니다. 별도 후속 결과가 필요한 협업 요청만 독립 Intent로 둡니다.
- SAM 내부 inbox 파일은 검토·상태 전달용 보조 입력이며 실행 원장을 대신하지 않습니다.

## 인계 필드

[접수 계약](heartbeat.md#2-inbox를-실행-가능한-요청으로-만든다)에 더해 협업 요청에는 아래를 남깁니다.

| 필드 | 내용 |
| --- | --- |
| `source_agent`, `source_intent`, `target_agent` | 요청자·원 작업·실행자 |
| `request_type`, `question`, `context` | 요청 종류·해결할 질문·관련 맥락 |
| `evidence`, `desired_output`, `output_contract` | 직접 근거·받을 결과·검증 기준 |
| `approval_boundary`, `user_visible` | 허용 범위·사용자 전달 필요 여부 |

일상적인 내부 협업은 `user_visible: false`로 둡니다. source Intent의 backlink는 결과를 찾는 연결이며 실행 트리거가 아닙니다. 개인정보·비공개 대화 원문은 필요한 범위만 전달합니다.

## 결과 회수

지니는 요청·근거·소유 문서를 읽고 승인 범위 안에서 실행합니다. [산출물 규칙](ARTIFACT_RULES.md)에 따라 결과·검증·필요한 Red를 확인하고 [종료 절차](heartbeat.md#6-결과와-archive를-함께-닫는다)를 마칩니다. source Intent의 다음 결정이 달라지면 결과 링크·남은 가정·차단·다음 행동을 갱신합니다. 공개 발송은 별도 승인 범위를 따릅니다.
