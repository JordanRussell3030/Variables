#Jordan Russell
#15/09/14
#Finding randomized values and outputting the total.

import time, random

random_one = random.randint(1,100)
random_two = random.randint(1,100)
random_three = random.randint(1,100)

user_number_one = int(input("You are competing against the computer to get a higher random score. Please input a number betwwen 1 and 50: "))
user_number_two = int(input("Please input a second number between 1 and 50: "))
user_number_three = int(input("Please input a third number between 1 and 50: "))

final_random = (random_one + random_two + random_three)
final_user_number = (user_number_one + user_number_two + user_number_three)

if (final_random > final_user_number):
    print("Unlucky, the computer has a higher score than you.")

elif (final_random < final_user_number):
    print("Congratulations, you scored higher than the computer!")
    
