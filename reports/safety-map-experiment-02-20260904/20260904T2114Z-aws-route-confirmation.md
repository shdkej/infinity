# T5.1 정식 AWS 경로 배포 확인

- 확인 시각: `2026-09-04T21:14:28Z`
- 대상: `https://safety-map.aws.shdkej.com/`
- 범위: 기존 Safety Map 전용 정적 배포의 읽기 전용 라이브 확인. 새 배포·Terraform apply·Travel Ops 변경은 수행하지 않았다.

## 라이브 경로

| 경로 | HTTP | Content-Type | delivery evidence |
| --- | --- | --- | --- |
| `/` | 200 | `text/html` | `server: AmazonS3`, `via: CloudFront`, `x-cache: RefreshHit from cloudfront` |
| `/app.js` | 200 | `text/javascript` | `server: AmazonS3`, `via: CloudFront`, `x-cache: Miss from cloudfront` |
| `/sources.html` | 200 | `text/html` | `server: AmazonS3`, `via: CloudFront`, `x-cache: RefreshHit from cloudfront` |

## 응답 무결성

- `/` SHA-256: `5c2bdb31aa012b1d9ee052b722c4bb745cf8d6b923b282c4e546612ab92e9435`
- `/app.js` SHA-256: `4ff1fefd42bf51de92b49ba9e1a955072665919da3f1d43f66ceb62d40ca3934`

## 경계

- 이 확인은 AWS 정적 경로가 접근 가능함을 증명한다. 실시간 안전 데이터·경로 안전성·Mapbox 토큰 값은 검증하거나 주장하지 않는다.
- T5.2의 라이브 지도 핵심 흐름 재확인과 T5.3의 terminal Slack receipt는 별도 leaf task로 남는다.
