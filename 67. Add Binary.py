class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        ans = a + b
        ans = bin(ans)
        return ans[2:]