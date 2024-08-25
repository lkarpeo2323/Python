import random
def game():
    weapon = input("rock, paper, scissors").lower()
    options = ["rock", "paper", "scissors"]

    if weapon not in options:
        print("loser")
    else:
        cpu_result = random.choice(options)
        print("computer chose", cpu_result)

        if cpu_result == weapon:
            print("its a tie")
        elif (cpu_result=="rock" and weapon=="paper") or \
            (cpu_result=="paper" and weapon=="scissors") or \
            (cpu_result=="scissors" and weapon=="rock"):
            print("You win")
        else:
            print("you lose")
game()
