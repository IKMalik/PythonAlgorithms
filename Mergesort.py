
def mergesort(data):

    if len(data) <= 1:
        return data
    mid = len(data)//2
    left = mergesort(data[:mid])
    right = mergesort(data[mid:])
    return merge(left, right)
  
def merge(left, right):

    aux = []
    i = j = 0

    while i < len(left) and j < len(right):
      if left[i] <= right[j]:
        aux.append(left[i])
        i += 1
      else:
        aux.append(right[j])
        j += 1
       
    # DO THE FOR LOOPS NOT THIS TO IMPROVE MEMORY COST
    if i < len(left):
        aux += left[i:]

    else:
        aux += right[j:]
    
    return aux

arr = [12, 11, 13, 5, 6, 7]  
print(mergesort(arr))
