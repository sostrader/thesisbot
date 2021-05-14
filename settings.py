
from ejtraderMT import Metatrader
from ejtraderIQ import IQOption

#  only warnings block
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

# IQ Option api Callback
iq = IQOption("tribolinux@gmail.com","tribopass@123","DEMO")

# Metatrader API Callback
mt = Metatrader(host="node-1")








symbol = "EURUSD"     
timeframe = "M1"   
contract = 2
expire_time = "M1"    


gale_multiply = 2      # FATOR DE MULTIPLICAÇÃO DE MARTINGALE
gale_seq = 5        # QUANTIDADE MAXIMA DE MARTINGALE
          
min_payout = 0.10    # MINIMO PAYOUT PARA ABRIR UMA ORDEM
min_balance =  0        # VALOR MINIMO NA CONTA PARA ABRIR UM TRADE
min_prob = 0.70     # % MINIMA DE PROBABILIDADE PARA ABIR UM TRADE 



# settings for predict on model
seq_len = 5
predict_period = 1 


# Hyperparameters
EPOCHS = 40
BATCH_SIZE = 32





