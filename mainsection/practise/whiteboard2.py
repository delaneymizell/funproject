def go():
    megalist = [1,2,3]
    appendlist(megalist)
    print(megalist)

def hand(n):
    n = sum()

def appendlist(m):
    thing = [1,2,3,"q","k"]
    sum = 0
    for i in thing:
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

    
    test = [1,2,3,"a"]
    sum = 0
    for i in test:
        if type(i) == int:
            sum += i
            print(sum)
        else:
            sum+=10
    print(sum)



if __name__ == "__main__":
    go()
