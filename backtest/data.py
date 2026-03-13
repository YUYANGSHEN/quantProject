import pandas as pd
from typing import Optional


class DataLoader:
    """数据加载器"""
    
    @staticmethod
    def load_csv(filepath: str, date_col: str = 'date') -> pd.DataFrame:
        """从CSV加载数据"""
        df = pd.read_csv(filepath, parse_dates=[date_col])
        df.set_index(date_col, inplace=True)
        return df
    
    @staticmethod
    def generate_sample_data(start: str = '2023-01-01', 
                            end: str = '2024-01-01', 
                            freq: str = 'D') -> pd.DataFrame:
        """生成示例数据（随机游走）"""
        import numpy as np
        dates = pd.date_range(start, end, freq=freq)
        price = 100 + np.cumsum(np.random.randn(len(dates)) * 2)
        return pd.DataFrame({
            'open': price * (1 + np.random.randn(len(dates)) * 0.01),
            'high': price * (1 + abs(np.random.randn(len(dates))) * 0.02),
            'low': price * (1 - abs(np.random.randn(len(dates))) * 0.02),
            'close': price,
            'volume': np.random.randint(1000000, 10000000, len(dates))
        }, index=dates)
