class Solution:
    def integerBreak(self, n: int) -> int:
        
        if n <= 3:
            return n - 1
        
        dp = [0] * (n+1)
        for i in range(4):
            dp[i] = i 
            
        for num in range(4, n + 1):
            temp = num
            
            for j in range(num + 1):
                
                temp = max(temp, j * dp[num - j])
                
            dp[num] = max(num, temp)
                
        # print(dp)
        return dp[n]