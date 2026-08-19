---
name: platform-xueqiu
description: >
  Manages AlphaForge Founder presence on Xueqiu (雪球): nickname, bio, homepage
  link, Chinese posts. Use when editing 雪球资料、简介、发帖, or xueqiu.com profile.
---

# Platform Skill: 雪球 (Xueqiu)

Version: v1.1

## Purpose / When to use

在雪球维护投资者语境下的 Builder 身份：改昵称 / 简介 / 主页链，发中文帖。更靠近 A 股用户，但仍 **不荐股**。

## Account

| 字段 | 值 |
|---|---|
| UID | `6230350172` |
| 旧昵称（废弃） | 刚好的金融小飞机场 |
| 显示名目标 | `AlphaForge Founder` |
| 主页 | https://xueqiu.com/u/6230350172 |

## Language & Limits

- **语言侧重**：**中文有限**
- 个人简介：约 **≤200 字**（用身份包 **中版**）
- 昵称：以平台规则为准；目标主名，冲突时记 blocker
- 发帖：中文；正文带 `github.com/grlib`，再视需要放 alphaforge
- 禁止：荐股、必涨、旧「金融小飞机场」叙事、旧个人域名

## Identity fields

| 字段 | 本站叫什么 | 用身份包哪一档 | 备注 |
|---|---|---|---|
| 显示名 | 昵称 | 主名 | 替换旧昵称 |
| 简介 | 个人简介 | **中版** | ≤200 字裁切 |
| 网站 / 主页 | 能填则填 | `https://github.com/grlib` | |
| 头像 | 头像 | `avatar-400.png` | 优先人工 |

## Copy source

`内容/品牌/身份统一包.md` → **中版**。

## Posting

### 入口（必读）

- **走「长文」**，不要用首页短框（`.medium-editor-element` 尺寸常为 0，写不进）
- 首页 / 创作入口点 **长文**；参考 [运营指南](https://xueqiu.com/operation/guide)
- 避免单独打开空白的 `mp.xueqiu.com/writeV2`（2026-08-18 已验证白页）
- 设置参考：`https://xueqiu.com/setting/user-info`
- 草稿：`内容/草稿/第00N期-雪球.md`；裁切规格见 `内容/内容模板.md`

### 形态

- **一个判断** + **2–4 个数字**（Skill 数、失败墙条数、URL）+ 图（能传则传）+ 提问
- 篇幅不宜过长；忌情绪帖、忌荐股
- 正文软链：`github.com/grlib` + `github.com/grlib/alphaforge`

### 截断 / 写入坑

- 首页短框：composer 高度 0 → fill / insertText 无效
- 多段 contenteditable：优先短段 CDP `insertText`，或长文编辑器一次粘贴后核对

### 发布门禁

- 公开预览 / 正文含判断句 + 至少 2 个数字 + 仓库链接

### 发后核对清单

- [ ] 公开 URL 可打开
- [ ] 判断句与数字在
- [ ] 不是首页短框空发
- [ ] URL 回写 `增长.md` / `每日/`

### Evidence 帖

- Day1：https://xueqiu.com/6230350172/405350495
- EP-002：https://xueqiu.com/6230350172/405576781（2026-08-19 长文；入口 `mp.xueqiu.com/write/?position=pc_home_post`）

## WebBridge ops

1. 遵守 `.cursor/rules/kimi-webbridge.mdc`
2. session 按任务命名，例如 `alphaforge-xueqiu-ep002`
3. 先确认能打开 xueqiu.com；若「无法访问此网站」→ **停**，记 blocker，不假装已改
4. **结束 `close_session`**

## Known pitfalls

- 浏览器偶发 **无法访问 xueqiu.com**（代理/防火墙）；2026-08-18 身份同步因此未完成
- 2026-08-18 EP-002：首页短框写不进；`writeV2` 空白页
- 旧昵称像普通股民号，必须换成 AlphaForge 叙事
- 多标签易卡；同任务少开 tab

## Reply / DM

**Status: Not implemented**

预留：回复评论、私信筛选有方法的投资者、拒绝荐股请求。  
实现门槛：有真实留言/私信后再开。

## Evidence

- `增长.md`；身份包落地记录
- 2026-08-18：站点不可达，昵称/简介/头像均待网络恢复后重试
