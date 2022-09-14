class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        n = len(mat)
        m = n//2
        for i in range(n):
            ans += (mat[i][i] + mat[i][n-i-1])
        if len(mat)%2 == 0:
            return ans
        else:
             return ans - mat[m][m]   