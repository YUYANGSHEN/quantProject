# 量化交易回测系统

基于 Binance API 的加密货币量化交易回测框架

## 功能特性

- ✅ Binance 历史数据获取
- ✅ 回测引擎
- ✅ SMA 移动平均策略
- ✅ 性能指标分析
- ✅ 权益曲线可视化

## 安装

```bash
pip install -r requirements.txt
```

## 使用方法

### 1. 回测模式

```bash
python main.py
```

### 2. 配置 API

编辑 `config.py`，填入你的 Binance API Key：

```python
BINANCE_API_KEY = 'your_api_key'
BINANCE_API_SECRET = 'your_secret'
USE_TESTNET = True  # 建议先用测试网
```

## 项目结构

```
quantProject/
├── data/              # 数据模块
│   ├── binance_data.py    # 数据获取
│   └── binance_trader.py  # 交易接口
├── strategy/          # 策略模块
│   ├── base.py           # 策略基类
│   └── sma_strategy.py   # SMA策略
├── backtest/          # 回测模块
│   └── engine.py         # 回测引擎
├── config.py          # 配置文件
└── main.py            # 主程序
```

## 回测结果示例

```
总收益率: 15.23%
最大回撤: -8.45%
胜率: 62.50%
夏普比率: 1.85
交易次数: 24
```

## 注意事项

⚠️ 量化交易有风险，投资需谨慎
⚠️ 建议先在测试网验证策略
⚠️ 实盘前务必小资金测试
