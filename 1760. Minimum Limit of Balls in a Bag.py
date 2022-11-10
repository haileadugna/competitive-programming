class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def helper(mid):
            count = 0
            for num in nums:
                count += (num-1)//mid
            return count <= maxOperations
        l, r = 1, max(nums)
        while l < r:
            mid = l + (r-l)//2
            if helper(mid):
                r = mid
            else:
                l = mid +1
        return l