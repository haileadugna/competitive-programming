class Solution:
    def hammingWeight(self, n: int) -> int:
        nums=bin(n)
        ans =nums.count(str(1))
        return ans