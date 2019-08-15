Kadane's Algorithm modified for max subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if nums is None:
            return 0
        
        curr_max = float('-inf')
        result = nums[0]
        
        
        for val in nums:
            curr_max = max(val, val + curr_max)
            
            result = max(result, curr_max)
        
        return result
            
