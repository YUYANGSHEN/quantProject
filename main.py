"""
量化交易回测系统 - 主程序
"""
import pandas as pd
from strategy.sma_strategy import SMAStrategy
from backtest.engine import BacktestEngine
import matplotlib.pyplot as plt


def main():
    # 1. 加载本地数据
    print("正在加载数据...")
    data = pd.read_csv('data/klines/BTCUSDT_1h.csv')
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    print(f"数据加载完成，共 {len(data)} 条")
    
    # 2. 创建策略
    strategy = SMAStrategy(short_window=10, long_window=30)
    
    # 3. 运行回测
    print("开始回测...")
    engine = BacktestEngine(strategy, initial_capital=10000)
    report = engine.run(data)
    
    # 4. 输出结果
    print("\n=== 回测结果 ===")
    print(f"总收益率: {report['total_return']:.2%}")
    print(f"最大回撤: {report['max_drawdown']:.2%}")
    print(f"胜率: {report['win_rate']:.2%}")
    print(f"夏普比率: {report['sharpe_ratio']:.2f}")
    print(f"交易次数: {report['total_trades']}")
    
    # 5. 绘制权益曲线
    plt.figure(figsize=(14, 7))
    
    # 权益曲线
    plt.subplot(2, 1, 1)
    plt.plot(report['equity_curve']['timestamp'], report['equity_curve']['equity'], linewidth=2)
    plt.title('Equity Curve - BTC/USDT 1H SMA Strategy', fontsize=14, fontweight='bold')
    plt.ylabel('Equity ($)', fontsize=12)
    plt.grid(True, alpha=0.3)
    
    # 回撤曲线
    plt.subplot(2, 1, 2)
    plt.fill_between(report['equity_curve']['timestamp'], 
                     report['equity_curve']['drawdown'] * 100, 
                     0, alpha=0.3, color='red')
    plt.plot(report['equity_curve']['timestamp'], 
             report['equity_curve']['drawdown'] * 100, 
             color='red', linewidth=1)
    plt.title('Drawdown', fontsize=12)
    plt.ylabel('Drawdown (%)', fontsize=12)
    plt.xlabel('Date', fontsize=12)
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('equity_curve.png', dpi=150)
    print("\n权益曲线已保存为 equity_curve.png")


if __name__ == '__main__':
    main()
