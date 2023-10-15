//
// Created by Ethan on 9/13/2023.
//

#include "hackathonbot.h"
#include <iostream>

// # Part 2: Company Hackathon

// ## Scenario
// It is now November, so it is time for the company hackathon! Unfortunately, most of your coworkers are focusing on getting their bonuses higher for the holidays, so there is not much competition.
// In order to qualify for the contest prize, which remains a surprise until the end, you must beat a baseline trading strategy with your strategy.
// Fortunately, your friend that is a QR was happy to give you some simple rules to build a strategy. You will need to build a strategy around those rules, pass all of the provided test cases,
// win the competition, and submit proof that you won in your PR. Good Luck!

// ## Ruleset
// - You can only have 1 stock at a time, and cannot short a stock (can't sell without having an explicit stock)
// - Assume the initial stock cost was 100
// - If the stock goes up in price for 52 windows, sell
// - If the stock goes down in price for 47 windows, sell
// - If the stock drops by over 62% from the purchase price bought, sell
// - If the stock raises by over 89% from the purchase price bought, sell
// - If (after buying) the stock raises by >= 20%, drops by <= 15%, raises again by >= 30% and the percent change in the 3 series window is up by >= 50% sell
// - If (after buying) the stock drops by <= 15%, raises by >= 15%, drops again by >= 25% and the percent change OVERALL is down by >= 45% sell
// - If stock stays +-5% for 10 cycles (after buying), sell
// - If the stock price is less than 52, buy
// - If the stock drops in price for 5 windows (after selling), buy

HackathonBot::HackathonBot() {};


void HackathonBot::takeAction(float price){

    // Check for up/down days
    if (!this->pricesHistory.empty()) {
        if (price > this->pricesHistory.back()) {
            this->priceUpDays++;
            this->priceDownDays = 0;
        } else if (price < this->pricesHistory.back()) {
            this->priceDownDays++;
            this->priceUpDays = 0;
        }
    }

    // add to prices history
    this->pricesHistory.push_back(price);

    if (this->holding) { // Sell
        if (priceUpDays >= 52 || priceDownDays >= 47) {
            this->sell();
            return;
        }

        const float priceBought = this->pricesHistory.front();
        if (price / priceBought > 1.89 || price / priceBought < 0.38) {
            this->sell();
            return;
        }

        // Series Window

        if (this->pricesHistory.size() > 3) {
            const int n = this->pricesHistory.size();

            const float firstSecond = this->pricesHistory[n-1] / this->pricesHistory[n-2];
            const float secondThird = this->pricesHistory[n-2] / this->pricesHistory[n-3];
            const float thirdFourth = this->pricesHistory[n-3] / this->pricesHistory[n-4];
            const float firstFourth = this->pricesHistory[n-1] / this->pricesHistory[n-4];

            if (thirdFourth >= 1.2 && secondThird <= 0.85 && firstSecond >= 1.3 && firstFourth >= 1.5) {
                this->sell();
                return;
            }

            if (thirdFourth <= 0.85 && secondThird >= 1.15 && firstSecond <= 0.75 && firstFourth <= 0.55) {
                this->sell();
                return;
            }

            if (this->pricesHistory.size() >= 10) {
                float priceBought = this->pricesHistory.front();
                for (const float &price : this->pricesHistory) {
                    float priceRatio = price / priceBought;
                    if (std::abs(priceRatio - 1) > 0.05) {
                        return;
                    }
                }
            }
            this->sell();

        }


    }

    else {
        if (price < 52 || this->priceDownDays >= 5) {
            this->buy();
        }
    }

}

double HackathonBot::getBalance(){
    return this->balance;
}

bool HackathonBot::isHolding(){
    return this->holding;
}

void HackathonBot::buy(){
    this->holding = true;
}

void HackathonBot::sell(){
    this->holding = false;
    this->pricesHistory.clear();
}
