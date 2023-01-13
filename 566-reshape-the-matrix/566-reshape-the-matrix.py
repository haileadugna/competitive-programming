class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        if r*c != rows*cols:
            return mat
        temp = []
        for row in range(rows):
            for col in range(cols):
                temp.append(mat[row][col])
        res= []
        temp.reverse()
        for i in range(r):
            ans = []
            for j in range(c):
                ans.append(temp.pop())
            res.append(ans)
        return res
        