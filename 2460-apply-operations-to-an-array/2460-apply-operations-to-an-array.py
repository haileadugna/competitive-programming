class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
            
        res  = []
        for j in range(len(nums)):
            if nums[j] != 0:
                res.append(nums[j])
                
        while len(res) < len(nums):
            res.append(0)
        return res