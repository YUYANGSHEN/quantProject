"""
简单移动平均策略
"""
import numpy as np
from strategy.base import Strategy


class SMAStrategy(Strategy):
    def __init__(self, short_window=10, long_window=30):
        super().__init__()
        self.short_window = short_window
        self.long_window = long_window
        self.prices = []
    
    def on_bar(self, bar):
        self.prices.append(bar['close'])
        
        if len(self.prices) < self.long_window:
            return 'HOLD'
        
        short_ma = np.mean(self.prices[-self.short_window:])
        long_ma = np.mean(self.prices[-self.long_window:])
        
        if short_ma > long_ma and len(self.positions) == 0:
            return 'BUY'
        elif short_ma < long_ma and len(self.positions) > 0:
            return 'SELL'
        return 'HOLD'
