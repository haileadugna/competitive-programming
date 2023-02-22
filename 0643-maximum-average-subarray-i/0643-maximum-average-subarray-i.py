class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        start = 0
        end = k
        max_sum = sum(nums[:k])
        
        prev = max_sum
        
        while end < len(nums):
            max_sum -= nums[start]
            max_sum += nums[end]
            prev = max(max_sum, prev)
            end += 1
            start += 1
            
        return prev/k
            
            
        