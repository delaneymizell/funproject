import random
import os
#game = True
#while game == True: 
def deck():
    fulldeck = [2,3,4,5,6,7,8,9,10,"j","q","k","a"] * 4

def hit(x):
    randcard = x[random.randrange(0,len(x))]
    return randcard

def dealerhand():
    dhand = []
    return dhand

def playerhand():
    phand = []
    return phand

def sumhand(x):
    sum = 0
    for i in x:
        if type(i) == int:
            sum += i
        else:
            if i == "j"or"q"or"k":
                sum += 10
            else:
                if sum < 11:
                    sum += 11
                else: 
                    sum += 1
    return sum

def dealerchoice():
    dealerhand()
    





randcard = deck[random.randrange(0,len(deck))]
deck.remove(randcard)
dealer = []
dealertotal = []
player = []
playertotal = []


dealer.append(randcard)
randcard = deck[random.randrange(0,len(deck))]
deck.remove(randcard)
dealer.append(randcard)
dealertotal = sum(dealer)
print("dealers hand is ", dealertotal ,dealer)