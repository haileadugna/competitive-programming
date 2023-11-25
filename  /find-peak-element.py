class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        temp = {}
        for j in range(len(nums)):
            temp[nums[j]] = j

        ans = max(nums)
        return temp[ans]