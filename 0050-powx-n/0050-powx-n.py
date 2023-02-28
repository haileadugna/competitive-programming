class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1
        if x == 0 :
            return 0
        
        mult = self.myPow(x, abs(n)//2)
        mult =  mult * mult
        
        if n % 2 == 1:
            res = mult * x
        else:
            res = mult
            
        if n>=0:
            return res  
        else: 
            return 1/res

        