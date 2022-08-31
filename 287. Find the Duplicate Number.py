class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s , f = 0, 0
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break
        s1 = 0
        while True:
            s = nums[s]
            s1 = nums[s1]
            if s == s1:
                return s