#! python3

# SD Computing Studies Assignment
import random


def stats():
    d6_1 = random.randrange(1,7)
    d6_2 = random.randrange(1,7)
    d6_3 = random.randrange(1,7)
    return (d6_1 + d6_2 + d6_3)

def main():
    strength = stats()
    dexterity = stats()
    constitution = stats()
    intelligence = stats()
    charisma = stats()
    wisdom = stats()
    print(f"your strength is {strength}, your dexterity is {dexterity}, your constitution is {constitution}, your intelligence is {intelligence}, your charisma is {charisma}, your wisdom is {wisdom}.")

main()