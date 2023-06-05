class Solution:
    def rob(self, nums: List[int]) -> int:
        temp1 = 0
        temp2 = 0
        if len(nums) <= 3:
            return max(nums)
        
        for i in range(len(nums)-1):
            temp = max(nums[i] + temp1, temp2)
            temp1 = temp2
            temp2 = temp
#         if the robber start from second house
        tmp1 = 0
        tmp2 = 0
        for i in range(1, len(nums)):
            tmp = max(nums[i] + tmp1, tmp2)
            tmp1 = tmp2
            tmp2 = tmp
        return max(temp2, tmp2)