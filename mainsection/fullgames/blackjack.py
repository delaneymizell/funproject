#this is an incredibly crude rendition of blackjack
#the goal of this game was to pactise lists and functions
#i learned alot about how to pass arguments through functions
#but most imporntly that python is a pass by argument language so it was difficult
#if any poor soul actuualy reads then and has any optimizations please let me know
import random
import os

def hit(person,deck):
    pickedcard = deck.pop(random.randrange(0,len(deck)))
    person.append(pickedcard)
    return person
        
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

def fullgame():
    fulldeck = [2,3,4,5,6,7,8,9,10,"j","q","k","a"] * 4
    playerhand = []
    dealerhand = []
    print("----------lets begin the game----------")
    hit(playerhand,fulldeck),hit(playerhand,fulldeck),hit(dealerhand,fulldeck)
    print("your first two cards are ", playerhand," for a total of ", sumhand(playerhand))
    print("the dealers face up card is ", dealerhand," for a total of ", sumhand(dealerhand))
    while True: 
        if sumhand(playerhand) > 21:
            print("you have busted loser ", playerhand)
            gameover()
        choice = input("would you like to hit? y/n")
        if choice == "y":
            hit(playerhand,fulldeck)
            print("Your hand is now ", playerhand, " for a total of ", sumhand(playerhand))
        else:
            break
    print("the dealers second card is ", hit(dealerhand,fulldeck), " for a total of ", sumhand(dealerhand))
    while True:
        if sumhand(dealerhand) < 17:
            print("the dealer hit ", hit(dealerhand,fulldeck), " for a total of ", sumhand(dealerhand))
        if sumhand(dealerhand) > 21:
            print("the dealer has busted you win")
            gameover()
        else:
            break
    if sumhand(playerhand) > sumhand(dealerhand):
        print("You have won congradulations")
        gameover()
    elif sumhand(playerhand) < sumhand(dealerhand):
        print("you lost you big loser")
        gameover()
    elif sumhand(playerhand) == sumhand(dealerhand):
        print("it is a tie and we all go home happy")
        gameover()
    else:
        print("bad programming")
        gameover()
    
def gameover():
    x = input("game is over, would you like to play again? y/n")
    if x == "y" or "Y":
        fullgame()
    else:
        print("??????????")

if __name__ == "__main__":
    fullgame()