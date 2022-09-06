class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        temp = 10**10
        ans = -1
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                distance = abs(x - points[i][0]) + abs(y - points[i][1])
                if distance < temp:
                    ans = i
                    temp = distance
        return ans   