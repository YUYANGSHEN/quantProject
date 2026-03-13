"""
Binance 交易接口
"""
from binance.client import Client
from binance.exceptions import BinanceAPIException
import time


class BinanceTrader:
    def __init__(self, api_key, api_secret, testnet=False):
        self.client = Client(api_key, api_secret, testnet=testnet)
    
    def get_balance(self, asset='USDT'):
        """获取余额"""
        balance = self.client.get_asset_balance(asset=asset)
        return float(balance['free'])
    
    def place_order(self, symbol, side, quantity, order_type='MARKET', price=None):
        """下单"""
        try:
            if order_type == 'MARKET':
                order = self.client.create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity
                )
            else:
                order = self.client.create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    timeInForce='GTC',
                    quantity=quantity,
                    price=price
                )
            return order
        except BinanceAPIException as e:
            print(f"下单失败: {e}")
            return None
    
    def get_price(self, symbol):
        """获取当前价格"""
        ticker = self.client.get_symbol_ticker(symbol=symbol)
        return float(ticker['price'])
