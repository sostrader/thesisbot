import numpy as np
import pandas as pd
import talib as TA


def Indicators(df):
    # df = df.pct_change()
    # df['open'] = df['open'].apply(lambda x: 1 if x>0 else 0)
    # df['high'] = df['high'].apply(lambda x: 1 if x>0 else 0)
    # df['low'] =  df['low'].apply(lambda x: 1 if x>0 else 0)
    # df['close'] = df['close'].apply(lambda x: 1 if x>0 else 0)

    # # timestamp to date
    date = pd.to_datetime(df.index,unit='s')
    # #for get year
    # df['YEAR'] = date.year
    # #for get month
    df['MONTH'] = date.month
    # #for get day
    df['DAY'] =date.day
    #for get hour
    df['HOUR'] = date.hour
    #for get minute
    df['MINUTE'] = date.minute

    # predict and train data manipulation
    df['return_next'] = df['close'].shift(-1)
    df['return'] = df['close']

    df['return'] = df['return']
    df['return_next'] = df['return_next']
    
        
    df = df.drop(columns = {'spread','open','low','high'})


    return df

