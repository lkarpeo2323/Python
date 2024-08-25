import random

print("welcome to rock paper scissors")

def game():
    weapon = input("rock, paper, scissors: ").lower()
    options = ["rock", "paper", "scissors"]

    if weapon not in options:
        print("disqualified")
    else:
        cpu = random.choice(options)
        print("the cpu chose", cpu)
        if cpu == weapon:
            print("its a tie")
        elif(weapon=="paper" and cpu=="rock") or \
            (weapon=="rock" and cpu=="scissors") or \
            (weapon=="scissors" and cpu=="paper"):
            peint("you win")
        else:
            print("you lose")

game()

