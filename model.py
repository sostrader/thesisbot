import numpy as np
import pandas as pd
import random
from collections import deque

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM, BatchNormalization
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping


import os

from settings import seq_len, EPOCHS, BATCH_SIZE, mt
from kerastuner.tuners import RandomSearch
from indicator import Indicators

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'



def classify(current,return_next):
    if float(return_next) > float(current):
        return 1
    else:
        return 0

def preprocess_df(df):
    df = df.drop("return_next", 1)
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    indexes = df.index
    df_scaled = scaler.fit_transform(df)

    df = pd.DataFrame(df_scaled,index = indexes)

    sequential_data = []
    prev_days = deque(maxlen=seq_len)

    for i in df.values:
        prev_days.append([n for n in i[:-1]])
        if len(prev_days) == seq_len:
            sequential_data.append([np.array(prev_days), i[-1]])

    random.shuffle(sequential_data)

    buys = []
    sells = []

    for seq, target in sequential_data:
        if target == 0:
            sells.append([seq, target])
        elif target == 1:
            buys.append([seq, target])

    random.shuffle(buys)
    random.shuffle(sells)


    lower = min(len(buys), len(sells))

    buys = buys[:lower]
    sells = sells[:lower]


    sequential_data = buys+sells
    random.shuffle(sequential_data)

    X = []
    y = []

    for seq, target in sequential_data:
        X.append(seq)
        y.append(target)

    return np.array(X), y



def train_data(symbol,timeframe):
    
    df = mt.history("EURUSD","M1",2)
    print("traning",df)
    
   
    df.isnull().sum().sum() # there are no nans
    df.fillna(method="ffill", inplace=True)
    df = df.loc[~df.index.duplicated(keep = 'first')]
    
    
    df = Indicators(df)
    
    
    df = df.dropna()
    df = df.fillna(method="ffill")
    df = df.dropna()
    
    df.sort_index(inplace = True)

    

    df['target'] = list(map(classify, df['return'], df['return_next']))
   
    print(df)
   
    df.dropna(inplace=True)
    df['target'].value_counts()
    df.dropna(inplace=True)
    df = df.astype('float32')

    df = preprocess_df(df)
    train_x, train_y = df
    validation_x, validation_y = df

    

    train_y = np.asarray(train_y)
    validation_y = np.asarray(validation_y)
    print(('%% of Class0 : %f Sell' % (np.count_nonzero(train_y == 0)/float(len(train_y)))))
    print(('%% of Class1 : %f Buy' % (np.count_nonzero(train_y == 1)/float(len(train_y)))))
        
    
      

    
    def build_model(hp):
        model = Sequential()
        
        model.add(LSTM(hp.Int('units', min_value=10, max_value=50, step=1), input_shape=(train_x.shape[1:]), return_sequences=True))
        model.add(Dropout(0.1))
        model.add(BatchNormalization())

        model.add(LSTM(units=hp.Int('units',
                                        min_value=10,
                                         max_value=50,
                                        step=1), return_sequences=True))
        model.add(Dropout(0.2))
        model.add(BatchNormalization())

        model.add(LSTM(units=hp.Int('units',
                                        min_value=10,
                                         max_value=50,
                                        step=1)))
        model.add(Dropout(0.2))
        model.add(BatchNormalization())

        model.add(Dense(hp.Int('units',
                                            min_value=10,
                                             max_value=50,
                                            step=1),
                            activation='relu'))
        model.add(Dropout(0.2))

        model.add(Dense(2, activation='softmax'))

    
        # Compile model
        model.compile(
            optimizer=Adam(
                hp.Choice('learning_rate',
                        values=[1e-2])),
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])
        return model

    tuner = RandomSearch(
            build_model,
            objective='val_accuracy',
            max_trials=10,
            executions_per_trial=1,
            directory='TUN',
            project_name='IQOTC')

    # tuner.search_space_summary() 
    stop_early = EarlyStopping(monitor='val_loss', patience=15)

   
    tuner.search(train_x,train_y,batch_size=BATCH_SIZE, epochs=EPOCHS,validation_split=0.2, verbose=1, callbacks=[stop_early]),


    best_hps=tuner.get_best_hyperparameters(num_trials=1)[0]

    print(f"""
    The optimal number of units layer is {best_hps.get('units')} 
    and the optimal learning rate for the optimizer is {best_hps.get('learning_rate')}.
    """)

    filepath = "ThesisBrain"
    # Build the model with the optimal hyperparameters and train it on the data for 50 epochs
    model = tuner.hypermodel.build(best_hps)
    
    history = model.fit(train_x, train_y,batch_size=BATCH_SIZE, epochs=EPOCHS, validation_split=0.2, verbose=1)
    val_acc_per_epoch = history.history['val_accuracy']
    best_epoch = val_acc_per_epoch.index(max(val_acc_per_epoch)) + 1
    print(('Best epoch: %d' % (best_epoch,)))
    hypermodel = tuner.hypermodel.build(best_hps)
    scores = model.evaluate(validation_x, validation_y, verbose=0)
    print(("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100)))
    
    del model
    del history
    # Retrain the model
    hypermodel.fit(validation_x, validation_y,batch_size=BATCH_SIZE, epochs=best_epoch, verbose=1)
    hypermodel.save("models/{}.h5".format(filepath))

    scores = hypermodel.evaluate(validation_x, validation_y, verbose=0)
    print(("%s: %.2f%%" % (hypermodel.metrics_names[1], scores[1]*100)))
    scores = scores[1]*100

    
    

    return scores

    
 
