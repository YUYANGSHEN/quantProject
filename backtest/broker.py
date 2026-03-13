from typing import Dict, List
from datetime import datetime


class Broker:
    """模拟交易经纪人"""
    
    def __init__(self, initial_cash: float = 100000.0, commission: float = 0.0003):
        self.initial_cash = initial_cash
        self.cash = initial_cash
        self.commission = commission
        self.positions: Dict[str, int] = {}
        self.trades: List[Dict] = []
        
    def buy(self, symbol: str, price: float, size: int, date: datetime):
        """买入"""
        cost = price * size * (1 + self.commission)
        if cost > self.cash:
            return False
        
        self.cash -= cost
        self.positions[symbol] = self.positions.get(symbol, 0) + size
        self.trades.append({
            'date': date, 'symbol': symbol, 'action': 'BUY',
            'price': price, 'size': size, 'commission': price * size * self.commission
        })
        return True
    
    def sell(self, symbol: str, price: float, size: int, date: datetime):
        """卖出"""
        if self.positions.get(symbol, 0) < size:
            return False
        
        revenue = price * size * (1 - self.commission)
        self.cash += revenue
        self.positions[symbol] -= size
        self.trades.append({
            'date': date, 'symbol': symbol, 'action': 'SELL',
            'price': price, 'size': size, 'commission': price * size * self.commission
        })
        return True
    
    def get_position(self, symbol: str) -> int:
        """获取持仓"""
        return self.positions.get(symbol, 0)
    
    def get_portfolio_value(self, current_prices: Dict[str, float]) -> float:
        """计算总资产"""
        position_value = sum(self.positions.get(s, 0) * current_prices.get(s, 0) 
                            for s in self.positions)
        return self.cash + position_value
