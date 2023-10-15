import cppimport.import_hook
import PricingUtil
import unittest

class TestPricingUtil(unittest.TestCase):
    def runTests(self):
        util = PricingUtil.PricingUtil()
        self.assertAlmostEqual(util.calcVal(3, 0.1, 3), 9, 3, "incorrect value")
        self.assertAlmostEqual(util.getVal(), 9, 3, "incorrect value")
        self.assertAlmostEqual(util.calcVal(45, 0.3, 4), 216, 3, "incorrect value")
        self.assertAlmostEqual(util.getVal(), 216, 3, "incorrect value")


if __name__ == "__main__":
    unittest.main()
