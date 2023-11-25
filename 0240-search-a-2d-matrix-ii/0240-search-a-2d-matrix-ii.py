class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m= len(matrix), len(matrix[0])
        l, r = 0, n-1
        while r >= 0 and l <m:
            if matrix[r][l] == target:
                return True
            if matrix[r][l] < target:
                l += 1
            else:
                r -= 1
        return False