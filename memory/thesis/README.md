# Investment Memory（最小）

Purpose: 让第二次 @ 能接上第一次 Thesis，而不是 Stateless Chat。

## Do Not Overbuild

只用 Markdown 文件。不要向量库、Knowledge Graph、多 Agent Memory。

## File layout

```text
memory/thesis/<object-slug>.md
```

`object-slug`：标的或主题的简短英文/拼音，如 `cb-valuation-2026`、`ai-theme`。

## Record schema（写在每个文件 frontmatter + 正文）

```yaml
---
thesis_id: th-YYYYMMDD-slug
user_handle: weilaihui-or-external
object: 可转债整体 / 某主题 / 某代码
thesis: 一句话
status: ACTIVE | STRENGTHENED | WEAKENED | INVALIDATED | CLOSED
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
source: jisilu | cursor | other
---
```

正文建议小节：

- Assumptions
- Evidence（Source / Date / 摘要）
- Counterarguments
- Invalidation Conditions
- Plan（Monitor / Trigger / Invalidation / Review）
- Changes（时间线：新增信息 → 对 Thesis 的影响）

## Workflow

1. 收到 @ 后，按 Object 搜本目录是否已有文件
2. 有 → 先读再回复「你上次… / 今天新增…」
3. 无 → 试炼后新建文件（Founder 确认对外发出后，或 User Zero 试跑后）
4. 用户纠正 → 追加 Changes + 必要时改 status

## Privacy

公开社区对话写入前脱敏持仓金额；敏感细节可只留本地、不进 Public repo 推送范围（若需私有，移出默认提交路径并告知 Founder）。
