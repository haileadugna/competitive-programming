class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num = Counter(nums)
        for i in nums:
            if num[i] >= 2:
                return True
        return False