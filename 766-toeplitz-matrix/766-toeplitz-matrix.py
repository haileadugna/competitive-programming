class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        
        left = m-1
        start = 0
        
        while left > 0:
            
            i, j = left, 0
            temp =  matrix[i][j]
            while i < m-1 and j < n-1:
                i += 1
                j += 1
                if temp != matrix[i][j]:
                    return False
            left -= 1
            
        while start < n :
            
            i, j = 0, start
            temp =  matrix[i][j]
            while i < m-1 and j < n-1:
                i += 1
                j += 1
                if temp != matrix[i][j]:
                    return False
            start += 1
        return True        
        
        
        
        
        
        
            
            