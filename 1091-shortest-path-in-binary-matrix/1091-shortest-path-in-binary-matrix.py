class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] :
            return -1
        q = collections.deque([(0,0,1)])
        dir = [(0,1), (0,-1), (1,0),(-1, 0), (1,1), (1,-1),(-1,1), (-1,-1)]
        grid[0][0] = 1
        while q :
            x,y,path = q.popleft()
            if (x,y) == (len(grid)-1, len(grid[0])-1):
                return path
            for i, j in dir:
                newi = x + i
                newj = y + j
                if (0 <= newi < len(grid)) and (0 <= newj < len(grid[0])) and not grid[newi][newj]:
                    grid[newi][newj] = 1
                    q.append((newi, newj, path + 1))
        return -1