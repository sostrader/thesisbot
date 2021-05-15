from settings import *
from predict import preprocess_prediciton
from utils.fuctions import *


model = retrain()

while(1):
    if check_stop_time():
        print('wating to pass opening market')
        countdown(1200)
        predict_count = 10
        
          
    t = 60
    if predict_count >= 10 and predict_count % 2 == 0:
        model = retrain()
        predict_count = 0
    if iq.remaning(timeframe) - 3 == iq.timeframe_to_sec(timeframe): 
        time_taker = time.time()
        pred = preprocess_prediciton(symbol,timeframe)              
        pred = pred.reshape(1,seq_len,pred.shape[3])     
        result = model.predict(pred)
        
       
        print(("probability of PUT: {:.2f}%".format(round(result[0][0],2))))
        print(("probability of CALL: {:.2f}%".format(round(result[0][1],2))))
        print(f'Time taken : {int(time.time()-time_taker)} seconds')
        predict_count = predict_count + 1
        payout = iq.payout(symbol) 
        balance = iq.balance()
        print(f'Simbol : {symbol}')
        print(f'Balance : {balance}')
        print(("Payout: {:.2f}%".format(payout)))
        print(("BET: {:.2f}$".format(contract)))
        print(("Next Martingale: {:.2f}$".format(contract * round(gale_multiply/iq.payout(symbol),2))))
        # print ("Winning Rate : {:.2f}%".format(percentage(win_count,buy_count+sell_count))+'\n'+"Trade N°: "+str(sell_count+buy_count)+'\n')
        print(("Winning Rate: {:.2f}%".format(percentage(win_count,buy_count+sell_count-Tiedtrade))+'\n'+"Trade N°: "+str(sell_count+buy_count)+'\n'))
        
       

    
        if result[0][0] > result[0][1] and result[0][0] > min_prob and iq.payout(symbol) >=min_payout and balance > min_balance:
            print("PUT")
            id =  iq.sell(contract,symbol,timeframe) 
            sell_count += 1
            predict_count = predict_count + 1
            trade = True
        elif result[0][1] > result[0][0] and result[0][1] > min_prob and iq.payout(symbol) >=min_payout and balance > min_balance:
            print("CALL")
            id = iq.buy(contract,symbol,timeframe) 
            buy_count += 1
            predict_count = predict_count + 1
            trade = True
        else:
            trade = False
            predict_count = predict_count + 1

            
        if trade:
            win = iq.checkwin(id)  
            profit += win 
            if win > 0:
                print(("WIN"+'\n')) 
                win_count += 1
                if gale_count >= gale_seq:
                     gale_count = 0
                     # predict_count = 10
                     contract = min_contract

                else:                                       
                    contract = contract + win              
                    gale_count += 1                         
                
            elif win < 0:                         
                contract = min_contract           
                gale_count = 0                    
                print(("LOSS"+'\n'))              
                

            elif win == 0:
                print(('Tied Wait for 3 minutes befor next Trade'+'\n')) 
                Tiedtrade += 1
                # countdown(180)
                # # predict_count = 10
                  