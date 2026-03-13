from abc import ABC, abstractmethod
import pandas as pd


class Strategy(ABC):
    """策略基类"""
    
    def __init__(self, name: str):
        self.name = name
        self.data = None
        self.broker = None
        
    def init(self, data: pd.DataFrame, broker):
        """初始化策略"""
        self.data = data
        self.broker = broker
        
    @abstractmethod
    def on_bar(self, date, bar):
        """每个bar的回调"""
        pass
