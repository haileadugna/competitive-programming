class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort()
        prev = points[0]
        ans = 1
        for start, end in points[1:]:
            if start > prev[1]:
                ans += 1
                prev = [start, end]
            else:
                prev[1] = min(prev[1], end)
        return ans
                