# Metrics

## North Star Candidate

> **Weekly Meaningful Decisions — WMD**

Agent 真正帮助用户完成多少次有意义的投资判断。

### 计入 WMD 的例子

- 过滤无关信息，并留下可复查的过滤依据
- 发现 Thesis 变化
- Plan Trigger
- Plan Invalidated
- 更新 Stock Pool
- 发现关键风险
- 完成 Review，并产生可执行的学习

### 不计入 WMD

- 模型输出了很多字
- 生成了一份好看的报告但没有判断
- 用户只是打开了产品
- Agent 给出买卖建议但用户未纳入决策过程

14 天内 WMD 样本会很小。小样本必须如实记录，禁止外推成市场结论。

---

## Supporting Metrics

只在有数据时记录。没有数据就写 `n/a`，不要编。

| Metric | 问的问题 |
|---|---|
| Activation | 用户是否完成第一次有意义的 Method → Skill 执行？ |
| D7 / W2 / W3 Retention | 是否回来继续跑 Loop？ |
| Time Saved | 同一 Job 前后耗时 |
| Signal-to-Noise | 输入信息条数 vs 真正留下的条数 vs 人工认可条数 |
| Human Correction Rate | Agent 结论被用户修正的比例 |
| Payment | 是否有人付真钱 |
| Renewal | 付过的人是否续 |
| Content → GitHub | 内容是否带来仓库访问 / Issue |
| GitHub → Skill | 访客是否开始用 Skill |
| Skill → Activation | 用了 Skill 是否完成第一次有效执行 |
| Activation → Paid | 激活后是否付费 |

---

## Anti-metrics / 不能单独当作成功证据

- Token 消耗
- Code Lines
- Feature Count
- GitHub Stars
- Followers
- Likes

这些可以记录为 Distribution 信号，但不能替代 Retention / Payment / WMD。

---

## How we log

每天 Daily Log 第 8 节记录当天数字。

需要跨天对照时，写入 `metrics/` 下的周记，而不是先做 metrics dashboard。
