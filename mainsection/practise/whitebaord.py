def func1():
    shitlist = [1,2,"shit"]
    return shitlist

def func2():
    import random
    addnum = random.randrange(0,10)
    return addnum

def func3(func1):
    func1.append(func2())
    print("this is append" ,func1)
    return func1

def func4():
    print("before", func1())
    func3(func1())
    print("after", func1())
if __name__ == "__main__":
    func4()()