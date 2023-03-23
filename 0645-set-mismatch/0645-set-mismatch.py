class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        left = 0
        while left < len(nums):
            while nums[left] != left + 1 and nums[left] != nums[nums[left] - 1]:
                temp = nums[nums[left] - 1]
                nums[nums[left] - 1] = nums[left]
                nums[left] = temp
            left += 1
        print(nums)
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                res = [nums[i], i + 1]
     
        return res