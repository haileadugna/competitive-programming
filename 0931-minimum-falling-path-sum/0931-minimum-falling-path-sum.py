class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        for i in range(1, n):
            for j in range(n):
                
                if j -1 >= 0:
                    left = matrix[i-1][j-1] 
                else: 
                    left = float("inf")
                if j+1 <n:
                    right = matrix[i-1][j+1] 
                else: 
                    right = float('inf')
                center = matrix[i-1][j]
                matrix[i][j] += min(left, right, center)
                
                
        return min(matrix[-1])