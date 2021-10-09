# value=int(input("enter some number"))
# if(value >100):
#     print("more than 100")
# else:
#     print("less than 100")

import random
ch=10
number = random.randint(1, 9)
print(number)
while ch >5:
    guess=int(input("enter some number"))
    ch=ch-1
    if(guess>number):   
        print("your guess is too high")
    elif(guess<number):
        print("your guess is too low")
    elif(guess==number):
        print("you won")