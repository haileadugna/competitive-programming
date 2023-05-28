class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        @cache
        def getMaximum(n):
        
            if n <= 0:
                return 0
            if n == 1:
                return 1

            if n % 2 == 0:
                return getMaximum(n//2)
            return getMaximum(n//2) + getMaximum(n//2 + 1)
        
        res = 0
        for i in range(n//2, n+1):
            res = max(getMaximum(i), res)
            
        return res