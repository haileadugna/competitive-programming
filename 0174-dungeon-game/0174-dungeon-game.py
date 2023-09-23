class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        n = len(dungeon)
        m = len(dungeon[0])
        dp = [[0 for i in range(len(dungeon[0]))] for j in range(len(dungeon))]
        for i in range(n-1, -1, -1):
            for j in range(m-1,-1, -1):
                
                if i == n -1 and j == m -1:
                    dp[i][j] = min(0, dungeon[i][j])
                elif i == n -1:
                    dp[i][j] = min(0, dungeon[i][j] + dp[i][j+1])
                    
                elif j == m -1:
                    dp[i][j] = min(0, dungeon[i][j] + dp[i +1][j])
                    
                else:
                    dp[i][j] = min(0, max(dp[i][j+1], dp[i+1][j]) + dungeon[i][j])
                    
        print(dp)
                    
        return abs(dp[0][0]) + 1
                
                
                