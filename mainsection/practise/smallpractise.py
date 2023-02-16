def givendate():
    ###print out a date given year month and day as numbers in simple format
    date = "07/04/1997"
    months = ["Jan","Mar","Feb","Apr","May","Jun","Jul","Aug","Sep","Nov","Oct","Dec"]
    dates = date.split("/",2 )
    month = months[(int(dates[0]))-1]
    year = dates[2]
    day = date[1]
    print("the date is the " + day + " of " + month + " in year " + year)

def cardgame():
    import random
    game = True
    while game == True: 
        deck = [2,3,4,5,6,7,8,9,10,"j","q","k","a"] * 4
        randcard = deck[random.randrange(0,len(deck))]
        print(deck + randcard)
        import random
        rand = random(0,20)
        print(rand)
    