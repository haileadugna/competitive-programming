class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        
        
        @cache
        def dfs(i, remain):
            
            if remain <= 0 :
                return 0
            
            if i == len(cost):
                return float('inf')
            
            paid = cost[i] + dfs(i + 1, remain - 1 - time[i])
            skip = dfs(i + 1, remain)
            
            return min(paid, skip)
        
        return dfs(0, len(time))