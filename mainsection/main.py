
import os
import datetime as datetime

def main ():
    print("this is delaneys work")

def dictprac ():
    uandp= [('user', input()), ('passw', input())]
    usernum1 = dict(uandp)
    print("the username is " + usernum1['user'] + " and the password is " + usernum1['passw'] + "!")

def loopprac ():                            #simple loop prac
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

def abstractprac(words):
    totalnum =  words + 'end'
    return totalnum

def abstractcaller(): # fixed this abstration prac but sill need to comment it out for it to work
    words = input()
    abstractprac(words)

def lastindexof():
    string1 = ("test.yaml.file.csv")
    filetype = string1[(string1.rindex(".") + 1):len(string1)]
    print(filetype)

def testy():
    name = "john"
    name2 = "john is bad"
    print(name2.isalpha())

def timetest():
    import datetime as datetime
    import time as time
    oldtime = datetime.datetime.now()
    time.sleep(3)
    nowtime = datetime.datetime.now()
    print(oldtime)
    print(nowtime)
    difftime = nowtime - oldtime
    if oldtime < nowtime:
        print("old time time bigger by more than 2 seconds")
        print(difftime)
    #elif nowtime > currenttime: 
     #   print("now bigger than current")
    else:
        print("something broke")

    print(nowtime)

def timetest2():
    import datetime as datetime
    now = "12/15/21 14:00"
    truedate = datetime.datetime.strptime(now, '%m/%d/%y %H:%M')
    timenow = datetime.datetime.now()
    print(now)
    print(truedate)
    if truedate < timenow:
        print("notbased")
    else:
        print("based")

def trytests():
    x = 2
    try:
         x +=3 
    except Exception as e: 
        print("poop")
    print(x)

if __name__ == "__main__":
    print(timetest)
    
def filereader():
    from pathlib import Path
    testpath = "funproject/"
    folder_loc = Path("C:/Users/delan/Documents/codebases/" + testpath + "testdoc.txt")
    f = open(folder_loc)
    print(f.read())

def functest():
    x = 1 
    y = '1'
    if x:
        print(x + 'yeet')
    if y:
        print(y + 'yeet')

def slicing():
    name = 'delaney'
    sliced = name[:-2] 
    print(name + ' ' + sliced)
    numbers = [1,2,3,4,5,6,7,8,9,10]
    ### [firstindex:lastindex:skiping(if neg go backwards)]
    number = numbers[0::2]
    backnum = numbers[:0:-2]
    print(number)
    print(backnum)

def split():
    name = "d.e.l.a.n.e.y"
    letters = name.split(".")
    full = ""
    for i in letters:
        full += i
    print(letters)
    print(full)

def multiplylist():
    name = "delaney"
    multiplied = name * 5 
    Nonelist = [None] * 5
    print(multiplied)
    print(Nonelist)

def containin():
    sentence = "Delaney is the best"
    'is the best' in sentence
    names = ["delaney","notdelaney"]
    input('enter your name: ') in names 

def lengthminmax():
    numbers =[3,7,10]
    print(len(numbers), min(numbers), max(numbers) )

def lists():
    letters = list('delaney')
    print(letters)
    name="".join(letters) #turns it back into object
    print(name)
    del letters[0]  #removes first index
    print(letters) 
    letters[:0] = ["D"] #replaces first index
    print(letters)
    letters.append("!") #pends on end
    letters.count("e") # check count 
    letters.extend("!!!") #can be used to combine different lists
    letters.index("e") #check index 
    letters.insert(0,"!") #inserts in index of
    letters.pop() #returns last element and removes it
    letters.remove("e") # takes first element out
    letters.reverse() #puts the list backwards
    reversed(letters) #only returns list backwards
    letters.sort() # sorts the list by number or by alphabet
    letters.sort(len()) #sorts the elements by length 
    letters.sort(reverse=True)
    newname = letters.clear() #clears list
