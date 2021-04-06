# Import Python library random

import random

Num = random.randint(1,100)

UserNum = int(input("Guess a number between 1 and 100 :"))
attempts = 0

  # Define how many times user attempts guesses..

while attempts < 5: 

    attempts +=1

    if UserNum < Num:
        print ("Too low!")
        UserNum = int(input("Try again...."))
        

    elif UserNum > Num:
        print("Too high")
        UserNum = int(input("Try again...."))
    
    elif UserNum == Num:
        break


if UserNum == Num:
        print("Great job!, after ", attempts, "attempt(s)")
else:
    print("You did not guess right")