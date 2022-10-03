class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            temp = (n >> i) & 1
            ans = ans | (temp << (31 - i))
        return ans