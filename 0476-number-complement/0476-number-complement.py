class Solution:
    def findComplement(self, num: int) -> int:
        
        # print(math.ceil(math.log2(6)))
        n = math.ceil(math.log2(num))
        res = 0
        for j in range(n):
            res += 2 ** j
            
        for i in range(n ):

            if (num >> i ) & 1 == 1:
                res -= 2**i

        return res