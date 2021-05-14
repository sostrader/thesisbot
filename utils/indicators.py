
from ejtrader import indicators as TA
from .candlestick import candlestick as cd
import numpy as np
import pandas as pd
import time
import multiprocessing as mp

class technical_analysis:
    def __init__(self, df=None, strategy=None):
        self.df = df
        self.strategy = strategy or "one"
       
        
    def strategy_one(self,df, qout):

        df["volati"] = df["close"].rolling(window=45).std() * np.sqrt(45)
        # simple moving avarage
        df['SMA_014'] = TA.SSMA(df,14)
        df['SMA_020'] = TA.SSMA(df,20)
        df['SMA_050'] = TA.SSMA(df,50)
        df['SMA_100'] = TA.SSMA(df,100)
        df['SMA_200'] = TA.SSMA(df,200)

        # exponential moving average
        df['EMA_014'] = TA.EMA(df,14, adjust=False)
        df['EMA_020'] = TA.EMA(df,20, adjust=False)
        df['EMA_050'] = TA.EMA(df,50, adjust=False)
        df['EMA_100'] = TA.EMA(df,100, adjust=False)
        df['EMA_200'] = TA.EMA(df,200, adjust=False)
    
        
        
        #Stochastic Oscillator
        df['%K'] = TA.STOCH(df, 14)
        df['%D'] = TA.STOCHD(df, 14)

        #Relative Strenght Index 'RSI'
        df['rsi'] = TA.RSI(df, 14)

        # CCI
        df['cci'] = TA.CCI(df,period=14)


        # Keltner Channels
        keltner = TA.KC(df)
        df['KC_UPPER'] = keltner['KC_UPPER']
        df['KC_LOWER'] = keltner['KC_LOWER']


        # DO Channels
        doch = TA.DO(df)
        df['DO_UPPER'] = doch['LOWER']
        df['DO_MID'] = doch['MIDDLE']
        df['DO_LOWER'] = doch['UPPER']

        # MACD
        MACD = TA.MACD(df)
        df['MACD'] = MACD['MACD']
        df['SIGNAL'] = MACD['SIGNAL']

        
        df['ROC'] = TA.ROC(df,1)
        df['ROC2'] = TA.ROC(df,2)
        df['ROC3'] = TA.ROC(df,3)
        df['ROC4'] = TA.ROC(df,4)
        df['ROC5'] = TA.ROC(df,5)

        # # timestamp to date
        # date = pd.to_datetime(df['date'],unit='s')
        # df['HOUR'] = date.dt.hour
        # df['MINUTE'] = date.dt.minute


        # predict and train data manipulation
        df['return_next'] = df['ROC'].shift(-1)
        df['return'] = df['ROC'] 

        # df['return'] = df['return'].apply(lambda x: 1 if x>0 else 0)
        # df['return_next'] = df['return_next'].apply(lambda x: 1 if x>0 else 0)

        
        df = df.drop(columns = {'date'})

        return df 


    def strategy_two(self,df):
        df["volati"] = df["close"].rolling(window=5).std() * np.sqrt(5)
        # simple moving avarage
        df['SMA_7'] = TA.SSMA(df,7)
        df['SMA_14'] = TA.SSMA(df,14)
        df['SMA_28'] = TA.SSMA(df,28)
        df['SMA_56'] = TA.SSMA(df,56)
        df['SMA_112'] = TA.SSMA(df,112)

        # exponential moving average
        df['EMA_3'] = TA.EMA(df,3, adjust=False)
        df['EMA_6'] = TA.EMA(df,6, adjust=False)
        df['EMA_12'] = TA.EMA(df,12, adjust=False)
        df['EMA_24'] = TA.EMA(df,24, adjust=False)
        df['EMA_48'] = TA.EMA(df,48, adjust=False)
    
        
        
        #Stochastic Oscillator
        df['%K'] = TA.STOCH(df, 7)
        df['%D'] = TA.STOCHD(df, 7)

        df['%K'] = TA.STOCH(df, 14)
        df['%D'] = TA.STOCHD(df, 14)

        #Relative Strenght Index 'RSI'
        df['rsi'] = TA.RSI(df, 14)
        df['cci'] = TA.CCI(df,period=14)

        df['rsi'] = TA.RSI(df, 7)
        df['cci'] = TA.CCI(df,period=7)

        
        df['ROC1'] = TA.ROC(df,1)
        df['ROC2'] = TA.ROC(df,2)
        df['ROC3'] = TA.ROC(df,3)
        df['ROC4'] = TA.ROC(df,4)
        df['ROC5'] = TA.ROC(df,5)

        # timestamp to date
        # date = pd.to_datetime(df['date'],unit='s')
        # df['HOUR'] = date.dt.hour
        # df['MINUTE'] = date.dt.minute


        # predict and train data manipulation
        df['return_next'] = df['ROC1'].shift(-1)
        df['return'] = df['ROC1'] 

        # df['return'] = df['return'].apply(lambda x: 1 if x>0 else 0)
        # df['return_next'] = df['return_next'].apply(lambda x: 1 if x>0 else 0)

        
        df = df.drop(columns = {'date'})

        return df 

    def strategy_three(self,df):
        # DO Channels
        doch = TA.DO(df)
        df['DO_UPPER'] = doch['LOWER']
        df['DO_MID'] = doch['MIDDLE']
        df['DO_LOWER'] = doch['UPPER']

       
        
        df['ROC'] = TA.ROC(df,1)

        # # timestamp to date
        df.index = pd.to_datetime(df.index)
        #for get year
        df['YEAR'] =df.index.dt.year

        #for get month
        df['MONTH'] =df.index.dt.month

        #for get day
        df['DAY'] =df.index.dt.day

        #for get hour
        df['HOUR'] = df.index.dt.hour

        #for get minute
        df['MINUTE'] = df.index.dt.minute

        

        # predict and train data manipulation
        df['return_next'] = df['ROC'].shift(-1)
        df['return'] = df['ROC'] 

        return df 


 
    
   