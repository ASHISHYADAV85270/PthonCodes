###Modified guessing number game 
import random
num=random.randint(1,100)
gameover=True
count=0
while gameover:
    guess=int(input("  GUESS AGAIN "))
    count+=1
    if guess==num:
        print(f"WINNER WINNER CHICKEN DINNER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! and you taked {count} attempts")
        gameover=False
    elif guess>num:
        print("LARGE ")    
    else:
        print("SMALL ")    