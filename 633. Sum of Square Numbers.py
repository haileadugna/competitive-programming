class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        s, e = 0, int(c**0.5)
        while s <= e :
            
            if s**2 + e**2 == c:
                return True
            elif s**2 + e**2 > c:
                e -=1
            else:
                s += 1 
        return False