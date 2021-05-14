from settings import *
import datetime
import time
from model import train_data
import tensorflow as tf

min_contract = contract
win_count = 0 
sell_count = 0
buy_count = 0
Tiedtrade = 0
predict_count = 0
gale_count = 0 
bid = True
trade = True
profit = 0



# define the countdown func. 
def countdown(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
      
    print('Ready for the Nex Trade!!')


#training fuction
def retrain():
    
    while train_data(symbol,timeframe) < 60:
        import os
        import sys
        import shutil

        # Get directory name
        TUNFILE= "TUN/"
        MODELFILE = "models/ThesisBrain.h5"
        try:
            shutil.rmtree(TUNFILE)
            os.remove(MODELFILE)
            print("Removing old Model..")
        except OSError:
            pass
            
        train_data(symbol,timeframe)
        
    else:
        model = tf.keras.models.load_model('models/ThesisBrain.h5')
        return model
    

def check_stop_time():
    hour = datetime.datetime.now().hour 
    minutes = datetime.datetime.now().minute
    # BERLIN 05:00 - 13:00 / LONDON 06:00 - 14:00 / NEW YORK 11:00 - 19:00 / SYDNEY 19:00 - 03:00 / TOKYO 21:00 - 05:00
    forex_open_close = ['4','12','5','13','10','18','2','25']
   
    for times_market in forex_open_close:
        stoptime = times_market
        if str(hour) == stoptime and minutes >= 50:
            return True
    
    return False


def percentage(entry1, entry2):
    try:
        return ( 100 * entry1 /entry2) 
    except ZeroDivisionError:
        return 0