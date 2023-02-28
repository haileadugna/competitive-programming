class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        
        grid = [[0]*n for _ in range(n)]
        # print(gird)
        for querie in queries:
            grid[querie[0]][querie[1]] += 1
            if querie[2] < n - 1 and querie[3] < n - 1:
                grid[querie[2] + 1][querie[3] + 1] += 1
                grid[querie[0]][querie[3] + 1] -= 1
                grid[querie[2] + 1][querie[1]] -= 1
            elif querie[2] < n - 1:
                grid[querie[2] + 1][querie[1]] -= 1
            elif querie[3] < n - 1:
                grid[querie[0]][querie[3] + 1] -= 1                
                
              
        box = [[0]*n for _ in range(n)]
        box[0][0] = grid[0][0]
        
        # Filling first row
        # and first column
        for i in range(1, n) :
            box[0][i] = (box[0][i - 1] + grid[0][i])
            
        for i in range(1, n) :
            box[i][0] = (box[i - 1][0] + grid[i][0])

        # updating the values in
        # the cells as per the
        # general formula
        for i in range(1, n) :
            for j in range(1, n) :

                # values in the cells of
                # new array are updated
                box[i][j] = (box[i - 1][j] + box[i][j - 1] - box[i - 1][j - 1] + grid[i][j])
   
        return box
            