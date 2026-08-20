# AlphaForge Convertible Bond Intelligence Skill

> **Data × Tools × Rules × LLM**

一个面向可转债研究的 Agent Skill。目标不是生成“万能研报”，而是把一个转债问题转化成：

**数据事实 → 计算关系 → 横向/历史比较 → 事件/情景分析 → 可解释结论**

## 核心定位

这个 Skill 不直接回答“XX 转债值得买吗？”，而优先回答：

- 现在贵不贵，贵在哪里？
- 正股和转债为什么今天表现不一致？
- 溢价率变化来自哪里？
- 当前更应该关注强赎、下修、回售、到期还是信用风险？
- 和同类转债相比，它异常在哪里？
- 如果正股涨跌 10%，机械情景会怎样？
- 哪些变量真正会改变判断？

## 适合的提问

```text
@AlphaForge XX转债为什么今天正股涨、转债反而跌？
@AlphaForge XX转债现在贵不贵？
@AlphaForge 这个转债最需要关注什么风险？
@AlphaForge 帮我比较 A转债 和 B转债
@AlphaForge 如果正股再跌10%，这个债会怎样？
```

## 核心原则

1. Facts before opinions
2. Calculator before LLM
3. Relative comparison before absolute labels
4. Scenario before recommendation
5. Unknown is better than fabricated
6. No fake precision
7. No generic stock-report template

## 快速测试

```bash
cd alphaforge-convertible-bond-skill
python tools/analyze_sample.py
python -m unittest tests/test_cb_math.py
```

## 数据源

Skill 不绑定数据源。可接 QMT / Baostock / 自有数据库 / 合法授权的数据服务 / MCP。

只要最终转换成 `ConvertibleBondSnapshot` 数据结构即可。

详见 `docs/DATA_CONTRACT.md` 和 `docs/INTEGRATION.md`。
