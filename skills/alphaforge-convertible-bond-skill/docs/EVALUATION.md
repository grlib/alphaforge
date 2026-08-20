# Evaluation

是否成功，不看“回复像不像研报”。

看是否比裸大模型多出：

> 可验证的数据、计算、比较和关系解释。

每项 0–2：

1. Data Correctness
2. Math Correctness
3. Intent Match
4. Relative Reasoning
5. Event Awareness
6. Scenario Clarity
7. Hallucination Control
8. Usefulness
9. Conciseness

满分 18。

## Release Gate

第一版发布前，找 20 个真实集思录可转债问题。

A = 裸大模型
B = AlphaForge Skill

Blind Review：

```text
B 明显更有价值 >= 70%
```

否则不公开发布。

## Failure Taxonomy

```text
DATA_MISSING
DATA_WRONG
MATH_ERROR
GENERIC_REPORT
BAD_ATTRIBUTION
NO_RELATIVE_CONTEXT
EVENT_MISSED
SCENARIO_CONFUSED
HALLUCINATION
TOO_LONG
NO_ACTIONABLE_WATCH
```
