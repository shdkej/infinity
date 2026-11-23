# 모두의정책 전용 Meta 픽셀 설치

- id: modu-policy-meta-pixel-20261123
- status: archived
- completed_at: 2026-11-23T13:33:29+00:00
- task_type: implementation
- report: reports/modu-policy-meta-pixel-20261123/20261123T133329Z.html
- red_report: artifacts/modu-policy-meta-pixel-20261123/work/review.md

모두의정책 전용 Meta 픽셀을 설치했습니다. 운영 홈페이지에서 광고 동의 전에는 Meta 요청이 없었고, 동의 후 PageView 1건에 HTTP 200 응답을 받았습니다.

모의 신청 서버와 Meta 수신 경로를 사용한 브라우저 테스트에서 신규 신청 성공만 Lead 1회를 보냈습니다. 중복·실패·재시도·다른 탭의 동의 철회·추적 방지 조건도 확인했습니다.

11월 23일 확인 시점에 Meta 이벤트 관리자의 오늘 보기에는 수신한 활동이 없었습니다. 실제 고객의 Lead 수신, 관리자 이벤트 집계와 광고 귀속은 미확인입니다.

[배포 검증](https://github.com/shdkej/space/blob/81bc0725d696238ad03b055f5d77bd3a59486a76/infra-aws-static-sites/sites/policycock/qa/deployment.json)
