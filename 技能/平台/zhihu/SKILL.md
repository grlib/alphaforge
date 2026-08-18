---
name: platform-zhihu
description: >
  Manages AlphaForge Founder presence on Zhihu (知乎): display name rules,
  one-liner headline, long bio, articles. Use when editing 知乎资料、一句话介绍、
  个人简介、发文章, or zhihu.com/people profile.
---

# Platform Skill: 知乎 (Zhihu)

Version: v1

## Purpose / When to use

改知乎公开资料（一句话 + 个人简介），发长文叙事。中文字数极紧；改名规则苛刻。

## Account

| 字段 | 值 |
|---|---|
| Handle | `maltsuger` |
| 当前显示名（2026-08-18） | 麦芽糖 |
| 显示名目标 | 主名 `AlphaForge Founder`；受限时短名 `AlphaForge` |
| 主页 | https://www.zhihu.com/people/maltsuger |
| 编辑页 | https://www.zhihu.com/people/edit |

## Language & Limits

- **语言侧重**：**中文有限**
- **一句话介绍**：约 **≤18 字** → 身份包 **超短**
- **个人简介**：可用 **长版**（多段）
- **名称规则（已验证）**：须 **2–8 个汉字**，或 **4–16 个字母**  
  - `AlphaForge Founder` 超限  
  - 短名 `AlphaForge`（10 字母）在规则内，但曾保存未生效（可能需会员改名）
- 禁止：荐股、`mian45.com`

## Identity fields

| 字段 | 本站叫什么 | 用身份包哪一档 | 备注 |
|---|---|---|---|
| 显示名 | 姓名 / 用户名 | 短名优先尝试 | 失败则保留现状 + 记 blocker |
| 一句话 | 一句话介绍 | **超短** | ≈18 字 |
| 个人简介 | 个人简介 | **长版** | textarea；多段用 evaluate 写 value |
| 网站 | 简介内链接 | github.com/grlib + 仓库 | |
| 头像 | 修改我的头像 | `avatar-400.png` | upload Not allowed → 人工 |

## Copy source

`内容/品牌/身份统一包.md` → 超短 + 长版。

## Posting

- 长文草稿：`内容/草稿/第001期-知乎.md`
- Day1 专栏：https://zhuanlan.zhihu.com/p/2072745440886388676（正文曾截断，需复查）
- 多段落发文：优先短段 CDP `insertText`，避免 contenteditable `fill` 截断
- URL 回写 `增长.md` / `每日/`

## WebBridge ops

1. 遵守 `.cursor/rules/kimi-webbridge.mdc`
2. session 例：`alphaforge-zhihu-profile` / `alphaforge-zhihu-post`
3. 简介长文：`fill` 常 Uncaught → 对 `textarea` 用 prototype set value + input/change，再点保存
4. **结束 `close_session`**

## Known pitfalls

- 改名失败提示：`姓名应为 2-8 个汉字，或 4-16 个字母`
- 会员「改名加速」可能挡短名保存
- 文章 / 简介多段 `fill` 截断
- 头像：`UploadPicture-input` upload → **Not allowed**
- Settings 有时跳到「账号与密码」而非编辑页 → 用 `/people/edit`

## Reply / DM

**Status: Not implemented**

预留：回答评论、处理私信、专栏互动。  
实现门槛：有真实讨论再开，不做空转客服机器人。

## Evidence

- `增长.md`；身份包落地记录
- 2026-08-18：超短 + 长版已更新；显示名仍「麦芽糖」；头像待人工
