class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])
        res = []
        currow = 0
        curcol = 0
        upgoing = True
        while len(res) != row*col:
            if upgoing:
                while currow >= 0 and curcol < col:
                    res.append(mat[currow][curcol])
                    currow -= 1
                    curcol += 1
                if curcol == col:
                    curcol -= 1
                    currow += 2
                else:
                    currow += 1
                upgoing = False
            else:
                while curcol >= 0 and currow < row:
                    res.append(mat[currow][curcol])
                    currow += 1
                    curcol -= 1
                if currow == row:
                    currow -= 1
                    curcol += 2
                else:
                    curcol += 1
                upgoing = True
        return res