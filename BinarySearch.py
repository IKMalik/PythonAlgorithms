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
