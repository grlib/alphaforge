from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from cb_math import snapshot_metrics
from scenario import stock_move_mechanical_scenario

sample = json.loads((ROOT / "examples" / "sample_snapshot.json").read_text(encoding="utf-8"))

print(json.dumps({
    "bond": f"{sample['bond_name']} ({sample['bond_code']})",
    "metrics": snapshot_metrics(sample),
    "scenario_stock_minus_10pct": stock_move_mechanical_scenario(sample, -0.10),
    "scenario_stock_plus_10pct": stock_move_mechanical_scenario(sample, 0.10),
}, ensure_ascii=False, indent=2))
