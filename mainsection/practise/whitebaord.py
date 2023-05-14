def stringBits(str):
    newstring= ""
    for char in str:
        if i % 2 == 0:
            newstring+= char
        i+=1
    print(newstring)

stringBits('Hello') # 'Hlo'
stringBits('Hi') # 'H'
stringBits('Heeololeo') # 'Hello'