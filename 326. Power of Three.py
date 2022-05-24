class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==0:
            return False
        def check(n):
            if n==1 or n/3==1:
                return True
            elif n%3==0:
                return check(n/3)
            else:
                return False
        return check(n)    
        
        