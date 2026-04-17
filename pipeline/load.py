from sqlalchemy import create_engine
from transform import coin_prices, recent_trades, recent_klines, latest_orders
from config import DB_CONFIG


user = DB_CONFIG["DB_USER"]
dbname = DB_CONFIG["DB_NAME"]
passwd = DB_CONFIG["DB_PASSWORD"]
port = DB_CONFIG["DB_PORT"]
host = DB_CONFIG["DB_HOST"]


engine = create_engine(f"postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{dbname}?sslmode=require")

class LoadData:
    def __init__(self, coin_prices, recent_trades, recent_klines, latest_orders):
        self.coin_prices = coin_prices
        self.recent_trades = recent_trades
        self.recent_klines = recent_klines
        self.latest_orders = latest_orders

    def load_market_coins(self):
        if self.coin_prices.empty:
            print("No coin prices")
            return 
        self.coin_prices.to_sql(name="prices", con=engine, if_exists="replace", index=False)

        print(f"Loaded {len(self.coin_prices)} records")
    def load_market_trades(self):
        if self.recent_trades.empty:
            print("Recent trades do not exist")
            return
        self.recent_trades.to_sql(name="recent_trades", con=engine, if_exists="append", index=False)

        print(f"Loaded {len(self.recent_trades)} records")


    def load_market_klines(self):
        if self.recent_klines.empty:
            print("Recent trades do not exist")
            return
        self.recent_klines.to_sql(name="recent_trades", con=engine, if_exists="append", index=False)

        print(f"Loaded {len(self.recent_klines)} records")

    def load_orders(self):
        if self.latest_orders.empty:
            print("Recent trades do not exist")
            return
        self.latest_orders.to_sql(name="latest_orders", con=engine, if_exists="append", index=False)

        print(f"Loaded {len(self.latest_orders)} records")


    
