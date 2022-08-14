# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        end = n
        start = 0
        while start <= end:
            mid = (end + start)//2
            if isBadVersion(mid):
                result = mid
                end = mid -1
            else:
                
                start = mid + 1
        else:
            return result