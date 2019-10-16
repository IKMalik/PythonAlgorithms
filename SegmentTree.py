class Node:
    
    def __init__(self, lo, hi):
        
        self.lo = lo
        self.hi = hi
        self.left = None
        self.right = None
        self.value = None


class NumArray:

    def __init__(self, nums: List[int]):
        
        if nums is None or len(nums) < 1:
            return 
        
        self.root = self.buildTree(nums, 0, len(nums)-1)
        
        
    def buildTree(self, nums, lo, hi):
        
        if lo == hi:
            node = Node(lo, hi)
            node.value = nums[hi]
            return node
        
        mid = (hi+lo)//2
        
        node = Node(lo, hi)
        
        node.left = self.buildTree(nums, lo, mid)
        node.right = self.buildTree(nums, mid+1, hi)
        
        node.value = node.left.value + node.right.value
        
        return node
        
        
    def update(self, i: int, val: int) -> None:
        
        self.changeVal(self.root, i, val)
    
    def changeVal(self,node, index, value):
        
        if node.lo == node.hi:
            node.value = value
            return
        
        mid = (node.lo+node.hi)//2
        
        if index <= mid:
            self.changeVal(node.left, index, value)
        else:
            self.changeVal(node.right, index, value)
        
        node.value = node.left.value + node.right.value
        return
        
    def sumRange(self, i: int, j: int) -> int:
        
        return self.rangeSum(self.root, i, j)
    
    def rangeSum(self, node, lo, hi):
        
        if node.lo == lo and node.hi == hi:
            return node.value
        
        mid = (node.lo+node.hi)//2
        
        if lo > mid:
            return self.rangeSum(node.right, lo, hi)
        
        elif hi <= mid:
            return self.rangeSum(node.left, lo, hi)
        
        else:
            return self.rangeSum(node.left, lo, mid) + self.rangeSum(node.right, mid+1, hi)
        
        
