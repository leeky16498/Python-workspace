from binance.client import Client
from binance import ThreadedWebsocketManager

api_key = "AWquD2VX7mC8IuB2ufoRYL2CNSNChVXnOEvGqpz657p37uIbYWMOJUzlTeQybtSA"
secret_key = "MBMdnjdNK6QYKRxer3B6iqHd4NCClEgnTYvG1SgUfKLmaNe9qdeG5fVjETVdHENQ"

client = Client(api_key=api_key, api_secret=secret_key, tld = "com", testnet=True)

sol = client.get_account()
print(sol)

twm = ThreadedWebsocketManager()
twm.start()

def simple_bot(msg):
    print(msg)

twm.start_symbol_ticker_socket(callback=simple_bot, symbol="BTCUSDT")
