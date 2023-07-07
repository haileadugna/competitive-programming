class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        dp = {}
        res = 0
        
        for num in arr:
            
            target = num - difference
            if target not in dp:
                dp[num] = 1
                
            else:
                dp[num] = 1 + dp[target]
                
            res = max(res, dp[num])
        return res
        