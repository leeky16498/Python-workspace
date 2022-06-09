from binance.client import Client
import websocket, json
import pandas as pd
import numpy as np
import datetime as dt

API_KEY = "XXfsr9leN7Wnel86MMBhFieVHe35zDQUOI4HeIl0FJD62OmRIccO09WzWNcVUJfx"
SECRET_KEY = "MNZEwgFn2f5SNOY0ciDG6nNsrDIB4zGGxD0cTLesXs4KjZRGzwZ3P1Sy8NYzzw3j"

client = Client(api_key=API_KEY, api_secret=SECRET_KEY, tld="com")
data = client.get_account()
print(data)

now = dt.datetime.utcnow()
past = str(now - dt.timedelta(days=2))
print(now, past)

bars = client.get_historical_klines(symbol="BTCUSDT", interval="1h",
                                    start_str=past, end_str=None, limit=1000)
print(bars)