import argparse
import json
import os
from decimal import Decimal

from binance import client
from dotenv import load_dotenv

load_dotenv()


def get_tickers():
    bin_client = client.Client(
        api_key=os.getenv("API_KEY"), api_secret=os.getenv("SECRET_KEY")
    )
    tickers = bin_client.get_all_tickers()
    tickers = [ticker for ticker in tickers if ticker["symbol"].endswith("USDT")]
    return sorted(tickers, key=lambda value: Decimal(value["price"]), reverse=True)


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--top", dest="top", type=int, default=0)
args = arg_parser.parse_args()
if args.top == 0:
    print(json.dumps(get_tickers()))
else:
    print(json.dumps(get_tickers()[: args.top]))
