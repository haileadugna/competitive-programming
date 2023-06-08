class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            nums[i] = [nums[i], i]
        
        nums.sort()
        
        start = 0
        end = len(nums) -1
        
        while start < end:
            
            if nums[end][0] + nums[start][0] > target:
                end -= 1
                
            elif nums[end][0] + nums[start][0] < target:
                start += 1
                
                
            else:
                return [nums[start][-1], nums[end][-1]]