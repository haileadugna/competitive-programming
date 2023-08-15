class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        res = nums[0]
        summ = nums[0]
        
        for i in range(1, len(nums)):
            
            summ += nums[i]
            mat = math.ceil(summ/(i + 1))
            
            res = max(res, mat)
            
        return res