class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        price = [float('inf')]* n
        price[src] = 0
        
        for i in range(k + 1):
            temp = price[:]
            
            for start, end, val in flights:
                
                if price[start] == float('inf'):
                    continue
                    
                if price[start] + val < temp[end]:
                    temp[end] = price[start] + val
                    
            price = temp
                    
        
        
        return price[dst] if price[dst] != float("inf") else -1