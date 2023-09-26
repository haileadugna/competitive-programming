class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        sum_stone = sum(stones)
        target = (sum_stone + 1)//2
        
        dp = {}
        def dfs(i, total):
            # print(dp)
            if total >= target or i == len(stones):
                
                return abs(total - (sum_stone - total))
            
            if (i,  total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = min(dfs(i + 1, total), dfs(i+1, total + stones[i]))
            
            return dp[(i, total)]
            
        return dfs(0,0)