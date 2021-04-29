import json
import os
from decimal import Decimal

from binance import client
from dotenv import load_dotenv

load_dotenv()

bin_client = client.Client(
    api_key=os.getenv("API_KEY"), api_secret=os.getenv("SECRET_KEY")
)
tickers = bin_client.get_all_tickers()
tickers = [ticker for ticker in tickers if ticker["symbol"].endswith("USDT")]
tickers = sorted(tickers, key=lambda value: Decimal(value["price"]), reverse=True)

print(json.dumps(tickers))
