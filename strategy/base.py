"""
策略基类
"""
from abc import ABC, abstractmethod


class Strategy(ABC):
    def __init__(self):
        self.positions = {}
    
    @abstractmethod
    def on_bar(self, bar):
        """每根K线触发，返回信号: 'BUY', 'SELL', 'HOLD'"""
        pass
