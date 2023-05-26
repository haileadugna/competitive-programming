class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums) -1
        @cache
        def dp(n):
            
            if n <= 1:
                return nums[n]

            if n ==  2:
                return nums[n] + nums[0]

            return nums[n] + max(dp(n-2), dp(n - 3))
            
        return max(dp(n), dp(n -1))