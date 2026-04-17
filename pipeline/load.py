from sqlalchemy import create_engine
from transform import coin_prices, recent_trades, recent_klines, latest_orders
from config import DB_CONFIG


user = DB_CONFIG["DB_USER"]
dbname = DB_CONFIG["DB_NAME"]
passwd = DB_CONFIG["DB_PASSWORD"]
port = DB_CONFIG["DB_PORT"]
host = DB_CONFIG["DB_HOST"]


engine = create_engine(f"postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{dbname}?sslmode=require")

def load_market_data():
    if coin_prices.empty:
        print("No coin prices")
        return 
    coin_prices.to_sql(name="prices", con=engine, if_exists="replace", index=False)

    print(f"Loaded {len(coin_prices)} records")

load_market_data()
    
