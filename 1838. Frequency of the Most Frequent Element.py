class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0,0
        ans = 0
        check = 0
        while r < len(nums):
            check += nums[r]
            # print(check)
            while nums[r] * (r-l+1) > check + k:
                check -= nums[l]
                l += 1
                print(check)
            ans = max(ans, r-l+1)
            r += 1
        return ans
                
        # print(len(nums))
        # temp = [0]
        # for i in range(1, len(nums)):
        #     temp.append(nums[i-1] - nums[i])
        # for j in range(1,len(temp)):
        #     temp[j] += temp[j -1]
        # ans = 0
        # l, r= 0, 0
        # check = 0
        # while l <= r and r < len(temp) :
        
        # # while k > 0 and r < len(temp):
        #     if k - temp[r] >= 0 :
        #         k -= temp[r]
        #         check += 1
        #         r += 1
        #         ans = max(ans, check)
        #     else:
        #         if l < r:
        #             k += temp[l]
        #             check -= 1
        #             l += 1
        #         else:
        #             check += 1
        #             r += 1
        #     ans = max(ans, check)
        #     # else:
        #     #     k += temp[l]
        #     #     check -= 1
        #     #     l += 1
        # return ans
        # print(temp)
