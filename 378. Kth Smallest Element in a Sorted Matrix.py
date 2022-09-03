class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums = []
        for i in matrix:
            nums.extend(i)
        nums.sort()
        return nums[k-1]