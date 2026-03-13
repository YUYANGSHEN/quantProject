"""
配置文件
"""

# Binance API 配置
BINANCE_API_KEY = 'your_api_key_here'
BINANCE_API_SECRET = 'your_api_secret_here'
USE_TESTNET = True  # 使用测试网

# 回测配置
INITIAL_CAPITAL = 10000
SYMBOL = 'BTCUSDT'
INTERVAL = '1h'

# 策略参数
SMA_SHORT = 10
SMA_LONG = 30
