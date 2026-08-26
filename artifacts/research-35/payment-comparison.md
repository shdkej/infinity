# research-35 앱·웹 결제 비교

조사 기준일: 2026-08-26. 공식 원문만 사용했으며, 사업자 심사 결과·계약 조건·세무 해석은 추정하지 않는다.

## 결론

가장 보수적인 기본 아키텍처는 `iOS/iPadOS 디지털 구매 = Apple In-App Purchase(StoreKit)`, `웹 디지털 구매 = 한국 사업자가 계약 가능한 국내 PG(예: KCP·이니시스·NICE 등) 또는 Paddle의 사업자 온보딩 승인 후 Merchant of Record`다. Superwall은 페이월·실험· entitlement/구매상태 통합 도구이지 PSP가 아니다. Stripe는 2026-08-26 공식 지원 국가 목록에 한국이 없고, 한국 사업자에게 해외 유심만으로 Stripe 계정을 만들 권한을 주지 않는다.

## 앱 결제

Apple [App Review Guidelines 3.1.1](https://developer.apple.com/app-store/review/guidelines/)은 앱 안에서 기능·디지털 콘텐츠를 잠금 해제하는 구독, 프리미엄 콘텐츠, 기능 등에 IAP를 요구한다. [StoreKit IAP 문서](https://developer.apple.com/documentation/storekit/in-app-purchase)는 consumable, non-consumable(1회 구매), auto-renewable subscription을 지원하고 Apple이 결제 처리·거래 검증 경로를 제공한다고 설명한다. 따라서 일반 글로벌 앱은 상품을 App Store Connect에 만들고 StoreKit으로 구매·복원·서버 검증을 구현하는 것이 기준선이다.

한국에서만 배포하는 iOS/iPadOS 앱은 [StoreKit External Purchase Entitlement](https://developer.apple.com/support/storekit-external-entitlement-kr/)로 제3자 PSP를 사용할 수 있다. 현재 사전 승인 PSP는 KCP, Inicis, Toss, NICE이며, 다른 PSP는 Apple의 별도 검토 대상이다. 계정 소유자의 entitlement 신청, 미게시 bundle ID, 한국 전용 별도 바이너리, 한국 storefront 한정, StoreKit API와 외부결제 모달, native flow, 고객지원 URL이 필요하다. Apple IAP와 같은 앱에서 함께 쓸 수 없고, 기존 IAP 앱의 한국 스토어 버전은 삭제 후 승인 조건이 적용될 수 있다. Apple commission은 사용자 결제액(부가세 총액 기준)의 26%이고 월별 거래 보고와 세금 징수·납부 책임이 개발자에게 있다. 즉 “토스 외 외국 PSP를 앱에 붙인다”는 선택은 단순 SDK 교체가 아니라 한국 전용 배포·PSP 심사·Apple 정산 의무가 붙은 별도 트랙이다.

## 웹 결제

웹은 App Store IAP가 아니라 웹 checkout/PG 계약과 사업자·세무·환불 운영이 핵심이다.

* Stripe: [Global availability](https://stripe.com/global) 공식 목록에 한국이 없으므로 한국 법인/사업자 주소만으로 Stripe Payments 계정을 개통할 수 있다고 결론 내릴 수 없다. [다른 국가 계정 요건](https://support.stripe.com/questions/requirements-to-open-a-stripe-account-in-another-country)은 해당 국가의 법인(또는 사업자), tax ID, 물리적 주소, 전화번호, 신분증, 웹사이트, 물리적 은행계좌를 요구한다. 해외 유심은 이 요건을 대체하지 않는다.
* Paddle: [지원 국가](https://www.paddle.com/help/legal/sanctions/which-countries-are-supported-by-paddle)는 금지국 외 소프트웨어 사업자 지원을 명시하며 한국을 금지 목록에 넣지 않는다. [결제수단 문서](https://www.paddle.com/help/start/intro-to-paddle/which-payment-methods-do-you-support)는 한국 로컬 카드 22종 이상을 명시한다. [MoR·세금 문서](https://www.paddle.com/help/sell/tax/how-paddle-handles-vat-on-your-behalf)는 Paddle이 Merchant of Record로 판매·세금 계산·징수·송장 발행을 맡는다고 설명한다. 다만 이는 사업자 온보딩·리스크 심사·지급 가능성을 보장하는 표현이 아니므로 계정 개설 전 확인이 필요하다. 한국 고객의 결제수단/원화 표시·환불·한국 부가세 처리와 한국 사업자 매출 회계 처리를 계약 전에 확인한다.
* 한국 PG: Apple의 한국 외부결제 entitlement 사전 승인 목록(KCP, Inicis, Toss, NICE)은 앱 트랙의 PSP 목록이다. 웹에서는 각 사업자의 일반 온라인 결제·정기결제 계약 가능 여부와 디지털 상품 정책을 별도로 확인해야 한다. Apple 목록에 있다는 사실만으로 웹 계약·조건이 확정되는 것은 아니다.

## Superwall의 역할

[Superwall Web-Only Checkout](https://superwall.com/docs/web-checkout/web-checkout-web-only)은 웹 checkout 설정에서 Stripe를 결제 provider로 구성하고, 구매 뒤 redirect·상품 접근 부여를 개발자가 처리하도록 설명한다. [FAQ](https://superwall.com/docs/web-checkout/web-checkout-faq)는 Stripe one-time price로 lifetime/consumable을 팔 수 있다고 명시한다. [Revenue Tracking](https://superwall.com/docs/dashboard/dashboard-settings/overview-settings-revenue-tracking)은 iOS App Store Connect, Android Google Play, 또는 RevenueCat 이벤트를 연결한다. 따라서 Superwall은 PSP/MoR가 아니며, Stripe 계정이 필요한 web checkout의 대체 자격을 제공하지 않는다. 앱에서는 Apple/Google 구매 레일을, 웹에서는 연결한 provider를 사용하고, Superwall은 paywall·A/B 테스트·구매상태/entitlement·웹훅을 통합하는 층으로 이해해야 한다.

## 해외 유심의 실제 영향

Apple [App Store availability](https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/manage-availability-for-your-app-on-the-app-store)는 고객의 Apple Account 국가/지역이 storefront를 결정한다고 한다. [Storefront](https://developer.apple.com/documentation/storekit/storefront)는 구매 storefront와 통화를 노출하며 값은 바뀔 수 있다고 경고한다. Apple 계정 국가 변경은 [결제수단·청구 주소](https://support.apple.com/en-asia/118283), 잔액 소진·구독 취소 등의 조건이 필요하다. 그러므로 해외 SIM/로밍은 통신망·전화번호 인증 또는 현재 네트워크 위치에 영향을 줄 수 있지만, 한국 사업자의 법적 소재지·세금번호·은행계좌·PSP 계약 자격이나 Apple 계정 storefront를 자동으로 바꾸지 않는다. Stripe도 국가별 법인·물리적 주소·은행계좌를 요구하므로 SIM으로 우회할 수 없다. 해외 SIM을 이용한 허위 국가·주소·계정 정보는 심사/정산/계정 정지 리스크가 있어 권하지 않는다.

## 추천 선택

1. 1차 출시: iOS는 Apple IAP(StoreKit)로 구독·non-consumable을 구현하고, 웹은 먼저 한국 PG 또는 Paddle 온보딩을 문서·계약으로 확인한다.
2. 웹과 앱의 동일 계정 entitlement를 서버에서 관리하고, Apple transaction과 웹 provider webhook을 각각 검증한 뒤 사용자 권한을 합친다. 웹에서 산 권한을 앱에서 읽는 경우에도 앱 내 구매를 유도하는 버튼/링크가 Apple 규정에 어긋나지 않는지 검토한다. [Multiplatform Services 3.1.3(b)](https://developer.apple.com/app-store/review/guidelines/)는 다른 플랫폼에서 산 콘텐츠 접근을 허용하되 앱 안에서도 IAP 상품이 제공되어야 한다고 설명한다.
3. 한국 전용 외부 PSP entitlement는 국내 카드 UX/정산이 반드시 필요하고, 한국 전용 별도 앱·26% commission·월별 보고를 감수할 때만 비교한다. 외국 PSP를 이 트랙에 넣으려면 Apple에 PSP 심사를 먼저 받아야 하며, 승인 전 구현을 전제하지 않는다.

## 계약·운영 체크리스트

사업자 등록 국가/주소, 지원 통화와 한국 카드·간편결제, 구독 자동결제·카드 저장, 환불/차지백·고객지원, MoR 여부와 한국 부가세/송장, 정산 통화·은행, 개인정보 국외 이전·DPA, Apple 26%/보고·세금, 상품별 App Store 규정, 웹 구매자의 앱 접근 entitlement, 테스트/샌드박스와 webhook 재처리를 계약 전에 확인한다. 법률·세무 확정은 한국 전문가와 공급자 계약 검토가 필요하다.
