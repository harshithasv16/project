#Game Program

import random
name = input("Enter a name:")
print("Hello ",name,"Guess number 1 to 20")

num = random.randint(1,20)
for i in range(1,6):
    gnum = int(input("Enter the guess number"))
    if gnum < num:
        print("Guessed number is low")
    elif gnum > num:
        print("Guessed number is high")
    else:
             break
if(gnum == num):
        print("You guessed in",i,"chances")

else:
        print("Not able to guess the number",num)
