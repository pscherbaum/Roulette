#!/usr/bin/env python3


import random
import sys


# mit so viel Geld starte ich
geld = 10000

zufall_0 = 0
zufall_1 = 0



def zufall_0_1():
    return round(random.random())



# spielen solange Geld vorhanden ist
while geld > 0:
    print (geld)
    geld -= 1
    zufall = zufall_0_1()
    if (zufall == 0):
        zufall_0 += 1
    elif (zufall == 1):
        zufall_1 += 1
    else:
        print("Zufallszahl stimmt nicht: ", zufall)
        sys.exit(1)


print("0: ", zufall_0)
print("1: ", zufall_1)
