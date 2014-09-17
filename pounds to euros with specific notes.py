#Jordan Russell
#17/09/14
#Python school exercise 7

import time

money_sterling = float(input("PLese input the amount of money in sterling you are taking on holiday: "))
exchange_rate = float(input("Please input the current exchange rate from pounds to euros: "))
money_euros = (money_sterling // exchange_rate)

print("You will receive {0} euros.".format(money_euros))
print("These are the notes you will be given: ")
euros50 = int(money_euros // 50)
remaining_euros = money_euros % 50
euros20 = int(remaining_euros // 20)
remaining_euros = remaining_euros % 20
euros10 = int(remaining_euros // 10)
remaining_euros = remaining_euros % 10
euros5 = int(remaining_euros // 5)
remaining_euros = remaining_euros % 5
time.sleep(1)
print("{0} 50 euro note(s)".format(euros50))
time.sleep(1)
print("{0} 20 euro note(s)".format(euros20))
time.sleep(1)
print("{0} 10 euro note(s)".format(euros10))
time.sleep(1)
print("{0} 5 euro note(s)".format(euros5))
time.sleep(1)
print("and {0} euro(s) in coins".format(remaining_euros))
      
