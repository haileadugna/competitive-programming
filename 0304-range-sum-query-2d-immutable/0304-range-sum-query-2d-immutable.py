class NumMatrix:
        
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        n, m = len(self.matrix), len(self.matrix[0])

        self.box = [[0 for _ in range(m)] for _ in range(n)]
        self.box[0][0] = self.matrix[0][0]
        
        
        # Filling first row
        # and first column
        for i in range(1, m) :
            self.box[0][i] = (self.box[0][i - 1] + self.matrix[0][i])
            
        for i in range(1, n) :
            self.box[i][0] = (self.box[i - 1][0] + self.matrix[i][0])

        # updating the values in
        # the cells as per the
        # general formula
        for i in range(1, n) :
            for j in range(1, m) :

                # values in the cells of
                # new array are updated
                self.box[i][j] = (self.box[i - 1][j] + self.box[i][j - 1] - self.box[i - 1][j - 1] +self.matrix[i][j])
# `        print(self.box)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        if row1 == 0 and col1 == 0:
            return self.box[row2][col2]
        elif row1 == 0:
            return self.box[row2][col2] - self.box[row2][col1-1]
        elif col1 == 0:
            return self.box[row2][col2] - self.box[row1-1][col2] 
        
        return self.box[row2][col2] - self.box[row1-1][col2] - self.box[row2][col1-1] + self.box[row1-1][col1-1]
    
    """
    [[3, 3, 4, 8, 10], 
     [8, 14, 18, 24, 27],
     [9, 17, 21, 28, 36],
     [13, 22, 26, 34, 49],
     [14, 23, 30, 38, 58]]
Sum(ABCD)=Sum(OD)−Sum(OB)−Sum(OC)+Sum(OA)
    """


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)