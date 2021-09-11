def main ():
    print("this is delaneys work")

def dictprac ():
    uandp= [('user', input()), ('passw', input())]
    usernum1 = dict(uandp)
    print("the username is " + usernum1['user'] + " and the password is " + usernum1['passw'] + "!")

def loopprac (word):                            #simple loop prac
    for x in range(1,10):                   #easist way to make a certain length loop
        print("the value of x is %d" %x)    #%d is integer %s is string
    else:
        print("the value is not in range")  #simple else 
    personname = ['bob', 'sally', 'john']   #list of names
    personage = [12, 25, 46]                #list of ages
    for x in range(len(personname)):        #loop length based on how many names
        print('person name and age', personname[x], personage[x], enumerate[x])

    word = 'dummy'
    while word:
        word = input()
        print('you entered this' , word)
        if word == 'stop':
            break

def caller(loopprac):
    print(loopprac)
