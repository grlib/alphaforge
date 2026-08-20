# Evaluation — 投资想法试炼器

## What to score（每条 Case / 真实 @）

| Dimension | Question | Score |
|---|---|---|
| Thesis Extraction | 是否正确理解用户真正观点？ | pass / fail / partial |
| Assumption Discovery | 是否发现关键隐含假设？ | pass / fail / partial |
| Evidence Relevance | Evidence 是否真正影响 Thesis？ | pass / fail / partial / n/a |
| Counterargument Quality | 是不是 Strongest Counterargument？ | pass / fail / partial |
| Falsifiability | 有没有真正可证伪条件？ | pass / fail / partial |
| Actionability | 能否形成可跟踪 Plan？ | pass / fail / partial / n/a |
| Hallucination | 是否出现无依据 Fact？ | none / suspected / clear |
| User Correction | 用户是否需要纠正？（有真实对话才填） | yes / no / n/a |

## Failure taxonomy

见主 SKILL。失败写入 `cases/failure/`，优先加 Case 不先加长 Prompt。

## Skeleton log

试跑汇总：`evaluation/试跑-2026-08-20.md`
