#! python3

# SD Computing Studies Assignment
import random

def coin():
    x = random.randrange(1,3)
    if x == 1:
        return "heads"
    elif x == 2:
        return "tails"

def ges(anser):
    gess = input("heads or tails: ")
    if gess == anser:
        print("you win!!")
    else:
        print(f"the anser is {anser}")

def main():
    ges(coin())

main()