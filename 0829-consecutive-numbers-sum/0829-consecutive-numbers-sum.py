class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        
        
        i=1
        res=0
        k=int((n*2)**0.5)
        while i<=k:
            if i%2:
                if n%i==0:
                    res+=1
            elif (n-(i//2))%i==0:
                res+=1
            i+=1
        return res