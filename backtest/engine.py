"""
回测引擎
"""
import pandas as pd
import numpy as np


class BacktestEngine:
    def __init__(self, strategy, initial_capital=10000):
        self.strategy = strategy
        self.initial_capital = initial_capital
        self.cash = initial_capital
        self.position = None
        self.trades = []
        self.equity_curve = []
    
    def run(self, data):
        """运行回测"""
        for i in range(len(data)):
            bar = data.iloc[i]
            signal = self.strategy.on_bar(bar)
            
            if signal == 'BUY' and self.position is None:
                quantity = (self.cash * 0.95) / bar['close']
                self.position = {'quantity': quantity, 'entry_price': bar['close']}
                self.cash -= quantity * bar['close']
                self.trades.append({
                    'timestamp': bar['timestamp'],
                    'action': 'BUY',
                    'price': bar['close'],
                    'quantity': quantity
                })
            
            elif signal == 'SELL' and self.position:
                proceeds = self.position['quantity'] * bar['close']
                pnl = proceeds - self.position['quantity'] * self.position['entry_price']
                self.cash += proceeds
                self.trades.append({
                    'timestamp': bar['timestamp'],
                    'action': 'SELL',
                    'price': bar['close'],
                    'quantity': self.position['quantity'],
                    'pnl': pnl
                })
                self.position = None
            
            equity = self.cash
            if self.position:
                equity += self.position['quantity'] * bar['close']
            
            self.equity_curve.append({
                'timestamp': bar['timestamp'],
                'equity': equity
            })
        
        return self.generate_report()
    
    def generate_report(self):
        """生成回测报告"""
        equity_df = pd.DataFrame(self.equity_curve)
        trades_df = pd.DataFrame(self.trades)
        
        total_return = (equity_df['equity'].iloc[-1] / self.initial_capital - 1)
        
        equity_df['peak'] = equity_df['equity'].cummax()
        equity_df['drawdown'] = (equity_df['equity'] - equity_df['peak']) / equity_df['peak']
        max_drawdown = equity_df['drawdown'].min()
        
        winning_trades = trades_df[trades_df['pnl'] > 0] if 'pnl' in trades_df.columns else pd.DataFrame()
        win_rate = len(winning_trades) / len(trades_df) if len(trades_df) > 0 else 0
        
        returns = equity_df['equity'].pct_change().dropna()
        sharpe = returns.mean() / returns.std() * np.sqrt(252) if len(returns) > 0 else 0
        
        return {
            'total_return': total_return,
            'max_drawdown': max_drawdown,
            'win_rate': win_rate,
            'sharpe_ratio': sharpe,
            'total_trades': len(trades_df),
            'equity_curve': equity_df,
            'trades': trades_df
        }
