"""
数据获取模块 - Binance API
"""
from binance.client import Client
import pandas as pd


class BinanceData:
    def __init__(self, api_key=None, api_secret=None):
        self.client = Client(api_key, api_secret) if api_key else Client()
    
    def get_klines(self, symbol, interval, start_str, end_str=None):
        """获取K线数据"""
        klines = self.client.get_historical_klines(symbol, interval, start_str, end_str)
        
        df = pd.DataFrame(klines, columns=[
            'timestamp', 'open', 'high', 'low', 'close', 'volume',
            'close_time', 'quote_volume', 'trades', 
            'taker_buy_base', 'taker_buy_quote', 'ignore'
        ])
        
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        for col in ['open', 'high', 'low', 'close', 'volume']:
            df[col] = df[col].astype(float)
        
        return df[['timestamp', 'open', 'high', 'low', 'close', 'volume']]
