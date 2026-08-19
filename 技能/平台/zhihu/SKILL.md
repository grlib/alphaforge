---
name: platform-zhihu
description: >
  Manages AlphaForge Founder presence on Zhihu (知乎): display name rules,
  one-liner headline, long bio, articles. Use when editing 知乎资料、一句话介绍、
  个人简介、发文章, or zhihu.com/people profile.
---

# Platform Skill: 知乎 (Zhihu)

Version: v1.1

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
- 禁止：荐股、旧个人域名

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
每日裁切规格：`内容/内容模板.md` → 知乎专栏叙事。

## Posting

### 入口

- 新文：知乎写文章 / 专栏编辑器
- 改已发：`https://zhuanlan.zhihu.com/p/{id}/edit`
- 草稿参考：`内容/草稿/第00N期-知乎.md`；导入用正文文件（无 frontmatter）如 `第002期-知乎-导入正文.md`

### 形态

- 钩子 → 判断句 H2 → 证据 → 引用失败墙 → 提问
- **禁止**五段日志标题；约 1500–3000 字讲清一个判断

### 可靠写入（优先）

Chrome 对 `input[type=file]` / CDP upload 常返回 **Not allowed**；`fill` / 多段 `insertText` 会让**屏幕有字、Draft.js 未入库**（公开页只剩结尾）。

**推荐自动化路径（2026-08-19 已验证）：**

1. 把 Markdown 收成知乎 HTML（`<p>` / `<h2>` / `<blockquote>` / `<ul>`）
2. 用页面登录态 `PATCH https://zhuanlan.zhihu.com/api/articles/{id}/draft`，body：`{title, content}`  
   - JSON 经 **UTF-8 → base64 → `TextDecoder`** 注入 evaluate；**禁止**裸 `atob`+`JSON.parse`（会把中文弄成 mojibake）
3. `PUT https://zhuanlan.zhihu.com/api/articles/{id}/publish`（空 JSON `{}` 即可）
4. 打开**无** `/edit` 的公开 URL 核对

次选：工具栏 **导入** Markdown →「确认并解析」。自动化选文件常被拦；不要依赖 Founder 每次手导。

**禁止：** 一次 `fill` 整篇；只看编辑器 `innerText` 就点发布。

### 发布门禁（不满足不准发）

- 编辑器底部字数 **> 800**（或 draft API `content` 纯文本等价长度达标）
- 正文含第一节判断（或钩子句）+ GitHub 双链（`grlib/alphaforge` 与 `grlib`）

### 配图

- 工具栏「图片」本地上传；CDP upload / `uploaded_images` 曾 **Not allowed / 403**
- 不要只贴 raw.githubusercontent 链接当正文图
- EP-002 配图路径：`内容/草稿/配图/ep002-{cover,skill-flow,results}.png`（正文已修好时图仍可能待补）

### 发后核对清单

- [ ] 公开页标题正确
- [ ] 钩子 / 第一节在，且未重复多遍
- [ ] H2 为真正标题（不是字面 `##`）
- [ ] GitHub 双链可点
- [ ] 结尾提问在
- [ ] URL 回写 `增长.md` / `每日/`

### Evidence 帖

- EP-002：https://zhuanlan.zhihu.com/p/2073100563609302884（2026-08-19 以 draft PATCH + publish PUT 补全文）
- Day1 专栏：https://zhuanlan.zhihu.com/p/2072745440886388676（正文曾截断，需复查）

## WebBridge ops

1. 遵守 `.cursor/rules/kimi-webbridge.mdc`
2. session 按任务命名，例如 `alphaforge-zhihu-fix`
3. 简介长文：`fill` 常 Uncaught → 对 `textarea` 用 prototype set value + input/change，再点保存
4. **结束 `close_session`**

## Known pitfalls

- **Draft.js 保存态 ≠ 屏幕 innerText**：公开页曾只剩结尾提问（EP-001 / EP-002）
- 改名失败提示：`姓名应为 2-8 个汉字，或 4-16 个字母`
- 头像 / 导入文件：upload **Not allowed**
- 配图 API `uploaded_images`：**403**
- Settings 有时跳到「账号与密码」→ 用 `/people/edit`

## Reply / DM

**Status: Not implemented**

## Evidence

- `增长.md`；身份包落地记录
- 2026-08-18：超短 + 长版已更新；显示名仍「麦芽糖」；头像待人工
- 2026-08-19：EP-002 公开页全文 + H2 已核对；配图仍待（upload 阻断）
