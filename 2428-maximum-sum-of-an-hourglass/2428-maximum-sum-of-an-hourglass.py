class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        c = copy.deepcopy(n)
        l = 0
        r = 3
        t, b = 0, 2
        ans = []
        while m > b:
            while n >= r :
                temp = sum(grid[t][l:r]) + grid[t+1][l+1] + sum(grid[b][l:r])
                ans.append(temp)
                l += 1
                r += 1
            t += 1
            b += 1
            l,r= 0,3
        return max(ans)