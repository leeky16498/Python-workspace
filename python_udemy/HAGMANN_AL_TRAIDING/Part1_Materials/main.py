from binance.client import Client
from binance import ThreadedWebsocketManager
import pandas as pd

my_api = "OkNTS53iVnQwQ4SvVn9rScwpqGbuX37uzAboebgssjVC53ZPBBOIycYE7tWcgKoA"
my_secret = "lIStreQbr4ob7I6x5A7DpOJHIRmb5shNDIve79H56A7kAfhcDoe1qLapUnHF4wt1"

client = Client(api_key=my_api, api_secret=my_secret, tld="com", testnet=True)

twm = ThreadedWebsocketManager(api_key=my_api, api_secret=my_secret)
twm.start()


def simple_bot(msg):
    ''' define how to process incoming WebSocket messages '''

    time = pd.to_datetime(msg["E"], unit="ms")
    price = float(msg["c"])

    print("Time: {} | Price: {}".format(time, price))

    if int(price) % 10 == 0:
        order = client.create_order(symbol="BTCUSDT", side="BUY", type="MARKET", quantity=0.1)
        print("\n" + 50 * "-")
        print("Buy {} BTC for {} USDT".format(order["executedQty"], order["cummulativeQuoteQty"]))
        print(50 * "-" + "\n")

        twm.stop()

twm.start_symbol_ticker_socket(callback=simple_bot, symbol="BTCUSDT")