import random

comp_choice = random.choice(["scissors", "paper", "rock"])

user_choice = input("Do you want - rock, paper, or scissors?\n")


print("You chose " + user_choice + "\n" + "Computer chose " + str(comp_choice))
if comp_choice == user_choice:
    print("TIE GAME")
elif user_choice == "rock" and comp_choice == "scissors":
    print("YOU WIN")
elif user_choice == "paper" and comp_choice == "rock":
    print("YOU WIN")
elif user_choice == "scissors" and comp_choice == "paper":
    print("YOU WIN")
else:
    print("YOU LOST")
