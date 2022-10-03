class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = Counter(nums)
        for i in range(len(nums)):
            if temp[nums[i]] == 1:
                return nums[i]