
class Solution:

    def findMaximumXOR(self, nums: List[int]) -> int:
        bit = 0
        xor_num = 0
        for i in range(31, -1, -1):
            bit = bit | (1 << i)

            found = set([])
            for n in nums:
                found.add(n & bit)
                
            temp = xor_num | 1 << i
            for f in found:
                if f^temp in found:
                    xor_num = temp
                    
        return xor_num