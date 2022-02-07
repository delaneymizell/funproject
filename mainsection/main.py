import os
import datetime as datetime

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
def abstractionprac():
    print(loopprac('dog'))

def lastindexof():
    string1 = ("test.yaml.file.csv")
    indexofperiod = string1.rindex(".") + 1
    filetype = string1[indexofperiod:len(string1)]
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
    x= 1 
    y = '1'
    if x:
        print('xyeet')
    if y:
        print('yyeet')

def minustest():
    name = 'delaney'
    newname = name[:-1] 
    print(name + ' ' + newname)

