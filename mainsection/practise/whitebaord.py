main = [1,2,3,4,5]
for i in range(main -1):
    while main[i] < main[i+1]:
        main[i],main[i+1]= main[i+1],main[i]
print(main)