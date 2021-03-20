import pandas as pd

def get_indicators(klines):
    data = []
    for kline in klines:
        print(kline)
        data.append({'close': kline.close, 'volume': kline.volume})
    df = pd.DataFrame.from_dict(data)
    df['ema12'] = pd.Series.ewm(df['close'], span=12).mean()
    df['ema26'] = pd.Series.ewm(df['close'], span=26).mean()
    df['dif']= df['ema12'] - df['ema26']
    df['dea']= pd.Series.ewm(df['dif'], span=9).mean()
    df['histogram']= df['dif'] - df['dea']
    df['ma20_volume'] = df['volume'].rolling(window=20).mean()
    df['ma20_close'] = df['close'].rolling(window=20).mean()
    return {
        'volume': df['volume'].iloc[-1],
        'ma20_volume': df['ma20_volume'].iloc[-1],
        'close': df['close'].iloc[-1],
        'ma20_close': df['ma20_close'].iloc[-1],
        'dif': df['dif'].iloc[-1],
        'histogram': df['histogram'].iloc[-1],
        'dea': df['dea'].iloc[-1],
        'previous_histogram': df['histogram'].iloc[-2],
    }