# 질문형 정책 페이지 배포 검증

세 주소에서 실제 HTTP 200 응답과 질문형 제목, 아래 공식 출처를 확인했다.

| 운영 페이지 | 질문 | 공식 출처 |
|---|---|---|
| [아동수당](https://policy.minimalcollector.com/policies/moon.html) | 2026년과 2027년 아동수당은 몇 살까지 받을 수 있나요? | 국가법령정보센터 |
| [청년기본소득](https://policy.minimalcollector.com/policies/lee.html) | 2026년 4분기 경기도 청년기본소득은 누가 언제까지 신청할 수 있나요? | 경기도 |
| [기후동행카드](https://policy.minimalcollector.com/policies/oh.html) | 2026년 10월 이후에도 후불 기후동행카드를 쓸 수 있나요? | 서울특별시 |

[배포 실행](https://github.com/shdkej/space/actions/runs/45171570216)은 소스 cd5dcc0ee6b254ee78fe2fe4239b096884cbcbfe에 대해 성공했다. [검증 기록](https://github.com/shdkej/space/blob/cad89493ffb2c08fc36f56422e3c1508697121a2/infra-aws-static-sites/sites/policycock/qa/deployment.json)에 배포 파일 대조를 남겼다. 운영 공개와 엔진의 실제 색인 여부는 별도로 검증한다.
