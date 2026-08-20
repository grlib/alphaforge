from __future__ import annotations
from copy import deepcopy
from cb_math import conversion_value, conversion_premium

def stock_move_mechanical_scenario(snapshot: dict, stock_return: float) -> dict:
    s = deepcopy(snapshot)
    old_stock = float(s["stock_price"])
    old_bond = float(s["bond_price"])
    conv_price = float(s["conversion_price"])
    face = float(s.get("face_value", 100.0))

    new_stock = old_stock * (1.0 + stock_return)
    old_cv = conversion_value(old_stock, conv_price, face)
    new_cv = conversion_value(new_stock, conv_price, face)
    old_prem = conversion_premium(old_bond, old_cv)
    new_prem = conversion_premium(old_bond, new_cv)

    return {
        "scenario_type": "mechanical",
        "stock_return": stock_return,
        "old_stock_price": round(old_stock, 4),
        "new_stock_price": round(new_stock, 4),
        "bond_price_assumed_unchanged": round(old_bond, 4),
        "old_conversion_value": round(old_cv, 4),
        "new_conversion_value": round(new_cv, 4),
        "old_conversion_premium": round(old_prem, 6),
        "new_conversion_premium": round(new_prem, 6),
        "warning": "Mechanical result only; this is not a prediction of bond market price."
    }
