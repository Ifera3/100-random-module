#! python3

# SD Computing Studies Assignment

#Create a list that contains a deck of cards. Shuffle and deal 5 card hands to 2 different players. You may want to make use of the list commands we have previously explored to remove cards when they have been dealt to players.
import random

def play():
    number = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    siuts = ['spades','clubs','hearts','dimonds']
    dec = []
    plyer1 = []
    plyer2 = []
    for i in siuts:
        for a in number:
            dec.append(f'{a} {i}')
    random.shuffle(dec)
    for i in range(5):
        plyer1.append(dec[0])
        dec.remove(plyer1[i])
    for i in range(5):
        plyer2.append(dec[0])
        dec.remove(plyer2[i])
    print(plyer1)
    print(plyer2)

play()