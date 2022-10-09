class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')
        for i in range(0, len(nums)-2):
            newnums = target - nums[i]
            l = i + 1
            r =  len(nums) -1
            while l < r:

                summ = nums[l] + nums[r]
                if summ == newnums:
                    return target
                if abs(ans) > abs(newnums - summ):
                    ans = newnums - summ
                if summ < newnums:
                    l += 1
                else:
                    r -= 1
        return target - ans
            
            
            
