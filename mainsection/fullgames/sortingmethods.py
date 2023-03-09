import random

def main():
    finallist = [1,2,3,4,5,6,7,8,9]
    scrambled = [1,2,3,4,5,6,7,8,9]
    random.shuffle(scrambled)

    bubble(scrambled,finallist)
    
def bubble(scram, final):
    actions = 0
    while scram != final:
        for i in scram:
            actions +=1
            if i < i+1:
                i = i+1
    return actions
                
if __name__ == "__main__":
    main()