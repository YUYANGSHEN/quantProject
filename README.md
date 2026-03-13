# 量化回测框架

简洁实用的 Python 量化交易回测系统。

## 功能特性

- ✅ 事件驱动的回测引擎
- ✅ 灵活的策略基类
- ✅ 完整的交易模拟（手续费、滑点）
- ✅ 详细的性能分析（收益率、夏普、回撤、胜率）
- ✅ 支持自定义策略
- ✅ 内置示例策略（双均线交叉）

## 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行示例

```bash
python main.py
```

## 框架结构

```
quantProject/
├── backtest/           # 核心回测模块
│   ├── engine.py      # 回测引擎
│   ├── strategy.py    # 策略基类
│   ├── broker.py      # 交易模拟
│   ├── data.py        # 数据加载
│   └── analyzer.py    # 性能分析
├── strategies/         # 策略实现
│   └── ma_cross.py    # 双均线策略
└── main.py            # 运行入口
```

## 自定义策略

继承 `Strategy` 基类并实现 `on_bar` 方法：

```python
from backtest.strategy import Strategy

class MyStrategy(Strategy):
    def __init__(self):
        super().__init__("My Strategy")
        
    def on_bar(self, date, bar):
        # 你的交易逻辑
        if 买入条件:
            self.broker.buy('symbol', bar['close'], size, date)
        elif 卖出条件:
            self.broker.sell('symbol', bar['close'], size, date)
```

## 使用真实数据

```python
from backtest import DataLoader

# 从 CSV 加载
data = DataLoader.load_csv('data.csv', date_col='date')

# 数据格式要求：
# date, open, high, low, close, volume
```

## 性能指标

- **总收益率** - 整个回测期间的收益
- **年化收益率** - 按年计算的收益率
- **波动率** - 收益的标准差（年化）
- **夏普比率** - 风险调整后收益
- **最大回撤** - 最大资产回撤百分比
- **胜率** - 盈利交易占比

## 下一步优化

- [ ] 接入真实行情数据源（tushare/akshare）
- [ ] 参数优化器（网格搜索/遗传算法）
- [ ] 多品种回测
- [ ] 可视化图表（matplotlib/plotly）
- [ ] 实盘接口对接

## License

MIT
