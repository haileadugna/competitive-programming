class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
                
        res = []
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(matrix[j][i])
            res.append(temp)
        return res