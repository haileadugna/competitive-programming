class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        sum = 0
        
        for ele in grid:
            low = 0
            high = len(ele) -1
            while low <= high:
                mid = (high + low)//2
                if ele[mid] < 0:
                    high = mid -1
                elif ele[mid] >= 0:
                    low = mid + 1
            sum += len(ele) - low
        return sum
                    
            
            