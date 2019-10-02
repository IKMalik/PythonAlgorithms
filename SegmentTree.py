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

    # if given empty list
    if lo > hi:
      return None
    
    #non empty list base case
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
  
  def sumRange(self, lo, hi):

    return _sumRange(self.root, lo, hi)
  
  def _sumRange(node, lo, hi):

    # base case
    if node.start == lo and node.end == hi:
      return node
    
    # 3 cases
