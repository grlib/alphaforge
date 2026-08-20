# Data Contract

Skill 不依赖特定数据源。

Provider 最终输出统一 `ConvertibleBondSnapshot`。

## Minimum Required

```json
{
  "bond_code": "123456",
  "bond_name": "示例转债",
  "bond_price": 125.0,
  "stock_price": 12.0,
  "conversion_price": 10.0
}
```

推荐补充：

```text
snapshot_time
stock_code
stock_name
face_value
redemption_price
ytm
remaining_years
remaining_size
rating
redemption_status
revision_status
put_status
maturity_status
```

历史数据建议提供：
- premium history
- price history
- YTM history
- conversion value history

截面数据建议提供：
- price
- conversion value
- premium
- ytm
- remaining years
- remaining size
- rating
- event status

推荐架构：

```text
Provider
↓
Adapter
↓
Canonical Snapshot
↓
Skill
```

不要把网页 HTML Parser 和核心 Skill 逻辑绑死。
