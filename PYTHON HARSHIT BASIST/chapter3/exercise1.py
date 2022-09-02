import random
n = random.randint(0,10) # y ek random int dedega between given range 
guess=int(input("ENTER A NUMBER BETWEEN 1 TO 10 "))
 #nested if else
if n==guess:
    print("YOU WIN MY BOY")
else:
    if n>guess:
        print(f"number gueesed is low and the actual number is {n}")
    else:
        print(f"number gueesed is high and the actual number is {n}")
