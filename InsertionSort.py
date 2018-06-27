
def InsertionSort(arrayvals):
        for i in range (0, len(arrayvals)):
                j = i 
                while (j>0):
                        if (arrayvals[j-1] > arrayvals[j]):
                                tempval = arrayvals[j]
                                arrayvals[j] = arrayvals[j-1]
                                arrayvals[j-1] = tempval
                        j-=1
        print (str(arrayvals))

InsertionSort([54,26,93,17,77,31,44,55,20])
