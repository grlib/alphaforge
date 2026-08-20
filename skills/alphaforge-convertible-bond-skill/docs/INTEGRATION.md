# Integration Guide

## Cursor / Codex 项目安装

把整个目录复制到：

```text
<your-project>/
└── skills/
    └── convertible-bond-intelligence/
```

然后在项目 `AGENTS.md` 增加：

```markdown
## Available Skills

### Convertible Bond Intelligence

Path:
`skills/convertible-bond-intelligence/SKILL.md`

When:
用户询问可转债异动、贵不贵、风险、比较、情景分析时读取该 Skill。

Rule:
涉及当前行情时必须先调用本地数据工具，不允许根据模型记忆猜数据。
```

推荐 Agent Workflow：

```text
Question
↓
Read SKILL.md
↓
Fetch real snapshot
↓
Run deterministic calculations
↓
Relative / event analysis
↓
LLM explanation
```

## 接 QMT / Baostock / Local DB

建议增加：

```text
tools/providers/
├── qmt_provider.py
├── baostock_provider.py
└── local_db_provider.py
```

统一输出：

```python
def get_convertible_bond_snapshot(code: str) -> dict:
    ...
```

满足 `docs/DATA_CONTRACT.md` 即可。

## 接 MCP

如果已有 QMT MCP：

```text
Question
↓
read SKILL.md
↓
call qmt-mcp / data-mcp
↓
normalize result
↓
cb_math.py
↓
scenario.py
↓
final answer
```

## 第一版不要做

- 自动交易
- 推荐排名
- 复杂评分系统
- 全市场 Radar
- 知识图谱
- 向量数据库
- 大型 Web UI

第一版目标只有：

> 单债问题回答明显优于裸大模型。
