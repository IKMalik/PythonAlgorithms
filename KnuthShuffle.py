import random

def knuthshuffle(data):

    for value in range(0, len(data)):
        randpos = random.randint(0,value)
        print(randpos)
        data[value], data[randpos] = data[randpos], data[value]
        print(data)


knuthshuffle([2,3,4,5,6,7,8])

