class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        a,b,c = -1,-2,-3
        while len(nums) + c >= 0:
            if nums[a] < nums[b] + nums[c] and nums[b] < nums[a] + nums[c] and nums[c] < nums[b] + nums[a]:
                ans = nums[a] + nums[b] + nums[c]
                return ans
            else:
                a -= 1
                b -= 1
                c -= 1
        return 0
        
