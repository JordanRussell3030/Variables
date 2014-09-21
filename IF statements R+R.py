#Jordan Russell
#21/09/14
#R+R Assignment IF statements.

import time

age = int(input("Please input your age: "))

years_until_retirement = (65 - age)

if (age < 18):
    print("You are not old enough to vote.")
    
else:
    if (age >= 18 - 65):
        print("You are old enough to vote, and you can retire in {0} years.".format(years_until_retirement))

    else:
        if (age >= 65):
            print("You are old enough to vote and you can retire now.")


