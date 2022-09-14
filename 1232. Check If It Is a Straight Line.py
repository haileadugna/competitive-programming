class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        ans = coordinates[:]
        if len(ans) == 2:
            return True
        xo = ans[0][0]
        yo = ans[0][1]
        x1 = ans[1][0]
        y1 = ans[1][1]
        for x, y in ans:
            if (y1 - yo) * (x - xo) != (x1 - xo) * (y - yo):
                return False
        return True