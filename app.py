#Create a Rock Paper Scissors multiplayer game with the following rules:
#Rock beats Scissors
#Scissors beats Paper
#Paper beats Rock
#Computer will be one of the players
#If both players choose the same, it is a tie
#The game should ask for their choices
#The game should print out the winner
#The game should ask if they want to play again
#The game should keep a running score
#The game should print out the score
#The game should print out the overall winner
#The game should be able to start a new game
#The game should be able to keep playing until the user quits
#The game should be able to keep playing until the user quits


import random
import sys
import os

def main():
    print("Welcome to Rock, Paper, Scissors!")
    print("The rules are simple: Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.")
    print("You will be playing against the computer.")
    print("Good luck!")
    print("")

    score = {"user": 0, "computer": 0}

    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ")
        user_choice = user_choice.lower()
        computer_choice = random.choice(["rock", "paper", "scissors"])

        print("The computer chose: " + computer_choice)

        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == "rock":
            if computer_choice == "scissors":
                print("You win!")
                score["user"] += 1
            else:
                print("You lose!")
                score["computer"] += 1
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("You win!")
                score["user"] += 1
            else:
                print("You lose!")
                score["computer"] += 1
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print("You win!")
                score["user"] += 1
            else:
                print("You lose!")
                score["computer"] += 1
        else:
            print("Invalid choice. Please try again.")
            continue

        print("The score is now: User " + str(score["user"]) + ", Computer " + str(score["computer"]))
        print("")

        play_again = input("Do you want to play again? (yes/no): ")
        play_again = play_again.lower()
        if play_again != "yes":
            break

    print("The final score is: User " + str(score["user"]) + ", Computer " + str(score["computer"]))
    if score["user"] > score["computer"]:
        print("You are the overall winner!")
    elif score["user"] < score["computer"]:
        print("The computer is the overall winner!")
    else:
        print("It's a tie!")

    print("Thanks for playing!")

if __name__ == "__main__":
    main()

# Run the program
# python app.py
# Welcome to Rock, Paper, Scissors!
#  
