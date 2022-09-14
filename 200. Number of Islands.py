class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        island = 0
        def check(r,c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                dirr = [[1,0], [-1,0],[0,1],[0,-1]]
                for rr, cc in dirr:
                    r, c = row + rr, col +cc
                    if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visit:
                        q.append((r,c))
                        visit.add((r,c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    check(r,c)
                    island += 1
        return island
                    