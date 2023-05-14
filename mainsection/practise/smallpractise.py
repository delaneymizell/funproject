def givendate():
    ###print out a date given year month and day as numbers in simple format
    date = "07/04/1997"
    months = ["Jan","Mar","Feb","Apr","May","Jun","Jul","Aug","Sep","Nov","Oct","Dec"]
    dates = date.split("/",2 )
    month = months[(int(dates[0]))-1]
    year = dates[2]
    day = date[1]
    print("the date is the " + day + " of " + month + " in year " + year)

    