class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        prev = [poured]
        
        for i in range(1, query_row + 1):
            
            cur = [0] * (i +1)
            for j in range(i):
                
                cur[j] += .5 * max(prev[j] -1, 0)
                cur[j+1] += .5 * max(prev[j] -1, 0)
                
            prev = cur
                
        return min(1, prev[query_glass])