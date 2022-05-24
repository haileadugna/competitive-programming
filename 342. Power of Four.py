class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==0:
            return False
        def check(n):
            if n==1 or n/4==1:
                return True
            elif n%4==0:
                return check(n/4)
            else:
                return False
        return check(n) 