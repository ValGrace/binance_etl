import requests as req

class Extract:
    def __init__(self):
        self.res = []
    
    def extract_crypto(self, url):
        self.res = req.get(url)
        self.res.raise_for_status()

        data = self.res.json()
        return data
    
crypto_data = Extract()
# trades = Extract()
# order_book = Extract()
# klines = Extract()
    

prices = crypto_data.extract_crypto("https://api.binance.com/api/v3/ticker/price")
trades = crypto_data.extract_crypto("https://api.binance.com/api/v3/trades?symbol=BTCUSDT&limit=40&interval=1h")
order_book = crypto_data.extract_crypto("https://api.binance.com/api/v3/depth?symbol=BTCUSDT&limit=40&interval=1h")
klines = crypto_data.extract_crypto("https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h&limit=60")