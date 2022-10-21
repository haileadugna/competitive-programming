class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        
        # ans = 0
        # for i in range(len(nums)):
        #     l = i+1
        #     temp = nums[i]
        #     if temp < k:
        #         ans +=1
        #     while l < len(nums):
        #         if temp * nums[l] < k:
        #             temp *= nums[l]
        #             ans += 1
        #             l += 1
        #         else:
        #             break            
        # return ans
        s = 0
        ans = 0
        temp = 1
        for i in range(len(nums)):
            temp *= nums[i]
            if temp >= k:
                while temp >= k and s <= i:
                    temp //= nums[s]
                    s += 1
            ans += i - s + 1

        return ans

















