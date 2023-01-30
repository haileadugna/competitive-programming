class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = []
        
        start = 0
        while start < n-2:
            ans = []
            for i in range(n-2):
                temp = 0
                for j in range(start , start +3):
                    check = 0
                    for k in range(i, i +3):
                        check = max(check, grid[j][k])
                    temp = max(check,temp)
                ans.append(temp)
            res.append(ans)
            start += 1
        return res