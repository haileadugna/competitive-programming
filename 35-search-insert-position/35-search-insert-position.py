class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        ind = bisect.bisect_left(nums, target)
        return ind