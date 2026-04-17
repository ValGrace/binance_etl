from pipeline.extract import Extract
from pipeline.transform import Transform
from pipeline.load import LoadData

def pipeline():
    try:

        crypto_data = Extract()
        prices = crypto_data.extract_crypto("https://api.binance.com/api/v3/ticker/price")
        trades = crypto_data.extract_crypto("https://api.binance.com/api/v3/trades?symbol=BTCUSDT&limit=40")
        order_book = crypto_data.extract_crypto("https://api.binance.com/api/v3/depth?symbol=BTCUSDT&limit=40")
        klines = crypto_data.extract_crypto("https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h&limit=60")


        transformed = Transform(prices, trades, order_book, klines)
        coin_prices = transformed.transform_prices()
        recent_trades = transformed.transform_trades()
        latest_orders = transformed.transform_trades()
        recent_klines = transformed.transform_trades()

        load_data = LoadData(coin_prices, recent_trades, recent_klines, latest_orders)
        load_data.load_market_coins()
        load_data.load_market_trades()
        load_data.load_market_klines()
        load_data.load_orders()

    except Exception as e:
        print(f"pipeline failed: {e}")