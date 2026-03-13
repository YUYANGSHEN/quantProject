from backtest import BacktestEngine, DataLoader
from strategies import MACrossStrategy


def main():
    # 1. 加载数据（这里用示例数据）
    data = DataLoader.generate_sample_data('2023-01-01', '2024-01-01')
    
    # 2. 创建策略
    strategy = MACrossStrategy(short_window=5, long_window=20)
    
    # 3. 运行回测
    engine = BacktestEngine(strategy, data, initial_cash=100000, commission=0.0003)
    results = engine.run()
    
    # 4. 输出结果
    print(f"\n{'='*50}")
    print(f"策略: {strategy.name}")
    print(f"{'='*50}")
    print(f"总收益率: {results['total_return']:.2f}%")
    print(f"年化收益率: {results['annual_return']:.2f}%")
    print(f"波动率: {results['volatility']:.2f}%")
    print(f"夏普比率: {results['sharpe_ratio']:.2f}")
    print(f"最大回撤: {results['max_drawdown']:.2f}%")
    print(f"胜率: {results['win_rate']:.2f}%")
    print(f"交易次数: {results['total_trades']}")
    print(f"最终资产: {results['final_value']:.2f}")
    print(f"{'='*50}\n")
    
    # 显示交易记录
    if not results['trades'].empty:
        print("交易记录:")
        print(results['trades'].to_string(index=False))


if __name__ == '__main__':
    main()
