#include <gtest/gtest.h>
#include "pricingutil.h"

TEST(sampleTest, sample) {
    EXPECT_EQ(4, 4);
}

TEST(PricingUtilTest, TestFormula) {
    PricingUtil pricingUtil = PricingUtil();

    float previousPrice = 100;
    float interest = 0.1;
    float oleoConstant = 0.5;

    float expected = (previousPrice * (0.9 + interest)) * oleoConstant;
    float actual = pricingUtil.calcVal(previousPrice, interest, oleoConstant);

    EXPECT_EQ(expected, actual);

    // Test that value is stored in the class
    EXPECT_NEAR(pricingUtil.getVal(), actual, 1e-4);
    EXPECT_NEAR(pricingUtil.calcVal(40, 0.1, 3), 120, 1e-4);
    EXPECT_NEAR(pricingUtil.getVal(), 120, 1e-4);
    EXPECT_NEAR(pricingUtil.calcVal(60, 0.35, 2), 150, 1e-4);
    EXPECT_NEAR(pricingUtil.getVal(), 150, 1e-4);

}



