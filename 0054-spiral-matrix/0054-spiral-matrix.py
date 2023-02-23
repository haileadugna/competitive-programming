class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m, n = len(matrix), len(matrix[0])
        first_row = 0 
        first_col = 0 
        last_row = m 
        last_col = n 
        res = []
        
        while first_row < last_row and first_col < last_col:
                       
            i = first_col
            while i < last_col:
                res.append(matrix[first_row][i])
                i += 1
            first_row += 1
            
            j = first_row
            while j < last_row:
                res.append(matrix[j][last_col - 1])
                j += 1
            last_col -= 1
            
            if not (first_col < last_col and first_row < last_row):
                break            
            k = last_col -  1
            while k >= first_col :
                res.append(matrix[last_row - 1][k])
                k -= 1
            last_row -= 1
                
            l = last_row - 1
            while l >= first_row:
                res.append(matrix[l][first_col])
                l -= 1
            first_col += 1

        return res   
    
             