# research-35 한국 사업자 앱·웹 디지털 결제수단 조사

## Dispatcher 결과

상태: archived / red_status: pass. 사용자 확정 조건(디지털 콘텐츠·기능, 앱+웹, 한국 사업자, 구독+1회 구매, 한국 고객)을 반영했다. 공개 발송·계정 생성·계약·결제는 하지 않았다.

## Planner

PRD는 [artifacts/research-35/planner-prd.md](../../artifacts/research-35/planner-prd.md)에 기록했다. 결정 단위는 앱 결제 레일, 웹 결제 provider/MoR, paywall 통합층, 사업자 국가·SIM 조건으로 분리했다.

## Developer — 공식 문서 수집 및 비교

비교 결과와 1차 자료 링크는 [artifacts/research-35/payment-comparison.md](../../artifacts/research-35/payment-comparison.md)에 기록했다. 핵심 근거는 Apple App Review Guidelines 3.1.1/3.1.3, StoreKit IAP, 한국 StoreKit External Purchase Entitlement, Stripe global availability와 타국 계정 요건, Paddle 지원 국가·한국 결제수단·MoR 세금 문서, Superwall web checkout/revenue tracking 문서다.

## Marketer — 사용자·가격 경험

한국 고객 중심이면 iOS에서 Apple 결제 시 익숙한 복원·구독관리·신뢰 경험을 얻고, 웹에서는 한국 카드와 원화/환불 안내를 전면에 두는 것이 전환에 유리하다. 한국 전용 외부 PSP entitlement는 앱을 한국 storefront로 제한하고 별도 결제 고지 모달을 노출하므로 글로벌 확장과 가격 체계를 복잡하게 만든다. Paddle은 한국 로컬 카드 지원을 문서화하지만, MoR의 장점이 한국 사업자의 회계·고객지원 책임을 모두 없애는 것은 아니므로 카피에서 “세금 완전 해결”처럼 과장하면 안 된다. Superwall은 결제수단 이름으로 노출하지 말고 “구독 화면/실험/접근권한 관리”로 설명한다.

## Operator — 심사·계정·운영 리스크

Stripe는 한국 사업자의 해외 SIM 우회 대상이 아니다. 한국 전용 Apple 외부결제는 entitlement 신청, PSP 승인/검토, 한국 전용 binary와 storefront 확인, native modal, 월별 Apple 거래 보고 및 26% 청구가 운영 정지점이다. 모든 provider는 환불·차지백·webhook 재처리·정산 통화·개인정보 국외 이전·세무 문서를 계약 전에 확인한다. 이번 실행에서는 어느 계정도 만들거나 심사·계약·결제를 시작하지 않았다.

## Genie synthesis

metric_question에 대한 답은 “예, 조건부로 하나를 선택할 수 있음”이다. 기본 조합은 `iOS Apple IAP + 웹 한국 PG 또는 온보딩 승인된 Paddle MoR + 서버 entitlement 통합 + Superwall은 선택적 paywall/분석 계층`이다. Stripe는 한국 사업자 기본 웹 provider로 확정하지 않는다. 한국 전용 외부결제 entitlement는 Apple 26%와 별도 binary·심사 부담으로 2차 검토다. 해외 SIM은 사업자 자격·계정 국가·세금번호·은행계좌를 바꾸지 않으므로 해결책이 아니다.

## Red

독립 검증 기록은 [artifacts/research-35/red-report.md](../../artifacts/research-35/red-report.md)이며 pass다. 앱/웹 분리, 공식 링크, Superwall 역할, SIM의 비영향, 승인 경계를 확인했다.

## Knowledge 판정

* knowledge_status: used
* knowledge_decision: no-promotion-needed
* knowledge_targets: agent-wiki README; Integration/Business 관련 원칙(공식 근거·현재 조건·운영 경계 우선)
* knowledge_reflection: 결제 선택은 인기 도구가 아니라 사업자 국가·스토어 storefront·상품 성격·정산/세무 책임의 인터페이스를 먼저 고정해야 한다. 외부 SIM처럼 표면 위치를 바꾸는 신호와 법적/금융 자격을 분리하는 판단을 재사용 원칙으로 남긴다.
* knowledge_commit: no-promotion-needed

## 산출물 및 다음 액션

원격 반영과 확인을 완료했다(`origin/main=2a0c9f1`). 이후 공급자 계정 생성이 아니라, 사용자가 별도 승인한 뒤 한국 PG 1곳과 Paddle의 실제 온보딩·요율·세무·개인정보 계약 문서를 비교한다.
