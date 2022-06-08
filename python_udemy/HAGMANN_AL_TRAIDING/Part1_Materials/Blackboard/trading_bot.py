from cgitb import text
from binance.client import Client
import websocket
import pandas as pd
import numpy as np

my_api = "eSpIC1boIZDc8yaLDIJZOMMCMUnhsPxXNefUjuq6r7PRnubuQcO3e4koe9KLYY0x"
my_secret = "mH7WXrNg2ldpFoysSundyFCZErIM9ovTDj4nfWP09GnLF9sXh68GtsqC4z7yQGLK"

client = Client(api_key=my_api, api_secret=my_secret, tld="com", testnet=True)
client.get_account()