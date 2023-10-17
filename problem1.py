#! python3

# SD Computing Studies Assignment
import random
import math

def statsa():
    d6_1 = random.randrange(1,7)
    d6_2 = random.randrange(1,7)
    d6_3 = random.randrange(1,7)
    d6_4 = random.randrange(1,7)
    return ((d6_1 + d6_2 + d6_3 + d6_4) - min(d6_1, d6_2, d6_3, d6_4))
    
def statst():
    d6_1 = random.randrange(1,7)
    if d6_1 == 1 or d6_1 == 2:
        d6_1 = random.randrange(1,7)
    d6_2 = random.randrange(1,7)
    if d6_2 == 1 or d6_2 == 2:
        d6_2 = random.randrange(1,7)
    d6_3 = random.randrange(1,7)
    if d6_3 == 1 or d6_3 == 2:
        d6_3 = random.randrange(1,7)
    d6_4 = random.randrange(1,7)
    if d6_4 == 1 or d6_4 == 2:
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
    aorb = input("rolling system a, b or t: ")
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
    elif aorb == "t":
        strength = statst()
        dexterity = statst()
        constitution = statst()
        intelligence = statst()
        charisma = statst()
        wisdom = statst()
    strengthMod = math.floor((strength - 10) / 2)
    if strengthMod >= 0:
        strengthMod = f"+{strengthMod}"
    dexterityMod = math.floor((dexterity - 10) / 2)
    if dexterityMod >= 0:
        dexterityMod = f"+{dexterityMod}"
    constitutionMod = math.floor((constitution - 10) / 2)
    if constitutionMod >= 0:
        constitutionMod = f"+{constitutionMod}"
    intelligenceMod = math.floor((intelligence - 10) / 2)
    if intelligenceMod >= 0:
        intelligenceMod = f"+{intelligenceMod}"
    charismaMod = math.floor((charisma - 10) / 2)
    if charismaMod >= 0:
        charismaMod = f"+{charismaMod}"
    wisdomMod = math.floor((wisdom - 10) / 2)
    if wisdomMod >= 0:
        wisdomMod = f"+{wisdomMod}"
    print(f"your strength is {strength} and your madifier is {strengthMod}, your dexterity is {dexterity} and your madifier is {dexterityMod}, your constitution is {constitution} and your madifier is {constitutionMod}, your intelligence is {intelligence} and your madifier is {intelligenceMod}, your charisma is {charisma} and your madifier is {charismaMod}, your wisdom is {wisdom} and your madifier is {wisdomMod}.")

main()