class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        temp = Counter(nums)
        for i in range(len(nums) +1):
            if i not in temp:
                return i
        