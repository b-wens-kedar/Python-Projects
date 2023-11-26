#Press the green "Run" button at the bottom to start the game

import random

def play():
    playerChoice = input("Let's play a game.\n'rock', 'paper', 'scissor'?\n").lower()
    options = ["rock", "paper", "scissors"]
    computerChoice = random.choice(options)
    return playerChoice, computerChoice


def checkWin(player, computer):
    print(f"You chose {player} and the computer chose {computer} ")
    if player == computer:
        print("It's a tie.🙃")
    elif player == "rock":
        if computer == "paper":
            print("The paper covers the rock. You lose.😥")
        else:
            print("The rock smashes the scissors. You win!😎")
    elif player == "paper":
        if computer == "rock":
            print("The paper covers the rock. You win!😎")
        else:
            print("The scissors cut the paper. You lose.😥")
    elif player == "scissors":
        if computer == "rock":
            print("The rock smashes the scissors. You lose.😥")
        else:
            print("The scissors cut the paper. You win!😎")


choices = play()
if choices[0] == "rock" or choices[0] == "paper" or choices[0] == "scissors":
    checkWin(choices[0], choices[1])
else:
    print("Please choose between 'rock', 'paper', or 'scissors'")

