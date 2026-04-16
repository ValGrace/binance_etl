import pandas as pd
from decimal import Decimal

class Transform:
    def __init__(self, prices, trades, order_book):
        self.prices = prices
        self.trades = trades
        self.order_book = order_book

    def transform_prices(self):
        _df = pd.DataFrame(self.prices)
        _df["price"] = _df["price"].apply(Decimal)
        return _df
    
    def transform_trades(self):
        trades_df = pd.DataFrame(self.trades)
        trades_df["price"] = trades_df["price"].apply(Decimal)
        trades_df["qty"] = trades_df["qty"].apply(Decimal)
        trades_df["quoteQty"] = trades_df["quoteQty"].apply(Decimal)
        trades_df["time"] = pd.to_datetime(trades_df["time"], unit='ms')
        return trades_df
    

    def transform_order_book(self):
        bids = self.order_book.get("bids", [])
        asks = self.order_book.get("asks", [])
        data = [bid + ask for bid, ask in zip(bids, asks)]
        orders_df = pd.DataFrame(data, columns=["bid_price", "bid_quantity", "ask_price", "ask_quantity"])
        return orders_df
    
    
    def transform_klines(self):
        pass
