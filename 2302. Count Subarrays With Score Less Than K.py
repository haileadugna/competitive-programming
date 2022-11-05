class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        tot = 0
        ans = 0
        l = 0
        for r in range(n):
            tot += nums[r]
            while tot * (r-l+1) >= k:
                tot -= nums[l]
                l += 1
            ans += (r-l+1)
            print(ans)
        return ans

        # temp = []
        # for i in range(1, len(nums)):
        #     nums[i] += nums[i-1]
        # l, r = 0, 0
        # ans = 0
        # while r < len(nums):
        #     if nums[r] * (r-l+1) < k:
        #         ans += 1
        #         r += 1
        #     else:
                    
        #         while l < r:
        #             if nums[r] * (r-l+1) < k:
        #                 ans += 1
        #             l += 1
        #             nums[r] -= nums[l]
                    
        # return ans