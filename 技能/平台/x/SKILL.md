---
name: platform-x
description: >
  Manages AlphaForge Founder presence on X/Twitter: display name, bio, website,
  posting Episode drafts. Use when editing X profile, Twitter bio, @daixiaolinuka88,
  or publishing short posts on X.
---

# Platform Skill: X (Twitter)

Version: v1.1

## Purpose / When to use

改 X 显示名 / Bio / Website，发短帖（第 N 期）。面向国际 Builder 信号；字数紧，英文有限。

## Account

| 字段 | 值 |
|---|---|
| Handle | `@daixiaolinuka88` |
| 登录相关名 | weilaihui（后台可能仍可见） |
| 显示名目标 | `AlphaForge Founder` |
| 主页 | https://x.com/daixiaolinuka88 |

## Language & Limits

- **语言侧重**：**英文有限**；Bio 约 **160 字符**（中英混排按字符计）
- Display name：可用 `AlphaForge Founder`
- Website：`https://github.com/grlib`（简介层）；帖子正文再放 alphaforge 仓库
- 发帖：优先单段短文；多段易截断
- 禁止：旧个人域名、荐股话术

## Identity fields

| 字段 | 本站叫什么 | 用身份包哪一档 | 备注 |
|---|---|---|---|
| 显示名 | Name | 主名 | Edit profile |
| 简介 | Bio | **短版**；超限用压成档 | `textarea[name=description]` |
| Website | Website / url | 身份包 Website | `https://github.com/grlib` |
| 头像 | Avatar | `avatar-400.png` | 自动化常 Not allowed → 人工 |

## Copy source

`内容/品牌/身份统一包.md` → 短版 / 压成档。

## Posting

### 入口

- 设置：`https://x.com/settings/profile`
- 发帖：主页 Compose；草稿 `内容/草稿/第00N期-X.md`
- 裁切规格：`内容/内容模板.md` → **Thread 5–8 条**，不要单条长墙

### 形态

- 钩子帖 + thread：钩子 → 昨日 → Skill/动作 → 工具 → 墙 → GitHub
- **一条一个点**；数字优先；失败比成功好点

### 截断坑

- 多段 contenteditable `fill` 易只发第一段 → 优先 **短段 CDP `insertText`**，或拆成回复链
- 配图 upload 常 **Not allowed** → 可先发文字 thread

### 发布门禁

- 钩子帖独立可读；thread 含至少 1 个失败点 + 仓库链接

### 发后核对清单

- [ ] 每条 URL 可打开
- [ ] 无整段截断
- [ ] URL 回写 `增长.md` / `每日/`

### Evidence

- EP-002：https://x.com/daixiaolinuka88/status/2089646778761244972

## WebBridge ops

1. 遵守 `.cursor/rules/kimi-webbridge.mdc`
2. session 按任务命名
3. Bio：`fill` 常 Uncaught → evaluate 写 `textarea[name=description]` 再 Save
4. 少开标签；**结束 `close_session`**

## Known pitfalls

- Bio / 富文本 `fill` 易失败；用 description textarea + evaluate
- Setup profile 向导曾卡住，阻断改 Bio（需 Founder 点过或跳过）
- 头像 upload / CDP 文件：**Not allowed**
- 发帖多段易只发出第一段 → 用 thread / 回复补全，并记真实 URL

## Reply / DM

**Status: Not implemented**

预留：回复 mention / 评论、处理 DM、筛选 ICP。  
实现门槛：有稳定互动量后再做。

## Evidence

- `增长.md` 账号账本
- 2026-08-18：Display name + Bio + Website 已核对公开页；头像待人工
