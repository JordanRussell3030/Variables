#Jordan Russell
#22/09/14
#Guess the right number program

import random, time

print("You have to guess the number that this program generates.")
time.sleep(1)
number = int(input("Please input a number between 1 and 10: "))
computer_number = random.randint(1, 10)
if (number < 1):
    print("That is not between 1 and 10.")
if (number > 10):
    print("That is too high.")
if (number == computer_number):
    print("Congratulations, you guessed right!")
else:
    print("Sorry, you guessed wrong.")
    
