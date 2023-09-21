class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        n = len(nums)
        target = sum(nums) - x
        window_sum = 0
        j = 0
        res = 0
        found = False
        
        for i in range(n):
            
            window_sum += nums[i]
            
            while j <= i and window_sum > target:
                window_sum -= nums[j]
                j += 1
                
            if window_sum == target:
                res = max(res, i - j  + 1)
                found = True
                
        return n - res if found else -1