---
name: platform-jisilu
description: >
  Manages AlphaForge Founder presence on Jisilu (集思录): bio, homepage link,
  avatar, community posts. Use when editing 集思录资料、简介、发帖, jisilu.cn
  profile, or 知识库发起.
---

# Platform Skill: 集思录 (Jisilu)

Version: v1

## Purpose / When to use

在集思录维护投资者语境下的 Builder 身份：改简介 / 主页链 / 头像，发社区主贴。  
更靠近有方法的 A 股投资者，但仍 **不荐股**。社区调性：**重数据、重逻辑、轻结论**；忌营销/灌水腔。

新加入时遵循 [`../说明.md`](../说明.md)「新加入流程」：先同步基础信息 → 再问是否同步已有文章。

## Account

| 字段 | 值 |
|---|---|
| Handle / 昵称 | `weilaihui`（**不改**） |
| 显示名策略 | 保留现有昵称；改名需 18 金币且降权新人 |
| 主页 | https://www.jisilu.cn/people/weilaihui |
| 设置入口 | https://www.jisilu.cn/setting/profile/ |
| 用户等级（2026-08-18） | **普通用户**（威望 4） |

## Language & Limits

- **语言侧重**：**中文有限**
- 个人简介（介绍 / 签名）：身份包 **中版**；但 **需「活跃用户」以上** 才能设置 → 普通用户阶段无法同步
- **昵称硬规则**：30 天内只能改一次、消耗 18 金币、改完降权为新人 → **默认不改**；当前金币 0，也无法改
- 无独立 Website 字段；链接只能写进签名（签名本身又被等级锁）
- 发帖：须绑定手机号（本账号已绑）；新人期主贴不能加图
- 禁止：荐股、必涨、产品发布腔、旧个人域名

## Identity fields

| 字段 | 本站叫什么 | 用身份包哪一档 | 备注 |
|---|---|---|---|
| 显示名 | 用户名 / 昵称 | — | **保留 `weilaihui`** |
| 简介 | 介绍（签名） | **中版** | **Blocker：需活跃用户以上** |
| 网站 / 主页 | 无独立字段 | — | 只能塞进签名 |
| 头像 | 头像设置 | `avatar-400.png` | **Blocker：需活跃用户以上** |

## Copy source

`内容/品牌/身份统一包.md` → **中版**。

## Posting

- 入口：https://www.jisilu.cn/publish/（社区知识库「发起」）
- 草稿：`内容/草稿/第001期-集思录.md`
- Day1 / EP-001：https://www.jisilu.cn/question/524510（分类选「其他」）
- 语气：问题 framing + 公开实验；对齐雪球版直接提问，避免营销感
- 多段正文：`#advanced_editor` textarea + evaluate 写 value；标题 `#question_contents`
- 发完立刻记公开 URL → `增长.md` / 当日 `每日/`
- 正文软链：`github.com/grlib` + `github.com/grlib/alphaforge`
- 备注：发布后曾出现「系统维护中：该文章暂时无法回复」

## WebBridge ops

1. 遵守 `.cursor/rules/kimi-webbridge.mdc`
2. session 例：`alphaforge-jisilu-onboard` / `alphaforge-jisilu-post`
3. 先确认能打开 jisilu.cn 且已登录；未登录 / 验证码 → 交 Founder
4. **不点「更改昵称」**，除非 Founder 已确认接受金币与降权
5. **结束 `close_session`**

## Known pitfalls

- **普通用户不能设签名 / 上传头像**（需「活跃用户」以上）——2026-08-18 已验证
- 无 Website 字段；链接只能写进签名
- 改昵称：30 天一次、18 金币、降权新人；当前金币 0 时也无法改
- 未绑手机不能发言（本账号已绑）
- 新人期：主贴无图、条数受限；会员数据权益 **不能** 解除社区新人限制
- 社区厌恶营销贴 / 灌水贴；EP 必须像真实问题，不像产品发布
- 新发帖可能提示「系统维护中：该文章暂时无法回复」（2026-08-18 EP-001）
- 多标签易卡；同任务少开 tab

## Reply / DM

**Status: Not implemented**

预留：回复主题评论、私信筛选有方法的投资者、拒绝荐股请求。  
实现门槛：有真实留言/私信后再开。

## Evidence

- `增长.md`；身份包落地记录
- 开通决策：D-009
- 2026-08-18：登录 `weilaihui`；昵称保留；简介/头像因普通用户等级 **未同步**
- 2026-08-18：EP-001 已发 https://www.jisilu.cn/question/524510
