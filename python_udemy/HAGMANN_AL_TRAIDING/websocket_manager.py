import websocket, json
import pandas as pd

'''
m -> minutes; h -> hours; d -> days; w -> weeks; M -> months

1m
3m
5m
15m
30m
1h
2h
4h
6h
8h
12h
1d
3d
1w
1M
'''

'''
<<DATA EXAMPLE>>
  "e": "kline",     // Event type
  "E": 123456789,   // Event time
  "s": "BNBBTC",    // Symbol
  "k": {
    "t": 123400000, // Kline start time
    "T": 123460000, // Kline close time
    "s": "BNBBTC",  // Symbol
    "i": "1m",      // Interval
    "f": 100,       // First trade ID
    "L": 200,       // Last trade ID
    "o": "0.0010",  // Open price
    "c": "0.0020",  // Close price
    "h": "0.0025",  // High price
    "l": "0.0015",  // Low price
    "v": "1000",    // Base asset volume
    "n": 100,       // Number of trades
    "x": false,     // Is this kline closed?
    "q": "1.0000",  // Quote asset volume
    "V": "500",     // Taker buy base asset volume
    "Q": "0.500",   // Taker buy quote asset volume
    "B": "123456"   // Ignore
'''

cc = "btcgbp"
interval = "1m"
socket = f"wss://stream.binance.com:9443/ws/{cc}@kline_{interval}"

def on_message(ws, message):
    json_data = json.loads(message)
    candle = json_data["k"]
    is_candle_closed = candle["x"]
    
    print(json_data)
    print(candle)
    print(is_candle_closed)
    

def on_error(ws, error):
    print(error)
    
def on_close(ws):
    print("closed")

ws = websocket.WebSocketApp(socket,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close
)

ws.run_forever()