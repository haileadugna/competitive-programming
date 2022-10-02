class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = 0
        ans = nums[0]
        for i in nums:
            if temp < 0:
                temp = 0
            temp += i
            ans = max(ans, temp)
        return ans
