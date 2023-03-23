class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        left = 0
        while left < len(nums):
            while nums[left] < len(nums) and nums[left] != left + 1 and nums[left] != nums[nums[left] - 1]:
                temp = nums[nums[left] - 1]
                nums[nums[left] - 1] = nums[left]
                nums[left] = temp
            left += 1
        # print(nums)   
        res = []
        temp = []
        for i in range(len(nums)):
            if i + 1 != nums[i] and i + 1 not in temp:
                res.append(i + 1)
                temp.append(nums[i])
     
        return res