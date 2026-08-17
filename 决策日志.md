# Decisions

所有重大决定记录在此。失败的决策不删除。

格式：

```markdown
## D-XXX — Decision

Date:

Status:

Context:

Evidence:

Decision:

Alternatives:

Why:

Implication:

Revisit When:
```

Status：`ACTIVE` `REVISITED` `SUPERSEDED`

---

## D-001 — Product hypotheses reset

Date: 2026-08-17

Status: ACTIVE

Context: Founder 过去积累了 CZSC、QMT、Baostock、Stock Pool、Report Generation 等系统。存在把旧系统直接迁入新仓库、当作 AlphaForge 需求的诱惑。

Evidence: 旧系统证明了「AI 能分析股票」的技术可行性，但没有证明「有人真正需要这个产品」。

Decision: 产品假设推倒重来。旧系统定义为 Reusable Assets，不定义为 Requirements。

Alternatives: 在旧系统上继续加 Agent 层；把旧功能作为 AlphaForge v1 范围。

Why: Asset ≠ Requirement。继续在旧假设上堆功能，会加速 Build Trap。

Implication: 任何旧能力的引入，必须先绑定一个新 Hypothesis 和一个便宜实验。

Revisit When: 某个实验明确证明需要某项旧能力（例如 QMT 行情、CZSC 结构分析）才能完成真实 Job。

---

## D-002 — Skill-first, UI-later

Date: 2026-08-17

Status: ACTIVE

Context: 投资产品默认会做成 Dashboard / App。这会把早期精力锁进界面。

Evidence: 无用户 Evidence。只有第一性原理：核心是 Method → Skills → Agent → Execution，不是屏幕。

Decision: Intelligence before Interface。优先 CLI、Markdown、Skills、Local Files、Existing Tools、Simple Scripts。

Alternatives: 先做 Web App / Dashboard 再补智能。

Why: 没人使用时做 UI，是 Architecture Trap 与 Feature Trap 的入口。

Implication: 初始化阶段禁止 Web App、Database、Login、Dashboard、Payment、Marketplace。

Revisit When: 至少一个 Skill 被 User Zero 或外部用户连续使用，并且界面成为执行瓶颈。

---

## D-003 — Build in Public from Day 1

Date: 2026-08-17

Status: ACTIVE

Context: AlphaForge 需要同时验证产品和获客。关起门来做 14 天，无法测试 H008。

Evidence: 无。H008 当前为 TESTING。

Decision: 从 Day 1 公开仓库、公开失败、公开工具与学习。Founder Positioning 是 Builder + Investor，不是 Stock Guru。

Alternatives: 先私有开发，有结果再公开；只公开成功。

Why: 内容本身是获客实验。只公开成功会制造 Confirmation Bias。

Implication: 每天必须有 Public Content Draft。不自动发布外部社交平台，除非 Founder 明确授权。

Revisit When: 14 天后评估 Build in Public 是否带来 ICP，而不是只带来围观。

---

## D-004 — Daily Founder Loop replaces fixed Feature Roadmap

Date: 2026-08-17

Status: ACTIVE

Context: 固定 14 天 Feature 清单会让团队（Founder + Agents）为完成任务而开发，而不是为降低不确定性而实验。

Evidence: 无。这是过程设计选择。

Decision: 14 天只规定方向。Day N+1 的具体任务必须由 Day N 的 Evidence 决定。

Alternatives: 预先写死 14 天功能计划并按表交付。

Why: 我们要学得足够快，而不是做得足够像一个创业公司。

Implication: Agent 不得在没有今天 Evidence 的情况下，提前实现 Day 9–14 的功能。

Revisit When: Day 8 Week 1 Review。如果 Loop 本身导致停滞，再修正。

---

## D-005 — Public GitHub repository under grlib/alphaforge

Date: 2026-08-17

Status: ACTIVE

Context: 需要一个可被世界看到的实验现场。GitHub MCP 已授权。`alphaforge` 在该账号下不存在。

Evidence: GitHub user `grlib`；search `user:grlib alphaforge in:name` 返回 0。

Decision: 创建 Public repository `alphaforge`。Description：Forge your investment method into an AI Agent. An open experiment in building a personal Investment Agent and an AI-native startup from zero.

Alternatives: Private repo；使用组织账号；换仓库名。

Why: D-003 要求 Day 1 公开。Founder 主 Prompt 已建议 Public，并授权 GitHub 操作。不另开组织，避免过早架构。

Implication: 不提交 secrets。失败案例默认可公开，敏感持仓与资金细节需脱敏。

Revisit When: 出现必须私有的用户数据或持仓 Evidence。

---

## D-006 — Milestones via GitHub API / gh；MCP 无 milestone tool

Date: 2026-08-17

Status: ACTIVE

Context: 需要 Milestone「14-Day Founder Experiment」。GitHub MCP 支持 repository、issues、files，不支持 milestones。

Evidence: 检查 MCP catalog 无 milestone tool。本地 `gh` 未登录。

Decision: 优先用 GitHub MCP 完成 repo / issues。Milestone 用 `gh` 或 GitHub API 创建；若当前环境无 gh 登录，则在能力恢复后补建，不为此阻塞 Founder OS。

Alternatives: 放弃 Milestone；为 milestone 自建脚本。

Why: Milestone 有用但不是 Existential。不为此造工具。

Implication: Issues 先创建，milestone 关联可能稍后补上。

Revisit When: gh 已登录或 MCP 增加 milestone 能力。

---

## D-007 — Defer LICENSE

Date: 2026-08-17

Status: ACTIVE

Context: Public repo 最终需要许可证。初始化时没有强约束。

Evidence: 无。

Decision: 暂缓 LICENSE，避免在实验第 1 天做法律设计。

Alternatives: MIT；Apache-2.0；保持默认版权保留。

Why: 不在 Existential Risk 路径上。

Implication: README 明确暂缓。他人 fork 时版权默认保留。

Revisit When: 有外部贡献者，或准备让 Skill 被他人使用。

---

## D-008 — `/start-day` and `/end-day` as Markdown Cursor commands

Date: 2026-08-17

Status: ACTIVE

Context: 需要可重复的日启动/日结束协议。

Evidence: 当前环境适合用 `.cursor/commands/*.md`，不必开发自定义 runtime。

Decision: 用 Markdown workflow 实现 `/start-day` 与 `/end-day`。不写 Hook、不写 Agent 框架。

Alternatives: Cursor Hooks；Python CLI；Slack bot。

Why: Do Not Overbuild。命令形式服务于 Loop，不服务于仪式感。

Implication: Founder 在 Cursor 输入 `/start-day` 或 `/end-day` 即可。若 slash command 未注册成功，直接打开对应 Markdown 作为 Prompt。

Revisit When: Loop 执行摩擦明显，或需要强制检查 Daily Log 完整性。
