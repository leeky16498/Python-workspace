from binance.client import Client
import websocket, json
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

##바이낸스 API
# api_key = "aQjoZfgE51Tz3vNv3vjAj0SccJEvxZGR1DFSQviVTrh50ENS4C4kaGOGT9Q2vE30"
# secret_key = "3VverBNcAfdCrcyFZHt3IHHnQDtToZee7tvyaFQkyjd631Wnb7IuCjjeS0IjAKuu"

##테스트넷 API
api_key = "AWquD2VX7mC8IuB2ufoRYL2CNSNChVXnOEvGqpz657p37uIbYWMOJUzlTeQybtSA"
secret_key = "MBMdnjdNK6QYKRxer3B6iqHd4NCClEgnTYvG1SgUfKLmaNe9qdeG5fVjETVdHENQ"

class Long_only_trader:
    def __init__(self, symbol, bar_length, return_thresh, volume_thresh, units, position=0):
        self.symbol = symbol
        self.bar_length = bar_length
        self.available_intervals = ["1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "12h", "1d", "3d",
                                    "1w", "1M"]
        self.units = units
        self.position = position
        self.trades = 0
        self.trade_values = []
        # *****************add strategy-specific attributes here******************
        self.return_thresh = return_thresh
        self.volume_thresh = volume_thresh
        # ************************************************************************

    def get_most_recent(self, symbol, interval, days):
        now = datetime.utcnow()
        past = str(now - timedelta(days=days))

        bars = client.get_historical_klines(symbol=symbol, interval=interval,
                                            start_str=past, end_str=None, limit=1000)
        df = pd.DataFrame(bars)
        df["Date"] = pd.to_datetime(df.iloc[:, 0], unit="ms")
        df.columns = ["Open Time", "Open", "High", "Low", "Close", "Volume",
                      "Clos Time", "Quote Asset Volume", "Number of Trades",
                      "Taker Buy Base Asset Volume", "Taker Buy Quote Asset Volume", "Ignore", "Date"]
        df = df[["Date", "Open", "High", "Low", "Close", "Volume"]].copy()
        df.set_index("Date", inplace=True)
        for column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")
        df["Complete"] = [True for row in range(len(df) - 1)] + [False]

        self.data = df

    def start_trading(self, historical_days, symbol="btcusdt", intervals="1m"):
        cc = symbol
        interval = intervals
        socket = f"wss://stream.binance.com:9443/ws/{cc}@kline_{interval}"

        def on_error(ws, error):
            print(error)

        def on_close(ws):
            print("closed")

        def on_message(ws, message):
            self.get_most_recent(symbol=self.symbol, interval=self.bar_length, days=historical_days)
            msg = json.loads(message)
            self.stream_candles(msg)
    
        self.ws = websocket.WebSocketApp(socket, on_message=on_message, on_error=on_error, on_close=on_close)

        if self.bar_length in self.available_intervals:
            self.ws.run_forever()

    def stream_candles(self, msg):
        event_time = pd.to_datetime(msg["E"], unit = "ms")
        start_time = pd.to_datetime(msg["k"]["t"], unit = "ms")
        first   = float(msg["k"]["o"])
        high    = float(msg["k"]["h"])
        low     = float(msg["k"]["l"])
        close   = float(msg["k"]["c"])
        volume  = float(msg["k"]["v"])
        complete=       msg["k"]["x"]
        
        if self.trades >= 5:
            self.ws.close()
            print("거래 횟수 5회를 달성하여 프로그램을 종료합니다.")

        print(".", end="", flush=True)
        # 이상이 있는 경우만 출력한다.
        self.data.loc[start_time] = [first, high, low, close, volume, complete]

        if complete:
            self.define_strategy()
            self.execute_trades()

    def define_strategy(self):
        df = self.data.copy()
        # ******************** define your strategy here ************************
        df = df[["Close", "Volume"]].copy()
        
        df["returns"] = np.log(df.Close / df.Close.shift(1))
        df["vol_ch"] = np.log(df.Volume.div(df.Volume.shift(1)))
        
        df.loc[df.vol_ch > 3, "vol_ch"] = np.nan
        df.loc[df.vol_ch < -3, "vol_ch"] = np.nan
        
        cond1 = df.returns >= self.return_thresh
        cond2 = df.vol_ch.between(self.volume_thresh[0], self.volume_thresh[1])
        df["position"] = 1
        df.loc[cond1 & cond2, "position"] = 0
        # ***********************************************************************
        self.prepared_data = df.copy()
        

    def execute_trades(self):
        if self.prepared_data["position"].iloc[-1] == 1: # if position is long -> go/stay long
            if self.position == 0:
                order = client.create_order(symbol = self.symbol, side = "BUY", type = "MARKET", quantity = self.units)
                self.report_trade(order, "매수하면서 매수포지션으로 갑니다.")
            self.position = 1
        elif self.prepared_data["position"].iloc[-1] == 0: # if position is neutral -> go/stay neutral
            if self.position == 1:
                order = client.create_order(symbol = self.symbol, side = "SELL", type = "MARKET", quantity = self.units)
                self.report_trade(order, "매도하면서 중립포지션으로 갑니다.")
            self.position = 0

    def report_trade(self, order, going):
        #extract data from order object
        side = order["side"]
        time = pd.to_datetime(order["transactTime"], unit="ms")
        base_units = float(order["executedQty"])
        quote_units = float(order["cummulativeQuoteQty"])
        price = round(quote_units / base_units, 5)

        #calculating trading profits
        self.trades += 1

        if side == "BUY":
            self.trade_values.append(-quote_units)
        elif side == "SELL":
            self.trade_values.append(quote_units)
        if self.trades % 2 == 0:
            real_profit = round(np.sum(self.trade_values[-2:]), 3)
            self.cum_profits = round(np.sum(self.trade_values), 3)
        else:
            real_profit = 0
            self.cum_profits = round(np.sum(self.trade_values[:-1]), 3)
        # print trade report
        print(2 * "\n" + 100 * "-")
        print("{} | {}".format(time, going))
        print("{} | 거래 매수량(Base_Unit) = {} | Quote_Units = {} | 현재 시가 = {} ".format(time, base_units, quote_units, price))
        print("{} | 거래 수익률 = {} | 누적 거래 수익률 = {} ".format(time, real_profit, self.cum_profits))
        print(100 * "-" + "\n")

##객체 필요 변수들---
symbol = "BTCUSDT"
bar_length = "1m"
return_thresh = 0
volume_thresh = [-3, 3]
units = 0.002
position = 0

#바이낸스 직렬
# client = Client(api_key=api_key, api_secret=secret_key, tld="com")

#테스트넷 직렬
client = Client(api_key=api_key, api_secret=secret_key, tld="com", testnet=True)

client.get_account()

trader = Long_only_trader(symbol=symbol, bar_length=bar_length, return_thresh=return_thresh, volume_thresh=volume_thresh
                          , units=units, position=position)

trader.start_trading(1/24)