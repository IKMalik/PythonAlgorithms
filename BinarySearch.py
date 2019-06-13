# RECURSIVE IMPLEMENTATION

class BinarySearch:

  def __init__(self, data):

    self.data = data
  
  def search(self, key):

    return _search(0, len(self.data)-1, key)

  def _search(lo, hi, key):

    if hi < lo:
      return False
    
    mid = (hi + lo)//2 

    if key === self.data[mid]:
      return True
    elif key < self.data[mid]:
      return self._search(0, mid-1, key)
    else:
      return self._search(mid+1, len(sel.data)-1, key)

# ITERATIVE IMPLEMENTATION

class BinarySearch:

  def __init__(self, data):

    self.data = data
  
  def search(self, key):

    lo = 0
    hi = len(self.data)-1
    while hi > lo:

      mid = (hi+lo)//2

      if key == self.data[key]:
        return True
      elif key < self.data[key]:
        hi = mid-1
      else:
        lo = mid+1 
    return False
