class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        left, right, n = matrix[0][0], matrix[-1][-1], len(matrix)
        
        def lessTheK(m):
            
            count = 0
            
            for i in range(n):
                
                x = bisect_right(matrix[i], m)
                count += x
                
            return count
        
        while left < right:
            
            mid = (left + right )//2
            
            if lessTheK(mid) < k:
                left = mid + 1
                
            else:
                right = mid
                
        return left