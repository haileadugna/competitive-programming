class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) -1
        temp = copy.deepcopy(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] =  temp[n-j][i]
        return matrix