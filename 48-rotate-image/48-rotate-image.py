class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for i in range(n//2):
            for j in range(i, n-i-1):
             
                temp = matrix[i][j]
                # matrix(i,j)
                a, b = i, j
                a,b = b, a
                b = n - b -1
                temp1 = matrix[a][b]
                matrix[a][b] = temp
              
                #matrix(a,b)
                c, d = a, b
                c,d = d, c
                d = n - d - 1
                temp2 = matrix[c][d]
                matrix[c][d] = temp1
            
                #mtric(c,d)
                a, b = c, d
                a,b = b, a
                b = n - b- 1
                temp3 = matrix[a][b]
                matrix[a][b] = temp2
          
                #matrix(a,b)
                c, d = a, b
                c,d = d, c
                d = n - d - 1
                matrix[c][d] = temp3
            
            