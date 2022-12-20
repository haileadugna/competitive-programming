class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        temp = 10000000
        ans = 0
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                des = abs(x - points[i][0]) + abs(y- points[i][1])
                if des < temp:
                    temp = des
                    ans = i
        if temp == 10000000:
            return -1
        return ans
                