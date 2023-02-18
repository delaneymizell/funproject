def deck():
    import random
    deckfull =  [1,2,3]
    pickedcard = deckfull.pop(random.randrange(0,len(deckfull)))
    print("this is the picked card", pickedcard)
    return pickedcard

def hit():
    playerhand()
    print("this is your hand", playerhand())

def playerhand():
    playhand = [1]
    return playhand

if __name__ == "__main__":
    hit()


