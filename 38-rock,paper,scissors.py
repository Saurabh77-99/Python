import random

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock,paper or scissors? :").lower()

    if player == computer:
        print("computer:",computer)
        print("player:",player)
        print("Tie!!")
    elif player == "rock":
        if computer == "paper":
            print("computer:",computer)
            print("player:",player)
            print("You LOSEE !")
        if computer == "scissors":
            print("computer:",computer)
            print("player:",player)
            print("You Win!")
    elif player == "paper":
        if computer == "scissors":
            print("computer:",computer)
            print("player:",player)
            print("You LOSEE !")
        if computer == "rock":
            print("computer:",computer)
            print("player:",player)
            print("You Win!")
    elif player == "scissors":
        if computer == "rock":
            print("computer:",computer)
            print("player:",player)
            print("You LOSEE !")
        if computer == "paper":
            print("computer:",computer)
            print("player:",player)
            print("You Win!")
    
    play_again = input("Play again ? (y/n) :").lower()

    if play_again != "y":
        break

print("Bye!!")
