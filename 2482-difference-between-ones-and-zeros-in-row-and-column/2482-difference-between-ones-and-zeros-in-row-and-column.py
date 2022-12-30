class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(grid)
        m = len(grid[0])
        temp1 = []
        temp2 = []
        for row in range(len(grid)):
            temp1.append(sum(grid[row]))
            
        # if n < m:
        i = 0

        while i < m:
            summ = 0
            j =0
            while j < n:
                summ += grid[j][i]
                j += 1
            i += 1
            temp2.append(summ)
#         if n >= m:
#             i = 0
            
#             while i < m:
#                 j =0
#                 summ = 0
#                 while j < n:
#                     summ += grid[j][i]
#                     j += 1
#                 i += 1
#                 temp2.append(summ)

        for i in range(n):
            ans = []
            for j in range(m):
                diff = temp1[i] + temp2[j] - (n-temp1[i] + (m-temp2[j]))
                ans.append(diff)
            res.append(ans)
        return res
                