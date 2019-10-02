class SegmentNode:

  def __init__(self, start, end):

    self.value = 0
    self.start = start
    self.end = end
    self.left = None
    self.right = None

class SegmentTree:

  def __init__(self, nums):

    self.root = self.buildTree(nums, 0, len(nums)-1)

  
  def buildTree(self, nums, lo, hi):

    if lo > hi:
      return None
    
    if lo == hi:
      curr = SegmentNode(lo, hi)
      curr.value = nums[lo]
      return curr
    
    mid = (lo + hi)//2

    curr = SegmentNode(lo, hi)
    curr.left = buildTree(lo, mid)
    curr.right = buildTree(mid+1, hi)

    curr.value = curr.left.value + curr.right.value

    return curr
    
