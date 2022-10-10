class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        l, r= 1, 1000000000
        if len(dist) -1 > hour:
            return -1
        while l <= r:
            mid = (l + r)//2
            temp = 0
            for i in range(len(dist)):
                if i == len(dist) - 1:
                    temp += dist[i]/mid
                else:
                    temp += math.ceil(dist[i]/mid)
            if temp == hour:
                return int(mid)
            elif temp < hour:
                r = mid -1
            else:
                l = mid + 1
        if int(l) > 10 **9:
            return -1
        return int(l)
