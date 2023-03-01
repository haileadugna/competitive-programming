class Solution:
    
    def findKthBit(self, n: int, k: int) -> str:
        
        def invert(s):
            s = list(s)
            for i in range(len(s)):
                if s[i] == "1":
                    s[i] = "0"
                else:
                    s[i] = "1"
                    
            s.reverse()
            return "".join(s)
        
        @cache
        def findKthBit(n):
            if n == 1 :
                return "0"
            else:
                temp =  findKthBit(n-1) + '1' + invert(findKthBit(n-1))
                return temp
    
        res = findKthBit(n)
        return res[k-1]

        
        