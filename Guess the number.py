import random

target=random.randint(1,100)

while True:
    userPick= input("Guess the target or Exit : ")
    if(userPick == "Exit"):
        break
    userPick=int(userPick)
    if(userPick == target):
        print("shabbashhhh")
        break
    elif(userPick < target):
        print("Your number small than target")
    else:
        print("Your Number Bigger than Target")

print("GAME OVER")