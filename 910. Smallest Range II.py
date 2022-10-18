class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        ans = max(nums) - min(nums)
        nums.sort()
        ma=max(nums)
        mi= min(nums)
        for i in range(len(nums)-1):
            curmax = max(ma-k, nums[i]+k)
            curmin = min(mi +k, nums[i+1] -k)
            ans = min(ans, (curmax - curmin))
        return ans