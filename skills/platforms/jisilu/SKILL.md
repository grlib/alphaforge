---
name: platform-jisilu
description: >
  Manages AlphaForge Founder presence on Jisilu (集思录): bio, homepage link,
  avatar, single-thread updates under EP-001, and jisilu-tick (collect @weilaihui,
  draft via investment-thesis-challenger, Founder-confirm reply). Use when 集思录资料、
  主贴回复、单帖推进、jisilu-tick、@weilaihui、炼一下、收问作答.
---

# Platform Skill: 集思录 (Jisilu)

Version: v1.5

## Purpose / When to use

在集思录维护 Builder 身份：改简介 / 主贴推进（D-010）；以及 **jisilu-tick**：收 **@weilaihui** → 加载 **投资想法试炼器** 出草稿 → Founder 确认后发。

社区调性：重数据、重逻辑、轻结论；忌营销/灌水。人格：愿意听逻辑、帮找漏洞、唱反调、记住上次为什么这么想——不是股神、不是客服百科。

新加入流程见 [`../说明.md`](../说明.md)。

## Account

| 字段 | 值 |
|---|---|
| Handle / 昵称 | `weilaihui`（**不改**） |
| 主页 | https://www.jisilu.cn/people/weilaihui |
| 设置入口 | https://www.jisilu.cn/setting/profile/ |
| 用户等级（2026-08-18） | **普通用户**（威望 4） |

## Language & Limits

- **中文有限**；简介需活跃用户以上才能设 → 普通用户阶段可能无法同步
- 改昵称：30 天一次、18 金币、降权新人 → **默认不改**
- 禁止：荐股、必涨、产品发布腔、`mian45.com`

## Identity fields

| 字段 | 本站 | 身份包 | 备注 |
|---|---|---|---|
| 显示名 | 昵称 | — | 保留 `weilaihui` |
| 简介 | 签名 | 中版 | Blocker：活跃用户 |
| 头像 | 头像 | avatar-400 | Blocker：活跃用户 |

## Copy source

`内容/品牌/身份统一包.md` → **中版**。

## Posting

**D-010 — 单帖推进。** 主贴：https://www.jisilu.cn/question/524510

日常形态：主贴下**回复**。草稿：`内容/草稿/第00N期-集思录.md`（标注 `形态: 主贴回复`）。

```text
打开 EP-001 → #advanced_editor 写短更新 → #save_answer_button → 核对可见 → close_session
```

例外才 `/publish/`。EP-002 为历史，不再挂日常更新。

## jisilu-tick（交易日 1 次）

收 @ + 实验短更新同一趟。节奏：收盘后或 `/end-day` 前。**不要** 5 分钟轮询。

```text
1. WebBridge session（alphaforge-jisilu-tick）；确认登录
2. 打开 EP-001 与/或通知；只收集含 @weilaihui 的提问
3. 未 @ → 跳过
4. 每条 @：Read `skills/investment-thesis-challenger/SKILL.md`
   → Intent（默认 THESIS_REVIEW）
   → 拆·查·驳·证·行 出草稿
   → 需要读表口径时再 Read `skills/low-risk-query/SKILL.md`（helper）
   → 有旧 Object则读 `memory/thesis/`
5. 草稿交 Founder；**未确认不得发出**
6. 确认后回复提问线程；写/更新 Memory
7. 若有实验短更新：同趟 EP-001 再回一条（条数少）
8. close_session
```

**不做：** 扫未 @ 评论、自动发帖、五站监听。

## WebBridge ops

遵守 `.cursor/rules/kimi-webbridge.mdc`；一任务一 session；用完 `close_session`。

## Known pitfalls

- 普通用户不能设签名/头像；改昵称成本高
- 单帖推进；防刷屏；多标签易卡
- 新帖可能「暂时无法回复」

## Reply / DM

**Status: thin hook (v1.5)**

- @weilaihui → **投资想法试炼器**（D-011）
- 低风险查询 = helper only
- 自动回复 = 未实现

## Evidence

- D-009 开通；D-010 单帖；D-011 试炼器为主 Skill
- EP-001 https://www.jisilu.cn/question/524510
- EP-002 https://www.jisilu.cn/question/524518（历史）
- 2026-08-20：jisilu-tick 改挂试炼器（v1.5）
