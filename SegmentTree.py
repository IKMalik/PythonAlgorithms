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
    curr.left = self.buildTree(nums, lo, mid)
    curr.right = self.buildTree(nums, mid+1, hi)

    curr.value = curr.left.value + curr.right.value

    return curr
  
  def sumRange(self, lo, hi):

    return self._sumRange(self.root, lo, hi)
  
  def _sumRange(self, node, lo, hi):

    # base case
    if node.start == lo and node.end == hi:
      return node.value

    mid = (hi + lo)//2 #WRONG vs node.start and node.end


    # 3 cases
    if hi <= mid:
      return self._sumRange(node.left, lo, hi)
    
    elif lo > mid:
      return self._sumRange(node.right, lo, hi)
    
    else:
      return self._sumRange(node.left, lo, mid) + self._sumRange(node.right, mid+1, hi)


a = SegmentTree([2,6,8,1,2,3,4])
print(a.sumRange(0, 6))
