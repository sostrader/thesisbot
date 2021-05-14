class trading_methodology(self,):
    def sohos():
        if result[0][0] > result[0][1] and result[0][0] > min_prob and ej.iq_get_payout(iq,symbol) >=min_payout and balance > min_balance:
            print("PUT")
            id = ej.iq_sell_binary(iq,contract,symbol,expire_time)
            sell_count += 1
            predict_count = predict_count + 1
            trade = True
        elif result[0][1] > result[0][0] and result[0][1] > min_prob and ej.iq_get_payout(iq,symbol) >=min_payout and balance > min_balance:
            print("CALL")
            id = ej.iq_buy_binary(iq,contract,symbol,expire_time) 
            buy_count += 1
            predict_count = predict_count + 1
            trade = True
        else:
            trade = False
            predict_count = predict_count + 1

            
        if trade:
            win = ej.iq_checkwin(iq,id)
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
                
                # 
            elif win < 0:
                contract = min_contract
                gale_count = 0
                print(("LOSS"+'\n'))
                

            elif win == 0:
                print(('Tied Wait for 3 minutes befor next Trade'+'\n')) 
                Tiedtrade += 1
                # countdown(180)
                # # predict_count = 10