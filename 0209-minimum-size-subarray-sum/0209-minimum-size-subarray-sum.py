class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans =  len(nums)
        end = 0
        tmpsum = 0
        for i in range(len(nums)):
            tmpsum += nums[i]
            while tmpsum >= target:
                ans = min(i - end + 1, ans)
                tmpsum -= nums[end]
                end += 1
        if sum(nums) < target:
            return 0
        return ans

        