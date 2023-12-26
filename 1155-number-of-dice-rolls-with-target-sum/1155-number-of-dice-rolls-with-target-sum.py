class Solution:
    

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        dp = [[-1] * (target + 1) for _ in range(n + 1)]
        mod = 10 ** 9 + 7

        def recursion(dp, n, k, target):
            if target == 0 and n == 0:
                return 1
            if n == 0 or target <= 0:
                return 0

            if dp[n][target] != -1:
                return dp[n][target]

            ways = 0
            for i in range(1, k + 1):
                ways = (ways + recursion(dp, n - 1, k, target - i)) % mod

            dp[n][target] = ways % mod
            
            return dp[n][target]
        
        return recursion(dp, n, k, target)