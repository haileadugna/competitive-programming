class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        N= len(triangle)
        cur_row,next_row = triangle[N-2], triangle[N-1]

        for r in range(N-2,-1,-1):
            for c in range(r+1):
                cur_row[c] += min(next_row[c] , next_row[c+1])

            next_row = cur_row
            cur_row = triangle[r-1]
        return next_row[0]