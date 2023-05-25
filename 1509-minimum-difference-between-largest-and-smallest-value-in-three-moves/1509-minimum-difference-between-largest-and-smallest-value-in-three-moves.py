class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        nums.sort()
        if len(nums) < 5:
            return 0
        ans1 = nums[-4] - nums[0]
        ans2 = nums[-1] - nums[3]
        ans3 = nums[-2] - nums[2]
        ans4 = nums[-3] - nums[1]
        return min(ans1, ans2, ans3, ans4)