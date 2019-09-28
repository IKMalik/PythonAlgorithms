
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


UPDATE:
    
    
a = [5, 2, 3, 1, 4]

def mergesort(nums):

  if len(nums) <= 1:
    return nums

  mid = len(nums)//2
  
  left = mergesort(nums[: mid])
  right = mergesort(nums[mid:])

  return partition(left, right)

def partition(left, right):

  result = []
  l = 0
  r = 0

  while l < len(left) and r < len(right):
    if left[l] <= right[r]:
      result.append(left[l])
      l += 1
    else:
      result.append(right[r])
      r += 1
  
  if l < len(left):
    for item in range(l, len(left)):
      result.append(left[item])
  
  if r < len(right):   
    for item in range(r, len(right)):
      result.append(right[item])
  
  return result 

print(mergesort(a))
