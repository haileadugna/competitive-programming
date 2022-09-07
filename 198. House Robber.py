class Solution:
    def rob(self, nums: List[int]) -> int:
        temp1 = 0
        temp2 = 0
        for i in range(len(nums)):
            temp = max(nums[i] + temp1, temp2)
            temp1 = temp2
            temp2 = temp
        return temp2