#! python3

# SD Computing Studies Assignment
import random

def cpu():
    x = random.randrange(1,6)
    if x == 1:
        return "rock"
    elif x == 2:
        return "paper"
    elif x == 3:
        return "scissors"
    elif x == 4:
        return "lizard"
    elif x == 5:
        return "spock"

def play(oponet):
    player = input("enter rock, paper, scissors, lizard or spock: ")
    print(oponet)
    if player == oponet:
        print("tie")
    else:
        if player == "rock":
            if oponet == "paper":
                print("you loss")
            elif oponet == "scissors":
                print("you win!!")
            elif oponet == "lizard":
                print("you win!!")
            elif oponet == "spock":
                print("you loss")
        elif player == "paper":
            if oponet == "rock":
                print("you Win!!")
            elif oponet == "scissors":
                print("you lose")
            elif oponet == "lizard":
                print("you lose")
            elif oponet == "spock":
                print("you win!!")
        elif player == "scissors":
            if oponet == "rock":
                print("you loss")
            elif oponet == "paper":
                print("you win!!")
            elif oponet == "lizard":
                print("you win!!")
            elif oponet == "spock":
                print("you loss")
        elif player == "lizard":
            if oponet == "rock":
                print("you loss")
            elif oponet == "paper":
                print("you win!!")
            elif oponet == "scissors":
                print("you loss")
            elif oponet == "spock":
                print("you win!!")
        elif player == "spock":
            if oponet == "rock":
                print("you win!!")
            elif oponet == "paper":
                print("you lose")
            elif oponet == "scissors":
                print("you Win!!")
            elif oponet == "lizard":
                print("you loss")

play(cpu())