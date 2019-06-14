
def quicksort(data):

    if len(data) < 2:
        raise ValueError("Too few items to sort ")

    else:
        quicksorthelper(data, 0, len(data)-1)


def quicksorthelper(data, lo, hi):
    
    if lo < hi:
        splitpoint = partition(data, lo, hi)
        quicksorthelper(data, lo, splitpoint-1)
        quicksorthelper(data, splitpoint+1, hi)


    
def partition(data, lo, hi):
    
    pivotval = data[lo]
    leftmark = lo+1
    rightmark = hi
    
    complete = False
    while not complete:

        while leftmark <= rightmark and data[leftmark] <= pivotval: # why < rightmark instead of < hi
            leftmark += 1
        

        while rightmark >= leftmark and data[rightmark] >= pivotval: # why > leftmark mark instead of > lo
            rightmark -= 1

        if rightmark < leftmark:
            complete = True

        else:
            data[leftmark], data[rightmark] = data[rightmark], data[leftmark]

    data[lo], data[rightmark] = data[rightmark], data[lo]
    return rightmark

    
alist = [54,26,93,55,77,31,44,55,20]
quicksort(alist)
print(alist)


