"""
批量下载 Binance K线数据
"""
from data.binance_data import BinanceData
import pandas as pd
import os
from datetime import datetime


def download_klines():
    """下载多个币种的K线数据"""
    
    # 配置
    symbols = ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT']
    intervals = ['1m', '5m', '15m', '30m', '1h', '4h', '1d']
    start_date = '1 Jan, 2024'
    
    # 创建数据目录
    os.makedirs('data/klines', exist_ok=True)
    
    # 初始化数据获取器
    fetcher = BinanceData()
    
    print("开始下载数据...")
    
    for symbol in symbols:
        print(f"\n处理 {symbol}...")
        
        for interval in intervals:
            try:
                print(f"  下载 {interval} 数据...", end=' ')
                
                # 获取数据
                df = fetcher.get_klines(symbol, interval, start_date)
                
                # 保存为CSV
                filename = f"data/klines/{symbol}_{interval}.csv"
                df.to_csv(filename, index=False)
                
                print(f"✓ 完成 ({len(df)} 条)")
                
            except Exception as e:
                print(f"✗ 失败: {e}")
    
    print("\n所有数据下载完成！")


if __name__ == '__main__':
    download_klines()
