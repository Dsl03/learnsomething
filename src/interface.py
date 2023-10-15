from collections import defaultdict
import heapq

class Trade:
    def __init__(self, trader, amount, price, position):
        self.trader = trader
        self.amount = amount
        self.price = price
        self.position = position

class Exchange:
    def __init__(self, initialBalance):
        self.trader_balances = defaultdict(lambda: initialBalance)
        self.buy_orders = []
        self.sell_orders = []

    def match_trade(self, trade):
        if trade.position == "BUY":
            while trade.amount > 0 and self.sell_orders and self.sell_orders[0][0] <= trade.price:
                price, amount, seller = heapq.heappop(self.sell_orders)
                executed_amount = min(amount, trade.amount)
                trade.amount -= executed_amount
                amount -= executed_amount
                self.trader_balances[seller] += executed_amount * price
                self.trader_balances[trade.trader] -= executed_amount * price
                if amount > 0:
                    heapq.heappush(self.sell_orders, (price, amount, seller))

        elif trade.position == "SELL":
            while trade.amount > 0 and self.buy_orders and -self.buy_orders[0][0] >= trade.price:
                price, amount, buyer = heapq.heappop(self.buy_orders)
                executed_amount = min(amount, trade.amount)
                trade.amount -= executed_amount
                amount -= executed_amount
                self.trader_balances[buyer] -= executed_amount * price
                self.trader_balances[trade.trader] += executed_amount * price
                if amount > 0:
                    heapq.heappush(self.buy_orders, (price, amount, buyer))

    def add_trade(self, trade):
        if trade.position not in ["BUY", "SELL"]:
            raise ValueError("Trade position must be either BUY or SELL.")
        if trade.amount <= 0 or trade.price <= 0:
            raise ValueError("Amount and price should be positive.")

        # Match the trade
        self.match_trade(trade)

        # Check trader's balance for the remaining unmatched amounts
        if trade.position == "BUY" and self.trader_balances[trade.trader] < trade.amount * trade.price:
            raise ValueError(f"Trader {trade.trader} has insufficient balance for this trade.")
        if trade.position == "SELL" and self.trader_balances[trade.trader] < trade.amount:
            raise ValueError(f"Trader {trade.trader} has insufficient assets for this trade.")

        # If there are remaining unmatched amounts, add them to the respective order book
        if trade.amount > 0:
            if trade.position == "BUY":
                heapq.heappush(self.buy_orders, (-trade.price, trade.amount, trade.trader))
            else:
                heapq.heappush(self.sell_orders, (trade.price, trade.amount, trade.trader))

    def get_trader_balance(self, trader):
        return self.trader_balances[trader]
