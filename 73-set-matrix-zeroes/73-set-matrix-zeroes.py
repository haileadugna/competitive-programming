class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        temp = [] # to know where are the zeros
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    temp.append([row, col])
        for index in temp:
            horizontal = index[0]
            vertical = index[1]
            #make the horizontal row 0
            start1 = 0
            while start1 < rows:
                matrix[start1][vertical] = 0
                start1 += 1
            #make the verticals 0
            start2 = 0
            while start2 < cols:
                matrix[horizontal][start2] = 0
                start2 += 1
        