# AlphaForge Toolchain

严格区分 Used Tools 与 Built Tools。

评分 1–5。没有真实使用证据时不打高分。

---

## Used Tools

### Cursor

Purpose: Founder 与 Agent 的主工作台；写文档、跑实验、执行 `/start-day` `/end-day`。

Best For: 仓库内推理、多文件编辑、把创业上下文留在项目里。

Weakness: 若 AGENTS.md 不被遵守，容易滑向 Feature Factory。

Current Score: 5（Day 1 初始化主场，实际完成 Founder OS）

Lessons: 先 Plan → Review → Execute，比直接生成代码更符合本项目。

---

### GitHub MCP

Purpose: 在 Agent 会话内创建/查询 GitHub repository、issues、files。

Best For: 把 GitHub 操作留在同一工作流，不必切换浏览器。

Weakness: 当前无 milestone tool；不能替代 git 历史的本地控制。

Current Score: 4（成功创建 Public repo `grlib/alphaforge`；无 milestone tool）

Lessons: 先 `get_me` 再操作；创建仓库前先 search 是否已存在。

---

### GitHub

Purpose: 公开实验现场、Issues、Milestone、Build in Public 的源仓库。

Best For: 把创业过程变成可订阅的 Evidence。

Weakness: Stars 容易变成 Vanity Metric。

Current Score: n/a（Day 1 创建当天）

Lessons: Issues 只建高价值问题，不建 Feature 清单。

---

## Built Tools

### AlphaForge Founder OS v1

Version: v1

Purpose: 让 Founder + Agent 在没有完整产品代码的情况下，仍能按同一套原则、假设、日循环和证据规则推进。

Status: ACTIVE

Used By: Founder, Cursor Agent

Evaluation: Day 1 结束时检验：明天 `/start-day` 是否能在不重建上下文的情况下继续。

Known Failures: 尚无。风险是文档过多导致 Agent 不读。因此 AGENTS.md 必须短而可执行。

Next Improvement: 用 Day 2 的 `/start-day` 实测缺口；缺什么再补，不预先设计 v2。

---

## Not Yet Tools

以下存在于 Founder 资产库，但 **尚未** 引入 AlphaForge：

CZSC、QMT / qmt-mcp、Baostock、Local Database、Theme Pool、Stock Pool。

引入前必须有 Hypothesis 与 Experiment。见 D-001。
