class Solution:
    def rob(self, nums: List[int]) -> int:
        
        temp1 = 0
        temp2 = 0
        for i in range(len(nums)):
            temp = max(nums[i] + temp1, temp2)
            temp1 = temp2
            temp2 = temp
        return temp2
#         n = len(nums) -1
#         @cache
#         def dp(n):
            
#             if n <= 1:
#                 return nums[n]

#             if n ==  2:
#                 return nums[n] + nums[0]

#             return nums[n] + max(dp(n-2), dp(n - 3))
            
#         return max(dp(n), dp(n -1))