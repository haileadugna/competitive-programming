class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n, m = len(mat[0]), len(mat)
        t = r*c
        if m*n != t:
            return mat
        ans = [[0 for _ in range(c)] for _ in range(r)]
        k = 0
        tmp =[]
        for b in range(m):
            for l in range(n):
                tmp.append(mat[b][l])
        for i in range(r):
            for j in range(c):
                ans[i][j] = tmp[k]
                k +=1
        return ans