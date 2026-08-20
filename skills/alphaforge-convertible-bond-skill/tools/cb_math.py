from __future__ import annotations

DEFAULT_FACE_VALUE = 100.0

def conversion_value(stock_price: float, conversion_price: float, face_value: float = DEFAULT_FACE_VALUE) -> float:
    if stock_price <= 0 or conversion_price <= 0 or face_value <= 0:
        raise ValueError("prices and face_value must be > 0")
    return stock_price / conversion_price * face_value

def conversion_premium(bond_price: float, conv_value: float) -> float:
    if bond_price <= 0 or conv_value <= 0:
        raise ValueError("bond_price and conv_value must be > 0")
    return bond_price / conv_value - 1.0

def gross_redemption_upside(bond_price: float, redemption_price: float) -> float:
    if bond_price <= 0 or redemption_price <= 0:
        raise ValueError("prices must be > 0")
    return redemption_price / bond_price - 1.0

def percent_change(current: float, previous: float) -> float:
    if previous == 0:
        raise ValueError("previous cannot be 0")
    return current / previous - 1.0

def percentile_rank(values, x: float) -> float:
    vals = [v for v in values if v is not None]
    if not vals:
        raise ValueError("values cannot be empty")
    return sum(1 for v in vals if v <= x) / len(vals)

def snapshot_metrics(snapshot: dict) -> dict:
    face = float(snapshot.get("face_value", DEFAULT_FACE_VALUE))
    cv = conversion_value(float(snapshot["stock_price"]), float(snapshot["conversion_price"]), face)
    premium = conversion_premium(float(snapshot["bond_price"]), cv)
    result = {
        "conversion_value": round(cv, 4),
        "conversion_premium": round(premium, 6),
    }
    if snapshot.get("redemption_price"):
        result["gross_redemption_upside"] = round(
            gross_redemption_upside(float(snapshot["bond_price"]), float(snapshot["redemption_price"])), 6
        )
    return result
