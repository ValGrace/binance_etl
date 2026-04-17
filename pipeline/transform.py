import pandas as pd
from decimal import Decimal
from extract import prices, trades, order_book, klines

class Transform:
    def __init__(self, prices, trades, order_book, klines):
        self.prices = prices
        self.trades = trades
        self.order_book = order_book
        self.klines = klines

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
        columns = ["open_time", "open_price", "high_price", "low_price", "close_price", "volume", "close_time", "quote_asset_volume", "no_of_trades", "base_asset_volume", "quote_asset_volume", "ignore"]
        klines_df = pd.DataFrame(self.klines, columns=columns)
        return klines_df

transformed = Transform(prices, trades, order_book, klines)
coin_prices = transformed.transform_prices()
recent_trades = transformed.transform_trades()
latest_orders = transformed.transform_trades()
recent_klines = transformed.transform_trades()

print(coin_prices)
