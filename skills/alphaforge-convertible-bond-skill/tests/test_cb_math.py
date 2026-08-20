import unittest
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from cb_math import conversion_value, conversion_premium, gross_redemption_upside, percentile_rank
from scenario import stock_move_mechanical_scenario

class TestCBMath(unittest.TestCase):
    def test_conversion_value(self):
        self.assertAlmostEqual(conversion_value(12, 10), 120)

    def test_premium(self):
        self.assertAlmostEqual(conversion_premium(130, 100), 0.30)

    def test_redemption_upside(self):
        self.assertAlmostEqual(gross_redemption_upside(100, 110), 0.10)

    def test_percentile_rank(self):
        self.assertAlmostEqual(percentile_rank([1,2,3,4], 3), 0.75)

    def test_scenario(self):
        s = {"bond_price": 120, "stock_price": 10, "conversion_price": 10, "face_value": 100}
        result = stock_move_mechanical_scenario(s, -0.10)
        self.assertAlmostEqual(result["new_stock_price"], 9.0)

if __name__ == "__main__":
    unittest.main()
