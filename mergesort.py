#merge sort

def mergesort(data):

    if (len(data)> 1):
        midpoint = len(data)//2
        fsthalf = data[:midpoint]
        sndhalf = data[midpoint:]

        mergesort(fsthalf)
        mergesort(sndhalf)

        lo = 0
        hi = 0
        pos = 0

        while (lo < len(fsthalf) and hi < len(sndhalf)): # fist half to finish, then add all the remnants in other 2 loops

            if(fsthalf[lo] < sndhalf[hi]):
                data[pos] = fsthalf[lo]
                lo += 1
                pos += 1
                
            else:
                data[pos] = sndhalf[hi]
                hi += 1
                pos += 1

        while lo < len(fsthalf):
            data[pos]=fsthalf[lo]
            lo += 1
            pos += 1

        while hi < len(sndhalf):
            data[pos]=sndhalf[hi]
            hi += 1
            pos += 1
            
    print(str(data))
        
mergesort([4,8, 2, 7, 12,41,1,0,23,1,-1])
