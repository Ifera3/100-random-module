#! python3

# SD Computing Studies Assignment
import random

anser = random.randrange(1,100)
gess = int(input("enter a number betwen 0 and 100: "))
atemps = 1

def hint(num):
    if num < anser:
        print(f"{num} is to small")
    elif num > anser:
        print(f"{num} is to big")

while gess != anser:
    atemps = atemps + 1
    hint(gess)
    gess = int(input("enter a new number betwen 0 and 100: "))
else:
    print(f"you win in {atemps} atemps")