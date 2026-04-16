import requests as req

class Extract:
    def __init__(self, url):
        self.url = url
    
    def extract_crypto(url):
        response = req.get(url)
        response.raise_for_status()

        data = response.json()
        return data
    
prices = Extract("https://api.binance.com/api/v3/ticker/price")
trades = Extract("https://api.binance.com/api/v3/trades?symbol=BTCUSDT&limit=5")
order_book = Extract("https://api.binance.com/api/v3/depth?symbol=BTCUSDT&limit=5")
klines = Extract("https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h&limit=5")
    

print(prices.extract_crypto())
print(trades.extract_crypto())
print(order_book.extract_crypto())
print(klines.extract_crypto())