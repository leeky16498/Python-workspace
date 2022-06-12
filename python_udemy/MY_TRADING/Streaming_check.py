from binance.client import Client
from binance import ThreadedWebsocketManager
import pandas as pd
import numpy as np

api_key = "aQjoZfgE51Tz3vNv3vjAj0SccJEvxZGR1DFSQviVTrh50ENS4C4kaGOGT9Q2vE30"
secret_key = "3VverBNcAfdCrcyFZHt3IHHnQDtToZee7tvyaFQkyjd631Wnb7IuCjjeS0IjAKuu"

client = Client(api_key = api_key, api_secret = secret_key, tld = "com")

client.get_account()

twm = ThreadedWebsocketManager()
twm.start()

def simple_bot(msg):
    ''' define how to process incoming WebSocket messages '''
    
    time = pd.to_datetime(msg["E"], unit = "ms")
    price = float(msg["c"])
    
    print("Time: {} | Price: {}".format(time, price))
    
    if int(price) % 10 == 0:
        order = client.create_order(symbol = "BTCUSDT", side = "BUY", type = "MARKET", quantity = 0.1)
        print("\n" + 50 * "-")
        print("Buy {} BTC for {} USDT".format(order["executedQty"], order["cummulativeQuoteQty"]))
        print(50 * "-" + "\n")
        
        twm.stop()
        
twm.start_symbol_miniticker_socket(callback = simple_bot, symbol = "BTCUSDT")

