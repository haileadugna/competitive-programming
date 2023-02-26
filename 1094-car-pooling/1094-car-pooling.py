class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        prefix = [0]*1001
        
        for trip in trips:
            
            prefix[trip[1]] += trip[0]
            prefix[trip[2]] -= trip[0]
            
        for i in range(1, len(prefix)):
            
            prefix[i] += prefix[i-1]
        
        # print(prefix)
        if max(prefix) > capacity:
            return False
        return True