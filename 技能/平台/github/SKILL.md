---
name: platform-github
description: >
  Manages AlphaForge Founder presence on GitHub: public profile name/bio/website,
  pinned repos, profile README, avatar path. Use when editing GitHub profile,
  grlib bio, pinning alphaforge, or GitHub Settings / Profile README.
---

# Platform Skill: GitHub

Version: v1

## Purpose / When to use

改 GitHub 公开身份、置顶仓库、核对 Profile README。主战场是 **Profile + `grlib/alphaforge` 仓库**，不是荐股内容分发。

## Account

| 字段 | 值 |
|---|---|
| Handle / login | `grlib` |
| 显示名目标 | `AlphaForge Founder` |
| Profile | https://github.com/grlib |
| 产品仓库 | https://github.com/grlib/alphaforge |
| Profile README 仓库 | `grlib/grlib` |

## Language & Limits

- **语言侧重**：**英文 Bio**（身份包短版 / 压成档）；禁止中文塞进 Bio
- Name：无严格汉字/字母套餐限制（相对知乎宽松）
- Bio：约 **160 字符**；超限用身份包「压成」短版
- Website：单 URL；填 `https://github.com/grlib/alphaforge`（或身份包允许的 github.com/grlib）
- 禁止：旧个人域名

## Identity fields

| 字段 | 本站叫什么 | 用身份包哪一档 | 备注 |
|---|---|---|---|
| 显示名 | Name | 主名 `AlphaForge Founder` | login 保持 `grlib` |
| 简介 | Bio | **短版**（可压成档） | Settings → Public profile |
| Website | URL | 仓库 URL | 优先 alphaforge |
| 头像 | Profile picture | `内容/品牌/头像/avatar-400.png` | 自动化上传常失败 → 人工 |
| 置顶 | Pinned | — | 第一位必须是 `alphaforge` |

## Copy source

`内容/品牌/身份统一包.md` → 短版 / 压成档。  
禁止另写第二套故事。

## Posting

- 主内容在仓库 README / Issues / Profile README，不是社交短帖
- 草稿参考：`内容/草稿/第001期-GitHub.md`、`内容/草稿/github-主页-README.md`
- 有公开动态 URL 时回写 `增长.md` 与 `每日/`

## WebBridge ops

1. 遵守 `.cursor/rules/kimi-webbridge.mdc`
2. session 例：`alphaforge-github-profile`
3. 资料页：`https://github.com/settings/profile`
4. Bio 若 `fill` 失败：对 `#user_profile_bio` / textarea 用 evaluate 写 value 再 Update profile
5. **任务结束 `close_session`**

### 工具优先级

1. 已登录时：GitHub MCP / `gh`（若可用）改能改的字段
2. 否则：WebBridge 打开 Settings
3. 头像：优先 Founder 手动上传（见 pitfalls）

## Known pitfalls

- 头像：CDP `DOM.setFileInputFiles` / upload 返回 **Not allowed**（Chrome）；记 blocker，人工传 `avatar-400.png`
- Billing 横幅可忽略，不阻塞改资料
- 旧个人域名必须从 Website 清掉
- 不要把 `-chanlun` / `AI-Trader` 置顶压过 `alphaforge`

## Reply / DM

**Status: Not implemented**

预留：Issue / Discussion 回复语气、何时转私聊、不荐股。  
实现门槛：仓库出现真实外部互动后再开 Experiment。

## Evidence

- 账号状态：`增长.md`
- 落地 blocker：身份包「落地记录」
- 2026-08-18：Name + Bio + URL 已同步；头像待人工
