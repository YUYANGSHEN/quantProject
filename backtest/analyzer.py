import pandas as pd
import numpy as np


class PerformanceAnalyzer:
    """性能分析器"""
    
    @staticmethod
    def analyze(equity_curve: pd.DataFrame, trades: pd.DataFrame, 
                initial_cash: float, risk_free_rate: float = 0.03):
        """全面分析回测结果"""
        values = equity_curve['value']
        returns = values.pct_change().dropna()
        
        # 基础指标
        total_return = (values.iloc[-1] / initial_cash - 1) * 100
        annual_return = ((values.iloc[-1] / initial_cash) ** (252 / len(values)) - 1) * 100
        
        # 风险指标
        volatility = returns.std() * np.sqrt(252) * 100
        sharpe = (returns.mean() * 252 - risk_free_rate) / (returns.std() * np.sqrt(252))
        
        # 回撤分析
        cummax = values.cummax()
        drawdown = (cummax - values) / cummax * 100
        max_drawdown = drawdown.max()
        
        # 交易分析
        if not trades.empty:
            wins = trades[trades['action'] == 'SELL'].copy()
            if len(wins) > 1:
                wins['pnl'] = wins['price'].diff() * wins['size'].shift()
                win_rate = (wins['pnl'] > 0).sum() / len(wins) * 100
            else:
                win_rate = 0
        else:
            win_rate = 0
            
        return {
            'total_return': total_return,
            'annual_return': annual_return,
            'volatility': volatility,
            'sharpe_ratio': sharpe,
            'max_drawdown': max_drawdown,
            'win_rate': win_rate,
            'total_trades': len(trades),
            'avg_trade_per_day': len(trades) / len(values) if len(values) > 0 else 0
        }
