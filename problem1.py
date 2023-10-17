#! python3

# SD Computing Studies Assignment
import random

def statsa():
    d6_1 = random.randrange(1,7)
    d6_2 = random.randrange(1,7)
    d6_3 = random.randrange(1,7)
    d6_4 = random.randrange(1,7)
    return ((d6_1 + d6_2 + d6_3 + d6_4) - min(d6_1, d6_2, d6_3, d6_4))

def statsb():
    d6_1 = random.randrange(1,7)
    if d6_1 == 1:
        d6_1 = random.randrange(1,7)
    d6_2 = random.randrange(1,7)
    if d6_2 == 1:
        d6_2 = random.randrange(1,7)
    d6_3 = random.randrange(1,7)
    if d6_3 == 1:
        d6_3 = random.randrange(1,7)
    return (d6_1 + d6_2 + d6_3)

def main():
    aorb = input("rolling system a or b: ")
    if aorb == "a":
        strength = statsa()
        dexterity = statsa()
        constitution = statsa()
        intelligence = statsa()
        charisma = statsa()
        wisdom = statsa()
    elif aorb == "b":
        strength = statsb()
        dexterity = statsb()
        constitution = statsb()
        intelligence = statsb()
        charisma = statsb()
        wisdom = statsb()
    print(f"your strength is {strength}, your dexterity is {dexterity}, your constitution is {constitution}, your intelligence is {intelligence}, your charisma is {charisma}, your wisdom is {wisdom}, ")

main()