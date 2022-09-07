class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for i in nums:
            if i >  0:
                temp = 1
            elif i < 0:
                temp = -1
            else:
                temp = 0
            ans *= temp
        return ans