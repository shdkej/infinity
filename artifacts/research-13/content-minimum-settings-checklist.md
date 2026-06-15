# Content Minimum Settings Checklist

- id: research-13
- date: 2026-06-15
- status: final
- use: Infinity content-creation brief defaults

## 결론

콘텐츠를 만들기 전에 필요한 최소 설정은 "누구에게, 어떤 상태에서, 무엇을 남기기 위해, 어떤 말투와 형식으로, 어떤 근거를 써서, 어떤 다음 행동으로 닫을 것인가"를 정하는 것이다.

너무 많은 입력칸은 제작을 늦춘다. Infinity에서는 아래 8개를 필수값으로 두고, 나머지 4개는 필요할 때만 켜는 것이 좋다.

## 필수 8개

| # | 설정값 | 왜 필요한가 | 짧은 입력 예시 |
|---|---|---|---|
| 1 | `target_reader` 타겟 독자 | 콘텐츠가 누구의 언어로 쓰일지 결정한다. | AI로 1인 여행/제품 실험을 시작하려는 사람 |
| 2 | `reader_state` 독자의 현재 상태 | 같은 독자라도 초보/비교/결정 직전이면 문장이 달라진다. | 관심은 있지만 어디서 시작할지 모름 |
| 3 | `reader_problem` 독자가 겪는 문제 | 글의 초반 압력과 사례 선택을 정한다. | 도구는 많은데 실제 산출물이 없음 |
| 4 | `content_goal` 콘텐츠 목적 | 정보 제공, 설득, 기록, 판매, 관계 형성 중 무엇인지 고른다. | 실행 기준 하나를 가져가게 하기 |
| 5 | `core_message` 핵심 메시지 | 글이 끝난 뒤 남아야 할 한 문장이다. | 시작은 도구가 아니라 반복 가능한 작은 출력이다 |
| 6 | `angle` 관점/비틀기 | 흔한 주제에서 이 글만의 시선을 만든다. | 생산성 팁이 아니라 여행 전 운영체계로 보기 |
| 7 | `tone_voice` 톤/보이스 | 같은 메시지도 친절한 안내, 날카로운 주장, 조용한 회고로 달라진다. | 담백함, 존댓말, 과장 금지, 실무자 말투 |
| 8 | `format_channel` 형식/채널 | 길이, 구조, CTA, 이미지 필요 여부를 정한다. | Threads 4줄 / 블로그 1,200자 / 유튜브 8분 |

## 거의 필수에 가까운 보조 4개

| 설정값 | 언제 필요한가 | 예시 |
|---|---|---|
| `evidence_pack` 근거/재료 | 주장형, 정보형, 리뷰형, 리서치형 콘텐츠 | 경험 1개 + 수치 1개 + 반례 1개 |
| `desired_action` 다음 행동/CTA | 독자가 글을 보고 무엇을 해야 하는지 정해야 할 때 | 저장하기, 댓글로 상황 남기기, 템플릿 써보기 |
| `boundary` 금지선/비대상 | 말투 드리프트, 과장, 내부어 노출을 막아야 할 때 | 돈 번다는 표현 금지, AI 만능론 금지 |
| `success_signal` 성공 기준 | 반복 콘텐츠, 캠페인, 실험형 콘텐츠 | 저장률, 답글 수, 상담 요청, 다음 글 소재 발생 |

## Infinity용 최소 스키마

```yaml
content_brief:
  target_reader: ""
  reader_state: ""
  reader_problem: ""
  content_goal: ""
  core_message: ""
  angle: ""
  tone_voice:
    voice: ""
    tone: ""
    avoid: []
  format_channel:
    channel: ""
    length: ""
    structure: ""
  evidence_pack:
    experience: []
    sources: []
    examples: []
  desired_action: ""
  boundary:
    must_include: []
    must_avoid: []
  success_signal: ""
```

## 한 줄 브리프 템플릿

`{target_reader}`가 `{reader_state}`에서 `{reader_problem}`을 겪고 있을 때, `{core_message}`를 `{tone_voice}` 톤으로 `{format_channel}`에 맞춰 전달하고, 마지막에는 `{desired_action}`으로 닫는다.

예시:

> AI로 여행 콘텐츠를 만들고 싶지만 시작 기준이 흐린 1인 창작자에게, "처음 필요한 것은 툴 목록이 아니라 반복 가능한 기록 포맷"이라는 메시지를 담백한 실무 톤의 Threads 4줄로 전달하고, 마지막에는 오늘 기록 포맷 1개를 고르게 한다.

## 기본값 제안

Infinity에서 콘텐츠 생성 Intent를 만들 때는 다음처럼 시작한다.

```yaml
defaults:
  tone_voice:
    voice: "담백하고 구체적인 존댓말"
    tone: "조용하지만 판단이 선명함"
    avoid:
      - "과장된 성공담"
      - "내부 자동화 용어"
      - "AI 만능론"
      - "추상적인 자기계발 문장"
  format_channel:
    channel: "Threads"
    length: "3-5줄"
    structure: "상황 1줄 -> 판단 1줄 -> 구체 예시 1-2줄 -> 다음 행동 1줄"
  evidence_pack:
    experience: ["사용자 실제 작업/여행/제품 실험에서 나온 장면"]
    sources: []
    examples: []
  boundary:
    must_include:
      - "구체 장면 또는 숫자 1개"
    must_avoid:
      - "프로젝트명만 나열하는 작업 로그"
      - "독자가 모르는 내부 약어"
```

## 짧은 검수 질문

1. 이 글의 독자가 한 문장으로 보이는가?
2. 독자의 현재 상태가 보이는가?
3. 글이 끝난 뒤 남을 한 문장이 있는가?
4. 톤이 "누구처럼"이 아니라 실제 문장 규칙으로 적혔는가?
5. 채널 길이와 구조가 정해졌는가?
6. 근거 없이 주장만 세게 하지 않는가?
7. 독자의 다음 행동이 있는가?
8. 쓰면 안 되는 말/범위가 정해졌는가?

## 출처 메모

- Content Marketing Institute: content brief는 과제 설명, 브랜드 세부사항, tone/voice/style, key messages, target audience insights를 포함해야 한다고 정리한다.
- HubSpot: content brief에는 content goal, strategy, target audience, keywords, page structure가 들어가며, brief가 없으면 tone drift와 message loss가 생긴다고 설명한다.
- Mailchimp: voice/tone 가이드는 target audience, goals, core values에서 출발한다.
- Nielsen Norman Group: tone of voice는 humor, formality, respectfulness, enthusiasm 네 축으로 분석할 수 있고, plain language는 사용자가 처음 읽을 때 이해 가능해야 한다고 본다.
- Content Marketing Institute: content strategy는 organization mission, target audience, business goals, content objectives 순서로 좁혀야 한다고 설명한다.

## 판단

Infinity에 넣을 최소 설정은 "콘텐츠 전략 전체"가 아니라 "초안 생성 직전의 브리프"여야 한다. 그래서 시장조사, 키워드, 유통 캘린더, 세부 SEO, 디자인 시스템은 기본 필수값에서 제외한다. 필요한 Intent에서만 보조 필드로 켠다.
