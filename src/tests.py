import interface
import unittest

class InterfaceTests(unittest.TestCase):
    def setUp(self):
        self.exchange = interface.Exchange(1000)  # Initial balance of 1000 for every trader

    def test_initial_balance(self):
        self.assertEqual(self.exchange.get_trader_balance("Alice"), 1000)

    def test_add_valid_trade(self):
        trade = interface.Trade("Alice", 100, 10, "BUY")
        self.exchange.add_trade(trade)
        self.assertEqual(len(self.exchange.buy_orders), 1)

    def test_match_trade(self):
        buy_trade = interface.Trade("Alice", 100, 10, "BUY")
        sell_trade = interface.Trade("Bob", 100, 10, "SELL")
        self.exchange.add_trade(buy_trade)
        self.exchange.add_trade(sell_trade)
        self.assertEqual(len(self.exchange.buy_orders), 0)
        self.assertEqual(len(self.exchange.sell_orders), 0)
        self.assertEqual(self.exchange.get_trader_balance("Alice"), 0)  # 1000 - 100*10
        self.assertEqual(self.exchange.get_trader_balance("Bob"), 2000)  # 1000 + 100*10


    def test_insufficient_balance(self):
        with self.assertRaises(ValueError) as context:
            trade = interface.Trade("Alice", 200, 10, "BUY")
            self.exchange.add_trade(trade)
        self.assertEqual(str(context.exception), "Trader Alice has insufficient balance for this trade.")

    def test_invalid_trade_position(self):
        with self.assertRaises(ValueError) as context:
            trade = interface.Trade("Alice", 100, 10, "HOLD")
            self.exchange.add_trade(trade)
        self.assertEqual(str(context.exception), "Trade position must be either BUY or SELL.")

    def test_negative_trade_amount(self):
        with self.assertRaises(ValueError) as context:
            trade = interface.Trade("Alice", -100, 10, "BUY")
            self.exchange.add_trade(trade)
        self.assertEqual(str(context.exception), "Amount and price should be positive.")

if __name__ == "__main__":
    unittest.main()
