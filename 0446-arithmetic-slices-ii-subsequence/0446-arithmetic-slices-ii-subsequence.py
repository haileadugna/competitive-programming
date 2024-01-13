class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res,  n = 0, len(nums)
        
        dp = [defaultdict(int) for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                
                dp[i][diff] += 1 + dp[j][diff]
                res += dp[j][diff] 
                # print(res, dp[i][diff])
        # print(dp)
        return res