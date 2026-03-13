import pandas as pd
from .broker import Broker
from .strategy import Strategy
from .analyzer import PerformanceAnalyzer


class BacktestEngine:
    """回测引擎"""
    
    def __init__(self, strategy: Strategy, data: pd.DataFrame, 
                 initial_cash: float = 100000.0, commission: float = 0.0003):
        self.strategy = strategy
        self.data = data
        self.broker = Broker(initial_cash, commission)
        self.equity_curve = []
        
    def run(self):
        """运行回测"""
        self.strategy.init(self.data, self.broker)
        
        for date, bar in self.data.iterrows():
            self.strategy.on_bar(date, bar)
            portfolio_value = self.broker.get_portfolio_value({'symbol': bar['close']})
            self.equity_curve.append({'date': date, 'value': portfolio_value})
        
        return self._generate_report()
    
    def _generate_report(self):
        """生成回测报告"""
        equity_df = pd.DataFrame(self.equity_curve).set_index('date')
        trades_df = pd.DataFrame(self.broker.trades)
        
        metrics = PerformanceAnalyzer.analyze(
            equity_df, trades_df, self.broker.initial_cash
        )
        
        return {
            **metrics,
            'final_value': equity_df['value'].iloc[-1],
            'equity_curve': equity_df,
            'trades': trades_df
        }
