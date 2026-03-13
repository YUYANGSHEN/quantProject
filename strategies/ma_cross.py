from backtest.strategy import Strategy


class MACrossStrategy(Strategy):
    """双均线交叉策略"""
    
    def __init__(self, short_window: int = 5, long_window: int = 20):
        super().__init__("MA Cross")
        self.short_window = short_window
        self.long_window = long_window
        self.position = 0
        
    def on_bar(self, date, bar):
        """每个bar的回调"""
        # 计算均线
        close_prices = self.data.loc[:date, 'close']
        if len(close_prices) < self.long_window:
            return
            
        short_ma = close_prices.iloc[-self.short_window:].mean()
        long_ma = close_prices.iloc[-self.long_window:].mean()
        
        # 交易信号
        if short_ma > long_ma and self.position == 0:
            # 金叉买入
            size = int(self.broker.cash / bar['close'])
            if self.broker.buy('symbol', bar['close'], size, date):
                self.position = 1
                
        elif short_ma < long_ma and self.position == 1:
            # 死叉卖出
            size = self.broker.get_position('symbol')
            if self.broker.sell('symbol', bar['close'], size, date):
                self.position = 0
