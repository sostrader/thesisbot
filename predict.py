from sklearn.preprocessing import MinMaxScaler
from collections import deque
from indicator import Indicators
from settings import mt, seq_len
import pandas as pd
import numpy as np
import time

def preprocess_prediciton(symbol,timeframe):

   
    df = mt.history(symbol,timeframe,1)
    print("predict",df)


    """
    strategy analysis components
    """

    df.isnull().sum().sum() 
    df.fillna(method="ffill", inplace=True)
    df = df.loc[~df.index.duplicated(keep = 'first')]

    start_time = time.time()
    df = Indicators(df)
    print(("--- %s seconds ---" % (time.time() - start_time)))
    

    df = df.drop("return_next", 1)

    df = df.dropna()
    df = df.fillna(method="ffill")
    df = df.dropna()
    
    df.sort_index(inplace = True)
    

    scaler = MinMaxScaler()
    indexes = df.index
    df_scaled = scaler.fit_transform(df)

    pred = pd.DataFrame(df_scaled,index = indexes)

    sequential_data = []
    prev_days = deque(maxlen = seq_len)

    for i in pred.iloc[len(pred) -seq_len :len(pred)   , :].values:
        prev_days.append([n for n in i[:]])
        if len(prev_days) == seq_len:
            sequential_data.append([np.array(prev_days)])

    X = []

    for seq in sequential_data:
        X.append(seq)
        
        


    return np.array(X)

