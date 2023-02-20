#1,2,3
#4,5,6
#7,8,9
#*,0,#
statement = input()
transfer = {1:9,2:8,3:7,4:6,5:0,6:4,7:3,8:2,9:1,0:5}
for i in statement:
    if i.isnumeric() == True:
        print(i)
        print(transfer[int(i)])
        statement.replace(i,str(transfer[int(i)]))
print(statement)


