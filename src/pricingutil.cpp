#include "pricingutil.h"

PricingUtil::PricingUtil() {};

float PricingUtil::calcVal(float previousPrice, float interest, float oleoConstant) {
    float output = (previousPrice * (0.9 + interest)) * oleoConstant;
    this->val = output;
    return output;
}

float PricingUtil::getVal() {
    return this->val;
}
