import pandas as pd

def movingAverage(df, n):
    
    MA = pd.Series(df['Close'].rolling(n, min_periods = n).mean(), name = 'MA_' + str(n))
    df = df.join(MA)
    return df
