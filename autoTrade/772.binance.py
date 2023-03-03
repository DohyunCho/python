# pip install python-binance
import time
import binance
from binance.client import Client
import datetime

api_key="my_key"
api_secret="my_secret"

def get_target_price(ticker, k):
    """Search the buy target with the volatility breakout strategy"""
    client = Client(api_key, api_secret)
    klines = client.futures_coin_get_klines(symbol=ticker, interval=Client.KLINE_INTERVAL_1HOUR, limit=2)
    current_price = float(klines[-1][4])
    high_price = float(klines[-1][2])
    low_price = float(klines[-1][3])
    target_price = current_price + (high_price - low_price) * k
    return target_price

def get_start_time(ticker):
    """Query start time"""
    client = Client(api_key, api_secret)
    klines = client.futures_coin_get_klines(symbol=ticker, interval=Client.KLINE_INTERVAL_1HOUR, limit=1)
    start_time = klines[0][0] / 1000
    return start_time

def get_balance(ticker):
    """Check your balance"""
    client = Client(api_key, api_secret)
    account_balance = client.futures_coin_account_balance()
    for b in account_balance:
        if b["asset"] == ticker:
            if float(b["balance"]) is not None:
                return float(b["balance"])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """Search the current price"""
    client = Client(api_key, api_secret)
    ticker_price = client.futures_coin_orderbook_ticker(symbol=ticker)
    return float(ticker_price["askPrice"])

# log in
client = Client(api_key, api_secret)
print("autotrade start")

# Start automatic trading
start_time = get_start_time("BTCUSDT")
while True:
    try:
        now = datetime.datetime.now().timestamp()
        end_time = start_time + 60*60

        if start_time < now < end_time - 10:
            target_price = get_target_price("BTCUSDT", 0.1)
            current_price = get_current_price("BTCUSDT")
            if target_price < current_price:
                usdt = get_balance("USDT")
                if usdt > 5000:
                    # Place a market buy order with 20x leverage
                    client.futures_coin_create_order(
                        symbol='BTCUSDT',
                        side='BUY',
                        type='MARKET',
                        quantity=(usdt*0.9995)/current_price*10,
                        positionSide='BOTH')
        else:
            start_time = get_start_time("BTCUSDT")
            btc = get_balance("BTC")
            if btc > 0.00008:
                # Place a market sell order
                client.futures_coin_create_order(
                    symbol='BTCUSDT',
                    side='SELL',
                    type='MARKET',
                    quantity=btc*0.9995,
                    positionSide='BOTH')
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)
