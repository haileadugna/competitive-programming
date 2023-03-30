class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        prev = ( (n >> 0) & 1 )
        for i in range(1, math.ceil(math.log2(n))):
    
            if prev != ( (n >> i) & 1 ):
                prev = ( (n >> i) & 1 )

            else:
                return False
        return True
