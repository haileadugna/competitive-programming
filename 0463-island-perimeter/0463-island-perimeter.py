class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
#         directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#         visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        
#         def inbound(row, col):
#             return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        
#         def dfs(grid, visited, row, col):
#             # base case
#             visited[row][col] = True
#             for row_change, col_change in directions:
#                 new_row = row + row_change
#                 new_col = col + col_change
                
#                 if inbound(new_row, new_col) and not visited[new_row][new_col]:
#                     dfs(grid, visited, new_row, new_col)


        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        perimeter = 0
        
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        def dfs(grid, visited, row, col):
            nonlocal perimeter
            # base case
            visited[row][col] = True
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                
                if inbound(new_row, new_col) and not visited[new_row][new_col]:
                    if grid[new_row][new_col] == 0:
                        perimeter += 1
                    else:
                        dfs(grid, visited, new_row, new_col)
                elif not inbound(new_row, new_col):
                    perimeter += 1
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j]:
                    dfs(grid, visited, i, j)
        
        return perimeter