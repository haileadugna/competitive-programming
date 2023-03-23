class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left = 0
        while left < len(nums):
            while nums[left] < len(nums) and nums[left] != left:
                temp = nums[nums[left]]
                nums[nums[left]] = nums[left]
                nums[left] = temp
            left += 1
        print(nums)   
        res = len(nums)
        for i in range(len(nums)):
            if i != nums[i]:
                res = i

        return res