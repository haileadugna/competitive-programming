class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        column = defaultdict(list)
        for i in range(n):
            for j in range(n):
                column[i].append(grid[j][i])
        newcolumn = list(column.values())
        res = 0
        for row in grid:
            for col in newcolumn:
                if row == col:
                    res += 1
        return res