class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        
        
        maxx, minn = max(nums), min(nums)
        
        diff, val = maxx - minn, 2*k
        
        if diff <= val:
            return 0
        
        else:
            return diff - val
            
            